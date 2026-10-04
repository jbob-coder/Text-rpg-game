# THE GAME — Repository Master Task Register

Updated: 2026-10-04 AST
Timezone: America/Puerto_Rico (AST, UTC-4)  
Status: `PENDING` / `IN_PROGRESS` / `BLOCKED` / `DONE`

This is the repository-native operational index for future coding agents. It intentionally stays concise. Repository source files and fresh execution evidence outrank this document if they conflict.

## Authority / read order

1. Current repository files and exact branch/HEAD.
2. Fresh build/test/runtime evidence.
3. `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`.
4. `docs/MASTER_DOCUMENTATION_RECORD.md`.
5. This task register.
6. `docs/IMPLEMENTATION_STATUS.md`.
7. `docs/V6_STABILIZATION_HANDOFF.md`.
8. Chat memory / historical summaries.

Do not mark a task `DONE` without evidence. Every `DONE` task must record `COMPLETED_AT` in America/Puerto_Rico time. Unknown historical times use `NOT_RECORDED`.

## 2026-10-01 PRIORITY OVERRIDE — MASTER DOCUMENTATION PROGRAM

**Priority repository:** `jbob-coder/Text-rpg-game`  
**Priority mode:** documentation-first; broad implementation expansion follows written contracts.  
**Current program:** [`MASTER_GAME_DEVELOPMENT_PROGRAM.md`](MASTER_GAME_DEVELOPMENT_PROGRAM.md)  
**Master documentation record:** [`MASTER_DOCUMENTATION_RECORD.md`](MASTER_DOCUMENTATION_RECORD.md)  
**Cross-reference:** [`DOCUMENTATION_CROSS_REFERENCE_MATRIX.md`](DOCUMENTATION_CROSS_REFERENCE_MATRIX.md)

This section supersedes older statements about the top-level product objective while preserving their exact historical verification evidence.

### TASK D-000 — Establish repository-wide master documentation authority
- STATUS: `DONE`
- PRIORITY: `P0`
- RESULT: master development program created; current repository designated priority game project; permissions, prohibitions, domain volumes, execution gates and final APK sequencing documented.
- BRANCH: `docs/master-game-development-program`
- COMPLETED_AT: `2026-10-01 AST`

### TASK D-001 — Build documentation cross-reference matrix
- STATUS: `DONE`
- PRIORITY: `P0`
- RESULT: major existing and planned documents mapped to scope, dependencies, implementation consumers and required follow-ups.
- COMPLETED_AT: `2026-10-01 AST`

### TASK D-002 — Define pixel-art runtime composition
- STATUS: `DONE`
- PRIORITY: `P0`
- RESULT: environment/prop/overlay/room-actor/player/FX/panel composition contract documented, including reuse compatibility and current-vs-planned asset-stage guidance.
- DOCUMENT: `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`
- COMPLETED_AT: `2026-10-01 AST`

### TASK D-003 — Establish world-development master index
- STATUS: `DONE`
- PRIORITY: `P0`
- RESULT: world hierarchy, coordinate layers, places, political entities, settlements, ecosystems, resources, beasts, loot/items, social hierarchy, NPCs, balance, tactical combat integration and dynamic-rival direction decomposed into future child standards.
- DOCUMENT: `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`
- COMPLETED_AT: `2026-10-01 AST`

### TASK D-004 — Document final Android/APK rebuild program
- STATUS: `DONE`
- PRIORITY: `P0`
- RESULT: final APK work defined as late-stage keep/extend/rework/replace/remove migration driven by completed system contracts.
- DOCUMENT: `docs/android/APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md`
- COMPLETED_AT: `2026-10-01 AST`

### TASK D-005 — Finish Gate Twelve region master plan Steps 8–14
- STATUS: `DONE`
- PRIORITY: `P0`
- RESULT: Steps 1–14 are complete as a first-pass proof-region contract covering UX, state layers, loading/performance, implementation order, verification, migration/removal, and execution handoff.
- DOCUMENT: `docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md`
- NEXT CONSUMER: TASK D-006 exact existing-state audit and Gate Twelve implementation/provenance reconciliation.
- COMPLETED_AT: `2026-10-02 08:01 AST`.

### TASK D-006 — Existing-state repository audit
- STATUS: `IN_PROGRESS / CURRENT-HEAD SOURCE INVENTORY COMPLETE / CROSS-BRANCH CONSUMER RECONCILIATION REMAINS`
- PRIORITY: `P0`
- CURRENT:
  - `docs/EXISTING_STATE_REWORK_DECISION_MATRIX.md` owns high-level KEEP / EXTEND / REWORK / REPLACE / REMOVE / UNKNOWN policy.
  - `docs/LIVE_REPOSITORY_STATE_AUDIT_2026-10-02.md` records earlier live program/PR landscape.
  - `docs/DEEP_SOURCE_EXISTING_STATE_AUDIT_2026-10-04.md` now inventories the current audited HEAD at module/component/content/save/asset/test/build level and attaches current responsibility/disposition.
- CURRENT-HEAD AUDIT COVERAGE:
  - 19 Python engine modules;
  - 35 Android main Kotlin files;
  - 2 authored content JSON files;
  - exact GameState/save-schema fields;
  - 24 runtime PNGs;
  - 21 Python tests, 27 Android JVM tests and 3 Android instrumented tests;
  - 2 workflows and 5 Android build/manifest configuration files.
- REMAINING:
  - exact field-to-composable/ViewModel/bridge consumer map;
  - per-catalog consumer and hardcoded-state audit;
  - D-029 asset lineage/equivalence completion;
  - D-020 cross-branch survivor/migration matrix;
  - D-044 remaining Class-C extraction;
  - zero-consumer/deprecation proof before any REMOVE action.
- OUTPUT: subsystem matrix with KEEP / EXTEND / REWORK / REPLACE / REMOVE / UNKNOWN and exact branch/HEAD evidence.

### TASK D-007 — Progression / class / rank master
- STATUS: `DONE`
- PRIORITY: `P1`
- DOCUMENT: `docs/systems/PROGRESSION_MASTER_PLAN.md`
- RESULT: progression/class/rank contract exists; implementation/migration remains separate.
- COMPLETED_AT: `2026-10-02 07:32 AST`

### TASK D-008 — NPC / social / dynamic-rival master
- STATUS: `DONE`
- PRIORITY: `P1`
- DOCUMENT: `docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md`
- RESULT: NPC memory/social/hierarchy/persistent-adversary direction documented; implementation remains separate.
- COMPLETED_AT: `2026-10-02 07:32 AST`

### TASK D-009 — Tactical combat master
- STATUS: `DONE`
- PRIORITY: `P1`
- DOCUMENT: `docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md`
- RESULT: original tactical-combat contract created without adopting protected XCOM presentation/terminology.
- COMPLETED_AT: `2026-10-02 07:32 AST`

### TASK D-010 — Items / economy / loot master
- STATUS: `DONE`
- PRIORITY: `P1`
- DOCUMENT: `docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md`
- RESULT: item/equipment/accessory/economy/loot provenance contract created.
- COMPLETED_AT: `2026-10-02 07:32 AST`

### TASK D-011 — Application UX master
- STATUS: `DONE`
- PRIORITY: `P1`
- DOCUMENT: `docs/android/APPLICATION_UX_MASTER_PLAN.md`
- RESULT: application-wide target surfaces and player-safe presentation ownership documented.
- COMPLETED_AT: `2026-10-02 07:32 AST`

### TASK D-013 — Documentation corpus architecture
- STATUS: `DONE`
- PRIORITY: `P0`
- DOCUMENT: `docs/DOCUMENTATION_CORPUS_ARCHITECTURE.md`
- RESULT: long-range volume, branch, record, cross-reference, counting and reconstruction rules documented.
- COMPLETED_AT: `2026-10-02 07:32 AST`

### TASK D-014 — World geography standard
- STATUS: `DONE`
- PRIORITY: `P0`
- DOCUMENT: `docs/world/WORLD_GEOGRAPHY_STANDARD.md`
- COMPLETED_AT: `2026-10-02 07:32 AST`

### TASK D-015 — Political entity standard/catalog seed
- STATUS: `DONE`
- PRIORITY: `P1`
- DOCUMENT: `docs/world/WORLD_POLITICAL_ENTITIES.md`
- COMPLETED_AT: `2026-10-02 07:32 AST`

### TASK D-016 — Settlement catalog standard
- STATUS: `DONE`
- PRIORITY: `P1`
- DOCUMENT: `docs/world/WORLD_SETTLEMENT_CATALOG.md`
- COMPLETED_AT: `2026-10-02 07:32 AST`

### TASK D-017 — World travel/route standard
- STATUS: `DONE`
- PRIORITY: `P1`
- DOCUMENT: `docs/world/WORLD_TRAVEL_AND_ROUTES.md`
- COMPLETED_AT: `2026-10-02 07:32 AST`

### TASK D-018 — Room actor/panel/overlay reuse packet standard
- STATUS: `DONE`
- PRIORITY: `P0`
- DOCUMENT: `docs/assets/ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md`
- RESULT: area packet, character-in-room, portrait/focus-panel, text/signage, overlay and reuse compatibility rules documented.
- COMPLETED_AT: `2026-10-02 07:32 AST`

### TASK D-019 — Reproducible documentation/world/asset inventory
- STATUS: `IN_PROGRESS / EXACT STRUCTURAL SNAPSHOT REFRESHED`
- PRIORITY: `P0`
- CURRENT:
  - `docs/REPOSITORY_CORPUS_INVENTORY_SNAPSHOT_2026-10-04.md` records exact recursive-tree structural counts for source HEAD `991cd9b29ea0752fa1c303a19e8f210713efe4b5`.
  - `docs/evidence/repository_inventory_2026-10-04.json` persists the same machine-readable checkpoint.
  - exact source-head structure: 490 tracked files; 320 repository Markdown files; 318 under `docs/`; 21 structured documentation paths; 24 PNGs; 42 Python files; 68 Kotlin/KTS files; 51 Python/Kotlin test-source paths.
  - bounded structured counts now include 104 asset-manifest rows / 95 unique asset IDs, the repository-owned 1,019-record Status Wave-001 structural audit, and the 9-node / 8-edge Gate Twelve baseline.
  - `tools/documentation_inventory.py` remains the deterministic complete-checkout path for word counts and broader local inventory.
- REMAINING:
  - execute/persist the tool from a complete checkout of the exact current program HEAD;
  - publish exact current-head Markdown word/heading counts;
  - add generalized structured world/domain record extractors beyond already audited packets;
  - reconcile asset-stage counts against provenance authority rather than last-seen manifest status;
  - separate executed-test evidence from test-source counts;
  - define/confirm how owner numeric targets map to reproducible units.
- OUTPUT: reproducible counts for active docs, words, records, assets, world entities, tasks, tests and evidence without assuming the owner's ambiguous numeric units.

### TASK D-020 — Reconcile stacked pixel/application implementation branches
- STATUS: `IN_PROGRESS / PR-LEVEL RECONCILIATION COMPLETE / SURVIVOR MIGRATION REMAINS`
- PRIORITY: `P0`
- INPUT: live audit plus implementation PRs #7–#31.
- CURRENT:
  - D-028 / `docs/IMPLEMENTATION_PR_7_31_RECONCILIATION_2026-10-02.md` completed exact PR-head/base/ancestry/workflow reconciliation.
  - D-029 now owns asset-family provenance and unresolved static/animation survivor decisions.
  - D-026/D-021 own Android consumer/projection reconciliation.
- REMAINING: consolidate the surviving visual/application implementation choices into the destination architecture and record which candidate branches are migrated, reimplemented, superseded or retained only as provenance.
- OUTPUT: one final branch/provenance survivor matrix suitable for implementation migration.

### TASK D-021 — Map Android consumers to final UX/domain contracts
- STATUS: `IN_PROGRESS`
- PRIORITY: `P0`
- CURRENT: D-026 materialized `docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md` with source-grounded GameSnapshot/GameEngine ownership and major screen mapping.
- REMAINING: complete line-by-line composable/ViewModel/bridge consumer mapping, asset packet ownership, missing projection fields and exact test/evidence coverage before broad UI replacement.
- OUTPUT: screen/component -> player-safe projection -> asset packet -> domain owner -> tests/evidence mapping.

### TASK D-022 — Trace expanded owner directive to repository authorities
- STATUS: `DONE`
- PRIORITY: `P0`
- DOCUMENT: `docs/OWNER_DIRECTIVE_TRACEABILITY_MATRIX_2026-10-02.md`
- RESULT: every major clause of the expanded 2026-10-02 directive is mapped to an owner document, current state, and next action; missing child contracts are explicitly identified.
- COMPLETED_AT: `2026-10-02 08:16 AST`

### TASK D-023 — Player activities / life-loop master
- STATUS: `DONE`
- PRIORITY: `P1`
- DOCUMENT: `docs/systems/PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md`
- RESULT: active/timed/scheduled/background activities, time, interruption, concurrency, training/study/work/recovery/social/diagnostic boundaries, persistence and UI projection are documented.
- COMPLETED_AT: `2026-10-02 08:16 AST`

### TASK D-024 — Operational world coordinate and scale standard
- STATUS: `DONE`
- PRIORITY: `P0`
- DOCUMENT: `docs/world/WORLD_COORDINATE_AND_SCALE_STANDARD.md`
- RESULT: W0–W4 operational coordinate rules, units/origins/bounds/transforms, logical/presentation separation, route anchors, verticality, versioning and validation are documented.
- COMPLETED_AT: `2026-10-02 08:16 AST`

### TASK D-025 — Asset provenance registry seed
- STATUS: `IN_PROGRESS`
- PRIORITY: `P0`
- DOCUMENT: `docs/assets/ASSET_PROVENANCE_REGISTRY.md`
- CURRENT: provenance schema and initial 24-raster seed/reconciliation queue documented.
- REMAINING: exact source-master/hash/branch/consumer/QA reconciliation for each asset family.

### TASK D-026 — Android consumer/projection map
- STATUS: `IN_PROGRESS`
- PRIORITY: `P0`
- DOCUMENT: `docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md`
- CURRENT: source-grounded `GameSnapshot`/`GameEngine` surface map plus major screen ownership and missing projection contracts documented.
- REMAINING: line-by-line composable/ViewModel/bridge consumer audit and test mapping.

### TASK D-047 — Establish master documentation record
- STATUS: `DONE`
- PRIORITY: `P0`
- DOCUMENT: `docs/MASTER_DOCUMENTATION_RECORD.md`
- RESULT: one repository-native control record now consolidates documentation areas, exact audited path counts, completed contract layers, partial areas, missing work, blockers, authority links, update rules and immediate execution order.
- AUDIT_BASE: `docs/master-game-development-program@28809b7abdaf6f7f05ccd58cf0d5e71efacf5e22`
- CREATED_COMMIT: `5c06fe354816d7f454ca27f75806271278fc09ff`
- MAINTENANCE_RULE: update the master record whenever a major documentation area's state, blocker, authority or next action materially changes.
- COMPLETED_AT: `2026-10-04 AST`

### TASK D-012 — Final APK keep/rebuild matrix and execution
- STATUS: `BLOCKED`
- PRIORITY: `LATE-STAGE`
- BLOCKED_BY: domain documentation contracts and migration plans.


## Current repository baseline

- Repository: `jbob-coder/Text-rpg-game`
- Current Android integration branch: `integration/android-open-world-v1-reconcile`
- Current verified pixel-asset runtime parent: `1c7e54e548ab3c28819af0b85ae8cbba53aff827` (PR #7)
- Stabilization branch retained: `fix/v6-runtime-boundaries`
- Stabilization baseline before continuity work: `fcfe8115a72eb07036fa4e74a61a0094eaa3ff10`
- V6 parent: `integration/rules-ability-v6-reconcile@7f5f104fb839068bdfaf5cec72f37129ae20d463`
- `main`: placeholder; do not treat it as the canonical implementation.
- Untouched V6 recorded execution: 258 tests, 245 passed, 1 failed, 12 errors.
- Repaired candidate recorded execution: 275 tests, 0 failures/errors/skips on CPython 3.12.14/Linux.
- Verified base-client content record at Android HEAD: 16 scenes, 25 choices, 3 quests, 1 power definition.
- Android runtime evidence: workflow run 65 / run ID 36351957867; Python 290/290 OK; Android build/compile gates OK; representative emulator API 35 x86_64 completed 3 tests successfully.
- APK SHA-256 for exact Android HEAD: `94e325d55c5dd1404dbab8d0209dbfe1f8c0c29c5abecfdd582736851da4cd74`.
- Physical handset validation and APK delivery remain separate gates.
- Seven-attribute schema and save schema 1 remain; no stat/save migration has been performed.

The 275-pass evidence is committed under `docs/verification/v6/`. It is historical evidence for that exact candidate, not proof for later code changes.

## Current product objective

Evolve the rules-engine vertical slice into an Android narrative RPG with:

- visible player character/avatar;
- large readable narrative presentation;
- separate Stats, Equipment, Inventory, Quests, Map, Saves, and Settings areas;
- better decision cards/pop-ups;
- interactive world/city navigation;
- branching persistent narrative rather than a repetitive text-choice loop;
- main quests, side quests, optional quests, and world/lore exploration;
- tap-to-narrate voice/audio controls;
- improved illustrations;
- developer/cheat panel separated from normal gameplay;
- authoritative engine state feeding a player-safe Android presentation layer.

Architecture direction:

`GameState -> World/Quest/Narrative -> Rules/Stats/Abilities/Equipment -> Player-safe projection -> Android UI`

The UI must not become the authoritative rules engine.

## P0 — Android startup

### TASK A-001 — Resolve Android black-screen incident
- STATUS: `DONE`
- PRIORITY: `P0 / BLOCKING`
- RESOLUTION: the exact failure inside the old ephemeral NativeActivity/WebView wrapper remains unrecoverable because its authoritative wrapper source/artifact was not retained. The incident was closed by replacing that wrapper with a repository-owned reproducible Kotlin/Compose + Chaquopy client with visible startup/error states.
- VERIFIED RUNTIME (2026-09-27 17:34 AST):
  - exact source `510851cc165702fbe19ef005083a03cbcd00a9f3`;
  - workflow run `36351957867` completed successfully;
  - real `MainActivity` booted on Android API 35 x86_64 emulator;
  - Python engine initialized and rendered visible gameplay;
  - first authored choice advanced to the next scene;
  - Save -> further choice -> Load/Continue restored the saved scene;
  - 3 connected Android instrumentation tests finished successfully.
- LIMITATION: this resolves the black-screen product failure class on a representative Android runtime; it does not retroactively prove the exact internal crash mechanism of the discarded wrapper.
- COMPLETED_AT: `2026-09-27 17:34 AST`

### TASK A-002 — Rebuild corrected APK
- STATUS: `IN_PROGRESS`
- DEPENDS_ON: A-001
- VERIFIED: debug APK builds from repository source; package structure checks pass for ARM64, ARMv7, x86_64 and bundled content. Exact SHA-256 at `510851cc…`: `94e325d55c5dd1404dbab8d0209dbfe1f8c0c29c5abecfdd582736851da4cd74`.
- REMAINING: produce/download the distributable artifact from a controlled build and deliver it to the user; physical handset install remains separate.
- DONE WHEN: package builds, integrity/signing is checked, and artifact is delivered.
- COMPLETED_AT: —

### TASK A-003 — Physical/representative Android validation
- STATUS: `DONE`
- DEPENDS_ON: A-002 build path
- VERIFIED: Android API 35 x86_64 representative emulator booted the real Activity and completed 3 connected tests, including visible startup/choice and Save/Continue restoration.
- LIMITATION: no physical handset is claimed by this task result.
- DONE WHEN: visible startup/gameplay is confirmed; black screen no longer reproduces on a representative Android runtime.
- COMPLETED_AT: `2026-09-27 17:34 AST`

## UI / UX reconstruction

### TASK U-001 — Primary gameplay layout
- STATUS: `DONE`
- RESULT: repository-owned Compose shell has persistent pixel avatar, scene illustration, large narrative panel, choice cards, top status/settings and separate bottom navigation.
- EVIDENCE: exact Android HEAD `510851cc…` compiled and booted on representative emulator.
- COMPLETED_AT: `2026-09-27 17:34 AST`

### TASK U-002 — Narrative readability
- STATUS: `DONE`
- RESULT: dedicated scrollable narrative surface, preserved authored title casing, large body typography, text-reveal control and scene-change scroll reset.
- COMPLETED_AT: `2026-09-27 17:34 AST`

### TASK U-003 — Decision presentation
- STATUS: `DONE`
- RESULT: pixel decision cards expose enabled/locked state and player-safe disabled reason; authoritative consequences remain Python-owned.
- COMPLETED_AT: `2026-09-27 17:34 AST`

### TASK U-004 — Settings/save separation
- STATUS: `IN_PROGRESS`
- Top-right Settings with Audio, Narration, Text speed/delay, Controls, Save, Load, Accessibility.
- Saves must not clutter the primary gameplay HUD.
- COMPLETED_AT: —

### TASK U-005 — Developer/cheat panel
- STATUS: `IN_PROGRESS`
- IMPLEMENTED: hideable Developer surface and validated Python whitelist (`FULLRESTORE`, `CLEARCONDITIONS`, `GIVE_RELAY`, `MAXATTR`, `DEBUGMAP`).
- Separate/hideable developer surface for XP, level, items, quests, stats, teleport, currency, abilities, world flags, time.
- COMPLETED_AT: —

## Character / stats / equipment

### TASK P-001 — Visible avatar
- STATUS: `DONE`
- RESULT: persistent pixel player avatar is visible in the gameplay layout and confirmed by connected Android smoke.
- COMPLETED_AT: `2026-09-27 17:34 AST`

### TASK P-002 — Equipment model + visual integration
- STATUS: `IN_PROGRESS`
- IMPLEMENTED: authoritative equipment slots, equip/unequip bridge, Android inventory/equipment controls, and verified 32x48 paper-doll presentation for explicitly authored overlays.
- VERIFIED CONTRACT: `fix/avatar-overlay-rig-contract` / PR #10 requires exact `itemId + slot + zOrder + 32x48 sprite` mappings at one shared character origin. Unmapped equipment remains logically equipped and does not receive invented avatar geometry.
- CURRENT AUTHORED STARTING OVERLAYS: Depot Jacket, Work Gloves, Signal Ring, Courier Neck Tag.
- Planned slots: Head, Chest, Hands, Legs, Feet, Main Hand, Off Hand, Ring 1, Ring 2, Neck, Accessory 1, Accessory 2.
- VERIFIED UI: the phone-safe Character screen now surrounds the central 32x48 avatar with semantic slot rails, opens one selected-equipment detail panel, routes unequip through the authoritative engine, and labels unmapped equipped items as logical-only rather than inventing artwork.
- REMAINING: additional authored overlays, held-object anchor integration, and physical-device visual review.
- COMPLETED_AT: —

### TASK P-003 — Dedicated detailed Stats screen
- STATUS: `IN_PROGRESS`
- IMPLEMENTED: separate Stats surface with compact player/resources summary, the canonical seven attributes, derived stats, skills and conditions from the player-safe projection. Attributes and skills are now selectable and request on-demand authoritative contribution explanations instead of duplicating modifier math in Compose.
- VERIFIED SLICE: `feature/player-safe-stat-inspection@4f1775e6812fba7133465a9cfcac8ee48f2b1c14`, PR #11, Android Pixel Client run 219 / ID `36792301545`: Python 303/303; Android unit/instrumentation compile/assemble/package passed; API 35 x86_64 emulator started 18 connected tests and completed successfully with 0 failures.
- APK SHA-256: `da3b870542bbd4dd1f49b284f9a86b09bcf9c8e245cc4c14fb56311780a6b154`.
- PLAYER-SAFE DETAIL: equipment sources appear through safe explanation provenance (for example `equipment:body`) while raw item modifier maps remain absent from the inventory/equipment projection.
- REMAINING: deeper derived-stat explanation and later progression/social presentation where authoritative data exists.
- COMPLETED_AT: —

### TASK P-004 — Inventory / Equipment panels
- STATUS: `DONE`
- RESULT: Inventory and Equipment are separate from narrative; equip/unequip mutations run through Python and return updated player-safe state.
- COMPLETED_AT: `2026-09-27 17:34 AST`
- Separate from main narrative screen.
- COMPLETED_AT: —

## World / map

### TASK W-001 — Interactive map
- STATUS: `IN_PROGRESS`
- IMPLEMENTED: authored location graph, discovered nodes, route rendering, selected destination and authoritative travel/time. Directly tappable pixel nodes and narrative destination travel are being validated in `feature/android-open-world-v1`.
- Start with a maintainable interactive 2D location/world map before heavier 3D.
- COMPLETED_AT: —

### TASK W-002 — City/location graph
- STATUS: `IN_PROGRESS`
- Locations/interiors/NPC destinations/events represented with stable IDs.
- Example labels are not automatically canon.
- COMPLETED_AT: —

### TASK W-003 — World interaction
- STATUS: `IN_PROGRESS`
- Movement between locations; NPC visits; optional exploration; location/world-state-triggered events.
- COMPLETED_AT: —

### TASK W-004 — Persistent world events
- STATUS: `IN_PROGRESS`
- Choices can set flags and produce delayed NPC/world changes and route changes.
- COMPLETED_AT: —

## Quest / narrative

### TASK Q-001 — Main Quest framework
- STATUS: `DONE`
- RESULT: authoritative staged quest graph exists and is projected to Android by category.
- COMPLETED_AT: `2026-09-27 17:34 AST`
- Branching main-story progression.
- COMPLETED_AT: —

### TASK Q-002 — Side Quest framework
- STATUS: `DONE`
- RESULT: side quest category and authored Gate Twelve quest are supported by the same authoritative quest system.
- COMPLETED_AT: `2026-09-27 17:34 AST`
- Optional integrated side stories.
- COMPLETED_AT: —

### TASK Q-003 — Optional Quest framework
- STATUS: `DONE`
- RESULT: optional quest category and Trace Stabilization content are supported and projected.
- COMPLETED_AT: `2026-09-27 17:34 AST`
- Optional activities not required for main progression.
- COMPLETED_AT: —

### TASK Q-004 — Lore/world narrative exploration
- STATUS: `IN_PROGRESS`
- CANDIDATE: `feature/android-open-world-v1` adds an authored lore quest and cross-location knowledge consequences; not DONE until integration gates pass.
- Optional discoverable world information.
- COMPLETED_AT: —

### TASK Q-005 — Branching narrative graph
- STATUS: `IN_PROGRESS`
- Persistent flags, delayed consequences, non-stat consequences, reconvergence and mutually exclusive routes where authored.
- COMPLETED_AT: —

### TASK Q-006 — Canon/context consistency
- STATUS: `IN_PROGRESS`
- RULE: current expansion is original project content; external/reference novel material is not silently imported as canon.
- Re-read authoritative project context before expanding story; do not silently import copyrighted/reference story content as canon.
- COMPLETED_AT: —

## Audio / visual presentation

### TASK M-001 — Tap-to-narrate
- STATUS: `IN_PROGRESS`
- IMPLEMENTED: native Android TTS, tap/read-aloud, replay, stop, auto-read, speech-rate and text-reveal controls. Voice selection/pause semantics remain follow-up work.
- Play/pause/replay; auto-read; speed/text delay; voice selection if supported.
- COMPLETED_AT: —

### TASK M-002 — Scene illustrations
- STATUS: `IN_PROGRESS`
- IMPLEMENTED: procedural pixel scene illustrations for the current depot/Gate Twelve slice; broader location coverage remains in progress.
- Consistent visual storytelling for locations/events/characters.
- COMPLETED_AT: —

### TASK M-003 — Character visual asset pipeline
- STATUS: `IN_PROGRESS`
- CANDIDATE: paper-doll equipment layers are implemented on `feature/android-open-world-v1`; reusable external asset pipeline is not finished.
- Reusable avatar/equipment visual pipeline rather than one-off replacements.
- COMPLETED_AT: —

## Repository / continuity

### TASK R-001 — Re-verify fixes after runtime repair
- STATUS: `DONE`
- RESULT: branch topology, `fcfe8115…` repair scope, PR #4 state, and committed 275-test evidence were verified from GitHub.
- COMPLETED_AT: `2026-09-27 14:12 AST`

### TASK R-002 — Repo-native agent continuity
- STATUS: `DONE`
- RESULT: root `AGENTS.md`, this task register, and README entrypoint were written to `fix/v6-runtime-boundaries` and fetched back from GitHub for verification.
- COMPLETED_AT: `2026-09-27 14:21 AST`



## Pixel asset production documentation

### TASK M-004 — Pixel asset production system and Batch 001
- STATUS: `DONE`
- BRANCH: `docs/pixel-asset-production-plan-v1`
- RESULT:
  - pixel asset master production rules documented;
  - detailed player paper-doll and NPC_TAMSIN blueprints documented;
  - full v1 roadmap contains five exact 100-unit batches, 500 unique planned asset units total;
  - Batch 001 covers current playable content; Batches 002–005 cover technical/non-canon character, equipment, world, UI/FX/accessibility expansion frameworks;
  - generated-reference -> reverse-engineered pixel blueprint pipeline documented;
  - machine-readable manifest/state-binding/QA schema documented;
  - mechanical verification confirms IDs 001–500 are continuous with no missing or duplicate numbers and no duplicate stable asset IDs;
  - visual bible linked to the new production documents.
- IMPORTANT: this task completes the v1 500-unit documentation/planning baseline only. It does not claim that any of the 500 assets have been generated, reconstructed, integrated or verified.
- COMPLETED_AT: `NOT_RECORDED`

### TASK M-005 — Produce Batch 001 assets
- STATUS: `IN_PROGRESS`
- DEPENDS_ON: M-004
- VERIFIED STATE:
  - complete v1 baseline: 500 unique planned units;
  - first broad concept board persisted as `REF_BATCH001_CONCEPT_BOARD_A` and audited as style-only, not canonical geometry;
  - Wave A reconstruction packet completed for assets 001, 002, 018, 021 and 022;
  - Wave A machine-readable manifest completed;
  - production branch: `feature/pixel-asset-wave-a`;
  - active reconciliation draft PR: #7; PR #6 is closed as superseded;
  - `PLAYER_GAMEPLAY_FRONT_BASE`, `ITEM_DEPOT_JACKET_ICON`, and `ITEM_DEPOT_JACKET_PAPERDOLL` are implemented as source-native pixel maps and integrated into Compose;
  - generated assets remain text-native/diffable rather than opaque binary blobs; PNG export can derive from the same authoritative pixel maps later;
  - exact jacket mapping requires `ITEM_DEPOT_JACKET` + `body` slot, preventing unrelated chest items from inheriting its art;
  - temporary player hair is explicitly technical/non-canon and excluded from the production asset set;
  - PR #6 verification at `0f6e3101753901ded43794ef3a1b4321b149d1c9`: Python 300/300; Android unit/assemble gate passed; API 35 x86_64 emulator completed 7/7 connected tests with 0 failures; APK SHA-256 `9ba444a729e83a090dc8b0721546b6f3f1291100a1cd043dbeec04685a7ea8b3`;
  - `PLAYER_BODYFRAME_A_TURNAROUND` and `NPC_TAMSIN_TURNAROUND` remain `BRIEF_LOCKED`; mixed generated boards remain rejected for canonical geometry.
  - Batch 001 assets 023–033 are now implemented/integrated: Work Gloves icon/layer, Signal Ring icon/layer, Courier Neck Tag icon/layer, Maintenance Seal icon, Dead Relay intact/opened/damaged/signal-lost visuals.
  - relay visual state crosses the Python→Android boundary only as `visuals.relay_state = null|intact|opened|damaged|signal_lost`; Compose never reads raw story flags.
  - exact-head integration evidence at `57151051ea2e0ac98810e5ee95cea9de1a2a4e97`, workflow `36378000460`: Python 301/301; Android unit/instrumentation/assemble/package gates passed; API 35 x86_64 emulator 8/8 with 0 failures; APK SHA-256 `9df410a12a8052cd76ca9dee40e5a583f98f77043c2376ea948d43c063ef4ca3`.
  - all 9/9 currently authored named locations now resolve to source-native 128x64 scene masters: Platform Nine, Relay Workbench, Gate Twelve, Service Tunnel, Quiet Stair, Trace Chamber, Depot Plaza, Municipal Archive, Workshop Row;
  - Batch 001 state overlays 046/048/051 are integrated: Gate Twelve Echo Active, Service Tunnel Aftershock, Trace Chamber Training;
  - scene-state overlays are selected only from already player-facing `GameSnapshot.sceneId`; Compose does not read raw story flags;
  - exact-head scene/overlay evidence at `1c7e54e548ab3c28819af0b85ae8cbba53aff827`, workflow `36384772701`: Python 301/301; Android unit/instrumentation/assemble/package gates passed; API 35 x86_64 emulator 10/10 with 0 failures; APK SHA-256 `18316402c65e9b614b80fa542817b125bed8a38be44eaf3ca89d187623f1897f`;
  - Batch 001 UI/map assets 076–095 are integrated: seven navigation icons, four resource icons, four quest-category icons, and five player-safe map markers;
  - navigation/resource/quest icons remain decorative and consume only existing Compose/GameSnapshot state; map marker current/reachable/discovered semantics remain projection-owned;
  - exact-head UI/map evidence at `61cd0ecba6d661522ef59e519f26b8e1697a113c`, workflow `36444738131`: Python 301/301; Android unit/instrumentation/assemble/package gates passed; API 35 x86_64 emulator 11/11 with 0 failures; APK SHA-256 `338f5024dfa0a07d67bfa3517bf19d802adc5ef58052abac77b7ee226d5370ab`;
  - the first UI-icon emulator gate correctly caught a phone-layout regression where horizontal icons pushed More off-screen; the navigation composition was compacted vertically and the exact rerun passed.
  - asset 039 `UI_ITEM_QUALITY_FRAMES` is integrated: separate 32x32 transparent standard/uncommon frame masters overlay existing item art without recoloring it. Inventory quality crosses the player-safe bridge only from explicit authored item-definition metadata; absent/unsupported values render no frame rather than being inferred. Exact-head evidence at `5bb0096d7570dca04a4eec3c6528985d84e23145`, workflow `36739855690`: Python 301/301; Android unit/instrumentation/assemble/package gates passed; API 35 x86_64 emulator 15/15 with 0 failures; APK SHA-256 `584727a5bd20c7a8a2e542aeb0807abd564e06bc9346b6e61f21bee2a6a5027a`.
  - asset 040 `UI_EQUIPMENT_SLOT_ICON_SET` is integrated and formally evidenced: 12 distinct 24x24 source-native slot silhouettes map only from the 12 projected semantic slot IDs and are wired into Character/Inventory. The exact-head gate at `5bb0096d7570dca04a4eec3c6528985d84e23145`, workflow `36739855690`, includes its unit and Compose rendering tests: Python 301/301; Android unit/instrumentation/assemble/package gates passed; emulator 15/15 with 0 failures; APK SHA-256 `584727a5bd20c7a8a2e542aeb0807abd564e06bc9346b6e61f21bee2a6a5027a`.
  - asset 053 `DISTRICT_PLAZA_BLACKOUT_SCENE` is integrated: a transparent 128x64 blackout/emergency-light overlay bound only to player-facing `sceneId = DISTRICT_HUB`, whose authored narrative explicitly says Depot Plaza remains under emergency lighting. Exact-head evidence at `a9aa658580bfb659fd6b499fb6b59494db7a60a9`, workflow `36742882890`: Python 301/301; Android unit/instrumentation/assemble/package gates passed; API 35 x86_64 emulator 15/15 with 0 failures; APK SHA-256 `cfc83d9cad0550001bd71c4243f78c5c763bed125509e0f1c51b4b07e26bcc89`.
  - asset 044 `RELAY_WORKBENCH_RELAY_OPEN_SCENE` is integrated: a transparent 128x64 inspection-state overlay bound only to `GameSnapshot.visuals.relayState` values `opened`, `damaged`, or `signal_lost` while at `RELAY_WORKBENCH`. Exact casing state remains owned by relay prop assets 031–033. Exact-head evidence at `025a407b83568ebf3d4706737d75ae760a92a19f`, workflow `36754045934`: Python 301/301; Android unit/instrumentation/assemble/package gates passed; API 35 x86_64 emulator 15/15 with 0 failures; APK SHA-256 `3c8cdfd5b4c6f5fd563bedbcbc6f488ca6d42e3a259ab6cec539158d38cfc23e`.
  - assets 062/063 `EMERGENCY_LIGHT_OVERLAY` / `BLACKOUT_SHADOW_OVERLAY` are integrated: two reusable 128x64 transparent masters consumed by asset 053 instead of duplicated shadow/light pixels. Exact-head evidence at `e388d9333ddb18228d6886f283a70047627b65b5`, workflow `36755094616`: Python 301/301; Android unit/instrumentation/assemble/package gates passed; API 35 x86_64 emulator 15/15 with 0 failures; APK SHA-256 `31067528314dac9e5052f48ce00a97a75d68518b602664dbc80d816a88eca75f`.
  - assets 072–075 are integrated: reusable Archive shelf, Archive terminal, Workshop bench and District notice-board masters are source-native and placed through the shared `PixelEnvironmentPropCatalog`. Exact-head evidence at `96831c00614cb4932a5ef39eb3de4cfb4f7b4e43`, workflow `36756037495`: Python 301/301; Android unit/instrumentation/assemble/package gates passed; API 35 x86_64 emulator 15/15 with 0 failures; APK SHA-256 `02c9d366889a871d06f7cc8257be73fb590461025eba1b4d773f400b061fc989`.
  - assets 067–071 are promoted INTEGRATED: reusable relay workbench, Gate Twelve door, tunnel pipe/cable sets and Trace Chamber apparatus masters render through the scene-pixel placement system using only player-facing location IDs. Exact-head evidence at `cedd6b5354e9890623bb9fdd1bef7fcb670e4463`, workflow `36757598567` / run 203: Python 301/301; Android unit/instrumentation/assemble/package gates passed; API 35 x86_64 emulator 15/15 with 0 failures; APK SHA-256 `16f44cc92c463b004480c0713a05b65d0530c856b2d2e86a02847d6f6161a7ef`.
  - asset 096 `FX_TRACE_ECHO_AMBIENT` is integrated: four deterministic 64x64 transparent frames, animated in `SceneIllustration`, selected only from player-facing Trace-related `sceneId` values. Exact-head evidence at `3ac499ba229f97ea5363a151d7c74729bdfd61fc`, workflow `36732669582`: Python 301/301; Android unit/instrumentation/assemble/package gates passed; API 35 x86_64 emulator 12/12 with 0 failures; APK SHA-256 `a66d2c1a94eec6cd8fa6d12d5b453f1f5646af62a9701dd5c221745e564f3cf7`.
  - asset 097 `FX_SIGNAL_PULSE` is integrated: six deterministic 64x64 expanding-pulse frames, overriding ambient Trace FX only in player-facing scene `POWER_FIRST_LIVE_USE`. Exact-head evidence at `d83eda284f0f3e390beb16d4e8d27a137ba791ef`, workflow `36734148687`: Python 301/301; Android unit/instrumentation/assemble/package gates passed; API 35 x86_64 emulator 12/12 with 0 failures; APK SHA-256 `4f7321cf429133d2ac35ddbe22a1b884dc12f052eaa2aa1e3ec8cfb5cb01de4b`.
  - asset 098 `FX_DIRECTIONAL_TRACE` is integrated: six deterministic 64x64 frames that collapse a broad sensing sector into a directional line only in player-facing scene `TRACE_DIRECTIONAL_DISCOVERY_RESULT`. Exact-head evidence at `9ac9f6417efabd963a3351c182a1b3d2ac584397`, workflow `36735143906`: Python 301/301; Android unit/instrumentation/assemble/package gates passed; API 35 x86_64 emulator 12/12 with 0 failures; APK SHA-256 `d02adae48ce1a9e0c5732900cbfa6d3186288d39ab700354a9cf95da4062e751`.
  - Batch 001 now has 66/100 units integrated/accepted after promoting 067–071; assets 039/040, 044, 053, 062/063, 067–075 and 096–100 are green/evidenced.
  - asset 099 `FX_TRACE_STRAIN` is integrated: four 32x48 avatar-overlay frames plus four 64x64 portrait-overlay masters. The avatar overlay activates only from projected `GameSnapshot.conditions` containing `COND_ECHO_STRAIN`; the portrait master is produced but its renderer remains deferred because the current client has no dedicated portrait surface. Exact-head evidence at `5a1f966f469572cc6242573595392d702b11eb33`, workflow `36736526973`: Python 301/301; Android unit/instrumentation/assemble/package gates passed; API 35 x86_64 emulator 13/13 with 0 failures; APK SHA-256 `e26fe7700956ab1e22aafa9c0782a0c984186ff88609a673be6f89da945cb366`.
  - asset 100 `UI_MAP_TRAVEL_TRANSITION` is integrated: eight deterministic 128x64 route-preserving frames rendered as a full-screen Compose overlay. The ViewModel emits its transient `TravelTransitionUiState` only inside successful `engine.travel()` handling and only when the confirmed location changes; button press/busy state alone cannot trigger it. Exact-head evidence at `ab6da2fcb3e60693240fd27c701e1e2b0e388080`, workflow `36738135641`: Python 301/301; Android unit/instrumentation/assemble/package gates passed; API 35 x86_64 emulator 14/14 with 0 failures; APK SHA-256 `26e6998c1e5274f3ac399d7dc1f4b55354c35c132730d676de31a5dd95fdbf00`.
- LIMITATION: automated Compose/runtime coverage proves the catalog/state binding and tested client behavior, but native-scale art review and physical Galaxy A03 visual QA are not yet claimed.
- NEXT: assets 064–066 are now implemented as candidate presentation-only signage, ambient decals and a default depot-door landmark. Validate them on an exact-head workflow; if green, promote all three and continue with remaining low-risk environment modules/atlas 058–061 before returning to character-reference-blocked work. Do not invent door/access state in Compose. Do not unblock player/Tamsin canonical geometry by approximation. Physical Galaxy A03 visual QA remains a separate acceptance gate.
- RULE: generated images are reference-only until reconstructed into native pixel masters with manifests and QA.
- DONE WHEN: all 100 Batch 001 units reach their documented integration/deferred-integration acceptance state.
- COMPLETED_AT: —
### Avatar overlay rig contract closure
- STATUS: `VERIFIED_IMPLEMENTATION`
- BRANCH: `fix/avatar-overlay-rig-contract`
- PR: #10 — `Enforce character-oriented paper-doll overlays`.
- VERIFIED IMPLEMENTATION HEAD: `5097011f2cb15511e9695edc5475f2fd69c5f655`.
- CONTRACT: visible character equipment is rendered only from explicit `itemId + slot + zOrder + 32x48 sprite` paper-doll mappings sharing the base character origin. Equipped items without an authored overlay remain logically equipped but render no invented placeholder geometry.
- VERIFIED GATE: Android Pixel Client run 215 / ID `36778523620` completed successfully for the exact implementation head: Python 301/301; Android unit tests, Compose instrumentation compilation, debug APK assembly/package checks passed; API 35 x86_64 connected emulator completed 16 tests with 0 failures (confirmed from job 110102441501 logs).
- APK SHA-256: `8e9f08f7281367621c9db05862215a041f0d519b5531348b5e2cac50345c416c`.
- PHYSICAL QA: Galaxy A03 visual review and native-scale art approval remain separate.
- NEXT: build product-facing Character/Equipment presentation on this contract; do not reintroduce generic slot geometry or bind held props without explicit player-safe presentation state.

### Player-safe stat inspection / Stats UI slice
- STATUS: `VERIFIED_IMPLEMENTATION`
- BRANCH: `feature/player-safe-stat-inspection`
- PARENT: `fix/avatar-overlay-rig-contract@7d4558ea5c9e3ad24bf29fe42c8f199ed0be60fe`.
- OBJECTIVE: make the approved Stats screen inspectable without moving authoritative modifier arithmetic into Compose.
- IMPLEMENTED CANDIDATE:
  - Android bridge exposes on-demand `inspect_status(path)` through the existing rules-layer `inspect_status_value` projection;
  - inspection is restricted by the rules layer to visible status namespaces and redacts hidden perk/condition provenance before Android receives it;
  - inventory/equipment projection still omits raw modifier maps;
  - Kotlin maps stat inspection into typed contribution records;
  - Stats UI uses compact player/resource summary, selectable attributes and skills, and a dedicated selected-detail panel;
  - equipment contribution rows derive from player-safe source keys such as `equipment:body`, never from duplicated UI arithmetic;
  - inspection is serialized against engine mutations so a read cannot race equip/choice/travel state changes.
- TESTS ADDED: Python bridge coverage for Endurance + Depot Jacket and Technical Systems + Work Gloves, invalid-path rollback, Kotlin mapper/error classification, and Compose request/render coverage for equipment contributions.
- VERIFIED IMPLEMENTATION HEAD: `4f1775e6812fba7133465a9cfcac8ee48f2b1c14`.
- VERIFIED GATE: Android Pixel Client run 219 / ID `36792301545`: Python 303/303; Android unit tests, Compose instrumentation compilation, debug APK assembly/package checks passed; API 35 x86_64 emulator started 18 connected tests and completed with 0 failures.
- APK SHA-256: `da3b870542bbd4dd1f49b284f9a86b09bcf9c8e245cc4c14fb56311780a6b154`.
- BOUNDARY: derived-stat deep breakdown remains read-only summary in this slice; no raw authored rule maps are projected to Compose.
- NEXT: improve the Character/Equipment screen on top of the verified paper-doll contract without inventing unmapped gear art.

### Character / Equipment paper-doll UI slice
- STATUS: `VERIFIED_IMPLEMENTATION`
- BRANCH: `feature/character-equipment-paperdoll-ui`
- PARENT: `feature/player-safe-stat-inspection@7cba26a4c31c31ce19562ff79e830d14e6bb96b3`.
- OBJECTIVE: replace the horizontally scrolling Character placeholder with a phone-safe equipment presentation that directly reflects the verified 32x48 paper-doll contract.
- IMPLEMENTED CANDIDATE:
  - left/right semantic slot rails surround the central player avatar using the 12 authoritative equipment slots;
  - selecting a slot opens one focused equipment-detail panel rather than duplicating a quick-equipment strip;
  - authored overlays report their explicit 32x48 / z-order contract;
  - logically equipped items without an authored overlay are labeled `LOGICAL EQUIPMENT ONLY` and do not receive invented avatar geometry;
  - missing item icons are reported as not authored instead of drawing a fake item shape;
  - unequip actions route back through the authoritative Python equipment mutation path;
  - current projected resources and canonical attributes are summarized below the character without introducing an Appearance subsystem.
- TESTS ADDED: authored Depot Jacket selection/overlay/unequip routing and an unmapped future-head-item case proving no visible avatar gear is fabricated.
- VERIFIED IMPLEMENTATION HEAD: `b324dd555922a13f0672752f005d74fff68a09aa`.
- VERIFIED GATE: Android Pixel Client run 221 / ID `36793138990`: Python 303/303; Android unit tests, Compose instrumentation compilation, debug APK assembly/package checks passed; API 35 x86_64 emulator started 20 connected tests and completed successfully with 0 failures.
- APK SHA-256: `c9e2d1f90b91b57af98de5620faa36bbd795d468de3febcfac73bc3bdd6b96bb`.
- NEXT: retain this paper-doll contract while expanding player-facing Skills and later authored equipment detail.


### TASK M-006 — Apply existing runtime assets and safe visual expansion
- STATUS: `IN_PROGRESS`
- BRANCH: `feature/pixel-assets-runtime-expansion`
- BASE: `feature/character-stats-inspection@791a839b23d4c3b9c43b6b1a4f9f204008a8c7df`
- OBJECTIVE: reuse already-produced game assets first, then implement only safe documented visual assets that can be bound to existing player-safe UI state without inventing canon or gameplay semantics.
- EXISTING ASSETS APPLIED:
  - Batch 001 Wave-L `DEPOT_FACADE_EXTERIOR` (058) now has an exact Map arrival-preview binding for `DISTRICT_PLAZA`;
  - Batch 001 Wave-L `MUNICIPAL_ARCHIVE_EXTERIOR` (060) now has an exact Map arrival-preview binding for `DISTRICT_ARCHIVE`;
  - `MAINTENANCE_CORRIDOR_CONNECTOR` (059) and `MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS` (061) remain produced/deferred because no legitimate runtime composition surface currently consumes them.
- NEW DOCUMENTED ASSETS PRODUCED/APPLIED:
  - Batch 002 asset 192 `CHARACTER_GROUND_SHADOW_MEDIUM` replaces the old hard-coded PlayerAvatarPanel shadow and remains aligned to the shared character ground pivot;
  - Batch 005 panel assets 401–408 are implemented as hard-edged scalable pixel chrome and bound to Story, Character, Stats, Inventory, Quest, Map, Settings and Developer surfaces;
  - choice states 409/410, primary button 412 and tab states 415/416 are bound to existing player-safe/Compose state;
  - asset 417 `UI_SCROLL_MARKER` appears only when the narrative scroll state has remaining content;
  - asset 490 `ACCESS_AUDIO_NARRATION_ICON` is applied to the existing READ ALOUD action;
  - 411/413/414 are produced but deliberately deferred because selected-choice and secondary/danger button semantics are not yet explicitly represented at their call sites.
- CONTRACTS PRESERVED:
  - no canonical player/Tamsin geometry was fabricated;
  - no unmapped equipment receives fake paper-doll geometry;
  - Map previews use exact stable location IDs only and do not decide reachability/travel;
  - UI chrome remains presentation-only and does not own rules, availability, or persistence state.
- MANIFEST: `docs/assets/manifests/RUNTIME_EXPANSION_ASSET_WAVE_2026-09-30.json`.
- TEST COVERAGE ADDED: environment module exact-binding tests; character staging master test; UI utility master tests; UI chrome ID/mapping tests; Compose narration-icon, scrollable-choice and overflowing-narrative scroll-marker coverage.
- VERIFIED IMPLEMENTATION HEAD: `48d9f2c122709f78f51a2ff4041d65e66daf1e0a`.
- VERIFIED GATE: Android Pixel Client run 239 / ID `36807128327` completed successfully: Python 308/308; Android unit tests passed; Compose instrumentation tests compiled; debug APK assembly/package verification passed; API 35 x86_64 emulator completed 27/27 connected tests with 0 failures; UI screenshot set verified/uploaded.
- APK SHA-256: `a694d8e8796ebc55f3531f5a5d6aa32c747b848eea340c784075ed8310289c4a`.
- UI-QA ARTIFACT: ID `11137599218`.
- VERIFIED SCOPE: assets 058, 060, 192, 401–410, 412, 415–417 and 490 are promoted to verified/integrated in the first slice. Assets 059, 061, 411, 413 and 414 remain produced/deferred until a legitimate runtime binding exists.
- MODAL FOLLOW-UP: Batch 005 asset 419 `UI_MODAL_FRAME` is now produced and applied to the existing Character equipment-detail Dialog rather than a placeholder surface.
- MODAL VERIFIED HEAD: `c55b4449b3449b7cd9ad3be22a3b52511d82657b`.
- MODAL VERIFIED GATE: Android Pixel Client run 244 / ID `36807746344` completed successfully: Python 308/308; Android unit tests passed; Compose instrumentation tests compiled; debug APK assembly/package verification passed; API 35 x86_64 emulator completed 27/27 connected tests with 0 failures; UI screenshot set verified/uploaded.
- MODAL APK SHA-256: `dc3637989bb67dcabdb143a07e1e40689039a4d7e627e8734d1c2cc9608f4859`.
- MODAL UI-QA ARTIFACT: ID `11138368083`.
- NEXT: continue only with safe documented UI/accessibility assets that have a real typed client surface; keep canonical character/NPC geometry and unbound combat/toast/feedback art blocked rather than fabricated.
- COMPLETED_AT: —


## Known technical follow-ups

These are not part of the Android black-screen fix unless directly implicated:

- canonical implementation-branch selection/promotion;
- seven-versus-eight stat decision with explicit migration if changed;
- `GameState.snapshot()` shallow-container contract;
- large-module extraction;
- direct subsystem mutation unification;
- platform/runtime coverage beyond Python 3.12/Linux;
- final release/build governance.

## Verification discipline

For engine behavior changes:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

For Android changes, also verify the Android build/startup path. Python tests cannot prove Android startup.

Before ending meaningful work, update:
- current objective;
- exact branch/HEAD;
- files changed;
- tests/commands actually run;
- observed results;
- blockers/unknowns;
- next action;
- task status and `COMPLETED_AT` if genuinely done.

## Character / Stats continuation — 2026-09-30

### TASK P-005 — Responsive Character loadout and selected Stats detail
- STATUS: `IN_PROGRESS`
- BRANCH: `feature/character-stats-inspection`
- BASE: `feature/character-equipment-paperdoll-ui@40c95ec2e2b44aeb6a8ae1a23c28bbaf04e7a6d7` (PR #12), retaining PR #11 inspection and PR #10 rig-contract ancestry. PR #13 preserves concurrent screenshot-export fixes at `746e2152d617e4150f92d9fb604fbb1d3643d757`.
- IMPLEMENTED: phone-width equipment slots surrounding the existing paper doll; selectable equipment detail with engine-owned equip/unequip; compact Stats summary, canonical attribute cards and one selected detail; player-safe attribute/skill contributions with existing hidden-source redaction.
- REGRESSION COVERAGE: canonical values and bonuses, save/load, cancellation, detached projections and hidden perk/condition provenance; JVM mapper/formatting checks; phone/large-text Compose interactions; real Activity equip -> Stats -> unequip.
- LOCAL VERIFICATION: `PYTHONPATH=src python -m unittest discover -s tests -v` — 308/308 passed after consolidation; `git diff --check` passed. Four new Python tests were observed failing before implementation.
- PREDECESSOR GATE: run 222 / `36793210191` at `ad856cfc792e19e844a8fa49159bacb34b56114f` passed Python 305/305, Android unit/compile/assemble and 22/22 emulator tests, but failed screenshot retrieval after testing.
- REQUIRED GATE: fresh consolidated exact-head Android unit/compile/assemble/package and API 35 emulator workflow; inspect emitted UI screenshots before recording verification.
- LIMITATIONS: no local Android SDK/Gradle or physical Galaxy A03 runtime available; no new canonical character geometry, held-reader binding, stat migration or save migration.
- HANDOFF: `docs/CHARACTER_STATS_INSPECTION_HANDOFF.md`.
- COMPLETED_AT: —

### Live PR evidence recovered
- PR #7: `a3970de6597c77939afccb5f30d6040bdf3d608d`, run 209 / `36773072464`, success.
- PR #8: `54a40bb5ad0aeafb428d128be7c1465f3d1a759b`, run 211 / `36773224465`, success; 058–061 remain deferred from runtime scene integration.
- PR #9: `063d5879413b81656cc5c7304be0afd02402f2fd`, run 217 / `36778591342`, success: Python 301/301, Android gates, emulator 15/15. Diagnostic reader remains PRODUCED / VERIFIED / DEFERRED INTEGRATION. Current-head APK SHA-256: `9d113494e413e44a36bba13a724b4197e33e627a3154aa793a283ec0052a905c`.
- PR #10: runtime `5097011f2cb15511e9695edc5475f2fd69c5f655`, run 215 / `36778523620`, success: Python 301/301, Android gates, emulator 16/16. Later documentation HEAD `7d4558ea5c9e3ad24bf29fe42c8f199ed0be60fe`, run 218 / `36791439179`, also completed successfully.
- PR #9/#10 Actions checked out temporary merge commits; their complete Git trees were compared with their implementation heads and matched exactly. See handoff and PR descriptions for tree/hash evidence.

## Immediate next action

Finish P-005 in PR #13 stacked above PR #12, preserving PR #11 inspection and PR #10 rig-contract dependencies and keep the validation head stable while CI runs. Inspect the real screenshots, repair any observed UI/CI defects, then record exact implementation evidence. Do not merge main or force held-reader/environment integration.

Historical asset continuation guidance (superseded by the live evidence above):

Continue `feature/pixel-asset-wave-a` through draft PR #7 using small verified slices. Assets 039, 040, 044, 053, 062/063, 072–075 and 096–100 are green and evidenced. Candidate assets 067–071 are implemented as reusable presentation-only infrastructure props and now require an exact-head gate. Do not block implementation on rejected mixed character references. Physical Galaxy A03 visual QA remains a separate acceptance gate before final visual approval.


## Cross-chat continuity — Gate Twelve visual production

### TASK CTX-001 — Preserve map/art/animation decisions across sessions
- STATUS: `IN_PROGRESS`
- PRIORITY: continuity / safety
- RESULT SO FAR:
  - created `docs/GAME_CONTEXT_LOGS/README.md`;
  - created `docs/GAME_CONTEXT_LOGS/2026-10-01_GATE_TWELVE_MAP_ART_ANIMATION.md`;
  - recorded that authored map geometry is the fixed scaffold and pixel art/animation must adapt to it;
  - recorded separation between this repository's engineering continuity and the separate private-RPG state/session hierarchy;
  - recorded standing permission for conservative reversible safety decisions while preserving approval boundaries for destructive/irreversible/external actions.
- RELATED: PR #29 documentation line.
- RUNTIME IMPACT: none; documentation/continuity only.
- VERIFICATION: repository files were created on `docs/gate-twelve-map-pixel-asset-blueprint`; runtime animation remains unimplemented and unverified.
- NEXT: inspect the exact animation rendering path and start the smallest reversible Service Tunnel ambient slice only after confirming no existing asset/overlay duplicates it.
- COMPLETED_AT: —

## 2026-10-02 DOCUMENTATION EXPANSION BATCH

Renumbering note: these continuation tasks were reassigned to D-034–D-043 on 2026-10-02 to eliminate collisions with earlier canonical D-013–D-022 task IDs. Task meaning/evidence was preserved.

### TASK D-034 — Decompose expanded owner directive
- STATUS: `DONE`
- PRIORITY: `P0`
- OUTPUT: `docs/MASTER_DIRECTIVE_EXECUTION_BREAKDOWN.md`
- RESULT: documentation/world/system/visual/APK work split into ordered migration-gated phases.

### TASK D-035 — Create rework decision matrix
- STATUS: `DONE`
- PRIORITY: `P0`
- OUTPUT: `docs/EXISTING_STATE_REWORK_DECISION_MATRIX.md`
- NOTE: high-level matrix complete; deep per-file audit remains TASK D-006.

### TASK D-036 — Create pixel art production/reuse ledger
- STATUS: `DONE`
- PRIORITY: `P0`
- OUTPUT: `docs/assets/PIXEL_ART_PRODUCTION_AND_REUSE_LEDGER.md`
- RESULT: actor/panel/overlay/reuse rules and Gate Twelve production packet needs recorded.

### TASK D-037 — Create world-scale coordinate/schema blueprint
- STATUS: `DONE`
- PRIORITY: `P0`
- OUTPUT: `docs/world/WORLD_SCALE_DOCUMENTATION_BLUEPRINT.md`
- RESULT: schema-first world hierarchy recorded; mass world generation remains gated.

### TASK D-038 — Create gameplay rebuild matrix
- STATUS: `DONE`
- PRIORITY: `P0`
- OUTPUT: `docs/systems/GAMEPLAY_SYSTEM_REBUILD_MATRIX.md`
- RESULT: current systems and target stats/skills/classes/ranks/social/combat/adversary systems classified.

### TASK D-039 — Create final APK reconstruction matrix
- STATUS: `DONE`
- PRIORITY: `P0 / LATE-STAGE AUTHORITY`
- OUTPUT: `docs/android/APK_FINAL_RECONSTRUCTION_MATRIX.md`
- RESULT: final screen/component keep/rework/replace/remove sequence documented; execution remains blocked.

### TASK D-040 — Track requested documentation scale
- STATUS: `DONE`
- PRIORITY: `P0`
- OUTPUT: `docs/DOCUMENTATION_PROGRESS_LEDGER.md`
- RESULT: numeric targets preserved without inventing units; reproducible count audit still pending.

### TASK D-041 — Finish Gate Twelve Step 8–14
- STATUS: `DONE`
- PRIORITY: `P0`
- CURRENT: Duplicate tracker reconciled with completed TASK D-005; Steps 1–14 first-pass contract exists. Runtime acceptance remains separate.
- COMPLETED_AT: `2026-10-02 08:01 AST` (existing D-005 evidence).

### TASK D-042 — Deep source-file existing-state audit
- STATUS: `IN_PROGRESS / CURRENT-HEAD PATH AND RESPONSIBILITY INVENTORY COMPLETE`
- PRIORITY: `P0`
- DOCUMENT: `docs/DEEP_SOURCE_EXISTING_STATE_AUDIT_2026-10-04.md`
- AUDITED_HEAD: `docs/master-game-development-program@d0382aaf6cca2920a7f315d08153ac6b0dddc5dd`
- COMPLETED CURRENT-HEAD SLICE:
  - exact Python engine module inventory and disposition;
  - exact Android runtime/application source inventory and grouped disposition;
  - vertical-slice/sample content counts;
  - exact durable GameState fields and save schema v1 boundary;
  - exact 24-raster runtime inventory;
  - exact Python/Android test-source inventory;
  - workflow/build configuration inventory.
- REMAINING: cross-branch consumer/survivor/deprecation reconciliation and exact runtime execution evidence are outside this current-head path slice and remain under D-006/D-020/D-021/D-026/D-029/D-044.
- RELATED: TASK D-006.

## Operational continuation — 2026-10-02 15:06 AST

### TASK D-043 — Baseline documentation/raster evidence and execution contracts
- STATUS: `DONE` (documentation deliverables; remote publication checked separately).
- PRIORITY: `P0`
- BASELINE: `4d596bcd27b6e2f8ef9ce3a93b9dab22f5f4812e`.
- OUTPUT: decision/rebuild register; complete baseline Markdown catalog + JSON; raster delivery ledger + JSON; exact Gate Twelve map evidence; world canon queue; room composition contract; directive context log.
- VERIFIED OBSERVATIONS: 76 baseline Markdown files / 123,707 words; 24 raster bindings; nine map nodes / eight edge records; fixed opening-actor lookup; preferred raster precedence.
- VERIFICATION: `git diff --check` passed; JSON assertions passed for all 76 document records/123,707 words, 24 bound PNGs and nine nodes/eight edge records; local Markdown links in changed documents resolved.
- TESTS: no runtime files changed; Python/Android runtime tests were not rerun for this documentation-only batch.
- COMPLETED_AT: `2026-10-02 15:06 AST`.
- NOT COMPLETE: D-006/D-042 full branch reconciliation, art approval, proposed actor projection, world-scale population, final APK, physical Galaxy A03 QA.
- NEXT: reconcile source/raster revisions and implementation branch ancestry; author Gate Twelve parent-world proposal and bounded area packets.


## 2026-10-02 final reconstruction integration update

### TASK D-027 — Final game reconstruction integration blueprint
- STATUS: `DONE`
- PRIORITY: `P0`
- DOCUMENT: `docs/FINAL_GAME_RECONSTRUCTION_BLUEPRINT.md`
- RESULT: cross-domain authority now connects change decisions, asset creation/stages/reuse, room actors/panels, world canon gaps, mechanics migration depth and final APK teardown/rebuild sequencing.
- COMPLETED_AT: `2026-10-02 AST`

### TASK D-028 — Reconcile implementation PR #7–#31
- STATUS: `DONE`
- PRIORITY: `P0`
- OUTPUT: `docs/IMPLEMENTATION_PR_7_31_RECONCILIATION_2026-10-02.md`.
- RESULT: PR #7–#31 exact heads/bases, ancestry versus the master documentation branch, workflow evidence, divergent survivor branches, conflict state and migration order recorded. Divergence does not equal rejection and ancestry does not equal promotion to `main`.
- COMPLETED_AT: `2026-10-02 AST`.

### TASK D-029 — Exactize asset provenance and production stage
- STATUS: `IN_PROGRESS`
- PRIORITY: `P0`
- OUTPUT: source master -> raster/export -> branch/head -> runtime consumer -> reuse signature -> QA -> canonical state for every current asset family.
- CURRENT FAMILY SLICE:
  - `docs/assets/ASSET_FAMILY_PROVENANCE_INDEX_2026-10-03.md`
  - `docs/assets/CHARACTER_EQUIPMENT_ITEM_ACTOR_PROVENANCE_2026-10-03.md`
  - `docs/assets/ENVIRONMENT_SCENE_MAP_PROVENANCE_2026-10-03.md`
  - `docs/assets/UI_FX_ANIMATION_PROVENANCE_2026-10-03.md`
- VERIFIED: current program-branch families are separated into PNG-preferred raster-bound assets versus procedural Kotlin code masters; runtime consumers and dedicated QA sources are mapped; PR #22 tail is reference/docs-only relative to its inherited ancestor; PR #9 held-prop and PR #31 ambient animation remain non-integrated candidates; PR #27/#28/#30 static refinements remain candidate/survivor work rather than current authority. PR #8's three 128x64 modules are now confirmed as exact Map arrival-preview integrations, while `MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS` remains `DEFERRED_INTEGRATION` because no main-UI consumer was found.
- PREVIOUS EXACT SLICE: `docs/assets/SOURCE_RASTER_RECONCILIATION_2026-10-02.md` owns the inherited nine-scene PNG baseline and divergent Service Tunnel/Quiet Stair source+raster evidence.
- REMAINING: execute the deterministic raster verifier/exporter once an exact-checkout execution environment is available and persist the result; repair/document any pixel mismatch; owner visual promotion decision for PR #27 Service Tunnel and PR #30 Quiet Stair; final Jack/portrait production; owner/canon approval; destination-head visual QA and physical-device QA. Current blocker: PR #33 / `docs/master-game-development-program` has no observed Actions run, no Codex environment is registered, and direct local checkout is network-blocked.
- EXACT RASTER LINEAGE: `docs/assets/RASTER_EXPORT_AND_SOURCE_CORRESPONDENCE_2026-10-03.md` + `docs/evidence/raster_export_lineage_2026-10-03.json` now map all 24 current PNGs to source files/revisions and exact export/refresh commits. Result: 17 initial-export rasters remain current; 7 were source-revised then raster-refreshed. PR #22's five player/loadout refreshes and the Platform Nine/Relay Workbench paired refinements are inherited current ancestry. The historical PR #19 exporter remains not persisted/found. A new repository-owned deterministic verifier/reconstruction exporter now exists, but fresh pixel-equality reproduction remains open until it executes and the output is inspected.
- RASTER RECONSTRUCTION TOOLING: `tools/verify_pixel_raster_equivalence.py` plus `tests/test_pixel_raster_equivalence_tool.py` encode source parsing, PNG decoding, identity/lineage checks, 24-asset pixel comparison, deterministic separate-tree PNG reconstruction and repository-root overwrite refusal. Test coverage rejects parent traversal, absolute paths, duplicate binding paths, duplicate asset symbols and duplicate resource names. `docs/evidence/raster_equivalence_verifier_status_2026-10-03.json` records `IMPLEMENTED_HARDENED_EXECUTION_BLOCKED_BY_ENVIRONMENT`. Two qualifying test commits—`e8b85b398b1069c2ae3353d3dbeb9c952538c6d6` through Git Data/ref update and `d42d3e5a258cac150795c41059d2c635caf5789e` through the normal Contents API—both produced zero PR/branch Actions runs or combined statuses. The missing run is therefore not specific to the earlier ref-update publishing method, and no current pixel-equality pass is claimed.
- PR #8 MODULE LINEAGE: exact catalog comparison found all four Wave-L module/atlas visual definitions preserved in the current catalog; current source only adds later player-safe arrival-preview mappings. PR #8 remains historical provenance, but no separate unique-geometry migration is required.
- PR #28 COMPOSITION: exact diff shows no new environment asset geometry; the branch reuses the existing municipal infrastructure atlas as Service Tunnel arrival-preview detail. Treat as optional composition behavior, not a competing source-master asset.
- INFRASTRUCTURE ATLAS DECISION: keep `MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS` as `PRODUCED_DEFERRED_INTEGRATION`; PR #28 supplies a legitimate presentation-only Service Tunnel arrival-preview consumer by reusing the existing atlas without new geometry. Future adoption should selectively reimplement that composition after visual/material review rather than merge the divergent branch.
- STATIC SURVIVOR TOPOLOGY: resolved technically. PR #30 is stacked on PR #27 and adds Quiet Stair only; it does not create a second Service Tunnel refinement. Remaining promotion choices are current baseline vs PR #27 for Service Tunnel and current baseline vs PR #30 for Quiet Stair. Both refined candidates remain `OWNER DECISION REQUIRED` for visual/canon promotion.
- PR #9 HELD-PROP OWNERSHIP: resolved as Tamsin actor-presentation art under D-030's player-safe pose/visual-family boundary. The 32x48 held master is not a player inventory/equipment asset; runtime remains `DEFERRED_INTEGRATION` until D-030 actor projection and verified Tamsin hand/wrist anchors exist. The 32x32 icon has no authorized current inventory consumer.
- PR #31 AMBIENT DECISION: `docs/assets/SERVICE_TUNNEL_AMBIENT_ANIMATION_MIGRATION_CONTRACT_2026-10-03.md` classifies PR #31 as `VERIFIED_BRANCH_EVIDENCE + DEFERRED_INTEGRATION + REIMPLEMENT_ON_SELECTED_STATIC_PARENT`. Track IDs/timing/bounds are preserved; reduced motion is Android presentation/accessibility state, not gameplay authority. Migration strategy is documented; actual reduced-motion/animation runtime implementation and destination-head QA remain future implementation work.
- LATEST_SLICE_BASELINE: `docs/master-game-development-program@58a61eb202bbb9443e01f8689e18e8ef0e99d3c7`; no runtime/content files changed from prior D-029 baseline `2ad50d7...` to this baseline.
- LATEST_SLICE_AT: `2026-10-03 AST`.
- COMPLETENESS: partial reconstruction-grade family coverage; D-029 is not complete.

### TASK D-030 — Player-safe actor/panel projection contract
- STATUS: `DONE (DOCUMENTED) / IMPLEMENTATION PENDING`
- PRIORITY: `P0`
- OUTPUT: `docs/android/PLAYER_SAFE_ROOM_ACTOR_PROJECTION_CONTRACT.md`.
- VERIFIED BASELINE: durable `state.npcs` exists, Android bridge has no room actor projection, Kotlin `GameSnapshot` has no room actor model, and `PixelStoryActorCatalog.placements(locationId, sceneId)` still owns current opening actor presence.
- RESULT: versioned player-safe `room` projection, redaction boundary, support-actor handling, semantic placement keys, Kotlin target types, mapper validation, opening-story equivalence fixtures, panel-selection lifecycle, save boundary and test gates are specified.
- RUNTIME: not implemented by this documentation task; existing scene/location actor heuristic remains active until a later bounded code slice passes equivalence/CI gates.

### TASK D-031 — Gate Twelve parent-world canon packet
- STATUS: `PROPOSAL_READY / OWNER_CANON_DECISION_REQUIRED`
- PRIORITY: `P0`
- OUTPUT: `docs/world/GATE_TWELVE_PARENT_WORLD_PROPOSAL.md`.
- RESULT: a bounded original parent settlement/region/municipal/route/terrain-climate proposal exists without changing local IDs, local route data, W3 coordinates or higher sovereign canon. Working names remain non-canon until accepted/revised.

### TASK D-032 — Mechanics schema/API migration packets
- STATUS: `PENDING`
- PRIORITY: `P0/P1`
- OUTPUT: progression/social/items/combat/adversary target schemas mapped to existing engine APIs, saves, projections and tests.

### TASK D-033 — APK teardown manifest
- STATUS: `BLOCKED`
- PRIORITY: `LATE-STAGE`
- BLOCKED_BY: D-020/D-026/D-028/D-030/D-032 and final domain contracts.
- OUTPUT: component-level keep/rework/replace/remove map with zero-consumer evidence before deletion.


### TASK D-044 — Reconcile PR #33 moving base
- STATUS: `IN_PROGRESS / SHARED-FILE RECONCILIATION COMPLETE / CLASS-C EXTRACTION REMAINS`
- PRIORITY: `P0`
- OUTPUTS:
  - `docs/PR33_MOVING_BASE_DRIFT_RECONCILIATION_2026-10-02.md`
  - `docs/BASE_BRANCH_DOCUMENT_CROSSWALK_2026-10-02.md`
  - `docs/PR33_LIVE_SHARED_FILE_RECONCILIATION_2026-10-03.md`
- VERIFIED: live ref audit resolved `docs/master-game-development-program@ab7c041d6916b2e37b75430523a2183f9483883b` and `docs/settlement-region-build-plan@65d2db8538c1b8302c314f2fbe9eb7a1b585b51d`; they remain diverged from merge base `c261b2aaf8bd978d27b46f8fea03435c0c5734d0` with 210 program-side commits and 99 target-side commits at that audit.
- SHARED FILE RESULT: `AGENTS.md`, `README.md`, `docs/IMPLEMENTATION_STATUS.md`, and `docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md` are `KEEP PROGRAM`. No whole-file migration or parallel active authority is required. Target Gate Twelve's GT-IMP-001 requirements are preserved by the current Gate Twelve plan and dedicated D-030 actor-projection contract.
- DECISION: no blind merge/rebase. Preserve current program authority, block the conflicting “2,000,000 separate files” interpretation, and migrate only unique non-conflicting children.
- MIGRATED CHILDREN:
  - `docs/assets/GLOBAL_ASSET_REUSE_OCCLUSION_MATRIX.md`
  - `docs/world/WORLD_ENTITY_ID_AND_REFERENCE_STANDARD.md`
  - `docs/world/REGION_SETTLEMENT_DOCUMENTATION_TEMPLATE.md`
  - `docs/world/GATE_TWELVE_EXTERNAL_CONNECTIONS_AND_EXPANSION_REGISTER.md`
- REMAINS: inspect remaining live target Class C / `EXTRACT UNIQUE` documents for genuinely absent requirements; keep unit-dependent corpus machinery blocked; then re-resolve both branch refs and reassess PR mergeability/target-branch handling.


## 2026-10-03 evolved-game design continuation

### TASK D-045 — Create evolved game through reconstruction-grade domain documentation
- STATUS: `IN_PROGRESS`
- PRIORITY: `P0`
- OWNER INTENT: use the current Text-rpg-game as the reference game, preserve its identity, and deliberately design a larger/upgraded version through documentation before broad implementation.
- FIRST DOMAIN: progression / classes / ranks.
- CURRENT OUTPUT: `docs/systems/PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md`.
- CURRENT RESULT: current progression/runtime facts are separated from target design; class/profession/rank/training/world-integration direction and creation requirements are documented.
- ART RULE: final character presentation uses authored pixel-art sprites/portraits generated through the project workflow; no geometry-built final character art.
- MATERIALIZED CHILD: `docs/systems/EVOLVED_SKILL_REGISTRY.md` — all 23 current skills expanded into target-game records covering training, world/tactical uses, class/profession relationships, advanced gates, content and pixel-art requirements.
- NEXT: create the combat class catalog, then profession/rank/status packet, training/mentor/facility standard, Gate Twelve proof packet and progression UX contract.
- IMPLEMENTATION: deferred until design contracts are sufficiently coherent.


### TASK D-046 — Build Status UI / ability / passive reconstruction corpus
- STATUS: `IN_PROGRESS / PHASE A COMPLETE / WAVE 001 STRUCTURALLY COMPLETE / PHASE C REFINEMENT ACTIVE`
- PRIORITY: `P0`
- PARENT: D-045 evolved-game design continuation.
- OWNER INTENT: devote substantial reconstruction-grade documentation to primary abilities, passive abilities, hidden requirements, rarity, discovery, evolution, knowledge, mapping, and related world/content systems.
- MASTER: `docs/systems/STATUS_UI_ABILITIES_AND_PASSIVES_MASTER_PLAN.md`.
- INDEX: `docs/systems/status/README.md`.
- VERIFIED DOCUMENTATION MILESTONES:
  - governing Status/ability/passive standards and authoring guides are materialized; Phase A is complete for the current design-authority layer;
  - Wave 001 structurally contains 1,019 records: 47 primary abilities, 230 passives, 188 techniques, 230 passive unlock paths, 230 passive knowledge profiles, 47 awakening profiles and 47 counter profiles;
  - structural audit reports 1,019 unique IDs, zero duplicate IDs and zero dangling parent references in the audited Wave-001 record classes;
  - primary-ability rarity-slice deep-authoring packet coverage is 47 / 47 identities;
  - passive Phase-C family baseline coverage is 23 / 23 families;
  - conceptual passive record owner/write-target mapping covers 230 / 230 passive IDs.
- CURRENT PHASE: reconstruction-grade Phase C refinement, blocker resolution, world evidence integration, normalization and canon-review preparation.
- REMAINING:
  - parent-system range/test fixtures and justified numeric envelopes;
  - evidence-backed world/knowledge integration where current world canon supports it;
  - unresolved state-owner/runtime projection mappings;
  - record-by-record canon review and owner approval;
  - Phase D world integration, Phase E canon promotion and Phase F implementation mapping.
- IMPORTANT: older NEXT text naming rarity/schema/requirement/visibility/Level/awakening standards is superseded because those files now exist.
- IMPLEMENTATION: deferred; current task remains documentation/design authority.
