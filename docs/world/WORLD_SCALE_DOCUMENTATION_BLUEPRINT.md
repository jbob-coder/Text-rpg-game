# THE GAME — World-Scale Documentation Blueprint

Status: **ACTIVE / SCHEMA-FIRST**  
Parent: `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`  
Purpose: define how the future large world is documented before thousands of places, resources, beasts, NPCs, and loot records are authored.

## 1. Core rule

Do not generate a large world as disconnected names.

Every world record must know:
- where it is;
- what contains it;
- what it contains;
- how it connects;
- who controls or uses it;
- what resources/ecology exist;
- what level/danger expectations apply;
- what changes over time;
- what game systems consume it.

## 2. Spatial hierarchy

Use stable hierarchy:

`WORLD -> MACROREGION/CONTINENT -> POLITICAL ENTITY -> REGION/PROVINCE -> SETTLEMENT/WILDERNESS ZONE -> DISTRICT -> SITE -> INTERIOR/ROOM -> TACTICAL CELL`

Not every layer is required for every place.

Examples:
- wilderness may skip settlement/district;
- an underground network may attach directly to a city district;
- a tactical encounter cell may be ephemeral and not permanent world geography.

## 3. Coordinate spaces

### W0 — World coordinate
Purpose:
- macro geography;
- continent/macroregion placement.

Final units: **not yet locked**.

### W1 — Regional coordinate
Purpose:
- cities;
- villages;
- resource zones;
- beast zones;
- roads;
- rivers;
- borders.

### W2 — Settlement coordinate
Purpose:
- districts;
- gates;
- transit;
- civic centers;
- neighborhoods.

### W3 — District/site coordinate
Purpose:
- buildings;
- plazas;
- interiors;
- local paths;
- underground connectors.

Gate Twelve's 256x144 presentation grid is a regional proof format, not automatically the universal world unit.

### W4 — Tactical coordinate
Purpose:
- combat/encounter positioning;
- cover;
- movement;
- hazards;
- line of sight.

Tactical coordinates must not redefine world geography.

## 4. Stable ID standard

Proposed pattern classes:
- `WORLD_*`
- `MACROREGION_*`
- `KINGDOM_*` / `NATION_*` / `CITYSTATE_*`
- `REGION_*`
- `CITY_*`
- `TOWN_*`
- `VILLAGE_*`
- `DISTRICT_*`
- `SITE_*`
- `INTERIOR_*`
- `BEAST_ZONE_*`
- `RESOURCE_ZONE_*`
- `ECOSYSTEM_*`
- `ROUTE_*`

Final naming conventions require registry validation before mass authoring.

## 5. Place record schema

Every permanent place should eventually include:
- stable_id;
- display_name;
- place_type;
- parent_id;
- coordinate_space;
- coordinates/bounds;
- elevation/depth if relevant;
- neighboring IDs;
- route IDs;
- controlling polity/faction;
- population estimate/band;
- settlement function;
- economy tags;
- resource tags;
- ecosystem IDs;
- beast-zone IDs;
- danger/level band;
- weather/climate;
- visual/material family;
- asset-kit IDs;
- discovery/access requirements;
- current world-state hooks;
- notable NPC/faction anchors;
- loot/resource provenance;
- authored scenes/quests;
- canon status;
- evidence/source;
- revision history.

## 6. Political entity schema

A kingdom/nation/city-state record must cover:
- ID/name;
- government;
- capital;
- subdivisions;
- laws;
- military/security;
- economy;
- resources;
- institutions;
- citizenship rules;
- class hierarchy;
- faction relations;
- historical conflicts;
- beast-zone policy;
- gate/technology policy;
- trade routes;
- languages/cultures if authored;
- prejudice/discrimination structures;
- current crises;
- player-facing reputation systems if implemented.

Do not assume every political entity is a monarchy merely because the user mentioned kingdoms.

## 7. Settlement schema

Cities/towns/villages must define:
- purpose/origin;
- population band;
- district list;
- housing;
- government;
- services;
- markets/economy;
- industry;
- transit;
- defenses;
- nearby resources;
- water/food supply;
- waste/infrastructure;
- social hierarchy;
- notable factions;
- schools/training;
- medical/public services;
- criminal/underground activity if authored;
- beast threats;
- level/danger range;
- expansion routes.

## 8. Resource-zone schema

Each resource zone:
- resource IDs;
- abundance;
- extraction method;
- renewal rate;
- ownership;
- legal restrictions;
- environmental effects;
- transport route;
- demand/use;
- loot/material grade;
- associated beasts;
- conflict risk;
- depletion state.

## 9. Ecosystem schema

Each ecosystem:
- biome;
- climate;
- terrain;
- flora;
- fauna;
- beast species;
- predator/prey relations;
- migration;
- reproduction;
- mutations/evolution if applicable;
- crystal/resource interactions if part of this game's final lore;
- hazards;
- human settlement pressure;
- seasonal/state changes.

No ecosystem should exist only as a backdrop if its resources/beasts affect gameplay.

## 10. Beast-zone schema

Each beast zone:
- bounds;
- ecosystem;
- species table;
- spawn/encounter logic only after gameplay contract;
- behavior;
- territory;
- threat band;
- resources/drops;
- migration;
- nests/lairs;
- faction/human interaction;
- route risk;
- world-state changes;
- boss/unique creatures only when authored.

## 11. Loot and item provenance

Loot should answer:
- why this item exists here;
- who made it;
- who carried/stored it;
- whether it is renewable;
- whether it comes from a beast/resource;
- quality/condition;
- legality;
- economy value;
- crafting/repair relevance if those systems exist.

Avoid arbitrary chest loot disconnected from world logic.

## 12. Population and NPC distribution

Each settlement/zone should have:
- population band;
- demographic categories only when worldbuilding requires them;
- occupation distribution;
- social-class distribution;
- institutional roles;
- faction presence;
- named-NPC anchors;
- procedural/supporting-NPC capacity;
- schedule density;
- migration/refugee/transient population if applicable.

Named NPCs should have stable identities. Generated/supporting NPCs need reproducible IDs when persistent.

## 13. Citizen hierarchy and discrimination

World documentation may include:
- legal class;
- wealth class;
- occupation prestige;
- citizenship;
- residency;
- faction status;
- lineage/culture/species where final lore establishes them;
- institutional privilege;
- discrimination/prejudice;
- segregation/access restrictions;
- propaganda;
- resistance/social mobility.

Required distinction:
- institutional rule;
- cultural norm;
- individual NPC belief.

This prevents one simplistic global prejudice variable from controlling the entire world.

## 14. World level/balance bands

Every region should eventually define:
- expected player progression band;
- ordinary civilian danger;
- environmental threat;
- common beast range;
- elite/unique threat;
- economic reward band;
- equipment availability;
- training opportunities;
- escape/avoidance routes.

Do not hard-scale every enemy to player level. The world should retain objective danger bands where design supports it.

## 15. Route schema

Routes include:
- road;
- transit;
- footpath;
- underground;
- gate;
- river/sea;
- air if later supported.

Each route:
- endpoints;
- directionality;
- travel time/distance once scale is locked;
- access;
- cost if any;
- risk;
- capacity;
- weather/state sensitivity;
- patrol/faction control;
- encounter hooks;
- visual transition assets.

## 16. Map-development target tracking

The owner requested a “10,000 map development” scope covering coordinates, places, zones, settlements, political entities, resources, ecosystems, loot, NPCs and related world data.

Until the unit is confirmed:
- track **map/place records**;
- track **route records**;
- track **resource/ecosystem/beast-zone records**;
- track **settlement/district/site records**;
- track words/docs separately.

No completion claim until the metric is accepted.

## 17. World authoring order

1. world physics/lore boundaries;
2. coordinate standard;
3. macroregions;
4. political entities;
5. major routes;
6. major cities;
7. regional resource/ecosystem bands;
8. villages/towns;
9. districts;
10. beast zones;
11. NPC population models;
12. loot/economy integration;
13. quests/events;
14. visual asset kits;
15. tactical encounter spaces.

Gate Twelve remains the proof region before this expands at scale.

## 18. Required child documents

Create later:
- `WORLD_GEOGRAPHY_STANDARD.md`
- `WORLD_POLITICAL_ENTITIES.md`
- `WORLD_SETTLEMENT_CATALOG.md`
- `WORLD_TRAVEL_AND_ROUTES.md`
- `WORLD_ECOSYSTEM_AND_RESOURCES.md`
- `WORLD_BEAST_ZONE_STANDARD.md`
- `WORLD_POPULATION_AND_CITIZEN_HIERARCHY.md`
- `WORLD_BALANCE_AND_LEVEL_BANDS.md`
- `WORLD_LOOT_PROVENANCE_STANDARD.md`

Each child must link back here and to the master program.
