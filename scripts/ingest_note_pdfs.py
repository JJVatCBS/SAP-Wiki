"""Verarbeitet SAP-Note- und KBA-PDFs aus notes/inbox/.

Je PDF:
  - Text extrahieren (pdftotext) nach notes/text/<nummer>.md
    -> eine Note behält immer dieselbe Datei; neue Versionen überschreiben sie,
       die Historie zeigt git log -p notes/text/<nummer>.md
  - Nummer, Version, Titel und Datum aus dem Text lesen und in notes/log.csv eintragen
  - PDF nach notes/archive/<nummer>_v<version>.pdf verschieben
"""
import csv, re, shutil, subprocess, sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "notes" / "inbox"
TEXT = ROOT / "notes" / "text"
ARCHIVE = ROOT / "notes" / "archive"
LOG = ROOT / "notes" / "log.csv"
FIELDS = ["verarbeitet", "nummer", "version", "titel", "freigabe", "datei"]


def pdf_text(pdf: Path) -> str:
    return subprocess.run(["pdftotext", "-layout", str(pdf), "-"], check=True,
                          capture_output=True, text=True).stdout


def parse(text: str, fallback: str) -> dict:
    """SAP-Note-PDFs beginnen mit '<Nummer> - <Titel>' und enthalten 'Version: n' und 'Release Date:'."""
    head = re.search(r"^\s*(\d{6,8})\s+-\s+(.+)$", text, re.M)
    num = head.group(1) if head else (re.search(r"\d{6,8}", fallback) or [None])[0]
    ver = re.search(r"Version\s*:?\s*(\d+)", text)
    rel = re.search(r"(?:Release\s*Date|Released\s*On)\s*:?\s*([0-9./-]{8,10})", text, re.I)
    return {"nummer": num or fallback,
            "titel": head.group(2).strip() if head else "",
            "version": ver.group(1) if ver else "",
            "freigabe": rel.group(1) if rel else ""}


def main() -> int:
    pdfs = sorted(INBOX.glob("*.pdf"))
    if not pdfs:
        print("Keine neuen PDFs")
        return 0
    TEXT.mkdir(parents=True, exist_ok=True)
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    new_log = not LOG.exists()
    with LOG.open("a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        if new_log:
            w.writeheader()
        for pdf in pdfs:
            text = pdf_text(pdf)
            meta = parse(text, pdf.stem)
            header = ("---\n"
                      f"source_type: SAP Note/KBA\nnumber: {meta['nummer']}\nversion: {meta['version']}\n"
                      f"title: \"{meta['titel']}\"\nrelease_date: {meta['freigabe']}\n"
                      f"url: https://me.sap.com/notes/{meta['nummer']}\n---\n\n")
            (TEXT / f"{meta['nummer']}.md").write_text(header + text, encoding="utf-8")
            target = ARCHIVE / f"{meta['nummer']}_v{meta['version'] or 'x'}.pdf"
            shutil.move(str(pdf), target)
            w.writerow({"verarbeitet": date.today().isoformat(), **meta, "datei": target.name})
            print(f"{meta['nummer']} v{meta['version']}: {meta['titel']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
