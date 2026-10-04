# THE GAME — Final Game Reconstruction Blueprint

Status: **PRIMARY INTEGRATION BLUEPRINT / DOCUMENTATION-FIRST / IMPLEMENTATION GATED**  
Repository: `jbob-coder/Text-rpg-game`  
Program branch: `docs/master-game-development-program`  
Parent authority: `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`  
Created: 2026-10-02 AST

## 1. Purpose

This document is the integration layer for the owner's full-scope directive.

It does not replace the domain masters. It connects them so a future session can answer, without relying on chat memory:

- what exists now;
- what is only provisional;
- what is planned;
- what may change;
- what will change;
- what may be intentionally broken and rebuilt;
- what must not be casually broken;
- which pixel-art assets exist and what production stage they are in;
- what visual assets still need to be created;
- how environment art, characters, equipment, overlays, text-art, FX and contextual panels combine;
- what world facts are decided;
- what world facts remain undecided;
- which mechanics are preserved, expanded, reworked, replaced or new;
- how the 3,000 / 2,000 / 10,000 / 10,000 / 2,000,000 documentation targets are tracked without inventing a unit;
- how the final Android/APK is audited, dismantled where justified, rebuilt, verified and promoted.

This repository is the priority game repository. Other game repositories remain historical/reference material unless an explicit migration record imports something.

## 2. Source-of-truth order

When records conflict, use:

1. exact current source/data on the branch/HEAD being changed;
2. exact-head test/build/runtime evidence;
3. `MASTER_GAME_DEVELOPMENT_PROGRAM.md`;
4. this integration blueprint;
5. domain master documents;
6. `THE_GAME_MASTER_TASK_REGISTER.md`;
7. current audits and provenance registries;
8. historical handoffs;
9. chat memory.

`main` is still a placeholder and is not implementation authority.

## 3. Decision vocabulary

Every significant subsystem, document, asset family and world record should use one or more of these states:

- **LOCKED CONTRACT** — may change only through an explicit migration/decision.
- **KEEP** — preserve current behavior/data contract.
- **EXTEND** — preserve the contract and add capability.
- **REWORK** — keep responsibility, substantially change implementation/presentation.
- **REPLACE** — target implementation differs; migration required.
- **NEW** — target capability does not yet exist at required scope.
- **REMOVE AFTER MIGRATION** — deletion is allowed only after consumers are migrated and evidence exists.
- **PROVISIONAL** — currently usable but not final/canon-approved.
- **UNDECIDED** — no canon/design decision yet.
- **BLOCKED** — intentionally gated by another contract or evidence requirement.
- **SUPERSEDED** — retained as evidence but no longer target direction.
- **REJECTED** — explicitly not the target.

A planned replacement is not permission to delete the old system immediately.

### 3.1 Current-phase asset-production boundary

The current program is a **documentation/reconstruction-authority phase**, not an active asset-production phase.

For the current phase:

- existing assets may be inspected, inventoried, classified, traced to consumers, and documented;
- future assets may receive briefs, technical specifications, native-grid requirements, composition rules, reuse classes, provenance requirements, QA gates, and implementation/migration instructions;
- documents may identify which assets should later be created, reworked, replaced, promoted, or retired;
- **no new runtime asset is to be created, modified, regenerated, exported, integrated, promoted, replaced, or deleted unless the owner explicitly authorizes that production/implementation step**;
- a completed asset brief, provenance record, production packet, or migration map does **not** itself authorize production;
- historical implementation branches remain evidence only unless separately selected for migration.

When this blueprint uses words such as `create`, `produce`, `replace`, or `integrate` in target-state or future-sequence sections, read them as **future required work**, not current execution authority.

## 4. What is locked or presumed preserved

Until a migration document says otherwise:

- deterministic Python gameplay authority;
- player-safe projection boundary;
- hidden/private state isolation from Android presentation;
- stable IDs for locations, quests, items, NPCs and authored content;
- save compatibility/versioning discipline;
- equipment slot semantics;
- authoritative route legality/discovery;
- authoritative stat/resource meaning for existing saves/content;
- source/asset provenance;
- exact verified behavior for an implementation head being used as a migration source.

These may evolve, but not through a silent presentation-only change.

## 5. What may change freely on a working branch

Subject to tests, provenance and migration boundaries, the project may:

- reorganize or expand documentation;
- replace weak UI layouts;
- redesign pixel presentation;
- improve map/room art;
- create new original assets;
- add room actors and portraits;
- add player-safe projected fields;
- expand world registries;
- create new classes/ranks/professions;
- redesign progression through an explicit migration;
- create tactical combat;
- create persistent adversary simulation;
- expand NPC/world simulation;
- replace provisional art;
- deprecate stale presentation code;
- change application navigation;
- create new tests/tooling;
- rebuild the APK late in the program.

## 6. What will change under the current target

The current target explicitly calls for:

1. one reconciled canonical implementation line instead of many unresolved stacked/sibling PRs;
2. production Jack visual identity replacing the generic/provisional player appearance;
3. fuller recurring-NPC identity families, including room actor + portrait/panel consistency;
4. authored modular pixel environments replacing weak technical/geometric presentation where appropriate;
5. final Gate Twelve visible map art using an approved authored raster/master rather than a procedurally reconstructed substitute;
6. a player-safe actor-presence projection capable of driving contextual room actors and panels;
7. progression/class/rank/profession/citizen-status taxonomy beyond the current limited runtime scope;
8. richer NPC schedules, factions, memory and social simulation;
9. original tactical positional combat;
10. an original persistent adversary network built on stable NPC identity and memory;
11. world-scale geography, politics, settlements, ecology, resources, beast zones, population and travel;
12. a final Android experience reconstructed from the documented domain contracts;
13. removal of obsolete presentation paths only after replacements, migration and evidence exist.

## 7. Documentation-scale program

Owner targets preserved exactly:

- 3,000 documentation;
- 2,000 guide/planning;
- 10,000 map-development scope;
- 10,000 final APK/development scope;
- 2,000,000 total documentation.

The unit remains unresolved. Therefore progress is tracked independently by:

- documents;
- words;
- stable structured records;
- guide/planning entries;
- place/route/zone records;
- asset records;
- world entities;
- mechanics/system records;
- tasks;
- tests;
- QA/evidence records.

No target is declared complete by silently choosing one convenient metric.

## 8. Pixel-art production architecture

### 8.1 Native families

Current production standards include:

- 16x16 micro/status/icon material;
- 24x24 navigation/UI icons;
- 32x32 item/prop icons;
- 32x48 gameplay actors and paper-doll layers;
- 64x64 portraits and bounded FX;
- 128x64 location/room scene masters;
- 256x144+ district/map masters.

Nearest-neighbor and integer/source-native alignment remain the target.

### 8.2 Runtime layer order

Back to front:

1. environment/base;
2. structural modules;
3. permanent props;
4. ambient decals;
5. room actors;
6. actor equipment/held objects;
7. player-safe state overlays;
8. transient FX;
9. contextual portrait/focus panel;
10. UI text/actions.

No lower presentation layer owns gameplay reachability, hidden quest state or NPC truth.

### 8.3 Reuse classes

- **R0 exact reuse** — same grid, perspective, role and state meaning.
- **R1 material/palette variant** — geometry reusable, local material/light adaptation required.
- **R2 structural-kit reuse** — walls, rails, doors, pipes, props recomposed into a new authored area.
- **R3 motion-rig reuse** — animation timing/anchor reusable, identity-specific pixels remain unique.
- **R4 semantic UI-family reuse** — same UI function, local icon/art may differ.
- **NO-REUSE** — identity-specific faces, unique landmarks, incompatible perspective/scale/state or story-specific art.

Reuse must pass pixel density, perspective, scale, anchor, palette/value, light direction, material, outline, wear, semantic state, z-order and animation-cadence compatibility.

### 8.4 Text-art rules

World text may be baked into art only when it is truly environmental and legible at native scale: route numbers, arrows, symbols, plates, warning marks, large signs.

Narrative, dialogue, item names, stats, quest descriptions, character details and tooltips remain UI text.

Do not fill scenes with fake micro-text/glyph noise.

### 8.5 Overlay rules

Use an overlay when architecture stays the same and only a bounded state changes, such as:

- emergency lighting;
- blackout/shadow;
- damage;
- power state;
- weather;
- Trace/ability response;
- temporary status/FX.

Create a new base scene when geometry, perspective, major prop placement or the functional identity of the space changes.

## 9. Pixel-art current stage snapshot

Exact per-ID authority remains `docs/assets/GATE_TWELVE_ASSET_STATUS_AND_PRODUCTION_MATRIX.md` and `ASSET_PROVENANCE_REGISTRY.md`.

### 9.1 Existing/integrated or code-present foundations

Confirmed current families include:

- player 32x48 base/front infrastructure;
- starting equipment icons/layers including Depot Jacket, Work Gloves, Signal Ring and Courier Neck Tag;
- maintenance-seal/dead-relay state art;
- nine named Gate Twelve location scene families;
- state overlays for Gate Twelve/Service Tunnel/Trace and other authored scene states;
- environment modules for depot/archive/maintenance infrastructure;
- structural/prop families for workbench, gate, tunnel pipes/cables, archive/workshop/notice-board elements;
- navigation/resource/quest/map-marker UI families;
- Trace/pulse/directional effect families;
- Kotlin source-native catalogs plus PNG runtime delivery for current raster families;
- Tamsin opening room-actor implementation at partial identity scope;
- supporting injured courier actor pose at partial scope.

These are not all canon-approved. Many remain provisional, code-present or QA-pending.

### 9.2 Open refinements with exact implementation evidence

- Service Tunnel scene refinement exists on PR #27.
- Quiet Stair refinement exists on PR #30; exact head `7adacd474ae22908bba2fc72247f500312ea7483` has green Android Pixel Client run #282.
- Service Tunnel ambient fan/panel/drip animation exists on PR #31; exact head `19807863e3d68cd3ffad0e627ad19130da9bdbed` has green run #285.

These remain refinement evidence until branch reconciliation chooses/preserves them.

### 9.3 Explicitly rejected/superseded direction

PR #32's procedural reconstruction of the final visible Gate Twelve map surface is **REJECTED as final visible art**.

Preserve useful topology/state logic if compatible, but the desired final visible map is the actual approved/authored map master/raster when available.

### 9.4 High-priority visual creation still required

Character:
- Jack six-view identity turnaround;
- Jack left/right/back gameplay masters;
- Jack neutral portrait and emotion/context portrait family;
- Jack required idle/walk/run/crouch/interact/hurt/ability animation sheets only where gameplay consumes them;
- final face/skin/hair source layers;
- visible status overlays;
- held-item anchors;
- Tamsin full turnaround/provenance reconciliation;
- Tamsin portrait/emotion family;
- Tamsin diagnostic/task poses;
- named supporting actor identity families as content requires.

Gate Twelve state/location gaps:
- Platform Nine evacuated state;
- Municipal Archive terminal close-up;
- Workshop Row rumor/event state;
- Trace Strain/status FX;
- final Gate Twelve authored map master/raster;
- final reusable emergency/shadow overlay reconciliation;
- final area actor safe zones/panel anchors;
- final material/native-scale QA for all nine named locations.

Application art:
- final item quality/slot frames;
- final coherent navigation/status/quest icon families;
- final map transition/loading art;
- final panel frames/portrait containers;
- accessibility-safe state distinctions that do not rely on color alone.

World-scale production comes later:
- settlement kits;
- political/faction visual identity kits;
- biome/resource/beast-zone kits;
- NPC population body/wardrobe families;
- beast bodies/animations;
- tactical terrain/cover/effect kits;
- profession/class/rank visual layers only after those systems are defined.

## 10. Area packet contract

Every playable area should eventually own an area packet containing:

- place/location stable IDs;
- parent place and coordinates;
- gameplay function;
- geometry/perspective;
- material/palette/light rules;
- base environment;
- structures;
- reusable props;
- unique landmarks;
- state overlays;
- actor slots/safe zones;
- interaction anchors;
- portrait/panel behavior;
- text/signage;
- ambient FX/animation;
- map representation;
- routes;
- loading/section boundary;
- asset provenance;
- QA screenshots;
- tests/evidence.

This prevents art from being generated without knowing how the area functions.

## 11. Character-in-room and contextual panel contract

Target flow:

`authoritative scene/world state -> player-safe actor projection -> room actor -> optional focus panel -> authored dialogue/actions`

Required actor projection fields should be designed explicitly and may include:

- actor stable ID;
- presentation identity/asset ID;
- current visible pose/state;
- current location/slot;
- visible equipment/held prop IDs;
- portrait variant;
- display name;
- player-visible relationship/status summary only when intentionally exposed;
- allowed interaction/action IDs.

Rules:

- Compose must not infer presence from hidden quest flags;
- a character not projected as present does not appear merely because a background image contains them;
- recurring identity uses one approved identity master across room sprite, portraits and panels;
- emotion/pose/state variants do not create a new identity;
- multiple present actors must use deterministic scene slots/occlusion rules;
- panel focus changes presentation only, not authoritative NPC state;
- panels may be absent when no focused actor is needed.

The current scene/location actor binding is transitional and should be replaced/extended by this projected actor model when the consumer audit is ready.

## 12. Gate Twelve proof-region production list

### Platform Nine
Preserve/extend:
- blackout/current scene family;
- depot/track/platform structural kit;
- signage and depot door;
- Tamsin/courier actor slots.

Create/reconcile:
- evacuated scene/state;
- crowd/evacuation actor strategy;
- emergency/shadow overlays;
- final material pass;
- future external entrance transition only after parent city exists.

### Relay Workbench
Preserve/extend:
- base and relay-open scene;
- relay object states;
- workbench prop.

Create/reconcile:
- diagnostic reader;
- Tamsin diagnostic pose;
- task-light/tool micro-props;
- relay ID naming/provenance reconciliation;
- actor/prop occlusion anchors.

### Gate Twelve
Preserve/extend:
- sealed scene;
- Echo-active overlay/state;
- gate-door prop;
- Trace FX.

Create/reconcile:
- final gate silhouette/material review;
- future open/powered-off variants only if engine state exists;
- actor safe zones;
- phone-scale overlay QA.

### Quiet Stair
Preserve/extend:
- stair/landing/rail/signage family;
- infrastructure atlas.

Create/reconcile:
- decide whether PR #30 refinement becomes canonical;
- future egress/continuation only after destination exists;
- actor/event slots only when content requires them.

### Service Tunnel
Preserve/extend:
- base and aftershock scenes;
- maintenance corridor kit;
- pipe/cable/atlas families;
- opening actor slots.

Create/reconcile:
- choose canonical combination of PR #27, #28 and #31;
- reduced-motion ambient-animation behavior;
- deeper-expansion visual stub;
- final native-scale review;
- actor/panel safe zones.

### Trace Chamber
Preserve/extend:
- idle/training scenes;
- apparatus;
- Trace FX.

Create/reconcile:
- Trace Strain visual;
- training actor poses;
- diagnostics/measurement props;
- controlled-room material pass;
- ensure FX cannot reveal hidden routes.

### Depot Plaza
Preserve/extend:
- open/blackout scene families;
- depot exterior;
- notice board;
- district material kit.

Create/reconcile:
- paving/curb/road module pass;
- lamps/vegetation/furniture;
- public actor slots;
- future parent-city entrance anchor only after parent geography is authored.

### Municipal Archive
Preserve/extend:
- default scene;
- exterior;
- shelf/terminal props.

Create/reconcile:
- terminal close-up;
- institutional facade/courtyard refinements;
- clerk/visitor actor slots after NPC population data;
- records/research indicators driven by projected state.

### Workshop Row
Preserve/extend:
- default scene;
- workshop bench;
- ambient decals.

Create/reconcile:
- rumor/event state;
- shutter/bay/awning/tool-cart/scrap-bin families;
- worker actor family after NPC population data;
- practical signage.

## 13. World: decisions already made

The repository has decided the following at schema/architecture level:

- world hierarchy exists as world -> macroregion -> political entity -> settlement/wilderness -> district/zone -> location -> room/encounter;
- multiple coordinate spaces are required and may not silently substitute for one another;
- Gate Twelve is the first proof district;
- stable IDs and explicit parent/route records are required;
- political entities, settlements, ecosystems/resources, beast zones, population/hierarchy, world balance, loot provenance and NPC population each have documented schemas;
- world navigation ultimately supports hierarchical travel;
- danger/threat should not default to magical player-level scaling;
- loot/resources should have provenance;
- beast placement should follow ecology or an authored anomaly;
- social hierarchy/discrimination is multidimensional, not one universal "racism" stat;
- existing seven attributes remain implementation reality until explicitly migrated;
- final world data must be original and not copied from unrelated game projects.

## 14. World: still undecided and must not be invented as fact

Not yet canonically decided in the current repository:

- final world name/overall macro geography where not already explicitly authored elsewhere in this repository;
- Gate Twelve's parent macroregion/city;
- named kingdoms/nations/city-states;
- capitals and borders;
- cultures and institutions;
- concrete citizen population distributions;
- concrete prejudice/discrimination patterns by region/institution;
- concrete economic/resource flows;
- biome/climate map;
- beast taxonomy and world distribution;
- world travel network;
- concrete threat/level bands;
- concrete profession/class/rank catalog;
- concrete NPC populations outside currently authored content;
- final loot/resource tables;
- final world coordinates.

These become canon only through the appropriate world/domain document and stable record.

## 15. World-development record sequence

Before mass population:

1. choose/record world-parent and Gate Twelve parent geography;
2. create first macroregion;
3. create first political entity only if Gate Twelve belongs to one;
4. create parent settlement/city;
5. anchor Gate Twelve within that settlement;
6. create routes and neighboring districts;
7. define climate/terrain/ecology;
8. define resources/economy dependencies;
9. define beast zones/threats;
10. define population/hierarchy/institutions;
11. create NPC population;
12. create loot/item provenance;
13. create world-balance bands;
14. create visual area packets;
15. validate travel and loading coordinates.

Do not create thousands of disconnected names before the first parent chain is coherent.

## 16. Mechanics rebuild decisions

### KEEP / EXTEND
- deterministic scene/choice engine;
- quests and branching foundations;
- knowledge;
- NPC memory/relationships/goals;
- equipment/inventory authority;
- effective stat/modifier foundation;
- time/training/recovery foundation;
- powers/techniques foundation;
- save/load and validation;
- player-safe projections.

### REWORK / MIGRATE
- final progression taxonomy;
- skill hierarchy;
- ability/passive/technique/class-feature taxonomy;
- classes/professions/ranks;
- citizen/social rank integration;
- world-balance formulas;
- item/economy/loot depth;
- richer NPC schedules/factions;
- map/world hierarchy integration;
- actor-presence/panel projection;
- final Android screen hierarchy.

### NEW
- original tactical positional combat;
- original persistent adversary network;
- world-scale registries/population;
- multidimensional institutional/cultural prejudice system at concrete world level;
- large-scale profession/activity framework;
- final world danger/threat bands;
- tactical terrain/cover encounter content.

### REPLACE
- generic/provisional player visual identity with Jack production identity;
- weak technical/geometric visible art where production authored art supersedes it;
- transitional scene-name actor inference with explicit player-safe actor projection when implemented;
- any final-map procedural substitute where an approved authored map master exists.

### REMOVE AFTER MIGRATION
Potential later removals:
- obsolete geometric placeholder renderers;
- duplicate asset paths;
- stale generic-player visual files;
- superseded UI components;
- prototype-only debug presentation;
- duplicate hardcoded presentation state.

Nothing in this category is deleted until consumer audit + replacement + migration + tests + rollback evidence exist.

## 17. Tactical combat direction

Target: original turn-based positional/squad tactics.

Document and prototype:

- initiative/turn sequence;
- action budget;
- movement/terrain cost;
- cover/stance;
- line of sight;
- range;
- accuracy/defense;
- reactions;
- abilities/items;
- conditions/injury;
- nonlethal/capture/retreat outcomes;
- terrain interaction where approved;
- AI roles;
- encounter rewards/consequences;
- persistence back into world/NPC state.

Use broad genre concepts only. Names, formulas, UI, classes, enemies, maps and presentation must be original.

## 18. Persistent adversary direction

Target: original persistent adversary network built on stable NPC identity and existing memory/social foundations.

Possible documented state:

- encounter history;
- wins/losses;
- injuries/recovery;
- perceived player traits;
- grudges/fear/respect;
- goals;
- promotion/demotion;
- faction relationships;
- allies/rivals;
- movement/schedule;
- capture/death/retirement;
- succession/replacement;
- generated world hooks from original rules.

Do not reproduce a branded hierarchy UI, proprietary names, distinctive dialogue structure or another game's exact system expression.

## 19. Final APK demolition/rebuild model

The existing Android client is a migration source and foundation, not disposable code and not automatically the final product.

For every Android subsystem, create a row with:

- source files/components;
- current consumers;
- projected fields/actions consumed;
- asset dependencies;
- current tests;
- target contract;
- decision: KEEP / EXTEND / REWORK / REPLACE / REMOVE;
- migration sequence;
- rollback path;
- verification evidence.

Final rebuild sequence:

1. freeze approved domain-document versions for the slice;
2. reconcile canonical implementation heads;
3. complete save/content/stable-ID migration plan;
4. complete player-safe projection contracts;
5. freeze first-region visual packets;
6. rebuild/harden navigation shell;
7. rebuild Story/room actor/panel composition;
8. rebuild Character/Stats/Skills;
9. rebuild Equipment/Bag;
10. rebuild Quests/relationships/world information;
11. rebuild hierarchical Map;
12. finish settings/accessibility/narration;
13. integrate tactical combat surface;
14. integrate adversary/world surfaces;
15. finish developer/debug surface;
16. prove zero consumers for deprecated components;
17. remove/archive superseded presentation code;
18. performance/memory pass;
19. complete regression + screenshot + emulator evidence;
20. physical Galaxy A03 installation/startup/play/visual QA as separate gate;
21. produce final APK provenance and handoff.

## 20. Documentation ownership map

| Need | Owning document |
| --- | --- |
| repository priority, permission, overall program | `MASTER_GAME_DEVELOPMENT_PROGRAM.md` |
| ordered phases | `MASTER_DIRECTIVE_EXECUTION_BREAKDOWN.md` |
| requirement traceability | `OWNER_DIRECTIVE_TRACEABILITY_MATRIX_2026-10-02.md` |
| operational tasks | `THE_GAME_MASTER_TASK_REGISTER.md` |
| doc ownership/dependencies | `DOCUMENTATION_CROSS_REFERENCE_MATRIX.md` |
| current live implementation evidence | `LIVE_REPOSITORY_STATE_AUDIT_2026-10-02.md` + exact-head CI |
| keep/rework/replace/remove decisions | `EXISTING_STATE_REWORK_DECISION_MATRIX.md` |
| pixel composition | `assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md` |
| asset stages/reuse | `assets/PIXEL_ART_PRODUCTION_AND_REUSE_LEDGER.md` |
| exact Gate Twelve asset status | `assets/GATE_TWELVE_ASSET_STATUS_AND_PRODUCTION_MATRIX.md` |
| asset source/branch provenance | `assets/ASSET_PROVENANCE_REGISTRY.md` |
| room actors/panels/overlays | `assets/ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md` |
| Gate Twelve region | `assets/GATE_TWELVE_REGION_MASTER_PLAN.md` |
| world hierarchy | `world/WORLD_DEVELOPMENT_MASTER_INDEX.md` |
| coordinates | `world/WORLD_COORDINATE_AND_SCALE_STANDARD.md` |
| politics | `world/WORLD_POLITICAL_ENTITIES.md` |
| settlements | `world/WORLD_SETTLEMENT_CATALOG.md` |
| routes | `world/WORLD_TRAVEL_AND_ROUTES.md` |
| ecology/resources | `world/WORLD_ECOSYSTEM_AND_RESOURCES.md` |
| beast zones | `world/WORLD_BEAST_ZONE_STANDARD.md` |
| population/hierarchy | `world/WORLD_POPULATION_AND_CITIZEN_HIERARCHY.md` |
| world balance | `world/WORLD_BALANCE_AND_LEVEL_BANDS.md` |
| loot provenance | `world/WORLD_LOOT_PROVENANCE_STANDARD.md` |
| NPC population | `world/WORLD_NPC_POPULATION_STANDARD.md` |
| progression/classes/ranks | `systems/PROGRESSION_MASTER_PLAN.md` |
| activities/life loop | `systems/PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md` |
| NPC/social/adversary | `systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md` |
| tactical combat | `systems/TACTICAL_COMBAT_MASTER_PLAN.md` |
| items/economy/loot | `systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md` |
| gameplay rebuild summary | `systems/GAMEPLAY_SYSTEM_REBUILD_MATRIX.md` |
| migration | `systems/SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md` |
| final app UX | `android/APPLICATION_UX_MASTER_PLAN.md` |
| Android consumers/projections | `android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md` |
| final APK rebuild | `android/APK_FINAL_RECONSTRUCTION_MATRIX.md` + `APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md` |

## 21. Immediate P0 execution packet

The next work must be evidence-producing, not broad invention:

### P0-A — Branch reconciliation
Create one matrix for PRs #7–#31:
- branch/head;
- parent/base;
- subsystem;
- files changed;
- exact-head CI;
- supersedes/conflicts with;
- preserve/migrate/reject decision;
- target canonical branch.

### P0-B — Asset provenance exactization
For every current raster/source-native asset:
- ID;
- source file/master;
- branch/head;
- export/raster;
- consuming catalog/component;
- reuse signature;
- QA evidence;
- current stage;
- canonical candidate.

### P0-C — Android consumer audit
Complete:
`screen/composable -> ViewModel -> GameEngine action/field -> Python owner -> asset packet -> test`.

### P0-D — Actor projection contract
Design the player-safe actor list and migrate room-actor/panel consumers without leaking hidden state.

### P0-E — First world-parent decision packet
Author only the minimum canon needed to place Gate Twelve correctly:
- parent settlement;
- parent region;
- political ownership if applicable;
- coordinate anchors;
- major routes;
- climate/terrain/material context.

### P0-F — Mechanics migration dependencies
Convert final progression/class/rank/activities/social/items/combat/adversary docs into explicit schema/API/save migration tasks.

### P0-G — Final APK teardown manifest
Do not delete anything yet. Build a complete consumer graph and candidate removal list with replacement prerequisites.

## 22. Verification standard

Documentation work is complete only when:
- linked from authority/indexes;
- no competing authority is introduced;
- status and owner are explicit;
- unresolved decisions are labeled;
- implementation claims cite exact source/HEAD/evidence;
- task register is updated.

Runtime work is complete only when the relevant exact-head tests/builds are executed and observed.

Physical handset results must remain separate from emulator evidence.

## 23. Final outcome

The final target is not merely a large documentation corpus or an APK that builds.

The target is a repository where:

- the game can be reconstructed from durable documentation;
- world data is structured and internally connected;
- visual assets have provenance and coherent reuse rules;
- characters appear consistently across rooms, portraits and panels;
- mechanics have one authoritative owner;
- save/stable-ID migrations are explicit;
- tactical combat and persistent adversaries are original;
- Android is a safe presentation/application layer;
- obsolete code is removed only after evidence proves it is no longer needed;
- a final APK can be traced to exact source, data, assets, tests and device QA.


## 24. 2026-10-02 execution and evidence children

The following child documents were added on the same program branch and are part of the current documentation graph:

- `docs/DECISION_AND_REBUILD_EXECUTION_REGISTER.md` — decomposes the owner directive into concrete deliverables, can/will/candidate decisions, migration gates and reconstruction acceptance.
- `docs/DOCUMENTATION_CATALOG_2026-10-02.md` — exact baseline Markdown catalog with headings, word counts, hashes and literal references for its recorded baseline.
- `docs/assets/ROOM_COMPOSITION_IMPLEMENTATION_CONTRACT.md` — operational room actor/panel/overlay/raster-precedence contract; does not imply the proposed actor projection already exists.
- `docs/world/WORLD_CANON_DECISION_QUEUE.md` — separates exact Gate Twelve map facts from unresolved parent-world/geography/politics/ecology/progression decisions.
- `docs/assets/RASTER_DELIVERY_EVIDENCE_2026-10-02.md` — baseline PNG dimensions, hashes and catalog bindings.
- `docs/evidence/documentation_catalog_2026-10-02.json` — machine-readable documentation evidence.
- `docs/evidence/gate_twelve_map_baseline_2026-10-02.json` — machine-readable Gate Twelve map baseline evidence.
- `docs/evidence/raster_bindings_2026-10-02.json` — machine-readable raster binding evidence.

These evidence children supplement this blueprint. They do not override newer exact-head source/CI evidence and must not be interpreted as proof that future mechanics, world canon or art approval is complete.
