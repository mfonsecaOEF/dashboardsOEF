# Data coverage research

Country-by-country public-data availability research for **city-scale** climate products.

```text
data_coverage/                ← lives in CCRADiscovery (GitHub)
├── README.md                 ← this file
├── streamlit_app/            ← Streamlit Community Cloud entrypoint
├── mitigation/               ← GPC GHG inventories
│   ├── coverage_research.md
│   ├── GPC_Data_Availability_Framework.xlsx
│   ├── countries/{ISO3}/
│   └── comparison/
└── adaptation/               ← CCRA climate risk (H×E×V)
    ├── coverage_research.md
    ├── 00_indicator_checklist.csv
    ├── 00_indicator_occurrences.csv
    ├── countries/{ISO3}/
    └── comparison/
```

**Streamlit Cloud main file:** `data_coverage/streamlit_app/app.py`

## Tracks

| Track | Framework | Unit of analysis | Countries |
|---|---|---|---|
| **Mitigation** | `GPC_Data_Availability_Framework.xlsx` (23 GPC subsectors) | GPC subsector (`I.1` … `VI.1`) | ARG, AUS, CAN, CRI, ETH, GBR, MAR, MEX, PHL |
| **Adaptation** | `geospatial-data/docs/climate_risk_indicators_by_sector.json` (41 CCRA indicators) | `CCRA-001` … `CCRA-041` | Same 9 ISO3 |

## Per-country package

Both tracks use the same package shape under `countries/{ISO3}/`:

| File | Purpose |
|---|---|
| `00_context_{ISO3}.md` | Institutions, languages, reference cities |
| `01_datasets_{ISO3}.csv` | Dataset × sector/indicator rows (+ explicit gaps) |
| `02_coverage_by_*_{ISO3}.md` | Coverage summary |
| `03_gaps_{ISO3}.md` | Missing / weak areas |
| `06_log_{ISO3}.md` | Research log |

## Comparison layers

Each track has `comparison/`:

- Leaderboard CSV (`01_country_summary.csv`)
- Matrix CSVs (counts + status)
- Detail / top-datasets drill-downs
- `dashboard.html` (self-contained interactive view)
- `README.md` (how to use the layer)

Open:

- Mitigation: `mitigation/comparison/dashboard.html`
- Adaptation: `adaptation/comparison/dashboard.html`
- **Team-shareable Streamlit app:** `streamlit_app/` → see `streamlit_app/README.md` (Streamlit Community Cloud URL; no local repo needed for viewers)
