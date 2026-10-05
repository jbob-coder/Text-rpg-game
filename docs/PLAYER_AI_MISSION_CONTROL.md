# THE GAME — Player-AI Mission Control

**Status:** ACTIVE / FAST ENTRY SURFACE  
**Repository:** `jbob-coder/Text-rpg-game`  
**Authority branch:** `docs/master-game-development-program`  
**Snapshot HEAD:** `f76df65f8c1ddb669d097c817fe9487a1058b008` — historical immediately after HEAD moves; re-fetch before acting.

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

## Coordination Room quick loop

Before a new primary:
`INTENT -> Bulletin CLAIM -> START`

During work:
post only meaningful `UPDATE / HELP / BLOCKED / REVIEW REQUEST` messages.

After a real completion:
`sync evidence -> FINISH -> NEXT -> INTENT -> Bulletin CLAIM -> START`

Room:
`docs/AI_COORDINATION_ROOM.md`

The room communicates work state; it never overrides Bulletin ownership.

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

## AXIOM — large code-problem escalation

**Project Overseer:** AXIOM  
**Intake:** `docs/overseer/CODE_PROBLEM_REVIEW_BOARD.md`  
**Evidence packets:** `docs/overseer/code_problems/`

Use AXIOM when the defect is bigger than ordinary local debugging: P0 blocking, cross-system, architectural, merge-state sensitive, save/privacy/determinism threatening, repeatedly red, or likely to require a workaround.

Player-AI submission minimum:
1. current task + exact observed HEAD;
2. failure and expected behavior;
3. smallest reproduction available;
4. exact executed test/workflow/log evidence;
5. affected files/APIs/domains;
6. what downstream work is blocked;
7. temporary patch status;
8. causal hypothesis clearly marked as hypothesis;
9. unverified facts.

AXIOM assigns a Problem Pressure Score and disposition.

For accepted CRITICAL-or-higher problems, AXIOM either:
- links the CPR to the existing causal-owner Bulletin task; or
- creates a Master Task Register + Bulletin task when no owner exists.

Do not create duplicate tasks for the same causal incident.

Reporting or attempting a difficult defect never reduces score.

## Next-player learning handoff

Before a primary task is fully handed off, append a compact Next Player Learning Record to:
`docs/player_guide/PLAYER_LEARNING_LEDGER.md`.

The required record is not a task summary. It is a shortcut for the next Player-AI:
- smallest Read First set;
- proven facts not to rediscover;
- real behavior owner;
- trap/false assumption;
- exact validation recipe;
- safe extension point;
- unresolved boundary;
- direct next-player shortcut.

D-080 owns the first-wave backfill for Nodus, Veyra, Kestrel and Veyr.

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
**Mission state:** **SURGICAL LIVE-AUTHORITY REBUILD / FINAL MERGE-STATE GATE**.

### Objective
Finish the bounded room/actor projection with the smallest current-authority integration delta. Do not redesign the room contract and do not merge historical/RED evidence PRs as the final patch.

### Read first
1. live Bulletin D-064 entry;
2. `docs/evidence/D064_LIVE_AUTHORITY_SURGICAL_REBASE_MANIFEST_2026-10-04.md`;
3. `docs/AI_RUNTIME_MERGE_STATE_GATE.md`;
4. only then the five production/test files named by the surgical manifest.

### Evidence roles — do not collapse them
- **PR #63 / run #354 — GREEN_COMPATIBILITY_PROOF:** synthetic merge `ee497f2` tested PR head `c8268ea...` with authority `b2849f24...`; Python 355/355 PASS, Android unit/build/package PASS, emulator smoke/screenshots PASS, APK SHA-256 `acaf6c8033ff187b5d9e2e2facfa0b47a5a60c20eb022a27a85e1fb353969e28`. Under OR-019 this remains reusable behavior/compatibility evidence because later drift is documentation/governance only. **Do not merge #63 as-is**: its nonessential `SceneIllustration.kt` / `PixelStoryActorCatalog.kt` compaction churn was explicitly rejected from the final authority patch.
- **PR #68 — RED_CONTRACT_ONLY:** current head `819a58379cc85a26b6a9e2da8bd2cf463243d503` now includes Platform Nine, Relay Workbench `90,14`, Service Tunnel `76,14`, empty-list, unknown-family and unknown-placement expectations. Run #355 proved the intended old-production API mismatch; amended run #356 is test evidence only. **Do not merge #68.**
- **FINAL MERGE_CANDIDATE:** none until Kestrel creates the fresh surgical branch from live authority.

### Exact next move
Follow the surgical manifest without widening scope:
1. fetch current authority HEAD and current SHAs for the manifest's five-file surface;
2. create a fresh short-lived D-064 branch;
3. apply only:
   - both `GameScreen.kt` `roomActors = snapshot.room.actors` wires;
   - `SceneIllustration.kt` `List<GameRoomActor>` parameter + projected catalog call;
   - `PixelStoryActorCatalog.kt` projected `visualFamily` mapping + existing `PixelStoryActorPlacementResolver`;
   - focused catalog equivalence/rejection tests;
   - focused source-wiring regression;
4. preserve unrelated presentation code/formatting;
5. open the fresh PR and require current merge-state Python + Android unit/build/package + emulator evidence;
6. if green, write D-064 evidence + Next Player Learning Record, FINISH, Brag/Scoreboard/Register/Bulletin handoff, then mark DONE;
7. promote D-069 to READY for Veyra immediately after the safe D-064 handoff.

### Exit gate
- authoritative versioned room projection + strict Python/Kotlin mapping;
- no hidden/private NPC leakage;
- actor presence driven only by player-safe `room.actors`;
- coordinates owned only by semantic `PixelStoryActorPlacementResolver`;
- Platform Nine / Relay Workbench / Service Tunnel visual equivalence;
- unknown visual family/key renders nothing;
- old scene/location actor-presence heuristic retired from the Android actor consumer;
- fresh surgical merge candidate green under the runtime merge-state gate;
- D-064 evidence + Learning Ledger handoff committed.

### Overlap
Kestrel owns this runtime/test surface. Nodus/Veyra/Veyr review only unless Kestrel explicitly requests a bounded edit.

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
**Mission state:** **DONE / SAFE HANDOFF**. D-069 remains blocked only by D-064 safe handoff; the green-authority checkpoint is already satisfied.

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

Veyra's next gameplay task is D-069. PR #65 / run #351 already proved the green Python + Android + emulator checkpoint. Substantive D-069 implementation waits only for D-064 safe handoff and the Bulletin Board unlock under the runtime merge-state gate. PR #63/#68 are D-064 diagnostic/RED evidence and do not themselves unlock D-069.

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


---

## D-080 — First-wave Player-AI repository learning trail — COMPLETED

**Player-AI:** Veyr  
**Mission state:** **DONE / VERIFIED PRIMARY / NEXT-PLAYER HANDOFF COMPLETE**.

### Verified result
- one evidence-backed Learning Ledger record each for Nodus D-067, Veyra D-068, Kestrel's completed Parallel P2 / D-029 provenance slice, and Veyr D-075;
- each record names the smallest Read First set, proven facts, real implementation owner, trap, validation path, safe extension point, unresolved boundary and direct shortcut;
- `docs/player_guide/FIRST_WAVE_FAST_PATH_AUDIT_2026-10-04.md` resolves four representative repository questions without a full master-corpus reread;
- 15 / 15 referenced source/test/evidence paths resolved at acceptance HEAD `9526fcbead1a37f4d1b0faaf8e3500e539efa691`;
- AGENTS, Mission Control and the field guide already require/link the Learning Ledger handoff;
- D-080's own Next Player Learning Record is present.

### Evidence
- `docs/player_guide/PLAYER_LEARNING_LEDGER.md`;
- `docs/player_guide/FIRST_WAVE_FAST_PATH_AUDIT_2026-10-04.md`;
- Master Task Register D-080 completion record.

### Boundary
- no gameplay/runtime/build/device result is claimed by D-080;
- the Ledger is navigation, not semantic authority;
- the broader D-029 asset program remains open despite the completed Kestrel provenance slice;
- D-080-B machine-readable map was intentionally not created without a concrete consumer/consistency need.

### Next Move
Do not reopen D-080 merely to expand documentation volume. Future completed primary tasks should append compact task-local Learning Ledger records. Veyr returns to bounded narrative/social review availability unless the live Bulletin exposes another eligible task.
