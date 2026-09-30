# Rounds 1311–1320 — Temporal Spatial Versioning and Microhistory Compiler

Status: PLANNED
Live-game clock effect: NONE

1311. Build temporal-version schema for one place across multiple historical eras.
1312. Create inheritance rule for coordinates when structures are rebuilt, moved, expanded, buried, flooded, or abandoned.
1313. Define spatial-diff format: footprint change, floor change, route change, access change, population/capacity change.
1314. Define microhistory record: place + year + ordinary actor + event pressure + lived consequence + later historical interpretation.
1315. Create "same street, different century" story template using pre-Crystal / post-Veinfall / 2670 versions.
1316. Create "same facility, different doctrine" template for hospital, depot, training center, or portal hub.
1317. Build coordinate provenance field set so later authors know which measurements are fixed, reconstructed, public, classified, or unknown.
1318. Define demolition/ruin/reuse rules for scenario generation.
1319. Create temporal-spatial query examples by ERA + REGION + SITE + YEAR.
1320. QA against existing Veinfall, Early Crystal, Portal Expansion, and Kharvori atlases.

Planned artifacts:
- reference/TEMPORAL_SPATIAL_VERSIONING_STANDARD_V1.md
- reference/MICROHISTORY_RECORD_STANDARD_V1.md
- templates/TEMPORAL_SPATIAL_DIFF_TEMPLATE.md
- templates/MICROHISTORY_PLACE_STORY_TEMPLATE.md
- qa/TEMPORAL_SPATIAL_VERSIONING_TESTS_V1.md

Story target:
A readable author-history vignette showing one ordinary location changing function across at least three eras without changing its underlying coordinate identity unless the record explicitly says it moved.

Spatial target:
At least three versioned footprints with dimension deltas and valid_from/valid_to windows.
