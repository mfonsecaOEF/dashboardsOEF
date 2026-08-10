# Country context — México (MEX)

| Parameter | Value |
|---|---|
| Country | México / Mexico |
| ISO3 | MEX |
| Languages searched | Spanish, English |
| National statistical office | Instituto Nacional de Estadística y Geografía (INEGI) |
| Open data | [datos.gob.mx](https://www.datos.gob.mx) |
| GHG inventory lead | INECC / SEMARNAT (INEGyCEI) |
| Latest national GHG | INEGyCEI actualizado (serie ~1990–2024 / BTR1) |
| Facility reporting | RENE (≥25,000 tCO2e) vía COA Web — microdatos poco abiertos |
| Reference cities | CDMX / ZMVM, Guadalajara, Monterrey, Puebla, León |
| Energy note | BNE + SIE + CENACE/CFE fuertes; ventas municipales abiertas heterogéneas |
| Research date | 2026-08-06 |
| Framework | `GPC_Data_Availability_Framework.xlsx` (23 subsectors) |

## Institutional map

| Domain | Key providers |
|---|---|
| Statistics / energy | INEGI; SENER (BNE, SIE); CENACE; CFE; CRE |
| Emissions | INEGyCEI (INECC); RENE (SEMARNAT); factores CONUEE |
| Oil & gas | CNH; PEMEX BDI; INEGyCEI fugitivas |
| Transport | INEGI parque vehicular; SICT/AFAC; anuarios |
| Waste / water | SEMARNAT residuos; CONAGUA / organismos operadores |
| AFOLU | Censo Agropecuario / SIAP; CONAFOR INFyS |
| Subnational city products | Inventario SEDEMA ZMVM; inventarios estatales/municipales parciales |

## Structural notes

1. México es **fuerte a escala nacional** (INEGyCEI, BNE/SIE, CNH) y tiene **RENE** como registro de grandes emisores, pero a diferencia de Canadá/Australia los **microdatos RENE no se publican como CSV abierto completo**.
2. **ZMVM/CDMX (SEDEMA)** es el referente urbano más maduro con GEI; no hay estadística oficial municipal para todos los municipios tipo UK DESNZ.
3. Preferir **INEGyCEI / BNE / SIE / CENACE / INEGI / INFyS** sobre productos internacionales modelados.
4. Solo **I.6** quedó sin dataset dedicado en este pase (fila gap).
