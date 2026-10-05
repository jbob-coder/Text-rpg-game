# D-068 Phase 1 Activity Proof Evidence — 2026-10-04

Status: **VERIFIED BOUNDED PHASE 1 ACTIVITY PROOF**
Agent: **Veyra**
Task: **D-068 — Phase 1 activity exact-head proof**
Authority branch: `docs/master-game-development-program`
Claim transfer head: `a13b2a2887ed9b64a6f3794e5bebee7891ca566d`
Authority implementation/test merge: `e883205559c64d2e82614160bd6548c2c9332808`

## 1. Proof target

D-068 proves Phase 1 requirement #8 using the existing authored Trace Chamber activity:

`TRAIN_POWER_FUNDAMENTALS_TWO_HOURS`

No activity registry, scheduler, profession system, background timer, or UI-owned progression arithmetic was added.

The proved chain is:

legitimate authored route
-> Trace Chamber activity availability
-> authoritative `skill_train`
-> exact time/resource cost
-> persistent Powers skill progress
-> player-safe projection
-> save/load
-> Android exact-choice delegation and authoritative snapshot mapping.

## 2. Current authored activity

Source: `content/vertical_slice_01.json`

The selected action is authored in `TRACE_STABILIZATION_HUB`, whose location is `TRACE_CHAMBER`.

Contract:
- choice ID: `TRAIN_POWER_FUNDAMENTALS_TWO_HOURS`;
- skill: `powers`;
- duration: 120 minutes;
- intensity: 1;
- authored requirements: stamina >= 16 and focus >= 10;
- next scene: `TRACE_STABILIZATION_HUB`.

The activity is absent from the initial opening scene and becomes available only after the legitimate Gate Twelve / Trace Echo route reaches the stabilization hub.

## 3. Authoritative engine behavior proved

`simulation.train` owns the calculation.

For 120 minutes at intensity 1:
- stamina cost = **16.0**;
- focus cost = **10.0**;
- world time advances by **120 minutes**;
- Powers skill starting from no explicit value / zero becomes **2.0** under the current training formula;
- a `training` history event is appended;
- the surrounding authored choice event is appended by `RulesEngine.choose`.

`RulesEngine.choose` deep-snapshots durable state before effects and restores that snapshot on any exception.

D-068 does not move any of these calculations into Android.

## 4. Proof tests merged to authority

### Python

New:
- `tests/test_phase1_activity.py`

Tests:
1. `test_trace_chamber_activity_commits_time_cost_progress_and_save_load`
   - proves activity not exposed at opening;
   - reaches Trace Chamber through the real authored route;
   - proves activity enabled in the authored context;
   - proves +120 world minutes exactly once;
   - proves -16 stamina / -10 focus;
   - proves Powers skill -> 2.0;
   - proves training + choice history;
   - proves projected time/resources/skill reflect authoritative state;
   - saves and loads;
   - proves time/resources/Powers progress survive load.

2. `test_activity_requirement_failure_spends_nothing`
   - forces stamina below the authored requirement;
   - proves the choice is disabled;
   - proves the bridge returns `CHOICE_ERROR`;
   - proves the full durable snapshot is unchanged.

3. `test_activity_rolls_back_when_time_preflight_fails`
   - injects malformed timed-condition state;
   - proves the authoritative time preflight rejects resolution;
   - proves the bridge returns `CHOICE_ERROR`;
   - proves the full durable snapshot is unchanged.

Tests 2 and 3 close **D-068-B — interruption/atomicity regression** for the current atomic Phase 1 activity model.

### Android JVM

Updated:
- `android/app/src/test/java/com/thegame/rpg/engine/PythonGameEngineContractTest.kt`

New contract test:
- `activity choice delegates exact id and maps authoritative progress`

It proves:
- Kotlin forwards the exact `TRAIN_POWER_FUNDAMENTALS_TWO_HOURS` ID through `PythonGameEngine.choose`;
- Kotlin does not calculate the activity;
- returned authoritative `timeMinutes`, `location`, stamina, focus and Powers skill values are mapped unchanged.

## 5. Exact-head / merge-state evidence

### Final proof branch

- branch: `ai/veyra-d068-activity-proof-v2`;
- base authority SHA: `05a7e8305e816a408073d820360cc03333fefba5`;
- proof head: `583e61dffc08c3989af4c15561d8eabf1ff6468d`;
- PR: **#59**;
- workflow: **Android Pixel Client**;
- run number: **341**;
- run ID: `37252547112`.

The authority branch advanced while CI executed. Before merge, Veyra compared the PR head to the live authority. The only authority-side drift was:
- `AGENTS.md`;
- `docs/AI_TASK_BULLETIN_BOARD.md`;
- `docs/OVERSEER_META_LOOP.md`;
- `docs/PLAYER_AI_MISSION_CONTROL.md`;
- `docs/PROJECT_OVERSEER_DECISION_LOG.md`.

No `src/`, `content/`, `tests/`, or `android/` runtime/test file differed.

PR #59 was then merged to authority as:
- `e883205559c64d2e82614160bd6548c2c9332808`.

A post-merge comparison from the tested proof head to that authority merge showed only the same governance/documentation files above. Therefore the runtime/content/Android/test tree carrying D-068 at the authority merge is equivalent to the tree evaluated by run #341.

## 6. Python execution evidence

Run #341 Python job executed the complete repository unittest command and discovered **341 tests**.

All D-068 tests executed **PASS**:
- `test_activity_requirement_failure_spends_nothing`;
- `test_activity_rolls_back_when_time_preflight_fails`;
- `test_trace_chamber_activity_commits_time_cost_progress_and_save_load`.

The aggregate Python job remained red with **1 failure / 12 errors** from separately owned D-064/D-067 transition defects, including:
- stale room-root expectation;
- pytest-style D-064 acceptance import under the unittest job;
- equipment bridge/API signature mismatch affecting D-067-related tests.

Those failures are not hidden and are not claimed fixed by D-068.

D-068 acceptance is based on its executed focused tests plus exact runtime-tree equivalence, not on a false claim that the repository-wide transition checkpoint is green.

## 7. Android execution evidence

Run #341 job `android-unit-and-assemble`: **SUCCESS**.

Observed successful steps:
- Android JVM/unit tests;
- Compose instrumentation-test compilation;
- debug APK assembly;
- APK contents/hash verification;
- APK artifact upload.

The D-068 Kotlin contract test is part of that JVM test target; the job completed successfully.

APK SHA-256:

`1fb6599802ed81f10d8c6b16b5bc4ab0ef2277c84a8859d669c81af12706ce8d`

D-068 did not change Compose/runtime UI behavior, so emulator execution is supplementary rather than required for this proof. No physical-device validation is claimed.

## 8. Player-facing boundary

The current Android path is intentionally simple:

`GameViewModel.choose(choiceId)`
-> `PythonGameEngine.choose(choiceId)`
-> Python `AndroidGameSession.choose`
-> authoritative engine resolution
-> refreshed player-safe snapshot
-> Kotlin mapping.

Current Android can:
- display the authored activity label as a normal choice;
- request the choice;
- display returned authoritative time/resource/skill state.

Current Android does **not** have a normalized activity-specific duration/cost preview DTO. That remains deferred V10/V11 refinement and is not required to prove the existing Phase 1 activity loop.

## 9. Result

**Phase 1 requirement #8 is satisfied by the existing Trace Chamber training activity.**

Proved:
- deterministic legal entry;
- invalid entry rejection;
- exact authoritative time/resource costs;
- persistent progression output;
- save/load preservation;
- player-safe projection;
- Android request/mapping path;
- atomic rollback on failure.

Not claimed:
- full activity registry;
- professions/jobs/economy;
- resumable/background/offline activities;
- full activity-specific Android UX;
- physical-device compatibility;
- a green repository-wide transition checkpoint.

D-069 remains gated until D-064, D-065, D-067 and D-068 are safely handed off and the authority merge state becomes green.
