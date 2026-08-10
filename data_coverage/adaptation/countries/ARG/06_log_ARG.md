# Research log — Argentina (ARG) CCRA / adaptation

| Date | Action |
|---|---|
| 2026-08-10 | Started ARG adaptation package |
| 2026-08-10 | Searched (ES/EN): INDEC Censo 2022 radios/NBI/EPH, Portal Geoestadístico, INA flood, SINAGIR, CABA/AMBA inundación, SMN + CN projections, SHN/SLR, SEGEMAR, CNA 2018, UMSEF bosques, SIB/APN, CAMMESA/BEN, AySA/ENGIRSU/CEAMSE, IGN/OSM, OEF screening |
| 2026-08-10 | Noted federated flood + constructed energy poverty; elevated OEF flood role vs GBR/AUS |
| 2026-08-10 | Kept `NO-COVERAGE` for stormwater asset coverage |
| 2026-08-10 | Wrote context/CSV/coverage/gaps/log |

## Decisions

- Prefer **INDEC radio + NBI** as E/V backbone (no SEIFA/IMD).
- Prefer **INA/provincial/municipal flood** when open; else **OEF + JRC/WRI**.
- Prefer **SMN/CN** for climate citation; OEF heat for urban UHI.
- Treat OEF as core packaging + flood gap-fill + heat UHI + landslide open fallback.
- Keep stormwater asset coverage as explicit hard gap.
