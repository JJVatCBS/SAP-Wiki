# Prompt: wöchentlicher Claude-Lauf (Wiki pflegen)

Lies im Repo sap-wiki den neuesten Bericht unter reports/weekly/ und alle darin verlinkten Dateien
(reports/mirrors/…, geänderte snapshots/…, neue notes/text/…).

1. Trage jede inhaltliche Änderung in wiki/changelog/<produkt>.md ein (neueste oben):
   Datum laut SAP, Seite, Art (neu/geändert/gelöscht), eine Zeile „Kurz“, Link auf Commit bzw. Datei.
   Reine Formatierungen weglassen.
2. Ändert sich ein Wert, den eine Seite unter wiki/topics/ beschreibt (Grenzwert, Wartungsdatum, Lizenzregel,
   unterstützte Quelle), aktualisiere dort „Aktueller Stand“ und ergänze die Verlaufstabelle. Alte Werte nie löschen.
3. Neue SAP Notes: Nummer, Version, Titel und Kernaussage in wiki/changelog/sap-notes.md; Verweis von betroffenen
   Themenseiten.
4. Kennzeichne eigene Einordnungen als „Ableitung“. Belegt ist nur, was im SAP-Text steht.
5. Schreib am Ende von reports/weekly/<datei> einen Abschnitt „Für Julian“: höchstens 5 Änderungen, die für
   Beratung zu BW, Datasphere, BDC, HANA oder SAC relevant sind, je ein Satz.

Keine Inhalte aus Kundenprojekten ins Wiki schreiben.
