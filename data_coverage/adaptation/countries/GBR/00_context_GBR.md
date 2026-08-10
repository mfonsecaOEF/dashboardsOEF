# Country context — United Kingdom (GBR) — CCRA / adaptation

| Parameter | Value |
|---|---|
| Country | United Kingdom |
| ISO3 | GBR |
| Languages searched | English (devolved portals noted) |
| Statistics | ONS (+ NRS / NISRA / Welsh Government) |
| Open data | [data.gov.uk](https://www.data.gov.uk) / Defra Data Services Platform |
| Flood / coastal | Environment Agency NaFRA / RoFRS / RoFSW / NCERM (England); SEPA / NRW / DfI parallels |
| Climate | Met Office UKCP18 / HadUK-Grid |
| Reference cities | London, Manchester, Birmingham, Glasgow, Cardiff, Belfast |
| Research date | 2026-08-10 |
| Framework | `climate_risk_indicators_by_sector.json` (41 CCRA indicators) |

## Institutional map

| Domain | Key providers |
|---|---|
| Population / deprivation | ONS Census 2021 LSOA; IMD/IoD (nation-specific) |
| Flood (fluvial/tidal) | EA RoFRS + Flood Map for Planning (+ CC) |
| Flood (pluvial) | EA RoFSW (+ CC) |
| Coastal erosion / SLR | NCERM 2024; UKCP18 marine |
| Landslide | BGS GeoSure (+ OEF complement) |
| Climate / drought / heat | UKCP18; HadUK-Grid; OEF heat_hazard |
| Energy / fuel poverty | DESNZ subnational meters + fuel poverty LSOA |
| Agri / forest / PA | Defra; Forest Research NFI; Natural England et al. |
| OEF screening | F/H/L H+R + shared E/V (pipeline-ready) |

## Structural notes

1. **Among the strongest CCRA stacks globally in this set** — EA open flood+coastal with UKCP18 futures + ONS/IMD LSOA E/V.
2. **Devolution matters:** many flagship layers are **England**; use SEPA/NRW/DfI for Scotland/Wales/NI.
3. **RoFSW ≠ stormwater asset coverage** — keep coverage gap; use RoFSW as related hazard.
4. **Fuel poverty LSOA** is a rare direct Energy poverty product.
5. BGS GeoSure may be **licence-gated** for bulk GIS — OEF landslide_hazard as open fallback.
