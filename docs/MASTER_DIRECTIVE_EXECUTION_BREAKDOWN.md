# THE GAME — Master Directive Execution Breakdown

Status: **ACTIVE / PRIMARY EXECUTION MAP**  
Repository: `jbob-coder/Text-rpg-game`  
Program branch: `docs/master-game-development-program`  
Parent authority: `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`  
Priority: **P0 — documentation first**

## 1. Purpose

This document converts the owner's large development directive into an ordered, auditable execution program. It is not a substitute for the domain master documents. It defines what must exist, in what order, what may change, what requires migration, and what must be verified before broad implementation.

The target is a game that can be reconstructed from repository documentation without depending on chat memory.

## 2. Priority declaration

For current game work, `jbob-coder/Text-rpg-game` is the highest-priority game repository.

Other game repositories, old prototypes, historical reports, and external references may be consulted only as:
- historical evidence;
- reusable abstract design lessons;
- explicitly migrated assets/systems;
- comparison material.

They do not override the current repository.

`main` remains a placeholder unless a later explicit promotion decision changes that.

## 3. Full-permission interpretation

Broad permission is granted to create, redesign, replace, remove, migrate, and rebuild game-development material when doing so improves the documented target game.

That permission includes:
- documentation;
- worldbuilding;
- pixel art;
- Android presentation;
- gameplay systems;
- content;
- tests;
- tooling;
- data schemas;
- migration code;
- replacement UI;
- new original mechanics.

It does not override standing prohibitions:
- no silent merge/promotion to `main`;
- no force-push/shared-history rewrite without explicit repository decision;
- no hidden/raw state read by player UI;
- no silent stable-ID or save-schema break;
- no unrelated-repository asset treated as native authority;
- no claim of physical-device QA from emulator evidence;
- no copying protected art, names, maps, characters, dialogue, or distinctive proprietary presentation from another game;
- no Code Assistant workflow previously prohibited by the owner.

## 4. Numeric documentation targets

The owner supplied long-range numeric targets including:
- 3,000 documentation;
- 2,000 guide/planning;
- 10,000 map-development scope;
- 10,000 final APK/development scope;
- 2,000,000 total documentation.

The units are not fully defined. Therefore the repository must track separately:
- document files;
- words;
- structured records;
- guide entries;
- map/place records;
- asset records;
- implementation tasks;
- tests/evidence records.

Do not claim a target is complete by silently choosing a convenient unit.

## 5. Program phases

### Phase 0 — Authority and continuity
Deliver:
- priority repository declaration;
- source-of-truth order;
- permissions/prohibitions;
- branch/evidence policy;
- continuity logs;
- cross-reference matrix.

Current state: **established**.

### Phase 1 — Existing-state audit
Deliver:
- complete subsystem inventory;
- exact branch/HEAD references where relevant;
- KEEP / EXTEND / REWORK / REPLACE / REMOVE / UNKNOWN classification;
- technical debt;
- duplicated systems;
- stale docs;
- migrations required.

Output:
`docs/EXISTING_STATE_REWORK_DECISION_MATRIX.md`

Current state: **started by this program; deeper code audit still required**.

### Phase 2 — Visual production authority
Deliver:
- pixel-art composition stack;
- character identity/rig rules;
- room-actor rules;
- character portrait/panel rules;
- environment/map asset rules;
- overlay/FX reuse rules;
- asset-stage ledger;
- per-area production packets;
- animation boundaries;
- QA gates.

Outputs include:
- `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`
- `docs/assets/PIXEL_ART_PRODUCTION_AND_REUSE_LEDGER.md`
- `docs/assets/CHARACTER_PIXEL_BLUEPRINTS.md`
- Gate Twelve asset/animation plans.

### Phase 3 — Gate Twelve proof region
Gate Twelve is the first region used to prove:
- geometry;
- materials;
- asset decomposition;
- room actors;
- map rendering;
- overlays;
- application UX;
- state binding;
- section/loading rules;
- verification;
- migration.

Current region master:
`docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md`

Current state: Steps 1–14 complete as a first-pass proof-region contract; runtime implementation remains separate.

### Phase 4 — World-scale schema
Before mass world creation, define:
- coordinate hierarchy;
- political geography;
- settlements;
- districts;
- interiors;
- routes;
- resources;
- ecosystems;
- beast zones;
- population;
- NPC distribution;
- loot/resource provenance;
- world-level bands.

Outputs:
- `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`
- `docs/world/WORLD_SCALE_DOCUMENTATION_BLUEPRINT.md`
- future child catalogs.

### Phase 5 — Progression and identity systems
Define:
- attributes;
- derived stats;
- skills;
- abilities;
- passives;
- techniques;
- classes;
- professions;
- ranks;
- mastery;
- training;
- level/band rules;
- citizen social rank;
- equipment progression.

No stat/save migration until this contract is approved.

### Phase 6 — Society / NPC / hierarchy simulation
Define:
- NPC memory;
- goals;
- schedules;
- relationships;
- factions;
- social hierarchy;
- wealth/status;
- institutional access;
- prejudice/discrimination systems;
- rumor/reputation propagation;
- rival evolution.

Sensitive fictional discrimination mechanics must be modeled as world systems with causes, consequences, and agency rather than as a simplistic “race stat.”

### Phase 7 — Items / resources / ecosystem / economy
Define:
- items;
- equipment;
- accessories;
- materials;
- quality;
- loot;
- beast drops;
- harvesting;
- resource scarcity;
- crafting/repair only if approved;
- vendor/economy systems only if approved;
- provenance.

### Phase 8 — Tactical combat
Create an original turn-based squad/position tactics system using broad genre ideas:
- action economy;
- cover;
- line of sight;
- movement;
- range;
- terrain;
- body/condition state;
- skills/abilities;
- AI;
- encounter persistence;
- rewards/consequences.

Do not copy protected XCOM terminology, maps, UI, units, fiction, or exact proprietary mechanics.

### Phase 9 — Dynamic rival / adversary simulation
Create an original persistent adversary system using broad genre ideas:
- persistent NPC identity;
- encounter memory;
- injuries/scars where authored;
- promotions/demotions;
- grudges/fears/respect;
- faction consequences;
- procedural titles only from original vocabularies;
- relationships among adversaries;
- replacement/succession;
- world-state persistence.

Do not reproduce the branded Nemesis System's names, UI, character archetypes, dialogue patterns, hierarchy presentation, or proprietary implementation.

### Phase 10 — Application UX master
Define final player experience:
- Story;
- character;
- room actors;
- portrait/dialogue panels;
- Stats;
- Equipment;
- Inventory/Bag;
- Skills;
- Quests;
- Map;
- Saves;
- Settings;
- accessibility;
- narration/audio;
- developer tools;
- phone responsiveness.

### Phase 11 — State/data migration planning
Before destructive rebuilds:
- stable-ID map;
- save schema map;
- content migration;
- projection migration;
- visual-ID migration;
- deprecated-field policy;
- compatibility tests;
- rollback.

### Phase 12 — Final Android/APK reconstruction
Use final documentation to classify every application subsystem as:
- KEEP;
- EXTEND;
- REWORK;
- REPLACE;
- REMOVE.

Then rebuild in dependency order while preserving authoritative engine ownership.

### Phase 13 — Verification and physical-device acceptance
Required evidence:
- Python tests;
- Android unit tests;
- instrumentation compile;
- APK assembly/package checks;
- emulator smoke;
- phone-sized screenshots;
- physical Galaxy A03 testing as a separate gate;
- save/load migration tests;
- performance/memory checks.

### Phase 14 — Promotion / release authority
Only after evidence:
- resolve stacked branches;
- document chosen canonical heads;
- merge/promote deliberately;
- archive superseded documents without deleting evidence;
- produce final APK provenance.

## 6. Documentation-first stop rules

Do not mass-generate:
- kingdoms;
- cities;
- villages;
- classes;
- beasts;
- NPC populations;
- loot tables;
- tactical encounters;
- final APK screens

until the corresponding schema/contract exists.

Do not create art for a region merely because a blank area exists. First verify:
- location identity;
- geometry;
- material family;
- state ownership;
- required actors;
- reusable assets;
- app surface consuming the asset.

## 7. Current immediate order

1. deepen the exact existing-state rework audit against live implementation heads;
2. create reproducible documentation/world/asset inventory counts;
3. reconcile Gate Twelve visual/runtime refinement branches and asset provenance;
4. begin bounded Gate Twelve implementation only where Steps 1–14 contracts are satisfied;
5. populate world catalogs under the established geography/political/settlement/ecosystem/beast/population standards;
6. deepen progression/social/items/combat balances as world records require;
7. maintain save/content migration matrices for every breaking domain change;
8. keep final APK reconstruction late-stage until domain contracts and migrations are mature.

## 8. Continuity handoff

A future session must start with:
1. `README.md`;
2. `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`;
3. this file;
4. `docs/DOCUMENTATION_CROSS_REFERENCE_MATRIX.md`;
5. `docs/THE_GAME_MASTER_TASK_REGISTER.md`;
6. the relevant domain master.

If repository source or exact-head evidence conflicts with a planning document, the source/evidence wins and the planning document must be corrected.

## 2026-10-02 materialized contract update

The following Phase 5–12 foundation contracts now exist:
- `docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md`;
- `docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md`;
- `docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md`;
- `docs/systems/WORLD_BALANCE_INTEGRATION_PLAN.md`;
- `docs/systems/SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md`;
- `docs/android/APPLICATION_UX_MASTER_PLAN.md`.

They turn several previously listed future outputs into real repository documents. Their unresolved decisions remain intentionally open; no runtime system is implied by document creation.


## Current continuation

See [Decision/rebuild execution register](DECISION_AND_REBUILD_EXECUTION_REGISTER.md) for operational steps and accepted versus candidate changes. The baseline catalog and raster audit now exist; branch reconciliation remains open.
