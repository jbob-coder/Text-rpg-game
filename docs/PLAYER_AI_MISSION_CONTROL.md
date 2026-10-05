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

`D-069` **READY — Veyra designated next claimant**
↓
`D-070 -> D-071 -> D-072 -> D-073 -> D-074`
↓
`D-076 -> D-077 -> D-078 -> D-079`
↓
**Phase 1 integrated acceptance candidate**

D-064/D-065/D-067/D-068 and D-075 are DONE. The green authority checkpoint is established. The current gameplay job is D-069 tactical schemas/grid core.

---

## Kestrel — D-064 — Projection / Presentation

**Player-AI class:** Player-Safe Projection, Presentation & Asset Lead  
**Mission state:** **DONE / PRIMARY + D-064-B VERIFIED / CPR-002 RESOLVED**.

### Verified result
- player-safe `room.actors` now owns story-actor presence in Android;
- `visualFamily` selects presentation sprite;
- `placementKey` resolves semantic coordinates;
- scene/location actor-presence heuristics are retired from `PixelStoryActorCatalog`;
- strict Kotlin actor-map allowlist rejects unauthorized/private extra keys;
- opening Platform Nine / Relay Workbench / Service Tunnel equivalence is tested;
- fallback scene catalog is regression-protected.

### Final evidence
- authority merge: `d7ebb7ca439695e256a429a1e5d160daae69a521`;
- PR #70 head: `014e05c9f5e451d8fb9eb552a9ba20e7cd1ed5ff`;
- workflow run #362 / `37261943012`;
- Python **355/355 OK**;
- Android unit/build/package PASS;
- emulator smoke/screenshots PASS;
- APK SHA-256 `1d1c974dba2a65ac94d3ac5bfa9b60f8725d360c01eab9b4a36add7f9133bb46`;
- evidence: `docs/evidence/D064_PLAYER_SAFE_ROOM_ACTOR_PROJECTION_FINAL_2026-10-05.md`;
- Learning Ledger: `D-064 — Projected room actors replace presentation heuristics`.

### CPR-002
**RESOLVED — 74/100 CRITICAL.**

Kestrel: **+235 critical root-cause reward**.  
Veyr: **+10 peer FIND credit**.

### Next Move
Do not reopen D-064 without new regression evidence. Kestrel is free for future projection/presentation review work after re-fetching the live Bulletin.


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

## Veyra — D-069 — Tactical Schemas / Pure Grid Core

**Player-AI class:** Gameplay Systems & Tactical Lead  
**Mission state:** **IN_PROGRESS — CLAIM WON / TACTICAL CORE ACTIVE**.

### Claim / unlock state
The transition gate is satisfied.

- D-064/D-065/D-067/D-068 are DONE.
- PR #65 / run #351 is the green authority checkpoint.
- D-064 final PR #70 / run #362 merged at `d7ebb7ca439695e256a429a1e5d160daae69a521`.
- Veyra won the live Bulletin claim for D-069.
- **CLAIM_HEAD:** `06bca70e2d004ca70635019b8c82afd7c916e05b`.
- **CLAIMED_AT:** 2026-10-05T12:17:00-04:00.

Do not repeat the unlock/claim sequence. Continue from the winning claim under `docs/AI_RUNTIME_MERGE_STATE_GATE.md`.

### Read first for active implementation
1. live Bulletin D-069;
2. `docs/evidence/D069_IMPLEMENTATION_PREFLIGHT_2026-10-04.md`;
3. `docs/AI_RUNTIME_MERGE_STATE_GATE.md`;
4. `docs/systems/PHASE_1_COMBAT_SCHEMA_API_MIGRATION_PACKET.md`;
5. `docs/systems/TACTICAL_COORDINATE_OCCUPANCY_STANDARD.md`;
6. `docs/systems/LOS_DETECTION_AND_COMBAT_KNOWLEDGE_STANDARD.md`;
7. `docs/systems/DIRECTIONAL_COVER_TERRAIN_STANDARD.md`;
8. only the current source files named below.

### Objective
Add backward-compatible authored tactical schemas plus pure deterministic tactical-grid primitives.

D-069 owns:
- optional tactical content schema/validation;
- integer x/y/z tactical coordinates;
- cardinal N -> E -> S -> W adjacency;
- bounds and occupancy queries;
- deterministic pathfinding;
- explicit vertical transitions;
- deterministic cell-center supercover LOS;
- incoming-edge cover resolution.

D-069 does **not** own:
- CombatSession or mutable tactical actor state;
- turns/action budgets;
- attack/damage;
- awareness AI;
- objectives/retreat runtime;
- aftermath;
- Gate Twelve encounter content;
- Android combat bridge/DTO/UI;
- save-schema v2 or mid-combat persistence.

### First implementation surface
New:
- `src/textrpg/combat_schema.py`
- `src/textrpg/combat_grid.py`
- `tests/test_combat_schema.py`
- `tests/test_combat_grid.py`

Bounded additions:
- `src/textrpg/content.py`
- `src/textrpg/validation.py`
- `src/textrpg/__init__.py`
- compatibility tests only where required.

### Recommended commit order
**Commit 1 — pure foundations**
- coordinate/map schema foundations;
- coordinate keying;
- N/E/S/W adjacency;
- bounds/occupancy primitives;
- focused schema/grid tests;
- no content-loader integration yet.

**Commit 2 — optional authored content**
- optional `tactical_maps`;
- optional `combat_actions`;
- optional `combat_actor_archetypes`;
- optional `encounters`;
- validation/cross-reference coverage;
- old packs without tactical sections remain valid.

**Commit 3 — deterministic geometry**
- equal-cost path tie rules;
- explicit z transitions;
- supercover LOS golden cases;
- cover incoming-edge determinism;
- D-069-B invariants when primary acceptance is coherent.

### Locked deterministic rules
- no diagonal movement;
- cardinal enumeration N -> E -> S -> W;
- same-z Manhattan heuristic;
- stable path tie tuple `(f_cost, h_cost, y, x, z, cell_key)`;
- movement cost comes from destination cell or explicit transition;
- enemy pass-through forbidden;
- ally-pass policy explicit;
- one solid final occupant per Phase-1 cell;
- no implicit z adjacency;
- LOS uses deterministic cell-center supercover and includes corner-touch cells;
- movement blocking does not automatically block LOS;
- cover uses target incoming edge;
- cover ratings: 0 none / 1 partial / 2 strong.

### Runtime merge-state workflow
After unlock:
1. append Coordination Room `INTENT`;
2. claim D-069 from live authority;
3. append `START`;
4. create a short-lived task branch;
5. implement the bounded commit sequence;
6. run focused/full Python tests;
7. open PR to `docs/master-game-development-program`;
8. require merge-state CI under `docs/AI_RUNTIME_MERGE_STATE_GATE.md`;
9. repair only demonstrated drift;
10. evidence + Learning Ledger + FINISH + Brag/Scoreboard/Register/Bulletin.

### Verification
Required command:
`PYTHONPATH=src python -m unittest discover -s tests -v`

Record:
- claim/task branch HEAD;
- authority merge base/current HEAD;
- test count/failures;
- PR/workflow;
- merge-state result;
- resulting authority HEAD.

### Bonus D-069-B
Candidate invariant packet:
- deterministic repeated path query;
- deterministic repeated LOS query;
- preview queries do not mutate occupancy;
- same geometry returns same incoming cover edge;
- no hidden occupancy introduced into public grid helpers.

### Current action
**Implement D-069 from the winning claim head.**

Use `docs/evidence/D069_IMPLEMENTATION_PREFLIGHT_2026-10-04.md` as the direct implementation shortcut. Keep D-070 turn/session state out of D-069.

### Active execution sequence
1. preserve the winning Bulletin claim;
2. append/maintain Coordination Room START/UPDATE state;
3. create/use the short-lived D-069 task branch from the exact claim-era authority;
4. execute the bounded commit sequence above;
5. run focused/full Python tests;
6. open PR to `docs/master-game-development-program`;
7. require merge-state CI;
8. repair only demonstrated drift;
9. evidence + Learning Ledger + FINISH + Brag/Scoreboard/Register/Bulletin.

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

## Quorix — Verification / Red-Team / Performance

**Status:** ACTIVE FIFTH PLAYER-AI / Parallel P5 D-042 bounded lane DONE.

### Verified result
- bounded cross-branch survivor audit completed for PR #27/#28/#30/#31;
- D-064, D-065/D-068 and D-067 completion heads independently confirmed in current authority ancestry at audit HEAD `f5c3731d0c494dd3948f88481a3d5b2d3d0f4138`;
- PR #27 Service Tunnel and PR #30 Quiet Stair static source+raster pairs classified as deferred D-029 migration candidates;
- PR #28 classified as a deferred arrival-preview presentation candidate;
- PR #31 ambient fan/panel/drip animation classified **REIMPLEMENT BEFORE MIGRATION** because the current composition standard requires reduced-motion behavior absent from that branch;
- stale D-042 remainder text that still treated completed D-020/D-044 work as open was corrected;
- machine-readable survivor matrix completed and verified.

### Evidence
- `docs/evidence/P5_D042_CROSS_BRANCH_SURVIVOR_AUDIT_2026-10-05.md`;
- `docs/evidence/P5_D042_CROSS_BRANCH_SURVIVOR_MATRIX_2026-10-05.json`;
- Learning Ledger: `P5 / D-042 — Raster-first presentation changes the migration unit`.

### Important boundary
Parallel P5 is DONE as a bounded lane. Master D-042 remains IN_PROGRESS for broader D-021/D-026 consumer work, D-029 asset lineage/visual promotion, deprecation proof and future materially unclassified branch families.

No Python/Android runtime tests, APK build, emulator/device run, raster-equivalence execution, visual promotion or branch merge is claimed by P5.

### Next Move
Do not reopen the P5 slice without new branch evidence. Remain available for independent verification/red-team review while Veyra owns D-069 and Strata owns D-083.

Preferred downstream leadership when unlocked:
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

PR #65 / workflow run #351 is the established transition checkpoint.

Verified:
- complete Python suite: **PASS**;
- Android unit/build/package: **PASS**;
- emulator smoke/screenshots: **PASS**;
- APK SHA-256: `7dfc02e4b6ce95fc0fb6ba6dbe1869366993cd6388811627efdc2deb7daeefda`.

D-065, D-067 and D-068 are DONE. D-064 safe handoff is the sole remaining transition gate before D-069.

## Green Authority Checkpoint

**Status:** SATISFIED by PR #65 / run #351.

This is no longer future work.

Current tactical unlock rule:
- D-064 synchronized DONE;
- Bulletin promotes D-069 READY;
- Veyra claims from the then-live authority HEAD under the runtime merge-state gate.

Do not rerun or recreate the transition checkpoint merely because documentation/governance HEAD moved. Re-run integration only when runtime/test/content drift makes new evidence necessary.

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
