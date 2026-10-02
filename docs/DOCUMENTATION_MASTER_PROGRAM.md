# THE GAME — Text Pixel RPG Master Documentation Program

Status: **P0 / ACTIVE / DOCUMENTATION-FIRST**
Repository: `jbob-coder/Text-rpg-game`
Program branch: `docs/text-pixel-rpg-master-program`
Started: 2026-10-02 AST
Primary purpose: convert the owner's complete game-development direction into a repository-native, cross-referenced body of design, world, system, visual, implementation, migration, QA, and handoff documentation before destructive reconstruction work begins.

---

## 0. Program authority

For this program, `jbob-coder/Text-rpg-game` is the **priority repository**.

That statement means:
- new design authority for THE GAME is written here first;
- subordinate reports should point back to this program;
- old prototypes and outside projects are evidence/reference only unless explicitly adopted;
- repository files and fresh verification evidence outrank chat memory;
- Gate Twelve remains a local region inside the larger world, not the entire world design;
- gameplay-authoritative data remains owned by engine/content systems, not UI art;
- the existing pixel-art direction remains mandatory.

This document does not change the GitHub default branch or promote `main`. Branch governance and code promotion remain explicit later operations.

The owner grants standing permission for routine game-development work, including documentation, refactors, replacement of presentation systems, asset-pipeline changes, testing, and creation of working branches, subject to the repository safeguards already stated in `AGENTS.md`.

---

## 1. Owner directive decomposed

The owner directive is decomposed into the following program goals.

### 1.1 Documentation before reconstruction
Documentation is the primary product of the current phase. Implementation should not outrun design authority.

Every major subsystem must document:
- confirmed current behavior;
- desired target behavior;
- what may change;
- what will change;
- what must not change without migration;
- dependencies;
- files/systems affected;
- data ownership;
- migration risks;
- verification gates;
- unresolved decisions;
- next executable task.

### 1.2 Visual and pixel-art system
Document:
- how environment pixel art is authored and reused;
- how player/NPC sprites are built;
- contextual character panels based on who is physically/narratively present;
- paper-doll equipment overlays;
- portrait/expression variants;
- scene/location layers;
- text-art/UI overlays;
- icon families;
- map markers;
- FX;
- palette and scale contracts;
- asset provenance;
- how reuse avoids visual mismatch.

### 1.3 World construction
Build a full world-development body covering:
- coordinates;
- world regions;
- kingdoms/states/polities;
- cities;
- villages;
- districts;
- wilderness;
- roads and travel corridors;
- interiors;
- underground layers;
- resources;
- climates;
- ecosystems;
- beast territories;
- population;
- social hierarchy;
- prejudice/discrimination systems where narratively relevant;
- factions/institutions;
- economies;
- loot;
- items;
- equipment/accessories;
- services;
- world events.

No single local map reference defines the global world.

### 1.4 Progression and character systems
Document/reconcile:
- attributes;
- derived stats;
- skills;
- abilities;
- passives;
- techniques;
- classes/archetypes;
- ranks;
- citizen/social ranks;
- faction standing;
- equipment;
- perks;
- conditions;
- training;
- recovery;
- progression speed;
- balance boundaries;
- world-level scaling.

### 1.5 NPC/world simulation
Document NPCs as persistent agents with:
- stable IDs;
- location;
- schedule/state;
- relationships;
- memory;
- knowledge;
- goals;
- faction;
- social status;
- resources;
- injuries/conditions;
- equipment;
- combat capability;
- event participation;
- consequences.

A dynamic rival/relationship system may use the design goal of memorable recurring opponents and emergent history, but must be an original implementation and must not copy proprietary names, characters, UI, dialogue, or exact mechanics from another game.

### 1.6 Tactical battle system
Target direction: turn-based/tactical combat with readable positioning, cover/terrain, action economy, status, abilities, equipment, AI goals, and persistent consequences.

The project may study the general design space associated with squad-tactical games, but the shipped implementation must use original terminology, rules, balance, UI, data structures, content, and encounter design.

### 1.7 APK evolution and final reconstruction
The Android client is not exempt from redesign.

The program must eventually classify every existing client element as:
- KEEP;
- KEEP + UPGRADE;
- REFACTOR;
- REPLACE;
- RETIRE;
- UNKNOWN PENDING AUDIT.

Only after the full design authority is coherent should destructive reconstruction occur.

The final APK documentation must define:
- target screen architecture;
- navigation;
- gameplay flow;
- rendering boundaries;
- Android/Python bridge contracts;
- asset loading;
- save/load;
- accessibility;
- narration/audio;
- error states;
- performance;
- device verification;
- migration/rollback;
- deletion/retirement plan;
- acceptance criteria.

---

## 2. Numeric documentation targets

The owner supplied large numeric targets including:
- 3,000 documentation;
- 2,000 guide/planning;
- 10,000 map development;
- final 10,000 APK/rebuild documentation;
- an overall final target of 2,000,000 documentation.

The **unit of these numbers was not explicitly defined** in the directive. Therefore this program records them as `OWNER_TARGET / UNIT_UNRESOLVED`.

Rule:
- do not claim a numeric target has been achieved until the measurement unit is explicitly established;
- do not inflate documentation with filler to satisfy a number;
- quality, traceability, and executability outrank raw length;
- word counts, document counts, and design-item counts must be tracked separately if quotas later become formal.

---

## 3. Documentation architecture

The program uses a dependency graph rather than unrelated reports.

```
MASTER_PROGRAM
├── PROJECT_PRIORITY_AND_AUTHORITY
├── DOCUMENTATION_INDEX
├── GAME_FOUNDATION
├── WORLD_BIBLE
│   ├── GLOBAL_COORDINATE_SYSTEM
│   ├── WORLD_ATLAS
│   ├── REGIONS_KINGDOMS_CITIES
│   ├── SETTLEMENTS_AND_DISTRICTS
│   ├── TRAVEL_AND_TRANSPORT
│   ├── RESOURCES_AND_ECONOMY
│   ├── ECOLOGY_AND_BEAST_ZONES
│   ├── SOCIETY_HIERARCHY_AND_CULTURE
│   └── WORLD_EVENTS_AND_PRESSURE
├── VISUAL_SYSTEM
│   ├── VISUAL_BIBLE
│   ├── PIXEL_ASSET_MASTER_PLAN
│   ├── CHARACTER_PIXEL_BLUEPRINTS
│   ├── PIXEL_ART_INTEGRATION_CONTRACT
│   ├── LOCATION_AND_MAP_ART
│   └── ASSET_MANIFESTS
├── GAME_SYSTEMS
│   ├── STATS_AND_DERIVED_VALUES
│   ├── SKILLS_ABILITIES_PASSIVES
│   ├── CLASSES_RANKS_PROGRESSION
│   ├── ITEMS_EQUIPMENT_LOOT
│   ├── QUESTS_KNOWLEDGE_SOCIAL
│   ├── NPC_SIMULATION
│   ├── TACTICAL_COMBAT
│   └── BALANCE_AND_WORLD_LEVELS
├── REGION_PLANS
│   └── GATE_TWELVE_REGION_MASTER_PLAN
├── APPLICATION
│   ├── SCREEN_AND_NAVIGATION_ARCHITECTURE
│   ├── CONTEXTUAL_CHARACTER_PANELS
│   ├── PLAYER_SAFE_PROJECTION
│   ├── AUDIO_NARRATION_ACCESSIBILITY
│   └── APK_RECONSTRUCTION_MASTER_PLAN
├── MIGRATION_AND_QA
│   ├── KEEP_REWORK_REPLACE_RETIRE_MATRIX
│   ├── SAVE_AND_DATA_MIGRATION
│   ├── PERFORMANCE_PLAN
│   ├── TEST_MATRIX
│   └── DEVICE_ACCEPTANCE
└── EXECUTION
    ├── IMPLEMENTATION_ORDER
    ├── BRANCH_PLAN
    ├── TASK_REGISTER
    └── SESSION_HANDOFF
```

No lower document may silently override a higher authority document. Conflicts must be recorded and resolved.

---

## 4. Decision states

Every significant design item uses one of:

- **CONFIRMED** — already supported by authoritative repository state or explicit owner decision.
- **ADOPTED** — intentionally selected by this program.
- **PROPOSED** — recommended but not yet implementation authority.
- **ASSUMED** — temporary reversible assumption needed to continue.
- **UNKNOWN** — insufficient evidence.
- **CONFLICTING** — sources disagree.
- **REJECTED** — deliberately not used.
- **DEPRECATED** — old authority retained only for migration/history.
- **RETIRED** — no longer valid after completed migration.

Each document must state which status applies.

---

## 5. Source precedence

Use this precedence order:

1. current repository source/data on the exact branch/HEAD;
2. fresh test/build/runtime evidence;
3. explicit owner decisions recorded in repository documentation;
4. this master program and its normative child documents;
5. prior project reports;
6. external reference material;
7. chat memory;
8. inference.

External material can inspire architecture, composition, pacing, hierarchy, or interaction patterns. It cannot silently import copyrighted story content, named characters, proprietary terminology, exact UI, or one-to-one system reproduction.

---

## 6. Visual reference classification

The current reference set is divided into two families.

### Family A — settlement/map architecture references
Useful for:
- top-down readability;
- hub/spoke organization;
- section decomposition;
- layer stacks;
- building blueprints;
- streets/paths;
- props;
- terrain;
- streaming ownership;
- collision/navigation planning;
- minimap logic;
- asset queues;
- performance and migration planning.

Do not inherit their exact:
- dimensions;
- number of areas;
- medieval identities;
- road widths;
- building counts;
- color coding;
- names.

### Family B — THE GAME pixel production references
Useful for:
- 32x48 character masters;
- six-view turnarounds;
- anchor points;
- paper-doll layers;
- equipment decomposition;
- NPC expressions;
- item icons;
- map icons;
- FX;
- 128x64 location previews;
- 256x144 district map composition;
- shared palette logic.

These references are still reference/blueprint material. Production assets must pass the existing native-pixel pipeline and manifest QA.

---

## 7. Pixel-art composition policy

A scene must be composed from reusable layers where practical.

Preferred composition model:

```
BACKGROUND / ARCHITECTURE
→ PERMANENT ENVIRONMENT MODULES
→ STATEFUL ENVIRONMENT OVERLAYS
→ PROPS / INTERACTABLES
→ NPC / PLAYER SPRITES
→ EQUIPMENT PAPER-DOLL LAYERS
→ STATUS / ABILITY FX
→ PLAYER-SAFE MARKERS
→ UI FRAME / TEXT / CONTEXT PANELS
```

Rules:
- stable architecture should not be redrawn for every story state;
- temporary damage, blackout, weather, Trace effects, faction control, alerts, and similar changes should use overlays when the geometry is unchanged;
- equipment is a projection of authoritative equipment state;
- contextual panels are a projection of present/known characters and scene state;
- hidden authored information cannot leak through an art layer;
- overlays require anchor, z-order, palette, occlusion, and state-binding metadata;
- visual reuse is rejected when scale, perspective, light direction, material language, or palette causes the asset to look pasted in.

---

## 8. Contextual character-panel model

The gameplay presentation may show character panels according to who is actually present and player-visible in the current scene/room.

Target model:

- player panel: persistent;
- primary speaker panel: shown when a speaker is present;
- additional party/NPC panels: shown only when scene state exposes them;
- portrait/expression is selected from player-safe emotional/state tags;
- equipment/status overlays may appear if visible and relevant;
- absent characters do not receive panels merely because their data exists;
- hidden observers/secrets cannot create UI evidence;
- group scenes may use a panel carousel/stack or compact roster;
- solo scenes collapse unused panel space back into narrative/art space.

The engine must expose safe presence/portrait tags. Compose/UI must not inspect raw hidden NPC state to decide who appears.

---

## 9. World-development program

The global map program must ultimately answer, for every place:

- stable ID;
- parent world/region/polity;
- coordinate/bounds;
- scale class;
- neighboring areas;
- route types;
- travel costs;
- climate;
- terrain;
- resource profile;
- ecosystem;
- danger profile;
- population;
- governing authority;
- social hierarchy;
- economy;
- services;
- major NPCs/factions;
- beasts;
- loot/materials;
- quests/events;
- art set;
- music/audio tag if used;
- loading ownership;
- map visibility;
- discovery rules;
- implementation status.

The world atlas may contain tens of thousands of entries over time, but entries must be stable, searchable, and generated from reusable schemas rather than unstructured prose alone.

---

## 10. Society, hierarchy, discrimination, and faction systems

World societies may include:
- legal class;
- profession;
- wealth;
- citizenship;
- faction membership;
- lineage/origin;
- species/ancestry when the setting contains multiple peoples;
- reputation;
- military/civic rank;
- access privileges.

Discrimination/prejudice can exist as worldbuilding and gameplay state, but it must be authored as a setting/system property rather than a universal assumption.

Documentation must separate:
- law/policy;
- social norm;
- individual prejudice;
- faction ideology;
- player reputation consequence;
- service/access restriction;
- story claim vs objective world truth.

---

## 11. Ecosystem, beasts, resources, and loot

Each ecological zone should define:
- biome;
- food/water;
- ambient hazards;
- ordinary wildlife;
- beast species;
- migration;
- predation;
- nesting;
- resource nodes;
- harvestable materials;
- crystal/material ecology where canon supports it;
- settlement pressure;
- trade links;
- danger rating.

Loot must have provenance. Items should come from:
- creatures;
- plants/minerals;
- crafting/industry;
- trade;
- quests;
- institutions;
- salvage;
- specific world events.

Avoid generic random loot that has no relationship to place or economy unless a documented system explicitly supports it.

---

## 12. Tactical combat + recurring rival system

### Tactical combat direction
Target qualities:
- turn/phase clarity;
- grid or discrete positional model if selected;
- cover/line-of-sight;
- movement cost;
- action/resource economy;
- status effects;
- equipment/ability interaction;
- objective-based encounters;
- destructible/interactive environment only where supported;
- deterministic rules;
- AI intent;
- persistent injuries/consequences where designed.

### Recurring rival direction
Target qualities:
- stable enemy/NPC identity;
- memory of encounters;
- wounds/scars/status where visible;
- rank/role changes;
- relationship with factions;
- grudges/fears/respect as authored state;
- promotions/replacements/succession;
- world events caused by survival or defeat.

This must be an original system. Do not reproduce protected names, UI, dialogue, ranking presentation, narrative content, or exact proprietary progression logic from other games.

---

## 13. APK reconstruction rule

No broad deletion is authorized merely because redesign is desired.

The client reconstruction sequence is:

1. inventory current APK/client surfaces;
2. trace each surface to authoritative engine/projection dependencies;
3. classify KEEP / UPGRADE / REFACTOR / REPLACE / RETIRE;
4. define target architecture;
5. create compatibility/migration boundaries;
6. build replacement slices beside old behavior where practical;
7. execute tests;
8. verify representative emulator;
9. verify physical handset where available;
10. only then retire superseded code/assets;
11. update save/data migration;
12. document final source of truth.

The current Kotlin/Compose + Chaquopy path remains current evidence until a later migration deliberately supersedes it.

---

## 14. Program stages

### Stage 0 — Authority and indexing
Deliver:
- master program;
- project priority declaration;
- documentation index;
- task-register pointer;
- Gate Twelve linkage.

### Stage 1 — Visual/pixel integration
Deliver:
- contextual character-panel contract;
- overlay/reuse rules;
- art-state bindings;
- asset gap list;
- reference lineage.

### Stage 2 — Global world schema
Deliver:
- coordinate conventions;
- world hierarchy;
- place schema;
- route/travel schema;
- region/city/village/district templates.

### Stage 3 — World content planning
Deliver:
- regions;
- settlements;
- resource/economy;
- ecology/beasts;
- factions/society;
- world events.

### Stage 4 — Progression and content systems
Deliver:
- stats;
- skills;
- abilities;
- passives;
- classes/ranks;
- items/equipment;
- loot;
- citizen/social standing.

### Stage 5 — NPC simulation
Deliver:
- memory;
- knowledge;
- schedules;
- goals;
- relationships;
- faction state;
- recurring rival history.

### Stage 6 — Tactical combat
Deliver:
- encounter schema;
- actions;
- cover/LOS;
- initiative/turn model;
- AI;
- persistence;
- balance.

### Stage 7 — Application architecture
Deliver:
- screen graph;
- contextual panels;
- map;
- story;
- character;
- inventory/equipment;
- quests;
- stats;
- saves/settings/dev;
- narration/accessibility.

### Stage 8 — Migration and APK rebuild plan
Deliver:
- full audit matrix;
- retirement plan;
- replacement sequence;
- compatibility;
- device gates.

### Stage 9 — Implementation execution
Only after prerequisites for each subsystem are documented.

---

## 15. Branch strategy

Documentation is separated by topic so very large work can proceed without one permanently conflicting branch.

Initial branch:
- `docs/text-pixel-rpg-master-program`

Planned descendants may include:
- `docs/world-atlas-v1`
- `docs/pixel-integration-v1`
- `docs/progression-systems-v1`
- `docs/npc-simulation-v1`
- `docs/tactical-combat-v1`
- `docs/android-reconstruction-v1`

Branches must point back to this program and should not silently fork incompatible design authority.

---

## 16. Immediate priority queue

P0:
1. establish master authority and cross-reference index;
2. preserve Gate Twelve Steps 1–4;
3. document pixel-art integration and contextual panels;
4. define the global world/map schema before expanding geography;
5. audit current mechanics against desired systems;
6. create keep/rework/replace/retire matrix;
7. defer destructive APK teardown until the matrix and target application architecture exist.

P1:
- produce world atlas content;
- progression/class/rank framework;
- ecosystem/beast/resource model;
- NPC simulation;
- tactical combat.

P2:
- deep content expansion and implementation after system contracts stabilize.

---

## 17. Continuity handoff

CURRENT_OBJECTIVE:
Build the repository-native documentation authority for the full Text Pixel RPG before broad reconstruction.

VERIFIED_STATE:
- repository exists and is writable;
- Gate Twelve master plan contains completed Steps 1–4;
- existing visual bible and asset-production documents define pixel constraints;
- existing Android/client work is repository-owned and has prior emulator evidence;
- the new program branch is based on the Gate Twelve documentation branch.

COMPLETED_THIS_STAGE:
- program scope decomposed;
- priority repository declared in documentation;
- documentation dependency graph defined;
- external references classified;
- pixel composition model defined;
- contextual-panel model defined;
- world/system/APK documentation stages defined.

NEXT_ACTION:
Create/maintain `docs/DOCUMENTATION_INDEX.md`, then execute Stage 1 visual/pixel integration and Stage 2 global world schema without deleting runtime code.

DO_NOT_ASSUME:
- the numeric documentation targets have a defined unit;
- external map dimensions/area counts are canon;
- all reference-board assets are production-ready;
- `main` is canonical;
- destructive APK replacement is ready to execute.
