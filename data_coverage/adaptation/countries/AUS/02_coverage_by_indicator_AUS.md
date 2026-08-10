# Coverage by CCRA indicator — Australia (AUS)

Dataset rows: `01_datasets_AUS.csv` (102 rows; 36 datasets + 1 gap)

## Summary

| Metric | Value |
|---|---|
| Indicators with ≥1 dataset | **40 / 41** |
| Hard gap (asset coverage) | `CCRA-039` stormwater network coverage |
| Soft gap | `CCRA-007` disease case GIS |
| OEF screening | 10 (`AUS-A028`–`A037`) |
| Standouts | **ABS SA1 + SEIFA**, **AFRIP + state floods + WOfS**, **BOM/CCiA**, **CAPAD**, **BOM NPR water** |

## Theme status

| Theme | Primary sources |
|---|---|
| E/V | ABS Census 2021 SA1 + SEIFA IRSD/IRSAD |
| Flood Threat | AFRIP catalogue + state flood portals + DEA WOfS |
| SLR / coast | CoastAdapt / Canute / state coastal overlays |
| Heat / drought | BOM grids + CCiA/NCRA + OEF heat_hazard |
| Landslide | GA landslide DB (+ OEF) |
| Energy | AES/AER + AEMO–CER plants; poverty via Census/SEIFA |
| Stormwater assets | **GAP** (WOfS/flood = related hazard proxy) |

## Practical city v1 stack (AUS)

1. **E/V:** ABS SA1 + SEIFA → OEF shared scores  
2. **H flood:** State flood maps via AFRIP; WOfS where studies missing; OEF flood_hazard as fill  
3. **H coastal:** CoastAdapt / state coastal + SLR  
4. **H heat:** OEF heat_hazard (DJF) + BOM/CCiA  
5. **H landslide:** GA/state or OEF  
6. **R:** OEF H×E×V (optionally wire state flood H)
