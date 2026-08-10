# GPC / mitigation — product comparison layer

Derived from `mitigation/countries/*/01_datasets_*.csv` for decision-making views.

## Files

| File | Product use |
|---|---|
| `01_country_summary.csv` | Leaderboard: score, covered/missing subsectors, top 3 datasets, notes |
| `02_country_x_sector_counts.csv` | Wide matrix `country × I.1…VI.1` = dataset counts (spreadsheet heatmap) |
| `03_country_x_sector_status.csv` | Same matrix with readable cells: `9 · city-ready`, `2 · needs downscaling (national)`, `missing` |
| `04_country_sector_detail.csv` | Country page by sector: granularity label + top 3 datasets + downscaling flag |
| `05_top_datasets_by_country_sector.csv` | Drill-down list of top datasets per country×sector |

Also: each country `01_datasets_*.csv` now has `granularity_class` next to `geographic_granularity`.

## Suggested UI / Notion / Sheets views

1. **Compare countries** → `01` + heatmap from `02`/`03`
2. **Open a country** → filter `04` by `iso3`
3. **Decide which datasets matter** → `05` or original country CSV
4. **Filter “where we need downscaling”** → `04` where `needs_city_downscaling = yes`

## Granularity classes (human labels)

| Class | Meaning for city GHGIs |
|---|---|
| `neighborhood_or_small_area` | City-ready (LSOA/MSOA/postcode) |
| `city_or_municipality` | City-ready (LA / LGA / cantón / municipality) |
| `facility_or_asset` | Point sources inside cities (not full community inventory) |
| `state_or_province` | Needs downscaling to city |
| `national` | Needs downscaling to city |
| `modeled_grid` | Cross-check / gap-fill only (EDGAR, Climate TRACE, etc.) |

## Caveats

- Counts = number of mapped datasets for that subsector (not quality-weighted).
- `city_ready` uses best granularity among datasets in the sector (heuristic).
- Tier/score currently from the research synthesis; can be recalibrated with product.
