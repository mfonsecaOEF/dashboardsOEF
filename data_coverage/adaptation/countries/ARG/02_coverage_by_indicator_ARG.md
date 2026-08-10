# Coverage by CCRA indicator — Argentina (ARG)

Dataset rows: `01_datasets_ARG.csv` (96 rows; 34 datasets + 1 gap)

## Summary

| Metric | Value |
|---|---|
| Indicators with ≥1 dataset | **40 / 41** |
| Hard gap (asset coverage) | `CCRA-039` stormwater network coverage |
| Soft gap | `CCRA-007` disease case GIS |
| OEF screening | 10 (`ARG-A028`–`A037`) |
| Standouts | **INDEC radio + NBI**, **CNA/UMSEF/APN**, **SMN/CN**, **CAMMESA**; flood more OEF/global-dependent |

## Theme status

| Theme | Primary sources |
|---|---|
| E/V | INDEC Censo 2022 radios + NBI (+ EPH in agglomerations) |
| Flood Threat | INA/provincial/municipal studies + JRC/WRI + OEF |
| SLR / coast | SHN + AR6 + local sudestada/coastal studies |
| Heat / drought | SMN/CN + CHIRPS/ERA5 + OEF heat_hazard |
| Landslide | SEGEMAR (+ OEF for Andes/Sierras) |
| Energy | BEN/CAMMESA + Census proxies |
| Stormwater assets | **GAP** |

## Practical city v1 stack (ARG)

1. **E/V:** INDEC radio + NBI → OEF shared scores  
2. **H flood:** Municipal/INA where open; else OEF flood_hazard + JRC  
3. **H coastal (AMBA/coast):** SHN/AR6 + local sudestada maps  
4. **H heat:** OEF heat_hazard (DJF) + SMN  
5. **H landslide:** SEGEMAR or OEF (skip on flat Pampa if irrelevant)  
6. **R:** OEF H×E×V
