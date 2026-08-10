# Country context — Morocco (MAR) — CCRA / adaptation

| Parameter | Value |
|---|---|
| Country | Morocco / Maroc / المغرب |
| ISO3 | MAR |
| Official languages for search | Arabic, French (+ English for international sources) |
| National statistical office | Haut-Commissariat au Plan (HCP) |
| Open data portal | [data.gov.ma](https://www.data.gov.ma/) |
| Meteorology | Direction Générale de la Météorologie (DGM / Météo Maroc) |
| Water / floods | Agences de Bassins Hydrauliques (ABH) + Ministère de l’Intérieur |
| Forests / protected areas | ANEF / Eaux et Forêts; MTEDD |
| Remote sensing | Centre Royal de Télédétection Spatiale (CRTS) |
| Reference cities (illustrative) | Casablanca, Rabat–Salé, Marrakech, Tangier, Agadir |
| Research date | 2026-08-10 |
| Framework used | `geospatial-data/docs/climate_risk_indicators_by_sector.json` (41 unique CCRA indicators) |

## Institutional map (priority providers)

| Domain | Key providers |
|---|---|
| Population / poverty / housing | HCP (RGPH 2024, pauvreté multidimensionnelle) |
| Admin boundaries | HCP → COD-AB on HDX |
| Climate / drought / heat | DGM (authoritative, mostly restricted); CHIRPS / ERA5 / SPEI gap-fills |
| Floods | ABH AZI (partial national coverage); Tensift web atlas; JRC/WRI/OEF FRI gap-fills |
| Landslides | No national open susceptibility GIS found; NASA LHASA + DEM drivers |
| Sea-level / coast | NASA/IPCC SLR + coastal DEM; ANP ports |
| Biodiversity | WDPA / KBA; ANEF PDAP-SIBE (docs); BII global |
| Agriculture / irrigation | data.gov.ma; MAPMDREF; research parcel ground-truth |
| Infrastructure | OSM; WRI power plants; ANP; ONEE/ANRE (partial) |
| Humanitarian composites | HDX HeiGIT ADM2 risk indicators |
| OEF city CCRA screening | `geospatial-data` flood / heat / landslide H + E/V + R (+ mechanism types); FRI/HWM input catalogs |

## Structural notes for city CCRA

1. **HCP RGPH 2024 is the strongest official E/V backbone** (population, age, housing/services), but bulk city-grid extracts are weaker than interactive commune tables.
2. **DGM drought/heat products are authoritative but not openly gridded** for city pipelines — CHIRPS/ERA5/SPEI are the practical open hazard stack (same pattern as GPC relying on EDGAR for spatialization).
3. **Flood AZI is the right official hazard**, but national open coverage is still incomplete; basin viewers (e.g. Tensift) and global flood rasters are needed for national city screening.
4. **No national open landslide susceptibility map** was found — only regional academic studies + global NASA LHASA / DEM.
5. **Two hard gaps in this pass:** confirmed disease cases (open geospatial) and urban stormwater drainage coverage.
6. **OEF screening products (flood / heat / landslide H + risk + shared E/V + mechanisms)** are listed as first-class datasets (`MAR-A034`–`A043`): methodology and global inputs exist; Moroccan city AOI publishes are not in the catalog yet.
