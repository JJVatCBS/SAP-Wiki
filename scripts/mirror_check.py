"""Abgleich: GitHub-Spiegel gegen die SAP-Hilfe (help.sap.com) für einen Guide.

Zuordnung über die SAP-Seiten-ID: GitHub-Dateien enden mit den ersten 7 Zeichen der ID
(z. B. ...-5a3419f.md), die Hilfe nutzt die volle ID als Dateiname (5a3419f....html).
Verglichen wird der reine Text (ohne Markdown-Zeichen, Links, Bilder, Leerraum).

Ergebnis: reports/mirror-check/<id>.md mit
  - Seiten nur in der Hilfe (fehlen auf GitHub)
  - Seiten nur auf GitHub
  - Ähnlichkeit je Seite in %, abweichende Seiten mit Beispielzeilen
Läuft nur, wenn der Guide seit dem letzten Abgleich neu veröffentlicht wurde (buildNo).
Übernimmt nichts in den Wiki-Bestand.
"""
import difflib, html, re, time
from datetime import date
from pathlib import Path

import fetch_help_guides as fg

ROOT = Path(__file__).resolve().parents[1]
MIRRORS = ROOT / ".cache" / "mirrors"
OUT = ROOT / "reports" / "mirror-check"


CHECK_FORMAT = "2"   # erhöhen, wenn sich der Vergleich ändert -> Abgleich läuft einmal neu

LABEL_WORDS = r"(note|caution|tip|restriction|example|remember|recommendation|important)"


def norm(text: str, title: str = "") -> list[str]:
    """Text für den Vergleich vereinheitlichen und in Sätze zerlegen.
    Entfernt alles, was sich zwischen GitHub-Markdown und Hilfe-HTML nur in der Form unterscheidet:
    Kopfdaten, Überschriften, Bilder, Link-Ziele und -Tooltips, Link-Symbole, Aufzählungs- und
    Schrittnummern, Tabellenzeichen, Hinweis-Etiketten (Note, Caution …), Leerzeichen vor Satzzeichen."""
    text = html.unescape(text)
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.S)              # Frontmatter
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)                  # HTML-Kommentare (loio-Kennung)
    text = re.sub(r"(?m)^\s*#.*$", "", text)                          # Überschriften (Titel steht in beiden)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)                    # Bilder
    text = re.sub(r'(\]\([^)\s]+)\s+"[^"]*"\)', r"\1)", text)            # Tooltip in Markdown-Links
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)                # Links -> Linktext
    text = re.sub(r":arrow[a-z_ ]*:", "", text)                         # GitHub-Symbol externer Link
    text = re.sub(r"</?[a-zA-Z][^>]*>", " ", text)                       # nur echte HTML-Tags, nicht "<="
    text = re.sub(r"\\([\\`*_{}\[\]()#+\-.!|>])", r"\1", text)           # Markdown-Escapes
    text = re.sub(r"(?m)^\s*(\d+\.|[-*+])\s+", "", text)                  # Schrittnummern, Aufzählungszeichen
    text = re.sub(r"(?m)^\s*\d+\.\s*$", "", text)                         # allein stehende Nummern "1."
    text = re.sub(r"\|?\s*-{3,}\s*\|?", " ", text)                         # Tabellen-Trennzeilen
    text = re.sub(r"(?mi)^\s*" + LABEL_WORDS + r"\b\s*:?", " ", text)    # Hinweis-Etikett am Zeilenanfang
    text = re.sub(r"(?i)\b" + LABEL_WORDS + r"\s*:", " ", text)            # "Note:" mitten im Text
    text = re.sub(r"[\ue000-\uf8ff]", "", text)                          # Symbolzeichen der SAP-Schrift
    text = re.sub(r"[#*_`|\[\]]", " ", text)
    text = re.sub(r"\(\s+", "(", text)
    text = re.sub(r"\s+([.,;:)!?])", r"\1", text)                       # Leerzeichen vor Satzzeichen
    words = re.sub(r"\s+", " ", text).strip().lower()
    t = re.sub(r"\s+", " ", title.lower()).strip()
    for _ in range(2):                                                  # Titel am Anfang (Hilfe: doppelt)
        if t and words.startswith(t):
            words = words[len(t):].lstrip(" -–")
    return [x for x in re.split(r"(?<=[.!?:])\s+", words) if x]


def run(req, c: dict, state: dict) -> str:
    """Einen Guide aus der Hilfe mit dem GitHub-Spiegel vergleichen und den Bericht reports/mirror-check/<id>.md schreiben."""
    u = fg.parse_url(c["url"])
    meta = fg.get_json(req, "deliverableMetadata", {
        "product_url": u["product_url"], "topic_url": u["topic_url"], "version": "LATEST",
        "loadlandingpageontopicnotfound": "true", "deliverable_url": u["deliverable_url"], "language": fg.LANG})
    d = meta.get("deliverable") or {}
    did, build = d.get("id"), d.get("buildNo")
    key = f"check:{c['id']}"
    if (state.get(key, {}).get("buildNo") == build and state.get(key, {}).get("format") == CHECK_FORMAT
            and (OUT / f"{c['id']}.md").exists()):
        return f"unverändert (buildNo {build}), kein neuer Abgleich"

    first = fg.get_json(req, "pagecontent", {"deliverableInfo": 1, "deliverable_id": did, "buildNo": build,
                                             "file_path": meta.get("filePath") or u["topic_url"]})
    toc = fg.flatten((first.get("deliverable") or {}).get("fullToc") or [])
    folder = MIRRORS / c["mirror"] / c.get("path", "docs")
    gh = {}
    for f in folder.rglob("*.md"):
        m = re.search(r"-([0-9a-f]{7})\.md$", f.name)
        if m:
            gh[m.group(1)] = f
    rows, only_help, matched = [], [], set()
    for page in toc:
        short = page["u"][:7]
        f = gh.get(short)
        if not f:
            only_help.append(page)
            continue
        matched.add(short)
        data = first if page["u"] == (meta.get("filePath") or u["topic_url"]) else fg.get_json(
            req, "pagecontent", {"deliverableInfo": 0, "deliverable_id": did, "buildNo": build, "file_path": page["u"]})
        a = norm(f.read_text(encoding="utf-8"), page["t"])
        b = norm(fg.body_to_md(data.get("body") or ""), page["t"])
        # Übereinstimmung wortweise (robust gegen andere Zeilen- und Satzgrenzen); Unterschiede satzweise anzeigen
        wa, wb = " ".join(a).split(), " ".join(b).split()
        ratio = difflib.SequenceMatcher(None, wa, wb, autojunk=False).ratio()
        diff = [l for l in difflib.unified_diff(a, b, lineterm="", n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---")]
        rows.append((ratio, page, f, diff))
        time.sleep(fg.PAUSE)
    only_gh = [f for k, f in gh.items() if k not in matched]

    ident = sum(1 for r in rows if r[0] >= 0.999)
    small = sum(1 for r in rows if 0.95 <= r[0] < 0.999)
    big = sum(1 for r in rows if r[0] < 0.95)
    md = [f"# Abgleich GitHub-Spiegel ↔ SAP-Hilfe: {c['title']}", "",
          f"Stand {date.today().isoformat()} · Hilfe: {c['url']} (buildNo {build}) · "
          f"Spiegel: {c['mirror']}/{c.get('path', 'docs')}", "",
          "| Kennzahl | Wert |", "|---|---|",
          f"| Seiten in der Hilfe | {len(toc)} |",
          f"| davon auf GitHub gefunden | {len(rows)} |",
          f"| – Text identisch | {ident} |",
          f"| – kleine Abweichung (95–99,9 %, z. B. einzelner Satz oder Zahl) | {small} |",
          f"| – deutliche Abweichung (< 95 %) | {big} |",
          f"| Seiten nur in der Hilfe | {len(only_help)} |",
          f"| Seiten nur auf GitHub (in diesem Ordner) | {len(only_gh)} |", "",
          "Hinweise: Übereinstimmung = Anteil gleicher Wörter in gleicher Reihenfolge; Formatierung, Links und Bilder zählen nicht. "
          "„Nur auf GitHub“ kann auch heißen, dass die Seite in der Hilfe zu einem anderen Guide gehört.", ""]
    if only_help:
        md += ["## Nur in der Hilfe", ""] + [f"- {p['t']} (`{p['u']}`)" for p in only_help] + [""]
    if only_gh:
        md += ["## Nur auf GitHub", ""] + [f"- `{f.relative_to(MIRRORS)}`" for f in sorted(only_gh)[:200]] + [""]
    diffs = sorted((r for r in rows if r[0] < 0.999), key=lambda r: r[0])
    if diffs:
        md += ["## Seiten mit abweichendem Text", "", "| Übereinstimmung | Seite |", "|---|---|"]
        md += [f"| {r[0]:.0%} | {r[1]['t']} |" for r in diffs]
        md += [""]
        for ratio, page, f, diff in diffs[:30]:
            md += [f"### {page['t']} ({ratio:.0%})", "", "`-` GitHub · `+` Hilfe", "", "```diff",
                   *[l[:300] for l in diff[:12]], "```", ""]
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{c['id']}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    state[key] = {"buildNo": build, "format": CHECK_FORMAT, "checked": date.today().isoformat()}
    return (f"{len(toc)} Hilfeseiten, {len(rows)} auf GitHub gefunden: {ident} identisch, {small} kleine, "
            f"{big} deutliche Abweichung; "
            f"{len(only_help)} nur in der Hilfe, {len(only_gh)} nur auf GitHub")
