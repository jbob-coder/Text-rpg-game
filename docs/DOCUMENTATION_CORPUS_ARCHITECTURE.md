# THE GAME — Documentation Corpus Architecture

Status: **ACTIVE / P0 PROGRAM CONTRACT**  
Repository: `jbob-coder/Text-rpg-game`  
Parent authority: `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`  
Priority: documentation first

## 1. Purpose

This document defines how the long-range documentation corpus is divided, counted, cross-referenced, expanded, and eventually used to rebuild the game. The goal is not a pile of unrelated Markdown files. The goal is a reconstructable specification graph where every important design decision has a durable owner, every implementation area knows which document governs it, and every future session can resume without depending on chat memory.

The owner supplied long-range targets including “3,000 documentation”, “2,000 guide and planning”, “10,000 map development”, “10,000 final APK/development”, and “2,000,000 total documentation”. Those targets remain preserved. Their unit is not silently assumed. This corpus therefore tracks documents, words, records, decisions, asset entries, world records, implementation tasks, tests, and evidence separately until an accepted completion metric is locked.

## 2. Repository priority

For current game development, `jbob-coder/Text-rpg-game` is the priority repository.

Other game repositories, prototypes, historical reports, references, or experiments are subordinate unless a migration record explicitly imports an abstract idea, asset, system, or data set.

The default `main` branch remains a placeholder and is not made authoritative by this document.

## 3. Corpus hierarchy

The documentation graph is divided into volumes.

### Volume 00 — authority and continuity
Owns:
- repository priority;
- permissions and prohibitions;
- source-of-truth order;
- branch policy;
- evidence requirements;
- handoff rules;
- corpus metrics.

Primary files:
- `MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `MASTER_DIRECTIVE_EXECUTION_BREAKDOWN.md`
- `DOCUMENTATION_CROSS_REFERENCE_MATRIX.md`
- `DOCUMENTATION_PROGRESS_LEDGER.md`
- this document.

### Volume 01 — existing-state audit
Owns:
- exact subsystem inventory;
- KEEP / EXTEND / REWORK / REPLACE / REMOVE / UNKNOWN;
- branch/HEAD evidence;
- technical debt;
- duplicate/stale contracts;
- migration risk.

Primary file:
- `EXISTING_STATE_REWORK_DECISION_MATRIX.md`

### Volume 02 — visual/pixel production
Owns:
- source-native pixel standards;
- asset lifecycle;
- character identity;
- equipment/paper-doll;
- room actors;
- portraits/focus panels;
- environment/map art;
- props;
- text/signage;
- overlays;
- FX;
- animation;
- reuse compatibility;
- per-area production packets.

### Volume 03 — proof region
Owns Gate Twelve:
- geometry;
- circulation;
- zone function;
- materials;
- asset decomposition;
- application UX;
- state layers;
- loading;
- migration;
- verification.

### Volume 04 — world
Owns:
- world coordinates;
- macroregions;
- political entities;
- settlements;
- districts/sites/interiors;
- routes;
- ecosystems;
- resources;
- beast zones;
- population;
- world balance;
- place provenance.

### Volume 05 — characters/social
Owns:
- NPC identity;
- memory;
- goals;
- schedules;
- relationships;
- factions;
- social hierarchy;
- prejudice/discrimination;
- reputation;
- persistent rivals/adversaries.

### Volume 06 — progression
Owns:
- stats;
- derived stats;
- skills;
- abilities;
- techniques;
- passives;
- classes;
- professions;
- ranks;
- mastery;
- training;
- progression/balance.

### Volume 07 — items/economy/loot
Owns:
- item taxonomy;
- equipment;
- accessories;
- materials;
- quality;
- legality;
- loot;
- beast drops;
- provenance;
- economy;
- repair/crafting only if approved.

### Volume 08 — tactical combat
Owns the original turn-based tactical system:
- turn/action model;
- movement;
- cover;
- LOS;
- range;
- terrain;
- targeting;
- abilities;
- AI;
- injuries/status;
- retreat/surrender;
- aftermath.

Broad genre inspiration may be used, but protected XCOM terminology, presentation, fiction, maps, classes, enemy designs, and proprietary structure are excluded.

### Volume 09 — persistent adversaries/world memory
Owns the original persistent adversary model:
- stable identity;
- memory;
- injuries;
- promotion/demotion;
- rivalries;
- grudges/fear/respect;
- faction movement;
- succession;
- world consequences.

It must not copy branded Nemesis System hierarchy screens, names, dialogue patterns, archetypes, or proprietary presentation.

### Volume 10 — activities/life simulation
Owns:
- work;
- study;
- training;
- research;
- rest;
- travel;
- social actions;
- medical recovery;
- faction duties;
- exploration;
- approved economy/crafting activities.

### Volume 11 — application UX
Owns:
- Story;
- character;
- panels;
- Stats;
- Skills;
- Equipment;
- Bag/Inventory;
- Quests;
- Map;
- Saves;
- Settings;
- accessibility;
- narration;
- developer tools;
- tactical/combat surfaces.

### Volume 12 — Android/APK reconstruction
Owns:
- current APK decomposition;
- keep/rework/replace/remove decisions;
- bridge;
- navigation shell;
- migrations;
- component retirement;
- exact-head QA;
- physical device acceptance;
- release provenance.

## 4. Documentation unit types

Every durable unit must be one of:

- **MASTER** — domain authority.
- **STANDARD** — reusable rule/contract.
- **CATALOG** — stable records for many entities.
- **PACKET** — one area/character/system implementation bundle.
- **MATRIX** — cross-system decision/state comparison.
- **LEDGER** — changing production/progress status.
- **GUIDE** — execution procedure.
- **AUDIT** — observed evidence about current implementation.
- **HANDOFF** — bounded continuity snapshot.
- **EVIDENCE** — test/build/runtime/visual proof.

A file may contain more than one unit only when their lifecycle is tightly coupled.

## 5. Required metadata

New major documents should state:
- status;
- repository;
- parent authority;
- child/consumer links;
- what the document owns;
- what it must not own;
- current implementation state;
- unresolved decisions;
- next required document or implementation;
- last meaningful update date.

World/catalog records additionally require stable IDs and coordinate/parent references.

## 6. Cross-reference rule

No major document may become an isolated island.

Every major document must point upward to its parent authority and downward to:
- child documents;
- affected runtime systems;
- affected assets;
- migration needs;
- verification needs.

The cross-reference matrix is the top-level map of that graph.

## 7. Branch architecture

Use small branch families rather than one irreversible mega-branch.

Current program authority:
- `docs/master-game-development-program`

Recommended future child branch families:
- `docs/world-*`
- `docs/systems-*`
- `docs/assets-*`
- `docs/android-*`
- `docs/guide-*`
- `audit/*`

Implementation branches remain separate from documentation authority until the relevant contract exists.

Do not create a second competing master authority. Child branches should identify their parent program branch and reconcile back through review.

## 8. Record-scale strategy

Large world scope must be catalog-driven.

Do not create one 100,000-line prose file containing every city, NPC, route, beast, and item.

Use:
- master standards;
- region catalogs;
- settlement catalogs;
- route catalogs;
- ecosystem/resource catalogs;
- NPC registries;
- item registries;
- asset manifests;
- generated indexes that point to human-authored records.

This permits thousands of records without destroying maintainability.

## 9. “2,000,000” target tracking

Until the unit is confirmed, the progress ledger must separately report:
- Markdown files;
- words;
- structured records;
- world/place records;
- routes;
- asset records;
- character/NPC records;
- item/loot records;
- beast/ecosystem/resource records;
- system rules;
- guides;
- decisions;
- tests;
- evidence artifacts.

Recommended eventual acceptance method:
1. choose the owner-approved primary metric;
2. preserve the secondary metrics;
3. generate a reproducible inventory;
4. exclude duplicates/archives from “active corpus” totals;
5. report active, historical, and generated documentation separately.

## 10. Documentation-before-destruction rule

Broad development permission includes deliberate replacement of weak systems.

Before a subsystem is broken or removed:
1. audit current behavior;
2. classify it;
3. write replacement contract;
4. write migration/compatibility plan;
5. define tests;
6. implement on a working branch;
7. verify exact HEAD;
8. migrate consumers;
9. only then retire old code/assets.

Persistent save/state identifiers require stricter migration than presentation components.

## 11. World documentation production order

1. geography/coordinate standard;
2. political entity standard/catalog;
3. settlement catalog;
4. route/travel catalog;
5. ecosystem/resource catalog;
6. beast-zone standard/catalog;
7. population/hierarchy catalog;
8. balance bands;
9. loot provenance;
10. region-specific production packets;
11. tactical encounter-space packets.

Gate Twelve remains the proof region before mass expansion.

## 12. Visual documentation production order

1. identity/reference authority;
2. source-native pixel master;
3. rig/anchor/pivot;
4. per-area environment packet;
5. room actors;
6. props;
7. overlays/state variants;
8. FX/animation;
9. portrait/focus panel;
10. UI integration;
11. screenshot QA;
12. runtime provenance.

## 13. Application documentation production order

1. authoritative projection contract;
2. navigation shell;
3. Story;
4. Character;
5. Stats/Skills;
6. Equipment/Bag;
7. Quests;
8. Map;
9. Saves;
10. Settings/accessibility/narration;
11. tactical combat;
12. adversary/world surfaces;
13. developer tools;
14. migration/removal;
15. final device/release evidence.

## 14. Completion gate

The corpus is not “complete” merely because a target count is large.

Final completion requires:
- accepted metric;
- no unresolved top-level authority conflicts;
- all active domain masters linked;
- world and system catalogs validated;
- implementation mapped to documentation;
- migrations recorded;
- tests/evidence linked;
- final APK reconstructed against the corpus;
- explicit known-gap register.

## 15. Immediate next actions

1. keep Gate Twelve documentation moving through Step 8–14;
2. complete the exact existing-state audit;
3. populate world child standards/catalogs;
4. expand progression/social/items/combat masters into executable child contracts;
5. add reproducible corpus inventory tooling;
6. only then scale content production aggressively.
