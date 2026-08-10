# Research log — Australia (AUS) CCRA / adaptation

| Date | Action |
|---|---|
| 2026-08-10 | Started AUS adaptation package |
| 2026-08-10 | Searched: ABS Census 2021 SA1, SEIFA 2021, ASGS Ed.3, AFRIP/GA flood studies, state flood portals, DEA WOfS, BOM climate + NPR/NWA, CCiA/NCRA, CoastAdapt/Canute, GA landslide DB, ABARES CLUM + Ag Census, CAPAD, AES/AER/AEMO–CER, OSM/Microsoft buildings, OEF screening |
| 2026-08-10 | Noted federated flood (AFRIP ≠ seamless national layer) and constructed energy poverty |
| 2026-08-10 | Kept `NO-COVERAGE` for stormwater asset coverage despite WOfS/flood proxies |
| 2026-08-10 | Wrote context/CSV/coverage/gaps/log |

## Decisions

- Prefer **ABS SA1 + SEIFA** as E/V backbone (IMD/ACS analogue).
- Prefer **AFRIP + state flood portals + WOfS** as Flood Threat path; OEF flood_hazard as gap-fill.
- Prefer **BOM + CCiA/NCRA** for climate/drought citation; OEF heat for urban UHI.
- Treat OEF as pipeline packaging + heat UHI + landslide open fallback.
- Keep stormwater asset coverage as explicit hard gap.
