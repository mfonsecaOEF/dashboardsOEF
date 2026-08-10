# Coverage by CCRA indicator — Ethiopia (ETH)

Framework: 41 unique indicators from `climate_risk_indicators_by_sector.json`  
Dataset rows: see `01_datasets_ETH.csv` (114 rows; 41 datasets + 2 explicit gaps)

## Summary

| Metric | Value |
|---|---|
| Indicators with ≥1 dataset | 39 / 41 |
| Explicit gaps | 2 (`CCRA-035` SLR landlocked; `CCRA-039` stormwater) |
| Unique datasets mapped | 41 |
| Of which OEF screening products | 10 (`ETH-A032`–`A041`) |
| Strongest official E/V | ESS/COD-PS + DHS/HCES |
| Hazard open stack | CHIRPS / SPEI / ERA5 + HDX flood footprints + OEF H/R |

## Indicator status (short)

| ID | Indicator | Best grain | Primary sources | Notes |
|---|---|---|---|---|
| CCRA-001 | Age Distribution | modeled_grid | WorldPop age-sex; COD-PS; OEF V | — |
| CCRA-002 | Agricultural GDP share | national | National accounts; AgSS | Downscale |
| CCRA-003 | Agricultural establishment density | state_or_province | AgSS | City-weak |
| CCRA-004 | Agricultural land area | modeled_grid | WorldCover; AgSS; WaPOR | — |
| CCRA-005 | Areas of global conservation value | facility_or_asset | KBA; WDPA | — |
| CCRA-006 | BII | modeled_grid | NHM BII | Global |
| CCRA-007 | Confirmed disease cases | state_or_province | DHS prevalence (weak) | Soft gap — not surveillance GIS |
| CCRA-008 | Dependence on large-scale irrigation | modeled_grid | WaPOR; AgSS | — |
| CCRA-009 | Electricity consumption | other_or_mixed | EEU/MoWE/MTF | City meters thin |
| CCRA-010 | Energy poverty | state_or_province | MTF; HCES | — |
| CCRA-011 | Flood Threat Index | modeled_grid | **OEF flood_hazard**; Climada; JRC/WRI; FRI | Pipeline-ready |
| CCRA-012 | Food production and marketing | state_or_province | AgSS | — |
| CCRA-013–014 | Forest cover / loss | modeled_grid | Hansen | — |
| CCRA-015 | Health and basic services access | city / survey | COD-PS/DHS; HDX | — |
| CCRA-016 | Health facility density | facility_or_asset | healthsites; OSM; HDX | MoH registry closed |
| CCRA-017 | Households in hazard-prone areas | modeled_grid | Buildings ∩ H + pop; OEF risk | — |
| CCRA-018–019 | Sanitation / water access | survey / city | DHS; COD-PS housing | — |
| CCRA-020 | Income | state_or_province | HCES/LSMS | SAE woreda uneven |
| CCRA-021 | Industrial GDP share | national | National accounts | Downscale |
| CCRA-022–023 | Landslide Susceptibility / Threat | modeled_grid | **OEF landslide_hazard**; LHASA; national studies | Highlands priority |
| CCRA-024–025 | CDD / Rx5day | modeled_grid | CHIRPS | — |
| CCRA-026 | Maximum temperature | modeled_grid | **OEF heat_hazard**; ERA5 HWM | Configure season |
| CCRA-027 | Natural vegetation cover | modeled_grid | WorldCover / DW / Hansen | — |
| CCRA-028 | Population density | modeled_grid | WorldPop; GHSL; COD-PS; OEF E | Shared E core |
| CCRA-029 | Port infrastructures | facility_or_asset | OSM dry ports / rail corridor | Landlocked proxy only |
| CCRA-030 | Power generation facilities | facility_or_asset | WRI GPPDB | Hydro-sensitive |
| CCRA-031 | Protected areas | facility_or_asset | WDPA | — |
| CCRA-032 / 034 | Rail / road density | facility_or_asset | OSM | — |
| CCRA-033 | Relative humidity | modeled_grid | ERA5-Land | — |
| CCRA-035 | Sea Level change | **GAP** | — | Landlocked N/A |
| CCRA-036–037 | SPEI / precip | modeled_grid | SPEI/HDX drought; CHIRPS; NMA restricted | — |
| CCRA-038 | Urban infra social vulnerability | neighborhood | HCES + housing + OSM; OEF V | — |
| CCRA-039 | Urban stormwater drainage | **GAP** | — | Municipal GIS not found |
| CCRA-040 | Waste Collection | city_or_municipality | Census/housing proxies | Facility tonnage thin |
| CCRA-041 | Water security index | modeled_grid | Aqueduct proxy | — |

## OEF screening products listed

| ID | Product |
|---|---|
| ETH-A032 | FRI (CHIRPS–COPDEM, present+SSP) |
| ETH-A033 | Flood Hazard Score |
| ETH-A034 | Heat Hazard Score |
| ETH-A035 | Landslide Hazard Score |
| ETH-A036–A038 | Risk H×E×V (flood / heat / landslide) |
| ETH-A039–A040 | Shared Exposure + Vulnerability |
| ETH-A041 | Mechanism-type (F/H/L) |

## Practical city v1 stack (ETH)

1. **E/V:** OEF scores ← WorldPop/COD-PS + DHS/HCES age & poverty/WASH  
2. **H:** OEF flood / heat / landslide hazard (run per city AOI)  
3. **R:** OEF H×E×V  
4. **Validate:** NMA, HDX flood footprints, national landslide studies where GIS obtainable  
5. **Skip SLR** on ETH territory; treat dry-port/corridor exposure separately if product needs logistics risk
