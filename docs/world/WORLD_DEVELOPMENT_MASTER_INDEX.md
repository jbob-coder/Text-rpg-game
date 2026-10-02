# THE GAME — World Development Master Index

Status: **FOUNDATION / SCHEMA-FIRST**  
Parent: `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`

---

# 1. Purpose

This document is the top-level index for building the game's world from the current Gate Twelve district outward.

The owner requested a complete world-development program covering:
- coordinates;
- places;
- zones;
- areas;
- cities;
- villages;
- kingdoms;
- resources;
- ecosystems;
- loot;
- items;
- accessories;
- skills;
- classes;
- ranks;
- citizen hierarchy;
- discrimination/prejudice;
- beast zones;
- NPCs;
- world level/balance;
- stats;
- abilities;
- passives;
- activities;
- tactical combat;
- recurring/dynamic rivals;
- Android presentation.

This document does not invent the full world immediately.

It creates the schema and production order so the world can be expanded without contradiction.

---

# 2. World hierarchy

Target hierarchy:

`WORLD -> MACROREGION -> POLITICAL ENTITY -> SETTLEMENT/WILDERNESS -> DISTRICT/ZONE -> LOCATION -> ROOM/ENCOUNTER CELL`

Not every level is mandatory for every place.

Examples:
- wilderness may skip settlement;
- underground infrastructure may belong to a city without being a public district;
- remote beast zone may belong to a macroregion but no political entity.

Gate Twelve currently proves:
`WORLD(unwritten) -> CITY/REGION(unwritten) -> GATE_TWELVE_DISTRICT -> named locations`.

Do not pretend the missing parent geography is known.

---

# 3. Stable ID families

Proposed prefixes:

- `WORLD_`
- `REGION_`
- `KINGDOM_`
- `NATION_`
- `CITY_`
- `VILLAGE_`
- `DISTRICT_`
- `ZONE_`
- `LOCATION_`
- `ROOM_`
- `ROUTE_`
- `FACTION_`
- `INSTITUTION_`
- `NPC_`
- `BEAST_`
- `RESOURCE_`
- `ITEM_`
- `CLASS_`
- `RANK_`
- `ABILITY_`
- `TECHNIQUE_`
- `PERK_`
- `ACTIVITY_`

Existing IDs must not be renamed merely to fit a new prefix scheme.

The scheme applies primarily to new IDs unless a migration is separately justified.

---

# 4. Coordinate systems

The world needs multiple explicit coordinate spaces.

## 4.1 World logical coordinates
Used for:
- large-scale placement;
- route distance;
- region adjacency.

## 4.2 Regional coordinates
Used for:
- settlement/biome placement;
- strategic routes.

## 4.3 Settlement coordinates
Used for:
- districts;
- streets;
- major landmarks.

## 4.4 Local gameplay graph coordinates
Used for:
- nodes;
- travel edges;
- location selection.

## 4.5 Presentation coordinates
Used for:
- map raster;
- pixel placement;
- UI rendering.

## 4.6 Tactical coordinates
Used for:
- turn-based battle spaces;
- movement;
- cover;
- line-of-sight.

No coordinate system may silently substitute for another.

Operational child standard:
`WORLD_COORDINATE_AND_SCALE_STANDARD.md`.

Status: materialized on the master documentation branch; canonical W0/W1 spaces remain unpopulated until world-parent decisions are authored.

---

# 5. Place record schema

Every place eventually records:

- stable ID;
- display name;
- aliases;
- class;
- parent;
- logical coordinate;
- presentation coordinate;
- size class;
- terrain;
- elevation/depth;
- climate;
- biome;
- permanent structures;
- routes;
- entrances/exits;
- travel cost;
- faction/political control;
- law/security;
- population;
- citizen hierarchy;
- resources;
- economy;
- institutions;
- services;
- beasts;
- hazards;
- quests;
- activities;
- loot/resource opportunities;
- NPC anchors;
- discovery;
- access;
- state variants;
- visual asset references;
- map asset references;
- audio identity;
- loading/stream cell;
- implementation state;
- verification state.

---

# 6. Political entities and kingdoms

Before creating named kingdoms, define:

- governance type;
- territory;
- capital;
- administrative hierarchy;
- military/security;
- economy;
- technology;
- resource access;
- population;
- citizen classes;
- laws;
- inter-state relations;
- discrimination systems;
- beast policy;
- gate/infrastructure policy;
- factions/institutions;
- visual identity.

Political entities should influence gameplay:
- access;
- law;
- prices/economy if authored;
- NPC attitudes;
- jobs;
- travel;
- quests;
- equipment legality;
- beast response policy;
- class/status.

Do not create dozens of names without functional distinctions.

---

# 7. Cities

Each city should define:

- purpose in world;
- parent political entity;
- population band;
- districts;
- major infrastructure;
- economy;
- resource dependency;
- transport;
- security;
- citizen hierarchy;
- major factions;
- institutions;
- services;
- slums/elite zones only when justified;
- beast threats;
- surrounding resource zones;
- world-level band;
- visual/material language;
- player-entry routes.

Gate Twelve should eventually have a parent city record.

That parent is currently undecided.

---

# 8. Villages and smaller settlements

A village must exist for a reason.

Possible roles:
- agriculture;
- mining;
- logging;
- beast-hunting;
- gate support;
- military outpost;
- trade;
- pilgrimage;
- research;
- resource refining;
- transport junction.

Every village needs:
- supply dependencies;
- threats;
- local institutions;
- class structure;
- nearby resources;
- nearby beast ecology;
- routes to larger settlements;
- reason the player would visit.

---

# 9. Ecosystems

The world cannot be only cities plus random monsters.

Each ecosystem record should define:
- climate;
- terrain;
- flora;
- prey;
- predators;
- beast species;
- mutated/evolved variants if applicable;
- resource cycles;
- human exploitation;
- hazards;
- seasons if simulated;
- migration;
- overharvesting impact;
- faction control;
- loot/material implications.

Beast placement should follow ecology or authored anomaly, not arbitrary level tables.

---

# 10. Resources

Resource categories may include:
- biological;
- mineral;
- crystal/energy;
- salvage;
- manufactured;
- agricultural;
- rare/anomalous.

Every resource needs:
- source;
- abundance;
- extraction method;
- danger;
- refinement;
- consumers;
- trade value model;
- gameplay use;
- ecological cost;
- faction interest;
- world distribution.

Do not add currencies or crafting recipes merely because a resource exists.

---

# 11. Beasts and beast zones

Every beast zone needs:
- habitat;
- controlling ecology;
- beast families;
- level/threat band;
- population behavior;
- aggression triggers;
- migration;
- nesting;
- resources/drops;
- body-part value if body-part loot becomes canonical;
- faction response;
- civilian risk;
- routes;
- tactical terrain;
- boss/elite logic if authored.

Every beast record needs:
- stable ID;
- body plan;
- senses;
- movement;
- attacks;
- defenses;
- behavior;
- habitat;
- social pattern;
- lifecycle;
- resources/drops;
- threat scaling;
- status interactions;
- tactical AI needs;
- visual assets;
- animation assets.

---

# 12. Loot and items

Loot must come from explainable sources.

Sources:
- beasts;
- containers;
- rewards;
- salvage;
- trade;
- crafting if authored;
- quest handoffs;
- institutions;
- world events.

Every item must define:
- source;
- scarcity;
- utility;
- equipment slot if any;
- modifiers;
- prerequisites;
- durability only if that system is approved;
- legality;
- visual icon;
- paper-doll/held layer if applicable;
- sell/buy behavior only if economy exists;
- quest relevance;
- lore/provenance.

---

# 13. Accessories

Accessory categories:
- rings;
- neck;
- trinkets;
- badges;
- identity tags;
- utility attachments;
- faction markers;
- ability-focus objects if authored.

Avoid accessory bloat.

Each should affect:
- identity;
- gameplay;
- faction/legal status;
- narrative;
or another clear system.

---

# 14. Stats and world balance

Current seven-attribute system is implementation reality until migrated.

Future balance documentation must distinguish:
- base attributes;
- effective attributes;
- derived stats;
- skills;
- resources;
- perks/passives;
- equipment modifiers;
- conditions;
- temporary world effects.

World balance must avoid simple “zone level = player level” scaling unless intentionally chosen.

Preferred design questions:
- What threats exist regardless of player?
- Which areas telegraph danger?
- Which threats scale by variant rather than magically changing stats?
- How do NPCs survive in high-threat regions?
- How do equipment, knowledge, tactics and party composition matter?
- How do low-level areas remain meaningful later?

---

# 15. Skills, classes and ranks

The class system is not yet final.

Required future design:

## Skills
- taxonomy;
- training method;
- checks;
- mastery;
- cap;
- prerequisites;
- social/world use;
- combat use.

## Classes
Decide whether class means:
- formal profession;
- combat archetype;
- social/legal rank;
- progression template;
- combination.

Do not mix meanings without explicit layers.

## Ranks
Ranks may exist in:
- skill mastery;
- class/profession;
- institutions;
- military;
- adventurer/hunter organizations if authored;
- citizen hierarchy;
- beasts.

Each rank system needs its own namespace.

---

# 16. Citizen hierarchy

A citizen/status hierarchy may include:
- legal class;
- economic class;
- professional rank;
- institutional rank;
- citizenship;
- residency;
- faction standing;
- criminal/legal status;
- ability/beast-related stigma.

Every hierarchy must define:
- how status is acquired;
- what rights it changes;
- what duties it creates;
- what services/access it changes;
- what NPCs know;
- whether status is visible;
- whether forged/hidden status is possible;
- how the player changes status.

---

# 17. Discrimination / prejudice systems

Use fictional world causes and institutions.

Document:
- targeted fictional group/status;
- historical cause;
- current institutional mechanism;
- region variation;
- NPC variation;
- material consequences;
- legal consequences;
- narrative purpose;
- ways characters resist or exploit the system;
- player agency;
- consequences of participation.

Avoid making every member of a population behave identically.

---

# 18. NPC world population

NPC tiers:

## Tier A — canonical recurring
Full:
- identity;
- goals;
- memory;
- relationships;
- schedule;
- assets;
- story state.

## Tier B — named local
Persistent but lower detail.

## Tier C — generated/supporting
Uses archetype plus stable seed/ID.

## Tier D — ambient crowd
Presentation-only unless promoted.

Promotion from lower tier to higher tier should preserve identity/history.

---

# 19. NPC schedules and autonomy

The world target includes NPCs who do things without waiting for the player.

Needed systems:
- goals;
- schedules;
- location movement;
- work;
- rest;
- social contact;
- faction duties;
- reactions;
- event participation;
- memory;
- knowledge sharing.

Determinism and save persistence must be considered before implementation.

---

# 20. Dynamic recurring rivals

Design goal:
recurring enemies/competitors can change because of encounters.

Possible state:
- victories;
- defeats;
- wounds;
- escapes;
- fear;
- respect;
- hatred;
- ambition;
- promotions;
- demotions;
- allies;
- subordinates;
- territory;
- traits;
- rumors.

Originality:
- use original terminology;
- use original UI;
- use original hierarchy;
- avoid copying another game's named proprietary system or exact presentation.

---

# 21. Passive activities

Possible passive/downtime systems:
- rest;
- study;
- training;
- job shifts;
- research;
- travel;
- recovery;
- maintenance;
- socializing;
- scouting;
- resource processing.

Each needs:
- time cost;
- requirements;
- outputs;
- risks;
- interruptions;
- world progression while time passes.

No passive system should freeze the rest of the world unless deliberately designed.

---

# 22. Tactical battle system integration

The tactical system should use:
- authoritative stats;
- abilities;
- equipment;
- conditions;
- environment;
- actor/NPC state.

Needed components:
- encounter map;
- grid/cell system;
- initiative;
- actions;
- movement;
- cover;
- line-of-sight;
- attack resolution;
- damage;
- armor/defense;
- status;
- terrain;
- objectives;
- AI;
- morale/retreat;
- rewards;
- persistence.

Do not build combat as a separate stat universe.

---

# 23. World-level bands

A future world threat model should classify areas by:
- environmental danger;
- beast threat;
- faction security;
- resource hazard;
- travel difficulty;
- anomaly/ability hazard.

Use bands as guidance, not invisible hard walls.

Possible labels should be designed later; do not copy rank names from another IP.

---

# 24. Map-development production program

The owner requested a very large coordinate/place/zone development body.

Production order:

1. lock place schema;
2. lock coordinate schema;
3. finish Gate Twelve;
4. define Gate Twelve parent city;
5. define surrounding districts/routes;
6. define regional political entity;
7. define resource/ecosystem context;
8. define beast zones;
9. define nearby settlements;
10. expand outward.

Every batch must include:
- records;
- map coordinates;
- adjacency;
- visuals;
- gameplay reason;
- system dependencies;
- verification.

---

# 25. What is decided now

- Gate Twelve District exists.
- Nine named locations exist.
- Its current route graph exists.
- Gate Twelve has three planned macrozones in the current region master plan.
- Depot Plaza is intended as public hub.
- Platform Nine is internal depot hub.
- Gate Twelve is threshold.
- Service Tunnel points deeper.
- Quiet Stair is alternate egress.
- Trace Chamber is repeatable Trace progression/research location.

---

# 26. What still needs decision

- parent city;
- world name if not already established elsewhere;
- continents/macroregions;
- governments/kingdoms;
- technology baseline outside the current district;
- large-scale gate infrastructure;
- beast taxonomy;
- ecology;
- currencies/economy;
- final class system;
- final rank systems;
- citizen hierarchy;
- discrimination models;
- combat rules;
- dynamic rival rules;
- world-level bands;
- full travel scale;
- full coordinate scale;
- final world map.

Do not fill these gaps silently.

---

# 27. Required child documents next

1. `WORLD_COORDINATE_AND_SCALE_STANDARD.md`
2. `WORLD_PLACE_RECORD_SCHEMA.md`
3. `WORLD_POLITICAL_ENTITY_STANDARD.md`
4. `WORLD_SETTLEMENT_STANDARD.md`
5. `WORLD_ECOSYSTEM_AND_RESOURCES.md`
6. `WORLD_BEAST_AND_ZONE_STANDARD.md`
7. `WORLD_CITIZEN_HIERARCHY_AND_SOCIAL_STATUS.md`
8. `WORLD_TRAVEL_AND_ROUTE_STANDARD.md`
9. `WORLD_LEVEL_AND_BALANCE_STANDARD.md`
10. `WORLD_NPC_POPULATION_STANDARD.md`

Gate Twelve documentation continues in parallel as the proof implementation.

## World-scale schema companion

`WORLD_SCALE_DOCUMENTATION_BLUEPRINT.md` is the schema-first companion for future mass world authoring.

It defines:
- coordinate layers;
- stable place hierarchy;
- political entity records;
- settlement records;
- resources/ecosystems;
- beast zones;
- population;
- citizen hierarchy/discrimination distinctions;
- world-level bands;
- routes;
- loot provenance.

Do not begin thousands of world records until those schema contracts are stable.


---

# 28. Materialized world child standards — 2026-10-02

The following child standards now exist:
- `WORLD_GEOGRAPHY_STANDARD.md` — hierarchy, W0–W4 coordinate roles, boundaries, terrain/climate/resource/beast/political geography and scale policy.
- `WORLD_POLITICAL_ENTITIES.md` — political/government/territorial/social-hierarchy schema and catalog seed.
- `WORLD_SETTLEMENT_CATALOG.md` — city/town/village/outpost/district record and production contract.
- `WORLD_TRAVEL_AND_ROUTES.md` — route/access/travel/risk/migration and hierarchical travel contract.

The earlier “required child documents” list contains provisional names from before these files materialized. Where names differ, these materialized files are the current child authorities unless a later migration explicitly replaces them.

Still required at world scale:
- ecosystem/resource catalog;
- beast/zone catalog;
- population/citizen hierarchy catalog;
- world balance/level-band catalog;
- loot provenance catalog;
- exact Gate Twelve parent settlement/city decision;
- macroregion and political-world canon.


# 29. World schema coverage after 2026-10-02 batch

Materialized child authorities now cover:
- geography/coordinates;
- political entities;
- settlements;
- routes/travel;
- ecosystems/resources;
- beast zones;
- population/citizen hierarchy;
- balance/level bands;
- loot provenance;
- NPC population/distribution.

Therefore the next world-development phase is **catalog population and canon decisions**, not inventing more overlapping schemas.

Still undecided and intentionally not filled:
- Gate Twelve parent city/settlement;
- macroregions/continents;
- named kingdoms/states;
- world political borders;
- full ecosystem map;
- resource belts;
- beast taxonomy/species catalog;
- population totals;
- final world threat-band names;
- full travel scale;
- full world map.

Those decisions should be made in ordered batches using the standards above.


## Current canon decision queue

[World canon decision queue](WORLD_CANON_DECISION_QUEUE.md) owns the ordered unresolved decisions and exact current local map baseline. Schema documentation is established; world-scale catalog population is not complete.


## 2026-10-02 final reconstruction integration update

### Decided now
- schema-first world hierarchy and stable-ID discipline;
- distinct world/regional/settlement/local/presentation/tactical coordinate spaces;
- Gate Twelve as the first proof district;
- route legality/discovery owned outside UI;
- separate political, settlement, ecosystem/resource, beast-zone, population, balance, loot-provenance and NPC-population schemas;
- ecology/provenance-driven beasts/resources rather than arbitrary placement;
- multidimensional social hierarchy/discrimination rather than one universal prejudice stat;
- current seven attributes remain runtime reality until explicit migration.

### Intentionally undecided
Do not invent as canon yet:
- Gate Twelve parent city/macroregion;
- final nations/kingdoms/borders;
- capitals/cities/villages beyond explicitly authored repository content;
- concrete culture/institution networks;
- biome/climate map;
- concrete resource/economic flows;
- beast taxonomy/distribution;
- world threat bands;
- world NPC population;
- final world coordinates and travel network.

### Next canon packet
The first world-population decision should be the minimum parent chain needed to place Gate Twelve: parent settlement, parent region, political ownership if applicable, W0/W1 anchors, major routes, terrain/climate/material context. Mass world generation stays blocked until this parent chain is coherent.
