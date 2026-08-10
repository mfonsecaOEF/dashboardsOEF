# Coverage by CCRA indicator — United Kingdom (GBR)

Dataset rows: `01_datasets_GBR.csv` (111 rows; 37 datasets + 1 gap)

## Summary

| Metric | Value |
|---|---|
| Indicators with ≥1 dataset | **40 / 41** |
| Hard gap (asset coverage) | `CCRA-039` stormwater network coverage |
| Soft gap | `CCRA-007` disease case GIS |
| OEF screening | 10 (`GBR-A028`–`A037`) |
| Standouts | **EA NaFRA/RoFRS/RoFSW/NCERM**, **ONS+IMD LSOA**, **UKCP18**, **DESNZ fuel poverty** |

## Theme status

| Theme | Primary sources |
|---|---|
| E/V | ONS Census 2021 LSOA + IMD + fuel poverty |
| Flood Threat | EA RoFRS + RoFSW + Flood Zones (+ climate change) |
| SLR / coast | NCERM + UKCP18 marine + RoFRS sea |
| Heat / drought | UKCP18 / HadUK-Grid + OEF heat_hazard |
| Landslide | BGS GeoSure (+ OEF) |
| Energy | DESNZ LSOA meters + fuel poverty |
| Stormwater assets | **GAP** (RoFSW = related hazard proxy) |

## Practical city v1 stack (GBR)

1. **E/V:** ONS LSOA + IMD (+ fuel poverty) → OEF shared scores  
2. **H flood:** EA RoFRS + RoFSW (+ CC layers)  
3. **H coastal:** NCERM + sea flood  
4. **H heat:** OEF heat_hazard + UKCP18  
5. **H landslide:** BGS or OEF  
6. **R:** OEF H×E×V (optionally wire EA H)
