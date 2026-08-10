# Country context — Argentina (ARG) — CCRA / adaptation

| Parameter | Value |
|---|---|
| Country | Argentina |
| ISO3 | ARG |
| Languages searched | Spanish, English |
| Statistics | INDEC (Censo 2022 radios; NBI; EPH) |
| Open data | [datos.gob.ar](https://datos.gob.ar) / Portal Geoestadístico INDEC |
| Flood / DRM | INA; provincial studies; SINAGIR; CABA/AMBA open layers |
| Climate | SMN + Comunicaciones Nacionales / proyecciones |
| Coastal / SLR | SHN + AR6 + sudestada / coastal studies (Río de la Plata) |
| Reference cities | CABA, Rosario, Córdoba, Mendoza, AMBA municipios |
| Research date | 2026-08-10 |
| Framework | `climate_risk_indicators_by_sector.json` (41 CCRA indicators) |

## Institutional map

| Domain | Key providers |
|---|---|
| Population / poverty | INDEC Censo 2022 radios; NBI; EPH (aglomerados) |
| Flood | INA + provincial flood studies; municipal inundación; SINAGIR |
| Coastal / SLR | SHN; IPCC AR6; local sudestada/coastal studies |
| Landslide | SEGEMAR (+ OEF; relevant Andean/Sierras) |
| Climate / drought / heat | SMN; CN projections; CHIRPS/ERA5; OEF heat_hazard |
| Energy | BEN / CAMMESA / ENRE–ENARGAS; Census energy proxies |
| Agri / forest / PA | CNA 2018 + MAGyP; UMSEF bosques; SIB/APN |
| Water / waste | AySA & utilities; ENGIRSU / CEAMSE (AMBA) |
| OEF screening | F/H/L H+R + shared E/V (pipeline-ready) |

## Structural notes

1. **Radio censal + NBI** is the E/V backbone (no SEIFA/IMD). Strong for WASH/age; income finer via EPH only in agglomerations.
2. Flood hazard is **federated/patchy** — OEF flood_hazard + JRC/WRI matter more than in GBR/AUS.
3. **AMBA/CABA** have richer open risk layers than interior cities.
4. **Hard gap:** stormwater drainage *coverage* (pipe %). Pluvial inundation ≠ asset inventory.
5. Energy poverty is **constructed** from Census NBI/housing + BEN aggregates.
