# Research log — Minnesota, USA (USA-MN)

## Run parameters

| Parameter | Value |
|---|---|
| Jurisdiction | Minnesota (U.S. state) |
| Package code | `USA-MN` |
| Framework | `GPC_Data_Availability_Framework.xlsx` (23 subsectors) |
| Prompt | `coverage_research.md` (same schema as CAN/CRI) |
| Languages | English |
| Date | 2026-08-10 |
| Intent | Full mitigation package as **state-scale benchmark** for city GHGI readiness |

## Outputs

| File | Content |
|---|---|
| `00_context_USA-MN.md` | Jurisdiction brief |
| `01_datasets_USA-MN.csv` | 26 datasets → **137 rows** (incl. I.6 + I.7 gaps) |
| `02_coverage_by_subsector_USA-MN.md` | Subsector mapping |
| `03_gaps_USA-MN.md` | Gaps |
| `04_state_vs_country_lessons_USA-MN.md` | Does the method still work at state scale? |
| `06_log_USA-MN.md` | This log |

## Format notes

Same schema as country packages:
- `related_gpc_sector` (singular)
- `row_id` (e.g. `MN-001-I.1`)
- `NO-COVERAGE-{sector}` for uncovered sectors
- Sorted by GPC code
- `granularity_class` uses `state_or_province` for Minnesota state products

## Comparative note

Among packages in this research set, Minnesota is closest to **Canada / Costa Rica** for city-product maturity (published city + metro inventories) and **stronger than most countries** on open **city VMT**. It should **not** enter the 9-country Program priority table without an explicit product decision to score U.S. states as a jurisdiction class.
