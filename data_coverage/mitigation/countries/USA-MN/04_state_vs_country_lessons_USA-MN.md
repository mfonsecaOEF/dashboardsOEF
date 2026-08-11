# State vs country — what Minnesota teaches about the method

**Question:** If program geography is sometimes a **state/province** (not a whole country), does our GPC city-data coverage approach still hold?

**Answer:** Yes — with three adjustments to how we *label* and *aggregate*, not to the city-level focus.

## What stayed the same (good news)

| Element | Still valid for Minnesota |
|---|---|
| Checklist | Same 23 GPC subsectors |
| Decision question | Enough public data for **city GHGI** / CityCatalyst-style work? |
| Evidence shape | Same package: context → datasets CSV → coverage → gaps |
| Program language | City-ready / Extra work / Accept downscaling still fits |
| City anchors | Minneapolis, Saint Paul, Met Council MSA play the role that PPCN (CRI) or Toronto/CEEI (CAN) play elsewhere |

The unit of *usefulness* was never “country inventory completeness.” It was always **can a city build a GHGI**. Minnesota confirms that framing survives when the host jurisdiction is a state.

## What changed (state-specific)

| Topic | Country packages | Minnesota (state) |
|---|---|---|
| Top inventory | National NIR / BTR | **State** MPCA inventory (+ EPA state GHG) |
| ISO3 | Real ISO3 | Use `USA-MN` (or similar) — do not fake a country code |
| Federal layer | Sometimes thin | **EPA GHGRP, EIA, Census** are first-class, not “international extras” |
| Utility data | Ministry / regulator | Commerce Rules 7610 + IOU/muni/coop patchwork |
| Through-traffic | Often ignored | Explicit issue: MnDOT city VMT vs community-generated VMT |
| Ranking | 9-country priority | Keep as **benchmark**, not #10 in C40 country list |

## Does “what we are doing” still serve the product?

| Use case | Verdict |
|---|---|
| Score readiness for **city programs** inside a state | **Works** — same checklist, clearer utility/DOT actors |
| Compare Minnesota to ARG/MAR/… in one priority table | **Misleading** unless you add a jurisdiction class (country vs state) |
| Validate metrics thresholds (ticket §4) | **Useful benchmark** — expect high coverage / City-ready band |
| Assume every U.S. state looks like MN | **No** — MN is relatively open (VMT by city, Met Council CPRG, active MPCA inventory) |

## Practical recommendation

1. Keep researching **city GHGI data availability** with the same GPC package shape for states/provinces when BD needs it.
2. Tag packages with `jurisdiction_type = country | state_or_province` before any combined ranking.
3. Treat Minnesota as a **positive control**: if metrics called Minnesota “Accept downscaling,” distrust the thresholds.
4. Do not dilute the 9-country C40 view by auto-merging `USA-MN` into Program priority.
