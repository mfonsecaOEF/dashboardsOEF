# Jurisdiction context — Minnesota, USA (USA-MN)

| Parameter | Value |
|---|---|
| Jurisdiction | Minnesota (U.S. state) — **not** a national ISO3 |
| Package code | `USA-MN` |
| Languages searched | English |
| Statistical / energy office | Minnesota Department of Commerce; U.S. Census; EIA |
| Open data | [MPCA climate data](https://www.pca.state.mn.us/air-water-land-climate/climate-change-trends-and-data); MnDOT roadway data; Met Council GitHub |
| GHG inventory lead | MPCA (+ Commerce for biennial reduction report) |
| Latest state GHG | Inventory 2005–2022 (2025 biennial report) |
| Facility reporting | U.S. EPA GHGRP / FLIGHT (≥25 kt CO2e typical) |
| Reference cities | Minneapolis, Saint Paul; Twin Cities MSA (Met Council) |
| Energy note | Strong utility regulation (Rules 7610); Xcel + municipal/coop mix; winter heating → natural gas material for buildings |
| Research date | 2026-08-10 |
| Framework | `GPC_Data_Availability_Framework.xlsx` (23 subsectors) |
| Research purpose | **Benchmark / state-scale stress test** of the same city-GHGI method used on the 9 priority countries — not a 10th C40 priority country |

## Institutional map

| Domain | Key providers |
|---|---|
| State GHG | MPCA inventory; EPA state GHG; Climate Action Framework |
| Energy | MN Commerce utility annual reports; EIA SEDS / EIA-861; eGRID; utilities (Xcel, CenterPoint, munis/coops) |
| Transport | MnDOT VMT (city/county); DPS vehicle registration; EIA/FHWA fuels; FAA/BTS aviation; ports (Duluth) |
| Waste / water | MPCA SCORE / landfills; Met Council Environmental Services; GHGRP landfills/WWTP |
| AFOLU | USDA NASS; MPCA LULUCF; MN DNR / USFS FIA |
| Oil & gas | Limited upstream; PHMSA + GHGRP + distribution utilities for fugitives |
| Subnational city products | **Minneapolis** inventory; **Saint Paul** Climate Dashboard; **Met Council Twin Cities MSA GHG** (open CPRG methods) |

## Structural notes

1. This package answers: **does the GPC city-data checklist still work when the unit is a U.S. state rather than a country?** Focus remains **city-scale GHGI**, not a second national inventory.
2. Minnesota is **data-rich at state + federal layers**, and unusually strong on **city/county VMT** and **published Twin Cities inventories**.
3. Prefer **MPCA / EPA GHGRP / Commerce / MnDOT / city & Met Council products** over EDGAR/TRACE when both exist.
4. Mapped gaps: **I.6** (residual) and **I.7** (no coal mining). Upstream oil/gas is thin; **I.8** is mostly midstream/distribution.
5. Keep **out of the 9-country Program priority ranking** unless product explicitly adds U.S. states as a jurisdiction class.
