# Morocco GPC coverage assessment

Checklist = 23 subsectors in `GPC_Data_Availability_Framework.xlsx`.  
Dataset catalogue = `01_datasets_MAR.csv` (MAR-001 … MAR-030).  
Rule: every subsector states whether datasets exist; gaps use **No suitable dataset identified** or explicit Partial.

Coverage legend:
- **Direct** — usable activity/emissions for that subsector (may still need allocation)
- **Supporting** — proxies / disaggregation aids
- **Potential** — modeled or indirect only
- **None** — no suitable public dataset found

---

## Stationary Energy

### I.1 Residential buildings — **Partial (Direct + Supporting)**

| Need | Finding |
|---|---|
| Residential electricity by municipality / customer class | **Partial.** City-scale volumes: Lydec filings for Grand Casablanca (MAR-008). National: ONEE (MAR-005), MEM (MAR-004), open indicators (MAR-002/003). Systematic open multi-city customer-class extracts: **not found**. |
| Residential fuels (butane/LPG, etc.) | **Partial.** National butane/LPG & energy keys (MAR-004, MAR-002). City fuel sales by municipality: **No suitable dataset identified**. |
| Emission factors / residential emissions | National: NIR (MAR-001). Modeled city/grid: EDGAR, Climate TRACE (MAR-024/025). |
| Supporting | HCP household electricity equipment (MAR-009); yearbook (MAR-010); regional energy diagnostic Fès-Meknès (MAR-011). |

**Authoritative sources:** ONEE/MEM/HCP (national); Lydec/SRM filings where published (city).  
**Alternatives:** EDGAR Cities; Climate TRACE urban.

### I.2 Commercial & institutional buildings — **Partial**

| Need | Finding |
|---|---|
| Commercial/institutional electricity & fuels | Same national stack as I.1 (MAR-004/005/002). City utility volumes rarely split by class in public PDFs (MAR-008 Partial). |
| Facility/public-building energy | **No suitable open national facility registry identified.** |
| Emissions | NIR (MAR-001); EDGAR/Climate TRACE (MAR-024/025). |

### I.3 Manufacturing industries & construction — **Partial (Direct national)**

| Need | Finding |
|---|---|
| Industrial energy / production | National energy & industry indicators (MAR-002/004/005); cement activity (MAR-021); NIR energy/IPPU tables (MAR-001). |
| Facility energy / PRTR | **No suitable open pollutant-release / facility energy register identified.** |
| Emissions | NIR; EDGAR; Climate TRACE assets. |

### I.4 Energy industries — **Yes (Direct)**

| Need | Finding |
|---|---|
| Generation by technology / plant | ONEE reports (MAR-005); ANRE generation mix (MAR-006); plant locations via Global Power Plant Database (MAR-030). |
| Plant emissions | NIR energy industries; Climate TRACE/EDGAR assets (MAR-024/025). |
| Grid geography support | ANRE hosting-capacity by distributor zone (MAR-007) — Supporting only. |

### I.5 Agriculture, forestry & fishing energy — **Partial / weak**

| Need | Finding |
|---|---|
| Farm/fishing fuel & electricity | National energy balances mention agriculture shares (MAR-004/002/011). Dedicated open municipal agri-energy series: **No suitable dataset identified**. |
| Supporting machinery/vessels | Agricultural census methodology exists historically; open machinery/vessel energy tables not found as reusable open datasets. |
| Emissions | NIR energy “other sectors”; EDGAR. |

### I.6 Non-specified sources — **Partial (residual only)**

Use national energy-balance residuals (MAR-002/004) after reconciling I.1–I.5.  
Dedicated unclassified municipal residual dataset: **No suitable dataset identified**.

### I.7 Fugitive emissions from coal — **None / not relevant for most cities**

Active city-boundary coal mining is not a general Moroccan urban source (power coal is largely imported).  
Mine-level open methane inventory for cities: **No suitable dataset identified**.  
National treatment (if any) only via NIR fugitive categories (MAR-001) — verify relevance before using.

### I.8 Fugitive oil & natural gas — **Partial**

| Need | Finding |
|---|---|
| Production / throughput | MEM/ONHYM national hydrocarbon indicators (MAR-004; MEM hydrocarbons pages); NIR 1.B.2 (MAR-001). |
| Pipeline/network leakage maps | **No suitable open distribution-network leakage dataset identified.** |
| Emissions | NIR; satellite/global methane products (not catalogued as Morocco-specific open official). |

---

## Transportation

### II.1 On-road transportation — **Partial**

| Need | Finding |
|---|---|
| Vehicle fleet | NARSA open registration/fleet stats (MAR-012); automobile monograph (MAR-014). |
| Fuel sales | National diesel/gasoline volumes via Competition Council monitoring (MAR-013); MEM petroleum (MAR-004). Municipal pump sales: **No suitable dataset identified**. |
| VKT / traffic counts | **No suitable national open VKT panel identified.** |
| Emissions | NIR transport; EDGAR/Climate TRACE road. |

### II.2 Railways — **Partial**

| Need | Finding |
|---|---|
| Passenger / freight activity | ONCF KPIs (MAR-015). |
| Diesel/electricity by route | **No suitable open energy-by-route dataset identified.** |
| Emissions | NIR rail; modeled products. |

### II.3 Waterborne navigation — **Yes (activity) / Partial (emissions)**

| Need | Finding |
|---|---|
| Port calls / throughput | ANP national port stats (MAR-016); Tanger Med facility reports (MAR-017). |
| Vessel fuel / AIS emissions | **No suitable official open bunkering/AIS emissions dataset identified** (use models). |

### II.4 Aviation — **Yes (activity) / Partial (emissions)**

| Need | Finding |
|---|---|
| Passengers / movements by airport | ONDA monthly Excel (MAR-018) — strong airport-level activity. |
| Fuel uplift / LTO by aircraft type | **No suitable open fuel-uplift dataset identified.** |
| Emissions | NIR aviation; Climate TRACE/EDGAR aviation. |

### II.5 Off-road transportation — **None**

Open equipment-class fuel/hours datasets for construction/ag off-road: **No suitable dataset identified**.  
Only coarse national fuel residuals / NIR “other transport” (MAR-001/004) as Potential.

---

## Waste

### III.1 Solid waste disposal — **Partial**

| Need | Finding |
|---|---|
| Waste generated/disposed, landfill type | National PNDM indicators & policy pages (MAR-020); NIR waste module (MAR-001). |
| Facility annual tonnage / composition / methane recovery | Comprehensive open facility time series: **No suitable dataset identified**. |
| Emissions | NIR; Climate TRACE landfills (Potential). |

### III.2 Biological treatment — **None / very weak**

Open national composting/anaerobic treatment mass-by-facility series: **No suitable dataset identified**.  
May appear only as minor NIR lines if estimated (MAR-001) — treat as insufficient for city inventories unless local operator data obtained.

### III.3 Incineration & open burning — **None / limited**

Municipal waste incineration is not a major published open statistical series.  
Open burning activity datasets: **No suitable dataset identified**.  
NIR may hold national estimates (MAR-001) — Potential only.

### III.4 Wastewater treatment & discharge — **Partial**

| Need | Finding |
|---|---|
| Population served / plants / capacity | ONEE sanitation KPIs (MAR-019); utility filings (MAR-008 for Casablanca wastewater volumes). |
| BOD/COD, N load, process pathways | **No suitable open plant-load dataset identified.** |
| Emissions | NIR wastewater. |

---

## IPPU

### IV.1 Industrial processes — **Partial (strong for cement nationally)**

| Need | Finding |
|---|---|
| Cement / mineral processes | APC cement sales & sector structure (MAR-021); NIR IPPU (MAR-001); open sectoral indicators (MAR-002). |
| Chemicals/metals facility process data | **No suitable comprehensive open facility process registry identified** (OCP reports are company-level, not full IPPU open DB). |
| Emissions | NIR; Climate TRACE industrial assets. |

### IV.2 Product use (F-gases, etc.) — **Partial (emissions only)**

| Need | Finding |
|---|---|
| Refrigerant/product sales stocks | **No suitable open refrigerant sales registry identified.** |
| Emissions | NIR HFC/product-use estimates (MAR-001) — national. |

---

## AFOLU

### V.1 Livestock — **Yes (national activity)**

| Need | Finding |
|---|---|
| Livestock populations | 2025 national livestock census aggregates (MAR-022); data.gov.ma sectoral indicators (MAR-002); FAOSTAT (MAR-028). |
| Manure systems / municipal herds | Open manure-management + farm geocodes: **No suitable dataset identified**. |
| Emissions | NIR agriculture; EDGAR; FAOSTAT-driven estimates. |

### V.2 Land — **Partial (Yes with RS + national inventory)**

| Need | Finding |
|---|---|
| Land cover / forest | ANEF/IFN via FRA & national forest stats (MAR-023); GFW (MAR-026); ESA WorldCover (MAR-027); NIR LULUCF (MAR-001). |
| Parcel carbon stocks inside cities | Official open urban carbon stock cadastre: **No suitable dataset identified** (use RS + national factors). |

### V.3 Aggregate non-CO₂ on land — **Partial**

| Need | Finding |
|---|---|
| Crops, fertilizer, burning | Sectoral indicators (MAR-002); FAOSTAT (MAR-028); NIR agriculture (MAR-001). |
| Municipal fertilizer application / rice (limited in Morocco) | Fine-scale open application maps: **No suitable dataset identified**. |

---

## Other Scope 3

### VI.1 Other Scope 3 — **None (standardized city CB inventories)**

City consumption-based / EEIO inventories published as open reusable datasets: **No suitable dataset identified**.  
Supporting only: HCP expenditure/trade yearbook tables (MAR-010); optional international EEIO (not Morocco-city official).  
Regional PCT GHG narratives (MAR-029) are Potential/scoping only.

---

## Coverage summary

| GPC | Subsector | Dataset found? | Best public anchors |
|---|---|---|---|
| I.1 | Residential | Partial | ONEE, MEM, Lydec/SRM (Casa), HCP, NIR, EDGAR |
| I.2 | Commercial/institutional | Partial | Same as I.1; NIR; EDGAR |
| I.3 | Manufacturing energy | Partial | MEM/ONEE, APC, NIR, Climate TRACE |
| I.4 | Energy industries | Yes | ONEE, ANRE, GPPD, NIR |
| I.5 | Agri/forestry/fishing energy | Partial | MEM energy shares; NIR |
| I.6 | Non-specified | Partial | Energy-balance residual only |
| I.7 | Coal fugitive | No* | *Generally not city-relevant |
| I.8 | Oil/gas fugitive | Partial | MEM/ONHYM, NIR |
| II.1 | On-road | Partial | NARSA, fuel market reports, NIR |
| II.2 | Rail | Partial | ONCF KPIs, NIR |
| II.3 | Waterborne | Yes (activity) | ANP, Tanger Med |
| II.4 | Aviation | Yes (activity) | ONDA |
| II.5 | Off-road | No | — |
| III.1 | Solid waste disposal | Partial | PNDM/NIR |
| III.2 | Biological treatment | No | — |
| III.3 | Incineration/open burning | No | — |
| III.4 | Wastewater | Partial | ONEE, utility filings, NIR |
| IV.1 | Industrial processes | Partial | APC, NIR |
| IV.2 | Product use | Partial | NIR HFCs only |
| V.1 | Livestock | Yes | Livestock census, FAOSTAT, NIR |
| V.2 | Land | Partial | IFN/ANEF, GFW, WorldCover, NIR |
| V.3 | Aggregate land non-CO₂ | Partial | FAOSTAT, sectoral indicators, NIR |
| VI.1 | Other Scope 3 | No | — |

\*I.7 marked **No suitable dataset identified** for city inventory use.

## Cross-cutting verdict

Morocco has a **solid national GHG inventory and energy/transport operator statistics**, plus a **useful open-data portal for sectoral indicators**. For **city-level GPC inventories**, the binding constraints are: (1) metered energy by customer class and municipality not systematically open; (2) VKT and municipal fuel sales; (3) waste facility tonnage/composition; (4) product-use stocks. **Airport, port, power-mix, livestock, and land-cover** layers are comparatively stronger.
