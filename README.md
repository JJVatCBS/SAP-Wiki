# SAP-Wiki

Verfolgt Änderungen in der SAP-Dokumentation über die Zeit. SAP zeigt auf help.sap.com nicht an, was sich
wann geändert hat. Dieses Repo holt die Quellen jede Woche ab und macht jede Änderung mit Datum und Quelle
nachvollziehbar. Später pflegt Claude darauf ein LLM-Wiki (Idee nach Andrej Karpathy: das Modell pflegt
dauerhaft Wissensseiten, statt bei jeder Frage die Rohquellen neu zu durchsuchen).

Nur für Julian und cbs intern. Das Repo bleibt privat (es enthält SAP Notes, die nur für lizenzierte Kunden bestimmt sind).

## Überblick

```
 Quellen                                   Wochenlauf (GitHub Actions)            Ablage im Repo
 ────────────────────────────────────      ───────────────────────────            ─────────────────────────────
 GitHub-Spiegel der SAP-Hilfe       ──►    sync_mirrors.py              ──►       reports/mirrors/<produkt>/
 What's New (help.sap.com)          ──►    fetch_help_pages.py          ──►       snapshots/, data/whatsnew/
                                           + whatsnew.py
 Ganze Guides ohne Spiegel          ──►    fetch_help_guides.py         ──►       guides/<guide>/
 (help.sap.com, seitenweise)               (+ mirror_check.py)                    reports/mirror-check/
 SAP Notes / KBAs (PDF, manuell)    ──►    ingest_note_pdfs.py          ──►       notes/
                                           build_weekly_report.py       ──►       reports/weekly/
                                                                                  (geplant: wiki/ durch Claude)
```

Der Lauf startet jeden Montag um 04:17 UTC automatisch und lässt sich jederzeit über
**Actions → SAP-Wiki Wochenlauf → Run workflow** starten (ohne Eingaben).

## Quellen und wie sie abgerufen werden

| Quelle | Produkte | Weg | Änderungshistorie |
|---|---|---|---|
| GitHub-Spiegel ([github.com/SAP-docs](https://github.com/SAP-docs)) | SAP Datasphere (3 Guides), SAP HANA Cloud Database und Data Lake, SAP Integration Suite, SAP AI | Repo klonen, neue SAP-Commits auswerten | aus SAPs eigenen Commits |
| What's New auf help.sap.com | SAP Business Data Cloud, SAP Analytics Cloud, SAP Datasphere, SAP HANA Cloud | Datenschnittstelle der Seite (`http.svc/whatsnew`): Anfrage der Seite mitschneiden, ohne Filter erneut senden, ganze Historie | Bestand je Eintrag über die feste SAP-ID |
| Guides auf help.sap.com ohne Spiegel | z. B. SAP BW/4HANA (Data Product Generator) | Schnittstelle der Hilfe: `deliverableMetadata` → Inhaltsverzeichnis (`fullToc`) → jede Seite (`pagecontent`) | Git-History je Seite; Abruf nur bei neuer `buildNo` |
| SAP Notes und KBAs | alle | PDF manuell aus SAP for Me in `notes/inbox/` legen | Archiv aller Versionen, Changelog mit geänderten Abschnitten |

Konfiguriert wird alles in [`config/sources.yaml`](config/sources.yaml).

## Ordner

| Ordner / Datei | Inhalt | Wer schreibt |
|---|---|---|
| `config/sources.yaml` | Quellen: Spiegel, What's-New-Seiten, Guides, Abgleiche | Julian / Claude |
| `scripts/` | Abruf und Aufbereitung (siehe unten) | Claude |
| `.github/workflows/weekly.yml` | Wochenlauf | Claude |
| `reports/weekly/<Jahr>-KW<nn>.md` | **Einstieg:** was sich in dieser Woche geändert hat, plus Warnungen | Job |
| `reports/mirrors/<produkt>/<datum>_<commit>.md` | je SAP-Commit eines Spiegels: geänderte Seiten mit geänderten Zeilen | Job |
| `snapshots/<produkt>-whats-new.md` | What's New lesbar: Übersichtstabelle und alle Einträge, Spalte „Geändert“ | Job |
| `data/whatsnew/<produkt>.json` | Bestand der What's-New-Einträge (Maschinenformat) | Job |
| `guides/<guide>/` | eine Datei je Hilfeseite, `README.md` = Inhaltsverzeichnis; Bilder als Link auf help.sap.com | Job |
| `reports/mirror-check/<id>.md` | Abgleich GitHub-Spiegel gegen SAP-Hilfe | Job |
| `notes/inbox/` | **hier SAP-Note-PDFs ablegen** (Dateiname egal) | Julian |
| `notes/archive/<nummer>_v<version>.pdf` | alle Versionen aller Notes | Job |
| `notes/text/<nummer>.md` | aktuelle Version jeder Note als lesbarer Text | Job |
| `notes/changelog.md` | neue Notes und Versionswechsel mit geänderten Abschnitten, neueste zuerst | Job |
| `notes/log.csv` | Übersicht aller Notes mit aktueller Version | Job |
| `state/` | Merkdateien des Jobs (letzter Stand je Quelle, Warnungen) | Job |
| `wiki/` | geplant: vom LLM gepflegtes Wiki (Changelogs je Produkt, Themenseiten); bisher zwei Beispielseiten | Claude |
| `prompts/` | Entwurf des Auftrags für den wöchentlichen Wiki-Lauf | Claude |

## Lesen

- **Diese Woche:** neueste Datei in `reports/weekly/`.
- **Was SAP angekündigt hat:** `snapshots/<produkt>-whats-new.md`.
- **Änderungen über die Zeit:** Datei öffnen → **History** (jeder Eintrag ist ein Wochenlauf, rot/grün zeigt die Änderung).
  **Blame** zeigt je Zeile, seit wann sie so dasteht.
- **Suchen:** Taste `t` (Datei finden) oder das Suchfeld oben (Text im ganzen Repo). Taste `.` öffnet einen Editor im Browser.

## SAP Notes ablegen

1. Note in SAP for Me öffnen und als PDF speichern (Dateiname egal).
2. PDF in `notes/inbox/` hochladen (**Add file → Upload files**).
3. Beim nächsten Lauf liest der Job **aus dem Inhalt** Nummer, Version, Titel, Freigabedatum und Komponente.
   - neue Note → Text in `notes/text/`, Eintrag „neu im Archiv“ im Changelog
   - höhere Version → Text ersetzt, Changelog-Eintrag mit den geänderten Abschnitten
   - gleiche Version noch einmal → verworfen; ältere Version → nur archiviert
   - Nummer oder Version nicht erkennbar → PDF bleibt in der Inbox, Meldung im Log

Ob es eine neue Version gibt, meldet SAP for Me per Mail (Note als Favorit markieren). Der Job selbst kann
SAP for Me nicht abfragen (Login).

## Neue Quellen hinzufügen

- **What's-New-Seite:** URL der Seite in `config/sources.yaml` unter `help_pages` eintragen.
- **Guide ohne GitHub-Spiegel:** Link auf *irgendeine* Seite des Guides (am besten Englisch,
  `help.sap.com/docs/<produkt>/<guide>/<seite>.html`) unter `help_guides` eintragen. Die Guide-ID in der URL
  bleibt stabil; die interne Nummer holt der Job bei jedem Lauf neu.
- **Prüfen, ob ein GitHub-Spiegel vollständig ist:** Eintrag unter `mirror_checks` (Spiegel, Ordner, Link auf
  den Guide in der Hilfe). Ergebnis unter `reports/mirror-check/`. Nach der Auswertung den Eintrag entfernen.

## Skripte

| Skript | Aufgabe |
|---|---|
| `sync_mirrors.py` | GitHub-Spiegel klonen bzw. aktualisieren, je neuem SAP-Commit einen Bericht schreiben |
| `fetch_help_pages.py` | help_pages abrufen; What's New über `whatsnew.py` |
| `whatsnew.py` | Datenschnittstelle der What's-New-Seiten, Bestand je Eintrag, lesbare Ausgabe |
| `fetch_help_guides.py` | ganze Guides seitenweise über die Schnittstelle der Hilfe; Bilder als Link |
| `mirror_check.py` | Abgleich GitHub-Spiegel gegen Hilfe (Text je Seite, satzweise) |
| `ingest_note_pdfs.py` | SAP-Note-PDFs auslesen, archivieren, Changelog schreiben |
| `build_weekly_report.py` | Wochenbericht aus allen Änderungen eines Laufs |

Jedes Skript beschreibt oben seinen Ablauf; jede Funktion hat eine kurze Beschreibung.

### Wartung

- **Sicherungen:** Liefert eine Quelle zu wenig (Seite verschoben, Aufbau geändert, Fehlerseite), überschreibt der
  Job den alten Stand nicht und meldet es oben im Wochenbericht unter „Achtung“ (`state/warnings*.md`).
- **Erkennung verbessert:** In `ingest_note_pdfs.py` (`PARSER_VERSION`) bzw. `fetch_help_guides.py` (`FORMAT`)
  die Versionsnummer erhöhen. Der nächste Lauf liest dann das Notes-Archiv bzw. alle Guides einmal neu ein.
- **Lokal ausführen** (optional): `pip install -r requirements.txt`, `python -m playwright install chromium`,
  Skripte einzeln starten, danach committen. Für Notes wird `pdftotext` (poppler) benötigt.

## Grenzen und offene Punkte

- **robots.txt:** help.sap.com bittet automatische Programme, `/whats-new/`, `/docs/` und `http.svc` nicht
  abzurufen. Der Job lädt die Seiten wie ein Browser und hält sich damit nicht an diese Bitte. Bewusst so
  entschieden; geringe Last (wenige Abrufe pro Woche, Guides nur bei neuer Veröffentlichung, Pausen zwischen Seiten).
- **GitHub-Spiegel** gibt es nicht für BDC, BW/BW4HANA, SAC, S/4HANA. Der Spiegel der SAP HANA Cloud Database
  wurde seit 28.10.2025 nicht aktualisiert (Stand 11/2026).
- **Datum der Spiegel:** SAP fasst Änderungen je Veröffentlichung zusammen („squashed“). Das Datum ist das
  Veröffentlichungsdatum im Spiegel, nicht zwingend das der Änderung auf help.sap.com.
- **Bilder** werden nur verlinkt. Tauscht SAP ein Bild unter gleichem Namen aus, sieht das Repo das nicht.
- **Noch nicht gebaut:** wöchentlicher Wiki-Lauf durch Claude (Schema, Ingest, Lint), Bilder herunterladen (optional).
