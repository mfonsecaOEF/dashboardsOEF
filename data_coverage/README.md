# Data coverage research

**One question:** for each priority country, do we have enough **public city-scale data** for CityCatalyst — and **what program should we design?**

Mitigation (GPC) and adaptation (CCRA) are two checklists for that same decision.

```text
dashboardsOEF/data_coverage/       ← working copy (this repo)
├── README.md                      ← this file
├── coverage_metrics_spec.md       ← shared metrics + viability + program approach
├── scripts/compute_coverage_metrics.py
├── comparison_unified/            ← computed metrics for all 9 countries (both tracks)
├── streamlit_app/                 ← Data Coverage Assessment (both tracks)
├── mitigation/                    ← GPC evidence (23 subsectors)
│   ├── countries/{ISO3}/
│   └── comparison/
└── adaptation/                    ← CCRA evidence (41 indicators)
    ├── countries/{ISO3}/
    └── comparison/
```

## How the pieces fit

| Layer | Role |
|---|---|
| **Country packages** (`mitigation/`, `adaptation/`) | Evidence: datasets, gaps, logs |
| **Comparison CSVs / HTML** | Matrices and qualitative scores |
| **`coverage_metrics_spec.md`** | Shared quantitative rules (coverage × years × T1/T2/T3) for both tracks |
| **`comparison_unified/`** | Metrics computed for all 9 countries from the country packages |
| **Streamlit app** | Decision UI: priority order + **City-ready / Extra work / Accept downscaling** |

Do not treat mitigation research, adaptation research, and the metrics spec as three projects — they feed one country recommendation.

## Tracks (checklists)

| Track | Framework | Cells | Countries |
|---|---|---|---|
| **Mitigation** | `GPC_Data_Availability_Framework.xlsx` | `I.1` … `VI.1` (23) | ARG, AUS, CAN, CRI, ETH, GBR, MAR, MEX, PHL |
| **Adaptation** | `geospatial-data/docs/climate_risk_indicators_by_sector.json` | `CCRA-001` … `CCRA-041` (41) | Same 9 ISO3 |

## Per-country package

Same shape under each track’s `countries/{ISO3}/`:

| File | Purpose |
|---|---|
| `00_context_{ISO3}.md` | Institutions, languages, reference cities |
| `01_datasets_{ISO3}.csv` | Dataset × cell rows (+ explicit gaps) |
| `02_coverage_by_*_{ISO3}.md` | Coverage summary |
| `03_gaps_{ISO3}.md` | Missing / weak areas |
| `06_log_{ISO3}.md` | Research log |

## Comparison + app

- Mitigation: `mitigation/comparison/`
- Adaptation: `adaptation/comparison/`
- Shared decision app: `streamlit_app/` (also published via `dashboardsOEF`)
- Metrics / viability rules: [`coverage_metrics_spec.md`](./coverage_metrics_spec.md)
