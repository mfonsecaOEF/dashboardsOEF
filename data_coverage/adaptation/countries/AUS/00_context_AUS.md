# Country context — Australia (AUS) — CCRA / adaptation

| Parameter | Value |
|---|---|
| Country | Australia |
| ISO3 | AUS |
| Languages searched | English |
| Statistics | Australian Bureau of Statistics (ABS) |
| Open data | [data.gov.au](https://data.gov.au) |
| Flood | Geoscience Australia AFRIP + state SES/flood portals; DEA WOfS |
| Climate | BOM observational grids; Climate Change in Australia / NCRA (CSIRO–BoM) |
| Coastal / SLR | CoastAdapt / Canute / state coastal hazard overlays |
| Reference cities | Sydney, Melbourne, Brisbane, Perth, Adelaide, Canberra |
| Research date | 2026-08-10 |
| Framework | `climate_risk_indicators_by_sector.json` (41 CCRA indicators) |

## Institutional map

| Domain | Key providers |
|---|---|
| Population / disadvantage | ABS Census 2021 SA1; SEIFA (IRSD/IRSAD) |
| Flood | AFRIP / GA Flood Study Database; state flood portals; DEA WOfS |
| Coastal / SLR | CoastAdapt; Canute; GA coastal; state planning overlays |
| Landslide | GA National Landslide Database + state inventories (+ OEF) |
| Climate / drought / heat | BOM AGCD/AWAP; CCiA/NCRA; OEF heat_hazard (UHI) |
| Energy | AES / AER / AEMO–CER generators; energy poverty via Census+SEIFA |
| Agri / forest / PA | ABARES CLUM + Ag Census; SOFR/NFI; CAPAD |
| Water security | BOM NPR + National Water Account |
| OEF screening | F/H/L H+R + shared E/V (pipeline-ready) |

## Structural notes

1. **Strong city CCRA stack:** SA1 Census + SEIFA (IMD analogue) + AFRIP/state floods + BOM/CCiA futures.
2. Flood hazard is **federated** (like Canada FHIMP) — AFRIP catalogues studies; capital cities usually have state/LGA maps; WOfS fills observation gaps.
3. **No UK-style fuel poverty LSOA** — construct energy poverty from Census low-income / cooling + SEIFA + AES aggregates.
4. **Hard gap:** urban stormwater drainage *coverage* (pipe/network %). Surface inundation ≠ asset inventory.
5. Geoscape buildings often licensed — prefer OSM / Microsoft footprints for open exposure.
