"""Verarbeitet SAP-Note- und KBA-PDFs.

Ablauf je Lauf:
  1. Neue PDFs aus notes/inbox/ nach notes/archive/ verschieben.
  2. Alle PDFs in notes/archive/ auslesen (das sind wenige, daher jedes Mal komplett):
     - Nummer, Version, Titel, Freigabedatum aus dem Kopf der Note
     - Archivdatei einheitlich benennen: <nummer>_v<version>.pdf
  3. notes/text/<nummer>.md aus der jeweils neuesten Version schreiben
     (eine Datei je Note; frühere Versionen zeigt die History dieser Datei).
  4. notes/log.csv aus dem Archiv neu aufbauen.

Weil Text und Log jedes Mal vollständig aus dem Archiv entstehen, korrigieren sich
falsch erkannte Einträge früherer Läufe von selbst.
"""
import csv, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "notes" / "inbox"
TEXT = ROOT / "notes" / "text"
ARCHIVE = ROOT / "notes" / "archive"
LOG = ROOT / "notes" / "log.csv"
FIELDS = ["nummer", "version", "titel", "freigabe", "komponente", "datei"]

# Abschnittsüberschriften in SAP Notes und KBAs
SECTIONS = ["Symptom", "Other Terms", "Reason and Prerequisites", "Cause", "Solution", "Environment",
            "Resolution", "Reproducing the Issue", "Keywords", "Attributes", "Products",
            "This document refers to", "This document is referenced by", "References",
            "Software Components", "Affected Releases", "Correction Instructions",
            "Support Packages & Patches", "Prerequisites", "See Also", "Related Content"]
SECTION_RE = re.compile(r"^(" + "|".join(re.escape(s) for s in SECTIONS) + r")\s*$")


def pdf_text(pdf: Path) -> str:
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


def main() -> int:
    INBOX.mkdir(parents=True, exist_ok=True)
    TEXT.mkdir(parents=True, exist_ok=True)
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    for pdf in INBOX.glob("*.pdf"):
        target = ARCHIVE / pdf.name
        if target.exists():
            target = ARCHIVE / f"neu_{pdf.name}"
        shutil.move(str(pdf), target)

    notes, problems = {}, []
    for pdf in sorted(ARCHIVE.glob("*.pdf")):
        text = pdf_text(pdf)
        meta = parse(text)
        if not meta["nummer"]:
            problems.append(pdf.name)
            print(f"{pdf.name}: Nummer nicht erkannt – bleibt unter altem Namen im Archiv")
            continue
        name = f"{meta['nummer']}_v{meta['version'] or 'x'}.pdf"
        if pdf.name != name:
            if (ARCHIVE / name).exists():
                pdf.unlink()                      # dieselbe Version liegt schon im Archiv
            else:
                pdf.rename(ARCHIVE / name)
        meta["datei"] = name
        best = notes.get(meta["nummer"])
        if best is None or int(meta["version"] or 0) >= int(best[0]["version"] or 0):
            notes[meta["nummer"]] = (meta, text)

    # Text je Note aus der neuesten Version; Dateien ohne passende Note entfernen
    for old in TEXT.glob("*.md"):
        if old.stem not in notes:
            old.unlink()
    for num, (meta, text) in sorted(notes.items()):
        header = ("---\n"
                  f"source_type: SAP Note/KBA\nnumber: {num}\nversion: {meta['version']}\n"
                  f"title: \"{meta['titel']}\"\nrelease_date: {meta['freigabe']}\n"
                  f"component: {meta['komponente']}\nurl: https://me.sap.com/notes/{num}\n---\n\n"
                  f"# {num} – {meta['titel']}\n\n"
                  f"Version {meta['version']} · freigegeben {meta['freigabe']} · Komponente {meta['komponente']} · "
                  f"[in SAP for Me öffnen](https://me.sap.com/notes/{num})\n\n")
        (TEXT / f"{num}.md").write_text(header + to_markdown(text), encoding="utf-8")
        print(f"{num} v{meta['version']} ({meta['freigabe']}): {meta['titel']}")

    with LOG.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        for num, (meta, _) in sorted(notes.items()):
            w.writerow({k: meta.get(k, "") for k in FIELDS})
    if problems:
        print(f"Nicht erkannt: {', '.join(problems)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
