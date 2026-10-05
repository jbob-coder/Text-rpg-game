# THE GAME — Player-AI Mission Control

**Status:** ACTIVE / FAST ENTRY SURFACE  
**Repository:** `jbob-coder/Text-rpg-game`  
**Authority branch:** `docs/master-game-development-program`  
**Snapshot HEAD:** `0ae5dae4df05cec19109ef4f9fad1674cbe2f4d3` — re-fetch before acting.

Mission Control is the shortest safe path into current work. It does not replace the Bulletin Board, Master Task Register, Council, tests, or source truth.

## ♾️ fast-entry rule

When a Player-AI receives `♾️`:

1. fetch live HEAD;
2. open this file;
3. locate its Player-AI mission card;
4. re-fetch the Bulletin Board entry for that task;
5. read only the card's **Must Read** set plus files directly changed by newer commits;
6. perform the card's **Next Move**;
7. verify against the **Exit Gate**;
8. synchronize evidence, Brag, Scoreboard and next-task state.

Do not reread the whole repository unless the task truly requires it.

## Common verification recipes

Use only commands available in the current environment. Record exactly what actually ran.

### Python authority suite
```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

### Android JVM/unit gate
```bash
gradle -p android testDebugUnitTest --stacktrace
```

### Compile instrumentation tests
```bash
gradle -p android :app:assembleDebugAndroidTest --stacktrace
```

### Build debug APK
```bash
gradle -p android :app:assembleDebug --stacktrace
```

### Full PR integration path
For runtime work after OR-009 transition, use the existing `.github/workflows/android-pixel-client.yml` pull-request workflow. It is the merge-state integration authority; do not invent a second CI path.

If an environment cannot run a gate, record it as **UNEXECUTED** rather than claiming pass/fail by inference.

## Critical defect quick triage

If a mission hits a serious code problem, spend a few minutes deciding whether it is a symptom or the cause.

Ask:
- What is the first incorrect API/state/contract in the failure chain?
- Does this defect break only my task, or multiple Player-AIs?
- Am I about to duplicate authoritative logic in a second layer?
- Would this workaround still be necessary if the underlying contract were correct?
- What test would fail on the bad state and prove the repair?

If immediate progress requires a workaround, mark it `TEMPORARY_PATCH` and record `ROOT_CAUSE_FOLLOWUP`. There is no scoring penalty for doing this safely.

If you eliminate the real cause, evaluate the work under `docs/AI_CRITICAL_ROOT_CAUSE_REWARDS.md`. A sufficiently serious incident can earn up to **+455 bonus points on top of the mission score**.

## Critical path to a complete Phase 1

`D-064` **safe handoff — last transition blocker**
↓
**green authority checkpoint already PASS: PR #65 / run #351**
↓
`D-069 -> D-070 -> D-071 -> D-072 -> D-073 -> D-074`
↓
`D-075 -> D-076 -> D-077 -> D-078 -> D-079`
↓
**Phase 1 integrated acceptance candidate**

The current transition job is to close D-064 without scope expansion. D-065, D-067 and D-068 are DONE; the green authority checkpoint is already established.

---

## Kestrel — D-064 — Projection / Presentation

**Player-AI class:** Player-Safe Projection, Presentation & Asset Lead  
**Mission state:** implementation materially advanced; finish verification/handoff, do not redesign.

### Mission objective
Finish the bounded room/actor projection so authored player-safe actor presence reaches Android through the strict snapshot boundary while preserving opening-scene visual equivalence and hidden-state redaction.

### Must Read
- `docs/systems/PLAYER_SAFE_ROOM_ACTOR_PROJECTION_CONTRACT.md` or current D-030 projection authority;
- `src/textrpg/room_projection.py`;
- room-presence content/sidecar used by current opening scenes;
- `android/app/src/main/java/com/thegame/rpg/engine/PlayerSafeSnapshotMapper.kt`;
- `android/app/src/main/java/com/thegame/rpg/engine/PythonGameEngine.kt`;
- D-064 Python/Kotlin/UI tests changed since claim.

### Already accomplished / do not redo
Recent repository history already contains:
- strict room projection invariants;
- authored opening room presence;
- production runtime routing through the player-safe mapper;
- semantic story actor placement resolver;
- opening actor placement equivalence tests;
- unittest-native room projection acceptance coverage;
- repair of the recursive snapshot helper.

Audit current source before adding anything else.

### Next Move
1. run/obtain exact-head D-064 focused evidence and required aggregate gates;
2. verify opening actor-set/placement equivalence;
3. verify malformed/duplicate/location/speaker rejection and private-state absence;
4. verify Android consumer mapping/screenshot behavior where acceptance requires it;
5. write one D-064 evidence packet and close the task if green.

### Exit Gate
- versioned authoritative room projection;
- Python + Kotlin strict mapping;
- no raw private NPC state or raw pixel/world authority leakage;
- current opening presentation equivalent through semantic placement;
- old heuristic retirement boundary is explicit;
- required exact-head tests/build evidence recorded.

### Do Not
- invent a dynamic spatial model now;
- widen `placement_key` into simulation position;
- redesign the root snapshot;
- expand final art scope.

### Required cross-review
- Veyr: NPC privacy fields if touched;
- Veyra: only if gameplay/tactical semantics are introduced;
- Nodus: integration/CI if shared runtime state changes.


### PR #63 failure triage — exact next repair
Workflow run #350 / `37253491745`:
- Python: map-travel room mismatch; already repaired on authority, so rebase rather than reimplement.
- Android emulator: PASS.
- Android JVM compile: FAIL because `PixelStoryActorCatalogTest.kt` still calls the removed `placements(locationId, sceneId)` API after production changed to `placements(actors: List<GameRoomActor>)`.

Exact failing test calls:
- lines 46–47 use obsolete named parameters `locationId` / `sceneId`;
- lines 59, 64, 69, 74 and 77 pass String arguments where `List<GameRoomActor>` is now required.

**One-shot repair:** rebase on authority, update only `PixelStoryActorCatalogTest.kt` to build projected `GameRoomActor` fixtures and call `placements(actors)`, then rerun PR CI.


### Exact PR #63 test migration recipe

Production in PR #63 already changes the actor catalog to:
`placements(actors: List<GameRoomActor>)`.

It maps:
- `visualFamily = "NPC_TAMSIN"` -> Tamsin sprite;
- `visualFamily = "SUPPORT_WOUNDED_COURIER"` -> courier sprite;
- `placementKey` through `PixelStoryActorPlacementResolver`;
- unknown family/key -> omitted.

Use `com.thegame.rpg.engine.GameRoomActor` in `PixelStoryActorCatalogTest.kt`.

Minimal fixture shape:
```kotlin
private fun actor(
    presentationId: String,
    visualFamily: String,
    placementKey: String,
) = GameRoomActor(
    presentationId = presentationId,
    knownActorId = null,
    displayName = presentationId,
    visualFamily = visualFamily,
    placementKey = placementKey,
    poseKey = null,
    outfitKey = null,
    visibleTags = emptyList(),
    inspectable = false,
    dialogueAvailable = false,
    actions = emptyList(),
)
```

Required bounded cases:
1. courier + Tamsin using `PLATFORM_NINE_COURIER_LEFT` and `PLATFORM_NINE_TAMSIN_RIGHT`;
2. Tamsin at `RELAY_WORKBENCH_TAMSIN_RIGHT`;
3. Tamsin at `SERVICE_TUNNEL_TAMSIN_RIGHT`;
4. unknown `visualFamily` -> empty;
5. unknown `placementKey` -> empty.

Direct PR conversation note: comment ID `5987024043`.

**Do not carry unnecessary formatting/compaction churn forward.** Rebase/rebuild from current authority and apply only the actor-authority migration plus its tests where practical.

---

## Veyr — D-065 — COMPLETED

**Player-AI class:** NPC, Social & Narrative-State Lead  
**Mission state:** DONE — primary + D-065-B verified.

### Verified result
- durable Tamsin shared-entry memory;
- save/load persistence;
- later authored reaction;
- deterministic route;
- player-safe privacy regression.

### Evidence
- `docs/evidence/D065_TAMSIN_MEMORY_PROOF_2026-10-04.md`;
- PR #59 workflow run #341 / `37252547112`.

### Next Move
Do not reopen D-065. Await/use the Veyr D-075 mission card if D-075 is unlocked after dependency audit.

---

## Nodus — D-067 — Inventory / Equipment Integration Proof

**Player-AI class:** Integration Architect & Systems Gatekeeper  
**Mission state:** **DONE / PRIMARY + D-067-B VERIFIED**.

### Verified result
- authoritative obtain/possess/equip/use loop;
- save/load across equipment and story inventory changes;
- Android player-safe inventory/equipment presentation;
- invalid-equip full rollback;
- exact authority checkpoint fully green.

### Evidence
- `docs/evidence/D067_PHASE1_INVENTORY_EQUIPMENT_PROOF_2026-10-04.md`;
- PR #65 / workflow run #351 / `37253975755`;
- APK SHA-256 `7dfc02e4b6ce95fc0fb6ba6dbe1869366993cd6388811627efdc2deb7daeefda`.

### Critical-fix credit
Separate **+310** root-cause award remains verified under OR-024 for the transition bridge/system-blocker repair.

### Next Move
Do not reopen D-067. Support Kestrel only as an integration reviewer if requested. The tactical gate now waits only on D-064 safe handoff.


---

## Veyra — D-068 — Activity Proof

**Player-AI class:** Gameplay Systems & Tactical Lead  
**Mission state:** **DONE / SAFE HANDOFF**. D-069 remains blocked pending the green-authority checkpoint.

### Result
D-068 proves the existing Trace Chamber `TRAIN_POWER_FUNDAMENTALS_TWO_HOURS` action as the bounded Phase 1 activity loop:
- legal entry through the authored Gate Twelve / Trace Echo route;
- exact +120 minutes;
- exact -16 stamina / -10 focus;
- Powers progress to 2.0 from zero under the current formula;
- training + choice history;
- player-safe projected result;
- save/load preservation;
- Android exact-choice delegation and authoritative returned-value mapping;
- invalid-entry and time-preflight failure atomicity.

Authority proof merge:
- `e883205559c64d2e82614160bd6548c2c9332808`.

Evidence:
- `docs/evidence/D068_PHASE1_ACTIVITY_PROOF_2026-10-04.md`;
- PR #59;
- workflow run #341 / `37252547112`.

### Exit Gate
- legal activity entry deterministic: **PASS**;
- invalid entry rejects cleanly: **PASS**;
- authoritative exact time/resource costs: **PASS**;
- result persists: **PASS**;
- save/load preserves result: **PASS**;
- player-facing projection exposes intended outcome: **PASS**;
- D-068-B atomicity regression: **PASS**;
- physical-device validation: **NOT CLAIMED**.

### Current blocker / next move
D-068 is no longer part of the transition blocker.

Veyra's next gameplay task is D-069. PR #65 / run #351 already proved the green Python + Android + emulator checkpoint. Substantive D-069 implementation must wait only for D-064 safe handoff and the Bulletin Board unlock under the runtime merge-state gate.

Until then Veyra may assist with bounded integration/checkpoint evidence or read-only D-069 preparation, but must not bypass the gate.

---

## Veyr — D-075 — Quest Branch / World Consequence

**Player-AI class:** NPC, Social & Narrative-State Lead  
**Mission state:** **DONE / PRIMARY + D-075-B VERIFIED**.

### Verified result
- cooperative and solo `QUEST_DEAD_RELAY` resolutions start from equivalent baselines;
- both complete and survive save/load;
- both navigate to the same later `DISTRICT_HUB` checkpoint;
- branch-specific NPC/relationship/route state remains durable;
- `ASK_TAMSIN_ABOUT_SHARED_ENTRY` is visible only on the cooperative path;
- private memory remains absent from player-safe projection;
- normalized branch-difference fixture proves only intended semantic differences.

### Evidence
- `docs/evidence/D075_PHASE1_QUEST_BRANCH_WORLD_CONSEQUENCE_2026-10-04.md`;
- PR #66 / run #352 / `37254171985`;
- Python 349 tests OK;
- Android unit/build/package PASS;
- emulator smoke/screenshots PASS;
- APK SHA-256 `4bb7c133dcecfbc9958651f6b3e10e3f3d6aec594c42c2896a87118b735fb28b`.

### Next Move
Do not reopen D-075. D-076 remains downstream of the tactical chain/integrated persistence prerequisites. Veyr is available for bounded narrative/social review without taking over another Player-AI's active primary.


---

## Fifth Player-AI Seat — Verification / Red-Team / Performance

**Status:** UNFILLED. Parallel P5 / D-042 is reserved for this Player-AI class while the seat remains open.

### Recommended first mission
Claim **Parallel P5 / D-042 — Cross-branch existing-state source audit** unless live Bulletin evidence exposes a higher-value independent integration defect.

### Mission objective
Act as an independent adversarial verifier, not another feature implementer.

### First Move
1. choose a Player-AI name;
2. claim P5/D-042 if still READY;
3. audit recent D-064/D-065/D-067/D-068 integration history and cross-branch survivors;
4. identify one concrete migration survivor, stale assumption or regression risk;
5. produce exact disposition/evidence;
6. use Bug Hunter bounty only for real material defects.

### Future specialization path
- D-076 integrated deterministic regression;
- D-078 low-end performance;
- D-079 final acceptance/APK provenance.

---

## Evidence reuse warning

Do not reuse a green run from another Player-AI merely because it happened later in wall-clock time.

Audit performed during the Overseer meta-loop:
- D-065 implementation/test commit `e339b4b0...` -> D-066 verification PR #42 head `c60f2ca1...`: **diverged**.
- D-067 canonical-session proof commit `d557b0d5...` -> the same PR head: **diverged**.
- The synthetic PR merge commit also diverged from both histories.

Therefore D-066's fully green run proves D-066, not exact-head completion of D-065 or D-067.

Veyr and Nodus should reuse test design/commands where useful, but must produce evidence against the actual integrated authority state that contains their work.

## Live checkpoint evidence

Checkpoint PR #65 / workflow run #351 is testing the repaired authority merge-state.
- complete Python suite: **PASS**;
- Android unit/build: still running at last observation;
- emulator smoke: still running at last observation.

Do not call the authority checkpoint green until every required job completes successfully.

## Green Authority Checkpoint

This checkpoint is the unlock condition for substantive D-069 work.

The checkpoint begins only after D-064, D-065, D-067 and D-068 are all safely handed off.

Minimum evidence:
- complete Python suite green on the authority merge state;
- required Android unit/build gates green for changed surfaces;
- no unresolved player-safe privacy leak;
- no known save/schema incompatibility;
- Bulletin/Master Register/Scoreboard synchronized;
- exact authority HEAD recorded.

Nodus coordinates the checkpoint. Veyra may then reclaim D-069 using `docs/AI_RUNTIME_MERGE_STATE_GATE.md`.

## Mission Control design principle

A Player-AI should spend its intelligence solving the game, not reconstructing the task-management system.

If a mission card becomes stale:
- update the card from live evidence;
- do not force the Player-AI to rediscover known completed work;
- do not mark work DONE without proof.
