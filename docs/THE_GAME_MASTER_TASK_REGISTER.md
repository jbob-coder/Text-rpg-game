# THE GAME — Repository Master Task Register

Updated: 2026-09-27 17:34 AST  
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
- IMPLEMENTED: authoritative equipment slots, equip/unequip bridge and Android equipment panel. Visual paper-doll integration is being validated in `feature/android-open-world-v1`.
- Planned slots: Head, Chest, Hands, Legs, Feet, Main Hand, Off Hand, Ring 1, Ring 2, Neck, Accessory 1, Accessory 2.
- Equipment must affect authoritative state/rules and eventually appearance.
- COMPLETED_AT: —

### TASK P-003 — Dedicated detailed Stats screen
- STATUS: `IN_PROGRESS`
- IMPLEMENTED: separate Stats surface with resources, attributes, derived stats, skills and conditions from the player-safe projection. Deeper contribution/meaning presentation remains in progress.
- Categories: Core, Combat, Resources, Social, Progression, Derived.
- Inspectable base/equipment/passive contributions and gameplay meaning.
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
- LIMITATION: automated Compose/runtime coverage proves the new catalog renders and does not regress the tested client, but native-scale art review and physical Galaxy A03 visual QA are not yet claimed.
- NEXT: keep player/Tamsin canonical reference selection isolated from implementation. Base coverage is 9/9, the first three player-safe state overlays are integrated, and UI/map assets 076–095 are integrated. Continue with asset 040 `UI_EQUIPMENT_SLOT_ICON_SET` using projected slot IDs only; defer quality-frame behavior (039) until inventory/equipment quality presentation is explicitly defined. Preserve physical Galaxy A03 visual QA as a separate acceptance gate.
- RULE: generated images are reference-only until reconstructed into native pixel masters with manifests and QA.
- DONE WHEN: all 100 Batch 001 units reach their documented integration/deferred-integration acceptance state.
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

## Immediate next action

Continue `feature/pixel-asset-wave-a` through draft PR #7 using small verified slices. Next target: asset 040 `UI_EQUIPMENT_SLOT_ICON_SET`, then reassess remaining Batch 001 props/FX against player-safe state availability. Do not block implementation on rejected mixed character references. Physical Galaxy A03 visual QA remains a separate acceptance gate before final visual approval.
