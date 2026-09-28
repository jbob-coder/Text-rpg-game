# THE GAME — Repository Master Task Register

Updated: 2026-09-27 21:40 AST  
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
- Current stabilization branch: `fix/v6-runtime-boundaries`
- Current Android working branch: `feature/android-runtime-bootstrap-v1`, based on `fix/v6-runtime-boundaries@7be1adef22a1bf9d4826691e665b7417235f53a5`.
- Stabilization baseline before continuity work: `fcfe8115a72eb07036fa4e74a61a0094eaa3ff10`
- V6 parent: `integration/rules-ability-v6-reconcile@7f5f104fb839068bdfaf5cec72f37129ae20d463`
- `main`: placeholder; do not treat it as the canonical implementation.
- Untouched V6 recorded execution: 258 tests, 245 passed, 1 failed, 12 errors.
- Repaired candidate recorded execution: 275 tests, 0 failures/errors/skips on CPython 3.12.14/Linux.
- Current content record: 16 scenes, 25 choices, 3 quests, 1 power definition.
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

### TASK A-001 — Diagnose Android black screen
- STATUS: `IN_PROGRESS`
- PRIORITY: `P0 / BLOCKING`
- OBSERVED: Jack installed/opened the generated Android test APK and reported a black screen.
- VERIFIED INVESTIGATION (2026-09-27 14:23 AST):
  - the repository at that checkpoint contained no Android project, manifest, Gradle files, NativeActivity source, or persisted wrapper source;
  - the previously generated `THE-GAME-V6-Android-Test.apk` was not available in the runtime or searchable Library/conversation files;
  - unrelated Android/Godot artifacts from other projects were found and explicitly excluded from this diagnosis.
- REPOSITORY-OWNED REPAIR SLICE (2026-09-27 21:40 AST):
  - `feature/android-runtime-bootstrap-v1` adds a reproducible Android project instead of recreating another ephemeral wrapper;
  - the toolchain is pinned to AGP 9.2.1, Gradle 9.4.1, JDK 17, Chaquopy 17.0.0, and Python 3.11;
  - the app packages the existing `src/textrpg` engine and `content/` directly, so Android does not become a second rules engine;
  - the launcher renders a visible boot surface before Python initialization, then exposes catchable startup failures on-screen and through Logcat while redirecting native/Python stdout and stderr for diagnosis;
  - ABI coverage includes `armeabi-v7a`, `arm64-v8a`, and `x86_64`; Python 3.11 was selected specifically to retain 32-bit ARM support;
  - the Python bridge exposes `build_scene_view()` and `build_status_view()` projections, applies choices through the existing engine, and persists schema-1 saves through Android internal storage.
- CURRENT BLOCKER: the new Android source has not yet been assembled or installed in an Android SDK/device environment. The historical black-screen root cause therefore cannot be narrowed beyond the lost/ephemeral wrapper, and the replacement path is not yet runtime-verified.
- REQUIRED CHECKS:
  - execute `./gradlew :app:assembleDebug` from `android/`;
  - inspect APK ABI/native-library and asset packaging;
  - install/launch on a representative Android runtime/device;
  - capture `TextRpgStartup`, `python.stdout`, `python.stderr`, `native.stdout`, `native.stderr`, and `AndroidRuntime` Logcat output;
  - verify visible boot UI, first scene, choice resolution, autosave, relaunch/resume, and visible error handling.
- DONE WHEN: root cause is identified or superseded by the repository-owned path, the replacement package builds, and visible gameplay is confirmed on a representative Android runtime/device.
- COMPLETED_AT: —

### TASK A-002 — Rebuild corrected APK
- STATUS: `PENDING`
- DEPENDS_ON: A-001
- DONE WHEN: package builds, integrity/signing is checked, and artifact is delivered.
- COMPLETED_AT: —

### TASK A-003 — Physical/representative Android validation
- STATUS: `PENDING`
- DEPENDS_ON: A-002
- DONE WHEN: visible startup/gameplay is confirmed; black screen no longer reproduces.
- COMPLETED_AT: —

## UI / UX reconstruction

### TASK U-001 — Primary gameplay layout
- STATUS: `PENDING`
- Character visible; map/scene visible; large narrative area; clear navigation.
- COMPLETED_AT: —

### TASK U-002 — Narrative readability
- STATUS: `PENDING`
- Larger text/container, long-text handling, readable spacing.
- COMPLETED_AT: —

### TASK U-003 — Decision presentation
- STATUS: `PENDING`
- Better cards/modals; choices may have immediate, delayed, hidden, or narrative-only consequences.
- COMPLETED_AT: —

### TASK U-004 — Settings/save separation
- STATUS: `PENDING`
- Top-right Settings with Audio, Narration, Text speed/delay, Controls, Save, Load, Accessibility.
- Saves must not clutter the primary gameplay HUD.
- COMPLETED_AT: —

### TASK U-005 — Developer/cheat panel
- STATUS: `PENDING`
- Separate/hideable developer surface for XP, level, items, quests, stats, teleport, currency, abilities, world flags, time.
- COMPLETED_AT: —

## Character / stats / equipment

### TASK P-001 — Visible avatar
- STATUS: `PENDING`
- Player has a persistent on-screen visual identity.
- COMPLETED_AT: —

### TASK P-002 — Equipment model + visual integration
- STATUS: `PENDING`
- Planned slots: Head, Chest, Hands, Legs, Feet, Main Hand, Off Hand, Ring 1, Ring 2, Neck, Accessory 1, Accessory 2.
- Equipment must affect authoritative state/rules and eventually appearance.
- COMPLETED_AT: —

### TASK P-003 — Dedicated detailed Stats screen
- STATUS: `PENDING`
- Categories: Core, Combat, Resources, Social, Progression, Derived.
- Inspectable base/equipment/passive contributions and gameplay meaning.
- COMPLETED_AT: —

### TASK P-004 — Inventory / Equipment panels
- STATUS: `PENDING`
- Separate from main narrative screen.
- COMPLETED_AT: —

## World / map

### TASK W-001 — Interactive map
- STATUS: `PENDING`
- Start with a maintainable interactive 2D location/world map before heavier 3D.
- COMPLETED_AT: —

### TASK W-002 — City/location graph
- STATUS: `PENDING`
- Locations/interiors/NPC destinations/events represented with stable IDs.
- Example labels are not automatically canon.
- COMPLETED_AT: —

### TASK W-003 — World interaction
- STATUS: `PENDING`
- Movement between locations; NPC visits; optional exploration; location/world-state-triggered events.
- COMPLETED_AT: —

### TASK W-004 — Persistent world events
- STATUS: `PENDING`
- Choices can set flags and produce delayed NPC/world changes and route changes.
- COMPLETED_AT: —

## Quest / narrative

### TASK Q-001 — Main Quest framework
- STATUS: `PENDING`
- Branching main-story progression.
- COMPLETED_AT: —

### TASK Q-002 — Side Quest framework
- STATUS: `PENDING`
- Optional integrated side stories.
- COMPLETED_AT: —

### TASK Q-003 — Optional Quest framework
- STATUS: `PENDING`
- Optional activities not required for main progression.
- COMPLETED_AT: —

### TASK Q-004 — Lore/world narrative exploration
- STATUS: `PENDING`
- Optional discoverable world information.
- COMPLETED_AT: —

### TASK Q-005 — Branching narrative graph
- STATUS: `PENDING`
- Persistent flags, delayed consequences, non-stat consequences, reconvergence and mutually exclusive routes where authored.
- COMPLETED_AT: —

### TASK Q-006 — Canon/context consistency
- STATUS: `PENDING`
- Re-read authoritative project context before expanding story; do not silently import copyrighted/reference story content as canon.
- COMPLETED_AT: —

## Audio / visual presentation

### TASK M-001 — Tap-to-narrate
- STATUS: `PENDING`
- Play/pause/replay; auto-read; speed/text delay; voice selection if supported.
- COMPLETED_AT: —

### TASK M-002 — Scene illustrations
- STATUS: `PENDING`
- Consistent visual storytelling for locations/events/characters.
- COMPLETED_AT: —

### TASK M-003 — Character visual asset pipeline
- STATUS: `PENDING`
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

Resume TASK A-001 on `feature/android-runtime-bootstrap-v1`: assemble the pinned Android project, inspect the generated APK, install it on a representative Android device/runtime, and capture startup Logcat. Do not mark A-001/A-002/A-003 complete or promote the branch until build plus device evidence exists.
