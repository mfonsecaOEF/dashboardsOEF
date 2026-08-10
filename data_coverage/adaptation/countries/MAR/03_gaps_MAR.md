# Gaps — Morocco (MAR) CCRA / adaptation

## Explicit gaps (no suitable public dataset in this pass)

| ID | Indicator | Why it matters | What we looked for | Likely next place to look |
|---|---|---|---|---|
| CCRA-007 | Confirmed disease cases | Public Health × Diseases vulnerability | MoH epidemiological bulletins, open case geodata, HDX health | Ministère de la Santé surveillance systems; WHO/national dashboards (usually aggregate, not city GIS) |
| CCRA-039 | Urban stormwater drainage coverage | Flood vulnerability (adaptive capacity) | Municipal open data Casablanca/Rabat/Marrakech; ONEE assainissement GIS | Régies/délégataires & commune SIG — typically not published |

## Soft gaps (datasets exist but weak for city CCRA)

| Theme | Issue |
|---|---|
| DGM climate | Authoritative SPI/SPEI/temp exist operationally but **not open national rasters** |
| Flood AZI | Official and high-value, but **national open coverage incomplete**; Tensift viewer is the clearest public example |
| Landslides | **No national open susceptibility GIS**; only regional papers + global models |
| Energy poverty / electricity | National/utility reports; **no open municipal customer-class extracts** (same as GPC) |
| Agricultural GDP / industrial GDP | **National only** — need regional accounts or proxies for city screens |
| Disease & drainage | Hard gaps above |
| ANEF SIPN / full SIBE GIS | Richer than WDPA likely, but **not bulk-open** |
| Water security index | Only **global Aqueduct proxy**; no official open national composite |

## Implication for product

For Morocco city CCRA screening, a practical v1 stack is:

- **E/V:** OEF shared scores fed by WorldPop/GHSL + HCP RGPH/poverty/age  
- **H:** OEF `flood_hazard` / `heat_hazard` / `landslide_hazard` (run per city AOI)  
- **R:** OEF H×E×V risk products  
- **Validate with:** ABH AZI, DGM, OSM infra; keep CHIRPS/ERA5/SPEI/SLR for drought & coast  

…with **explicit caveats** on disease incidence and stormwater drainage until municipal/MoH data opens.  
OEF mechanism-type `drainage_constrained` remains a **proxy** for the stormwater gap (`CCRA-039`).
