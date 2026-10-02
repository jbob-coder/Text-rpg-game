# THE GAME — World & Map Development Program

Status: **FOUNDATIONAL WORLD-BIBLE PROGRAM**
Target: minimum 10,000 words/units for first full world-map framework, expanding far beyond that as the 2,000,000-documentation program grows.

## 1. Purpose

Create a world that can be simulated, mapped, expanded, balanced, and rendered without inventing geography ad hoc during implementation.

The world hierarchy is:

`WORLD -> POLITICAL REGION -> KINGDOM/STATE -> SETTLEMENT -> DISTRICT -> LOCATION -> ROOM -> INTERACTABLE`

Parallel ecological hierarchy:

`WORLD -> BIOME -> ECOREGION -> BEAST ZONE -> HABITAT -> RESOURCE SITE`

Parallel travel hierarchy:

`WORLD ROUTE -> REGIONAL ROUTE -> SETTLEMENT ROUTE -> DISTRICT ROUTE -> LOCATION EDGE`

## 2. Coordinate model to document before global expansion

A global coordinate convention is still undecided.

The final system must distinguish:
- global/world coordinates;
- regional coordinates;
- settlement map coordinates;
- local district presentation coordinates;
- room anchors;
- tactical-combat coordinates.

Gate Twelve's 256x144 map grid remains a presentation coordinate system, not proof of global physical scale.

The world bible must later lock:
- origin;
- axis direction;
- units;
- scale;
- conversion between presentation and simulation;
- elevation/depth;
- underground layers;
- fast-travel/travel-time derivation;
- map LOD.

## 3. Stable world IDs

Every place receives a stable ID before it becomes gameplay content.

Proposed hierarchy examples:
- `WORLD_...`
- `REGION_...`
- `KINGDOM_...`
- `CITY_...`
- `VILLAGE_...`
- `DISTRICT_...`
- `LOCATION_...`
- `ROOM_...`
- `ROUTE_...`
- `RESOURCE_SITE_...`
- `BEAST_ZONE_...`
- `FACTION_...`

Naming examples are schema guidance, not canon names.

## 4. Political geography documentation

For every kingdom/state:
- stable ID;
- name;
- government;
- ruler/institutions;
- borders;
- capital;
- cities;
- villages;
- military;
- economy;
- dominant resources;
- class structure;
- laws;
- relationships;
- conflicts;
- roads/trade;
- monster/beast pressures;
- internal factions;
- historical claims;
- population;
- technology level;
- power-level distribution.

No kingdom is canon until explicitly authored.

## 5. Settlement hierarchy

### Capital / major city
Document:
- districts;
- residential classes;
- government;
- markets;
- workshops;
- education;
- military;
- transit;
- hospitals/healing;
- entertainment;
- crime;
- resources;
- NPC population;
- beast defenses;
- gates/roads.

### Town
Document smaller versions with a clear economic reason to exist.

### Village
Document:
- food/resource basis;
- population;
- local authority;
- nearby beast threats;
- local crafts;
- roads;
- social hierarchy;
- dependencies on larger settlements.

### Outpost / camp / station
Document:
- purpose;
- supply;
- defense;
- duration;
- faction;
- travel relation.

## 6. District and area design

Every district should answer:
- why it exists;
- who lives/works there;
- what the player does there;
- what resources flow through it;
- danger level;
- crime/law presence;
- NPC density;
- map landmarks;
- routes;
- time-of-day behavior;
- events;
- pixel-art family;
- reusable modules;
- expansion boundaries.

Gate Twelve is the first district-level reference implementation.

## 7. Resource system documentation

World resources need:
- stable ID;
- category;
- source biome;
- rarity;
- extraction method;
- regeneration/depletion;
- legal status;
- value;
- processing;
- item recipes if crafting exists;
- beast/ecosystem dependency;
- political importance;
- trade route dependency;
- environmental consequence.

Categories may include:
- food;
- water;
- timber;
- stone;
- metals;
- crystals/energy materials only if canon;
- fibers;
- medicines;
- beast materials;
- industrial salvage.

No resource is added only to fill a table.

## 8. Ecosystem documentation

Each biome/ecoregion needs:
- climate;
- terrain;
- flora;
- prey;
- predators;
- apex threats;
- migration;
- reproduction;
- resource competition;
- human settlement pressure;
- seasonal/event variation;
- invasive/mutated species if canon;
- danger bands.

Beasts must occupy believable ecological roles unless explicitly supernatural rules override ecology.

## 9. Beast zones

Each beast zone requires:
- stable zone ID;
- boundary;
- biome;
- species;
- population density;
- rank/level range;
- behavior;
- nests;
- territory;
- migration;
- resources/loot;
- travel risk;
- faction control;
- escalation conditions;
- encounter rules;
- visual/environment asset needs.

A dangerous beast zone should affect roads, settlement economy, NPC schedules, and local prices rather than existing only as a combat arena.

## 10. Loot and item geography

Loot must have provenance.

Possible sources:
- beast;
- environment;
- NPC;
- shop;
- quest;
- salvage;
- crime;
- battlefield;
- resource site;
- crafting/processing.

Every loot table should reference:
- location/zone;
- source entity;
- level/rank;
- rarity;
- quantity;
- condition;
- ownership/legal state;
- respawn/regeneration rule;
- economy effect.

## 11. Citizens and social hierarchy

If the world uses rigid social hierarchy, document it systemically.

Possible dimensions:
- political rank;
- wealth;
- profession;
- military status;
- guild/faction membership;
- ability/power rank;
- citizenship;
- species/ethnic identity only if authored;
- criminal status;
- reputation.

If racism/species prejudice/discrimination exists in the setting, document:
- who discriminates against whom;
- historical/social cause;
- law/institution support;
- regional variation;
- NPC behavior;
- gameplay consequences;
- how the system avoids reducing every character to a stereotype;
- what information is visible to the player.

It must serve world logic and narrative, not be added as shock content.

## 12. NPC world placement

Every recurring NPC must eventually have:
- stable NPC ID;
- home/base;
- work/activity locations;
- schedule;
- route;
- faction;
- social class;
- relationships;
- inventory;
- skills/abilities;
- goals;
- memory;
- knowledge;
- room presence rules;
- portrait/sprite;
- death/absence handling;
- replacement/succession if applicable.

NPCs should move through the world according to simulation rules rather than teleporting solely because a UI scene needs them.

## 13. World level system

The world should not scale blindly to the player.

Documentation must define:
- absolute danger bands;
- local recommended progression;
- low/high outliers;
- elite/apex entities;
- protected/civilian zones;
- faction power;
- equipment floor/ceiling;
- travel warnings;
- how player knowledge communicates danger.

Potential model:
- fixed regional baselines;
- state/event modifiers;
- limited adaptive encounter selection;
- no universal enemy stat inflation merely because the player leveled.

Final numbers remain undecided.

## 14. Area content package

Every completed area eventually needs:
- map coordinates;
- stable IDs;
- routes;
- environment art specification;
- room list;
- NPC list;
- resource list;
- loot list;
- beast threats;
- quests/events;
- social/faction state;
- level/danger band;
- day/night behavior;
- ambient audio needs;
- asset list;
- state overlays;
- test cases;
- save/persistence implications.

## 15. Map production layers

Global map:
- political;
- physical;
- routes;
- known/unknown;
- danger;
- resources if discovered;
- faction control if known.

Settlement map:
- districts;
- major services;
- landmarks;
- gates;
- routes.

District map:
- buildings;
- streets;
- named locations;
- entrances;
- underground routes.

Room map/scene:
- interaction anchors;
- characters;
- props;
- state overlays.

Tactical map:
- combat grid;
- cover;
- elevation;
- hazards;
- destructibility only if rules support it.

## 16. World documentation backlog

The first 10,000-word/unit world-map package should cover:
1. global coordinate schema;
2. world-scale hierarchy;
3. region template;
4. kingdom template;
5. settlement template;
6. district template;
7. biome template;
8. beast-zone template;
9. resource-site template;
10. route/travel template;
11. danger/level framework;
12. social hierarchy framework;
13. NPC placement/schedule framework;
14. loot provenance framework;
15. art/asset requirements per area;
16. integration with Android Map/Story screens.

After that, canon world content can be added region by region.
