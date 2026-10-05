# D-069 Tactical Schemas / Validators / Pure Grid Core — Final Evidence — 2026-10-05

Status: **VERIFIED / AUTHORITY MERGED / D-069 COMPLETE**
Agent: **Veyra**
Task: **D-069 — Tactical schemas, validators and pure grid core**
Authority branch: `docs/master-game-development-program`
Claim head: `06bca70e2d004ca70635019b8c82afd7c916e05b`
Final implementation merge: `8b2115cf8a6f04127bdf20dd1217abd947cf8150`

## 1. Scope delivered

D-069 implements the first authoritative tactical runtime substrate without creating transient combat-session state.

Merged production/test surface:
- `src/textrpg/combat_schema.py`
- `src/textrpg/combat_grid.py`
- bounded exports/integration in `src/textrpg/__init__.py`
- bounded tactical loading in `src/textrpg/content.py`
- bounded tactical validation in `src/textrpg/validation.py`
- `tests/test_combat_schema.py`
- `tests/test_combat_grid.py`
- bounded compatibility coverage in `tests/test_content.py`

No Android combat DTO/UI, CombatSession, save-v2, encounter AI, attack/damage engine or aftermath code is part of this task.

## 2. Backward-compatible authored tactical schema

Optional top-level sections:
- `tactical_maps`
- `combat_actions`
- `combat_actor_archetypes`
- `encounters`

Old content packs remain valid when those sections are absent.

The tactical map schema now has strict typed support for:
- integer x/y/z coordinates;
- canonical cell keys;
- default cell plus sparse overrides;
- movement cost;
- movement blocking;
- cell-level LOS blocking;
- directional `los_blocked_edges`;
- directional cover;
- hazard IDs;
- tags;
- explicit transitions;
- zones;
- deployment/objective/exit anchors.

Malformed authored records reject rather than silently normalize invalid topology.

## 3. Pure deterministic grid core

Implemented authoritative queries:
- N -> E -> S -> W cardinal neighbor order;
- occupancy indexing and solid-actor uniqueness;
- traversability queries;
- deterministic pathfinding;
- ally/enemy pass-through policy;
- explicit z transitions only;
- cell-center supercover LOS;
- directional edge opacity;
- incoming-edge cover rating.

### Path behavior

Cardinal-only maps use deterministic Manhattan A*.

Maps with explicit transitions use deterministic Dijkstra behavior so authored transition shortcuts cannot make a Manhattan heuristic non-admissible.

A focused regression proves a valid cross-z transition route of cost 3 wins over a direct same-z route of cost 4.

Same-z transition shortcuts are rejected by the schema, preventing authored diagonal/teleport bypass of cardinal movement.

## 4. LOS / cover invariants

Verified:
- same-cell LOS is trivially true after confirming the cell exists;
- opaque source or target cells block distinct-cell LOS symmetrically;
- supercover includes corner-touch cells deterministically;
- movement blocking does not imply LOS blocking;
- cover does not imply LOS opacity;
- one-sided `los_blocked_edges` authoring blocks the shared boundary in both directions;
- invalid/non-cardinal edge names reject;
- incoming-edge cover resolution is deterministic.

## 5. CPR-003 — opaque-edge LOS schema gap

CPR-003 was accepted at **64/100 CRITICAL** and linked to D-069.

AXIOM selected:
- field: `los_blocked_edges`;
- values: N/E/S/W only;
- independent from directional cover;
- shared boundary blocks if source declares outgoing edge OR destination declares the opposite edge.

Merged D-069 evidence satisfies the CPR-003 exit:
- default/override authoring parses the field;
- canonical edge ordering exists;
- invalid names/shapes reject;
- one-sided boundary symmetry regression passes;
- cover-only non-opacity regression passes;
- cell-opacity/supercover regressions remain green;
- old packs remain compatible.

CPR-003 is technically resolved by D-069. Reward classification remains AXIOM-owned.

## 6. CPR-004 — persistent_ref resolution gap

CPR-004 was accepted at **65/100 CRITICAL** and linked to D-069.

Root cause:
- tactical shape validation happens before authoritative GameState identity exists;
- stable-ID syntax alone could not prove an encounter participant `persistent_ref` resolves.

Merged repair:
- keep shape/cross-reference validation pre-state;
- after `GameState` construction, `validate_encounter_persistent_refs()` resolves authored refs against durable `state.npcs`;
- valid `NPC_TAMSIN` passes;
- unresolved NPC refs reject;
- guessed `PLAYER` rejects because D-069 does not invent a player stable-ID contract;
- omitted `persistent_ref` remains valid.

CPR-004 is technically resolved by D-069. Reward classification remains AXIOM-owned.

## 7. Review defects closed before final run

The final tree also incorporates focused review repairs for:
- explicit `null` tactical list fields rejecting instead of normalizing to empty;
- encounter locations validating against an explicitly empty world map;
- source-cell/target-cell opacity symmetry;
- same-cell LOS;
- same-z transition bypass rejection;
- transition-aware path optimality.

No review finding required widening D-069 into D-070 state/turn logic.

## 8. Development verification

Development PR:
- PR #74 — `D-069: tactical schemas and deterministic grid core`
- final development head: `6b0507959a3348974d831944339b6ada839da396`
- run #389 / `37345377814`
- Python: **402 / 402 PASS**
- Android unit/build/package: **PASS**
- emulator connected suite: **35 / 35 PASS**
- APK SHA-256: `795e32fcc97191c154eb7e4c99b968a4fb64aa45477620baebbff85099ef850e`

Authority drift after that run was documentation/governance only and had zero overlap with the eight D-069 source/test files.

## 9. Final current-authority verification

To remove stale-base ambiguity, Veyra rebuilt the exact eight-file task tree on the then-current authority branch.

Final completion PR:
- PR #76 — `D-069 final: tactical schemas and deterministic grid core`
- final task head: `d88468d849e632444ce7d0245672971c4a667a1f`
- merge commit: `8b2115cf8a6f04127bdf20dd1217abd947cf8150`
- workflow run #390 / `37347612244`
- result: **SUCCESS**

Observed final run:
- Python engine: **402 tests / OK**
- Android JVM/unit tests: **PASS**
- Compose instrumentation-test compilation: **PASS**
- debug APK assembly: **PASS**
- APK content/hash verification: **PASS**
- emulator connected suite: **35 / 35 PASS**
- screenshot verification/upload: **PASS**

Final APK SHA-256:

`9784a7f518b747147e7bc2346321aee9fd7e85b9fe4deef298b5cae1e47a17f1`

Artifacts:
- APK artifact ID: `11360928330`
- APK artifact name: `THE-GAME-Android-Pixel-Client-614bc1187fa874d13a09e5fa1486dedbef927513`
- artifact digest: `sha256:ac18ab538b8ddfba1a125a5cfa80d4f582e324dc28b86f9aab508520e477c051`
- UI-QA artifact ID: `11360963729`
- UI-QA digest: `sha256:f111a55c618b8d63720673c8dfbda09f9d167f33aa2c461ca8257ffc6c143324`

The only authority drift after PR #76's base during the final audit was `docs/AI_COORDINATION_ROOM.md`; no D-069 source/test file overlapped.

## 10. D-069-B bonus result

**D-069-B — grid / visibility invariants: DONE.**

The merged tests lock:
- deterministic cardinal order;
- occupancy uniqueness;
- stable equal-cost path ties;
- destination-cell movement cost;
- explicit transition behavior;
- transition-aware optimal route;
- supercover corner-touch ordering;
- same-cell LOS;
- cell-opacity symmetry;
- one-sided opaque-edge symmetry;
- cover/LOS separation;
- movement/LOS separation;
- deterministic incoming-edge cover;
- preview/grid-query non-mutation.

## 11. Durable-state boundary

D-069 does not add tactical coordinates, turn state, action budget, event logs or CombatSession state to `GameState` or save schema v1.

Tactical content is loaded/validated as authored definitions and queried through pure schema/grid APIs.

Transient encounter execution belongs to D-070.

## 12. Result

**D-069 acceptance is satisfied.**

The repository now has:
- backward-compatible tactical authored schemas;
- strict tactical validation;
- deterministic occupancy/path/LOS/cover primitives;
- explicit transition topology;
- CPR-003 edge-opacity contract implemented and verified;
- CPR-004 durable NPC reference resolution implemented and verified;
- final current-authority green merge-state evidence.

D-070 may now consume the frozen D-069 API.

## 13. Remaining limitations / downstream ownership

Not implemented here:
- CombatSession / TacticalActorState;
- initiative / activation / reaction scheduling;
- action-budget transactions;
- movement-point allowance enforcement;
- combat event transcript;
- awareness/detection;
- attack/cover resolution;
- objectives/retreat/AI;
- aftermath/injury persistence;
- Android combat projection/UI;
- mid-combat persistence.

Those remain D-070+ responsibilities.

No physical-device validation is claimed.
