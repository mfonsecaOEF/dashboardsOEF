# Research log — United Kingdom (GBR)

## Run parameters

| Parameter | Value |
|---|---|
| Country | United Kingdom |
| ISO3 | GBR |
| Framework | `GPC_Data_Availability_Framework.xlsx` (23 subsectors) |
| Prompt | `coverage_research.md` (+ expanded CSV format used for ETH/MAR/PHL/CAN) |
| Languages | English (+ DA product awareness) |
| Date | 2026-08-06 |

## Outputs

| File | Content |
|---|---|
| `00_context_GBR.md` | Country brief |
| `01_datasets_GBR.csv` | 25 datasets → **141 rows** (1 sector/row + I.6 gap) |
| `02_coverage_by_subsector_GBR.md` | Subsector mapping |
| `03_gaps_GBR.md` | Gaps |
| `06_log_GBR.md` | This log |

## Format notes

Same schema as ETH/MAR/PHL/CAN:
- `related_gpc_sector` (singular)
- `row_id` (e.g. `GBR-001-I.1`)
- `NO-COVERAGE-{sector}` for uncovered sectors
- Sorted by GPC code

## Comparative note

Among MAR / ETH / PHL / CAN / GBR, the UK is strongest for **local-authority-ready** official products (DESNZ LA GHG + subnational meters + DfT LA traffic + WasteDataFlow). Canada remains very strong on facility GHGRP and published city inventories; UK’s differentiator is systematic national LA emissions tables for every authority.
