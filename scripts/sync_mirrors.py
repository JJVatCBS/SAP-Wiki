"""Holt die GitHub-Spiegel der SAP-Hilfe und schreibt je neuem SAP-Commit einen Änderungsbericht.

Aufruf:
  python scripts/sync_mirrors.py                      # normaler Wochenlauf
  python scripts/sync_mirrors.py --backfill-since 2026-08-01   # beim ersten Lauf Historie nachholen

Ergebnis:
  reports/mirrors/<id>/<datum>_<sha>.md   ein Bericht je SAP-Commit
  state/mirrors.json                     zuletzt verarbeiteter Commit je Spiegel
"""
import argparse, json, re, subprocess, sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / ".cache" / "mirrors"
STATE = ROOT / "state" / "mirrors.json"
OUT = ROOT / "reports" / "mirrors"
MAX_SNIPPETS = 12          # geänderte Zeilen je Datei im Bericht
SNIPPET_LEN = 400


def git(repo: Path, *args: str) -> str:
    """Git-Befehl in einem geklonten Spiegel ausführen und die Ausgabe zurückgeben."""
    return subprocess.run(["git", "-C", str(repo), *args], check=True,
                          capture_output=True, text=True).stdout


def update_clone(m: dict) -> Path:
    """Spiegel nach .cache/mirrors/<id> klonen bzw. auf den neuesten Stand von SAP bringen."""
    target = CACHE / m["id"]
    if (target / ".git").exists():
        git(target, "fetch", "--quiet", "origin")
        branch = git(target, "rev-parse", "--abbrev-ref", "origin/HEAD").strip()
        git(target, "reset", "--quiet", "--hard", branch)
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "clone", "--quiet", "--filter=blob:none", m["repo"], str(target)], check=True)
    return target


def title_of(repo: Path, sha: str, path: str) -> str:
    """Seitentitel (erste '# '-Zeile) einer Markdown-Datei in einem bestimmten Commit lesen."""
    try:
        text = git(repo, "show", f"{sha}:{path}")
    except subprocess.CalledProcessError:
        return Path(path).stem
    for line in text.splitlines():
        if line.startswith("# "):
            return re.sub(r"<[^>]+>", "", line[2:]).strip()
    return Path(path).stem


def snippets(repo: Path, sha: str, path: str) -> list[str]:
    """Geänderte Textzeilen; Zeilen mit Zahlen zuerst (dort stecken meist Grenzwerte, Versionen, Daten)."""
    diff = git(repo, "show", "--format=", "--unified=0", sha, "--", path)
    lines = [l for l in diff.splitlines()
             if l[:1] in "+-" and not l.startswith(("+++", "---")) and l[1:].strip()]
    norm = lambda s: re.sub(r"\s+", " ", s[1:]).strip()
    removed = {norm(l) for l in lines if l[0] == "-"}
    added = {norm(l) for l in lines if l[0] == "+"}
    same = removed & added                      # nur verschoben oder umformatiert
    lines = [l for l in lines if norm(l) not in same]
    lines.sort(key=lambda l: 0 if re.search(r"\d", l) else 1)
    out = []
    for l in lines[:MAX_SNIPPETS]:
        t = l[1:].strip()
        out.append(f"{l[0]} {t[:SNIPPET_LEN]}{'…' if len(t) > SNIPPET_LEN else ''}")
    return out


def report_commit(m: dict, repo: Path, sha: str) -> Path | None:
    """Für einen SAP-Commit den Bericht reports/mirrors/<id>/<datum>_<sha>.md schreiben: geänderte Seiten mit Link und geänderten Zeilen."""
    meta = git(repo, "show", "-s", "--format=%cs%n%s", sha).splitlines()
    day = meta[0]
    files = git(repo, "show", "--format=", "--name-status", sha, "--", f"{m['path']}/*.md").splitlines()
    if not files:
        return None
    web = m["repo"].removesuffix(".git")
    md = [f"# {m['product']} – Änderung vom {day}", "",
          f"- Quelle: [SAP-Commit {sha[:7]}]({web}/commit/{sha})",
          f"- Geänderte Seiten: {len(files)}", ""]
    format_only = []
    for entry in files:
        parts = entry.split("\t")
        status, path = parts[0][0], parts[-1]
        label = {"A": "neu", "M": "geändert", "D": "gelöscht", "R": "umbenannt"}.get(status, status)
        ref = sha if status != "D" else f"{sha}^"
        title = title_of(repo, ref, path)
        snip = snippets(repo, sha, path) if status == "M" else []
        if status == "M" and not snip:
            format_only.append(title)
            continue
        md.append(f"## {title} ({label})")
        md.append(f"[{path}]({web}/blob/{ref}/{path})")
        md.append("")
        if snip:
            md += ["```diff", *snip, "```", ""]
    if format_only:
        md += ["## Nur Formatierung geändert", "", *[f"- {t}" for t in format_only], ""]
    target = OUT / m["id"] / f"{day}_{sha[:7]}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(md), encoding="utf-8")
    return target


def main() -> None:
    """Alle Spiegel aus config/sources.yaml abrufen und je neuem SAP-Commit einen Bericht schreiben; Stand in state/mirrors.json merken."""
    ap = argparse.ArgumentParser()
    ap.add_argument("--backfill-since", help="beim ersten Lauf: Historie ab diesem Datum (YYYY-MM-DD) nachholen")
    ap.add_argument("--only", help="nur diesen Spiegel (id) verarbeiten")
    a = ap.parse_args()

    cfg = yaml.safe_load((ROOT / "config" / "sources.yaml").read_text(encoding="utf-8"))
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    written = []
    for m in cfg["mirrors"]:
        if a.only and m["id"] != a.only:
            continue
        repo = update_clone(m)
        head = git(repo, "rev-parse", "HEAD").strip()
        last = state.get(m["id"], {}).get("sha")
        if last:
            rng = [f"{last}..{head}"]
        elif a.backfill_since:
            rng = [f"--since={a.backfill_since}", head]
        else:
            print(f"{m['id']}: Ausgangsstand gesetzt ({head[:7]}), noch kein Bericht")
            rng = None
        if rng:
            shas = git(repo, "rev-list", "--reverse", *rng).split()
            for sha in shas:
                p = report_commit(m, repo, sha)
                if p:
                    written.append(p)
            print(f"{m['id']}: {len(shas)} neue SAP-Commits")
        last_day = git(repo, "show", "-s", "--format=%cs", head).strip()
        state[m["id"]] = {"sha": head, "upstream_last_change": last_day, "checked": date.today().isoformat()}
    STATE.parent.mkdir(exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"{len(written)} Berichte geschrieben")


if __name__ == "__main__":
    sys.exit(main())
