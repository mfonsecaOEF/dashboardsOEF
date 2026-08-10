# Coverage by CCRA indicator — Canada (CAN)

Dataset rows: `01_datasets_CAN.csv` (107 rows; 37 datasets + 1 gap)

## Summary

| Metric | Value |
|---|---|
| Indicators with ≥1 dataset | **40 / 41** |
| Hard gap | `CCRA-039` stormwater |
| Soft gap | `CCRA-007` disease (aggregates only) |
| OEF screening | 10 (`CAN-A028`–`A037`) |
| Standouts | **StatCan DA**, **NRCan flood susceptibility**, **CanCoast / CAN-EWLAT**, **ClimateData.ca** |

## Theme status

| Theme | Primary sources |
|---|---|
| E/V core | StatCan Census 2021 DA (age, LIM, housing) |
| Flood Threat | NRCan FS (+ future); CFM/FHIMP; OEF flood_hazard |
| Landslide | GSC/provincial + OEF landslide_hazard |
| Heat / drought / precip | ClimateData.ca; AAFC drought; OEF heat_hazard |
| SLR / ports | CanCoast; CAN-EWLAT; TC/ports; OSM |
| Agriculture | AAFC ACI + Census of Agriculture |
| Protected areas | CPCAD |
| Stormwater | **GAP** (mechanism proxy only) |

## Practical city v1 stack (CAN)

1. **E/V:** StatCan DA → OEF shared scores (same pattern as Plymouth ACS)  
2. **H flood:** NRCan FS (± CFM local maps) + optional OEF ensemble  
3. **H heat:** OEF heat_hazard + ClimateData.ca  
4. **H landslide:** OEF + local inventories  
5. **SLR:** CanCoast / CAN-EWLAT for coastal cities  
6. **R:** OEF H×E×V
