# Research log — Morocco (MAR)

## Run parameters

| Parameter | Value |
|---|---|
| Country | Morocco |
| ISO3 | MAR |
| Framework | `GPC_Data_Availability_Framework.xlsx` (23 subsectors) |
| Prompt | `coverage_research.md` |
| Languages searched | English, French (Arabic portal labels as encountered) |
| Date | 2026-08-06 |

## Process

1. Parsed Excel framework into 23 GPC subsector requirements (Essential Activity + Direct Emissions columns).
2. Searched official portals and operators: data.gov.ma, HCP, MEM, ONEE, ANRE, NARSA, ONCF, ONDA, ANP, TMPA, MAPMDREF/ANEF, MTEDD, UNFCCC NIR.
3. Added international/modeled gap-fills: EDGAR, Climate TRACE, GFW, ESA WorldCover, FAOSTAT, Global Power Plant Database.
4. Documented 30 dataset records with required metadata fields.
5. Mapped every subsector; explicit **No suitable dataset identified** where warranted.

## Outputs

| File | Content |
|---|---|
| `00_context_MAR.md` | Country brief & institutions |
| `01_datasets_MAR.csv` | Dataset inventory (metadata) |
| `02_coverage_by_subsector_MAR.md` | Requirement → dataset mapping |
| `03_gaps_MAR.md` | Explicit gaps list |
| `06_log_MAR.md` | This log |

## Evidence notes

- NIR 2024 PDF verified on UNFCCC (document 645214).
- ONDA statistics page lists monthly Excel downloads including year 2025.
- NARSA organization page on data.gov.ma lists vehicle registration datasets.
- Lydec AMMC filings disclose Casablanca electricity GWh — rare city-scale public utility volume.
- data.gov.ma homepage theme counters sometimes show 0 in UI scrapes; dataset URLs above still resolve to published packages (portal UX inconsistency — do not treat as empty catalogue).

## Limitations of this pass

- Not every municipal open-data portal (all communes) was exhaustively crawled.
- Some operator microdata likely exists under restricted/commercial access and is correctly marked Restricted/not identified rather than invented.
- License fields often “Not identified” when reuse terms were not explicit on the landing page.
