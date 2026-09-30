# SPATIAL_REGISTRY_INDEX

Status: ACTIVE_ARCHITECTURE
Authority: SPATIAL_REFERENCE_STANDARD_V1
Purpose: index of persistent coordinates and dimensions used by world history and scenario construction

## Current rules

Canonical standard:
- docs/world_history/spatial/SPATIAL_REFERENCE_STANDARD_V1.md

Template:
- docs/world_history/templates/SPATIAL_ENTITY_TEMPLATE.md

## Registry families

Future records should use:
- WORLD_*
- REGION_*
- SETTLEMENT_*
- DISTRICT_*
- SITE_*
- CAMPUS_*
- BUILDING_*
- FLOOR_*
- ROOM_*
- ZONE_*
- PORTAL_SITE_*
- BATTLEFIELD_*
- HABITAT_*
- ROUTE_*

## Current populated atlases

- SPATIAL_STORY_ATLAS_1600_1896_V1.md — historical sites used in Book 02 Chapter 01.
- SPATIAL_STORY_ATLAS_1896_2228_V1.md — hidden-program sites used in Book 02 Chapter 02.

## Current persistent historical sites

1600–1896:
- SITE_GREYBRIDGE_INFIRMARY_1738
- SITE_VALE_ANATOMICAL_HALL_1811
- SITE_MERROW_INSTRUMENT_HOUSE_1867
- SITE_CALDER_STATE_RESEARCH_ANNEX_1896

1896–2228:
- SITE_NORTHMERE_SECURE_ARCHIVE_1904
- SITE_BRAEWOOD_FIELD_EVALUATION_RANGE_1918
- SITE_RAVELIN_MEDICAL_VARIANCE_CENTER_1946
- SITE_HELIX_SIGNAL_ANALYTICS_CENTER_2038
- SITE_KAIROU_GENOMIC_OBSERVATORY_2088
- SITE_MERIDIAN_EXCHANGE_NODE_2228

## Rule

A location is not considered spatially locked merely because prose mentions it.
It becomes spatially locked only when a spatial record gives a frame, dimensions where applicable, temporal validity, and uncertainty class.

Do not silently reuse a historical site's later footprint for an earlier/later era after renovation, destruction, abandonment, or expansion.
