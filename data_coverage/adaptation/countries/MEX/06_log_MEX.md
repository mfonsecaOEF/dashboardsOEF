# Research log — México (MEX) CCRA / adaptation

| Date | Action |
|---|---|
| 2026-08-10 | Started MEX adaptation package |
| 2026-08-10 | Searched (ES/EN): INEGI Censo 2020 AGEB/manzana, CONEVAL GRS/pobreza AGEB, CENAPRED ANR flood & laderas, atlas estatales, CONAGUA sequía/puntos críticos, SMN/INECC, CONAFOR/CONANP, SIAP/Censo Agropecuario, SENER BNE/SIE, CLUES, OEF screening |
| 2026-08-10 | Explicitly separated Census drenaje (sanitation) from stormwater asset coverage gap |
| 2026-08-10 | Preferred CENAPRED as primary Flood/Landslide Threat over OEF |
| 2026-08-10 | Wrote context/CSV/coverage/gaps/log |

## Decisions

- Prefer **INEGI AGEB + CONEVAL GRS** as E/V backbone (IMD/SEIFA-class).
- Prefer **CENAPRED ANR** as primary Flood and Landslide Threat.
- Prefer **SMN/INECC** for climate citation; OEF heat for urban UHI; FRI for flood futures.
- Keep stormwater asset coverage as explicit hard gap; never equate Census drenaje with CCRA-039.
