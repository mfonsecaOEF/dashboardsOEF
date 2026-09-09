# Research log — Philippines (PHL)

## Run parameters

| Parameter | Value |
|---|---|
| Country | Philippines |
| ISO3 | PHL |
| Framework | `GPC_Data_Availability_Framework.xlsx` (23 subsectors) |
| Prompt | `coverage_research.md` |
| Languages | English (+ Filipino terms as encountered) |
| Date | 2026-08-06 |

## Process

1. Same method as MAR/ETH runs.
2. Prioritized DOE Power Statistics & KES, PSA OpenSTAT, CCC/NICCDIES/BTR1, LTO, PPA, CAAP, NSWMC/EMB, NAMRIA/FMB, Quezon City inventory, Meralco, plus EDGAR/Climate TRACE/FAOSTAT/GFW.
3. Documented 24 datasets; mapped all 23 subsectors; recorded gaps. The LCCAP community inventory manual (PHL-015) was later withdrawn from the catalogue because it is guidance, not a dataset (2026-09-09).

## Classification pass (2026-09-09)

Added `data_tier` and `usage_type` to `01_datasets_PHL.csv`. Applied by `dataset_id`, not by opening source files.

| Rule | Applied to |
|---|---|
| `usage_type` = validation | Official inventories for specific years: BTR1 (PHL-001), national GHGI brief (PHL-002), Quezon City GPC inventory (PHL-014) |
| `usage_type` = alternative international | Climate TRACE (PHL-020); FAOSTAT/GFW (PHL-021); GPPD (PHL-022). EDGAR (PHL-019) stays in this class but is **downscaling baseline only**, not a primary source (see below). |
| `usage_type` = local source | Philippine activity products (DOE, PSA, LTO, PPA, utilities, NAMRIA, etc.) |
| `data_tier` = Local + activity-based | Local activity stats and official inventories compiled from activity methods |
| `data_tier` = International + activity-based | GPPD; FAOSTAT + GFW / WorldCover |
| `data_tier` = International / global + downscaled | EDGAR; Climate TRACE |
| Left blank | `NO-COVERAGE` (I.6) |

No PHL dataset mapped to **Local + downscaled** (no local gridded/downscaled emissions product in the catalogue).

## EDGAR role (OEF–C40/GCOM, August 2026)

Workshop of 14 August 2026. OEF and C40/GCOM agreed:

> EDGAR data will be used as a downscaling baseline only (not primary source): OEF/GCOM will use EDGAR city/national coefficients to downscale national UNFCCC inventories for cities without local data, acknowledging methodological limitations.

Applied in `01_datasets_PHL.csv` to PHL-019 (`short_description`, `limitations`). `data_tier` remains **International / global + downscaled**; `usage_type` remains **alternative international**.

## Outputs

| File | Content |
|---|---|
| `00_context_PHL.md` | Country brief |
| `01_datasets_PHL.csv` | Dataset inventory |
| `02_coverage_by_subsector_PHL.md` | Subsector mapping |
| `03_gaps_PHL.md` | Gaps |
| `06_log_PHL.md` | This log |

## Comparative note (vs MAR / ETH)

- **Stronger than both** on open electricity sales by sector/region (DOE) and port statistics (PPA).
- **Stronger institutional GHG system** (EO 174 + BTR1 + published LGU inventory for Quezon City).
- **City inventory published** for Quezon City (like Addis for ETH; unlike MAR’s thinner city GHG publications).
- Shared gaps: VKT, municipal fuels, landfill APIs, F-gases, Scope 3 CB.
