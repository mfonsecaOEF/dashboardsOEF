# Country context — México (MEX) — CCRA / adaptation

| Parameter | Value |
|---|---|
| Country | México |
| ISO3 | MEX |
| Languages searched | Spanish, English |
| Statistics | INEGI (Censo 2020 AGEB/manzana) |
| Poverty / deprivation | CONEVAL (GRS AGEB; pobreza urbana) |
| Open data | [datos.gob.mx](https://www.datos.gob.mx) |
| Flood / landslide | CENAPRED Atlas Nacional de Riesgos (ANR) |
| Climate | SMN / CONAGUA; INECC escenarios |
| Coastal / SLR | INECC / SEMARNAT coastal vulnerability + AR6 |
| Reference cities | CDMX / ZMVM, Guadalajara, Monterrey, Puebla, León |
| Research date | 2026-08-10 |
| Framework | `climate_risk_indicators_by_sector.json` (41 CCRA indicators) |

## Institutional map

| Domain | Key providers |
|---|---|
| Population / deprivation | INEGI Censo AGEB/manzana; CONEVAL GRS/pobreza |
| Flood | CENAPRED ANR índices + atlas estatales/municipales; CONAGUA puntos críticos |
| Landslide | CENAPRED susceptibilidad de laderas 2020 |
| Climate / drought / heat | SMN/CONAGUA; INECC; Monitor de Sequía; OEF heat_hazard |
| Coastal / SLR | INECC coastal vulnerability; IPCC AR6 |
| Energy | SENER BNE/SIE; CENACE/CFE/CRE |
| Agri / forest / PA | Censo Agropecuario / SIAP; CONAFOR INFyS; CONANP/CONABIO |
| Water / waste | CONAGUA; SEMARNAT residuos |
| OEF screening | F/H/L H+R + shared E/V (pipeline-ready) |

## Structural notes

1. **Among the strongest CCRA stacks in this set** — AGEB/manzana + CONEVAL GRS + CENAPRED national flood & landslide layers.
2. Census **drenaje** = household sanitation connection — **not** stormwater network coverage (`CCRA-039` remains a hard gap).
3. ANR flood is strong for **present** peril; **climate-change flood futures** still thinner than GBR NaFRA CC — use OEF FRI/INECC.
4. Energy poverty is **constructed** (Census electricity + CONEVAL carencias), not a DESNZ-style fuel poverty product.
