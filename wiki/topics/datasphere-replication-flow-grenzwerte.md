---
thema: SAP Datasphere – Grenzwerte Replication Flows
stand: 2026-11-03
quellen: SAP Help (GitHub-Spiegel SAP-docs/sap-datasphere)
---

# Replication Flows: parallele Jobs und Threads

**Aktueller Stand (SAP Help, Version vom 10.02.2026):** maximal 16 parallele Replication-Flow-Jobs je Tenant,
damit bis zu 80 Work Orders für Datentransfer und 80 für Housekeeping. Beim Initial Load nutzt ein Flow
standardmäßig maximal 10 Threads je Quelle und Ziel.

## Verlauf

| Datum | Parallele Jobs je Tenant | Threads je Flow (Initial Load) | Beleg |
|---|---|---|---|
| bis 11.11.2025 | 10 | 10 | [b8e432d](https://github.com/SAP-docs/sap-datasphere/commit/b8e432d) |
| 12.11.2025 | 16 | 16 | [ad58ac7](https://github.com/SAP-docs/sap-datasphere/commit/ad58ac7) |
| 27.01.2026 | 16 | 10 | [47abe7f](https://github.com/SAP-docs/sap-datasphere/commit/47abe7f) |

## Hinweise

- Ältere Blogs und SAP Notes nennen noch 10 parallele Jobs. Für Tenants, die vor September 2025 konfiguriert wurden,
  regelt SAP Note 3649926 die Erhöhung (Notiz aus früherer Recherche, Note-Text hier nicht archiviert).
- Seite: [Sizing, Capacity Planning and Load Balancing for Replication Flow](https://github.com/SAP-docs/sap-datasphere/blob/main/docs/Acquiring-Preparing-Modeling-Data/Acquiring-and-Preparing-Data-in-the-Data-Builder/sizing-capacity-planning-and-load-balancing-for-replication-flow-5a3419f.md)
