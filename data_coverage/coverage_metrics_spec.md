# Coverage metrics specification

**One product question:** for each priority country, do we have enough **public city-scale data** to run CityCatalyst-style work — and **what kind of program** should we design?

Mitigation (GPC) and adaptation (CCRA) are **two checklists for the same decision**, not two separate projects.  
This spec is the shared measurement layer on top of the research already in `mitigation/` and `adaptation/`.

```text
                    ┌─────────────────────────────────────┐
                    │  CityCatalyst / GCoM replication    │
                    │  “Enough data? What program type?”  │
                    └─────────────────┬───────────────────┘
                                      │
              ┌───────────────────────┴───────────────────────┐
              ▼                                               ▼
     Mitigation checklist                            Adaptation checklist
     23 GPC subsectors                               41 CCRA indicators
     mitigation/countries/*/                         adaptation/countries/*/
              │                                               │
              └───────────────────────┬───────────────────────┘
                                      ▼
                    Shared metrics (this spec)
                    coverage × years × quality tier
                    → viability band + program approach
                                      │
                    ┌─────────────────┴─────────────────┐
                    ▼                                   ▼
         Quantitative summary                  Qualitative synthesis
         (formulas below)                      (0–100 scores + dashboard)
```

| Layer | What it is | Where it lives |
|---|---|---|
| **Evidence** | Dataset × checklist rows (+ gaps) | `mitigation/countries/`, `adaptation/countries/` |
| **Comparison** | Matrices, tops, HTML dashboards | `*/comparison/` |
| **Metrics (this doc)** | Same formulas for both tracks | `coverage_metrics_spec.md` |
| **Decision UI** | Combined priority + program approach | `streamlit_app/` / dashboardsOEF |

---

## 0. How to use what we already did

Do **not** restart research. Reuse packages as the evidence base:

| Already have | Use for |
|---|---|
| `01_datasets_{ISO3}.csv` | Cell coverage, best dataset, tier mapping, temporal strings |
| `comparison/01_country_summary.csv` | Qualitative score + legacy A/B/C → program approach |
| `comparison/03*_status.csv` / `04_*_detail.csv` | Covered vs missing, city-ready vs needs downscaling |
| Streamlit / HTML dashboards | Strategic narrative for BD / program design |

**Workflow**

1. Keep collecting evidence only in `mitigation/` + `adaptation/` (same 9 ISO3, same package shape).  
2. Derive **track metrics** with the formulas in §3 (GPC and CCRA separately).  
3. Derive **country decision** by combining both tracks (§2.3) — same language as the dashboard.  
4. Optionally refine qualitative 0–100 scores so they stay consistent with the quantitative bands.

The ticket’s emissions/GPC focus is the **mitigation slice** of this same system; adaptation uses identical metric definitions on the CCRA checklist.

---

## 1. Coverage dimensions (shared)

### 1.1 Units of analysis

| Track | Checklist | Cell | Denominator |
|---|---|---|---|
| **Mitigation** | GPC Data Availability Framework | Country × `gpc_ref` (`I.1`…`VI.1`) | **23** |
| **Adaptation** | `climate_risk_indicators_by_sector.json` | Country × `CCRA-xxx` | **41** (exclude `n/a` from denominator when flagged, e.g. ETH SLR) |

**Time window (both tracks):** calendar years **2015–2024** (10 years).  
For adaptation hazards/E/V, a year “hits” if the source provides a usable present-day or scenario product dated/applicable in that window (see §1.3 notes).

### 1.2 Dimension A — Checklist coverage

| Term | Definition |
|---|---|
| **Covered** | ≥1 usable public dataset for that cell (not an explicit Gap / `NO-COVERAGE` row) |
| **Track metric** | `coverage_pct = (# covered cells) / denominator` |

Mitigation alias used in tickets: `sector_pct` (= `coverage_pct` on GPC).  
Adaptation alias: `indicator_pct`.

### 1.3 Dimension B — Year coverage (2015–2024)

| Term | Definition |
|---|---|
| **Year hit** | Year `y` evidenced by ≥1 dataset for that cell |
| **Cell** | `year_frac = years_covered / 10` |
| **Track metric** | `year_pct = mean(year_frac)` over covered cells (0 if none covered) |

Notes (both tracks):
- Ranges like `2018–2021` expand inside 2015–2024.
- Single-year inventories count one year unless a series is documented.
- Undated “present” snapshots → do not auto-fill 10 years; set documented years only (or 0 until confirmed).
- Adaptation futures (`2030`, SSP) count toward product readiness but **not** toward `year_pct` unless they include a historical/present anchor in 2015–2024.

### 1.4 Dimension C — Quality tier

Same tier scale for both tracks (engineering / ticket language):

| Tier | Label | Mitigation examples | Adaptation examples |
|---|---|---|---|
| **T1** | Vetted / primary | Official GHGI, regulator sales, cantonal GPC inventories | Official census E/V, national hazard GIS (NOAH, AZI, EA), statistical office |
| **T2** | Global / modeled | EDGAR, Climate TRACE, Google EIE | WorldPop, CHIRPS/ERA5, JRC flood, OEF screening rasters |
| **T3** | Proxy / scaled | Population-scaled national totals, weak proxies | DHS regional prevalence only, crude downscales |

**Cell rule:** `best_tier = min(T1,T2,T3)` among datasets for that cell.  

**Track metrics:** `t1_pct`, `t2_pct`, `t3_pct`, `t1_t2_pct` among covered cells.

### 1.5 Optional — city readiness

`city_ready_pct` = share of checklist cells whose best `granularity_class` is city/municipality or finer  
(adaptation: modeled hazard grids may count as screening-ready per adaptation comparison rules).

### 1.6 Map from existing CSV columns

| Field in `01_datasets_*.csv` | Metric use |
|---|---|
| `related_gpc_sector` / `related_ccra_indicator` | Cell id |
| Non-Gap row present | `covered=1` |
| `authoritative_tier` | Seed T1/T2/T3 (analyst may override for city use) |
| `temporal_coverage` | `years_covered` |
| `granularity_class` | Optional city-ready |

**Suggested authoritative_tier → tier seed**

| `authoritative_tier` (research) | Seed |
|---|---|
| Primary official, National program / cantonal, Utility | T1 |
| International modeled, OEF derived screening | T2 |
| Research/NGO (case-by-case), weak proxy, Gap | T3 or uncovered |

---

## 2. Thresholds & program approach (shared language)

Quantitative bands and dashboard language are **the same three outcomes**:

| Viability band (metrics) | Program approach (dashboard) | Typical qualitative score |
|---|---|---|
| **Viable — scale-friendly** | **City-ready** | ≈80–100 (legacy A) |
| **Viable — extra work** | **Extra work** | ≈60–79 (legacy B) |
| **Constrained — accept downscaling** | **Accept downscaling** | ≈0–59 (legacy C) |
| **Insufficient** (metrics only) | Still “Accept downscaling” for BD if strategically needed | — |

### 2.1 Per-track rules

Applied independently to mitigation (`coverage_pct` on 23) and adaptation (`coverage_pct` on 41):

| Band | Rule |
|---|---|
| Scale-friendly / City-ready | `coverage_pct ≥ 0.80` **AND** `year_pct ≥ 0.50` **AND** `t1_t2_pct ≥ 0.70` |
| Extra work | `coverage_pct ≥ 0.60` **AND** `year_pct ≥ 0.30` (and not scale-friendly) |
| Accept downscaling | `coverage_pct ≥ 0.40` (and not above) |
| Insufficient | `coverage_pct < 0.40` |

### 2.2 Ticket “viable” (emissions / GCoM slice)

For GPC-only ticket language: **`viable_ticket = 1`** iff mitigation band is **scale-friendly**.  
Optional inclusive start flag: mitigation in {scale-friendly, extra work}.

### 2.3 Combined country decision (mitigation + adaptation)

Same rule as the Streamlit overview — **more constrained track wins**:

```text
program_approach = worse(mitigation_approach, adaptation_approach)
# City-ready < Extra work < Accept downscaling
```

| Combined score (dashboard) | Definition |
|---|---|
| `combined_score` | `(mitigation_qual_score + adaptation_qual_score) / 2` |
| Priority order | Sort by `program_approach`, then `combined_score` descending |

Qualitative scores remain research synthesis; they should **not contradict** the quantitative band without a written note (e.g. “high coverage but all T3 → Accept downscaling”).

---

## 3. Formulas

### 3.1 Per cell

```text
covered       = 1 if ≥1 usable dataset else 0
years_covered = |years in [2015,2024] evidenced|
year_frac     = years_covered / 10
best_tier     = T1 | T2 | T3   # null if uncovered
```

### 3.2 Per track (mitigation or adaptation)

```text
coverage_pct = sum(covered) / N          # N=23 or 41 (or 41−n/a)
year_pct     = mean(year_frac | covered=1)
t1_pct, t2_pct, t3_pct, t1_t2_pct as in §1.4
viability_band / program_approach from §2.1
```

### 3.3 Per country (both tracks)

```text
mitigation_*   from GPC cells
adaptation_*   from CCRA cells
program_approach = worse(mitigation, adaptation)   # §2.3
combined_score   = (mit_qual_score + adp_qual_score) / 2
delta            = adp_qual_score − mit_qual_score
```

### 3.4 Output tables (unified folder)

Recommend one shared folder later, e.g. `comparison_unified/` (or populate under each track with the same schema):

**`coverage_by_country_cell.csv`**
```text
iso3,country,track,cell_id,cell_name,covered,years_covered,year_frac,best_tier,best_dataset_id,best_dataset_name,notes
```
`track` = `mitigation` | `adaptation`  
`cell_id` = `I.1` or `CCRA-001`

**`coverage_by_country_dataset.csv`**
```text
iso3,country,track,dataset_id,dataset_name,publisher,tier,cells_touched,n_cells,years_contributed,n_years,notes
```

**`coverage_country_summary.csv`**
```text
iso3,country,
mit_coverage_pct,mit_year_pct,mit_t1_t2_pct,mit_band,mit_approach,mit_qual_score,
adp_coverage_pct,adp_year_pct,adp_t1_t2_pct,adp_band,adp_approach,adp_qual_score,
program_approach,combined_score,delta,viable_ticket,notes
```

---

## 4. Validation

1. Run formulas on **Costa Rica** for **both** tracks (packages already exist).  
2. Add one emissions benchmark if required by ticket (e.g. Minnesota) on **mitigation** only.  
3. Confirm bands differentiate and match program-approach intuition in the dashboard.  
4. Adjust §2.1 thresholds if needed; log changes in §8.

---

## 5. Done checklist

- [x] Shared dimensions for mitigation + adaptation (§1)  
- [x] Shared thresholds / program approach (§2)  
- [x] Formulas + unified output schema (§3)  
- [x] Explicit reuse path for existing country packages (§0)  
- [x] Metrics computed for all 9 countries → `comparison_unified/` (script: `scripts/compute_coverage_metrics.py`)  
- [ ] Spot-check / lock thresholds after review (esp. year parsing + MN benchmark if required) (§4)  

---

## 6. Change log

| Date | Change |
|---|---|
| 2026-08-10 | Initial GPC-focused spec |
| 2026-08-10 | Unified with adaptation: same metrics, shared program approach, reuse of existing research packages |
| 2026-08-10 | Computed metrics for 9 countries into `comparison_unified/` |
