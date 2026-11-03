"""Rendert Seiten von help.sap.com ohne GitHub-Spiegel (z. B. What's New) und speichert den Text.

Die Änderungshistorie entsteht über die Commits dieses Repos: Ändert sich eine Seite,
zeigt git diff snapshots/<id>.md genau, was SAP geändert hat.

Sicherung: Ist der neue Text deutlich kürzer als der gespeicherte (Seite verschoben, Fehlerseite,
Ladeproblem), wird nicht überschrieben, sondern eine Warnung nach state/warnings.md geschrieben.
"""
import sys
from datetime import date
from pathlib import Path

import yaml
from playwright.sync_api import TimeoutError as PWTimeout, sync_playwright

ROOT = Path(__file__).resolve().parents[1]
SNAP = ROOT / "snapshots"
WARN = ROOT / "state" / "warnings.md"
MIN_CHARS = 1000        # weniger Text = Seite nicht richtig geladen
MIN_RATIO = 0.5         # neuer Text < 50 % des alten = nicht überschreiben


def load(page, p: dict) -> str:
    try:
        # What's-New-Seiten laden laufend nach, "networkidle" wird dort nie erreicht
        page.goto(p["url"], wait_until="domcontentloaded", timeout=90000)
    except PWTimeout:
        pass  # trotzdem versuchen, was bis dahin geladen ist
    if p.get("wait_for"):
        page.wait_for_selector(p["wait_for"], timeout=60000)
    else:
        page.wait_for_timeout(15000)
    # Listen laden beim Scrollen bzw. per Button nach: bis zu 40 Runden
    for _ in range(40):
        before = page.evaluate("document.body.innerText.length")
        page.mouse.wheel(0, 20000)
        btn = page.query_selector("button:has-text('More'), button:has-text('Load more'), "
                                  "button:has-text('Show more')")
        if btn and btn.is_visible():
            btn.click()
        page.wait_for_timeout(1500)
        if page.evaluate("document.body.innerText.length") == before:
            break
    text = page.inner_text("main") if page.query_selector("main") else page.inner_text("body")
    return "\n".join(l.rstrip() for l in text.splitlines() if l.strip())


def main() -> int:
    cfg = yaml.safe_load((ROOT / "config" / "sources.yaml").read_text(encoding="utf-8"))
    pages = [p for p in cfg.get("help_pages", []) if p.get("url")]
    SNAP.mkdir(parents=True, exist_ok=True)
    WARN.parent.mkdir(parents=True, exist_ok=True)
    warnings = []
    if not pages:
        print("Keine help_pages mit URL konfiguriert")
    else:
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            page = browser.new_page(locale="en-US")
            for p in pages:
                target = SNAP / f"{p['id']}.md"
                try:
                    body = load(page, p)
                except Exception as e:  # eine fehlerhafte Seite soll den Lauf nicht abbrechen
                    warnings.append(f"{p['id']}: nicht geladen ({str(e).splitlines()[0]})")
                    print(f"{p['id']}: FEHLER {e}")
                    continue
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
