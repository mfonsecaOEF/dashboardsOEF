"""
Data Coverage Assessment — Open Earth Foundation
Mitigation (GPC) + Adaptation (CCRA)

Shareable via Streamlit Community Cloud. Teammates only need the URL.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent  # data_coverage/
MIT = ROOT / "mitigation" / "comparison"
ADP = ROOT / "adaptation" / "comparison"
UNIFIED = ROOT / "comparison_unified"

TIER_COLORS = {"A": "#0f6b5c", "B": "#9a6b12", "C": "#8a3a32"}

# Human-readable decision labels (source tier stays A/B/C in CSVs)
TIER_QUALITY = {
    "A": "Strong data",
    "B": "Limited data",
    "C": "Sparse open data",
}
# Strategic framing: how to run a program — not yes/no gatekeeping
TIER_APPROACH = {
    "A": "City-ready",
    "B": "Extra work",
    "C": "Accept downscaling",
}
TIER_APPROACH_NOTE = {
    "A": "Public stack supports city-scale products with limited caveats — good for scale-style programs",
    "B": "Doable with partners + sector fills; expect some national→city downscaling",
    "C": "Still doable — plan for population/national downscaling and/or OEF modeled fills; accept lower city precision",
}
QUALITY_TO_TIER = {v: k for k, v in TIER_QUALITY.items()}
APPROACH_ORDER = {
    "City-ready": 0,
    "Extra work": 1,
    "Accept downscaling": 2,
    "Insufficient": 3,
}

# Score bands used in the research synthesis (approximate)
SCORE_BANDS = {
    "A": "≈80–100",
    "B": "≈60–79",
    "C": "≈0–59",
}

STATUS_ICONS = {
    "city-ready": "🟢",
    "facility": "🔵",
    "mixed": "🟣",
    "needs downscaling": "🟠",
    "missing": "🔴",
    "n/a": "⚪",
    "other": "⬜",
}

# Adaptation theme roll-ups (same as comparison layer)
ADP_THEMES = [
    ("EV_social", "E/V social", ["CCRA-001", "CCRA-015", "CCRA-016", "CCRA-018", "CCRA-019", "CCRA-020", "CCRA-028", "CCRA-038", "CCRA-040"]),
    ("Flood", "Flood threat", ["CCRA-011", "CCRA-017", "CCRA-039"]),
    ("Landslide", "Landslide", ["CCRA-022", "CCRA-023"]),
    ("Heat", "Heat", ["CCRA-026"]),
    ("Drought_water", "Drought / water", ["CCRA-024", "CCRA-036", "CCRA-008", "CCRA-041"]),
    ("Precip", "Precip extremes", ["CCRA-025", "CCRA-037", "CCRA-033"]),
    ("SLR_coast", "SLR / coast", ["CCRA-035", "CCRA-029"]),
    ("Food_agri", "Food / agri", ["CCRA-002", "CCRA-003", "CCRA-004", "CCRA-012"]),
    ("Biodiversity", "Biodiversity", ["CCRA-005", "CCRA-006", "CCRA-013", "CCRA-014", "CCRA-027", "CCRA-031"]),
    ("Energy", "Energy", ["CCRA-009", "CCRA-010", "CCRA-030"]),
    ("Infra", "Infra networks", ["CCRA-021", "CCRA-032", "CCRA-034"]),
    ("Health", "Disease cases", ["CCRA-007"]),
]
THEME_LABEL_TO_IDS = {label: ids for _, label, ids in ADP_THEMES}


@st.cache_data
def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def _tier_key(tier: str) -> str:
    return str(tier).strip().upper()


def tier_quality(tier: str) -> str:
    return TIER_QUALITY.get(_tier_key(tier), str(tier))


def tier_approach(tier: str) -> str:
    return TIER_APPROACH.get(_tier_key(tier), "—")


def tier_approach_note(tier: str) -> str:
    return TIER_APPROACH_NOTE.get(_tier_key(tier), "")


def worst_tier(mit_tier: str, adp_tier: str) -> str:
    """More demanding track wins (C > B > A) — sets the program design constraint."""
    rank = {"A": 0, "B": 1, "C": 2}
    m, a = _tier_key(mit_tier), _tier_key(adp_tier)
    return m if rank.get(m, 0) >= rank.get(a, 0) else a


def combined_approach(mit_tier: str, adp_tier: str) -> str:
    return tier_approach(worst_tier(mit_tier, adp_tier))


def delta_meaning(delta: float) -> str:
    if delta >= 10:
        return "Adaptation much stronger → prefer CCRA-first"
    if delta <= -10:
        return "Mitigation much stronger → prefer GPC-first"
    return "Balanced (±10) — similar readiness on both tracks"


def enrich_summary(summary: pd.DataFrame) -> pd.DataFrame:
    out = summary.copy()
    out["data_quality"] = out["tier"].map(tier_quality)
    out["approach"] = out["tier"].map(tier_approach)
    out["approach_note"] = out["tier"].map(tier_approach_note)
    return out.sort_values("score", ascending=False).reset_index(drop=True)


def status_key(cell: str) -> str:
    s = str(cell).lower()
    if s.startswith("missing") or s == "missing":
        return "missing"
    if "n/a" in s:
        return "n/a"
    if "city-ready" in s:
        return "city-ready"
    if "facility" in s:
        return "facility"
    if "downscaling" in s or "downscale" in s:
        return "needs downscaling"
    if "mixed" in s:
        return "mixed"
    return "other"


def decorate_status(val: str) -> str:
    return f"{STATUS_ICONS.get(status_key(val), '⬜')} {val}"


def soften_col(name: str) -> str:
    return (
        name.replace("_status", "")
        .replace("EV_social", "E/V social")
        .replace("Drought_water", "Drought / water")
        .replace("SLR_coast", "SLR / coast")
        .replace("Food_agri", "Food / agri")
        .replace("Precip", "Precip extremes")
        .replace("Flood", "Flood threat")
        .replace("Health", "Disease cases")
        .replace("Infra", "Infra networks")
        .replace("Biodiversity", "Biodiversity")
        .replace("Energy", "Energy")
        .replace("Landslide", "Landslide")
        .replace("Heat", "Heat")
    )


def unsoften_col(label: str, status_cols: list[str]) -> str | None:
    for col in status_cols:
        if soften_col(col) == label:
            return col
    return None


def selection_cells(event) -> list:
    if not event or not getattr(event, "selection", None):
        return []
    sel = event.selection
    if isinstance(sel, dict):
        return sel.get("cells", []) or []
    return getattr(sel, "cells", []) or []


def datasets_for_matrix_cell(
    track: str,
    iso3: str,
    col_label: str,
    status_cols: list[str],
    tops: pd.DataFrame,
    detail: pd.DataFrame,
) -> tuple[str, pd.DataFrame]:
    if track == "Mitigation":
        raw = unsoften_col(col_label, status_cols) or col_label
        sector = raw.replace("_status", "")
        sub = sector
        if "related_gpc_sector" in detail.columns:
            hit = detail[(detail["iso3"] == iso3) & (detail["related_gpc_sector"] == sector)]
            if len(hit) and "sector_name" in hit.columns:
                sub = f"{sector} — {hit.iloc[0]['sector_name']}"
                if "coverage_status" in hit.columns:
                    sub += f" · {hit.iloc[0]['coverage_status']}"
        t = tops[(tops["iso3"] == iso3) & (tops["related_gpc_sector"] == sector)].copy()
        if "rank_in_sector" in t.columns:
            t = t.sort_values("rank_in_sector")
        return sub, t

    indicator_ids = THEME_LABEL_TO_IDS.get(col_label, [])
    sub = ", ".join(indicator_ids) if indicator_ids else col_label
    t = tops[(tops["iso3"] == iso3) & (tops["related_ccra_indicator"].isin(indicator_ids))].copy()
    if len(t) and "dataset_id" in t.columns:
        if "rank" in t.columns:
            t = t.sort_values(["dataset_id", "rank"]).drop_duplicates("dataset_id", keep="first")
            t = t.sort_values("rank")
        else:
            t = t.drop_duplicates("dataset_id")
    return sub, t


def render_leaderboard(summary: pd.DataFrame, track: str) -> None:
    st.subheader("Priority ranking (easier → more constrained programs)")
    st.caption(
        "Ordered by score within approach. "
        "**City-ready** (≈80–100) · **Extra work** (≈60–79) · "
        "**Accept downscaling** (≈0–59) — still feasible; plan for lower city precision."
    )
    if summary.empty:
        st.info("No countries match the current filters.")
        return
    ranked = enrich_summary(summary)
    cols = st.columns(3)
    for i, (_, row) in enumerate(ranked.iterrows()):
        with cols[i % 3]:
            tier = str(row["tier"]).strip().upper()
            color = TIER_COLORS.get(tier, "#333")
            quality = tier_quality(tier)
            call = tier_approach(tier)
            covered_label = (
                f"{int(row['subsectors_covered'])}/23 subsectors"
                if track == "Mitigation"
                else f"{int(row['indicators_covered'])}/41 indicators"
            )
            city_ready = (
                row["city_ready_subsectors"]
                if track == "Mitigation"
                else row["city_ready_indicators"]
            )
            missing = (
                row.get("missing_sectors", "")
                if track == "Mitigation"
                else row.get("missing_indicators", "")
            )
            st.markdown(
                f"""
                <div style="background:#fff;border:1px solid #c5d2cc;border-radius:14px;
                            padding:14px 16px;margin-bottom:12px;box-shadow:0 8px 24px rgba(20,35,31,.06);">
                  <div style="font-size:.75rem;color:#5a6e68;font-weight:600;">#{i+1} · {row['iso3']}</div>
                  <div style="font-family:Georgia,serif;font-size:1.25rem;font-weight:650;margin:4px 0;">
                    {row['country']}
                  </div>
                  <div style="display:flex;align-items:baseline;gap:10px;margin:8px 0;flex-wrap:wrap;">
                    <span style="font-family:Georgia,serif;font-size:2rem;font-weight:650;color:#0b5f63;">
                      {int(row['score'])}
                    </span>
                    <span style="border:1px solid {color};color:{color};border-radius:999px;
                                 padding:2px 8px;font-size:.75rem;font-weight:700;">
                      {call}
                    </span>
                    <span style="color:#5a6e68;font-size:.78rem;font-weight:600;">{quality}</span>
                  </div>
                  <div style="font-size:.82rem;color:#5a6e68;line-height:1.45;">
                    <b style="color:#14231f;">{covered_label}</b> ·
                    <b style="color:#14231f;">{int(city_ready)}</b> city-ready ·
                    <b style="color:#14231f;">{int(row['unique_datasets'])}</b> datasets
                    {"<br/><span style='color:#8a3a32;'>Gaps: " + str(missing) + "</span>" if pd.notna(missing) and str(missing).strip() else ""}
                  </div>
                  <div style="margin-top:8px;font-size:.8rem;color:#0b5f63;line-height:1.35;">
                    <b>Approach:</b> {tier_approach_note(tier)}
                  </div>
                  <div style="margin-top:8px;font-size:.84rem;color:#5a6e68;line-height:1.4;">
                    {row['notes']}
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    with st.expander("How is the score calculated?"):
        render_score_methodology()


def render_matrix(
    status_df: pd.DataFrame,
    tops: pd.DataFrame,
    detail: pd.DataFrame,
    track: str,
    title: str,
    widget_key: str,
) -> None:
    st.subheader(title)
    st.caption(
        "Click a readiness cell to load datasets (like the HTML dashboard drawer). "
        "🟢 city-ready · 🔵 facility · 🟣 mixed · 🟠 needs downscaling · 🔴 missing · ⚪ n/a"
    )
    status_cols = [c for c in status_df.columns if c.endswith("_status")]
    if not status_cols or status_df.empty:
        st.info("No matrix rows for the current filters.")
        return

    show = status_df[["iso3", "country"] + status_cols].copy()
    rename_map = {c: soften_col(c) for c in status_cols}
    show = show.rename(columns=rename_map)
    display_cols = [rename_map[c] for c in status_cols]

    interactive = show.copy()
    for c in display_cols:
        interactive[c] = interactive[c].map(decorate_status)

    view = interactive.drop(columns=["iso3"])
    event = st.dataframe(
        view,
        use_container_width=True,
        height=420,
        hide_index=True,
        on_select="rerun",
        selection_mode="single-cell",
        key=widget_key,
    )

    cells = selection_cells(event)

    st.markdown("#### Cell datasets")
    if not cells:
        st.info("Select a matrix cell to load datasets.")
        return

    cell = cells[0]
    if isinstance(cell, dict):
        row_idx = cell.get("row")
        col_name = cell.get("column")
    else:
        row_idx, col_name = cell[0], cell[1]

    if col_name in ("country", "tier", None) or row_idx is None:
        st.info("Select a readiness cell (not the country name).")
        return

    row = show.iloc[int(row_idx)]
    iso3 = row["iso3"]
    country = row["country"]
    cell_raw = row[col_name] if col_name in row.index else ""

    subtitle, ds = datasets_for_matrix_cell(
        track, iso3, str(col_name), status_cols, tops, detail
    )
    st.markdown(f"**{country} ({iso3}) · {col_name}**")
    st.caption(f"{subtitle} · cell status: `{cell_raw}`")

    if ds.empty:
        st.warning("No mapped datasets for this cell (explicit gap / N/A, or no tops listed).")
        return

    show_cols = [
        c
        for c in [
            "rank_in_sector",
            "rank",
            "related_gpc_sector",
            "sector_name",
            "related_ccra_indicator",
            "indicator_name",
            "dataset_name",
            "publisher",
            "authoritative_tier",
            "confidence_level",
            "granularity_class",
            "granularity_label",
            "role",
            "horizons_covered",
        ]
        if c in ds.columns
    ]
    st.dataframe(ds[show_cols].reset_index(drop=True), use_container_width=True, hide_index=True, height=320)


def render_country_detail(
    summary: pd.DataFrame,
    detail: pd.DataFrame,
    tops: pd.DataFrame,
    track: str,
) -> None:
    st.subheader("Country drill-down")
    if summary.empty:
        st.info("No countries match the current filters.")
        return

    countries = summary["country"].tolist()
    country = st.selectbox("Country", countries, key=f"country_{track}")
    row = summary[summary["country"] == country].iloc[0]
    iso = row["iso3"]

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Score", int(row["score"]))
    c2.metric("Approach", tier_approach(row["tier"]))
    if track == "Mitigation":
        c3.metric("Covered", f"{int(row['subsectors_covered'])}/23")
        c4.metric("City-ready", int(row["city_ready_subsectors"]))
        key_col = "related_gpc_sector"
        name_col = "sector_name"
    else:
        c3.metric("Covered", f"{int(row['indicators_covered'])}/41")
        c4.metric("City-ready", int(row["city_ready_indicators"]))
        key_col = "related_ccra_indicator"
        name_col = "indicator_name"
    st.caption(
        f"**{tier_quality(row['tier'])}** · {tier_approach_note(row['tier'])} "
        f"(band {SCORE_BANDS.get(_tier_key(row['tier']), '—')})."
    )

    st.markdown(f"**Notes:** {row['notes']}")
    st.markdown("**Top datasets (country anchors)**")
    for k in ("top_dataset_1", "top_dataset_2", "top_dataset_3"):
        if pd.notna(row.get(k)) and str(row[k]).strip():
            st.write(f"- {row[k]}")

    d = detail[detail["iso3"] == iso].copy()
    if "readiness_status" not in d.columns and "best_granularity_label" in d.columns:
        d["readiness_status"] = d["best_granularity_label"]

    if "coverage_status" in d.columns:
        gaps = d[d["coverage_status"].isin(["missing", "n/a"])]
        if len(gaps):
            st.markdown("**Gaps / N/A**")
            gap_cols = [
                c
                for c in [key_col, name_col, "coverage_status", "readiness_status", "best_granularity_label"]
                if c in gaps.columns
            ]
            st.dataframe(gaps[gap_cols].reset_index(drop=True), use_container_width=True, hide_index=True)

    st.markdown("**Coverage detail**")
    show_cols = [
        c
        for c in [
            key_col,
            name_col,
            "dataset_count",
            "coverage_status",
            "readiness_status",
            "best_granularity_label",
            "needs_city_downscaling",
            "top_dataset_1",
            "top_note",
        ]
        if c in d.columns
    ]
    st.dataframe(d[show_cols].reset_index(drop=True), use_container_width=True, hide_index=True, height=360)

    st.markdown("**Top mapped datasets**")
    t = tops[tops["iso3"] == iso].copy()
    rank_col = "rank_in_sector" if "rank_in_sector" in t.columns else "rank"
    if rank_col in t.columns:
        t = t[t[rank_col] <= 3]
    show_t = [
        c
        for c in [
            key_col,
            name_col,
            rank_col,
            "dataset_name",
            "publisher",
            "authoritative_tier",
            "confidence_level",
            "granularity_class",
            "role",
        ]
        if c in t.columns
    ]
    st.dataframe(t[show_t].reset_index(drop=True), use_container_width=True, hide_index=True, height=320)


def _pct_label(x: float) -> str:
    try:
        return f"{float(x) * 100:.0f}%"
    except (TypeError, ValueError):
        return "—"


def page_overview(
    mit_sum: pd.DataFrame,
    adp_sum: pd.DataFrame,
    unified: pd.DataFrame | None = None,
) -> None:
    st.subheader("How should we approach each country?")
    st.caption(
        "Product view: **what kind of program** to design — not a yes/no gate. "
        "Ordered by research judgment (City-ready → Extra work → Accept downscaling), then score."
    )
    if mit_sum.empty or adp_sum.empty:
        st.info("No countries match the current filters.")
        return

    selected = set(mit_sum["iso3"]).intersection(set(adp_sum["iso3"]))
    mit_t = mit_sum.set_index("iso3")["tier"]
    adp_t = adp_sum.set_index("iso3")["tier"]
    mit_score = mit_sum.set_index("iso3")["score"]
    adp_score = adp_sum.set_index("iso3")["score"]

    # Build decision rows from qualitative research (product priority)
    base = mit_sum.loc[mit_sum["iso3"].isin(selected), ["iso3", "country"]].drop_duplicates()
    rows = []
    for _, r in base.iterrows():
        iso = r["iso3"]
        mt, at = str(mit_t.get(iso, "C")), str(adp_t.get(iso, "C"))
        qual_approach = combined_approach(mt, at)
        mq, aq = int(mit_score.get(iso, 0)), int(adp_score.get(iso, 0))
        rows.append(
            {
                "iso3": iso,
                "country": r["country"],
                "program_approach": qual_approach,
                "approach_note": tier_approach_note(worst_tier(mt, at)),
                "combined_score": round((mq + aq) / 2),
                "mit_score": mq,
                "adp_score": aq,
                "mit_quality": tier_quality(mt),
                "adp_quality": tier_quality(at),
            }
        )
    decision = pd.DataFrame(rows)
    decision["_ord"] = decision["program_approach"].map(APPROACH_ORDER).fillna(9)
    decision = decision.sort_values(
        ["_ord", "combined_score"], ascending=[True, False]
    ).reset_index(drop=True)
    decision.insert(0, "priority", decision.index + 1)
    n = len(decision)
    decision["priority_label"] = decision["priority"].map(
        lambda i: f"#{i} of {n} — start here" if i == 1 else f"#{i} of {n}"
    )

    st.markdown("#### Program priority")
    st.caption(
        "Read left → right: **where to start**, **what kind of program**, **what to plan for**. "
        "No opaque 0–100 score in this table — relative order is the priority number."
    )
    st.dataframe(
        decision[
            [
                "priority_label",
                "country",
                "iso3",
                "program_approach",
                "approach_note",
                "mit_quality",
                "adp_quality",
            ]
        ].rename(
            columns={
                "priority_label": "Priority",
                "country": "Country",
                "iso3": "ISO3",
                "program_approach": "Program approach",
                "approach_note": "What to plan for",
                "mit_quality": "Mitigation data",
                "adp_quality": "Adaptation data",
            }
        ),
        use_container_width=True,
        hide_index=True,
        height=360,
    )

    st.markdown(
        """
| Program approach | Meaning |
|---|---|
| **City-ready** | Strong public city-scale stack — closest to a scale-style program |
| **Extra work** | Doable with partners, sector fills, some downscaling |
| **Accept downscaling** | Still doable — accept coarser / national→city or modeled data (lower precision) |

| Mitigation / Adaptation data | Meaning |
|---|---|
| **Strong data** | City-scale public stack looks solid for that track |
| **Limited data** | Feasible, but expect gaps and extra work |
| **Sparse open data** | Possible only if you accept downscaling / lower precision |

Hard gaps almost everywhere: **CCRA-039** (stormwater coverage) · **I.6** (fugitive fuels).
"""
    )

    # Ticket / quantitative metrics (secondary)
    with st.expander("Optional: research scores (0–100) used only to order countries inside a band", expanded=False):
        st.caption(
            "These numbers are a relative research ranking, not a % complete and not a pass/fail. "
            "Higher ≈ easier city-product fit within the same program approach."
        )
        st.dataframe(
            decision[
                [
                    "priority_label",
                    "country",
                    "iso3",
                    "program_approach",
                    "combined_score",
                    "mit_score",
                    "adp_score",
                ]
            ].rename(
                columns={
                    "priority_label": "Priority",
                    "country": "Country",
                    "iso3": "ISO3",
                    "program_approach": "Program approach",
                    "combined_score": "Combined research rank",
                    "mit_score": "Mitigation research rank",
                    "adp_score": "Adaptation research rank",
                }
            ),
            use_container_width=True,
            hide_index=True,
            height=280,
        )

    with st.expander("Coverage metrics (ticket: % sectors, % years, quality tier, viable)", expanded=False):
        st.caption(
            "Automatic checklist math from `comparison_unified/` / `coverage_metrics_spec.md`. "
            "Use for scoring inputs — not as a “don’t engage” gate."
        )
        if unified is None or unified.empty:
            st.warning("Missing `comparison_unified/coverage_country_summary.csv`.")
        else:
            u = unified[unified["iso3"].isin(selected)].copy()
            u["qual_approach"] = [
                combined_approach(mit_t.get(i, "C"), adp_t.get(i, "C")) for i in u["iso3"]
            ]
            # Keep same priority order as decision table
            order_map = dict(zip(decision["iso3"], decision["priority"]))
            u["priority"] = u["iso3"].map(order_map)
            u = u.sort_values("priority")
            metrics_show = pd.DataFrame(
                {
                    "Priority": u["priority"],
                    "Country": u["country"],
                    "ISO3": u["iso3"],
                    "Program approach (research)": u["qual_approach"],
                    "Checklist view (auto)": u["program_approach"],
                    "Meets GPC viable bar?": u["viable_ticket"].map({1: "Yes", 0: "No"}),
                    "Mit % checklist": u["mit_coverage_pct"].map(_pct_label),
                    "Mit % years 2015–24": u["mit_year_pct"].map(_pct_label),
                    "Mit % T1+T2": u["mit_t1_t2_pct"].map(_pct_label),
                    "Mit % city grain": u["mit_city_ready_pct"].map(_pct_label),
                    "Adp % checklist": u["adp_coverage_pct"].map(_pct_label),
                    "Adp % years 2015–24": u["adp_year_pct"].map(_pct_label),
                    "Adp % T1+T2": u["adp_t1_t2_pct"].map(_pct_label),
                    "Adp % city grain": u["adp_city_ready_pct"].map(_pct_label),
                }
            )
            st.dataframe(metrics_show, use_container_width=True, hide_index=True, height=320)
            st.markdown(
                """
**Ticket dimensions:** checklist coverage % · years covered 2015–2024 · quality tier (T1 vetted / T2 global-modeled / T3 proxy) · viable bar for GPC replication.  
If **Checklist view** is easier than **Program approach (research)**, global fills are padding the checklist — still plan for lower city precision.
"""
            )

    with st.expander("Score methodology", expanded=False):
        render_score_methodology()


def render_score_methodology() -> None:
    st.markdown("### Score methodology")
    st.markdown(
        """
The **country score (0–100)** is a **qualitative product ranking** from the country research packages —
not an automated formula and not an official completeness audit. It answers:
*“How usable is the public data stack for a city-scale CityCatalyst product in this country?”*

#### What goes into the judgment

Each country is reviewed against a fixed checklist:

| Track | Checklist | Coverage unit |
|---|---|---|
| **Mitigation** | GPC Data Availability Framework | 23 GPC subsectors (`I.1` … `VI.1`) |
| **Adaptation** | CCRA climate-risk indicators (`climate_risk_indicators_by_sector.json`) | 41 indicators (`CCRA-001` … `CCRA-041`) |

For every unit we map public datasets and record:

1. **Coverage** — is there at least one suitable public dataset, an explicit gap, or n/a?
2. **Granularity / readiness** — best spatial grain for city use (`city-ready`, `needs downscaling`, `facility`, `missing`, …)
3. **Authority & confidence** — primary official vs research/NGO vs international modeled vs OEF screening
4. **Hard gaps** — explicit `NO-COVERAGE` / Gap rows count as **missing** even if a proxy exists
5. **City product fit** — can a municipal officer run GPC inventory / CCRA screening without proprietary bulk buys?

OEF pipeline-ready screening products (flood / heat / landslide H×E×V, shared E/V, etc.) **count** as usable layers even when a country-specific publish is not yet in the catalog.

#### How the score is set (research synthesis)

There is **no closed equation** like `score = 2 × covered + …`.  
Analysts synthesize the package into a 0–100 score and a quality band:

| Data quality | Program approach | Legacy tier | Score band |
|---|---|---|---|
| **Strong data** | **City-ready** | A | ≈ **80–100** |
| **Limited data** | **Extra work** | B | ≈ **60–79** |
| **Sparse open data** | **Accept downscaling** | C | ≈ **0–59** |

Within a band, higher scores mean stronger city-ready coverage, fewer hard gaps, and less dependence on national-only or modeled gap-fills.  
**Sparse open data does not mean “don’t engage”** — it means design the program assuming population/national downscaling and lower city precision (Morocco-style).

**Typical downward pressures on the score**
- Many sectors/indicators only at **national / state** grain (needs downscaling)
- Missing **city meters / VKT / waste** (mitigation) or **hazard GIS / fine E/V** (adaptation)
- Reliance on global models where official open layers are closed
- Extra hard gaps beyond the cross-cutting ones (e.g. MAR disease cases; ETH SLR n/a)

**Typical upward pressures**
- Official **city / neighborhood** census or inventory layers
- Open multi-hazard portals (e.g. Project NOAH) or mature LA GHG inventories
- Broad coverage with few explicit gaps

#### What *is* calculated in this app

**Qualitative (research scores)**

| Metric | Formula |
|---|---|
| **Combined qual. score** | `(mitigation_score + adaptation_score) / 2` |
| **Delta** | `adaptation_score − mitigation_score` |
| **Program approach (qualitative)** | Strong→City-ready · Limited→Extra work · Sparse→Accept downscaling; worse track wins |

**Quantitative (`comparison_unified/`, see `coverage_metrics_spec.md`)**

| Metric | Formula |
|---|---|
| **Coverage %** | covered checklist cells / N (23 GPC or 41 CCRA) |
| **Years %** | mean(years in 2015–2024 / 10) on covered cells |
| **T1+T2 %** | share of covered cells with best tier T1 or T2 |
| **Program approach (metrics)** | thresholds on coverage × years × T1+T2; worse track wins |
| **Viable (GPC ticket)** | mitigation band = scale-friendly |

#### Caveats

- Dataset **counts** in the matrices are not quality-weighted.
- Metrics can look strong when **global modeled** fills dominate; qualitative scores capture city-product thinness.
- Year % is best-effort from `temporal_coverage` text in research CSVs.
- Data approach is necessary but **not sufficient** for a full Brazil-style program (partnerships, methodology localization, financing pathway still matter).
"""
    )


def main() -> None:
    st.set_page_config(
        page_title="Data Coverage Assessment",
        page_icon="🌍",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown(
        """
        <style>
          .block-container { padding-top: 1.2rem; }
          h1 { font-family: Georgia, serif !important; color: #0b5f63 !important; margin-bottom: 0.15rem !important; }
          .oef-brand { color: #5a6e68; font-size: 1.05rem; margin: 0 0 0.75rem 0; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Data Coverage Assessment")
    st.markdown('<p class="oef-brand">Open Earth Foundation</p>', unsafe_allow_html=True)
    st.markdown(
        "Public city-scale data for CityCatalyst-style **Mitigation (GPC)** and "
        "**Adaptation (CCRA)** — scored and ranked by **how to design the program**, "
        "not whether a country is in or out."
    )
    st.caption(
        "Program approach: **City-ready** · **Extra work** · **Accept downscaling**. "
        "Overview ranks countries by program type — not by a cryptic 0–100 score."
    )

    try:
        mit_sum = load_csv(str(MIT / "01_country_summary.csv"))
        mit_status = load_csv(str(MIT / "03_country_x_sector_status.csv"))
        mit_detail = load_csv(str(MIT / "04_country_sector_detail.csv"))
        mit_tops = load_csv(str(MIT / "05_top_datasets_by_country_sector.csv"))
        adp_sum = load_csv(str(ADP / "01_country_summary.csv"))
        adp_status = load_csv(str(ADP / "03b_country_x_theme_status.csv"))
        adp_detail = load_csv(str(ADP / "04_country_indicator_detail.csv"))
        adp_tops = load_csv(str(ADP / "05_top_datasets_by_country_indicator.csv"))
    except FileNotFoundError as e:
        st.error(f"Missing comparison CSV: {e}")
        st.stop()

    unified_path = UNIFIED / "coverage_country_summary.csv"
    unified = load_csv(str(unified_path)) if unified_path.exists() else None

    country_options = (
        mit_sum[["iso3", "country"]]
        .drop_duplicates()
        .sort_values("country")
        .assign(label=lambda d: d["iso3"] + " — " + d["country"])
    )
    label_to_iso = dict(zip(country_options["label"], country_options["iso3"]))
    all_labels = country_options["label"].tolist()

    with st.sidebar:
        st.header("Navigation")
        view = st.radio(
            "View",
            ["Overview", "Mitigation (GPC)", "Adaptation (CCRA)"],
            index=0,
        )
        quality_options = ["Strong data", "Limited data", "Sparse open data"]
        qualities = st.multiselect(
            "Filter by data quality",
            quality_options,
            default=quality_options,
            help=(
                "Strong → City-ready (≈80–100) · Limited → Extra work (≈60–79) · "
                "Sparse → Accept downscaling (≈0–59). Replaces A/B/C."
            ),
        )

        c1, c2 = st.columns(2)
        if c1.button("All countries", use_container_width=True):
            st.session_state["country_filter"] = all_labels
            st.rerun()
        if c2.button("Clear countries", use_container_width=True):
            st.session_state["country_filter"] = []
            st.rerun()

        if "country_filter" not in st.session_state:
            st.session_state["country_filter"] = all_labels
        st.session_state["country_filter"] = [
            label for label in st.session_state["country_filter"] if label in all_labels
        ]

        countries_selected = st.multiselect(
            "Filter countries",
            all_labels,
            key="country_filter",
            help="Choose one or more countries. Combines with the data-quality filter.",
        )
        st.divider()
        st.caption("Qualitative: `data_coverage/{mitigation,adaptation}/comparison/`")
        st.caption("Quantitative: `data_coverage/comparison_unified/`")
        st.caption("9 ISO3 research packages.")

    if not qualities:
        st.warning("Select at least one data-quality band.")
        st.stop()
    if not countries_selected:
        st.warning("Select at least one country.")
        st.stop()

    selected_isos = {label_to_iso[label] for label in countries_selected if label in label_to_iso}
    selected_tiers = {QUALITY_TO_TIER[q] for q in qualities if q in QUALITY_TO_TIER}

    def apply_filters(df: pd.DataFrame) -> pd.DataFrame:
        return df[df["tier"].isin(selected_tiers) & df["iso3"].isin(selected_isos)].reset_index(drop=True)

    mit_sum_f = apply_filters(mit_sum)
    adp_sum_f = apply_filters(adp_sum)
    mit_status_f = apply_filters(mit_status)
    adp_status_f = apply_filters(adp_status)
    mit_detail_f = mit_detail[mit_detail["iso3"].isin(selected_isos)].copy()
    adp_detail_f = adp_detail[adp_detail["iso3"].isin(selected_isos)].copy()
    mit_tops_f = mit_tops[mit_tops["iso3"].isin(selected_isos)].copy()
    adp_tops_f = adp_tops[adp_tops["iso3"].isin(selected_isos)].copy()

    if mit_sum_f.empty and adp_sum_f.empty:
        st.warning("No countries match the current quality + country filters.")
        st.stop()

    if view == "Overview":
        page_overview(mit_sum_f, adp_sum_f, unified)
    elif view == "Mitigation (GPC)":
        tab1, tab2, tab3 = st.tabs(["Leaderboard", "Sector matrix", "Country detail"])
        with tab1:
            render_leaderboard(mit_sum_f, "Mitigation")
        with tab2:
            render_matrix(
                mit_status_f,
                mit_tops_f,
                mit_detail_f,
                "Mitigation",
                "GPC subsector readiness",
                "matrix_mitigation",
            )
        with tab3:
            render_country_detail(mit_sum_f, mit_detail_f, mit_tops_f, "Mitigation")
    else:
        tab1, tab2, tab3 = st.tabs(["Leaderboard", "Theme matrix", "Country detail"])
        with tab1:
            render_leaderboard(adp_sum_f, "Adaptation")
        with tab2:
            render_matrix(
                adp_status_f,
                adp_tops_f,
                adp_detail_f,
                "Adaptation",
                "CCRA theme readiness (41 indicators rolled up)",
                "matrix_adaptation",
            )
        with tab3:
            render_country_detail(adp_sum_f, adp_detail_f, adp_tops_f, "Adaptation")

    st.divider()
    st.caption(
        "Open Earth Foundation · Data coverage research · "
        "Scores are qualitative rankings for city product use."
    )


if __name__ == "__main__":
    main()
