# Canada GPC coverage assessment

Catalogue = `01_datasets_CAN.csv` (25 datasets → 117 rows; gap row for I.6).

## Summary by subsector

| GPC | Subsector | Found? | Best anchors |
|---|---|---|---|
| I.1 | Residential | Yes | StatCan energy, utility sales, NIR, Toronto/Calgary/CEEI |
| I.2 | Commercial/institutional | Yes | Same + GHGRP large buildings/facilities |
| I.3 | Manufacturing energy | Yes | RESD, GHGRP, NPRI, NIR |
| I.4 | Energy industries | Yes | NIR electricity tables, CER, GHGRP, GPPD |
| I.5 | Agri energy | Partial | RESD/Census of Agriculture supporting |
| I.6 | Non-specified | **No** | Gap row (`NO-COVERAGE-I.6`) |
| I.7 | Coal fugitive | Partial | NIR (relevant where mining occurs) |
| I.8 | Oil/gas fugitive | Yes | NIR, GHGRP, CER, AER/Petrinex |
| II.1 | On-road | Yes | Vehicle registrations + road fuel sales; CEEI/Toronto |
| II.2 | Rail | Yes | StatCan/Transport Canada rail activity; NIR |
| II.3 | Waterborne | Yes | Marine/port stats; NIR; Climate TRACE |
| II.4 | Aviation | Yes | Airport movement tables; NIR |
| II.5 | Off-road | Partial | NIR + GHGRP on-site transport |
| III.1 | Solid waste | Yes | Waste stats + GHGRP landfills; city inventories |
| III.2 | Biological treatment | Partial | Waste survey / NIR |
| III.3 | Incineration/open burning | Partial | NIR + NPRI/GHGRP where applicable |
| III.4 | Wastewater | Yes | Federal wastewater reporting; utilities; GHGRP; cities |
| IV.1 | Industrial processes | Yes | GHGRP + NIR IPPU + NPRI |
| IV.2 | Product use | Yes | NIR HFC/product-use |
| V.1 | Livestock | Yes | Census of Agriculture; NIR |
| V.2 | Land | Yes | NFI; NIR LULUCF; CEEI land-use; RS |
| V.3 | Aggregate land non-CO₂ | Yes | Census of Agriculture; NIR agriculture |
| VI.1 | Other Scope 3 | Partial | SEEA / household surveys; city CBEI examples (e.g. Toronto notes) — not a single national city CB standard dataset |

## Cross-cutting verdict

Canada has **strong official coverage** across nearly all GPC subsectors via NIR + GHGRP + StatCan, plus **mature city inventories** (Toronto, Calgary) and **BC CEEI**. The only empty mapped sector in this pass is **I.6 Non-specified** (residual category). Remaining practical city frictions: LDC meter extracts by municipality/class, municipal VKT, and refrigerant stock registers.
