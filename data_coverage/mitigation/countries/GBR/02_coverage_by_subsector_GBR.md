# United Kingdom GPC coverage assessment

Catalogue = `01_datasets_GBR.csv` (25 datasets → 141 rows; gap row for I.6).

## Summary by subsector

| GPC | Subsector | Found? | Best anchors |
|---|---|---|---|
| I.1 | Residential | Yes | Subnational electricity/gas; LA GHG; DUKES; LEGGI |
| I.2 | Commercial/institutional | Yes | Same + non-domestic meters; Pollution Inventory large sites |
| I.3 | Manufacturing energy | Yes | Subnational energy; PI/PRTR; LA GHG; GHGI |
| I.4 | Energy industries | Yes | DUKES; NESO; PI; NSTA; LA GHG; GHGI |
| I.5 | Agri energy | Partial | DUKES + residual fuels + agricultural structure |
| I.6 | Non-specified | **No** | Gap row (`NO-COVERAGE-I.6`) |
| I.7 | Coal fugitive | Partial | GHGI only (limited remaining UK mining) |
| I.8 | Oil/gas fugitive | Yes | GHGI; NSTA; PI; LA GHG (where allocated) |
| II.1 | On-road | Yes | DfT TRA89 VKT; vehicle licensing; LA road fuel; LA GHG |
| II.2 | Rail | Yes | ORR; LA GHG (rail allocation); GHGI |
| II.3 | Waterborne | Partial | DfT ports/maritime + GHGI; **excluded from LA GHG** |
| II.4 | Aviation | Partial | CAA airports + GHGI; **excluded from LA GHG** |
| II.5 | Off-road | Partial | GHGI + PI on-site; conversion factors |
| III.1 | Solid waste | Yes | WasteDataFlow / Defra LA waste; LA GHG; PI landfills |
| III.2 | Biological treatment | Yes | WasteDataFlow composting/AD destinations |
| III.3 | Incineration/open burning | Yes | WasteDataFlow EfW; PI incinerators; LA GHG |
| III.4 | Wastewater | Yes | PI large STWs; utilities; LA GHG; GHGI |
| IV.1 | Industrial processes | Yes | PI/PRTR; GHGI IPPU; LA GHG |
| IV.2 | Product use | Partial | GHGI F-gases / conversion factors; **not in LA GHG** |
| V.1 | Livestock | Yes | June Agricultural Survey; LA GHG; GHGI |
| V.2 | Land | Yes | NFI; UKCEH LULUCF LA; LA GHG; LEGGI |
| V.3 | Aggregate land non-CO₂ | Yes | Agriculture stats; LA GHG; GHGI |
| VI.1 | Other Scope 3 | Partial | ONS environmental accounts; conversion factors; LEGGI notes — no single national city CBEI standard |

## Cross-cutting verdict

The UK is the strongest package so far for **city-ready official inputs**: DESNZ local authority GHG statistics plus LSOA/MSOA electricity and gas meters, DfT LA traffic, and WasteDataFlow. Remaining hard spots mirror DESNZ’s own LA exclusions — **aviation, shipping, F-gases** — plus residual **I.6** and thin open **city refrigerant stocks**.
