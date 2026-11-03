# SAP-Wiki

Verfolgt Änderungen in der SAP-Dokumentation über die Zeit. SAP versioniert help.sap.com nicht sichtbar;
dieses Repo macht jede Änderung mit Datum und Quelle nachvollziehbar. Nur für Julian und cbs intern.

## Aufbau

```
config/sources.yaml          welche Quellen abgerufen werden
scripts/                     Abruf und Aufbereitung (läuft wöchentlich in GitHub Actions)
reports/mirrors/<produkt>/   ein Bericht je SAP-Änderung aus den GitHub-Spiegeln
reports/weekly/              Wochenzusammenfassung = Eingabe für Claude
snapshots/                   Text von help.sap.com-Seiten ohne Spiegel (What's New); Historie über git log
notes/inbox/                 hier SAP-Note-PDFs ablegen
notes/text/, notes/log.csv   aufbereitete Notes (eine Datei je Note, Versionen über git log)
wiki/changelog/              Änderungen je Produkt (Claude pflegt)
wiki/topics/                 Themenseiten mit aktuellem Stand und Verlauf (Claude pflegt)
prompts/weekly-claude-run.md Auftrag für den wöchentlichen Claude-Lauf
```

## Einrichtung (einmalig)

1. ZIP entpacken und den Inhalt in dein privates Repo hochladen (alle Ordner, auch `.github/`).
   Mit Git: Inhalt ins geklonte Repo kopieren, dann `git add -A`, `git commit -m "SAP-Wiki Start"`, `git push`.
   Im Browser: „Add file → Upload files“; Ordner, die mit einem Punkt beginnen (`.github`), lädt der Browser
   manchmal nicht mit hoch – dann `.github/workflows/weekly.yml` über „Create new file“ anlegen und den Inhalt einfügen.
2. Im Repo: Settings → Actions → General → „Workflow permissions“ auf **Read and write permissions** stellen.
3. Actions → „SAP-Wiki Wochenlauf“ → **Run workflow**. Beim ersten Lauf bei `backfill_since` z. B. `2026-09-01`
   eintragen, dann werden die SAP-Änderungen seit diesem Datum nachgeholt.
4. Nach dem Lauf im Log den Schritt „help.sap.com-Seiten“ prüfen. Erst wenn dort URLs eingetragen sind
   (config/sources.yaml, help_pages), wird etwas abgerufen. Kommt ein Fehler, ist help.sap.com aus GitHub Actions
   gesperrt; dann diesen Schritt lokal laufen lassen.

Danach läuft der Job jeden Montag um 04:17 UTC.

## SAP Notes

SAP for Me schickt bei Änderungen an Favoriten nur eine allgemeine Mail ohne Note-Nummer. Ablauf:
Mail kommt → Note in SAP for Me öffnen → als PDF speichern → in `notes/inbox/` hochladen.
Der nächste Lauf liest Nummer, Version und Titel aus, legt den Text unter `notes/text/<nummer>.md` ab
(eine Datei je Note; ältere Versionen über die Git-Historie) und archiviert das PDF.
SAP Notes sind nur für lizenzierte Kunden bestimmt: Repo privat halten.

## Grenzen

- GitHub-Spiegel gibt es nicht für alle Produkte (kein BDC, BW, SAC, S/4HANA). Für diese die What's-New-Seiten
  in config/sources.yaml eintragen.
- Der Spiegel der SAP HANA Cloud Database wurde seit 28.10.2025 nicht aktualisiert (Stand 03.11.2026).
- SAP fasst Änderungen pro Veröffentlichung zusammen („squashed“). Das Datum ist das Veröffentlichungsdatum
  im Spiegel, nicht zwingend das Datum der Änderung auf help.sap.com.
