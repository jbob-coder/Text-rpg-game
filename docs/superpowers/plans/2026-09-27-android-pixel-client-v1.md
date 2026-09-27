# Android Pixel Client V1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a reproducible Android client which boots visibly, embeds the existing authoritative Python RPG engine, renders a coherent pixel-style mobile interface, and replaces the unreproducible wrapper which produced the black-screen APK.

**Architecture:** Kotlin/Jetpack Compose owns Android presentation and lifecycle only. Chaquopy embeds Python 3.10 and calls a narrow `textrpg.android_bridge` facade; authoritative rules, saves, quests, stats, equipment, powers, and narrative remain Python-owned. Android must expose startup phase/error state on-screen and in Logcat so a future failure cannot collapse into an unexplained black screen.

**Tech Stack:** Android Gradle Plugin 9.2.0, Gradle 9.4.1, JDK 17, Kotlin compatible with AGP 9.2, Jetpack Compose BOM 2026.09.00, Chaquopy 17.0.0, Python 3.10, minSdk 24, ARM64 + ARMv7.

**Spec:** `docs/VISUAL_BIBLE.md`, `docs/THE_GAME_MASTER_TASK_REGISTER.md`, `AGENTS.md`

## Global Constraints

- Pixel style is mandatory for gameplay UI, avatars, map presentation, equipment visuals, icons, portraits, and scene art.
- Do not use smooth illustrations with a pixel filter as canonical game art.
- Preserve authoritative flow: `GameState -> World/Quest/Narrative -> Rules/Stats/Abilities/Equipment -> player-safe projection -> Android UI`.
- Do not duplicate RPG calculations in Kotlin.
- Android startup failures must render a diagnostic state instead of a blank screen whenever the Activity can render.
- `minSdk = 24`.
- First sideload build supports `armeabi-v7a` and `arm64-v8a`.
- Python runtime is pinned to 3.10 for this first dual-ABI proof.
- Offline-first; no paid hosted services are required to play.
- Save data stays in Android app-private storage and remains versioned by the Python persistence contract.
- No task is `DONE` merely because source files exist; exact build/test evidence is required.
- Physical-device startup remains a separate gate from desktop/unit-test success.

## Review Focus

1. Python engine startup exception: app must show `ENGINE_ERROR` with a safe user-facing message and log technical detail rather than remain black.
2. Missing/corrupt bundled content: startup must fail deterministically with a visible content-load error.
3. Save incompatibility/corruption: Continue must not destroy the prior save and must surface a recoverable error.
4. Rotation/recreation/process lifecycle: authoritative session state must not be silently duplicated or reset by Compose recomposition.
5. Pixel scaling: nearest-neighbor/pixel-snapped assets must remain crisp at supported mobile densities and must not become filtered/blurred.

---

### Task 1: Android repository scaffold and boot-state contract

**Files:**
- Create: `android/settings.gradle.kts`
- Create: `android/build.gradle.kts`
- Create: `android/gradle.properties`
- Create: `android/app/build.gradle.kts`
- Create: `android/app/src/main/AndroidManifest.xml`
- Create: `android/app/src/main/java/com/thegame/rpg/MainActivity.kt`
- Create: `android/app/src/main/java/com/thegame/rpg/boot/BootState.kt`
- Test: `android/app/src/test/java/com/thegame/rpg/boot/BootStateTest.kt`

**Interfaces:**
- Produces: `sealed interface BootState` with `Starting`, `PythonStarting`, `ContentLoading`, `Ready`, and `Error(stage, publicMessage, technicalDetail)`.
- Produces: launcher `MainActivity` which always renders one BootState.

- [ ] **Step 1: Write the failing BootState tests**
  - Assert all startup phases have stable machine-readable stage IDs.
  - Assert `Error` separates public text from technical detail.
- [ ] **Step 2: Run the unit test and confirm RED**
  - Run: `cd android && ./gradlew testDebugUnitTest --tests '*BootStateTest*'`
  - Expected: failure because BootState does not exist.
- [ ] **Step 3: Implement minimal scaffold and BootState**
  - Package ID: `com.thegame.rpg`.
  - `minSdk = 24`; `compileSdk = 37`; `targetSdk = 37`.
  - Enable Compose.
  - Configure Chaquopy plugin `17.0.0` in the app module only.
  - Configure Python `3.10` and ABI filters `armeabi-v7a`, `arm64-v8a`.
- [ ] **Step 4: Verify GREEN and compile the Android app**
  - Run BootState tests, then `./gradlew :app:assembleDebug`.
  - Expected: both succeed.
- [ ] **Step 5: Commit**
  - `feat(android): add reproducible boot scaffold`

### Task 2: Python Android bridge with player-safe projection

**Files:**
- Create: `src/textrpg/android_bridge.py`
- Create: `tests/test_android_bridge.py`
- Modify only as required: `src/textrpg/__init__.py`

**Interfaces:**
- Produces: `create_session(content_path: str, save_path: str | None = None) -> AndroidGameSession`.
- Produces: `AndroidGameSession.scene_view() -> dict`.
- Produces: `AndroidGameSession.choose(choice_id: str) -> dict`.
- Produces: `AndroidGameSession.save(path: str) -> None` and `load(path: str) -> dict`.
- Kotlin consumes only JSON-compatible player-safe values from this facade.

- [ ] **Step 1: Write failing Python tests**
  - New session exposes current scene and only available player choices.
  - Hidden perk/rule provenance does not leak.
  - Invalid choice returns controlled bridge error without mutating authoritative state.
  - Save/load round-trip preserves player state.
- [ ] **Step 2: Run targeted tests and confirm RED**
  - Run: `PYTHONPATH=src python -m unittest tests.test_android_bridge -v`.
- [ ] **Step 3: Implement minimal bridge using existing engine APIs**
  - Reuse `build_scene_view`, `available_choices`, content loader, and persistence layer.
  - No duplicate stat/rule calculations.
- [ ] **Step 4: Run targeted tests and the complete Python suite**
  - Run targeted test, then `PYTHONPATH=src python -m unittest discover -s tests -v`.
- [ ] **Step 5: Commit**
  - `feat(android): expose player-safe Python bridge`

### Task 3: Kotlin↔Python startup boundary and visible diagnostics

**Files:**
- Create: `android/app/src/main/java/com/thegame/rpg/engine/PythonGameEngine.kt`
- Create: `android/app/src/main/java/com/thegame/rpg/engine/GameEngine.kt`
- Create: `android/app/src/test/java/com/thegame/rpg/engine/PythonGameEngineContractTest.kt`
- Modify: `android/app/src/main/java/com/thegame/rpg/MainActivity.kt`

**Interfaces:**
- Produces: `GameEngine.start(context): Result<GameSnapshot>`.
- Produces: `GameSnapshot(sceneId, title, body, choices, location, resources)`.
- Maps Python/asset failures into `BootState.Error`.

- [ ] **Step 1: Write failing contract tests**
  - Python startup failure maps to `ENGINE_ERROR`.
  - Content failure maps to `CONTENT_ERROR`.
  - Valid bridge payload maps to GameSnapshot without exposing unknown raw fields.
- [ ] **Step 2: Confirm RED**.
- [ ] **Step 3: Implement the smallest Chaquopy adapter**.
- [ ] **Step 4: Run unit tests and assembleDebug**.
- [ ] **Step 5: Commit**
  - `feat(android): connect Python engine with visible startup diagnostics`

### Task 4: Pixel gameplay shell

**Files:**
- Create: `android/app/src/main/java/com/thegame/rpg/ui/GameScreen.kt`
- Create: `android/app/src/main/java/com/thegame/rpg/ui/PixelTheme.kt`
- Create: `android/app/src/main/java/com/thegame/rpg/ui/components/PixelPanel.kt`
- Create: `android/app/src/main/java/com/thegame/rpg/ui/components/ChoiceCard.kt`
- Create: `android/app/src/main/java/com/thegame/rpg/ui/components/PlayerAvatarPanel.kt`
- Test: `android/app/src/androidTest/java/com/thegame/rpg/ui/GameScreenTest.kt`

**Interfaces:**
- Consumes: GameSnapshot + choice intents.
- Produces: landscape/mobile-safe pixel presentation with visible avatar region, large narrative region, choice cards, compact resources, and bottom navigation placeholders.

- [ ] **Step 1: Write failing Compose UI tests**
  - Narrative is visible and scrollable.
  - Every available choice is rendered as a tappable card.
  - Avatar panel exists.
  - Stats/Inventory/Quests/Map/More navigation affordances exist without dumping full sheets on the narrative screen.
- [ ] **Step 2: Confirm RED**.
- [ ] **Step 3: Implement minimum pixel shell**
  - Use hard edges, pixel-aligned spacing, nearest-neighbor image filtering for raster pixel assets, limited palette tokens, and no smooth-gradient dependency for readability.
- [ ] **Step 4: Run Compose tests + assembleDebug**.
- [ ] **Step 5: Commit**
  - `feat(android): add pixel gameplay shell`

### Task 5: Save/Continue and crash-safe startup

**Files:**
- Create: `android/app/src/main/java/com/thegame/rpg/save/SaveRepository.kt`
- Create: `android/app/src/test/java/com/thegame/rpg/save/SaveRepositoryTest.kt`
- Modify: Python bridge only where required for safe save/load errors.

**Interfaces:**
- Produces: app-private canonical save path.
- Produces: non-destructive `continueGame()` result which preserves incompatible/corrupt files for diagnostics/recovery.

- [ ] **Step 1: Write failing save tests** for missing, valid, corrupt, and unsupported-schema saves.
- [ ] **Step 2: Confirm RED**.
- [ ] **Step 3: Implement minimal repository/bridge behavior**.
- [ ] **Step 4: Run Android tests + full Python suite + assembleDebug**.
- [ ] **Step 5: Commit**
  - `feat(android): add safe local save and continue`

### Task 6: Device smoke proof and black-screen closure gate

**Files:**
- Create: `docs/ANDROID_PIXEL_CLIENT_VALIDATION.md`
- Modify: `docs/THE_GAME_MASTER_TASK_REGISTER.md`

**Interfaces:**
- Consumes: debug APK from exact feature HEAD.
- Produces: evidence record tying source SHA → APK hash → install/launch → visible first frame → Python engine ready → one choice → save → restart → continue.

- [ ] **Step 1: Build exact APK and record SHA-256**.
- [ ] **Step 2: Inspect APK contents/signature/ABIs**.
- [ ] **Step 3: Install and launch on representative Android runtime/device**.
- [ ] **Step 4: Capture Logcat startup phases and confirm visible UI**.
- [ ] **Step 5: Execute one narrative choice, save, force-stop/restart, Continue**.
- [ ] **Step 6: Update register**
  - `A-001` can become `DONE` only if the prior black-screen class is eliminated by the reproducible replacement and visible startup is confirmed.
  - `A-002` becomes `DONE` when the corrected APK is built/verified/delivered.
  - `A-003` becomes `DONE` only after representative/physical Android confirmation.
- [ ] **Step 7: Commit**
  - `test(android): record device smoke proof`
