# Research log — Philippines (PHL) CCRA / adaptation

| Date | Action |
|---|---|
| 2026-08-10 | Started PHL adaptation package |
| 2026-08-10 | Searched: PSA OpenSTAT/CPH 2020 HDX barangay, COD-AB, Project NOAH flood/landslide/surge (UPRI + mirrors), PAGASA drought/CliMap, NAMRIA/Geoportal, PPA, DOE/HECS, DOH NHFR, WDPA/KBA, WaPOR/NIA, global CHIRPS/ERA5/SPEI/SLR |
| 2026-08-10 | Listed full OEF screening family as pipeline-ready complement (NOAH preferred for flood/landslide H) |
| 2026-08-10 | Hard gap: `CCRA-039` stormwater; soft: disease surveillance |
| 2026-08-10 | Wrote context, CSV (122 rows), coverage, gaps, log |

## Decisions

- Treat **Project NOAH** as primary official hazard for flood, landslide, and storm surge.
- Treat **PSA 2020 barangay** as primary E/V backbone.
- Keep OEF products even where NOAH dominates — easy to run; useful for heat LST, SSP FRI, and H×E×V packaging.
- Emit stormwater `NO-COVERAGE` despite mechanism proxy.
