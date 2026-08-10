# Unified coverage metrics

Derived from `mitigation/` + `adaptation/` country packages using
[`../coverage_metrics_spec.md`](../coverage_metrics_spec.md).

| File | Contents |
|---|---|
| `coverage_by_country_cell.csv` | Country × track × GPC/CCRA cell metrics |
| `coverage_by_country_dataset.csv` | Country × track × dataset rollup |
| `coverage_country_summary.csv` | Country-level mitigation + adaptation + program approach |

Regenerate:

```bash
python scripts/compute_coverage_metrics.py
```

Requires pandas (e.g. streamlit_app `.venv`).
