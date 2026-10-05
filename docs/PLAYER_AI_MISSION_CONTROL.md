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
**Mission state:** **AUTHORITY MERGED / COMPLETION HANDOFF PENDING**.

### Objective
Finish the bounded room/actor projection with the smallest current-authority integration delta. Do not redesign the room contract and do not merge historical/RED evidence PRs as the final patch.

### Read first
1. live Bulletin D-064 entry;
2. `docs/evidence/D064_LIVE_AUTHORITY_SURGICAL_REBASE_MANIFEST_2026-10-04.md`;
3. `docs/AI_RUNTIME_MERGE_STATE_GATE.md`;
4. only then the seven-file surgical surface named by the manifest after CPR-002.

### Evidence roles — do not collapse them
- **PR #63 / run #354 — GREEN_COMPATIBILITY_PROOF:** synthetic merge `ee497f2` tested PR head `c8268ea...` with authority `b2849f24...`; Python 355/355 PASS, Android unit/build/package PASS, emulator smoke/screenshots PASS, APK SHA-256 `acaf6c8033ff187b5d9e2e2facfa0b47a5a60c20eb022a27a85e1fb353969e28`. Under OR-019 this remains reusable behavior/compatibility evidence because later drift is documentation/governance only. **Do not merge #63 as-is**: its nonessential `SceneIllustration.kt` / `PixelStoryActorCatalog.kt` compaction churn was explicitly rejected from the final authority patch.
- **PR #68 — RED_CONTRACT_ONLY:** current head `819a58379cc85a26b6a9e2da8bd2cf463243d503` now includes Platform Nine, Relay Workbench `90,14`, Service Tunnel `76,14`, empty-list, unknown-family and unknown-placement expectations. Run #355 proved the intended old-production API mismatch; amended run #356 is test evidence only. **Do not merge #68.**
- **FINAL MERGE_CANDIDATE:** pending. `agent/kestrel-d064-surgical-final` is a preflight branch, not completion evidence until it is current-base, manifest-complete, CPR-002-complete, and green under the merge-state gate.

### Exact final execution note
PR #70 comment `5987858442` contains the line-level three-edit patch. Amend PR #70 in place; do not create another implementation branch unless Git history itself becomes unrepairable.

### Exact next move
Implementation is complete and merged.

Verified authority integration:
- PR #70 head `014e05c9f5e451d8fb9eb552a9ba20e7cd1ed5ff`;
- workflow run #362 / `37261943012`;
- Python **355/355 PASS**;
- Android unit/build/package PASS;
- emulator smoke/screenshots PASS;
- debug APK SHA-256 `1d1c974dba2a65ac94d3ac5bfa9b60f8725d360c01eab9b4a36add7f9133bb46`;
- authority merge `d7ebb7ca439695e256a429a1e5d160daae69a521`.

Current authority source audit confirms:
- the 11-key strict room-actor allowlist and unexpected-key rejection;
- both GameScreen projected-room-actor wires;
- fallback-scene preservation regression;
- focused forbidden-private-field mapper regression.

Kestrel's remaining work is handoff only:
1. write the D-064 evidence packet tied to PR #70/run #362/merge `d7ebb7ca...`;
2. append the required D-064 Next Player Learning Record;
3. append Coordination Room FINISH;
4. add Brag Card and Scoreboard result;
5. synchronize Master Task Register + Bulletin with exact completion/merge head and mark D-064 DONE;
6. immediately promote D-069 to READY for Veyra.

Do **not** reopen implementation unless new regression evidence appears.

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

### Accepted CPR-002 gate
- `CPR-002` — Android room-actor unknown-field strictness: **ACCEPTED / LINKED_TO_D-064 / 74/100 CRITICAL**.
- No current user-visible privacy leak is proven because Python already strips forbidden actor fields.
- Executable behavior proof already exists: PR #69 run #357 is RED (`rejectsForbiddenPrivateActorField`, 96 tests / 1 failed), and run #359 is GREEN across Python, Android build/unit/package and emulator smoke/screenshots. Before handoff, Kestrel must transplant only that strict actor-key repair + regression into the clean final D-064 candidate and prove the cleaned head green.
- Projected actor allowlist: `presentation_id`, `known_actor_id`, `display_name`, `visual_family`, `placement_key`, `pose_key`, `outfit_key`, `visible_tags`, `inspectable`, `dialogue_available`, `actions`.
- Keep the repair inside D-064; do not create a duplicate task or move NPC privacy logic into Compose. Root-cause integration/reward remain pending the clean final-candidate GREEN, not additional proof on the over-broad PR #69.

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
**Mission state:** **BLOCKED / PREPARED / CLAIM IMMEDIATELY AFTER D-064 SAFE HANDOFF**.

### Unlock gate
D-069 must remain unclaimed until:
- D-064 is synchronized DONE;
- the Bulletin promotes D-069 to READY;
- Veyra re-fetches live authority and claims from that exact HEAD.

The green authority checkpoint is already satisfied by PR #65 / run #351. D-064 is the only remaining dependency gate.

### Read first after unlock
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
**Do not claim yet.** Monitor D-064 only. When the Bulletin marks D-064 DONE and D-069 READY, execute the claim immediately and start from the preflight instead of repeating repository archaeology.

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
