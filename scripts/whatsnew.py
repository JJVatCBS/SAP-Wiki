"""Zerlegt den Text einer What's-New-Seite von help.sap.com in einzelne Einträge und pflegt einen
dauerhaften Bestand je Produkt.

Aufbau einer Seite (Stand 11/2026):
  Oct 20, 2026                                    <- Datumsüberschrift
  Administration - Assign More Than 100 Spaces    <- Bereich - Titel
  There is no longer any limit ...                <- Beschreibung (mehrere Zeilen, inkl. "See ...")
  Info only                                       <- Kennzeichen
  2026.22                                         <- Version = Ende des Eintrags

Bestand: data/whatsnew/<id>.json. Einträge, die aus dem 6-Monats-Fenster der Seite fallen,
bleiben erhalten. Ändert SAP den Text eines Eintrags, wird er überschrieben; der alte Text
steht in der Git-Historie.
"""
import json, re
from datetime import date, datetime
from pathlib import Path

DATE_RE = re.compile(r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}, \d{4}$")
VERSION_RE = re.compile(r"^\d{4}\.\d{1,2}$|^Q[1-4] \d{4}$|^\d{4} (FPS|SP)\d+$")
HEAD_RE = re.compile(r"^([A-Z][^\n]{1,60}?) - (.{3,})$")
NOISE = ("Page size", "Showing ", "Was this What's New helpful", "What's New Archive")


TAG_WORDS = re.compile(r"\b(only|required|action|optional|recommended|deprecated|deleted|changed|"
                       r"available|availability|beta|preview|new|announcement|planned)\b", re.I)


def is_tag(line: str) -> bool:
    """Kennzeichen wie 'Info only' oder 'Customer action required' - keine Linktitel."""
    return len(line.split()) <= 4 and not line.endswith((".", ":")) and bool(TAG_WORDS.search(line))


def parse(lines: list[str]) -> list[dict]:
    entries, cur, day = [], None, None
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith(NOISE):
            continue
        if DATE_RE.match(line):
            day = datetime.strptime(re.sub(r"^(\w{3})\w*", r"\1", line), "%b %d, %Y").date().isoformat()
            continue
        if day is None:
            continue                       # Kopfbereich der Seite
        if cur is None:
            m = HEAD_RE.match(line)
            if m:
                cur = {"date": day, "area": m.group(1).strip(), "title": m.group(2).strip(), "body": []}
            continue
        if VERSION_RE.match(line):
            body = cur.pop("body")
            tags = []
            while body and is_tag(body[-1]):
                tags.insert(0, body.pop())
            cur.update(version=line, tags=tags, text="\n".join(body))
            entries.append(cur)
            cur = None
            continue
        cur["body"].append(line)
    return entries


def key(e: dict) -> str:
    return f"{e['date']}|{e['area']}|{e['title']}"


def merge(store_path: Path, entries: list[dict]) -> dict:
    store = json.loads(store_path.read_text(encoding="utf-8")) if store_path.exists() else {}
    today = date.today().isoformat()
    stats = {"neu": 0, "geändert": 0}
    for e in entries:
        k = key(e)
        old = store.get(k)
        if old is None:
            store[k] = {**e, "first_seen": today, "last_seen": today, "changed": ""}
            stats["neu"] += 1
        else:
            if (old["text"], old["tags"], old["version"]) != (e["text"], e["tags"], e["version"]):
                old.update(text=e["text"], tags=e["tags"], version=e["version"], changed=today)
                stats["geändert"] += 1
            old["last_seen"] = today
    store_path.parent.mkdir(parents=True, exist_ok=True)
    store_path.write_text(json.dumps(store, indent=1, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    return {**stats, "gesamt": len(store), "store": store}


def render(p: dict, store: dict) -> str:
    items = sorted(store.values(), key=lambda e: (e["date"], e["area"], e["title"]), reverse=True)
    md = [f"# What's New – {p['product']}", "",
          f"Quelle: [{p['url']}]({p['url']}) · {len(items)} Einträge · Stand {date.today().isoformat()}", "",
          "„Erstmals gesehen“ = erster Lauf, in dem der Eintrag auftauchte. „Geändert“ = SAP hat den Text "
          "nachträglich angepasst (alter Text: History dieser Datei).", "",
          "## Übersicht", "",
          "| Datum | Version | Bereich | Titel | Kennzeichen | Geändert |",
          "|---|---|---|---|---|---|"]
    for e in items:
        title = e["title"].replace("|", "/")
        md.append(f"| {e['date']} | {e['version']} | {e['area']} | {title} | "
                  f"{', '.join(e['tags'])} | {e['changed']} |")
    md += ["", "## Einträge", ""]
    current = None
    for e in items:
        if e["date"] != current:
            current = e["date"]
            md += [f"### {current}", ""]
        md += [f"#### {e['area']} – {e['title']}", "",
               f"*Version {e['version']} · {', '.join(e['tags']) or '–'} · erstmals gesehen {e['first_seen']}"
               + (f" · geändert {e['changed']}" if e["changed"] else "") + "*", ""]
        md += [l + "  " for l in e["text"].splitlines()]   # zwei Leerzeichen = Zeilenumbruch in Markdown
        md.append("")
    return "\n".join(md) + "\n"
