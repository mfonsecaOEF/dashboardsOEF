# CCRA / adaptation — product comparison layer

Derived from `adaptation/countries/*/01_datasets_*.csv` for decision-making views.

## Files

| File | Product use |
|---|---|
| `01_country_summary.csv` | Leaderboard: score, covered/missing indicators, top 3 datasets, notes |
| `02_country_x_indicator_counts.csv` | Wide matrix `country × CCRA-001…041` = dataset counts |
| `03_country_x_indicator_status.csv` | Same matrix with readable cells: `3 · city-ready`, `missing`, `n/a (landlocked)` |
| `02b_country_x_theme_counts.csv` | Compact heatmap matrix by **theme** (12 themes) |
| `03b_country_x_theme_status.csv` | Theme readiness status cells |
| `04_country_indicator_detail.csv` | Country page by indicator: granularity + top datasets + downscaling flag |
| `05_top_datasets_by_country_indicator.csv` | Drill-down list of top datasets per country×indicator |
| `dashboard.html` | Self-contained interactive leaderboard + theme matrix |

## Suggested UI / Notion / Sheets views

1. **Compare countries** → `01` + heatmap from `02b`/`03b` (or open `dashboard.html`)
2. **Open a country** → filter `04` by `iso3`
3. **Decide which datasets matter** → `05` or original country CSV
4. **Filter “where we need downscaling”** → `04` where `needs_city_downscaling = yes`
5. **Full indicator audit** → `02` / `03` (41 columns; wide for Sheets)

## Themes (dashboard heatmap)

| Theme | Indicators (roll-up) |
|---|---|
| E/V social | CCRA-001, 015, 016, 018, 019, 020, 028, 038, 040 |
| Flood threat | CCRA-011, 017, 039 |
| Landslide | CCRA-022, 023 |
| Heat | CCRA-026 |
| Drought / water | CCRA-024, 036, 008, 041 |
| Precip extremes | CCRA-025, 037, 033 |
| SLR / coast | CCRA-035, 029 |
| Food / agri | CCRA-002, 003, 004, 012 |
| Biodiversity | CCRA-005, 006, 013, 014, 027, 031 |
| Energy | CCRA-009, 010, 030 |
| Infra networks | CCRA-021, 032, 034 |
| Disease cases | CCRA-007 |

## Granularity classes (city CCRA)

| Class | Meaning for city CCRA |
|---|---|
| `neighborhood_or_small_area` | City-ready E/V (AGEB / SA1 / LSOA / barangay / radio / DA / distrito) |
| `city_or_municipality` | City-ready (LGA / cantón / municipality) |
| `facility_or_asset` | Point assets inside cities |
| `modeled_grid` | **City screening-ready** for hazards (unlike GPC, where modeled was usually gap-fill only) |
| `state_or_province` | Needs downscaling to city |
| `national` | Needs downscaling to city |

## Leaderboard (qualitative)

| Tier | Countries | Score band |
|---|---|---|
| A | GBR, MEX, PHL, AUS, CAN | 86–94 |
| B | CRI, ARG | 68–72 |
| C | MAR, ETH | 48–52 |

## Cross-cutting findings

- **Hard gap in all 9:** `CCRA-039` urban stormwater drainage *coverage* (pipe/network %). Flood/pluvial hazard ≠ asset inventory.
- **ETH only:** `CCRA-035` sea-level rise marked **n/a** (landlocked).
- **MAR only (extra):** `CCRA-007` confirmed disease cases also hard-gapped.

## Gap vs proxy rule

If a country CSV includes an explicit `NO-COVERAGE-*` / `authoritative_tier=Gap` row for an indicator, that indicator is counted as **missing** even when related proxy layers (e.g. RoFSW, OEF `drainage_constrained`) are also mapped. Proxies remain listed in `04`/`05` with `role=related_proxy`.

## Caveats

- Counts = number of mapped datasets for that indicator (not quality-weighted).
- `city-ready` uses best granularity among datasets (heuristic); OEF pipeline-ready products count.
- Tier/score from research synthesis + coverage structure; recalibrate with product if needed.
- Dashboard matrix is **theme-level**; use `02`/`03`/`04` for full indicator resolution.
