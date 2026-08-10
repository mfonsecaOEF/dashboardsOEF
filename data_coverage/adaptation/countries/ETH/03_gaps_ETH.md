# Gaps — Ethiopia (ETH) CCRA / adaptation

## Explicit gaps (no suitable public dataset in this pass)

| ID | Indicator | Why | What we looked for | Next place |
|---|---|---|---|---|
| CCRA-035 | Sea Level change | **Not geographically applicable** — Ethiopia is landlocked | NASA/IPCC SLR, coastal DEM | Only relevant if product expands to Djibouti corridor / partner ports outside ETH |
| CCRA-039 | Urban stormwater drainage coverage | Adaptive capacity for pluvial flood | Addis/other municipal open GIS; AAWSA drainage | City utilities / municipal SIG (typically unpublished) |

## Soft gaps (weak / proxy only)

| Theme | Issue |
|---|---|
| Confirmed disease cases (`CCRA-007`) | DHS prevalence only — MoH DHIS2 case GIS not open |
| Port infrastructures (`CCRA-029`) | No seaport — OSM dry ports / Ethio–Djibouti rail as logistics proxy |
| NMA climate | Authoritative but not open city rasters |
| Landslide national GIS | Rich academic/GSE literature; bulk open COG portal lacking |
| EEU retail electricity | Same as GPC — no systematic open woreda/customer-class extract |
| Agricultural / industrial GDP | National (or regional) — needs downscaling |
| Water security index | Global Aqueduct proxy only |

## Product implication

City CCRA v1 in Ethiopia can lean hard on **OEF flood/heat/landslide screening + WorldPop/COD-PS E + DHS/HCES V**, with **SLR omitted** and **stormwater** flagged as unknown until municipal data opens. Mechanism-type `drainage_constrained` remains a proxy for the stormwater gap.
