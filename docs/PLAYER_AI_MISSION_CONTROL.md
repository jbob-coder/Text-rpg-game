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

## Veyr — D-065 — Tamsin Memory / Social Reaction

**Player-AI class:** NPC, Social & Narrative-State Lead  
**Mission state:** core implementation/tests already exist in repository history; focus on exact-head proof and closure.

### Mission objective
Prove one existing interaction creates durable Tamsin memory and one later authored behavior reacts to it across save/load, deterministically, without exposing private NPC state.

### Must Read
- `docs/systems/SOCIAL_SCHEMA_API_MIGRATION_PACKET.md`;
- current NPC memory query/effect implementation;
- Tamsin authored shared-entry reaction content;
- D-065 tests;
- persistence paths relevant to NPC nested state;
- player-safe projection path only for redaction verification.

### Already accomplished / do not redo
Repository history already contains:
- read-only NPC memory query;
- exported memory query;
- NPC memory validation/effects;
- semantic NPC memory execution;
- authored Tamsin shared-entry reaction;
- durable-memory reaction test.

### Next Move
1. inspect those commits against current HEAD for drift;
2. prove save -> reload -> later reaction;
3. prove deterministic same-seed behavior;
4. add/confirm negative redaction regression for D-065-B only if primary is green;
5. write evidence and close D-065.

### Exit Gate
- durable Tamsin memory created by an existing interaction;
- later authored state/choice/behavior reacts;
- save/load persistence proven;
- deterministic regression proven;
- private NPC memory/knowledge/goal data remains unavailable to player-safe projection.

### Do Not
- build a general social simulator;
- add a second top-level social owner;
- implement OR-017 nested versioning now unless D-065 cannot close without it.

### Required cross-review
- Nodus: persistence behavior if durable format changes;
- Kestrel: projection/redaction only if presentation contract changes.

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
**Mission state:** newly reassigned; this is the only active primary. D-069 stays blocked.

### Mission objective
Prove the selected Trace Chamber / training activity as one authoritative Phase 1 life-action loop: legality -> cost -> elapsed time -> persistent result -> save/load -> presentation.

### Must Read
- current V10 activity contract / selected Trace Chamber activity authority;
- authoritative training/activity execution source;
- relevant progression/resource/time mutation code;
- save/load tests;
- Android consumer path if a current activity/result surface exists;
- D-068 task acceptance.

### Next Move
1. locate the exact selected activity ID and its existing execution path;
2. write the smallest focused failing test if any acceptance dimension is missing;
3. repair only the missing dimension;
4. prove legality, resource/time cost, persistent result, save/load and available Android projection;
5. close D-068;
6. participate in the green authority checkpoint;
7. only then reclaim D-069 through the runtime merge-state gate.

### Exit Gate
- legal activity entry is deterministic;
- invalid entry rejects cleanly;
- time/resource costs are authoritative and exact;
- result persists;
- save/load preserves result;
- current player-facing projection exposes only intended outcome;
- exact-head evidence recorded.

### Bonus
D-068-B interruption/atomicity regression after primary acceptance.

### Do Not
- start D-069 runtime implementation yet;
- use D-068 to redesign progression;
- move activity legality/math into Kotlin/Compose.

### Required cross-review
- Nodus: persistence/integration;
- Kestrel: only if Android projection shape changes.

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
