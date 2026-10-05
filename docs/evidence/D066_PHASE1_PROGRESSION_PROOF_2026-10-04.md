# D-066 Phase 1 Progression Proof Evidence — 2026-10-04

Status: **VERIFIED BOUNDED PHASE 1 PROOF**
Agent: **Veyra**
Task: **D-066 — Phase 1 progression proof**
Authority branch: `docs/master-game-development-program`
Claim head: `4b038103380491866ecb1c686d5f81c0b4ecbb3f`

## 1. Proof target

D-066 proves Phase 1 requirement 5 through the existing Gate Twelve Trace Echo route without introducing a second progression owner or changing save schema v1.

Selected route:
- discover `ABILITY_TRACE_ECHO`;
- discover `TECHNIQUE_SIGNAL_PULSE`;
- execute authored `PRACTICE_SIGNAL_PULSE_ONE_HOUR`;
- gain durable technique and ability mastery;
- pay stamina/focus and world time;
- persist through save/load;
- reproduce the same result with and without a save boundary;
- project only player-safe discovered progression into Android.

## 2. Authority implementation

Relevant authority-branch implementation commits include:
- `58c6ae25b9b31d998e82b5ab4932585b7acf1ef1` — stable ability ID added to Python player-safe projection;
- `ee0e01d10288722700ece98b944dc41f071da02d` — deterministic save-boundary progression regression;
- `e3a77da21d708cde70a3533ce3d14e016c0889ef` — typed Android ability/technique/resource mapping;
- `04ccc2c0797f9568c51a657f5cb3f757d41063ff` — Android mapper/privacy tests;
- `e259c31f0fcbd7e4dd1115f0d8f1a4ed72460c8d` — bounded Stats ability consumer;
- `a06a60f6c0b4265545bc9cad462f26dc29bd0645` — Compose progression assertion.

Current authority blobs were rechecked after parallel merges:
- `src/textrpg/powers.py`: `d75ab4099f171dd4950bd7f852a0ad7d9f560e6f`;
- `tests/test_status.py`: `785a6b8db92c7c92fc036ea36be71b922592032c`;
- `tests/test_save_resume_routes.py`: `f021bc84f4941771784af3b475b69f88057630e9`;
- `android/app/src/main/java/com/thegame/rpg/ui/StatsSection.kt`: `fba4f4314d366d584bd1161c023efc6c6ef8fae2`;
- `android/app/src/androidTest/java/com/thegame/rpg/ui/CharacterStatsSectionTest.kt`: `fdf64e34baa8b144a38b259824d7a4fc7d475c4a`.

The authority `GameEngine.kt` also retains all D-066 DTO/mapper/privacy markers after concurrent room/inventory work:
`GameAbilityResource`, `GameTechnique`, `GameAbility`, `GameSnapshot.abilities`, `status["abilities"]` mapping, forbidden authored-progression guard, and final `abilities = abilities` snapshot assignment.

## 3. Isolated exact verification tree

Because the live authority branch was simultaneously receiving D-064/D-065/D-067 changes, D-066 was also verified on a clean isolated tree:

- verification base branch: `ai/veyra-d066-proof-base`;
- base SHA: `4b038103380491866ecb1c686d5f81c0b4ecbb3f`;
- verification branch: `ai/veyra-d066-phase1-proof`;
- final verification head: `48ce6223fb84c3d31457c7f1dacaec87ce0d3df2`;
- verification PR: **#42**;
- PR diff: only the seven D-066 files needed for Python projection/persistence plus Android mapping/UI tests.

The verification tree intentionally excluded concurrent D-064 room runtime changes. A first verification attempt exposed copied D-064 room assertions in the shared `BridgeStatusMapperTest.kt`; Veyra rebuilt that verification test file from the clean claim-head version plus only the three D-066 mapper tests before the final run.

## 4. GitHub Actions evidence

Workflow: **Android Pixel Client**
Final D-066 verification run: **#312**
Run ID: `37250124885`
Verification head: `48ce6223fb84c3d31457c7f1dacaec87ce0d3df2`

### Python progression evidence

The workflow's aggregate Python job reports one unrelated environment error because the unchanged clean-base `tests/test_room_projection.py` imports `pytest` while the workflow installs no pytest package.

Observed aggregate result:
- **320 tests discovered**;
- **1 error**: `ModuleNotFoundError: No module named 'pytest'`;
- no D-066 test failure.

D-066-relevant executed tests observed **PASS**:
- `test_first_power_practice_is_deterministic_across_save_boundary`;
- `test_first_power_practice_survives_save_resume`;
- `test_status_projection_uses_rules_and_does_not_mutate_state`;
- `test_first_power_requires_discovery_then_paid_practice`.

Therefore the repository-wide Python gate is not claimed green, but the D-066 authoritative progression/persistence/projection tests executed successfully.

### Android JVM / build evidence

Job: `android-unit-and-assemble` — **SUCCESS**

Observed successful steps:
- Android unit tests;
- Compose instrumentation-test compilation;
- debug APK assembly;
- APK content verification;
- APK SHA-256 generation;
- artifact upload.

APK SHA-256:
`a14ee38462da6a77a159225b71d2506bb0e18a051430b3a5f90e9a291eb81d8d`

Uploaded artifact:
- artifact ID: `11319893955`;
- uploaded ZIP SHA-256: `83815f2b4cdb3cd84db9b61b68f7e1271959b55c07c55cdda6a17db171fec207`.

### Android emulator / Compose evidence

Job: `android-emulator-smoke` — **SUCCESS**

Observed:
- `gradle -p android connectedDebugAndroidTest --stacktrace`;
- **35 tests started** on API 35 emulator;
- **35 tests finished**;
- Gradle **BUILD SUCCESSFUL**;
- expected screenshot evidence set verified successfully and uploaded.

The D-066 Compose test is an ordinary, unfiltered instrumentation `@Test` in that connected test target; the connected suite completed without failures.

## 5. Player-safe projection boundary

D-066 adds only discovered/player-safe progression data to Android:
- stable ability ID;
- display name/fallback;
- rank;
- mastery stage/XP;
- form/state;
- safe ability resource values;
- discovered techniques with mastery/stage/use/cooldown state;
- completed evolution IDs already exposed by the Python safe view.

The typed mapper rejects authored `requirements`, `discovery_requirements`, and `effects` if they attempt to cross the Android progression boundary.

No Android mutation endpoint was added. Mastery/resource/time/unlock authority remains in Python.

## 6. Result

**Phase 1 requirement 5 is satisfied by a bounded implemented proof.**

This does **not** mean the final progression/class/profession/rank design is complete. It proves one reusable Gate Twelve progression path:
authoritative action -> mastery/resource/time change -> save/load -> deterministic replay -> safe typed Android projection -> real Compose/emulator consumption.

## 7. Remaining repository-level issue

The global Python workflow remains red until the separate room-projection test/environment mismatch is resolved:
`tests/test_room_projection.py` imports `pytest`, but the workflow's Python job does not install pytest.

That issue is outside D-066 and was not modified to manufacture a green result.
