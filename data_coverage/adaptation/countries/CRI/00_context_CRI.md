# Country context — Costa Rica (CRI) — CCRA / adaptation

| Parameter | Value |
|---|---|
| Country | Costa Rica |
| ISO3 | CRI |
| Languages searched | Spanish, English |
| Statistics | INEC (Censo 2011; población/vivienda 2022 distrito; proyecciones) |
| Deprivation | PNUD–UCR Atlas Desarrollo Humano Cantonal (IDH/IPM) |
| Open data / SNIT | [snitcr.go.cr](https://www.snitcr.go.cr/) / [datosabiertos.go.cr](https://www.datosabiertos.go.cr/) |
| Flood / landslide | CNE threat layers via SNIT OGC |
| Climate | IMN observations + proyecciones regionalizadas / DCC-MINAE |
| Coastal / SLR | IMN/MINAE coastal assessments + IPCC AR6 |
| Reference cities | San José, Alajuela, Cartago, Heredia (GAM cantones) |
| Research date | 2026-08-10 |
| Framework | `climate_risk_indicators_by_sector.json` (41 CCRA indicators) |

## Institutional map

| Domain | Key providers |
|---|---|
| Population / poverty | INEC distrito; Atlas DH cantonal (IPM/IDH) |
| Flood / landslide | CNE via SNIT; municipal atlases / DesInventar |
| Climate / drought / heat | IMN + DCC-MINAE; OEF heat_hazard |
| Coastal / SLR | IMN/MINAE + AR6 |
| Energy | SEPSE BNE / ARESEP / ICE (highly renewable) |
| Agri / forest / PA | ENA/MAG; SENARA; SINAC/FONAFIFO ASP |
| Water | AyA / ASADAS; SENARA–SINIGIRH aquifers |
| OEF screening | F/H/L H+R + shared E/V (pipeline-ready) |

## Structural notes

1. **CNE+SNIT** give open national inundation & landslide threat layers — strong Hazard path for a small country.
2. **E/V grain is coarser** than MEX/GBR/AUS: distrito (~491) + cantonal IPM, not AGEB/LSOA/SEIFA.
3. Electricity is **nearly universal and renewable** — energy poverty less discriminating.
4. **Hard gap:** stormwater drainage *coverage* (pipe %).
5. GAM city AOIs are **multi-cantón / multi-distrito** by design.
