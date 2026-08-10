# Coverage by CCRA indicator — México (MEX)

Dataset rows: `01_datasets_MEX.csv` (95 rows; 33 datasets + 1 gap)

## Summary

| Metric | Value |
|---|---|
| Indicators with ≥1 dataset | **40 / 41** |
| Hard gap (asset coverage) | `CCRA-039` stormwater network coverage |
| Soft gap | `CCRA-007` disease case GIS |
| OEF screening | 10 (`MEX-A028`–`A037`) |
| Standouts | **INEGI AGEB/manzana**, **CONEVAL GRS**, **CENAPRED ANR flood + laderas**, **SMN/INECC** |

## Theme status

| Theme | Primary sources |
|---|---|
| E/V | INEGI Censo 2020 AGEB/manzana + CONEVAL GRS/pobreza |
| Flood Threat | CENAPRED ANR + atlas estatales/municipales |
| SLR / coast | INECC coastal vulnerability + AR6 |
| Heat / drought | SMN/INECC + Monitor de Sequía + OEF heat_hazard |
| Landslide | CENAPRED susceptibilidad de laderas (+ OEF) |
| Energy | BNE/SIE + Census/CONEVAL proxies |
| Stormwater assets | **GAP** (do not use Census drenaje) |

## Practical city v1 stack (MEX)

1. **E/V:** INEGI AGEB + CONEVAL GRS → OEF shared scores  
2. **H flood:** CENAPRED ANR (+ municipal atlas); OEF as fill/futures  
3. **H coastal:** INECC/AR6 for coastal cities  
4. **H heat:** OEF heat_hazard + SMN/INECC  
5. **H landslide:** CENAPRED laderas (primary)  
6. **R:** OEF H×E×V (optionally wire CENAPRED H)
