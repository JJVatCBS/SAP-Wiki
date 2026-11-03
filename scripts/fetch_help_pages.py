"""Rendert Seiten von help.sap.com ohne GitHub-Spiegel (z. B. What's New) und speichert den Text.

Die Änderungshistorie entsteht über die Commits dieses Repos: Ändert sich eine Seite,
zeigt git diff snapshots/<id>.md genau, was SAP geändert hat.
"""
import sys
from datetime import date
from pathlib import Path

import yaml
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
SNAP = ROOT / "snapshots"


def main() -> int:
    cfg = yaml.safe_load((ROOT / "config" / "sources.yaml").read_text(encoding="utf-8"))
    pages = [p for p in cfg.get("help_pages", []) if p.get("url")]
    if not pages:
        print("Keine help_pages mit URL konfiguriert")
        return 0
    errors = 0
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(locale="en-US")
        for p in pages:
            try:
                page.goto(p["url"], wait_until="networkidle", timeout=90000)
                if p.get("wait_for"):
                    page.wait_for_selector(p["wait_for"], timeout=60000)
                else:
                    page.wait_for_timeout(8000)
                # What's-New-Listen laden beim Scrollen bzw. per Button nach: bis zu 40 Runden
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
                lines = [l.rstrip() for l in text.splitlines()]
                body = "\n".join(l for l in lines if l.strip())
                header = (f"---\nproduct: {p['product']}\ntitle: {p['title']}\nurl: {p['url']}\n"
                          f"source_type: SAP Help\n---\n\n")
                (SNAP / f"{p['id']}.md").write_text(header + body + "\n", encoding="utf-8")
                print(f"{p['id']}: {len(body)} Zeichen")
            except Exception as e:  # eine fehlerhafte Seite soll den Lauf nicht abbrechen
                errors += 1
                print(f"{p['id']}: FEHLER {e}")
        browser.close()
    (ROOT / "state" / "help_pages_last_run.txt").write_text(f"{date.today().isoformat()} Fehler: {errors}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
