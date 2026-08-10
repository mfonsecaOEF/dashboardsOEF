"""
OEF Data Coverage Dashboard — Mitigation (GPC) + Adaptation (CCRA)

Shareable via Streamlit Community Cloud. Teammates only need the URL.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent  # data_coverage/
MIT = ROOT / "mitigation" / "comparison"
ADP = ROOT / "adaptation" / "comparison"

TIER_COLORS = {"A": "#0f6b5c", "B": "#9a6b12", "C": "#8a3a32"}

# Human-readable decision labels (source tier stays A/B/C in CSVs)
TIER_QUALITY = {
    "A": "Strong data",
    "B": "Limited data",
    "C": "Weak data",
}
TIER_CALL = {
    "A": "YES",
    "B": "MAYBE",
    "C": "NO",
}
QUALITY_TO_TIER = {v: k for k, v in TIER_QUALITY.items()}

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


def tier_quality(tier: str) -> str:
    return TIER_QUALITY.get(str(tier).strip().upper(), str(tier))


def tier_call(tier: str) -> str:
    return TIER_CALL.get(str(tier).strip().upper(), "—")


def combined_call(mit_tier: str, adp_tier: str) -> str:
    """YES if neither track is weak and at least one is strong; NO if any weak; else MAYBE."""
    tiers = {str(mit_tier).strip().upper(), str(adp_tier).strip().upper()}
    if "C" in tiers:
        return "NO"
    if "A" in tiers:
        return "YES"
    return "MAYBE"


def delta_meaning(delta: float) -> str:
    if delta >= 10:
        return "Adaptation much stronger → prefer CCRA-first"
    if delta <= -10:
        return "Mitigation much stronger → prefer GPC-first"
    return "Balanced (±10) — similar readiness on both tracks"


def enrich_summary(summary: pd.DataFrame) -> pd.DataFrame:
    out = summary.copy()
    out["data_quality"] = out["tier"].map(tier_quality)
    out["recommend"] = out["tier"].map(tier_call)
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
    st.subheader("Priority ranking (most → least recommended)")
    st.caption(
        "Ordered by score. **YES** = Strong data (≈80–100) · "
        "**MAYBE** = Limited data (≈60–79) · **NO** = Weak data (≈0–59)."
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
            call = tier_call(tier)
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
                  <div style="margin-top:10px;font-size:.84rem;color:#5a6e68;line-height:1.4;">
                    {row['notes']}
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


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
    c2.metric("Recommend", tier_call(row["tier"]))
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
        f"Data quality: **{tier_quality(row['tier'])}** "
        f"(legacy tier {row['tier']}, band {SCORE_BANDS.get(str(row['tier']).upper(), '—')}). "
        "YES ≈80–100 · MAYBE ≈60–79 · NO ≈0–59."
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


def page_overview(mit_sum: pd.DataFrame, adp_sum: pd.DataFrame) -> None:
    st.subheader("Which country should we prioritize?")
    st.caption(
        "Decision view for CityCatalyst-style expansion: ordered from most recommended to least. "
        "Same 9 countries, mitigation (GPC) + adaptation (CCRA)."
    )
    if mit_sum.empty or adp_sum.empty:
        st.info("No countries match the current filters.")
        return

    m = mit_sum[["iso3", "country", "tier", "score"]].rename(
        columns={"tier": "mitigation_tier", "score": "mitigation_score"}
    )
    a = adp_sum[["iso3", "tier", "score"]].rename(
        columns={"tier": "adaptation_tier", "score": "adaptation_score"}
    )
    both = m.merge(a, on="iso3")
    both["priority_score"] = (
        both["mitigation_score"] + both["adaptation_score"]
    ) / 2.0
    both["delta"] = both["adaptation_score"] - both["mitigation_score"]
    both["mitigation_quality"] = both["mitigation_tier"].map(tier_quality)
    both["adaptation_quality"] = both["adaptation_tier"].map(tier_quality)
    both["mitigation_call"] = both["mitigation_tier"].map(tier_call)
    both["adaptation_call"] = both["adaptation_tier"].map(tier_call)
    both["recommend"] = [
        combined_call(mt, at)
        for mt, at in zip(both["mitigation_tier"], both["adaptation_tier"])
    ]
    both["delta_meaning"] = both["delta"].map(delta_meaning)
    order = {"YES": 0, "MAYBE": 1, "NO": 2}
    both["_ord"] = both["recommend"].map(order)
    both = both.sort_values(["_ord", "priority_score"], ascending=[True, False]).reset_index(drop=True)
    both.insert(0, "priority", both.index + 1)

    show = both[
        [
            "priority",
            "country",
            "iso3",
            "recommend",
            "priority_score",
            "adaptation_score",
            "adaptation_call",
            "adaptation_quality",
            "mitigation_score",
            "mitigation_call",
            "mitigation_quality",
            "delta",
            "delta_meaning",
        ]
    ].copy()
    show["priority_score"] = show["priority_score"].round(0).astype(int)
    show["delta"] = show["delta"].astype(int)
    show = show.rename(
        columns={
            "priority": "Priority",
            "country": "Country",
            "iso3": "ISO3",
            "recommend": "Recommend",
            "priority_score": "Combined score",
            "adaptation_score": "Adaptation score",
            "adaptation_call": "Adaptation",
            "adaptation_quality": "Adaptation data",
            "mitigation_score": "Mitigation score",
            "mitigation_call": "Mitigation",
            "mitigation_quality": "Mitigation data",
            "delta": "Delta (adapt − mit)",
            "delta_meaning": "What the delta means",
        }
    )
    st.dataframe(show, use_container_width=True, hide_index=True, height=420)

    st.markdown(
        """
**How to read the decision**

| Signal | Meaning | Cutoff |
|---|---|---|
| **Recommend = YES** | Worth prioritizing for CityCatalyst-style work | At least one track is **Strong data**, and neither is **Weak data** |
| **Recommend = MAYBE** | Possible pilot with caveats / heavier OEF fills | Both tracks are **Limited data** |
| **Recommend = NO** | Not recommended for Brazil-style rollout near-term | Either track is **Weak data** |
| **Strong / Limited / Weak data** | Replaces old A / B / C tiers | Strong ≈80–100 · Limited ≈60–79 · Weak ≈0–59 |
| **Combined score** | Average of mitigation + adaptation scores | Higher = higher priority within the same Recommend band |
| **Delta (adapt − mit)** | Which product track has better public data | **≈0 (±10)** balanced · **≥+10** CCRA-first · **≤−10** GPC-first |

**Tracks**
- **Mitigation** = public data for city GPC GHG inventories (23 subsectors)
- **Adaptation** = public data for city CCRA indicators (41 H×E×V indicators)

**Known hard gaps (all / most countries)**
- Adaptation: **CCRA-039** stormwater drainage *coverage*
- Mitigation: **I.6** fugitive emissions from fuels
"""
    )


def main() -> None:
    st.set_page_config(
        page_title="OEF Data Coverage",
        page_icon="🌍",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown(
        """
        <style>
          .block-container { padding-top: 1.2rem; }
          h1 { font-family: Georgia, serif !important; color: #0b5f63 !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("OEF Data Coverage")
    st.markdown(
        "Which countries have enough **public city-scale data** for CityCatalyst-style "
        "**Mitigation (GPC)** and **Adaptation (CCRA)** — and in what priority order?"
    )
    st.caption(
        "Recommend: **YES** (Strong data) · **MAYBE** (Limited data) · **NO** (Weak data). "
        "Score bands ≈ 80–100 / 60–79 / 0–59."
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
        quality_options = ["Strong data", "Limited data", "Weak data"]
        qualities = st.multiselect(
            "Filter by data quality",
            quality_options,
            default=quality_options,
            help="Strong ≈ YES (80–100) · Limited ≈ MAYBE (60–79) · Weak ≈ NO (0–59). Replaces A/B/C.",
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
        st.caption("Data from `data_coverage/{mitigation,adaptation}/comparison/`")
        st.caption("Updated with country research packages (9 ISO3).")

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
        page_overview(mit_sum_f, adp_sum_f)
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
