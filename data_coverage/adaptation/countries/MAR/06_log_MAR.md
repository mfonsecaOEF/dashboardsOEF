# Research log — Morocco (MAR) CCRA / adaptation

| Date | Action |
|---|---|
| 2026-08-10 | Created adaptation research track under `projects/data_coverage/adaptation/` |
| 2026-08-10 | Derived checklist from `geospatial-data/docs/climate_risk_indicators_by_sector.json` → 41 unique indicators (`00_indicator_checklist.csv`) |
| 2026-08-10 | Searched FR/EN: HCP RGPH 2024, poverty mapping, data.gov.ma, ABH AZI / Tensift atlas, DGM drought, HDX COD-AB / WorldPop / HeiGIT risk indicators, WDPA/KBA, CHIRPS/ERA5/SPEI, JRC/WRI flood, NASA LHASA, SLR, OSM, WRI power plants, agri irrigation ground-truth |
| 2026-08-10 | Cross-walked OEF `geospatial-data/catalog/datasets.yaml` hazard products (CHIRPS Rx*, ERA5 HWM, FRI, GHSL, Hansen, DEM) as allowed international gap-fills |
| 2026-08-10 | Wrote `countries/MAR/` package: context, datasets CSV (97 rows), coverage, gaps |
| 2026-08-10 | Added OEF screening products flood/heat/landslide H + R + shared E/V + mechanism types (`MAR-A035`–`A043`); clarified FRI as `MAR-A034` → CSV now 121 rows |

## Search terms (sample)

- `RGPH 2024 resultats2024.rgphapps.ma`
- `Atlas zones inondables ABH Tensift`
- `Maroc pauvreté multidimensionnelle HCP`
- `Morocco HDX risk assessment indicators`
- `CHIRPS SPEI Morocco drought`
- `NASA LHASA Morocco landslide`
- `WDPA Morocco aires protégées`
- `crop irrigation ground-truth Morocco`

## Decisions

- Collapse Present/2030/2050 JSON variants into one conceptual indicator; record horizons on dataset rows.
- Treat global modeled rasters as first-class gap-fills (parallel to EDGAR/Climate TRACE in GPC work).
- Emit explicit `NO-COVERAGE-*` rows for disease cases and stormwater drainage.
