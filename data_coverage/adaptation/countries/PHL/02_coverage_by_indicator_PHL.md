# Coverage by CCRA indicator — Philippines (PHL)

Framework: 41 unique indicators  
Dataset rows: `01_datasets_PHL.csv` (122 rows; 43 datasets + 1 explicit gap row)

## Summary

| Metric | Value |
|---|---|
| Indicators with ≥1 usable dataset | **40 / 41** |
| Explicit hard gap | 1 (`CCRA-039` stormwater) |
| Soft gap | `CCRA-007` disease (NDHS prevalence only) |
| Unique datasets | 43 |
| OEF screening products | 10 (`PHL-A034`–`A043`) |
| Standout national assets | **Project NOAH** + **PSA barangay census** + **PAGASA CliMap** |

## Indicator highlights

| Theme | Status |
|---|---|
| Flood Threat | **NOAH** primary; JRC/WRI/OEF secondary |
| Landslide Threat/Susceptibility | **NOAH** primary; LHASA/OEF secondary |
| Sea level / coastal | NASA/IPCC SLR + **NOAH storm surge** + PPA/OSM ports |
| Heat / precip / drought | PAGASA CliMap + drought/SPEI; CHIRPS/ERA5; **OEF heat_hazard** for urban LST |
| Population / age / WASH | PSA CPH 2020 barangay / city — city-ready |
| Income / energy poverty | PSA poverty + HECS/DOE |
| Agriculture / irrigation | PSA/DA + NIA/WaPOR |
| Stormwater drainage | **GAP** (mechanism proxy only) |

## OEF screening listed

| ID | Product | Role vs NOAH/PAGASA |
|---|---|---|
| PHL-A034 | FRI present+SSP | Futures complement |
| PHL-A035 | Flood Hazard | Ensemble cross-check (NOAH preferred) |
| PHL-A036 | Heat Hazard | Urban LST (fills municipal-average CliMap) |
| PHL-A037 | Landslide Hazard | Cross-check (NOAH preferred) |
| PHL-A038–A040 | Risk H×E×V | Composite with PSA E/V (± NOAH H) |
| PHL-A041–A042 | Shared E/V | Barangay-fed scores |
| PHL-A043 | Mechanism-type | Incl. drainage_constrained proxy |

## Practical city v1 stack (PHL)

1. **H flood/landslide/surge:** Project NOAH  
2. **H heat:** OEF heat_hazard (+ PAGASA CliMap for official climate)  
3. **E/V:** PSA barangay census + poverty/WASH → OEF shared scores  
4. **R:** OEF H×E×V (optionally wire NOAH H)  
5. **SLR futures:** NASA/IPCC + NOAH surge for extremes  
6. **Flag:** stormwater unknown; disease surveillance GIS closed
