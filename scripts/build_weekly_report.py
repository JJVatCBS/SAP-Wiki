"""Fasst die Änderungen eines Laufs in reports/weekly/<JJJJ>-KW<nn>.md zusammen.

Läuft nach den Abruf-Skripten und vor dem Commit. Grundlage ist git status:
neue Spiegel-Berichte, geänderte help.sap.com-Snapshots und neue oder geänderte Notes.
Dieser Bericht ist die Eingabe für den wöchentlichen Claude-Lauf, der das Wiki pflegt.
"""
import subprocess, sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True, capture_output=True, text=True).stdout


def changed(prefix: str) -> list[tuple[str, str]]:
    out = []
    for line in git("status", "--porcelain", "--untracked-files=all", "--", prefix).splitlines():
        status, path = line[:2].strip(), line[3:]
        if path.endswith(".gitkeep"):
            continue
        out.append(("neu" if status in ("??", "A") else "geändert", path))
    return out


def main() -> int:
    y, w, _ = date.today().isocalendar()
    mirrors = changed("reports/mirrors")
    snaps = changed("snapshots")
    notes = changed("notes/text")
    md = [f"# Änderungen KW {w}/{y}", "", f"Lauf vom {date.today().isoformat()}", ""]
    warn = ROOT / "state" / "warnings.md"
    if warn.exists() and "- keine" not in warn.read_text(encoding="utf-8"):
        md += ["## Achtung: Quellen nicht vollständig abgerufen", "",
               *warn.read_text(encoding="utf-8").splitlines()[2:], ""]
    md += ["## SAP-Hilfe aus GitHub-Spiegeln", ""]
    md += [f"- [{Path(p).parent.name} · {Path(p).stem}](../../{p})" for _, p in mirrors] or ["- keine Änderungen"]
    md += ["", "## help.sap.com-Seiten (What's New u. a.)", ""]
    for kind, p in snaps or []:
        md.append(f"- {p} ({kind})")
        if kind == "geändert":
            diff = git("diff", "--unified=0", "--", p)
            lines = [l for l in diff.splitlines() if l[:1] in "+-" and not l.startswith(("+++", "---"))]
            md += ["", "```diff", *lines[:60], "```", ""]
    if not snaps:
        md.append("- keine Änderungen")
    md += ["", "## SAP Notes und KBAs", ""]
    md += [f"- {Path(p).stem} ({k})" for k, p in notes] or ["- keine neuen PDFs"]
    target = ROOT / "reports" / "weekly" / f"{y}-KW{w:02d}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(target.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
