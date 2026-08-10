# CCRA / adaptation data availability research

Framework (do not redesign):

[`geospatial-data/docs/climate_risk_indicators_by_sector.json`](../../../geospatial-data/docs/climate_risk_indicators_by_sector.json)

Supporting checklist (derived, unique conceptual indicators):

- `00_indicator_checklist.csv` — one row per indicator (`CCRA-001` …)
- `00_indicator_occurrences.csv` — full Sector × Climatic risk × Component × Index expansion

## Objective

Identify publicly available datasets in **[COUNTRY]** that can operationalize the CCRA indicators for **city-scale climate risk assessment** (Hazard × Exposure × Vulnerability).

Do **not** invent new indicators. Use the JSON as the checklist.

For every indicator in `00_indicator_checklist.csv`:

1. Determine whether one or more datasets exist
2. Identify the most authoritative source
3. Identify alternatives / gap-fills when appropriate
4. Document metadata
5. If none found, emit an explicit gap row: `NO-COVERAGE-{indicator_id}`

## Unit of analysis

- **Primary key:** `related_ccra_indicator` = `CCRA-NNN` (unique conceptual indicator; Present/2030/2050 collapsed)
- Tag `sectors_served` / `climatic_risks_served` / `risk_components` from the checklist
- Note whether present and/or future horizons are covered in `horizons_covered`

## Search strategy

Search in:

- English
- Official language(s) of the country

Prioritize:

1. National statistical office / census
2. Meteorological / hydrological agencies
3. Civil protection / basin agencies / environment ministry
4. Municipal / regional open data
5. Utilities / infrastructure operators
6. Universities / research institutes
7. NGOs / humanitarian (HDX)
8. International / global rasters (explicitly allowed as gap-fills, like EDGAR was for GPC)

Search for both:

- **Observed / statistical** datasets
- **Modeled / remote-sensing** hazard & land-cover products

## Output package (per country)

Under `countries/{ISO3}/`:

| File | Purpose |
|------|---------|
| `00_context_{ISO3}.md` | Institutions, languages, city references |
| `01_datasets_{ISO3}.csv` | One row per dataset × indicator (plus gap rows) |
| `02_coverage_by_indicator_{ISO3}.md` | Checklist coverage summary |
| `03_gaps_{ISO3}.md` | Missing / weak indicators |
| `06_log_{ISO3}.md` | Search log |

## CSV columns (`01_datasets_*.csv`)

```text
indicator_name,
dataset_id,
row_id,
dataset_name,
publisher,
dataset_type,          # Hazard | Exposure | Vulnerability | Hybrid | Boundary | Other
information_requirements_satisfied,
related_ccra_indicator,
sectors_served,
climatic_risks_served,
risk_components,
geographic_coverage,
geographic_granularity,
granularity_class,     # neighborhood_or_small_area | city_or_municipality | facility_or_asset | state_or_province | national | modeled_grid | other_or_mixed | unknown
horizons_covered,      # present | present;2030;2050 | n/a | …
temporal_coverage,
update_frequency,
data_format,
open_restricted,
license,
api_available,
download_url,
documentation_url,
short_description,
limitations,
confidence_level,      # High | Medium | Low
authoritative_tier     # Primary official | Secondary official | Research/NGO | International modeled | OEF derived screening | Gap
```

Also always include **OEF CCRA screening products** from `geospatial-data` when they operationalize an indicator — even if not yet published for that country’s cities:

- `flood_hazard` / `flood_risk` (+ FRI inputs)
- `heat_hazard` / `heat_risk` (+ HWM/LST inputs)
- `landslide_hazard` / `landslide_risk`
- shared `exposure_score` / vulnerability score
- optional `nbs_*_mechanism_type`

Mark geographic coverage as **pipeline-ready for city AOIs** when catalog publishes exist only for other countries (POA/MN examples).

## Granularity guidance (city CCRA)

Prefer city-usable grain:

1. `modeled_grid` / `neighborhood_or_small_area` / `facility_or_asset`
2. `city_or_municipality` (commune / municipalité)
3. `state_or_province` (needs downscaling)
4. `national` (needs downscaling)

Do not classify phrases like “no city boundary” as city-ready.
