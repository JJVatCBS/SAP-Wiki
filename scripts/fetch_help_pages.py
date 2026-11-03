"""Rendert Seiten von help.sap.com ohne GitHub-Spiegel (z. B. What's New) und speichert den Text.

Die Änderungshistorie entsteht über die Commits dieses Repos: Ändert sich eine Seite,
zeigt git diff snapshots/<id>.md genau, was SAP geändert hat.

What's-New-Seiten sind in Seiten zu 25 Einträgen aufgeteilt: das Skript versucht zuerst die
größte Seitengröße zu wählen und blättert danach über "Next" bzw. die Seitenzahlen weiter.

Sicherung: Ist der neue Text deutlich kürzer als der gespeicherte (Seite verschoben, Fehlerseite,
Ladeproblem), wird nicht überschrieben, sondern eine Warnung nach state/warnings.md geschrieben.

Übergangsweise schreibt das Skript den HTML-Aufbau der ersten Seite nach debug/<id>.html,
damit die Einträge später sauber als Tabelle ausgelesen werden können.
"""
import sys
from datetime import date
from pathlib import Path

import yaml

import whatsnew
from playwright.sync_api import TimeoutError as PWTimeout, sync_playwright

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "whatsnew"
SNAP = ROOT / "snapshots"
DEBUG = ROOT / "debug"
WARN = ROOT / "state" / "warnings.md"
MIN_CHARS = 1000        # weniger Text = Seite nicht richtig geladen
MIN_RATIO = 0.5         # neuer Text < 50 % des alten = nicht überschreiben
MAX_PAGES = 60

NEXT_SELECTORS = [
    "button[aria-label*='Next' i]:not([disabled])",
    "a[aria-label*='Next' i]",
    "[role='button'][aria-label*='Next' i]:not([aria-disabled='true'])",
    "button[title*='Next' i]:not([disabled])",
    "button:has-text('›'):not([disabled])",
    "button:has-text('>'):not([disabled])",
]


def main_text(page) -> str:
    el = page.query_selector("main")
    return (el or page.query_selector("body")).inner_text()


def try_max_page_size(page) -> None:
    """Falls es eine Auswahl der Seitengröße gibt (25/50/100/All), die größte wählen."""
    for sel in page.query_selector_all("select"):
        opts = sel.eval_on_selector_all("option", "os => os.map(o => o.value)")
        if any(o.strip().isdigit() for o in opts):
            best = max((o for o in opts if o.strip().isdigit()), key=lambda o: int(o))
            all_opt = [o for o in opts if o.lower().startswith("all")]
            sel.select_option(all_opt[0] if all_opt else best)
            page.wait_for_timeout(4000)
            return


def click_next(page) -> bool:
    for s in NEXT_SELECTORS:
        el = page.query_selector(s)
        if el and el.is_visible():
            el.click()
            page.wait_for_timeout(3000)
            return True
    return False


def load(page, p: dict) -> tuple[list[str], str]:
    try:
        # What's-New-Seiten laden laufend nach, "networkidle" wird dort nie erreicht
        page.goto(p["url"], wait_until="domcontentloaded", timeout=90000)
    except PWTimeout:
        pass
    if p.get("wait_for"):
        page.wait_for_selector(p["wait_for"], timeout=60000)
    else:
        page.wait_for_timeout(15000)
    first_html = page.evaluate("(document.querySelector('main') || document.body).outerHTML")
    try_max_page_size(page)
    pages, seen = [], set()
    for _ in range(MAX_PAGES):
        t = main_text(page)
        if t in seen:
            break
        seen.add(t)
        pages.append(t)
        if not click_next(page):
            break
    lines = []
    for t in pages:
        lines += [l.strip() for l in t.splitlines() if l.strip()]
    print(f"{p['id']}: {len(pages)} Seite(n) gelesen")
    return lines, first_html


def main() -> int:
    cfg = yaml.safe_load((ROOT / "config" / "sources.yaml").read_text(encoding="utf-8"))
    pages = [p for p in cfg.get("help_pages", []) if p.get("url")]
    for d in (SNAP, DEBUG, DATA, WARN.parent):
        d.mkdir(parents=True, exist_ok=True)
    warnings = []
    if not pages:
        print("Keine help_pages mit URL konfiguriert")
    else:
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            page = browser.new_page(locale="en-US", viewport={"width": 1600, "height": 2000})
            for p in pages:
                target = SNAP / f"{p['id']}.md"
                try:
                    lines, html = load(page, p)
                    (DEBUG / f"{p['id']}.html").write_text(html, encoding="utf-8")
                except Exception as e:  # eine fehlerhafte Seite soll den Lauf nicht abbrechen
                    warnings.append(f"{p['id']}: nicht geladen ({str(e).splitlines()[0]})")
                    print(f"{p['id']}: FEHLER {e}")
                    continue
                if "/whats-new/" in p["url"]:
                    entries = whatsnew.parse(lines)
                    if len(entries) < 5:
                        warnings.append(f"{p['id']}: nur {len(entries)} Einträge erkannt – nicht übernommen. "
                                        f"Seitenaufbau geändert oder URL verschoben? {p['url']}")
                        print(f"{p['id']}: nur {len(entries)} Einträge erkannt, nicht übernommen")
                        continue
                    r = whatsnew.merge(DATA / f"{p['id']}.json", entries)
                    target.write_text(whatsnew.render(p, r["store"]), encoding="utf-8")
                    print(f"{p['id']}: {len(entries)} Einträge gelesen, {r['neu']} neu, "
                          f"{r['geändert']} geändert, Bestand {r['gesamt']}")
                    continue
                body = "\n\n".join(lines)
                old = target.read_text(encoding="utf-8") if target.exists() else ""
                if len(body) < MIN_CHARS or (old and len(body) < MIN_RATIO * len(old)):
                    warnings.append(f"{p['id']}: nur {len(body)} Zeichen (vorher {len(old)}) – "
                                    f"nicht übernommen. Seite verschoben? URL prüfen: {p['url']}")
                    print(f"{p['id']}: zu wenig Text ({len(body)}), nicht übernommen")
                    continue
                header = (f"---\nproduct: {p['product']}\ntitle: {p['title']}\nurl: {p['url']}\n"
                          f"source_type: SAP Help\n---\n\n")
                target.write_text(header + body + "\n", encoding="utf-8")
                print(f"{p['id']}: {len(body)} Zeichen")
            browser.close()
    WARN.write_text(f"# Warnungen help.sap.com, Lauf {date.today().isoformat()}\n\n"
                    + ("\n".join(f"- {w}" for w in warnings) if warnings else "- keine") + "\n",
                    encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
