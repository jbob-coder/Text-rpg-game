# D-069 Implementation Preflight — Tactical Schemas, Validators & Pure Grid Core

Status: **BLOCKED PREPARATION / NO TASK CLAIM / NO RUNTIME IMPLEMENTATION**
Agent: **Veyra**
Observed authority HEAD: `2479971faf44c8e47b530fa038d7e363c99e4c03`
Date: 2026-10-04 AST

Task:
- D-069 — Implement tactical schemas, validators and pure grid core.

This artifact prepares the first implementation slice without violating the live dependency gate.

D-069 remains blocked until D-064 is synchronized DONE on the Bulletin Board.

Nothing in this packet:
- claims D-069;
- changes GameState;
- adds tactical runtime state;
- implements combat actions;
- changes Android;
- changes save schema;
- overrides the D-064 gate.

---

## 1. Gate state

Current required gate:
- D-060 DONE;
- D-032 migration packet approved;
- D-065 DONE;
- D-067 DONE;
- D-068 DONE;
- PR #65 / run #351 established the green authority checkpoint;
- **D-064 safe handoff remains the sole blocker**.

On unlock:
1. re-fetch live authority HEAD;
2. verify D-064 is actually DONE;
3. promote/confirm D-069 READY on the Bulletin;
4. claim D-069 as Veyra from that exact HEAD;
5. create a short-lived D-069 task branch;
6. re-read the files listed below before writing.

Do not reuse this observed HEAD as the future claim head.

---

## 2. Current source reality

At the observed authority:
- no `src/textrpg/combat_*.py` module exists;
- no combat tests exist under `tests/`;
- GameState has no tactical field;
- save schema remains v1;
- `content_pack_from_mapping` validates current story/RPG content and preserves raw authored data;
- `validation.py` already uses an error-list + assertion pattern suitable for additive tactical validators;
- old content packs contain no tactical sections and must continue loading unchanged.

This means D-069 can be additive and rollback-safe.

---

## 3. Locked authority set

Read before implementation:
- `docs/systems/PHASE_1_COMBAT_SCHEMA_API_MIGRATION_PACKET.md`;
- `docs/systems/TACTICAL_COORDINATE_OCCUPANCY_STANDARD.md`;
- `docs/systems/LOS_DETECTION_AND_COMBAT_KNOWLEDGE_STANDARD.md`;
- `docs/systems/DIRECTIONAL_COVER_TERRAIN_STANDARD.md`;
- `docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md`;
- D-069 entry in `docs/THE_GAME_MASTER_TASK_REGISTER.md`;
- `docs/AI_RUNTIME_MERGE_STATE_GATE.md`.

No broader repository archaeology should be required for the first commit.

---

## 4. First implementation surface

### New modules

`src/textrpg/combat_schema.py`

Owns immutable/validated authored tactical structures for:
- integer x/y/z tactical coordinates;
- tactical cell/map definitions;
- explicit z transitions;
- deployment zones;
- objective anchors;
- exits;
- combat action definitions;
- actor archetype definitions;
- encounter definitions.

It must not own:
- mutable encounter state;
- action resolution;
- AI;
- aftermath;
- Android DTOs.

`src/textrpg/combat_grid.py`

Owns pure deterministic spatial functions:
- coordinate keying;
- N -> E -> S -> W cardinal adjacency;
- bounds;
- occupancy queries;
- traversability;
- deterministic pathfinding;
- explicit vertical-transition traversal;
- cell-center supercover LOS;
- incoming-edge cover selection.

It must be side-effect free and must not mutate GameState.

### Bounded current-file additions

`src/textrpg/content.py`
- read optional top-level:
  - `tactical_maps`;
  - `combat_actions`;
  - `combat_actor_archetypes`;
  - `encounters`;
- missing sections remain valid;
- retain backward compatibility with existing packs.

`src/textrpg/validation.py`
- add dedicated tactical validators;
- reject malformed records;
- cross-reference encounters/maps/actions/archetypes and existing registries where required;
- preserve the existing validation style.

`src/textrpg/__init__.py`
- export only stable public tactical schema/grid interfaces needed by tests/consumers.

### New tests

`tests/test_combat_schema.py`

`tests/test_combat_grid.py`

Compatibility additions may be made to:
- `tests/test_content.py`;
- `tests/test_validation.py`.

---

## 5. Tactical schema invariants

### Coordinate

Phase 1 coordinate:
- x: integer;
- y: integer;
- z: integer.

Cell key:
- `x,y,z`.

Tactical coordinates are not:
- world coordinates;
- room-visual coordinates;
- Android screen coordinates.

### Tactical map

Minimum target record contains:
- map_id;
- version;
- width;
- height;
- z_layers;
- default_cell;
- overrides;
- transitions;
- deployment_zones;
- objective_anchors;
- exits.

Validate:
- stable uppercase IDs where required;
- positive dimensions;
- unique/in-bounds cells;
- finite positive movement cost for traversable cells;
- N/E/S/W cover edges only;
- valid transition endpoints;
- valid deployment/objective/exit anchors;
- no silent topology repair.

### One-cell occupancy

Phase 1:
- one solid actor per final occupied cell;
- enemy pass-through forbidden;
- ally pass-through explicit policy;
- blocked cells cannot be endpoints;
- non-solid markers never own occupancy.

---

## 6. Pure-grid contract

### Cardinal order

Always enumerate:
1. north: y - 1;
2. east: x + 1;
3. south: y + 1;
4. west: x - 1.

No diagonal movement.

### Pathfinding

Use deterministic A* or Dijkstra.

Same-z Manhattan heuristic.

Movement cost:
- destination cell;
- or explicit transition edge.

Stable tie behavior must be deterministic.

Approved tie tuple:
`(f_cost, h_cost, y, x, z, cell_key)`.

Preview and committed movement later must use the same query semantics.

### Vertical movement

No implicit z adjacency.

Only explicit authored transitions may connect z layers.

### LOS

Use deterministic cell-center supercover.

Required properties:
- include corner-touch cells;
- stable enumeration;
- movement blocking does not imply LOS blocking;
- opaque cell/edge stops LOS;
- canonical edge-opacity field is `los_blocked_edges`;
- a shared boundary is opaque when either adjacent cell declares the corresponding edge/opposite edge;
- cover ratings never imply LOS opacity;
- golden corner cases are mandatory.

### Cover

Target-cell incoming edge determines cover.

Ratings:
- 0 = none;
- 1 = partial;
- 2 = strong.

Phase-1 modifiers (+0/+10/+20) belong to later attack resolution; D-069 only needs the deterministic rating/edge query.

No hidden flank bonus.

---

## 6.1 CPR-003 resolution — opaque edge authoring

AXIOM resolved the schema ambiguity before D-069 completion.

Locked representation:
- canonical/authored cell field: `los_blocked_edges`;
- allowed values: N/E/S/W only;
- independent from `cover`;
- a shared boundary is blocked if either adjacent cell declares that edge/opposite edge;
- reciprocal duplicate authoring is allowed but not required;
- runtime LOS must therefore produce the same blocked result A→B and B→A for one one-sided authored opaque boundary.

The first D-069 schema/grid branch already uses this field and checks both sides of the boundary. Remaining work is to synchronize authored parsing/validation and add/retain symmetry + invalid-edge regressions.

Do not invent a structured edge-object schema in D-069.

## 7. Minimum D-069 test matrix

### Backward compatibility
- old content pack without tactical sections still loads;
- empty optional tactical sections do not mutate existing content behavior;
- no GameState/save-schema field appears.

### Schema / validation
- tactical section must be mapping;
- malformed record rejected;
- duplicate coordinate rejected;
- out-of-bounds coordinate rejected;
- non-positive traversable movement cost rejected;
- invalid cover edge rejected;
- invalid transition rejected;
- invalid deployment/objective/exit anchor rejected;
- encounter unknown map rejected;
- encounter unknown action/archetype rejected;
- existing condition/knowledge/item references validated where applicable.

### Coordinate / occupancy
- cell-key round trip;
- N/E/S/W order;
- no diagonal adjacency;
- blocked endpoint rejected;
- occupied endpoint rejected;
- enemy pass-through rejected;
- ally pass policy explicit.

### Path
- deterministic equal-cost path;
- no diagonal shortcut;
- destination movement cost used;
- explicit z-transition path;
- unavailable z transition rejected.

### LOS
- straight clear LOS;
- opaque cell block;
- opaque edge block using `los_blocked_edges`;
- reverse-direction symmetry across the same one-sided authored opaque boundary;
- cover/LOS-opacity separation;
- invalid `los_blocked_edges` edge rejection;
- movement-blocker / LOS-blocker separation;
- corner supercover golden case;
- symmetry where contract says symmetry is appropriate.

### Cover
- correct incoming edge;
- none/partial/strong rating;
- deterministic corner case;
- cover separate from LOS blocker.

### Bonus D-069-B candidate invariants
- path result is stable across repeated identical queries;
- LOS result is stable across repeated identical queries;
- occupancy never changes during preview queries;
- same geometry produces the same incoming cover edge;
- hidden occupancy is not introduced into public grid helpers.

---

## 8. Explicit non-goals

Do not implement in D-069:
- CombatSession;
- TacticalActorState mutation;
- initiative/turn engine;
- action budgets;
- attack/damage;
- detection/awareness state;
- AI scoring;
- objectives/retreat state;
- aftermath;
- bridge combat projection/actions;
- Kotlin combat DTOs;
- Compose tactical UI;
- Gate Twelve encounter content;
- save schema v2.

Those belong to D-070+ / D-073 / D-074 and later accepted work.

---

## 9. First-commit recommendation after unlock

The safest first D-069 commit is:

1. `combat_schema.py` coordinate/map schema foundations;
2. `combat_grid.py` coordinate/cardinal/bounds/occupancy primitives;
3. `tests/test_combat_schema.py`;
4. `tests/test_combat_grid.py`;
5. no content-loader integration until the pure structures/tests are green.

Second commit:
- optional tactical content parsing/validation;
- compatibility tests for missing sections.

Third commit:
- deterministic path/supercover/cover golden tests;
- D-069-B invariants if primary acceptance is already coherent.

This commit order minimizes blast radius and makes regressions attributable.

---

## 10. Verification plan

Required local/CI command once implementation begins:

`PYTHONPATH=src python -m unittest discover -s tests -v`

Record:
- exact task-branch HEAD;
- exact authority merge base/current HEAD;
- test count;
- failures;
- PR number;
- workflow run;
- merge-state result;
- resulting authority HEAD.

Do not mark D-069 DONE while merge-state CI is red.

---

## 11. Immediate next action

**Blocked on D-064 handoff only.**

When D-064 becomes DONE:
- this preflight becomes the fast-start checklist;
- revalidate live source/contract drift;
- claim D-069;
- begin the first commit above.

If D-064 changes tactical/content contracts while closing, update this preflight before implementation rather than silently carrying stale assumptions.
