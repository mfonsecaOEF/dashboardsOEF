# Coverage by CCRA indicator — Morocco (MAR)

Framework: 41 unique indicators from `climate_risk_indicators_by_sector.json`  
Dataset rows: see `01_datasets_MAR.csv` (121 rows; 43 datasets + 2 explicit gaps)

## Summary

| Metric | Value |
|---|---|
| Indicators with ≥1 dataset | 39 / 41 |
| Explicit gaps | 2 (`CCRA-007`, `CCRA-039`) |
| Unique datasets mapped | 43 |
| Of which OEF screening products | 10 (`MAR-A034`–`MAR-A043`) |
| Best grain mostly `modeled_grid` / `facility_or_asset` | Hazard + global E layers |
| Official local E/V strength | HCP RGPH 2024 + poverty mapping |

## Indicator status

| ID | Indicator | Best grain | Primary sources (short) | Notes |
|---|---|---|---|---|
| CCRA-001 | Age Distribution | modeled_grid | WorldPop age-sex; HCP RGPH; HDX ADM2 | City-ready via WorldPop; validate vs RGPH |
| CCRA-002 | Agricultural GDP share | national | data.gov.ma sector indicators | Needs downscaling |
| CCRA-003 | Agricultural establishment density | facility_or_asset | Research parcels; agriculture open data | Partial regional sample |
| CCRA-004 | Agricultural land area | modeled_grid | WorldCover/DW; open agri stats | EO + national stats |
| CCRA-005 | Areas of global conservation value | facility_or_asset | KBA; SIBE docs; WDPA | National SIBE GIS uneven |
| CCRA-006 | Biodiversity Intactness Index (BII) | modeled_grid | NHM/GEO BON BII | Global model |
| CCRA-007 | Confirmed disease cases | **GAP** | — | No open geospatial case dataset found |
| CCRA-008 | Dependence on large-scale irrigation | facility_or_asset | Crop/irrigation ground-truth (5 plains) | Not national census |
| CCRA-009 | Electricity consumption | other_or_mixed | ONEE/ANRE; data.gov.ma | City meters thin |
| CCRA-010 | Energy poverty | neighborhood_or_small_area | HCP poverty (proxy); ONEE | No direct energy-poverty microdata |
| CCRA-011 | Flood Threat Index | modeled_grid | **OEF flood_hazard**; ABH AZI; JRC/WRI; FRI | City screening pipeline-ready |
| CCRA-012 | Food production and marketing | facility_or_asset / national | Agri open data; research parcels | Mostly national |
| CCRA-013 | Forest cover | modeled_grid | Hansen; WorldCover | Argan/dryland caveats |
| CCRA-014 | Forest loss | modeled_grid | Hansen loss | — |
| CCRA-015 | Health and basic services access | neighborhood_or_small_area | HCP RGPH/poverty; HDX access | Strong census proxies |
| CCRA-016 | Health facility density | facility_or_asset | OSM; HCP establishment mapping | MoH master list not open GIS |
| CCRA-017 | Households in hazard-prone areas | modeled_grid | Buildings ∩ flood/SLR/landslide + pop | Composite method |
| CCRA-018 | Inadequate Sanitation | city_or_municipality | HCP RGPH housing | Commune tables |
| CCRA-019 | Inadequate water access | city / modeled | HCP RGPH; Aqueduct proxy | — |
| CCRA-020 | Income | neighborhood_or_small_area | HCP multidimensional poverty | Best local V proxy |
| CCRA-021 | Industrial GDP share | national | data.gov.ma | Needs downscaling |
| CCRA-022 | Landslide Susceptibility | modeled_grid | **OEF landslide_hazard**; NASA LHASA; DEM | City screening pipeline-ready |
| CCRA-023 | Landslide Threat Index | modeled_grid | **OEF landslide_hazard** (+ risk H×E×V) | Preferred OEF product |
| CCRA-024 | Maximum Consecutive Dry Days (CDD) | modeled_grid | CHIRPS-derived; DGM restricted | — |
| CCRA-025 | Maximum Precipitation 5 days (Rx5day) | modeled_grid | CHIRPS (OEF catalog) | — |
| CCRA-026 | Maximum temperature | modeled_grid | **OEF heat_hazard**; ERA5 HWM inputs | City LST ensemble preferred |
| CCRA-027 | Natural vegetation cover | modeled_grid | WorldCover / Dynamic World / Hansen | — |
| CCRA-028 | Population density | modeled_grid | WorldPop; GHSL; HCP | Shared E core |
| CCRA-029 | Port infrastructures | facility_or_asset | ANP stats; OSM; SLR context | — |
| CCRA-030 | Power generation facilities | facility_or_asset | WRI Global Power Plant DB | — |
| CCRA-031 | Protected areas | facility_or_asset | WDPA | ANEF SIPN richer but closed |
| CCRA-032 | Railroad density | facility_or_asset | OSM | — |
| CCRA-033 | Relative humidity | modeled_grid | ERA5-Land | — |
| CCRA-034 | Road density | facility_or_asset | OSM; national road km stats | — |
| CCRA-035 | Sea Level change | modeled_grid | NASA/IPCC SLR + coastal DEM | — |
| CCRA-036 | SPEI | modeled_grid | SPEIbase / ERA5–CHIRPS; DGM restricted | Prefer recomputed fine SPEI |
| CCRA-037 | Total precipitation | modeled_grid | CHIRPS; data.gov.ma means; DGM | — |
| CCRA-038 | Urban infrastructure social vulnerability | neighborhood_or_small_area | HCP poverty + housing + OSM | Composite |
| CCRA-039 | Urban stormwater drainage coverage | **GAP** | — | Municipal GIS not found open |
| CCRA-040 | Waste Collection | city_or_municipality | HCP housing/services proxies | Facility tonnage still thin |
| CCRA-041 | Water security index | modeled_grid | WRI Aqueduct (proxy) | No official open national index |

## Cross-cutting reusable stacks (city pipeline)

1. **Shared Exposure:** OEF E score (`MAR-A041`) fed by WorldPop/GHSL (+ buildings)  
2. **Shared Vulnerability:** OEF V score (`MAR-A042`) fed by HCP RGPH/poverty + age  
3. **Flood / Heat / Landslide screening:** OEF `flood_hazard` / `heat_hazard` / `landslide_hazard` + risk H×E×V (`MAR-A035`–`A040`)  
4. **Mechanism interpretation:** OEF NbS mechanism-type layers (`MAR-A043`)  
5. **Official validation:** ABH AZI (flood), DGM (climate), where open  
6. **Global inputs still listed:** CHIRPS, ERA5/HWM, FRI, JRC, LHASA, DEM

### OEF screening products explicitly listed

| ID | Product | Maps to |
|---|---|---|
| MAR-A034 | FRI (CHIRPS–COPDEM, present+SSP) | Flood threat input / futures |
| MAR-A035 | Flood Hazard Score | CCRA-011, 017 |
| MAR-A036 | Heat Hazard Score | CCRA-026 |
| MAR-A037 | Landslide Hazard Score | CCRA-022, 023 |
| MAR-A038 | Flood Risk H×E×V | CCRA-011, 017, 028 |
| MAR-A039 | Heat Risk H×E×V | CCRA-026, 028, 001 |
| MAR-A040 | Landslide Risk H×E×V | CCRA-022, 023, 017, 028 |
| MAR-A041 | Shared Exposure score | CCRA-028, 017 |
| MAR-A042 | Shared Vulnerability score | CCRA-001, 020, 038 |
| MAR-A043 | Mechanism-type (F/H/L) | CCRA-011, 026, 023, 039 |

Note: published catalog tiles today are POA/MN; for Morocco these are **pipeline-ready** once a city site config exists — not yet national MAR publishes.
