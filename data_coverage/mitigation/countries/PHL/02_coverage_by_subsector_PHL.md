# Philippines GPC coverage assessment

Checklist = 23 subsectors in `GPC_Data_Availability_Framework.xlsx`.  
Catalogue = `01_datasets_PHL.csv` (PHL-001 … PHL-024).

---

## Stationary Energy

### I.1 Residential buildings — **Partial → relatively strong national**

| Need | Finding |
|---|---|
| Residential electricity | **Yes (national/regional).** DOE Power Statistics sales by sector & region (PHL-003); Meralco franchise volumes (PHL-006); FIES supporting (PHL-023). Open barangay/LGU automatic extracts: **Partial** (typically via LGU request to DU — documented in PHL-015). |
| Residential fuels (LPG, kerosene, biomass) | **Partial.** DOE KES petroleum by sector (PHL-004). LGU fuel sales registers: **No suitable open dataset identified**. |
| Emissions | BTR1 (PHL-001); Quezon City inventory (PHL-014); EDGAR/Climate TRACE (PHL-019/020). |

### I.2 Commercial & institutional — **Partial (strong electricity)**

DOE commercial sales (PHL-003); Meralco; CCC manual notes Makati collects fuel/electricity via business permits (PHL-015).  
Open nationwide LGU commercial fuel registry: **No suitable dataset identified**.

### I.3 Manufacturing industries & construction — **Partial**

DOE industrial electricity (PHL-003); KES fuels (PHL-004); cement proxies (PHL-018); BTR1.  
Open facility energy/PRTR for all plants: **No suitable comprehensive dataset identified**.

### I.4 Energy industries — **Yes**

DOE generation by technology/grid/region (PHL-003); KES; GPPD (PHL-022); BTR1; Climate TRACE assets.

### I.5 Agriculture, forestry & fishing energy — **Partial**

KES sector fuels (PHL-004); PSA agri supporting (PHL-012).  
Open municipal agri-energy meters: **No suitable dataset identified**.

### I.6 Non-specified — **Partial**

Energy-balance residuals (PHL-004) only. Dedicated residual LGU dataset: **No suitable dataset identified**.

### I.7 Fugitive coal — **Partial (where mines exist)**

Coal production by source in KES (PHL-016); BTR1 fugitives if estimated.  
Most cities: not relevant. Mine-level open methane CEMS: **No suitable dataset identified**.

### I.8 Fugitive oil & gas — **Partial**

Oil/gas production in KES (PHL-017); BTR1.  
Open distribution leakage/network attributes: **No suitable dataset identified**.

---

## Transportation

### II.1 On-road — **Partial (strong fleet)**

| Need | Finding |
|---|---|
| Fleet | LTO registration by type/region/fuel (PHL-007) — **Yes**. |
| Fuel sales | National petroleum by sector (PHL-004). Municipal pump sales: **No suitable dataset identified**. |
| VKT | **No suitable national open VKT panel identified.** |
| Emissions | BTR1 transport; Quezon City GPC; EDGAR/Climate TRACE. |

### II.2 Railways — **Partial**

Ridership KPIs for LRT/MRT/PNR (PHL-010).  
Open electricity/diesel by line: **No suitable dataset identified** (often confidential).

### II.3 Waterborne — **Yes (activity)**

PPA port statistics by port/PMO (PHL-008).  
Fuel bunkering/AIS emissions: **No suitable official open dataset identified**.

### II.4 Aviation — **Yes (activity) / Partial (fuel)**

CAAP/airport authority traffic stats (PHL-009).  
Fuel uplift open database: **No suitable dataset identified**.

### II.5 Off-road — **None / weak**

Equipment fuel/hours: **No suitable dataset identified** (only coarse KES residuals — Potential).

---

## Waste

### III.1 Solid waste disposal — **Partial**

NSWMC/EMB generation & facility status (PHL-011); BTR1 waste; Quezon City inventory; LGU SWM plans.  
National open facility annual tonnage+composition API: **No suitable dataset identified**.

### III.2 Biological treatment — **Partial / weak**

MRF/composting counts in EMB tables (PHL-011) as Supporting.  
Mass treated by process open series: **No suitable dataset identified**.

### III.3 Incineration & open burning — **None / limited**

Large MSW incineration uncommon; open burning poorly measured.  
Open activity dataset: **No suitable dataset identified** (BTR1 Potential only).

### III.4 Wastewater — **Partial**

MWSS concessionaire reports for Metro Manila (PHL-024); CCC LGU datasheets (PHL-015); BTR1.  
Open BOD/COD dashboards nationwide: **No suitable dataset identified**.

---

## IPPU

### IV.1 Industrial processes — **Partial**

Cement industry figures (PHL-018); BTR1 IPPU (DENR lead).  
Full open multi-industry process facility registry: **No suitable dataset identified**.

### IV.2 Product use — **Partial**

Open refrigerant sales registry: **No suitable dataset identified**.  
BTR1 product-use/HFC if reported — national Potential.

---

## AFOLU

### V.1 Livestock — **Yes**

PSA livestock/poultry surveys via OpenSTAT (PHL-012); FAOSTAT (PHL-021); BTR1.  
Manure systems + geocoded city herds: **No suitable dataset identified**.

### V.2 Land — **Yes**

NAMRIA land cover / FMB stats / FRL (PHL-013); GFW/WorldCover (PHL-021); BTR1 LULUCF.  
Official open urban carbon cadastre: **No suitable dataset identified**.

### V.3 Aggregate non-CO₂ on land — **Partial (strong rice/crops nationally)**

PSA crops (incl. rice) (PHL-012); FAOSTAT; BTR1 agriculture.  
Municipal fertilizer application maps: **No suitable dataset identified**.

---

## Other Scope 3

### VI.1 Other Scope 3 — **None (standardized city CB)**

Published open city EEIO/consumption-based inventories: **No suitable dataset identified**.  
Supporting: FIES (PHL-023).

---

## Coverage summary

| GPC | Subsector | Found? | Best anchors |
|---|---|---|---|
| I.1 | Residential | Partial | DOE Power Stats, Meralco, FIES, BTR1, QC inventory |
| I.2 | Commercial | Partial | DOE, Meralco, LGU permit practice |
| I.3 | Manufacturing energy | Partial | DOE industrial sales, KES, cement |
| I.4 | Energy industries | Yes | DOE generation, GPPD, BTR1 |
| I.5 | Agri energy | Partial | KES, PSA agri |
| I.6 | Non-specified | Partial | Energy balance residual |
| I.7 | Coal fugitive | Partial | KES coal production (site-specific) |
| I.8 | Oil/gas fugitive | Partial | KES oil/gas; BTR1 |
| II.1 | On-road | Partial | LTO fleet; KES fuels; BTR1 |
| II.2 | Rail | Partial | LRT/MRT/PNR ridership |
| II.3 | Waterborne | Yes (activity) | PPA |
| II.4 | Aviation | Yes (activity) | CAAP / airport authorities |
| II.5 | Off-road | No | — |
| III.1 | Solid waste | Partial | NSWMC/EMB; LGU SWM; BTR1 |
| III.2 | Biological treatment | Partial | EMB MRF counts only |
| III.3 | Incineration/open burning | No | — |
| III.4 | Wastewater | Partial | MWSS reports; BTR1 |
| IV.1 | Industrial processes | Partial | Cement; BTR1 IPPU |
| IV.2 | Product use | Partial | BTR1 only |
| V.1 | Livestock | Yes | PSA livestock |
| V.2 | Land | Yes | NAMRIA/FMB/FRL |
| V.3 | Aggregate land non-CO₂ | Partial | PSA crops/rice; BTR1 |
| VI.1 | Other Scope 3 | No | — |

## Cross-cutting verdict

The Philippines offers **above-average open national electricity and energy statistics**, **strong port/airport activity data**, **institutionalized national GHG inventories (EO 174 / BTR1)**, and a **working LGU inventory guidance system** with at least one published city result (Quezon City). Remaining city bottlenecks: **VKT**, **open LGU fuel sales**, **systematic landfill tonnage APIs**, and **F-gas stocks**.
