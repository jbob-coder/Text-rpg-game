# D-069 — Tactical Schemas, Validators and Pure Grid Core — Final Evidence

Status: **DONE / AUTHORITY MERGED / FINAL COMPLETION GATE GREEN**

Player-AI: **Veyra**  
Task: **D-069**  
Claim head: `06bca70e2d004ca70635019b8c82afd7c916e05b`  
Final task branch: `agent/veyra-d069-final`  
Final branch head: `d88468d849e632444ce7d0245672971c4a667a1f`  
PR: **#76 — D-069 final: tactical schemas and deterministic grid core**  
Workflow run: **#390 / 37347612244**  
Synthetic tested merge: `614bc11` = PR head merged into `ae44e3a8a66868f5aac1ec7a16712e6e167452bc`  
Authority merge / completion head: `8b2115cf8a6f04127bdf20dd1217abd947cf8150`

## 1. What shipped

D-069 adds the bounded authored tactical schema and deterministic pure-grid foundation required before transient combat state can exist.

Authority now contains:

- `src/textrpg/combat_schema.py`
  - integer x/y/z tactical coordinates;
  - tactical cells;
  - movement/LOS/cover metadata;
  - deployment/objective/exit anchors;
  - explicit z-changing transitions;
  - tactical maps;
  - combat actions;
  - combat actor archetypes;
  - encounters;
  - strict authored parsing/validation helpers.

- `src/textrpg/combat_grid.py`
  - N -> E -> S -> W cardinal neighbors;
  - occupancy validation;
  - deterministic pathing;
  - transition-aware optimal routing;
  - deterministic cell-center supercover;
  - LOS with cell- and edge-opacity separation;
  - directional incoming-edge cover resolution.

- bounded integration in:
  - `src/textrpg/content.py`;
  - `src/textrpg/validation.py`;
  - `src/textrpg/__init__.py`.

- regression coverage in:
  - `tests/test_combat_schema.py`;
  - `tests/test_combat_grid.py`;
  - `tests/test_content.py`.

No D-070 transient `CombatSession`, turn state, action resolution, tactical AI, Android combat DTO/UI, aftermath or save-schema expansion was added.

## 2. Backward compatibility and state boundary

The tactical sections remain optional.

Old content packs with no tactical data continue to load.

The implementation does not add tactical state to `GameState` or save schema v1.

D-069 owns static authored schema, validation and pure grid queries only.

Durable encounter `persistent_ref` validation is deliberately split:
- shape/stable-ID validation remains pre-state;
- after `GameState` construction, non-empty encounter `persistent_ref` values resolve against durable `state.npcs`;
- unresolved NPC refs reject;
- no player stable-ID sentinel was invented.

## 3. Deterministic grid invariants

Executed tests cover the D-069 contract, including:

- cardinal neighbor order N -> E -> S -> W;
- no diagonal movement;
- occupancy uniqueness;
- blocked destination and enemy pass-through rejection;
- explicit ally pass-through policy;
- destination-cell movement cost;
- deterministic equal-cost path tie;
- explicit vertical transitions;
- same-z transition shortcuts rejected;
- transition-aware optimal routing uses Dijkstra when explicit transitions exist;
- stable supercover corner-touch ordering;
- same-cell LOS is trivially true;
- opaque cell LOS blocking;
- movement blocker vs LOS blocker separation;
- directional edge opacity;
- one-sided opaque edge blocks LOS in both directions;
- directional cover does not imply LOS opacity;
- opaque source/target endpoint symmetry;
- deterministic incoming-edge cover;
- preview/grid queries do not mutate occupancy.

These invariants satisfy **D-069-B**.

## 4. Strict authored validation

Executed schema/content tests also cover:

- optional tactical sections default cleanly;
- malformed tactical roots reject;
- duplicate/out-of-bounds cells reject;
- unknown transition/deployment/objective/exit references reject;
- authored `los_blocked_edges` parses from default and override cells;
- invalid/non-cardinal LOS edges reject;
- explicit `null` tactical list fields reject instead of silently normalizing;
- action/archetype unknown fields and cross-references reject;
- encounter map/archetype/action/deployment references reject;
- encounter location rejects against an explicitly empty world-map node set;
- valid tactical content loads without mutating `GameState`;
- persistent NPC ref must resolve to durable `state.npcs`.

## 5. CPR-003 — opaque-edge LOS schema gap

CPR-003 was accepted at **64/100 CRITICAL** and linked to D-069.

The selected contract is now implemented and authority-merged:

- canonical authored field: `los_blocked_edges`;
- legal values: N/E/S/W;
- independent from directional cover;
- default-cell and sparse override parsing supported;
- invalid edge names reject;
- shared boundary is opaque when either adjacent cell declares the matching edge/opposite edge;
- one-sided authoring remains LOS-symmetric.

Focused regressions include:
- `test_authored_los_blocked_edges_parse_from_default_and_override`;
- `test_authored_map_rejects_non_cardinal_los_blocked_edge`;
- `test_opaque_edge_blocks_los`;
- `test_one_sided_opaque_edge_blocks_los_in_both_directions`;
- `test_cover_alone_does_not_block_los`.

Causal repair status: **GREEN ON AUTHORITY**.  
Any Critical Root-Cause reward remains AXIOM-owned.

## 6. CPR-004 — persistent_ref resolution gap

CPR-004 was accepted at **65/100 CRITICAL** and linked to D-069.

The selected repair is now implemented and authority-merged:

- tactical shape validation remains pre-state;
- `validate_encounter_persistent_refs()` runs after `GameState` construction;
- valid `NPC_TAMSIN` ref passes;
- unresolved `NPC_DOES_NOT_EXIST` rejects;
- guessed `PLAYER` ref rejects because D-069 does not invent player identity;
- omitted `persistent_ref` remains valid.

Focused content regression:
- `test_tactical_persistent_ref_must_resolve_to_durable_npc`.

Causal repair status: **GREEN ON AUTHORITY**.  
Any Critical Root-Cause reward remains AXIOM-owned.

## 7. Final merge-state execution evidence

PR #76 run #390 / `37347612244` completed **SUCCESS**.

### Python

Job: `111890068014`

Observed:
- checkout: synthetic merge `614bc11`;
- **402 tests**;
- **OK**.

### Android unit/build/package

Job: `111890068277`

Observed:
- `testDebugUnitTest`: PASS;
- `assembleDebugAndroidTest`: PASS;
- `assembleDebug`: PASS;
- debug APK SHA-256:
  `9784a7f518b747147e7bc2346321aee9fd7e85b9fe4deef298b5cae1e47a17f1`.

### Android emulator / screenshots

Job: `111890068242`

Observed:
- **35 tests** started;
- **35/35 completed with 0 failed**;
- emulator job PASS;
- screenshot verification PASS.

Observed screenshot hashes include:
- `inventory-320dp.png` — `fdf17df17117e6939cdd0074897fe194cc24c55020ac13646769be18b7b8fe4f`;
- `map-gate-twelve-320dp.png` — `868a0e2b81aaf3ce1d591535bc8a5372caaece771b7931ab177a4f3e747e8856`;
- `skills-320dp.png` — `0b5fa73c7a30d2903a60c01ea21391ec85924fbbbeec1e0d6feed89b8b9dbde9`;
- `stats-320dp.png` — `915cf335499824c34613156af8eee4a8af678d932e0fc8154d86de0cbe8ebe19`;
- `stats-perception-detail.png` — `1781438d8c8f179f05e3bc635c175df90d981e5a660e05816867ecb7bf34ca4b`.

## 8. Merge-state and authority drift

The final PR changed exactly eight D-069 source/test files.

Pre-merge authority drift after the tested base:
- `ae44e3a8a66868f5aac1ec7a16712e6e167452bc` -> `9c6e197d19364e9061b0b2048345436ae92035a9`;
- one file changed: `docs/AI_COORDINATION_ROOM.md`;
- zero overlap with the D-069 implementation/test surface.

PR #76 remained clean/mergeable and was merged into authority as:

`8b2115cf8a6f04127bdf20dd1217abd947cf8150`

No post-test gameplay/runtime repair was required.

## 9. Review defects absorbed before completion

D-069 also closed all task-local review findings reported during implementation:

- explicit tactical-list `null` rejection;
- encounter location validation against explicit empty world-map nodes;
- source/target opaque-cell LOS symmetry;
- same-cell LOS contract;
- same-z transition bypass rejection;
- transition-aware path optimality with explicit z shortcuts;
- CPR-003 edge-opacity contract;
- CPR-004 persistent durable-NPC ref resolution.

Earlier cancelled workflow runs were superseded by branch pushes and are not counted as test failures.

## 10. Acceptance result

D-069 acceptance is **SATISFIED**.

Verified:
- backward-compatible tactical schemas;
- deterministic coordinate/occupancy/path/LOS/cover core;
- strict malformed-topology rejection;
- edge-opacity contract;
- persistent NPC ref resolution;
- no tactical `GameState` / save-schema expansion;
- current merge-state Python + Android + emulator green evidence.

Bonus **D-069-B** is **DONE** through deterministic grid/path/visibility/cover invariant regressions.

## 11. What remains downstream

D-070 owns:
- transient `CombatSession`;
- tactical actor runtime state;
- initiative/activation;
- four-unit action budget;
- movement allowance transaction rules;
- reaction reserve/consume/expire;
- deterministic reaction ordering;
- reinforcement admission;
- committed event sequence / preview non-consumption.

D-071 and later tasks retain awareness, attack/cover effects, objectives/retreat/AI, aftermath and Android combat presentation.

D-069 should not be reopened unless new regression evidence demonstrates a defect in its frozen schema/grid contract.
