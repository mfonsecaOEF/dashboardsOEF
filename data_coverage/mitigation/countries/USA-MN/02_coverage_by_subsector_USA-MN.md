# Minnesota GPC coverage assessment

Catalogue = `01_datasets_USA-MN.csv` (26 datasets → 137 rows; gap rows for I.6 and I.7).

## Summary by subsector

| GPC | Subsector | Found? | Best anchors |
|---|---|---|---|
| I.1 | Residential | Yes | Commerce/EIA utility sales; eGRID; MPCA/EPA; Minneapolis / St Paul / Met Council |
| I.2 | Commercial/institutional | Yes | Same + GHGRP large facilities |
| I.3 | Manufacturing energy | Yes | EIA/Commerce; GHGRP; NEI; Met Council industrial |
| I.4 | Energy industries | Yes | GHGRP power plants; EIA; eGRID; GPPD |
| I.5 | Agri energy | Partial | SEDS + Commerce + NASS farm context |
| I.6 | Non-specified | **No** | Gap row (`NO-COVERAGE-I.6`) |
| I.7 | Coal fugitive | **No** | Gap row (`NO-COVERAGE-I.7`) — no meaningful coal mining |
| I.8 | Oil/gas fugitive | Partial | GHGRP + PHMSA + distribution (little upstream) |
| II.1 | On-road | Yes | **MnDOT VMT by city/county**; fuel sales; city/MSA inventories |
| II.2 | Rail | Partial | BTS/FRA + MPCA/EPA + Climate TRACE |
| II.3 | Waterborne | Partial | Duluth-Superior / USACE; limited for Twin Cities |
| II.4 | Aviation | Yes | FAA/BTS MSP + inventory sectors |
| II.5 | Off-road | Partial | SEDS/fuels + fleet + state inventory |
| III.1 | Solid waste | Yes | MPCA SCORE; GHGRP landfills; city/MSA inventories |
| III.2 | Biological treatment | Partial | SCORE / waste reports + state inventory |
| III.3 | Incineration/open burning | Partial | SCORE/facility + GHGRP where applicable |
| III.4 | Wastewater | Yes | Met Council / utilities; city inventories; GHGRP |
| IV.1 | Industrial processes | Yes | GHGRP + NEI/TRI + state/MSA inventories |
| IV.2 | Product use | Partial | State/EPA IPPU + GHGRP suppliers (city stocks weak) |
| V.1 | Livestock | Yes | NASS county + MPCA/EPA agriculture |
| V.2 | Land | Yes | MPCA LULUCF sink + DNR/USFS; Met Council natural systems |
| V.3 | Aggregate land non-CO₂ | Yes | NASS + MPCA/EPA agriculture |
| VI.1 | Other Scope 3 | Partial | Met Council / city notes + ACS proxies — not a single statewide CBEI standard |

## Cross-cutting verdict

Minnesota looks **City-ready as a state host for city GHGIs**: official state inventory, federal GHGRP, regulated utility reporting, **city-published VMT**, and live Twin Cities inventory products (Minneapolis, Saint Paul, Met Council MSA). Gaps that remain are the same *class* as in rich countries: residual I.6, irrelevant I.7, refrigerant stocks, and tidy **city-boundary utility extracts** without bilateral data-sharing.

**Program approach (qualitative):** **City-ready** for Twin Cities and other MN cities that can obtain utility class extracts — closer to CAN/CRI than to MAR/ETH. Smaller cities outside the metro still lean on county/state downscaling for some sectors.
