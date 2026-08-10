# Country context — Canada (CAN) — CCRA / adaptation

| Parameter | Value |
|---|---|
| Country | Canada / Canada |
| ISO3 | CAN |
| Languages searched | English, French |
| National statistical office | Statistics Canada |
| Open data | [open.canada.ca](https://open.canada.ca) |
| Climate portal | [ClimateData.ca](https://climatedata.ca/) |
| Flood mapping | NRCan Flood Susceptibility; CFM inventory; FHIMP |
| Coastal / SLR | CanCoast; CAN-EWLAT (DFO) |
| Reference cities | Toronto, Vancouver, Montréal, Calgary, Ottawa |
| Research date | 2026-08-10 |
| Framework | `climate_risk_indicators_by_sector.json` (41 CCRA indicators) |

## Institutional map

| Domain | Key providers |
|---|---|
| Population / income / housing | StatCan Census 2021 DA profiles + boundary files |
| Flood | NRCan FS (historic/future); CFM; provincial FHIMP maps |
| Landslide | GSC / provincial inventories (uneven); OEF landslide_hazard |
| Climate / drought / heat | ClimateData.ca; AAFC/ECCC drought; CHIRPS/ERA5/OEF |
| Sea level / coast | CanCoast; CAN-EWLAT; port authorities |
| Agriculture | AAFC Annual Crop Inventory; Census of Agriculture |
| Forests / PA | CFS / CPCAD |
| Energy / power | CER; StatCan; WRI GPPDB |
| OEF screening | F/H/L H+R + shared E/V (MN pipeline is close analogue) |

## Structural notes

1. **Closest analogue to OEF MN CCRA:** StatCan **Dissemination Areas** ≈ ACS block groups for E/V.
2. **Flood:** national open **Flood Susceptibility** (+ futures) plus inventory of regulatory maps — strong, but not one seamless regulatory layer.
3. **SLR:** CanCoast + CAN-EWLAT are unusually strong official coastal products.
4. **Landslide** national open coverage weaker than flood — OEF fills city consistency.
5. Hard gap: **stormwater drainage coverage**; soft: disease case GIS.
