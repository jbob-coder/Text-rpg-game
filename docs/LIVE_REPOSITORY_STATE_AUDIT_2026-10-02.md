# THE GAME — Live Repository State Audit — 2026-10-02

Status: **ACTIVE / EXACT SNAPSHOT CONTROL**  
Repository: `jbob-coder/Text-rpg-game`  
Documentation authority branch: `docs/master-game-development-program`  
Audited program HEAD before this audit: `f9981cdcd4d82c8eced330a2da081e60ee2ed510`  
Parent program PR: **#33 — Establish master game development and documentation program**

## 1. Purpose

This audit is the first repository-native answer to the owner's requirement that documentation state exactly what exists, what is provisional, what can change, what is planned to change, and what must be reconciled before broad rebuilding.

It is a **repository-state audit**, not a claim that every implementation branch is already unified.

Fresh source/CI evidence always outranks this snapshot after the recorded HEAD moves.

## 2. Priority and authority

Current priority game repository:

`jbob-coder/Text-rpg-game`

Current top-level documentation authority:

`docs/master-game-development-program`

Current source-of-truth order:

1. exact repository files on the branch/HEAD being changed;
2. fresh tests/build/runtime evidence for that exact HEAD;
3. `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`;
4. `docs/MASTER_DIRECTIVE_EXECUTION_BREAKDOWN.md`;
5. domain master documents;
6. `docs/THE_GAME_MASTER_TASK_REGISTER.md`;
7. historical implementation reports/handoffs;
8. chat memory.

`main` remains a placeholder and is not silently promoted by this program.

## 3. Program-branch snapshot

At audited HEAD `f9981cd...` the recursive Git tree contained:

- 231 tracked files;
- 2,621,807 bytes of tracked blob content;
- 90 tracked files under `docs/`;
- 69 Markdown files repository-wide;
- 67 Markdown files under `docs/`;
- 24 PNG raster assets;
- 39 Python files;
- 65 Kotlin files;
- 18 JSON files;
- 50 Python/Kotlin source files whose path contains `test`;
- 12 world-document Markdown files;
- 8 systems-document Markdown files;
- 22 asset-document Markdown files;
- 3 Android-document Markdown files;
- 3 Game Context Log Markdown files.

These are structural counts only. They do not define the owner's numeric documentation units.

## 4. Documentation program state

Draft PR #33 was observed as:

- head: `docs/master-game-development-program`;
- base: `docs/settlement-region-build-plan`;
- 93 commits ahead of its base at the audited snapshot;
- 46 changed files relative to that base;
- 13,995 additions / 42 deletions at the audited snapshot;
- open and draft;
- mergeable according to GitHub metadata at the time of inspection.

The program already contains top-level contracts for:

- project authority and permissions;
- documentation corpus architecture;
- cross-reference ownership;
- Gate Twelve Steps 1–14;
- pixel-art composition and reuse;
- room actors / character portraits / contextual panels;
- world hierarchy / coordinates / political entities / settlements;
- ecosystems / resources / beast zones / population;
- loot provenance;
- progression / classes / ranks;
- NPC/social/persistent-adversary direction;
- tactical combat;
- items/economy/loot;
- world balance;
- save/content migration;
- Android UX;
- final APK reconstruction.

This means the project has a **documentation architecture**, not that the game systems are implemented.

## 5. Open-PR landscape

The live PR search returned 30 open PRs.

### A. Program authority

- #33 — `docs/master-game-development-program`

This is the current documentation program. It must not be treated as proof that all stacked implementation PRs are integrated.

### B. Pixel/application implementation and refinement stack

Observed open PRs include:

- #7 — pixel asset reconciliation;
- #8 — reusable environment modules/infrastructure atlas;
- #9 — diagnostic reader production masters;
- #10 — avatar overlay rig contract;
- #11 — player-safe stat inspection;
- #12 — character equipment paper-doll UI;
- #13 — Character/Stats refinement;
- #14 — player-safe Skills;
- #15 — player-hub runtime recovery;
- #16 — pixel asset runtime expansion;
- #17 — existing secondary-button asset reuse;
- #18 — scene-first Story;
- #19 — PNG pixel-art runtime;
- #20 — Story resource HUD;
- #21 — authored pixel art beneath district Map;
- #22 — player avatar art pass;
- #23 — opening Story actor pixel art;
- #24 — mobile Bag pixel art;
- #25 — mobile Skills/Stats hierarchy;
- #26 — Service Tunnel arrival art;
- #27 — Service Tunnel scene refinement;
- #28 — Service Tunnel atlas detail;
- #29 — Gate Twelve map geometry/pixel-asset blueprint;
- #30 — Quiet Stair scene refinement;
- #31 — Service Tunnel ambient animation.

These PRs are evidence and implementation candidates. Their stacking/base relationships must be reconciled before a final implementation branch is declared.

### C. Engine/foundation PRs

Observed open PRs include:

- #1 — canonical game direction/screen contract;
- #2 — effective-stat pipeline;
- #4 — V6 runtime stabilization;
- #5 — Android open-world integration.

Historical verification remains useful, but these PRs do not override the master program.

## 6. Current implementation invariants to preserve until migration

The audit keeps these as high-risk invariants:

- gameplay state stays outside Compose;
- Android consumes player-safe projections;
- hidden/private authored state is not used to choose player-visible art;
- stable location/quest/item/NPC IDs are not silently renamed;
- save compatibility is not silently broken;
- equipment slot semantics and paper-doll anchors remain stable until migrated;
- route legality and discovery remain engine/content authority;
- nearest-neighbor/source-native pixel rendering remains the target;
- physical-device QA is never claimed from emulator evidence;
- unrelated repository assets are not native authority without explicit migration/provenance.

## 7. What may change

With the owner's standing development permission, the following may be changed on working branches when the replacement is documented and verified:

- Android screen composition;
- Story/Map/Character/Stats/Bag/Skills visual hierarchy;
- provisional geometric environment art;
- generic player appearance;
- room-actor presentation;
- contextual character panels;
- portrait families;
- map background and route styling;
- visual asset manifests/provenance;
- content schemas through explicit migration;
- progression/class/rank systems through explicit migration;
- combat implementation;
- persistent-adversary implementation;
- NPC schedules/social hierarchy;
- world registries;
- economy/loot systems;
- build/release architecture;
- obsolete presentation code after consumer audit and replacement evidence.

## 8. What is explicitly planned to change

Current documentation calls for:

- replacing the generic/provisional player look with Jack-compatible production art;
- keeping the 32x48 paper-doll contract while improving final sprite identity/equipment alignment;
- adding 64x64 portrait families and contextual actor panels;
- replacing weak geometric map/scene presentation with modular authored pixel art;
- retaining map state overlays as state overlays rather than baking them into art;
- deepening room-actor composition so present characters appear in the room from player-safe state;
- using text/signage only where it belongs in-world and keeping normal UI text separate;
- expanding the world beyond Gate Twelve through explicit hierarchy/coordinate records;
- adding original tactical combat and original persistent-adversary systems;
- reconciling progression/classes/ranks before stat/save migrations;
- performing a final APK reconstruction only after domain contracts and migrations are ready.

## 9. Pixel-art current-state audit

The audited program tree contains 24 PNG files.

Current raster families visible in the program branch include:

- Gate Twelve named-location scene rasters;
- current player front/base raster;
- current technical hair placeholder;
- starting equipment/item icons;
- paper-doll overlays for jacket, gloves, ring, neck tag;
- dead-relay state rasters;
- maintenance-seal icon.

Current Kotlin visual catalogs include:

- `PixelAssetCatalog.kt`;
- `PixelCharacterStagingCatalog.kt`;
- `PixelEnvironmentDecalCatalog.kt`;
- `PixelEnvironmentModuleCatalog.kt`;
- `PixelEnvironmentOverlayCatalog.kt`;
- `PixelEnvironmentPropCatalog.kt`;
- `PixelEquipmentSlotCatalog.kt`;
- `PixelItemQualityFrameCatalog.kt`;
- `PixelMapArtCatalog.kt`;
- `PixelMapMarkerCatalog.kt`;
- `PixelMapTravelTransition.kt`;
- `PixelRasterCatalog.kt`;
- `PixelSceneCatalog.kt`;
- `PixelSceneOverlayCatalog.kt`;
- `PixelStoryActorCatalog.kt`;
- `PixelTraceFxCatalog.kt`;
- `PixelTraceStrainCatalog.kt`;
- `PixelUiChromeCatalog.kt`;
- `PixelUiIconCatalog.kt`;
- `PixelUiUtilityCatalog.kt`.

These catalogs demonstrate a real layered visual runtime foundation, but final art quality/provenance varies by asset family and must be reconciled against the production ledger.

## 10. Character/room/panel direction

Target room composition is:

`environment -> structure -> permanent props -> decals -> room actors -> equipment/held objects -> player-safe state overlays -> FX -> focus/panel UI -> text/actions`

A named character may use:

1. room actor sprite;
2. canonical portrait;
3. contextual focus/dialogue panel.

Character presence must come from a player-safe actor projection. UI must never infer an actor's presence from hidden quest flags or private NPC goals.

Jack remains a separate identity-production track from the 32x48 rig itself.

## 11. World-development state

The world beyond Gate Twelve is **not yet canonically populated**.

What is decided:

- world hierarchy and place-record schema;
- multiple coordinate spaces;
- political-entity schema;
- settlement schema;
- route/travel schema;
- ecology/resource schema;
- beast-zone schema;
- population/citizen-hierarchy schema;
- world level/balance schema;
- loot provenance;
- NPC population schema.

What still needs actual world decisions/content:

- parent world/macroregion of Gate Twelve;
- named nations/kingdoms;
- capitals/cities/towns/villages;
- political borders;
- cultures/institutions;
- population distributions;
- economic/resource flows;
- ecosystems and beast territories;
- world travel network;
- world-level progression bands;
- concrete NPC populations;
- concrete loot/resource tables;
- exact world coordinates.

Schemas must precede mass content generation.

## 12. Mechanics state

### Existing foundations to keep/extend

- deterministic authored scene/choice engine;
- quests;
- knowledge;
- NPC relationships/memory/goals;
- equipment;
- stats/effective modifiers;
- resources;
- abilities/techniques;
- training/recovery;
- persistence;
- validation;
- player-safe status/scene projection.

### Target systems requiring rework/new implementation

- final progression/class/rank taxonomy;
- citizen hierarchy/access;
- broader profession/activity framework;
- original tactical turn-based positional combat;
- original persistent rival/adversary evolution;
- world-level balance;
- expanded item/economy/loot provenance;
- richer NPC simulation/schedules/factions;
- hierarchical world navigation;
- final actor-panel/presence projection;
- final APK screen/navigation architecture.

## 13. Copyright-safe inspiration boundary

The project may use broad genre ideas such as:

- tactical turn-based positioning;
- action economy;
- cover;
- line of sight;
- persistent named rivals;
- encounter memory;
- promotions/injuries/recovery;
- faction consequences.

It must use original terminology, data structures, UI, balance, fiction, art, maps, characters, dialogue and presentation.

No protected XCOM or Nemesis-system expression is copied.

## 14. APK reconstruction state

The current Android client is a foundation, not the final product.

Final APK work remains late-stage and must classify each subsystem as:

- KEEP;
- EXTEND;
- REWORK;
- REPLACE;
- REMOVE;
- ARCHIVE.

No broad deletion should occur before:

1. consumer audit;
2. replacement exists;
3. migration is defined;
4. exact-head tests/builds pass;
5. screenshot/emulator QA passes;
6. physical-device QA is performed when required;
7. rollback/provenance is recorded.

## 15. Immediate unresolved controls

P0 unresolved work after this audit:

1. reproducible corpus/world/asset inventory tooling and snapshot;
2. exact branch/HEAD reconciliation of the visual implementation stack;
3. asset provenance reconciliation across current raster/source-master/branch variants;
4. mapping of every Android screen consumer to the final UX contract;
5. mapping of every engine subsystem to KEEP/EXTEND/REWORK/REPLACE/REMOVE with concrete file consumers;
6. only then bounded runtime migrations.

## 16. Audit conclusion

The repository now has enough documentation structure to stop treating development as isolated patches.

The next development stage is **reconciliation**, not mass deletion and not indiscriminate feature creation.

The program must first know exactly:

- which branch owns each current implementation;
- which asset is source/provisional/final;
- which systems are already authoritative;
- which planned changes require migration;
- what can be reused without visual or semantic mismatch.

This audit is a snapshot control for that process.
