# THE GAME — Repository Master Task Register

Updated: 2026-09-30 21:21 AST
Timezone: America/Puerto_Rico (AST, UTC-4)  
Status: `PENDING` / `IN_PROGRESS` / `BLOCKED` / `DONE`

This is the repository-native operational index for future coding agents. It intentionally stays concise. Repository source files and fresh execution evidence outrank this document if they conflict.

## Authority / read order

1. Current repository files and exact branch/HEAD.
2. Fresh build/test/runtime evidence.
3. This task register.
4. `docs/IMPLEMENTATION_STATUS.md`.
5. `docs/V6_STABILIZATION_HANDOFF.md`.
6. Chat memory / historical summaries.

Do not mark a task `DONE` without evidence. Every `DONE` task must record `COMPLETED_AT` in America/Puerto_Rico time. Unknown historical times use `NOT_RECORDED`.

## Current repository baseline

- Repository: `jbob-coder/Text-rpg-game`
- Current verified Android UI/APK candidate: `fix/player-hub-runtime-recovery@f88453c38b8efd91a4af74b3cd4f59b6903a9a03` (PR #15), run 233 / `36799678887`; runtime evidence in `docs/verification/character_stats/apk_delivery.json`.
- Current Android integration branch: `integration/android-open-world-v1-reconcile`
- Verified pixel-asset baseline: `feature/pixel-asset-wave-a@a3970de6597c77939afccb5f30d6040bdf3d608d` (PR #7), run 209 / `36773072464` passed; earlier `1c7e54e…` is historical.
- Stabilization branch retained: `fix/v6-runtime-boundaries`
- Stabilization baseline before continuity work: `fcfe8115a72eb07036fa4e74a61a0094eaa3ff10`
- V6 parent: `integration/rules-ability-v6-reconcile@7f5f104fb839068bdfaf5cec72f37129ae20d463`
- `main`: placeholder; do not treat it as the canonical implementation.
- Untouched V6 recorded execution: 258 tests, 245 passed, 1 failed, 12 errors.
- Repaired candidate recorded execution: 275 tests, 0 failures/errors/skips on CPython 3.12.14/Linux.
- Verified base-client content record at Android HEAD: 16 scenes, 25 choices, 3 quests, 1 power definition.
- Android runtime evidence: workflow run 65 / run ID 36351957867; Python 290/290 OK; Android build/compile gates OK; representative emulator API 35 x86_64 completed 3 tests successfully.
- APK SHA-256 for exact Android HEAD: `94e325d55c5dd1404dbab8d0209dbfe1f8c0c29c5abecfdd582736851da4cd74`.
- Current APK delivery is complete (A-002/A-004); physical handset validation remains a separate acceptance gate.
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
- STATUS: `DONE`
- DEPENDS_ON: A-001
- VERIFIED: debug APK builds from repository source; package structure checks pass for ARM64, ARMv7, x86_64 and bundled content. Exact SHA-256 at `510851cc…`: `94e325d55c5dd1404dbab8d0209dbfe1f8c0c29c5abecfdd582736851da4cd74`.
- DELIVERED: the current debug APK at `f88453c…`, workflow run 233, was downloaded, verified against the CI SHA-256, checked for complete ZIP/ABI/content payload and saved for user download; APK Signature Scheme v2 verified in CI. Hash: `8decee3cb660015e8b048a495509a8856673023bdc2c9f99d4200148ef243fe3`. Physical handset installation remains separate.
- DONE WHEN: package builds, integrity/signing is checked, and artifact is delivered.
- COMPLETED_AT: `2026-09-30 21:21 AST`

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

### TASK P-006 — Dedicated Skills screen
- STATUS: `IN_PROGRESS`
- IMPLEMENTED CANDIDATE: a schema-driven player-safe Skills surface is reachable from `More` without adding another primary Galaxy-A03 bottom-navigation tab. Skills are grouped from projected categories, future learned skills appear automatically, and selecting a skill reuses the authoritative stat-inspection boundary for base/modifier contributions.
- BOUNDARY: no skill formulas or progression rules are duplicated in Compose; only projected skill state and sanitized inspection data are rendered.
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

### Dedicated player-safe Skills UI slice
- STATUS: `IN_PROGRESS`
- BRANCH: `feature/player-safe-skills-ui`
- PARENT: `feature/character-equipment-paperdoll-ui@b324dd555922a13f0672752f005d74fff68a09aa`.
- OBJECTIVE: deliver the missing Skills product surface without crowding the phone bottom bar or hard-coding the four starting skills.
- IMPLEMENTED CANDIDATE:
  - `Skills` is a secondary section opened from `More`, while the primary bottom navigation remains Story / Character / Stats / Inventory / Quests / Map / More;
  - the redundant Character shortcut was removed from `More` because Character already has a primary bottom tab;
  - rendered skills come from `snapshot.skills`, grouped and sorted by projected category/name;
  - selecting a skill requests `skills.<id>` through the already-verified player-safe inspection boundary;
  - equipment/perk/condition contributions render from sanitized provenance rather than UI-side modifier arithmetic;
  - future learned skills appear automatically when the player-safe projection contains them.
- TESTS ADDED: More -> Skills navigation/Technical Systems inspection request and rendering the Work Gloves `equipment:hands +1` contribution.
- EXACT-HEAD GATE: pending.
- NEXT: verify the stacked Character gate, then run exact-head Python + Android + emulator gates for this Skills slice.

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
- STATUS: `DONE`
- BRANCH: `feature/character-stats-inspection`
- BASE: `feature/character-equipment-paperdoll-ui@40c95ec2e2b44aeb6a8ae1a23c28bbaf04e7a6d7` (PR #12), retaining PR #11 inspection and PR #10 rig-contract ancestry. PR #13 preserves concurrent screenshot-export fixes at `746e2152d617e4150f92d9fb604fbb1d3643d757`.
- IMPLEMENTED: phone-width equipment slots surrounding the existing paper doll; selectable equipment detail with engine-owned equip/unequip; compact Stats summary, canonical attribute cards and one selected detail; player-safe attribute/skill contributions with existing hidden-source redaction.
- REGRESSION COVERAGE: canonical values and bonuses, save/load, cancellation, detached projections and hidden perk/condition provenance; JVM mapper/formatting checks; phone/large-text Compose interactions; real Activity equip -> Stats -> unequip.
- LOCAL VERIFICATION: `PYTHONPATH=src python -m unittest discover -s tests -v` — 308/308 passed after consolidation; `git diff --check` passed. Four new Python tests were observed failing before implementation.
- PREDECESSOR GATE: run 222 / `36793210191` at `ad856cfc792e19e844a8fa49159bacb34b56114f` passed Python 305/305, Android unit/compile/assemble and 22/22 emulator tests, but failed screenshot retrieval after testing.
- VERIFIED GATE: initial consolidation run 229 passed at `0fe6a9f…` with 26/26 connected tests. Visual/recovery follow-up at `f88453c…` passed run 233 / `36799678887`: Python 308/308, Android unit/compile/assembly/signature/payload gates, 30/30 connected tests and four inspected PNGs. Source and tested-merge trees match exactly. APK delivered; see `docs/ANDROID_APK_DESKTOP_HANDOFF.md`.
- LIMITATIONS: no local Android SDK/Gradle or physical Galaxy A03 runtime available; no new canonical character geometry, held-reader binding, stat migration or save migration.
- HANDOFF: `docs/CHARACTER_STATS_INSPECTION_HANDOFF.md`.
- COMPLETED_AT: `2026-09-30 21:21 AST`

### Live PR evidence recovered
- PR #7: `a3970de6597c77939afccb5f30d6040bdf3d608d`, run 209 / `36773072464`, success.
- PR #8: `54a40bb5ad0aeafb428d128be7c1465f3d1a759b`, run 211 / `36773224465`, success; 058–061 remain deferred from runtime scene integration.
- PR #9: `063d5879413b81656cc5c7304be0afd02402f2fd`, run 217 / `36778591342`, success: Python 301/301, Android gates, emulator 15/15. Diagnostic reader remains PRODUCED / VERIFIED / DEFERRED INTEGRATION. Current-head APK SHA-256: `9d113494e413e44a36bba13a724b4197e33e627a3154aa793a283ec0052a905c`.
- PR #10: runtime `5097011f2cb15511e9695edc5475f2fd69c5f655`, run 215 / `36778523620`, success: Python 301/301, Android gates, emulator 16/16. Later documentation HEAD `7d4558ea5c9e3ad24bf29fe42c8f199ed0be60fe`, run 218 / `36791439179`, also completed successfully.
- PR #9/#10 Actions checked out temporary merge commits; their complete Git trees were compared with their implementation heads and matched exactly. See handoff and PR descriptions for tree/hash evidence.

## Immediate next action

P-005 and APK delivery are complete at the verified PR #15 runtime `f88453c…`, retaining the PR #10–#14 dependencies. Follow `docs/ANDROID_APK_DESKTOP_HANDOFF.md` for computer checkout/build commands and physical Galaxy A03 acceptance. Keep current deferred assets and canonical-reference blockers explicit. Do not merge main or force held-reader/environment integration.

Historical asset continuation guidance (superseded by the live evidence above):

Continue `feature/pixel-asset-wave-a` through draft PR #7 using small verified slices. Assets 039, 040, 044, 053, 062/063, 072–075 and 096–100 are green and evidenced. Candidate assets 067–071 are implemented as reusable presentation-only infrastructure props and now require an exact-head gate. Do not block implementation on rejected mixed character references. Physical Galaxy A03 visual QA remains a separate acceptance gate before final visual approval.


## APK delivery / recovery continuation — 2026-09-30

### TASK A-004 — Deliver the Character/Stats Android candidate
- STATUS: `DONE`
- BRANCH: `fix/player-hub-runtime-recovery`, PR #15; based on PR #13 and consolidating PR #14 Skills source/tests.
- USER REQUEST: finish the outstanding work, supply the Android APK, review rendered screens and leave an actionable desktop branch handoff.
- OBSERVED BASELINE: run 229 / `36795598719` at PR #13 `0fe6a9f58601c00957ab5ccc4355f57e603e7534` passed all gates and 26 emulator tests; screenshot review found oversized equipment details and awkward accessory labels.
- OBSERVED REGRESSIONS: run 230 / `36797063299` at PR #15 `9b9c7d9c8ea7fdd7a541e3a25b75174a8b0d2fac` passed Python/build but had 5 emulator failures. That commit contains regression tests without their runtime fixes.
- IMPLEMENTED CANDIDATE: preserve playable snapshot after runtime load failures and show the public error inside the game; integrate the Skills surface with the existing inspection API; wrap/cap equipment dialogs, shorten accessory display labels while keeping full semantic labels; capture screenshots against the actual dark application background.
- VERIFICATION: run 233 / `36799678887` passed at `f88453c…`: 308 Python tests, Android unit/compile/assembly/signature/ABI/content gates, 30 connected tests and four reviewed screenshots. Local Python 308/308 and `git diff --check` passed. APK downloaded/hash-verified and saved for user download. No canonical stats, authored bonuses, save schema, novel material or character-overlay geometry changed.
- DELIVERY EVIDENCE: `docs/verification/character_stats/apk_delivery.json`; APK SHA-256 `8decee3cb660015e8b048a495509a8856673023bdc2c9f99d4200148ef243fe3`; complete tested/source Git trees both `f238a2e20665695ea2ed9a959251fbbf3c2962a9`.
- APK retention: one day in Actions; only manual runs and this explicitly requested PR #15 delivery upload the APK. No release or store publication.
- REMAINING: physical Galaxy A03 installation, appearance/input/performance/TTS review; canonical player/Tamsin reference and diagnostic-reader integration remain separate.
- COMPLETED_AT: `2026-09-30 21:21 AST`
