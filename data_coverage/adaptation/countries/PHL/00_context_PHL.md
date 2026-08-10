# Country context — Philippines (PHL) — CCRA / adaptation

| Parameter | Value |
|---|---|
| Country | Philippines / Filipinas / Pilipinas |
| ISO3 | PHL |
| Languages searched | English (+ Filipino/Tagalog terms as needed) |
| National statistical office | Philippine Statistics Authority (PSA) — [OpenSTAT](https://openstat.psa.gov.ph/) |
| Meteorology / climate | DOST-PAGASA (drought advisories, CliMap) |
| Multi-hazard maps | DOST / UP Resilience Institute — **Project NOAH** |
| Mapping agency | NAMRIA; [Philippine Geoportal](https://www.geoportal.gov.ph/) |
| Humanitarian hub | [HDX Philippines](https://data.humdata.org/group/phl) |
| Reference cities | Quezon City, Manila, Makati, Cebu City, Davao City, Taguig |
| Geography note | Archipelagic + highly coastal — **SLR / storm surge / ports highly relevant** |
| Research date | 2026-08-10 |
| Framework | `geospatial-data/docs/climate_risk_indicators_by_sector.json` (41 unique CCRA indicators) |

## Institutional map

| Domain | Key providers |
|---|---|
| Population / poverty / WASH | PSA CPH 2020 (barangay), FIES/poverty, OpenSTAT, HDX |
| Admin boundaries | COD-AB (PSGC 10-digit) |
| Flood / landslide / surge | **Project NOAH** (primary); Geoportal |
| Climate / drought / heat | PAGASA CliMap + drought/SPEI products; CHIRPS/ERA5 gap-fills |
| Sea level / coast | NASA/IPCC SLR + NOAH storm surge; PPA ports |
| Biodiversity | WDPA / KBA; DENR-BMB NIPAS |
| Agriculture / irrigation | PSA/DA OpenSTAT; NIA; WaPOR |
| Energy | DOE Power Statistics; Meralco/coops; HECS |
| Health facilities | DOH NHFR; healthsites.io |
| OEF screening | flood / heat / landslide H+R + shared E/V + mechanisms (pipeline-ready) |

## Structural notes for city CCRA

1. **Strongest hazard stack in this country set:** Project NOAH open flood (5/25/100-yr), landslide, and storm-surge maps (ODC-ODbL).
2. **Strongest E/V stack:** PSA Census 2020 at **barangay** (age/sex) plus city/municipality WASH/housing — rare fine grain.
3. **PAGASA CliMap** gives municipal historical + CMIP6 futures for temperature/rainfall — good official climate horizons.
4. **OEF screening** remains listed as easy-to-run complement (esp. urban heat LST; SSP FRI futures; H×E×V composites with PSA E/V). Prefer NOAH as primary flood/landslide H.
5. Hard gap remains **urban stormwater drainage coverage**; disease cases only via NDHS prevalence (soft).
