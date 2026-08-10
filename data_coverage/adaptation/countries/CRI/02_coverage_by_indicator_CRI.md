# Coverage by CCRA indicator — Costa Rica (CRI)

Dataset rows: `01_datasets_CRI.csv` (96 rows; 33 datasets + 1 gap)

## Summary

| Metric | Value |
|---|---|
| Indicators with ≥1 dataset | **40 / 41** |
| Hard gap (asset coverage) | `CCRA-039` stormwater network coverage |
| Soft gap | `CCRA-007` disease case GIS; neighbourhood V grain |
| OEF screening | 10 (`CRI-A028`–`A037`) |
| Standouts | **CNE/SNIT flood+landslide**, **IMN projections**, **SINAC ASP**, **SENARA/AyA water**; E/V mid |

## Theme status

| Theme | Primary sources |
|---|---|
| E/V | INEC distrito + Atlas DH IPM/IDH (cantón) |
| Flood Threat | CNE inundation-potential (SNIT) |
| SLR / coast | IMN/MINAE + AR6 |
| Heat / drought | IMN + OEF heat_hazard |
| Landslide | CNE (primary; high relevance) |
| Energy | ARESEP/ICE + Census proxies (low variance) |
| Stormwater assets | **GAP** |

## Practical city v1 stack (CRI)

1. **E/V:** INEC distrito (+ cantonal IPM cautiously) → OEF shared scores  
2. **H flood:** CNE SNIT inundation; OEF FRI for futures  
3. **H landslide:** CNE (primary)  
4. **H heat:** OEF heat_hazard + IMN  
5. **H coastal:** IMN/AR6 for coastal cantones  
6. **R:** OEF H×E×V (wire CNE H)
