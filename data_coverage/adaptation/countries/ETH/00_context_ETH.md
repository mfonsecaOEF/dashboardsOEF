# Country context — Ethiopia (ETH) — CCRA / adaptation

| Parameter | Value |
|---|---|
| Country | Ethiopia / ኢትዮጵያ |
| ISO3 | ETH |
| Official languages for search | Amharic, English (+ regional languages as needed) |
| National statistical office | Ethiopian Statistical Service (ESS; formerly CSA) |
| Interactive stats | [IMIS Ethiopia](http://imisethiopia.gov.et/), ESS StatBank |
| Meteorology | National Meteorology Agency (NMA) |
| Environment / forests | EPA; Ethiopian Forestry Development (EFD); EWCA (protected areas) |
| Humanitarian data hub | [HDX Ethiopia](https://data.humdata.org/group/eth) |
| Reference cities | Addis Ababa, Dire Dawa, Hawassa, Bahir Dar, Mekelle, Adama |
| Geography note | **Landlocked** — no national seaport / SLR coastline; Ethio–Djibouti corridor critical for logistics |
| Research date | 2026-08-10 |
| Framework used | `geospatial-data/docs/climate_risk_indicators_by_sector.json` (41 unique CCRA indicators) |

## Institutional map (priority providers)

| Domain | Key providers |
|---|---|
| Population / poverty / housing | ESS/CSA, COD-PS (HDX), HCES/LSMS, DHS |
| Admin boundaries | COD-AB (HDX) |
| Climate / drought / heat | NMA (authoritative, mostly restricted); CHIRPS / ERA5 / SPEI gap-fills |
| Floods | HDX Climada/Floodbase footprints; JRC/WRI; OEF flood_hazard/FRI |
| Landslides | National/regional academic + GSE studies; NASA LHASA; OEF landslide_hazard |
| Biodiversity | WDPA / KBA; EWCA (docs) |
| Agriculture / irrigation | ESS AgSS; FAO WaPOR/AQUASTAT |
| Energy | EEU / MoWE / MTF (energydata.info); WRI power plants |
| Health facilities | healthsites.io / HDX; MoH DHIS2 (restricted) |
| OEF city CCRA screening | flood / heat / landslide H + E/V + R (+ mechanism types) |

## Structural notes for city CCRA

1. **ESS/COD-PS + WorldPop** are the practical E backbone; last full census is **2007**, so projections/dasymetrics matter.
2. **DHS / HCES** carry most open WASH, poverty, and energy-poverty proxies — not city-block rasters.
3. **NMA is authoritative** for climate but not an open city-ready raster portal — CHIRPS/ERA5/SPEI are the operational open hazard stack.
4. **Flood & landslide open national portals are thin**; HDX footprints + global models + OEF screening fill the gap. Highland landslide literature is rich but GIS rarely bulk-open.
5. **Sea-level rise is not applicable** on Ethiopian territory (landlocked) — explicit gap `CCRA-035`.
6. **OEF screening (flood/heat/landslide)** is pipeline-ready for ETH cities; not yet published in catalog (same note as MAR).
