"""Ganze Guides von help.sap.com seitenweise abrufen (für Produkte ohne GitHub-Spiegel, z. B. BW/4HANA).

Konfiguration: config/sources.yaml, Abschnitt help_guides. Es reicht die URL irgendeiner Seite des Guides:
  https://help.sap.com/docs/<produkt>/<guide-id>/<seite>.html
Die Guide-ID bleibt stabil; die interne Nummer (deliverable_id) und die Veröffentlichungsnummer
(buildNo) holt der Job bei jedem Lauf neu über http.svc/deliverableMetadata.

Ablauf je Guide:
  1. deliverableMetadata -> deliverable_id, buildNo
  2. buildNo unverändert seit letztem Lauf -> Guide überspringen (SAP hat nichts neu veröffentlicht)
  3. pagecontent (deliverableInfo=1) -> Inhaltsverzeichnis (fullToc)
  4. jede Seite einzeln abrufen -> guides/<id>/<seiten-id>.md, Seiten, die nicht mehr im
     Inhaltsverzeichnis stehen, werden entfernt. Änderungen zeigt die Git-History.
  5. guides/<id>/README.md = Inhaltsverzeichnis mit Links
"""
import html, json, re, sys, time
from datetime import date
from pathlib import Path
from urllib.parse import urlencode, urlparse

import yaml
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "guides"
STATE = ROOT / "state" / "guides.json"
WARN = ROOT / "state" / "warnings_guides.md"
SVC = "https://help.sap.com/http.svc"
PAUSE = 0.3          # Sekunden zwischen Seitenabrufen (schonend für help.sap.com)
LANG = "en-US"
FORMAT = "2"         # erhöhen, wenn sich die Umwandlung ändert -> alle Guides einmal neu abrufen


def parse_url(url: str) -> dict:
    """help.sap.com-URL in Produkt, Guide-ID und Seite zerlegen."""
    parts = urlparse(url).path.strip("/").split("/")   # docs/<product>/<loio>/<topic>.html
    if len(parts) < 4 or parts[0] != "docs":
        raise ValueError(f"URL nicht im Format help.sap.com/docs/<produkt>/<guide>/<seite>.html: {url}")
    return {"product_url": parts[1], "deliverable_url": parts[2], "topic_url": parts[3]}


def get_json(req, endpoint: str, params: dict) -> dict:
    """GET-Anfrage an http.svc/<endpoint> der Hilfe; liefert den Inhalt von 'data' oder bricht mit Fehlermeldung ab."""
    resp = req.get(f"{SVC}/{endpoint}?{urlencode(params)}", timeout=60000)
    if not resp.ok:
        raise RuntimeError(f"{endpoint}: HTTP {resp.status}")
    payload = resp.json()
    if payload.get("status") != "OK":
        raise RuntimeError(f"{endpoint}: Status {payload.get('status')}")
    return payload.get("data") or {}


def flatten(nodes: list, path: tuple = ()) -> list[dict]:
    """Inhaltsverzeichnis (Baum) in eine flache Liste aller Seiten mit Titel, Datei und übergeordnetem Pfad umwandeln."""
    out = []
    for n in nodes or []:
        if n.get("u"):
            out.append({"u": n["u"], "t": (n.get("t") or "").strip(), "path": path, "id": n.get("id")})
        out += flatten(n.get("c") or [], path + ((n.get("t") or "").strip(),))
    return out


SEEN_IMG = []   # erste Bildpfade je Lauf, zur Kontrolle im Log


def _img(tag: str, base: str) -> str:
    """Bild-Tag in einen Markdown-Bildlink umwandeln; relative Pfade werden auf help.sap.com ergänzt."""
    src = re.search(r'src="([^"]+)"', tag)
    if not src or "sap_link.png" in src.group(1):          # Symbol "externer Link" weglassen
        return ""
    alt = re.search(r'alt="([^"]*)"', tag)
    url = html.unescape(src.group(1))
    if len(SEEN_IMG) < 3:
        SEEN_IMG.append(url)
    if url.startswith("//"):
        url = "https:" + url
    elif url.startswith("/"):
        url = "https://help.sap.com" + url
    elif not url.startswith("http"):
        url = base + url
    return f"\n![{(alt.group(1) if alt else '').strip() or 'Bild'}]({url})\n"


def body_to_md(s: str, img_base: str = "https://help.sap.com/") -> str:
    """HTML einer Hilfeseite in lesbares Markdown (Überschriften, Listen, Links, Tabellen, Code, Bilder als Link)."""
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", s, flags=re.S | re.I)
    s = re.sub(r"<img[^>]*>", lambda m: _img(m.group(0), img_base), s, flags=re.I)
    s = re.sub(r"<pre[^>]*>(.*?)</pre>", lambda m: "\n```\n" + re.sub("<[^>]+>", "", m.group(1)) + "\n```\n", s, flags=re.S)
    s = re.sub(r"<h([1-6])[^>]*>(.*?)</h\1>",
               lambda m: "\n" + "#" * (int(m.group(1)) + 1) + " " + re.sub("<[^>]+>", "", m.group(2)).strip() + "\n",
               s, flags=re.S)
    s = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>',
               lambda m: f"[{re.sub('<[^>]+>', '', m.group(2)).strip()}]({_abs(m.group(1))})", s, flags=re.S)
    s = re.sub(r"</t[hd]>\s*", " | ", s)
    s = re.sub(r"<tr[^>]*>", "\n| ", s)
    s = re.sub(r"<li[^>]*>", "\n- ", s)
    s = re.sub(r"</(p|div|ul|ol|li|table|tr|section|dl|dt|dd)>|<br\s*/?>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    out, in_code = [], False
    for raw in s.splitlines():
        if raw.strip().startswith("```"):
            in_code = not in_code
            out.append("```")
            continue
        out.append(raw.rstrip() if in_code else re.sub(r"[ \t]+", " ", raw).strip())
    # Leerzeilen zwischen Listenpunkten und Tabellenzeilen entfernen, Tabellenkopf markieren
    tidy = []
    for line in out:
        if line == "" and tidy and tidy[-1][:2] in ("- ", "| "):
            tidy.append("")            # vorläufig, wird entfernt, wenn dieselbe Art folgt
            continue
        if tidy and tidy[-1] == "" and len(tidy) > 1 and line[:2] in ("- ", "| ") and tidy[-2][:2] == line[:2]:
            tidy.pop()
        if line.startswith("| ") and (not tidy or not tidy[-1].startswith("|")):
            tidy.append(line.rstrip())
            tidy.append("|" + " --- |" * max(1, line.rstrip().count("|") - 1))
            continue
        tidy.append(line)
    md = "\n".join(tidy)
    return re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"


def _abs(url: str) -> str:
    """Link vollständig machen: relative help.sap.com-Pfade ergänzen, Umleitungen über link-disclaimer auflösen."""
    url = html.unescape(url)
    m = re.search(r"link-disclaimer\?site=([^&]+)", url)
    if m:
        from urllib.parse import unquote
        return unquote(m.group(1))
    return "https://help.sap.com" + url if url.startswith("/") else url


def slug(text: str) -> str:
    """Dateinamen-tauglichen Kurztext aus einem Seitentitel bilden."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60] or "seite"


def fetch_guide(req, g: dict, state: dict) -> str:
    """Einen Guide abrufen: Metadaten, bei neuer buildNo Inhaltsverzeichnis und alle Seiten; gelöschte Seiten entfernen."""
    u = parse_url(g["url"])
    meta = get_json(req, "deliverableMetadata", {
        "product_url": u["product_url"], "topic_url": u["topic_url"], "version": "LATEST",
        "loadlandingpageontopicnotfound": "true", "deliverable_url": u["deliverable_url"], "language": LANG})
    d = meta.get("deliverable") or {}
    did, build = d.get("id"), d.get("buildNo")
    if not did:
        raise RuntimeError("deliverableMetadata ohne deliverable.id – Guide verschoben?")
    old = state.get(g["id"], {})
    if (old.get("buildNo") == build and old.get("deliverable_id") == did and old.get("format") == FORMAT
            and (OUT / g["id"]).exists()):
        return f"unverändert (buildNo {build})"

    first = get_json(req, "pagecontent", {"deliverableInfo": 1, "deliverable_id": did, "buildNo": build,
                                          "file_path": meta.get("filePath") or u["topic_url"]})
    toc = flatten((first.get("deliverable") or {}).get("fullToc") or [])
    if not toc:
        raise RuntimeError("Inhaltsverzeichnis leer")
    target = OUT / g["id"]
    target.mkdir(parents=True, exist_ok=True)
    wanted, errors = set(), 0
    for i, page in enumerate(toc):
        try:
            data = first if page["u"] == (meta.get("filePath") or u["topic_url"]) else \
                get_json(req, "pagecontent", {"deliverableInfo": 0, "deliverable_id": did,
                                              "buildNo": build, "file_path": page["u"]})
        except Exception as e:
            errors += 1
            print(f"  {page['u']}: {e}")
            continue
        name = f"{slug(page['t'])}-{page['u'].removesuffix('.html')[:7]}.md"
        wanted.add(name)
        link = f"https://help.sap.com/docs/{u['product_url']}/{u['deliverable_url']}/{page['u']}?locale={LANG}"
        head = (f"---\nguide: {g['title']}\nproduct: {g['product']}\ntitle: \"{page['t']}\"\n"
                f"page: {page['u']}\nurl: {link}\nsource_type: SAP Help\n---\n\n"
                f"# {page['t']}\n\n*{' › '.join(page['path']) or g['title']} · [auf help.sap.com öffnen]({link})*\n\n")
        img_base = f"https://help.sap.com/doc/{u['deliverable_url']}/{d.get('versionName') or 'latest'}/{LANG}/"
        (target / name).write_text(head + body_to_md(data.get("body") or "", img_base), encoding="utf-8")
        time.sleep(PAUSE)
        if (i + 1) % 100 == 0:
            print(f"  {i + 1}/{len(toc)} Seiten")
    if errors > len(toc) * 0.2:
        raise RuntimeError(f"{errors} von {len(toc)} Seiten nicht abrufbar – Stand nicht übernommen")
    for f in target.glob("*.md"):
        if f.name not in wanted and f.name != "README.md":
            f.unlink()
    index = [f"# {g['title']} ({g['product']})", "",
             f"Quelle: {g['url']} · {len(toc)} Seiten · buildNo {build} · Stand {date.today().isoformat()}", ""]
    for page in toc:
        name = f"{slug(page['t'])}-{page['u'].removesuffix('.html')[:7]}.md"
        index.append(f"{'  ' * len(page['path'])}- [{page['t']}]({name})")
    (target / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    state[g["id"]] = {"deliverable_id": did, "buildNo": build, "pages": len(toc), "format": FORMAT,
                      "checked": date.today().isoformat()}
    return (f"{len(toc)} Seiten gelesen (buildNo {old.get('buildNo')} → {build}), {errors} Fehler; "
            f"Beispiel-Bildpfade: {SEEN_IMG}")


def main() -> int:
    """Alle help_guides und mirror_checks aus config/sources.yaml abarbeiten; Stand in state/guides.json, Warnungen in state/warnings_guides.md."""
    cfg = yaml.safe_load((ROOT / "config" / "sources.yaml").read_text(encoding="utf-8"))
    guides = [g for g in cfg.get("help_guides", []) if g.get("url")]
    checks = cfg.get("mirror_checks", []) or []
    STATE.parent.mkdir(parents=True, exist_ok=True)
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    warnings = []
    if not guides and not checks:
        print("Keine help_guides konfiguriert")
    else:
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            ctx = browser.new_context(locale=LANG)
            page = ctx.new_page()
            try:   # einmal die Hilfe öffnen, damit die Sitzung wie im Browser besteht
                page.goto((guides or checks)[0]["url"], wait_until="domcontentloaded", timeout=90000)
                page.wait_for_timeout(3000)
            except Exception:
                pass
            for g in guides:
                try:
                    print(f"{g['id']}: {fetch_guide(ctx.request, g, state)}")
                except Exception as e:
                    warnings.append(f"{g['id']}: {e} ({g['url']})")
                    print(f"{g['id']}: FEHLER {e}")
            for c in cfg.get("mirror_checks", []) or []:
                try:
                    import mirror_check
                    print(f"Abgleich {c['id']}: {mirror_check.run(ctx.request, c, state)}")
                except Exception as e:
                    warnings.append(f"Abgleich {c['id']}: {e}")
                    print(f"Abgleich {c['id']}: FEHLER {e}")
            browser.close()
    STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    WARN.write_text(f"# Warnungen Guides, Lauf {date.today().isoformat()}\n\n"
                    + ("\n".join(f"- {w}" for w in warnings) if warnings else "- keine") + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
