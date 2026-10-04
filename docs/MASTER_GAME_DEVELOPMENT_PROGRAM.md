# THE GAME — Master Development & Documentation Program

Status: **PRIMARY PROJECT / DOCUMENTATION-FIRST / EXECUTION DEFERRED UNTIL CONTRACTS EXIST**  
Repository: `jbob-coder/Text-rpg-game`  
Priority designation: **CURRENT HIGHEST-PRIORITY GAME REPOSITORY**  
Program branch: `docs/master-game-development-program`  
Started: 2026-10-01 AST  
Owner authorization: broad game-development authority granted, subject to the explicit prohibitions, evidence rules, safety boundaries, and no-silent-downgrade rules already recorded in the repository.

---

## 0. Why this document exists

This document converts the owner's large 2026-10-01 directive into a repository-native program that can be executed across many sessions without repeatedly reconstructing intent from chat history.

The project is no longer treated as a collection of isolated UI, map, pixel-art, Android, rules-engine, and worldbuilding tasks. Those tasks are now subordinate tracks inside one long-range game-development program.

The program must answer, in durable documentation:

- what already exists;
- what is provisional;
- what is approved;
- what may be changed;
- what will be changed;
- what may be broken deliberately in order to rebuild correctly;
- what must never be silently broken;
- what pixel art exists and what stage it is in;
- what pixel art must be created;
- how characters, room actors, panels, equipment, props, overlays and map layers compose;
- what world geography is decided;
- what world geography is not decided;
- what mechanics exist;
- what mechanics need redesign, expansion, migration or replacement;
- how the world, items, creatures, NPCs, progression, tactical combat, dynamic rivals and social hierarchy fit together;
- how every document points to the next required document or implementation task;
- how the Android APK is eventually audited, dismantled where necessary, rebuilt and verified against the final documentation corpus.

The immediate goal is **documentation authority**, not mass implementation.

---

# 1. Project priority

## 1.1 Priority repository

For current game-development work, the repository

`jbob-coder/Text-rpg-game`

is the **priority repository**.

When prior chats, older handoffs, other game repositories, experimental prototypes or historical notes conflict with this repository's current documented direction, use the following priority order:

1. exact current repository source on the branch being worked;
2. exact-head tests/build/runtime evidence;
3. this Master Development & Documentation Program;
4. `docs/MASTER_DOCUMENTATION_RECORD.md` for the consolidated done/partial/missing/blocker state;
5. `docs/THE_GAME_MASTER_TASK_REGISTER.md`;
6. current domain master documents;
7. current context logs;
8. older handoffs and historical summaries;
9. memory/chat recollection.

The default `main` branch is still a placeholder and is not implementation authority merely because it is the default branch.

## 1.2 Other projects

Other repositories may remain historically useful, but they must not silently become authority for this game.

In particular:

- Godot Pixel RPG / goblin / underwater projects are separate unless an explicit migration record is created.
- Private campaign memory systems are separate unless an explicit migration record is created.
- Monster Choice / older prototypes are not visual or gameplay authority.
- External games supplied by the owner are design references only unless a specific concept is deliberately adapted into an original implementation.

A cross-project idea may be reused only after recording:
- source/reference;
- what abstract idea is being retained;
- what is being changed;
- what is rejected;
- why the resulting design is original and compatible with this game.

---

# 2. Owner authorization and boundaries

## 2.1 Broad development permission

The owner explicitly grants broad permission to:

- create, rewrite, expand and reorganize game documentation;
- create new development branches;
- create or replace pixel-art systems;
- improve the Android presentation;
- replace weak UI layouts;
- restructure map presentation;
- create new original assets;
- author new world systems;
- expand the rules engine;
- redesign progression;
- add tests and verification infrastructure;
- break presentation-level compatibility where necessary to replace it with a documented better design;
- deprecate or remove obsolete presentation assets and code after migration evidence exists;
- create migration plans for save/content/state changes;
- create new original gameplay systems inspired by broad genre patterns.

This permission is not permission to ignore earlier explicit prohibitions.

## 2.1.1 Current execution authorization — updated 2026-10-04 AST

The owner has now **explicitly authorized transition beyond documentation-only work** and granted broad project-development execution permission.

Current interpretation:
- documentation remains a required authority layer and must stay synchronized with implementation;
- bounded implementation, refactoring, tooling, testing, runtime work, and asset production may proceed when they serve the current objective;
- agents do not need a second routine confirmation merely because work crosses from documentation into implementation or asset production;
- changes should remain evidence-driven, reversible where practical, migration-aware, and performed on appropriate working branches;
- implementation must not silently contradict current domain contracts; when design changes, update the contract and migration record;
- broad permission does not convert destructive, externally consequential, security-sensitive, financial, or repository-governance actions into routine work.

The earlier documentation-only asset/implementation freeze is therefore **superseded as a current-phase restriction**. Its historical purpose remains relevant: documentation and contracts must exist before large or destructive expansion.

Standing safeguards in section 2.2 and repository-level approval boundaries remain in force.

## 2.2 Standing prohibitions still apply

Do not:

- treat `main` as implementation authority;
- silently merge/promote branches;
- force-push or rewrite shared history without an explicit repository operation decision;
- delete durable data without a migration and rollback boundary;
- claim physical Galaxy A03 validation from emulator evidence;
- expose hidden/raw state to player UI;
- move authoritative gameplay logic into Compose presentation code;
- silently change stable IDs;
- silently change save schema;
- use unrelated repository assets as if they belonged here;
- use Code Assistant/plugin workflows previously prohibited by the owner;
- copy protected characters, names, maps, art, UI, dialogue, lore or distinctive presentation from another commercial game;
- claim a reference image is production pixel art merely because it looks pixelated;
- create geometry only because it is easy to draw when authored art is required;
- downgrade approved art or established behavior without an explicit replacement decision.

## 2.3 What may be deliberately broken

A subsystem may be deliberately broken and rebuilt when all of the following are true:

1. the existing behavior is documented;
2. the reason it is insufficient is documented;
3. the replacement contract is written first;
4. authoritative data ownership is preserved or migrated explicitly;
5. migration impact is known;
6. tests or QA exist for the replacement;
7. a rollback boundary exists when practical;
8. the change happens on a working branch;
9. exact-head verification is performed before promotion.

Presentation code is more replaceable than persistent gameplay state.

## 2.4 What cannot be casually broken

High-risk contracts include:

- save compatibility;
- stable content IDs;
- item IDs;
- NPC IDs;
- quest IDs;
- location IDs;
- player-safe projection boundaries;
- authoritative route legality;
- equipment slot semantics;
- resource/stat semantics;
- hidden-state boundaries;
- current verified gameplay progression;
- asset provenance.

Breaking these requires a migration document, not merely a visual improvement rationale.

---

# 3. Documentation-first program

## 3.1 User-specified scale target

The owner requested an extremely large long-range documentation corpus, including the phrases:

- “3,000 documentation”;
- “2,000 guide and planning”;
- “10,000 map development”;
- a final “10,000” APK/development reconstruction section;
- an overall target described as “2,000,000 documentation.”

The unit of those numeric targets was not explicitly defined as words, lines, records, files or documents.

Therefore:

- preserve the requested numbers;
- do not fabricate that they mean a specific unit;
- track **document count**, **word count**, **structured records**, **guide entries**, **map records**, and **implementation tasks** separately;
- do not claim the numerical target has been completed until the metric itself is explicitly resolved or the owner accepts the tracker interpretation.

The practical objective is a reconstruction-grade corpus large enough that a new session can understand and build the game without relying on chat memory.

## 3.2 Documentation classes

The corpus is divided into these classes:

### A. Authority and governance
Defines:
- project priority;
- source-of-truth order;
- permissions;
- prohibitions;
- branch policy;
- migration policy;
- evidence standards;
- completion criteria.

### B. World bible
Defines:
- world hierarchy;
- historical eras;
- geography;
- political entities;
- cities;
- villages;
- districts;
- wilderness;
- resources;
- ecosystems;
- beasts;
- institutions;
- economies;
- citizen classes;
- prejudice/discrimination systems;
- routes;
- technology;
- infrastructure.

### C. Gameplay systems
Defines:
- stats;
- skills;
- abilities;
- passives;
- classes;
- ranks;
- equipment;
- loot;
- items;
- activities;
- quests;
- relationships;
- NPC autonomy;
- world simulation;
- tactical combat;
- dynamic rival/memory systems;
- balance and progression.

### D. Visual production
Defines:
- pixel style;
- native grids;
- characters;
- portraits;
- room actors;
- environmental assets;
- map assets;
- overlays;
- animation;
- UI art;
- item icons;
- paper-doll equipment;
- reuse/compatibility rules;
- provenance and QA.

### E. Application / Android
Defines:
- screen architecture;
- game-state projection;
- touch behavior;
- navigation;
- responsive design;
- accessibility;
- save/load;
- audio/narration;
- developer tools;
- build/release pipeline;
- final APK rebuild.

### F. Implementation guides
Defines:
- exact task sequences;
- dependency graphs;
- migrations;
- tests;
- branch stacks;
- verification;
- rollback;
- evidence capture.

### G. Continuity and audits
Defines:
- current exact HEAD;
- what changed;
- what is pending;
- known contradictions;
- missing assets;
- blocked decisions;
- QA gaps;
- next action.

---

# 4. Long-range documentation volumes

The program will be authored as linked volumes, not one unmaintainable file.

## Volume 00 — Program authority
Documents:
- this file;
- `docs/MASTER_DOCUMENTATION_RECORD.md` — consolidated documentation state, completed work, gaps, blockers and next actions;
- task register;
- cross-reference matrix;
- context-log index;
- branch/evidence policy.

## Volume 01 — Existing-state audit
Must inventory:
- Python engine;
- Android client;
- content pack;
- tests;
- current PR stack;
- current pixel-art assets;
- current UI;
- current map;
- current saves/schema;
- current known technical debt.

Output:
- KEEP / REWORK / REPLACE / REMOVE / UNKNOWN classification for each major subsystem.

## Volume 02 — Pixel-art production system
Must cover:
- scene masters;
- room actors;
- player and NPC paper dolls;
- portraits;
- equipment layers;
- props;
- environment modules;
- map tiles;
- state overlays;
- animation layers;
- reuse compatibility;
- asset lineage;
- QA.

Primary companion:
`docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`.

## Volume 03 — Gate Twelve region
Current documents:
- `GATE_TWELVE_REGION_MASTER_PLAN.md`;
- `GATE_TWELVE_MAP_PIXEL_ASSET_BLUEPRINT.md`;
- `GATE_TWELVE_MAP_ANIMATION_BLUEPRINT.md`.

Gate Twelve is the first detailed implementation region and the proving ground for the world pipeline.

## Volume 04 — World development
Primary companion:
`docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`.

Must eventually contain structured records for:
- continents / macroregions;
- nations / kingdoms / city-states;
- cities;
- villages;
- districts;
- interiors;
- roads;
- transit;
- underground;
- beast zones;
- resource zones;
- ecosystems;
- NPC populations;
- factions;
- institutions.

## Volume 05 — Character and social simulation
Must define:
- player identity;
- recurring NPCs;
- generated/supporting NPC rules;
- personality;
- memory;
- goals;
- schedules;
- relationships;
- citizen hierarchy;
- discrimination/prejudice systems;
- faction loyalties;
- rival evolution.

## Volume 06 — Progression
Must define:
- attributes;
- derived stats;
- skills;
- abilities;
- passives;
- techniques;
- classes;
- ranks;
- professions;
- citizen status;
- training;
- mastery;
- costs;
- resources;
- caps;
- progression curves.

## Volume 07 — Items / economy / loot
Must define:
- item taxonomy;
- equipment;
- accessories;
- materials;
- rarity/quality;
- vendors if later authored;
- repair if later authored;
- loot tables;
- beast drops;
- resource extraction;
- economy sinks/sources;
- ownership/provenance.

## Volume 08 — Tactical combat
The target may use broad tactical inspirations such as:
- turn-based positioning;
- cover;
- line-of-sight;
- action economy;
- destructible/interactive terrain;
- status effects;
- squad/party roles;
- persistent injuries;
- tactical AI.

The implementation must be original. Do not reproduce another game's names, UI, exact class trees, maps, formulas or signature presentation.

## Volume 09 — Dynamic rivals and world memory
The target may use the broad fantasy of a world where recurring enemies/NPCs:
- remember encounters;
- gain traits;
- form grudges;
- rise/fall in hierarchy;
- react to player history;
- change relationships and goals.

The implementation must use original terminology, data structures, progression rules and presentation. It must not clone a proprietary named system or its distinctive expression.

## Volume 10 — Activities and life simulation
Must define:
- training;
- rest;
- work;
- research;
- crafting only if intentionally added;
- travel;
- social visits;
- contracts;
- exploration;
- resource collection;
- downtime;
- world events.

## Volume 11 — UI/UX and player experience
Must define every major screen:
- Story;
- Map;
- Character;
- Stats;
- Skills;
- Equipment;
- Inventory/Bag;
- Quests;
- Relationships;
- world information;
- settings;
- save/load;
- developer tools.

## Volume 12 — Android architecture and final APK rebuild
Primary companion:
`docs/android/APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md`.

This is deliberately late in the program.

The final APK rebuild must be driven by the completed system contracts instead of repeatedly patching presentation without knowing the final shape.

---

# 5. World-coordinate program

## 5.1 Coordinate hierarchy

The final world model must distinguish:

1. world coordinate;
2. macroregion coordinate;
3. kingdom/nation coordinate;
4. settlement coordinate;
5. district coordinate;
6. location/building coordinate;
7. room/interior coordinate;
8. tactical encounter coordinate;
9. visual presentation coordinate.

These systems must not be conflated.

Example:
- Gate Twelve map uses a 256x144 **presentation** grid;
- its gameplay map currently uses percentage-style node positions and authored graph edges;
- a future world map may use a different logical coordinate system.

A coordinate conversion/mapping contract must be documented before world-scale tooling is built.

## 5.2 Map record requirements

Every authored world place eventually needs:
- stable ID;
- display name;
- place class;
- parent region;
- logical coordinate;
- visual coordinate if applicable;
- entrances/exits;
- travel edges;
- travel cost model;
- terrain;
- climate;
- resources;
- hazards;
- beast presence;
- NPC population;
- faction control;
- legal/social status;
- services;
- loot/resource opportunities;
- quest hooks;
- discovery rules;
- state variants;
- asset references;
- performance/loading cell;
- verification status.

## 5.3 Gate Twelve as first proof

Gate Twelve is the first fully documented district.

Do not expand to thousands of places by copying empty templates before Gate Twelve proves:
- place hierarchy;
- geometry;
- asset decomposition;
- route behavior;
- player-safe presentation;
- application UX;
- state layering;
- loading/performance strategy.

---

# 6. Pixel-art integration decisions

The detailed standard is in:
`docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`.

Core program decisions:

1. Pixel art is not a single flattened screenshot.
2. A room is composed from:
   - base environment;
   - permanent props;
   - state overlay;
   - character actors;
   - item/interaction props;
   - FX;
   - UI/panel layer.
3. Characters that are actually present in a room can receive room-scene actor sprites and player-facing character panels.
4. Character panels must be driven by projected actor presence, not hidden NPC state.
5. Player paper-doll equipment remains layered and tied to authoritative equipped items.
6. Reusable assets require shared:
   - pixel density;
   - perspective;
   - palette/value family;
   - lighting direction;
   - anchor conventions;
   - z-order;
   - state ownership.
7. Existing source-native pixel art may be reused when compatible.
8. Generated references may guide reconstruction but are not automatically production masters.
9. Final art direction must be cohesive pixel-art RPG and not neon/cyberpunk by default.
10. Geometry is not a substitute for actual art.

---

# 7. Character-in-room and panel direction

A future room presentation may include:
- room/environment art;
- player sprite;
- one or more visible NPC sprites;
- actor focus/portrait panel;
- dialogue/narrative panel;
- choices/actions;
- status/context controls.

Rules:

- actor presence must be explicitly projected by the engine/content layer;
- do not infer an NPC is present merely from a scene name in Compose once a formal actor projection exists;
- current `PixelStoryActorCatalog` scene/location binding is an acceptable transitional implementation but should evolve toward a reusable projected actor model;
- an actor panel may show only player-safe data;
- the same recurring NPC identity must reuse the same approved identity master across room sprites, portraits and panels;
- temporary pose/emotion/state is an overlay/variant, not a new identity.

Required future contract:
`GameSnapshot.actors` or an equivalent player-safe projected actor list.

That contract is not yet implemented and must be designed before the UI is rebuilt around dynamic actor panels.

---

# 8. Mechanics audit program

Every mechanic receives one of five statuses:

- KEEP;
- EXTEND;
- REWORK;
- REPLACE;
- REMOVE.

Current broad starting classification:

## KEEP / preserve unless evidence changes
- data-driven content;
- deterministic state transitions;
- stable IDs;
- player-safe projection concept;
- relationships;
- NPC knowledge/memory/goals;
- quest graphs;
- equipment slots;
- perks/conditions;
- ability/technique progression;
- save/load with schema versioning;
- authoritative engine -> UI separation.

## EXTEND
- world map;
- NPC autonomy;
- social simulation;
- world events;
- inventory/equipment content depth;
- abilities;
- activities;
- classes/ranks;
- economy;
- world geography;
- pixel-art coverage;
- animation.

## REWORK
- current branch governance;
- outdated status/handoff pointers;
- map presentation;
- provisional avatar art;
- room actor system;
- screen information architecture where current layout blocks the intended experience;
- current fragmented visual pipeline where older procedural art still competes with authored pixel masters.

## REPLACE when the replacement contract is ready
- obsolete technical/geometric placeholders;
- outdated visual masters that conflict with approved references;
- presentation-only implementations that cannot support modular art/state layering.

## UNKNOWN / must be designed before changing
- final stat schema;
- final class system;
- final citizen rank hierarchy;
- final combat action economy;
- final tactical map scale;
- final dynamic-rival design;
- final economy/crafting system;
- final world-level scaling;
- final save migration needs;
- final release architecture.

---

# 9. Tactical combat direction

The tactical battle system should feel deliberate, spatial and persistent.

Desired principles:
- meaningful positioning;
- action economy;
- cover/terrain;
- line-of-sight;
- initiative/turn order;
- ability costs;
- status effects;
- injuries/conditions;
- environment interaction;
- enemy intent/AI;
- party roles;
- retreat/surrender when appropriate;
- consequences persisting after battle.

Originality rules:
- create original names and UI;
- create original calculations;
- create original class/ability trees;
- create original enemy archetypes;
- create original encounter maps;
- avoid copying another game's exact action-point values, cover iconography, faction structures, visual grammar or tutorial sequence.

Combat must integrate with the existing stat/ability/state system rather than becoming a separate disconnected game.

---

# 10. Dynamic rival / memory direction

The desired world should support recurring agents who evolve from history.

Potential original-system concepts:
- encounter memory;
- injury/scar history;
- victories/defeats;
- fear/respect/resentment;
- faction reputation;
- promotion/demotion;
- rivalry;
- mentorship;
- revenge goals;
- territory influence;
- social connections;
- rumor propagation;
- player recognition.

Do not call the shipped system by another game's proprietary system name.

Before implementation, write:
- state model;
- event model;
- persistence contract;
- rank/hierarchy rules;
- mutation limits;
- anti-exploit rules;
- content-generation boundaries;
- UI presentation;
- deterministic testing strategy.

---

# 11. Social hierarchy, class and discrimination

The world may contain:
- economic class;
- legal status;
- occupation rank;
- institutional rank;
- citizenship;
- faction standing;
- inherited status;
- species/beast-related prejudice;
- regional prejudice;
- ability-based social stratification.

These are worldbuilding/game systems, not a license to use real-world protected groups as a shortcut for hostility.

Every discrimination mechanic must define:
- fictional basis;
- institutions enforcing it;
- historical origin;
- player-facing consequences;
- NPC variation;
- exceptions;
- resistance/reform groups;
- gameplay effects;
- narrative purpose.

Avoid reducing populations to one trait or making prejudice a purely cosmetic label.

---

# 12. Asset creation program

The existing v1 asset roadmap contains 500 planned units.

The larger program will not blindly discard it.

For every planned/created asset track:
- stable asset ID;
- family;
- gameplay binding;
- current stage;
- source/reference;
- blueprint;
- production file;
- integration consumer;
- replacement status;
- native-scale QA;
- Android-scale QA;
- physical-device QA where required;
- canon approval.

Additional asset families required by the expanded program include:
- world-map tiles;
- regional biomes;
- city/village architecture;
- kingdom/faction heraldry;
- citizen class clothing;
- professions;
- beasts;
- beast parts;
- loot;
- resources;
- tactical terrain;
- tactical cover;
- weapons/tools if authored;
- accessories;
- skills/classes/ranks icons;
- activities;
- NPC portraits;
- actor pose sets;
- room panels;
- combat feedback;
- world-state overlays.

Do not create all of them before their data models exist.

---

# 13. Documentation cross-reference rule

Every master document must include:
- scope;
- authority;
- inputs;
- outputs;
- dependencies;
- decisions;
- unknowns;
- prohibited assumptions;
- implementation consumers;
- verification;
- next document/action.

The repository-level cross-reference is:
`docs/DOCUMENTATION_CROSS_REFERENCE_MATRIX.md`.

No major document should become an isolated dead end.

---

# 14. Branch program

Recommended documentation branches:

- `docs/master-game-development-program` — repository-wide authority and indexes.
- `docs/world-master` — world hierarchy/geography/economy/ecosystem.
- `docs/progression-master` — stats/skills/classes/ranks/abilities.
- `docs/combat-master` — tactical combat.
- `docs/social-rival-master` — NPC/social/rival simulation.
- `docs/pixel-production-master` — art composition, asset lifecycle, QA.
- `docs/android-final-rebuild` — late-stage APK reconstruction.

Implementation branches should stack only when dependency is explicit.

Do not create hundreds of empty branches. Create a branch when a bounded document or implementation slice has a real deliverable.

---

# 14.1 Three-track execution direction

The project now operates three synchronized tracks.

## Track A — Full reconstruction corpus
Expand the complete documentation graph across every game domain using the first-pass quota authority:
- `docs/FIRST_PASS_DOMAIN_DOCUMENTATION_QUOTAS.md`.

## Track B — Phase 1 solo playable
Maintain a bounded Gate Twelve playable integration line governed by:
- `docs/PHASE_1_SOLO_PLAYABLE_PARALLEL_TRACK.md`.

Track B waits only for the direct contracts it consumes. It must not be blocked by unrelated long-range corpus expansion.

## Track C — Synchronization and evidence
Keep documentation, implementation and evidence aligned.

Every meaningful task closure must update:
- task status;
- evidence;
- affected domain/quota;
- Phase 1 impact where relevant;
- dependencies unlocked or newly blocked;
- the next recommended direction;
- stale NEXT instructions;
- master/index documents whose status changed.

A task is not operationally closed if the repository still points future agents toward an obsolete next action.

# 15. Execution gates

## Gate 1 — documentation authority
Required before large redesign:
- master program;
- cross-reference matrix;
- priority pointer;
- current-state audit.

## Gate 2 — domain contracts
Required:
- world contract;
- progression contract;
- combat contract;
- social/NPC contract;
- visual contract;
- Android UX contract.

## Gate 3 — data schemas
Required:
- stable IDs;
- persistence;
- migrations;
- registries;
- state projections.

## Gate 4 — prototype implementations
One bounded example per system:
- one region;
- one tactical encounter;
- one dynamic rival chain;
- one class/progression route;
- one reusable room actor/panel flow;
- one world resource/ecosystem loop.

## Gate 5 — integration
Connect systems without duplicating authority.

## Gate 6 — final Android rebuild
Only after the final documents describe:
- what to keep;
- what to remove;
- what to replace;
- migration sequence;
- target screen architecture;
- target asset system;
- verification.

---

# 16. Current established facts versus future targets

## Established
- deterministic Python RPG engine exists;
- Android Compose client exists;
- player-safe projection exists;
- Gate Twelve playable content exists;
- nine named district locations exist;
- current world graph exists;
- pixel-art catalogs and raster resources exist;
- 500-unit v1 pixel-asset planning baseline exists;
- current scene/state overlays exist;
- paper-doll equipment contract exists;
- player and Tamsin visual work exists on dedicated branches;
- map-art and environment work exists on dedicated branches;
- automated Android/emulator evidence exists for several exact heads.

## Not established
- complete world;
- kingdoms/nations;
- final city/village network;
- final class system;
- final citizen hierarchy;
- final discrimination model;
- final beast ecology;
- final loot economy;
- final tactical combat system;
- final dynamic-rival system;
- final world-level balance;
- final Android screen architecture;
- final save migration;
- final APK.

The documentation must never write a future target as though it already exists.

---

# 17. Immediate repository-wide documentation tasks

Priority order:

1. create this master program;
2. create cross-reference matrix;
3. create pixel-art runtime composition standard;
4. create world-development master index;
5. create Android rebuild/evolution master plan;
6. create a durable context-log record for the owner's 2026-10-01 directive;
7. update task register to point to this program;
8. update implementation status so old stabilization work is historical, not current objective;
9. update asset index to point to the new composition standard;
10. update context-log index;
11. update root README on this branch to identify the current priority program;
12. open a draft PR for review without merging to `main`.

---

# 18. Completion definition for this program stage

This first repository-wide documentation stage is complete when:

- all immediate documents above exist;
- indexes point to them;
- old status files no longer imply V6 stabilization is the current top objective;
- the repository clearly states that documentation is primary;
- pixel-art use/reuse/overlay rules are explicit;
- the world-development scope is decomposed;
- the final APK rewrite is explicitly last-stage work;
- the next action is unambiguous.

This stage does not mean the total long-range documentation corpus is complete.

---

# 19. Continuity handoff

Current top-level objective:

**Build the complete documentation authority for THE GAME before broad implementation expansion.**

Read next:

1. `docs/DOCUMENTATION_CROSS_REFERENCE_MATRIX.md`
2. `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`
3. `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`
4. `docs/android/APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md`
5. `docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md`
6. `docs/THE_GAME_MASTER_TASK_REGISTER.md`

Do not start mass world generation, mass asset generation or final APK reconstruction until the corresponding contracts are written.

# 20. 2026-10-02 directive-expansion batch

The owner's expanded directive is now decomposed into dedicated decision documents rather than being left only in chat/context.

New current documents:
- `docs/MASTER_DIRECTIVE_EXECUTION_BREAKDOWN.md` — complete step order from documentation authority through world/system design and final APK promotion.
- `docs/EXISTING_STATE_REWORK_DECISION_MATRIX.md` — KEEP / EXTEND / REWORK / REPLACE / REMOVE / NEW decisions.
- `docs/DOCUMENTATION_PROGRESS_LEDGER.md` — preserves the 3,000 / 2,000 / 10,000 / 10,000 / 2,000,000 targets without inventing their unit.
- `docs/assets/PIXEL_ART_PRODUCTION_AND_REUSE_LEDGER.md` — current-vs-required pixel art, room actor/panel composition, overlay/reuse rules, area packet requirements.
- `docs/world/WORLD_SCALE_DOCUMENTATION_BLUEPRINT.md` — coordinate hierarchy and schemas for places, political entities, settlements, resources, ecosystems, beast zones, population, loot and balance.
- `docs/systems/GAMEPLAY_SYSTEM_REBUILD_MATRIX.md` — stats/skills/abilities/classes/ranks/social hierarchy/activities/combat/adversary/NPC/save decisions.
- `docs/android/APK_FINAL_RECONSTRUCTION_MATRIX.md` — final keep/rework/replace/remove model for the Android client.

These documents supplement this master program. They do not authorize mass implementation by themselves.

## 20.1 Current program state

Documentation remains the primary objective.

Immediate order:
1. finish Gate Twelve Steps 8–14;
2. perform the deeper existing-state source audit;
3. write the progression/class/rank master;
4. write the NPC/social/adversary master;
5. write the item/economy/loot master;
6. write the tactical combat master;
7. write the application UX master;
8. write save/content migrations;
9. then schedule broad rebuilds.

## 20.2 Rebuild authority

Broad development permission is recorded, but destructive work remains migration-gated.

Presentation may be deliberately replaced once:
- the target contract exists;
- consumers are known;
- replacement is implemented;
- exact-head tests/evidence are green.

Persistent state, stable IDs and save data require stronger migration gates.

## 20.3 World-scale authoring rule

Do not satisfy the requested world scale with filler.

Each permanent world record must participate in:
- coordinates;
- containment;
- routes;
- polity/faction;
- resources/ecology;
- threat/balance;
- NPC/population;
- visual kit;
- state/content hooks.

The requested numerical scale is tracked in `DOCUMENTATION_PROGRESS_LEDGER.md` until its unit is explicitly accepted.

## 20.4 Pixel-art rule

Final visuals are assembled from reusable compatible layers rather than one flattened generated image.

The production/reuse ledger is now the required companion for:
- Jack;
- Tamsin;
- room actors;
- panels;
- Gate Twelve area packets;
- world-map kits;
- overlays;
- text/signage;
- animation;
- asset-stage tracking.

## 20.5 Final APK rule

The current Android application is a verified foundation, not the final product.

The late-stage APK rebuild must consume the final world/system/visual contracts, then classify every component as:
KEEP / EXTEND / REWORK / REPLACE / REMOVE.

No mass deletion is authorized before that audit/migration sequence.


# 21. 2026-10-02 corpus-architecture continuation

The full-scope directive is now decomposed one layer further.

New active child authorities:
- `docs/DOCUMENTATION_CORPUS_ARCHITECTURE.md`;
- `docs/world/WORLD_GEOGRAPHY_STANDARD.md`;
- `docs/world/WORLD_POLITICAL_ENTITIES.md`;
- `docs/world/WORLD_SETTLEMENT_CATALOG.md`;
- `docs/world/WORLD_TRAVEL_AND_ROUTES.md`;
- `docs/assets/ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md`.

These documents formalize:
- how the very large documentation corpus is split into maintainable volumes and records;
- how world coordinates and geography scale without forcing one coordinate system;
- how kingdoms/states/political hierarchies will be represented without inventing canon prematurely;
- how cities/villages/settlements are authored as functional places rather than names;
- how route legality remains world authority while art/UI visualize it;
- how each room/area composes environment, player, NPC actors, equipment, panels, text, overlays, FX and reusable art coherently.

Current priority remains documentation. Gate Twelve Steps 1–14 are now complete as the first proof-region planning packet. The next P0 tracks are the exact existing-state repository audit and a reproducible corpus/world/asset inventory before broad runtime migration.


## 2026-10-02 operational continuation

- [Decision/rebuild execution register](DECISION_AND_REBUILD_EXECUTION_REGISTER.md): decomposed owner requirements, can/will/candidate changes, migration gates and unresolved corpus units.
- [Full baseline document catalog](DOCUMENTATION_CATALOG_2026-10-02.md): every tracked Markdown file, actual headings, words, hashes and literal references; semantic audit remains separate.
- [World canon decision queue](world/WORLD_CANON_DECISION_QUEUE.md): exact nine-node/eight-edge baseline and ordered unresolved geography/politics/ecology/progression decisions.
- [Room composition implementation contract](assets/ROOM_COMPOSITION_IMPLEMENTATION_CONTRACT.md): current actors versus proposed presence projection, focus panels, pixel/text reuse and raster-precedence gates.
- [Raster delivery evidence](assets/RASTER_DELIVERY_EVIDENCE_2026-10-02.md): all 24 baseline PNG dimensions, hashes and catalog bindings.

These supplement existing masters. They do not supersede approved identity references or imply new gameplay APIs.


## 2026-10-02 final reconstruction integration update

The program now has an integration-level execution authority at `docs/FINAL_GAME_RECONSTRUCTION_BLUEPRINT.md`.

It is subordinate to this master program and above domain-specific implementation planning. It consolidates:
- exact change/preserve/rework/replace/remove vocabulary;
- visual asset creation/stage/reuse decisions;
- room actor + portrait/panel projection direction;
- Gate Twelve per-area production gaps;
- world facts already decided versus canon still intentionally undecided;
- mechanics KEEP/EXTEND/REWORK/REPLACE/NEW decisions;
- tactical-combat and persistent-adversary originality boundaries;
- final APK deconstruction/rebuild gates;
- immediate P0 reconciliation packets.

New work must use the blueprint to choose the correct domain owner rather than creating another competing master document.
