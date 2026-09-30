# Rounds 1411–1420 — Settlement Lineage and Place-History Standard

Status: PLANNED
Live-game clock effect: NONE

1411. Define PLACE_LINEAGE record linking one geographic site through multiple settlement/institution versions.
1412. Define foundation-state fields: why founded, founding authority, original population, original footprint, original access routes.
1413. Define growth-state fields: annexations, new districts, utilities, roads, transit, defensive perimeters, population capacity.
1414. Define disaster-state fields: damaged area, unusable structures, casualty/displacement zones, contamination, route failures.
1415. Define abandonment/reuse fields: ruins, salvage, squatting, ecological succession, redevelopment, memorialization.
1416. Define jurisdiction-history model for boundary changes, occupation, corporate control, municipal creation, wartime administration.
1417. Define population/capacity timeline with low/medium/high confidence instead of false exact counts.
1418. Build one worked example spanning at least four historical versions of the same place.
1419. Write one place-centered microhistory showing how three generations experience the same street differently.
1420. QA against existing Veinfall, industrial, portal, Kharvori, war, and 2670 spatial standards.

Planned artifacts:
- reference/PLACE_LINEAGE_STANDARD_V1.md
- templates/PLACE_HISTORY_RECORD_TEMPLATE.md
- templates/PLACE_TEMPORAL_VERSION_TEMPLATE.md
- book/MICROHISTORY_THE_SAME_STREET_THREE_GENERATIONS.md
- qa/PLACE_LINEAGE_VERSIONING_TESTS_V1.md

Spatial requirements:
- anchor coordinate;
- versioned footprint;
- versioned height/density;
- route changes;
- utility changes;
- population/capacity change;
- demolished/rebuilt polygons.

Story target:
A location must become recognizable as the same place even after architecture, ownership, and social meaning change.
