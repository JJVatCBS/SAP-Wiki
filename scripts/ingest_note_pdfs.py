"""Verarbeitet SAP-Note- und KBA-PDFs.

Normalfall: nur neue PDFs aus notes/inbox/.
  1. Nummer, Version, Titel, Freigabedatum, Komponente werden aus dem INHALT des PDFs gelesen,
     nie aus dem Dateinamen. Das PDF wird als notes/archive/<nummer>_v<version>.pdf abgelegt.
  2. notes/text/<nummer>.md enthält immer die neueste Version (frühere: History der Datei).
  3. Neue Note oder neue Version: Eintrag in notes/changelog.md mit Versionswechsel,
     Freigabedatum und den geänderten Abschnitten (welche Zeilen dazu- oder weggekommen sind).
  4. notes/log.csv: Übersicht aller Notes mit aktueller Version.

Wurde die Erkennung in diesem Skript verbessert (PARSER_VERSION erhöht), liest der nächste Lauf
einmalig das ganze Archiv neu – automatisch, ohne Eingabe.
"""
import csv, difflib, re, shutil, subprocess, sys
from datetime import date
from pathlib import Path

PARSER_VERSION = "3"
ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "notes" / "inbox"
TEXT = ROOT / "notes" / "text"
ARCHIVE = ROOT / "notes" / "archive"
LOG = ROOT / "notes" / "log.csv"
CHANGELOG = ROOT / "notes" / "changelog.md"
PARSER_STATE = ROOT / "state" / "notes_parser_version.txt"
FIELDS = ["nummer", "version", "titel", "freigabe", "komponente", "datei"]

# Abschnittsüberschriften in SAP Notes und KBAs
SECTIONS = ["Symptom", "Other Terms", "Reason and Prerequisites", "Cause", "Solution", "Environment",
            "Resolution", "Reproducing the Issue", "Keywords", "Attributes", "Products",
            "This document refers to", "This document is referenced by", "References",
            "Software Components", "Affected Releases", "Correction Instructions",
            "Support Packages & Patches", "Prerequisites", "See Also", "Related Content"]
SECTION_RE = re.compile(r"^(" + "|".join(re.escape(s) for s in SECTIONS) + r")\s*$")


def pdf_text(pdf: Path) -> str:
    """Text aus einem PDF lesen (pdftotext aus poppler-utils)."""
    return subprocess.run(["pdftotext", str(pdf), "-"], check=True, capture_output=True, text=True).stdout


def parse(text: str) -> dict:
    """Kopf einer Note: '<Nummer> - <Titel>' (Nummern haben 3 bis 8 Stellen, alte Notes sind kurz),
    darunter 'Component: …, Version: n, Released On: TT.MM.JJJJ'."""
    head = re.search(r"^\s*(\d{3,8})\s+-\s+(.+)$", text, re.M)
    ver = re.search(r"Version\s*:\s*(\d+)", text)
    rel = re.search(r"(?:Released\s*On|Release\s*Date)\s*:?\s*([0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}|[0-9-]{10})", text, re.I)
    comp = re.search(r"Component\s*:\s*([A-Z0-9][A-Z0-9_-]+(?:-[A-Z0-9_]+)*)", text)
    return {"nummer": head.group(1) if head else "",
            "titel": " ".join(head.group(2).split()) if head else "",
            "version": ver.group(1) if ver else "",
            "freigabe": rel.group(1) if rel else "",
            "komponente": comp.group(1) if comp else ""}


def to_markdown(text: str) -> str:
    """Note-Text lesbar machen: Abschnitte wie 'Symptom' oder 'Solution' als Überschrift, Aufzählungszeichen als Liste."""
    out = []
    for raw in text.replace("\f", "\n").splitlines():
        line = raw.strip()
        if SECTION_RE.match(line):
            out += ["", f"## {line}", ""]
        elif line[:1] in ("•", "▪", "") and len(line) > 1:
            out.append("- " + line[1:].strip())
        elif line[:1] in ("◦", "○") and len(line) > 1:
            out.append("  - " + line[1:].strip())
        else:
            out.append(line)
    md = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"


def read_front(md: Path) -> dict:
    """Kopfdaten (Frontmatter zwischen den ---) einer Note-Datei lesen."""
    meta, lines = {}, md.read_text(encoding="utf-8").split("---", 2)
    if len(lines) == 3:
        for l in lines[1].strip().splitlines():
            k, _, v = l.partition(":")
            meta[k.strip()] = v.strip().strip('"')
    return meta


def sections(md: str) -> dict:
    """Markdown einer Note in Abschnitte zerlegen (Kopf bis zur ersten Überschrift = 'Kopf')."""
    out, cur = {"Kopf": []}, "Kopf"
    for line in md.splitlines():
        if line.startswith("## "):
            cur = line[3:].strip()
            out.setdefault(cur, [])
        elif line.strip():
            out[cur].append(line.strip())
    return out


def body_of(md_file_text: str) -> str:
    """Notiztext ohne den von diesem Skript erzeugten Kopf (Frontmatter, Titelzeile, Infozeile)."""
    parts = md_file_text.split("---", 2)
    rest = parts[2] if len(parts) == 3 else md_file_text
    i = rest.find("\n## ")
    return rest[i:] if i >= 0 else rest


def diff_entry(num: str, old: dict, new: dict, old_body: str, new_body: str) -> list[str]:
    """Changelog-Eintrag für eine neue Version: Versionswechsel, Freigabedatum, je Abschnitt die dazu- und weggekommenen Zeilen."""
    today = date.today().isoformat()
    lines = [f"## {num} – {new['titel']}", "",
             f"*erfasst {today} · Version {old.get('version', '?')} → {new['version']} · "
             f"freigegeben {new['freigabe']} · [SAP for Me](https://me.sap.com/notes/{num})*", ""]
    if old.get("title") and old.get("title") != new["titel"]:
        lines += [f"Titel geändert: „{old['title']}“ → „{new['titel']}“", ""]
    a, b = sections(old_body), sections(new_body)
    changed = False
    for name in list(dict.fromkeys(list(a) + list(b))):
        if name == "Kopf":
            continue
        ol, nl = a.get(name, []), b.get(name, [])
        if ol == nl:
            continue
        changed = True
        plus = [l for l in difflib.ndiff(ol, nl) if l.startswith("+ ")]
        minus = [l for l in difflib.ndiff(ol, nl) if l.startswith("- ")]
        status = "neu" if not ol else "entfernt" if not nl else f"+{len(plus)} / −{len(minus)} Zeilen"
        lines += [f"**{name}** ({status})", "", "```diff"]
        shown = sorted(minus + plus, key=lambda l: 0 if re.search(r"\d", l) else 1)[:10]
        lines += [l[:300] for l in shown]
        if len(minus) + len(plus) > 10:
            lines.append(f"… {len(minus) + len(plus) - 10} weitere Zeilen, siehe History von notes/text/{num}.md")
        lines += ["```", ""]
    if not changed:
        lines += ["Inhalt der Abschnitte unverändert (nur Versionsnummer/Kopf geändert).", ""]
    return lines


def add_changelog(entries: list[list[str]]) -> None:
    """Neue Einträge oben in notes/changelog.md einfügen (neueste zuerst)."""
    if not entries:
        return
    head = ["# Änderungen an SAP Notes und KBAs", "",
            "Neueste zuerst. Grundlage sind die PDFs in notes/archive; erkannt wird nur, was hochgeladen wurde.", ""]
    old = CHANGELOG.read_text(encoding="utf-8").split("\n", len(head))[-1] if CHANGELOG.exists() else ""
    body = "\n".join(l for e in entries for l in e)
    CHANGELOG.write_text("\n".join(head) + "\n" + body + "\n" + old, encoding="utf-8")


def write_note(num: str, meta: dict, text: str) -> str:
    """notes/text/<nummer>.md mit Kopfdaten, Infozeile und Text schreiben; gibt den Text als Markdown zurück."""
    md = to_markdown(text)
    header = ("---\n"
              f"source_type: SAP Note/KBA\nnumber: {num}\nversion: {meta['version']}\n"
              f"title: \"{meta['titel']}\"\nrelease_date: {meta['freigabe']}\n"
              f"component: {meta['komponente']}\nfile: {meta['datei']}\n"
              f"url: https://me.sap.com/notes/{num}\n---\n\n"
              f"# {num} – {meta['titel']}\n\n"
              f"Version {meta['version']} · freigegeben {meta['freigabe']} · Komponente {meta['komponente']} · "
              f"[in SAP for Me öffnen](https://me.sap.com/notes/{num})\n\n")
    (TEXT / f"{num}.md").write_text(header + md, encoding="utf-8")
    return md


def archive(pdf: Path, meta: dict) -> str:
    """PDF als notes/archive/<nummer>_v<version>.pdf ablegen; liegt diese Version schon dort, wird die neue Datei verworfen."""
    name = f"{meta['nummer']}_v{meta['version'] or 'x'}.pdf"
    target = ARCHIVE / name
    if pdf.resolve() != target.resolve():
        if target.exists():
            pdf.unlink()                    # diese Version liegt schon im Archiv
        else:
            shutil.move(str(pdf), target)
    return name


def main() -> int:
    """Neue PDFs verarbeiten (nach Änderung der Erkennung einmalig auch das Archiv), Changelog und log.csv aktualisieren."""
    for d in (INBOX, TEXT, ARCHIVE, PARSER_STATE.parent):
        d.mkdir(parents=True, exist_ok=True)
    rescan = (PARSER_STATE.read_text().strip() if PARSER_STATE.exists() else "") != PARSER_VERSION
    todo = sorted(INBOX.glob("*.pdf")) + (sorted(ARCHIVE.glob("*.pdf")) if rescan else [])
    if rescan:
        print(f"Erkennung geändert (Version {PARSER_VERSION}): Archiv wird einmalig neu eingelesen")
    if not todo:
        print("Keine neuen PDFs")
        return 0

    parsed, problems = [], []
    for pdf in todo:
        text = pdf_text(pdf)
        meta = parse(text)
        if not meta["nummer"] or not meta["version"]:
            problems.append(pdf.name)
            print(f"{pdf.name}: Nummer oder Version nicht erkannt – bleibt liegen")
            continue
        meta["datei"] = archive(pdf, meta)
        parsed.append((meta, text, pdf.parent == INBOX))

    # je Note die höchste Version dieses Laufs
    best = {}
    for meta, text, new in parsed:
        cur = best.get(meta["nummer"])
        if cur is None or int(meta["version"]) > int(cur[0]["version"]):
            best[meta["nummer"]] = (meta, text, new)

    entries = []
    for num, (meta, text, _) in sorted(best.items()):
        f = TEXT / f"{num}.md"
        old_text = f.read_text(encoding="utf-8") if f.exists() else ""
        old = read_front(f) if f.exists() else {}
        old_ver = int(old.get("version") or 0)
        new_ver = int(meta["version"])
        if old and new_ver < old_ver:
            print(f"{num} v{new_ver}: älter als vorhandene v{old_ver} – nur archiviert")
            continue
        new_md = write_note(num, meta, text)
        if not old:
            if not rescan or not any(e.startswith(f"## {num} ") for e in
                                     (CHANGELOG.read_text(encoding='utf-8').splitlines() if CHANGELOG.exists() else [])):
                entries.append([f"## {num} – {meta['titel']}", "",
                                f"*erfasst {date.today().isoformat()} · neu im Archiv · Version {new_ver} · "
                                f"freigegeben {meta['freigabe']} · [SAP for Me](https://me.sap.com/notes/{num})*", ""])
            print(f"{num} v{new_ver} ({meta['freigabe']}): {meta['titel']} – neu")
        elif new_ver > old_ver:
            entries.append(diff_entry(num, old, meta, body_of(old_text), new_md))
            print(f"{num}: v{old_ver} → v{new_ver} ({meta['freigabe']}) – Änderungen protokolliert")
        else:
            print(f"{num} v{new_ver}: unverändert")
    add_changelog(entries)

    if rescan:   # Texte zu Notes, die es im Archiv nicht mehr gibt (z. B. falsch erkannte Nummer), entfernen
        known = {m["nummer"] for m, _, _ in parsed}
        for md in TEXT.glob("*.md"):
            if md.stem not in known:
                md.unlink()
        PARSER_STATE.write_text(PARSER_VERSION + "\n")

    with LOG.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        for md in sorted(TEXT.glob("*.md")):
            f = read_front(md)
            w.writerow({"nummer": f.get("number", ""), "version": f.get("version", ""),
                        "titel": f.get("title", ""), "freigabe": f.get("release_date", ""),
                        "komponente": f.get("component", ""), "datei": f.get("file", "")})
    if problems:
        print(f"Nicht erkannt: {', '.join(problems)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
