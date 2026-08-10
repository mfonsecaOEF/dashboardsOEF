# Country context — United Kingdom (GBR)

| Parameter | Value |
|---|---|
| Country | United Kingdom / Royaume-Uni |
| ISO3 | GBR |
| Languages searched | English (Welsh/Gaelic portals checked for DA products) |
| National statistical office | Office for National Statistics (ONS) |
| Open data | [data.gov.uk](https://www.data.gov.uk) / GOV.UK statistics |
| GHG inventory lead | Department for Energy Security and Net Zero (DESNZ) via NAEI (Ricardo) |
| Latest national GHG | NID / UK GHGI 1990–2024 (2026 submission) |
| Facility reporting | Environment Agency Pollution Inventory / UK PRTR (+ SEPA/NIEA parallels) |
| Reference cities | London (LEGGI), Manchester, Birmingham, Glasgow, Cardiff, Belfast |
| Energy note | Subnational electricity & gas meters to LSOA/MSOA — unusually strong for city inventories |
| Research date | 2026-08-06 |
| Framework | `GPC_Data_Availability_Framework.xlsx` (23 subsectors) |

## Institutional map

| Domain | Key providers |
|---|---|
| Statistics / energy | ONS; DESNZ DUKES & Energy Trends; subnational electricity/gas |
| Emissions | DESNZ/NAEI GHGI (NID); LA & regional GHG statistics; conversion factors |
| Transport | DfT road traffic & vehicle licensing; DESNZ LA road fuel; ORR; CAA; DfT maritime |
| Waste / water | WasteDataFlow / Defra (+ DA); Pollution Inventory STWs; water companies |
| AFOLU | June Agricultural Survey; Forest Research NFI; UKCEH LULUCF LA maps |
| Oil & gas | NSTA; NAEI/GHGI fugitives; Pollution Inventory |
| Subnational city products | DESNZ LA GHG (all LAs); LEGGI (London); SCATTER-using LAs |

## Structural notes

1. The UK is **exceptionally strong at local-authority scale** via DESNZ LA GHG statistics + subnational meter data — closer to “ready city inventory inputs” than most countries in this batch.
2. **Gaps at LA level** (explicit in DESNZ docs): aviation, shipping, military transport, and **F-gases**.
3. Prefer **DESNZ LA GHG / subnational energy / GHGI** over modeled international products when both exist.
4. Only residual category **I.6** lacked a dedicated mapped dataset in this pass (gap row added). Coal fugitives (**I.7**) are covered nationally via GHGI only (limited UK mining).
