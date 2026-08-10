# Research log — Ethiopia (ETH) CCRA / adaptation

| Date | Action |
|---|---|
| 2026-08-10 | Started ETH adaptation package under `projects/data_coverage/adaptation/countries/ETH/` |
| 2026-08-10 | Searched EN: ESS/CSA COD-PS & COD-AB, DHS/HCES/LSMS, NMA, HDX risk indicators & Climada flood footprints, Global Drought Hazard/SPEI, national landslide susceptibility literature, WDPA/KBA, AgSS, WaPOR, healthsites, EEU/MTF, WRI power plants, OSM |
| 2026-08-10 | Included full OEF screening family (FRI + flood/heat/landslide H + R + shared E/V + mechanisms) as pipeline-ready for ETH cities |
| 2026-08-10 | Explicit gaps: `CCRA-035` (landlocked N/A), `CCRA-039` (stormwater) |
| 2026-08-10 | Wrote context, datasets CSV (114 rows), coverage, gaps, log |

## Search terms (sample)

- `Ethiopia COD-PS COD-AB HDX`
- `Ethiopia DHS water sanitation HDX`
- `Ethiopia Climada flood footprint`
- `Ethiopia landslide susceptibility national`
- `NMA Ethiopia climate drought`
- `ESS Agricultural Sample Survey`
- `WaPOR Ethiopia irrigation`

## Decisions

- Treat **SLR as explicit N/A gap** (not force-fit coastal products).
- Keep **CCRA-007** as soft-covered via DHS with strong limitation (not a hard NO-COVERAGE).
- Map **port infrastructures** to dry-port/rail corridor OSM proxy with clear landlocked caveat.
- Mirror MAR: always list OEF screening even if ETH city publishes are not in catalog yet.
