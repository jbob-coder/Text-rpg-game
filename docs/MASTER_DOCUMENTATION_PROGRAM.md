# THE GAME — Master Documentation & Development Program

Status: **PRIMARY PROGRAM / DOCUMENTATION-FIRST**
Repository: `jbob-coder/Text-rpg-game`
Priority: **ACTIVE GAME PROJECT / FIRST REPOSITORY TO READ**
Program branch: `docs/master-documentation-program`
Started: 2026-10-02

## 1. Purpose

This program converts the current Text RPG + Pixel Art Stack into a repository-native development system where documentation is written before destructive rewrites, bulk asset production, large world expansion, or final APK reconstruction.

The final objective is not merely to add more documents. The objective is to produce enough structured, cross-referenced design and implementation evidence that the game can be rebuilt, extended, visually upgraded, balanced, tested, and handed between agents without relying on chat memory.

Documentation is therefore treated as an implementation dependency.

## 2. Owner mandate captured

The project owner has granted broad standing development authority for this game, including authority to redesign, refactor, replace, remove, or rebuild implementation when the documented target architecture requires it.

That authority is bounded by earlier explicit restrictions and repository safety rules:

- do not silently promote or merge `main`;
- do not force-push or rewrite shared history;
- do not use another game repository as authority;
- do not silently import copyrighted story/game content;
- do not reproduce another game's protected maps, characters, names, UI, assets, or exact mechanics;
- do not substitute code-drawn boxes, rectangles, geometry, or procedural placeholders for final visual pixel art;
- do not use paid/billing-risk tooling without explicit approval;
- do not claim tests, builds, device validation, asset completion, or integration that has not actually been verified;
- preserve stable gameplay IDs, player-safe projection, save/state ownership, and authored contracts unless a documented migration replaces them;
- generated images are reference material until converted into approved production assets through the pixel-art pipeline.

Routine project engineering does not require repeated permission. Irreversible external actions still require their normal approval boundary.

## 3. Priority-repository rule

For this project, agents must treat:

`jbob-coder/Text-rpg-game`

as the first repository to inspect and the primary active game project.

Other repositories, old prototypes, Godot projects, abandoned RPGs, and unrelated Jack/Pixel RPG continuities are external references only unless the owner explicitly requests a migration.

When documentation conflicts:
1. exact live repository/branch/HEAD;
2. fresh test/build/runtime evidence;
3. repository-native master documentation;
4. domain plans and task registers;
5. older reports/handoffs;
6. chat memory.

## 4. Documentation-scale target

The owner set a long-term target of approximately **2,000,000 total documentation words/units** across the complete project.

Until the owner defines another counting system, this program interprets those numbers as **documentation-volume targets**, not promises that thousands of tiny files must be created.

Target planning layers:

- roughly **3,000 documentation units** for factual/specification records;
- roughly **2,000 guide/planning units** for implementation, QA, content authoring, migration, and production guidance;
- at least **10,000 words/units of map/world-development planning** for the first full world framework;
- at least **10,000 words/units for the final APK rebuild/evolution plan**;
- cumulative program target: approximately **2,000,000 words/units** before the final documentation program is considered exhaustive.

Quality outranks word count. Raw volume is never evidence of completion.

## 5. Program architecture

The program is divided into 16 documentation tracks.

### Track A — Project authority, continuity, and decision governance
Covers:
- source-of-truth order;
- branch rules;
- repository priority;
- standing permissions;
- prohibited tools/actions;
- decision status;
- unknowns;
- migration approvals;
- superseded reports;
- handoff rules.

### Track B — Current implementation inventory
Covers:
- Android/Compose structure;
- Python engine;
- player-safe projection;
- state/save pipeline;
- current quests/scenes;
- world map;
- current gameplay systems;
- current UI panels;
- current assets and their real lifecycle stage;
- tests/workflows;
- APK evidence;
- known defects.

### Track C — Pixel art production and visual integration
Covers:
- player body;
- character panels and portraits;
- NPC presentation;
- paper-doll equipment;
- rooms;
- environment;
- map;
- props;
- items;
- loot;
- effects;
- UI;
- overlays;
- animation;
- reusable atlases/modules;
- provenance;
- visual coherence.

### Track D — World map and spatial development
Covers:
- coordinates;
- regions;
- zones;
- subzones;
- areas;
- cities;
- villages;
- settlements;
- kingdoms/states;
- roads;
- transit;
- interiors;
- underground areas;
- beast territories;
- dangerous zones;
- resource sites;
- expansion boundaries;
- travel cost and scale.

### Track E — Ecology, resources, and environmental simulation
Covers:
- biomes;
- ecosystems;
- beast populations;
- food chains;
- resource distribution;
- scarcity;
- extraction;
- environmental hazards;
- migration;
- seasonal/event effects;
- regeneration/depletion.

### Track F — Society, hierarchy, population, and institutions
Covers:
- governments;
- kingdoms;
- civic classes;
- professions;
- wealth levels;
- social rank;
- discrimination/racism/species prejudice where the setting intentionally supports it;
- laws;
- crime;
- punishment;
- factions;
- institutions;
- education;
- military;
- labor;
- religion only if canonically authored later;
- population behavior.

### Track G — NPC simulation
Covers:
- stable IDs;
- schedules;
- homes/work;
- goals;
- memory;
- knowledge;
- relationships;
- social networks;
- reputation;
- injuries;
- inventory;
- factions;
- death/replacement;
- persistence;
- room/scene presence;
- character panels.

### Track H — Items, loot, equipment, accessories, economy
Covers:
- item taxonomy;
- rarity/quality;
- materials;
- equipment slots;
- accessories;
- loot tables;
- vendors only where authored;
- repair/modification only if implemented;
- prices/currency;
- scarcity;
- ownership;
- provenance;
- theft/crime consequences;
- inventory presentation.

### Track I — Stats, abilities, passives, skill trees, classes, ranks
Covers:
- base attributes;
- derived stats;
- resource pools;
- skills;
- abilities;
- techniques;
- passives;
- perks;
- class/rank frameworks;
- prerequisites;
- growth;
- caps;
- counters;
- status effects;
- training;
- respec rules if ever introduced;
- balance targets.

### Track J — World-level and progression balance
Covers:
- player growth curves;
- enemy/beast level bands;
- regional danger;
- equipment progression;
- encounter budgets;
- soft/hard gates;
- recovery;
- time cost;
- economy balance;
- ability power budgets;
- progression pacing;
- anti-snowball rules.

### Track K — Tactical battle system
Target direction:
- original turn-based tactical combat inspired by broad squad-tactics principles;
- grid/position/cover/action-economy concepts may be used at the genre level;
- no protected names, exact UI, mission structures, classes, assets, or copied formulas from XCOM.

Documentation must define:
- initiative/turn order;
- action points;
- movement;
- cover;
- line of sight;
- range;
- terrain;
- elevation;
- status effects;
- reactions;
- suppression/control;
- injuries;
- morale if used;
- AI behavior;
- escape;
- nonlethal outcomes;
- rewards;
- integration with narrative state.

### Track L — Persistent rival / nemesis-like system
Target direction:
- original persistent rival/adversary memory system inspired by the general idea of enemies remembering prior encounters;
- do not copy proprietary names, branded hierarchy terminology, exact promotion ladders, UI, dialogue structure, or patented/protected implementation details.

Documentation must define an original system for:
- persistent enemy IDs;
- memory of encounters;
- wounds/scars;
- fear/respect/hatred;
- goals;
- faction standing;
- promotions/demotions only if original and systemically justified;
- survival/escape;
- rivalry triggers;
- relationship with world events;
- replacement succession;
- procedural titles only if original;
- player-safe presentation.

### Track M — Narrative, quests, knowledge, choices, and consequences
Covers:
- main/side/optional/lore quests;
- world knowledge;
- hidden knowledge;
- branching;
- reconvergence;
- mutually exclusive paths;
- consequence timing;
- NPC knowledge;
- player knowledge;
- reputation;
- persistent flags;
- authored randomness;
- fail states;
- world responses.

### Track N — Android application / APK architecture
Covers:
- Compose shell;
- navigation;
- Story;
- Map;
- Character;
- Stats;
- Equipment;
- Inventory;
- Quests;
- Settings;
- Developer tools;
- audio/narration;
- saves;
- accessibility;
- responsive layout;
- performance;
- asset loading;
- error states.

### Track O — QA, evidence, migrations, and release gates
Covers:
- unit tests;
- integration tests;
- Android instrumentation;
- screenshot QA;
- accessibility;
- performance;
- save migrations;
- state migrations;
- asset provenance;
- exact-head verification;
- emulator vs physical handset evidence;
- rollback.

### Track P — Final reconstruction program
The final phase uses all prior documentation to decide:
- what old code is retained;
- what is deprecated;
- what is deleted;
- what is cut from scope;
- what is rewritten;
- what is migrated;
- what is rebuilt from zero;
- how the APK evolves into the final application;
- how old placeholders are removed without losing authoritative gameplay state.

No final rebuild begins until the documentation and migration matrix are sufficiently complete.

## 6. Step-by-step execution order

### Phase 0 — Priority and authority
1. Mark Text-rpg-game as active priority.
2. Create global documentation index.
3. Create decision/gap register.
4. Point current reports to the new master program.
5. Preserve existing repository restrictions.
6. Record superseded/legacy reports rather than silently deleting them.

### Phase 1 — Current-state census
1. Inventory branches/PRs.
2. Inventory source modules.
3. Inventory screens.
4. Inventory gameplay systems.
5. Inventory current content.
6. Inventory assets.
7. Record lifecycle stage for every visual asset.
8. Record verification evidence.
9. Record missing evidence.

### Phase 2 — Gate Twelve complete documentation
Continue the existing Gate Twelve master plan through:
- geometry;
- visual language;
- asset decomposition;
- app UX;
- state overlays;
- performance;
- implementation;
- verification;
- migration;
- execution handoff.

### Phase 3 — Pixel-art integration system
Create:
- character-room panel specification;
- environment layer standard;
- overlay/reuse rules;
- character/NPC portrait and sprite rules;
- item/equipment/weapon/accessory rules;
- animation roadmap;
- map tile/atlas rules;
- visual state ownership rules.

### Phase 4 — World bible
Build the world hierarchy from global world -> political region -> settlement -> district -> location -> room -> interactable.

### Phase 5 — System bibles
Create separate bibles for:
- stats;
- skills;
- abilities;
- classes/ranks;
- items/equipment;
- economy;
- NPC simulation;
- ecology;
- beasts;
- combat;
- rival system;
- quests;
- social hierarchy;
- law/crime;
- progression.

### Phase 6 — Cross-system integration
Document how each system interacts with:
- time;
- travel;
- world state;
- UI;
- saves;
- NPC memory;
- quests;
- combat;
- economy;
- pixel-art state.

### Phase 7 — Prototype migrations
Replace only the systems whose target contract is already documented.

### Phase 8 — World/content expansion
Add settlements, factions, classes, beasts, loot, NPCs, and maps only through stable IDs and documented contracts.

### Phase 9 — Final APK reconstruction
Use the final migration matrix to remove obsolete presentation and rebuild the application shell around the documented game.

### Phase 10 — Release certification
Run exact-head verification, emulator QA, physical handset QA, save compatibility/migration tests, visual review, and documentation closure.

## 7. Change authority matrix

### May be changed freely on a working branch when documented and verified
- Compose layouts;
- presentation architecture;
- navigation;
- map rendering;
- scene presentation;
- asset loading;
- old placeholder/procedural art;
- technical geometry used only for placeholder visuals;
- tests;
- docs;
- build tooling;
- asset manifests;
- developer tools;
- internal APIs when migrated safely.

### May be replaced, but requires an explicit migration record
- stable IDs;
- save schema;
- player-safe projection;
- world-map graph;
- quest state;
- stats/rules formulas;
- ability state;
- equipment slots;
- NPC memory/state;
- persistence model;
- content IDs.

### Must not be silently changed
- hidden/story state semantics;
- player knowledge vs world truth;
- copyrighted/reference material boundaries;
- canonical facts already authored;
- user-only player agency rules where applicable;
- verification evidence.

### Protected repository operations
Still require their specific approval boundary:
- force-push;
- destructive history rewrite;
- delete repository;
- change visibility;
- publish store/release build;
- promote/merge `main` simply because routine engineering authority exists.

## 8. What is already decided

Currently documented and accepted:
- Text-rpg-game is the active project;
- Android narrative RPG with pixel-art presentation;
- authoritative engine feeds player-safe UI;
- nine current Gate Twelve locations;
- Gate Twelve three-macrozone spatial model;
- Depot Plaza public hub;
- Platform Nine internal hub;
- Gate Twelve threshold;
- Service Tunnel deeper branch;
- Quiet Stair alternate egress;
- Trace Chamber repeatable Trace training/research;
- 256x144 Gate Twelve map master;
- 32x48 gameplay-character production grid;
- 64x64 portrait target;
- 32x32 item icon target;
- 128x64 scene target;
- nearest-neighbor/source-native pixel rendering;
- layered paper-doll equipment;
- real pixel assets over placeholder geometry;
- references are not production assets;
- permanent art must not encode temporary gameplay state.

## 9. What is still undecided

Still requires documentation before locking:
- full world geography;
- kingdoms/states;
- city/village count;
- real-world scale;
- global coordinate convention;
- full ecology;
- beast taxonomy;
- loot economy;
- final class/rank model;
- full skill trees;
- complete passive system;
- combat formulas;
- rival/adversary system formulas;
- world-level scaling;
- full social hierarchy;
- law/crime systems;
- economy/currency expansion;
- full NPC simulation depth;
- full animation coverage;
- all character appearances;
- final player character visual identity details not already reference-approved;
- final APK navigation architecture;
- final save migration strategy;
- final performance budget;
- final release scope.

## 10. Required core documents

This program must eventually maintain at minimum:

- `docs/MASTER_DOCUMENTATION_PROGRAM.md`
- `docs/PROJECT_PRIORITY_AND_CONTEXT_ROUTING.md`
- `docs/DOCUMENTATION_INDEX.md`
- `docs/DECISION_AND_GAP_REGISTER.md`
- `docs/WORLD_AND_MAP_DEVELOPMENT_PROGRAM.md`
- `docs/PIXEL_ART_INTEGRATION_AND_REUSE_STANDARD.md`
- `docs/MECHANICS_REWORK_AND_REBUILD_PROGRAM.md`
- `docs/APK_EVOLUTION_AND_FINAL_REBUILD_PROGRAM.md`
- existing Gate Twelve master plan;
- existing Pixel Asset Master Plan;
- existing 001–500 asset roadmap;
- asset reference registry;
- task register;
- implementation status;
- verification/handoff records.

## 11. Completion rule

This master program is not complete when the file exists.

It is complete only when:
- each documentation track has an authoritative index;
- all major current systems have a status;
- all major planned systems have a design contract or are explicitly deferred;
- all destructive migrations have retain/rework/replace/delete decisions;
- all production assets have provenance/lifecycle state;
- all maps and zones have stable IDs and coordinates;
- all app screens have state ownership and UX contracts;
- combat/rival systems are original and documented;
- final APK reconstruction has a tested migration path;
- a new agent can resume from repository files without reconstructing the project from chat.

## Continuity handoff

Current action:
- this file establishes the global program;
- current Gate Twelve documentation Steps 1–4 remain valid and continue under this program;
- next documentation work should create the priority/context router, documentation index, decision/gap register, pixel-art integration standard, world/map program, mechanics rebuild program, and APK final-rebuild program;
- after those foundations, resume Gate Twelve Step 5 rather than skipping directly into bulk art or code reconstruction.
