"""What's-New-Seiten von help.sap.com über die Datenschnittstelle der Seite abrufen.

Die Seite lädt ihre Einträge per POST https://help.sap.com/http.svc/whatsnew. Welches Produkt
gemeint ist, steht in der Anfrage (Spalten "outputloio" und "deliverable.version"); die Werte
holt sich die Seite vorher aus http.svc/whatsnewconfig.

Vorgehen: Seite einmal im Browser öffnen, die erste Datenanfrage der Seite mitschneiden und
selbst erneut schicken – mit allen Einträgen auf einmal und ohne Datums-/Versionsfilter,
also mit der ganzen Historie. Kein Klicken, kein Blättern.

Bestand: data/whatsnew/<id>.json, Schlüssel = feste Eintrags-ID von SAP ("id").
"""
import html, json, re
from datetime import date
from pathlib import Path

SCHEMA = 3
API = "https://help.sap.com/http.svc/whatsnew"
KEEP_FILTERS = ("outputloio", "deliverable")   # bestimmen das Produkt, alles andere wird geleert
PAGE = 500
SKIP_FIELDS = {"id", "Description", "Latest_Revision", "Valid_as_Of", "Title"}


def fetch(page, url: str, timeout_ms: int = 90000) -> tuple[list[dict], dict]:
    """Öffnet die Seite, schneidet die Datenanfrage mit und holt alle Einträge."""
    captured = {}
    seen = []

    def on_response(resp):
        # Die Seite schickt mehrere Anfragen an http.svc/whatsnew; gebraucht wird die mit Einträgen
        """Antworten der Seite mitlesen und die Datenanfrage merken, deren Antwort Einträge enthält."""
        if resp.request.method != "POST" or not resp.url.startswith(API) or "body" in captured:
            return
        try:
            data = (resp.json() or {}).get("data") or {}
        except Exception:
            return
        seen.append(len(data.get("results") or []))
        if data.get("results"):
            captured["body"] = resp.request.post_data

    page.on("response", on_response)
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)
    except Exception:
        pass
    for _ in range(60):
        if "body" in captured:
            break
        page.wait_for_timeout(500)
    page.remove_listener("response", on_response)
    if "body" not in captured:
        raise RuntimeError(f"Datenanfrage mit Einträgen nicht gefunden (Antworten: {seen})")

    original = json.loads(captured["body"])
    log = {"produktfilter": [c["name"] for c in original.get("columns", [])
                             if c.get("name", "").startswith(KEEP_FILTERS) and c.get("query")]}
    # Varianten von "alles" bis "genau wie die Seite"; die erste mit Treffern gewinnt
    variants = [("ohne Filter, Datum offen", True, "", 500),
                ("ohne Filter, Datum 1900-2100", True, "wide", 500),
                ("ohne Filter, Datum 1900-2100, 100 je Abruf", True, "wide", 100),
                ("ohne Filter, Datum 1900-2100, 25 je Abruf", True, "wide", 25),
                ("Original der Seite", False, None, original.get("size", 25))]
    tried = []
    for name, clear, dates, size in variants:
        body = _variant(original, clear, dates)
        results, total, note = _collect(page, body, size)
        tried.append(f"{name}: {total}{' ' + note if note else ''}")
        if total:
            log.update(variante=name, gesamt_laut_sap=total, gelesen=len(results))
            return [_entry(r) for r in results], log
    log["versuche"] = tried
    return [], log


def _variant(original: dict, clear: bool, dates) -> dict:
    """Kopie der mitgeschnittenen Anfrage: Produktfilter behalten, alle anderen Filter leeren; Datum offen oder 1900–2100."""
    body = json.loads(json.dumps(original))
    if not clear:
        return body
    for col in body.get("columns", []):
        if col.get("name", "").startswith(KEEP_FILTERS):
            continue
        if "query" in col:
            col["query"] = []
        if "dateFrom" in col and col.get("name") != "Latest_Revision":
            col["dateFrom"], col["dateTo"] = ("", "") if dates == "" else ("1900-01-01", "2100-12-31")
    return body


def _collect(page, body: dict, size: int) -> tuple[list, int, str]:
    """Anfrage seitenweise an http.svc/whatsnew schicken, bis alle Einträge da sind. Rückgabe: Einträge, Gesamtzahl laut SAP, Fehlerhinweis."""
    results, start, total = [], 0, None
    while total is None or start < total:
        body["from"], body["size"] = start, size
        resp = page.request.post(API, data=json.dumps(body), headers={"Content-Type": "application/json"})
        if not resp.ok:
            return results, 0, f"HTTP {resp.status}"
        payload = resp.json()
        data = payload.get("data") or {}
        if payload.get("status") != "OK":
            return results, 0, f"Status {payload.get('status')}"
        total = data.get("total", 0) or 0
        batch = data.get("results", [])
        results += batch
        if not batch:
            break
        start += size
    return results, total or 0, ""


def _text(value) -> str:
    """Feldwert von SAP als Text: Listen werden mit Komma verbunden."""
    if isinstance(value, list):
        return ", ".join(str(v) for v in value)
    return "" if value is None else str(value)


def html_to_md(s: str) -> str:
    """Beschreibung (HTML) in lesbares Markdown mit Links umwandeln."""
    s = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>',
               lambda m: f"[{re.sub('<[^>]+>', '', m.group(2)).strip()}]({_abs(m.group(1))})", s, flags=re.S)
    s = re.sub(r"<li[^>]*>", "\n- ", s)
    s = re.sub(r"</(p|div|ul|ol|li)>|<br\s*/?>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    lines = [re.sub(r"[ \t]+", " ", l).strip() for l in s.splitlines()]
    return "\n".join(l for l in lines if l)


def _abs(url: str) -> str:
    """Link vollständig machen: relative help.sap.com-Pfade ergänzen, Umleitungen über link-disclaimer auflösen."""
    url = html.unescape(url)
    m = re.search(r"link-disclaimer\?site=([^&]+)", url)
    if m:
        from urllib.parse import unquote
        return unquote(m.group(1))
    return "https://help.sap.com" + url if url.startswith("/") else url


def _entry(r: dict) -> dict:
    """Einen SAP-Datensatz in unser Format bringen: ID, Datum, Titel, Beschreibung als Markdown, übrige Felder."""
    fields = {k: _text(v) for k, v in r.items() if k not in SKIP_FIELDS and _text(v)}
    return {"id": str(r.get("id")), "date": r.get("Valid_as_Of", "") or "",
            "title": (r.get("Title") or "").strip(),
            "text": html_to_md(r.get("Description") or ""),
            "revision": r.get("Latest_Revision") or "", "fields": fields}


def merge(store_path: Path, entries: list[dict]) -> dict:
    """Einträge in den Bestand data/whatsnew/<id>.json übernehmen: neue anlegen, geänderte markieren, nichts löschen."""
    store = {}
    if store_path.exists():
        data = json.loads(store_path.read_text(encoding="utf-8"))
        if data.get("_schema") == SCHEMA:
            store = data["entries"]
    today = date.today().isoformat()
    stats = {"neu": 0, "geändert": 0}
    for e in entries:
        old = store.get(e["id"])
        if old is None:
            store[e["id"]] = {**e, "first_seen": today, "last_seen": today, "changed": ""}
            stats["neu"] += 1
            continue
        if any(old.get(k) != e[k] for k in ("date", "title", "text", "fields")):
            old.update({k: e[k] for k in ("date", "title", "text", "fields", "revision")}, changed=today)
            stats["geändert"] += 1
        old["last_seen"] = today
    store_path.parent.mkdir(parents=True, exist_ok=True)
    store_path.write_text(json.dumps({"_schema": SCHEMA, "entries": store}, indent=1,
                                     ensure_ascii=False, sort_keys=True), encoding="utf-8")
    return {**stats, "gesamt": len(store), "store": store}


def _cell(s: str) -> str:
    """Text tabellentauglich machen (keine senkrechten Striche, keine Zeilenumbrüche)."""
    return s.replace("|", "/").replace("\n", " ")


def render(p: dict, store: dict) -> str:
    """Bestand als lesbare Markdown-Datei ausgeben: Übersichtstabelle und Einträge mit Beschreibung."""
    items = sorted(store.values(), key=lambda e: (e["date"], e["title"]), reverse=True)
    # Spalten der Übersicht: was SAP für dieses Produkt liefert (technische Felder ausgenommen)
    hidden = {"deliverable.version", "outputloio", "Line_of_Business", "Sub_Process"}
    extra = []
    for e in items:
        for h in e["fields"]:
            if h not in hidden and h not in extra:
                extra.append(h)
    md = [f"# What's New – {p['product']}", "",
          f"Quelle: [{p['url']}]({p['url']}) · {len(items)} Einträge · Stand {date.today().isoformat()}", "",
          "„Geändert“ = SAP hat den Eintrag nachträglich angepasst (alter Text: History dieser Datei).", "",
          "## Übersicht", "",
          "| Datum | Titel | " + " | ".join(extra) + " | Geändert |",
          "|---|---|" + "---|" * len(extra) + "---|"]
    for e in items:
        md.append(f"| {e['date']} | {_cell(e['title'])} | "
                  + " | ".join(_cell(e["fields"].get(h, "")) for h in extra) + f" | {e['changed']} |")
    md += ["", "## Einträge", ""]
    for e in items:
        meta = " · ".join(f"{h}: {_cell(e['fields'][h])}" for h in extra if e["fields"].get(h))
        md += [f"### {e['date']} · {e['title']}", "",
               f"*{meta} · SAP-ID {e['id']}*" + (f" · *geändert {e['changed']}*" if e["changed"] else ""), ""]
        md += [l + "  " for l in e["text"].splitlines()]
        md.append("")
    return "\n".join(md) + "\n"
