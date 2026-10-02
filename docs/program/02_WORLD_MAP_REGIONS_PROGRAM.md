# World, Map and Regions Program

Status: ACTIVE / ARCHITECTURE
Pilot: Gate Twelve District

## Scope

Owns spatial/world documentation for:
- world hierarchy;
- realms/kingdoms/polities;
- regions;
- cities;
- villages;
- districts;
- interiors;
- routes;
- coordinates;
- terrain;
- resource zones;
- beast zones;
- ecosystem boundaries;
- expansion stubs;
- loading/streaming partitions when they become technical requirements.

## Spatial hierarchy

Target planning hierarchy:

`WORLD -> POLITY/KINGDOM -> REGION -> SETTLEMENT/CITY -> DISTRICT -> LOCATION -> SUBLOCATION/INTERIOR -> INTERACTION ANCHOR`

Technical loading cells may exist beneath this hierarchy but must not automatically become player-facing geography.

## Coordinate policy

Every map layer must declare its coordinate system. Do not silently mix:
- world geographic coordinates;
- region coordinates;
- local presentation pixels;
- node percentages;
- UI viewport coordinates.

Gate Twelve currently demonstrates this rule with gameplay node percentages separate from a 256x144 presentation master.

## Settlement planning contract

Each settlement eventually documents:
- role in world;
- population band;
- controlling authority;
- economy/resources;
- class/hierarchy distribution;
- districts;
- entrances/exits;
- transport;
- important NPC populations;
- services;
- risks/threats;
- beast/ecology interaction;
- quest/content hooks;
- expansion boundaries;
- visual/material identity;
- world-state variants.

## External-reference extraction

Adopt:
- central orientation nodes;
- modular districts;
- side branches;
- entrances/exits reserved for expansion;
- reusable building families;
- build-by-section production.

Reject as automatic canon:
- exact section count;
- exact building count;
- exact dimensions;
- exact color coding;
- medieval-specific forms;
- names and lore.

## World-scale map corpus

The owner's large map-documentation target is decomposed by hierarchy instead of one enormous file. Each map unit should be independently addressable and cross-linked.

Minimum document families:
- WORLD_OVERVIEW
- POLITY_*
- REGION_*
- SETTLEMENT_*
- DISTRICT_*
- ROUTE_*
- RESOURCE_ZONE_*
- BEAST_ZONE_*
- ECOSYSTEM_*
- MAP_COORDINATE_CONTRACT_*
- MAP_STATE_VARIANTS_*

## Pilot dependencies

Gate Twelve authoritative inputs:
- `docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md`
- `docs/assets/GATE_TWELVE_MAP_PIXEL_ASSET_BLUEPRINT.md`
- `content/vertical_slice_01.json`
- `PixelMapArtCatalog.kt`

## Required next decisions

- Gate Twelve geometry contract is documented in the Master Plan; implementation/migration evidence remains pending where applicable;
- Plaza <-> Platform Nine gameplay migration decision;
- larger surface-world destination outside Depot Plaza;
- Quiet Stair external destination;
- Service Tunnel deeper destination;
- regional/world coordinate model;
- world settlement density;
- world travel-time model;
- loading/streaming boundaries;
- world-level scaling relationship to geography.

## Acceptance rule

A map is implementation-ready only when geography, authored node IDs, route ownership, visual geometry, runtime states and expansion boundaries no longer contradict one another.


## Global world foundation documents now created

- `docs/world/WORLD_SPATIAL_HIERARCHY_AND_COORDINATES.md`
- `docs/world/WORLD_ENTITY_ID_AND_REFERENCE_STANDARD.md`
- `docs/world/REGION_SETTLEMENT_DOCUMENTATION_TEMPLATE.md`
- `docs/world/WORLD_MAP_PRODUCTION_SEQUENCE.md`

These documents lock the hierarchy and documentation method without inventing the actual world geography.

Still unresolved:
- actual global geography;
- actual polity/kingdom list;
- actual region list;
- final WORLD_GEO coordinate representation;
- settlement density;
- regional travel-time model;
- beast/resource/ecosystem placement.


## Gate Twelve outward-expansion subdocument

- `docs/world/GATE_TWELVE_EXTERNAL_CONNECTIONS_AND_EXPANSION_REGISTER.md` — records the district's outward interfaces, unresolved destinations, route-creation gates, and separation between external expansion and the proposed internal Plaza <-> Platform Nine bridge.
