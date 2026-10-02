# Gate Twelve External Connections and Expansion Register

Status: **REVIEWABLE / WORLD EXPANSION SUBDOCUMENT**
Program: `D-01 World / Map / Regions`
Authority/evidence class: `CONFIRMED_DOCUMENTED + UNKNOWN + PROPOSED`
Pilot: `Gate Twelve District`

## Purpose

Own the boundary between the documented Gate Twelve district and the still-undefined larger world.

This file does not invent the outside world. It records every known expansion edge, its current authority status, what is still missing, and the conditions required before an edge becomes a real gameplay route.

## Upstream

- `EXISTING::docs/program/02_WORLD_MAP_REGIONS_PROGRAM.md`
- `EXISTING::docs/program/09_DECISION_GAP_REGISTER.md`
- `EXISTING::docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md`
- `EXISTING::docs/world/WORLD_SPATIAL_HIERARCHY_AND_COORDINATES.md`
- `EXISTING::docs/world/WORLD_ENTITY_ID_AND_REFERENCE_STANDARD.md`
- `EXISTING::docs/world/WORLD_MAP_PRODUCTION_SEQUENCE.md`

## Downstream consumers

- future WORLD/POLITY/REGION/SETTLEMENT documents;
- future route records;
- world-map UI;
- travel-time rules;
- discovery/access rules;
- loading/streaming boundaries where later required;
- map art and route overlays;
- save/migration logic if routes become persistent gameplay state.

## 1. Ownership

This document owns only the outward expansion interfaces of Gate Twelve.

It does **not** own:
- final world geography;
- final polity or kingdom list;
- regional travel formulas;
- exact coordinates outside Gate Twelve;
- final settlement density;
- new NPCs, quests, ecosystems, resources, or beasts beyond already documented scope.

## 2. Current confirmed internal boundary state

Gate Twelve is a DISTRICT-level pilot inside a larger hierarchy:

`WORLD -> POLITY -> REGION -> SETTLEMENT -> DISTRICT -> LOCATION -> SUBLOCATION -> INTERACTION_ANCHOR`

Gate Twelve already has documented local locations and routes. External expansion must connect through stable entities rather than decorative map edges.

## 3. Expansion interfaces

### GT-EXT-001 — Depot Plaza outward surface connection

Evidence class: `UNKNOWN`

Known:
- Depot Plaza is the public orientation hub of the Surface Civic District.
- The larger surface-world destination outside Depot Plaza is not yet defined.

Unknown:
- destination stable ID;
- parent settlement/region relationship outside Gate Twelve;
- route class;
- directionality;
- travel cost/time;
- discovery/access conditions;
- world-state variants;
- visual representation.

Rule:
Do not create a canonical outside destination in art or UI until the destination entity and route identity exist.

### GT-EXT-002 — Quiet Stair outward connection

Evidence class: `UNKNOWN`

Known:
- Quiet Stair / EVAC_STAIR is an alternate evacuation/egress branch in the Lower Maintenance Network.
- Its external destination remains undefined.

Unknown:
- whether it exits to surface, another district, service infrastructure, or another region layer;
- route class and travel semantics;
- access restrictions;
- discovery state;
- world-state variants.

Rule:
Reserve the boundary without presenting an invented destination as reachable.

### GT-EXT-003 — Service Tunnel deeper continuation

Evidence class: `UNKNOWN`

Known:
- Service Tunnel is the deeper maintenance continuation from Gate Twelve.
- A deeper destination exists conceptually as an expansion direction, but its actual identity is not documented.

Unknown:
- destination entity;
- whether the continuation remains inside the same settlement/district hierarchy or crosses into another district/region;
- travel model;
- hazards/access rules;
- ecosystem/beast/resource relationship;
- streaming boundary if later required.

Rule:
Do not convert the continuation into a canonical destination until its parent hierarchy and route record are defined.

### GT-EXT-004 — Depot Plaza <-> Platform Nine internal bridge

Evidence class: `PROPOSED / DOCUMENTED DESIGN`

Known:
- the current authored gameplay graph has separate surface and depot/lower components;
- the design documentation identifies `DISTRICT_PLAZA <-> PLATFORM_NINE` as the preferred connector;
- the decision-gap register still records that the connector is not implemented in the authored graph.

Rule:
This is an internal district migration, not an external-world route. It must remain distinct from GT-EXT-001.

## 4. Route creation gate

An expansion edge may become a gameplay route only when all of the following exist:

1. destination stable entity ID;
2. parent hierarchy placement;
3. route stable ID;
4. coordinate spaces for both endpoints;
5. directionality;
6. discovery/access rules;
7. travel cost/time model or explicit deferred field;
8. hazard/state-variant semantics where relevant;
9. UI/map representation rule;
10. persistence/migration impact when route state is saved;
11. verification plan.

Missing required data keeps the edge `UNKNOWN`, `PROPOSED`, or `BLOCKED`; it does not become canon through artwork.

## 5. Current-to-target delta

Current:
- Gate Twelve has local documented geography and known outward interfaces.
- actual external destinations are largely undefined.

Target:
- each outward interface connects to a stable world entity through a stable route record;
- world hierarchy, map UI, travel rules, content, and art reference the same identities;
- hidden or future destinations remain concealed until gameplay state permits discovery.

Delta:
- author global geography;
- choose WORLD_GEO representation;
- define parent settlement/region around Gate Twelve;
- define outward destination entities;
- define route records and travel semantics;
- integrate map/UI/runtime state;
- verify persistence and migration.

## 6. Revision triggers

Revise when:
- the world hierarchy around Gate Twelve is authored;
- any GT-EXT destination receives a stable ID;
- a route becomes implemented;
- WORLD_GEO is selected;
- travel-time or discovery systems change;
- the district is moved under a different parent settlement/region.

## 7. Acceptance

This subdocument is accepted when future world expansion can identify Gate Twelve's unresolved edges without inventing locations from chat memory or map art.

## 8. Next unresolved action

Define the parent settlement/region context around Gate Twelve before assigning canonical external destinations.