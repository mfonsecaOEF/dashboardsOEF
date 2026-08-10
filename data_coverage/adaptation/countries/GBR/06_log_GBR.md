# Research log — United Kingdom (GBR) CCRA / adaptation

| Date | Action |
|---|---|
| 2026-08-10 | Started GBR adaptation package |
| 2026-08-10 | Searched: ONS Census 2021 LSOA, IMD/IoD2025, EA RoFRS/RoFSW/Flood Zones/NCERM (NaFRA 2024), UKCP18/HadUK-Grid, BGS GeoSure, DESNZ fuel poverty & subnational energy, Defra agri, Natural England sites, OEF screening |
| 2026-08-10 | Mapped RoFSW as related to stormwater but kept `NO-COVERAGE` for asset coverage |
| 2026-08-10 | Noted England-centric EA products + devolved parallels |
| 2026-08-10 | Wrote context/CSV/coverage/gaps/log |

## Decisions

- Prefer **EA NaFRA family** as primary Flood Threat (not OEF).
- Prefer **ONS+IMD+fuel poverty** as V stack.
- Treat OEF as pipeline packaging + urban heat LST + landslide open fallback.
- Keep stormwater asset coverage as explicit gap despite RoFSW.
