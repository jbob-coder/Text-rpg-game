# THE GAME — World Geography Standard

Status: **ACTIVE / WORLD VOLUME STANDARD**  
Parent: `docs/world/WORLD_SCALE_DOCUMENTATION_BLUEPRINT.md`  
Repository: `jbob-coder/Text-rpg-game`

## 1. Purpose

This standard defines how physical world space is represented before cities, villages, kingdoms, ecosystems, beast zones, tactical maps, or travel content are authored at scale.

It does not invent the final size of the world. It defines a coordinate and containment model capable of supporting a large world without forcing every region to share one arbitrary scale.

## 2. Spatial hierarchy

Use:

`WORLD -> MACROREGION -> REGION -> POLITICAL/ADMINISTRATIVE AREA -> SETTLEMENT -> DISTRICT -> SITE -> INTERIOR -> TACTICAL CELL`

A place may skip levels only when the missing level has no world meaning. Technical loading cells are not player-facing geography by default.

## 3. Coordinate layers

### W0 — world
Purpose:
- macroregion placement;
- global routes;
- climate bands;
- major political borders.

Coordinates remain abstract until world scale is locked.

### W1 — region
Purpose:
- regional topography;
- cities/towns/villages;
- major ecosystems;
- resource belts;
- dangerous zones;
- major routes.

### W2 — settlement
Purpose:
- settlement footprint;
- districts;
- walls/gates;
- roads;
- civic/industrial/residential areas.

### W3 — district/site
Purpose:
- player-facing local maps such as Gate Twelve;
- buildings;
- alleys;
- entrances;
- interiors;
- local route anchors.

### W4 — tactical
Purpose:
- combat/encounter geometry;
- cover;
- LOS;
- movement costs;
- hazards;
- interactable terrain.

W4 is not automatically identical to W3 pixel-art coordinates.

## 4. Stable place identity

Each place record requires:
- stable `place_id`;
- type;
- parent ID;
- display name;
- aliases;
- status;
- coordinate layer;
- coordinate/bounds;
- route anchors;
- discovery policy;
- player-safe description;
- hidden/developer metadata separated;
- visual packet pointer;
- content/scene pointers;
- world-state hooks.

IDs are never silently reused.

## 5. Boundary types

Every boundary is one of:
- physical;
- political;
- administrative;
- ecological;
- danger/threat;
- route/access;
- technical/loading;
- unknown/unmapped.

Technical boundaries must not masquerade as walls/rivers/borders unless the world actually contains them.

## 6. Terrain record

A terrain unit may define:
- elevation band;
- slope;
- surface;
- drainage/water;
- vegetation;
- traversability;
- weather sensitivity;
- tactical implications;
- resource implications;
- construction suitability.

Do not over-specify simulation values until mechanics consume them.

## 7. Water and climate

World geography must eventually account for:
- watersheds;
- rivers;
- lakes;
- coastlines;
- rainfall;
- seasonal effects;
- prevailing climate;
- agriculture/resource implications;
- travel barriers;
- settlement placement.

These relationships should explain why places exist where they do.

## 8. Settlement placement logic

A settlement should have at least one reason for location:
- water;
- route intersection;
- defensible position;
- resource extraction;
- agriculture;
- port/transit;
- religious/cultural site;
- administrative center;
- beast-zone frontier;
- historical legacy.

Random settlement placement without world logic is rejected.

## 9. Resource geography

Resources are spatial records, not generic loot tables.

Each resource area eventually points to:
- extraction site;
- abundance;
- renewal/depletion;
- owners;
- transport routes;
- settlements that consume it;
- ecological consequences;
- conflicts;
- item/material outputs.

## 10. Beast-zone geography

Beast zones must have:
- bounds;
- habitat;
- migration links;
- water/food/resource relations;
- nearby routes/settlements;
- threat band;
- expansion/contraction state;
- visual/tactical packet pointers.

## 11. Political geography

Political borders reference physical geography but do not overwrite it.

Each border must distinguish:
- claimed;
- controlled;
- disputed;
- open;
- fortified;
- culturally recognized;
- temporary/event-driven.

## 12. Scale policy

No universal real-world meter conversion is locked yet.

Each coordinate layer must declare:
- unit type;
- intended precision;
- whether distances are canonical, estimated, or presentation-only;
- conversion rule if one exists.

Gate Twelve's 256x144 presentation geometry remains a local W3 presentation grid, not proof of world meters.

## 13. World-growth rule

Expansion must attach through reserved boundaries and routes rather than by rewriting old regions whenever possible.

When geometry changes:
- preserve stable IDs;
- record old/new bounds;
- migrate route anchors;
- audit scene/map art;
- audit save references;
- add regression tests.

## 14. Required child catalogs

- political entities;
- settlements;
- routes;
- ecosystems/resources;
- beast zones;
- population/hierarchy;
- balance bands;
- loot provenance.

## 15. Gate Twelve proof mapping

Gate Twelve currently demonstrates:
- REGION/DISTRICT containment;
- stable named subzones;
- route graph;
- presentation grid;
- reserved expansion edges;
- functional macrozones.

Its lessons inform this standard but do not force every future region into the same three-band layout.
