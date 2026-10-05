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

## Critical path to a complete Phase 1

`D-064 + D-065 + D-067 + D-068`
↓
**one green authority checkpoint**
↓
`D-069 -> D-070 -> D-071 -> D-072 -> D-073 -> D-074`
↓
`D-075 -> D-076 -> D-077 -> D-078 -> D-079`
↓
**Phase 1 integrated acceptance candidate**

The current job is to close the four transition tasks without expanding them.

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
**Mission state:** implementation + proof tests exist; finish exact-head integration evidence and handoff.

### Mission objective
Prove one bounded Phase 1 obtain/possess/equip/use loop across authoritative Python state, persistence and Android player-safe presentation.

### Must Read
- `docs/systems/PHASE_1_ITEMS_ECONOMY_SCHEMA_API_MIGRATION_PACKET.md`;
- authoritative inventory/equipment state implementation;
- D-067 proof tests including canonical session factory coverage;
- Android inventory/equipment mapper/tests;
- save/load path for inventory/equipment.

### Already accomplished / do not redo
Repository history already contains:
- authoritative inventory hardening;
- integrated Phase 1 inventory/equipment proof test;
- Android inventory projection hardening;
- strict inventory projection mapping test;
- canonical-session-factory D-067 regression.

### Next Move
1. inspect current HEAD for drift since those commits;
2. run/obtain exact-head Python + save/load + Android evidence;
3. repair only concrete failures;
4. close D-067;
5. after handoff, switch to integration checkpoint work rather than reopening D-068.

### Exit Gate
- acquisition/possession and at least one meaningful equipment/use mutation proven;
- invalid mutation cannot partially corrupt state;
- save/load preserves authoritative inventory/equipment;
- Android renders player-safe current state;
- exact-head evidence recorded.

### Bonus
D-067-B invalid-equip/rollback atomicity only after primary acceptance.

### Do Not
- add currency/vendor/crafting scope;
- redesign item schema when bounded proof already works.

### Required cross-review
- Kestrel: Android presentation fields if mapper surface changes;
- Veyra: only if equipment modifies gameplay/tactical contract.

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

Veyra's next gameplay task is D-069, but substantive tactical implementation must not begin until:
1. D-064, D-065 and D-067 reach safe handoff;
2. one complete Python authority checkpoint is green;
3. required Android integration gates for the transition state are green;
4. the Bulletin Board reopens D-069 under the runtime merge-state gate.

Until then Veyra may assist with bounded integration/checkpoint evidence or read-only D-069 preparation, but must not bypass the gate.

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
