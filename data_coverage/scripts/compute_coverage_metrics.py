#!/usr/bin/env python3
"""Compute unified coverage metrics from mitigation + adaptation country packages.

Reads data_coverage/{mitigation,adaptation}/countries/*/01_datasets_*.csv
(in the dashboardsOEF repo) and comparison qualitative scores.
Writes comparison_unified/*.csv per coverage_metrics_spec.md.
"""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "comparison_unified"
YEAR_MIN, YEAR_MAX = 2015, 2024
YEAR_WINDOW = list(range(YEAR_MIN, YEAR_MAX + 1))
N_YEARS = len(YEAR_WINDOW)

GPC_REFS = [
    "I.1", "I.2", "I.3", "I.4", "I.5", "I.6", "I.7", "I.8",
    "II.1", "II.2", "II.3", "II.4", "II.5",
    "III.1", "III.2", "III.3", "III.4",
    "IV.1", "IV.2",
    "V.1", "V.2", "V.3",
    "VI.1",
]

COUNTRIES = ["ARG", "AUS", "CAN", "CRI", "ETH", "GBR", "MAR", "MEX", "PHL"]

TIER_RANK = {"T1": 1, "T2": 2, "T3": 3}
APPROACH_RANK = {"City-ready": 0, "Extra work": 1, "Accept downscaling": 2, "Insufficient": 3}

T1_TIERS = {
    "primary official",
    "primary official / utility",
    "national program",
    "national program / cantonal",
    "utility",
    "secondary official",
}
T2_TIERS = {
    "international modeled",
    "international",
    "international compiled",
    "oef derived screening",
    "open government",
}
T3_TIERS = {
    "research/ngo",
}


def map_tier(auth: str) -> str | None:
    s = str(auth or "").strip().lower()
    if not s or s == "gap" or s == "nan":
        return None
    if s in T1_TIERS:
        return "T1"
    if s in T2_TIERS:
        return "T2"
    if s in T3_TIERS:
        return "T3"
    # fallbacks
    if "primary" in s or "official" in s or "utility" in s or "national program" in s:
        return "T1"
    if "modeled" in s or "oef" in s or "international" in s:
        return "T2"
    if "research" in s or "ngo" in s or "proxy" in s:
        return "T3"
    return "T3"


def is_gap_row(row: pd.Series) -> bool:
    did = str(row.get("dataset_id", "") or "")
    auth = str(row.get("authoritative_tier", "") or "")
    name = str(row.get("dataset_name", "") or "")
    if did.upper().startswith("NO-COVERAGE"):
        return True
    if auth.strip().lower() == "gap":
        return True
    if "no suitable dataset" in name.lower():
        return True
    return False


def parse_years(text: object, horizons: object = None) -> set[int]:
    """Best-effort year extraction for research temporal_coverage / horizons strings."""
    years: set[int] = set()

    def _consume(s: str) -> None:
        nonlocal years
        if not s or not str(s).strip() or str(s).lower() == "nan":
            return
        s = str(s)

        # Ranges: 2015-2021, 2015–2030, 2010–presente
        range_pat = re.compile(
            r"(20\d{2}|19\d{2})\s*[–\-—/]\s*(20\d{2}|19\d{2}|presente|present|ongoing|actual|hoy)",
            re.I,
        )
        for m in range_pat.finditer(s):
            start = int(m.group(1))
            end_raw = m.group(2)
            end = int(end_raw) if re.match(r"^\d{4}$", end_raw) else YEAR_MAX
            lo, hi = min(start, end), max(start, end)
            for y in range(lo, hi + 1):
                if YEAR_MIN <= y <= YEAR_MAX:
                    years.add(y)

        for m in re.finditer(r"\b(19\d{2}|20\d{2})\b", s):
            y = int(m.group(1))
            if YEAR_MIN <= y <= YEAR_MAX:
                years.add(y)

        ongoing = bool(
            re.search(
                r"\b(ongoing|presente|present|current|actual|mensual|continua|continúa|"
                r"aligned|climatology|pipeline-ready|updated|updates)\b",
                s,
                re.I,
            )
        )
        if ongoing and years:
            start = min(years)
            for y in range(start, YEAR_MAX + 1):
                years.add(y)
        elif ongoing and not years:
            years.add(YEAR_MAX)

        plus = re.search(r"(20\d{2})\s*\+", s)
        if plus:
            start = int(plus.group(1))
            for y in range(max(start, YEAR_MIN), YEAR_MAX + 1):
                years.add(y)

        # horizons like present;2030;2050 → count present as current year in window
        if re.search(r"\bpresent\b", s, re.I):
            years.add(YEAR_MAX)

    _consume(text)
    _consume(horizons)
    return years


def is_city_ready_grain(granularity_class: object, track: str) -> bool:
    g = str(granularity_class or "").strip().lower()
    if g in {"neighborhood_or_small_area", "city_or_municipality", "facility_or_asset"}:
        return True
    # Adaptation: modeled grids count as screening-ready for hazards
    if track == "adaptation" and g == "modeled_grid":
        return True
    return False


def band_for(coverage_pct: float, year_pct: float, t1_t2_pct: float) -> tuple[str, str]:
    if coverage_pct >= 0.80 and year_pct >= 0.50 and t1_t2_pct >= 0.70:
        return "Viable — scale-friendly", "City-ready"
    if coverage_pct >= 0.60 and year_pct >= 0.30:
        return "Viable — extra work", "Extra work"
    if coverage_pct >= 0.40:
        return "Constrained — accept downscaling", "Accept downscaling"
    return "Insufficient", "Insufficient"


def worse_approach(a: str, b: str) -> str:
    # Insufficient folds into Accept downscaling for program language
    def norm(x: str) -> str:
        return "Accept downscaling" if x == "Insufficient" else x

    a, b = norm(a), norm(b)
    return a if APPROACH_RANK[a] >= APPROACH_RANK[b] else b


def load_checklist_names() -> tuple[dict[str, str], dict[str, str]]:
    gpc_names: dict[str, str] = {}
    # from any mitigation detail
    detail = pd.read_csv(ROOT / "mitigation/comparison/04_country_sector_detail.csv")
    for _, r in detail.drop_duplicates("related_gpc_sector").iterrows():
        gpc_names[str(r["related_gpc_sector"])] = str(r["sector_name"])

    adp = pd.read_csv(ROOT / "adaptation/00_indicator_checklist.csv")
    ccra_names = dict(zip(adp["indicator_id"].astype(str), adp["indicator_name"].astype(str)))
    return gpc_names, ccra_names


def load_qual_scores() -> pd.DataFrame:
    mit = pd.read_csv(ROOT / "mitigation/comparison/01_country_summary.csv")[
        ["iso3", "country", "score", "tier"]
    ].rename(columns={"score": "mit_qual_score", "tier": "mit_qual_tier"})
    adp = pd.read_csv(ROOT / "adaptation/comparison/01_country_summary.csv")[
        ["iso3", "score", "tier"]
    ].rename(columns={"score": "adp_qual_score", "tier": "adp_qual_tier"})
    return mit.merge(adp, on="iso3")


def load_na_indicators() -> dict[str, set[str]]:
    """Indicators marked n/a in adaptation detail (e.g. ETH SLR)."""
    path = ROOT / "adaptation/comparison/04_country_indicator_detail.csv"
    if not path.exists():
        return {}
    d = pd.read_csv(path)
    out: dict[str, set[str]] = {}
    if "coverage_status" not in d.columns:
        return out
    na = d[d["coverage_status"].astype(str).str.lower().isin(["n/a", "na"])]
    for iso, g in na.groupby("iso3"):
        out[str(iso)] = set(g["related_ccra_indicator"].astype(str))
    return out


def process_track(
    track: str,
    iso3: str,
    country: str,
    cells: list[str],
    cell_names: dict[str, str],
    cell_col: str,
    name_col: str,
    na_cells: set[str] | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    path = ROOT / track / "countries" / iso3 / f"01_datasets_{iso3}.csv"
    df = pd.read_csv(path)
    na_cells = na_cells or set()

    # dataset-level aggregation
    ds_rows = []
    cell_rows = []

    usable = df[~df.apply(is_gap_row, axis=1)].copy()
    usable["_tier"] = usable["authoritative_tier"].map(map_tier)
    horiz = usable["horizons_covered"] if "horizons_covered" in usable.columns else None
    if horiz is not None:
        usable["_years"] = [
            parse_years(t, h) for t, h in zip(usable["temporal_coverage"], horiz)
        ]
    else:
        usable["_years"] = usable["temporal_coverage"].map(parse_years)
    if "granularity_class" in usable.columns:
        usable["_city_ready"] = usable["granularity_class"].map(
            lambda g: is_city_ready_grain(g, track)
        )
    else:
        usable["_city_ready"] = False

    for cell in cells:
        if cell in na_cells:
            cell_rows.append(
                {
                    "iso3": iso3,
                    "country": country,
                    "track": track,
                    "cell_id": cell,
                    "cell_name": cell_names.get(cell, ""),
                    "covered": 0,
                    "years_covered": 0,
                    "year_frac": 0.0,
                    "best_tier": "",
                    "city_ready": 0,
                    "best_dataset_id": "",
                    "best_dataset_name": "",
                    "notes": "n/a (excluded from denominator)",
                    "_exclude_denom": True,
                }
            )
            continue

        sub = usable[usable[cell_col].astype(str) == cell]
        if sub.empty:
            cell_rows.append(
                {
                    "iso3": iso3,
                    "country": country,
                    "track": track,
                    "cell_id": cell,
                    "cell_name": cell_names.get(cell, ""),
                    "covered": 0,
                    "years_covered": 0,
                    "year_frac": 0.0,
                    "best_tier": "",
                    "city_ready": 0,
                    "best_dataset_id": "",
                    "best_dataset_name": "",
                    "notes": "no usable dataset / gap",
                    "_exclude_denom": False,
                }
            )
            continue

        # best tier
        sub = sub.copy()
        sub["_rank"] = sub["_tier"].map(lambda t: TIER_RANK.get(t or "T3", 9))
        best = sub.sort_values(["_rank", "dataset_id"]).iloc[0]
        years_union: set[int] = set()
        for ys in sub["_years"]:
            years_union |= set(ys)
        years_covered = len(years_union)
        city_ready = bool(sub["_city_ready"].any())
        cell_rows.append(
            {
                "iso3": iso3,
                "country": country,
                "track": track,
                "cell_id": cell,
                "cell_name": cell_names.get(cell, best.get(name_col, "")),
                "covered": 1,
                "years_covered": years_covered,
                "year_frac": years_covered / N_YEARS,
                "best_tier": best["_tier"] or "T3",
                "city_ready": int(city_ready),
                "best_dataset_id": best.get("dataset_id", ""),
                "best_dataset_name": best.get("dataset_name", ""),
                "notes": "",
                "_exclude_denom": False,
            }
        )

    # datasets
    if len(usable):
        for did, g in usable.groupby("dataset_id"):
            cells_touched = sorted({str(c) for c in g[cell_col].dropna().astype(str) if str(c) in cells})
            years_u: set[int] = set()
            for ys in g["_years"]:
                years_u |= ys
            tiers = [t for t in g["_tier"] if t]
            best_t = min(tiers, key=lambda t: TIER_RANK[t]) if tiers else "T3"
            ds_rows.append(
                {
                    "iso3": iso3,
                    "country": country,
                    "track": track,
                    "dataset_id": did,
                    "dataset_name": g.iloc[0].get("dataset_name", ""),
                    "publisher": g.iloc[0].get("publisher", ""),
                    "tier": best_t,
                    "cells_touched": ";".join(cells_touched),
                    "n_cells": len(cells_touched),
                    "years_contributed": ";".join(str(y) for y in sorted(years_u)),
                    "n_years": len(years_u),
                    "notes": "",
                }
            )

    cell_df = pd.DataFrame(cell_rows)
    ds_df = pd.DataFrame(ds_rows)

    active = cell_df[~cell_df["_exclude_denom"]]
    n = len(active)
    covered_n = int(active["covered"].sum())
    coverage_pct = covered_n / n if n else 0.0
    covered_cells = active[active["covered"] == 1]
    year_pct = float(covered_cells["year_frac"].mean()) if len(covered_cells) else 0.0
    if len(covered_cells):
        t1 = (covered_cells["best_tier"] == "T1").sum() / len(covered_cells)
        t2 = (covered_cells["best_tier"] == "T2").sum() / len(covered_cells)
        t3 = (covered_cells["best_tier"] == "T3").sum() / len(covered_cells)
    else:
        t1 = t2 = t3 = 0.0
    t1_t2 = t1 + t2
    city_ready_pct = (
        float(covered_cells["city_ready"].mean()) if len(covered_cells) else 0.0
    )
    band, approach = band_for(coverage_pct, year_pct, t1_t2)

    summary = {
        "coverage_pct": round(coverage_pct, 4),
        "year_pct": round(year_pct, 4),
        "t1_pct": round(t1, 4),
        "t2_pct": round(t2, 4),
        "t3_pct": round(t3, 4),
        "t1_t2_pct": round(t1_t2, 4),
        "city_ready_pct": round(city_ready_pct, 4),
        "n_cells": n,
        "n_covered": covered_n,
        "band": band,
        "approach": approach,
    }
    return cell_df.drop(columns=["_exclude_denom"]), ds_df, summary


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    gpc_names, ccra_names = load_checklist_names()
    ccra_ids = list(pd.read_csv(ROOT / "adaptation/00_indicator_checklist.csv")["indicator_id"].astype(str))
    qual = load_qual_scores()
    na_map = load_na_indicators()

    all_cells = []
    all_ds = []
    summaries = []

    for iso3 in COUNTRIES:
        country = qual.loc[qual["iso3"] == iso3, "country"].iloc[0]
        mit_cells, mit_ds, mit_s = process_track(
            "mitigation", iso3, country, GPC_REFS, gpc_names,
            "related_gpc_sector", "sector_name",
        )
        adp_cells, adp_ds, adp_s = process_track(
            "adaptation", iso3, country, ccra_ids, ccra_names,
            "related_ccra_indicator", "indicator_name",
            na_cells=na_map.get(iso3, set()),
        )
        all_cells.extend([mit_cells, adp_cells])
        all_ds.extend([mit_ds, adp_ds])

        program_approach = worse_approach(mit_s["approach"], adp_s["approach"])
        mit_q = int(qual.loc[qual["iso3"] == iso3, "mit_qual_score"].iloc[0])
        adp_q = int(qual.loc[qual["iso3"] == iso3, "adp_qual_score"].iloc[0])
        combined = round((mit_q + adp_q) / 2, 1)
        delta = adp_q - mit_q
        viable_ticket = 1 if mit_s["band"] == "Viable — scale-friendly" else 0
        viable_program_start = 1 if mit_s["approach"] in ("City-ready", "Extra work") else 0

        summaries.append(
            {
                "iso3": iso3,
                "country": country,
                "mit_coverage_pct": mit_s["coverage_pct"],
                "mit_year_pct": mit_s["year_pct"],
                "mit_t1_pct": mit_s["t1_pct"],
                "mit_t2_pct": mit_s["t2_pct"],
                "mit_t3_pct": mit_s["t3_pct"],
                "mit_t1_t2_pct": mit_s["t1_t2_pct"],
                "mit_city_ready_pct": mit_s["city_ready_pct"],
                "mit_n_covered": mit_s["n_covered"],
                "mit_n_cells": mit_s["n_cells"],
                "mit_band": mit_s["band"],
                "mit_approach": mit_s["approach"],
                "mit_qual_score": mit_q,
                "adp_coverage_pct": adp_s["coverage_pct"],
                "adp_year_pct": adp_s["year_pct"],
                "adp_t1_pct": adp_s["t1_pct"],
                "adp_t2_pct": adp_s["t2_pct"],
                "adp_t3_pct": adp_s["t3_pct"],
                "adp_t1_t2_pct": adp_s["t1_t2_pct"],
                "adp_city_ready_pct": adp_s["city_ready_pct"],
                "adp_n_covered": adp_s["n_covered"],
                "adp_n_cells": adp_s["n_cells"],
                "adp_band": adp_s["band"],
                "adp_approach": adp_s["approach"],
                "adp_qual_score": adp_q,
                "program_approach": program_approach,
                "combined_score": combined,
                "delta": delta,
                "viable_ticket": viable_ticket,
                "viable_program_start": viable_program_start,
                "notes": (
                    "Metrics derived from country 01_datasets CSVs per coverage_metrics_spec.md; "
                    "year_pct is best-effort from temporal_coverage text."
                ),
            }
        )

    cells_out = pd.concat(all_cells, ignore_index=True)
    ds_out = pd.concat([d for d in all_ds if len(d)], ignore_index=True)
    summary_out = pd.DataFrame(summaries)

    # sort summary like dashboard: approach then combined score
    summary_out["_ord"] = summary_out["program_approach"].map(
        lambda x: APPROACH_RANK.get(x, 9)
    )
    summary_out = summary_out.sort_values(
        ["_ord", "combined_score"], ascending=[True, False]
    ).drop(columns=["_ord"])

    cells_path = OUT / "coverage_by_country_cell.csv"
    ds_path = OUT / "coverage_by_country_dataset.csv"
    sum_path = OUT / "coverage_country_summary.csv"
    cells_out.to_csv(cells_path, index=False)
    ds_out.to_csv(ds_path, index=False)
    summary_out.to_csv(sum_path, index=False)

    # README for the folder
    (OUT / "README.md").write_text(
        """# Unified coverage metrics

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
""",
        encoding="utf-8",
    )

    print(f"Wrote {cells_path} ({len(cells_out)} rows)")
    print(f"Wrote {ds_path} ({len(ds_out)} rows)")
    print(f"Wrote {sum_path} ({len(summary_out)} rows)")
    print()
    print(summary_out[
        [
            "iso3",
            "mit_coverage_pct",
            "mit_year_pct",
            "mit_approach",
            "adp_coverage_pct",
            "adp_year_pct",
            "adp_approach",
            "program_approach",
            "combined_score",
            "viable_ticket",
        ]
    ].to_string(index=False))


if __name__ == "__main__":
    main()
