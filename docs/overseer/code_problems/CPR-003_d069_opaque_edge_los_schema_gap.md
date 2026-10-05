# CPR-003 — D-069 opaque-edge LOS schema gap

- **REPORTER:** Vector — independent Verification / Red-Team review
- **CURRENT_TASK:** no primary claim; read-only review of active D-069
- **OBSERVED_HEAD:** `04100a044cbb22248d0940493661144ae9868c38`
- **FAILURE:** D-069's normative LOS contract and preflight require opaque **edge** blockers and an `opaque edge block` regression, but the approved authored tactical schema does not define a distinct field/record that can encode LOS opacity on a directional edge. The current cell schema defines cell-level `blocks_los` and directional cover metadata only, while the cover authority explicitly states that cover is separate from LOS blocking.
- **EXPECTED_BEHAVIOR:** D-069 must have one explicit authoritative representation for N/E/S/W edge LOS opacity, validated independently from directional cover, so the pure grid can implement and test opaque wall-edge LOS without inventing schema or treating cover as opacity.
- **REPRODUCTION:**
  1. Read `docs/systems/TACTICAL_COORDINATE_OCCUPANCY_STANDARD.md`: tactical cells may define `blocks_los` and edge cover metadata; no edge-LOS field is defined.
  2. Read `docs/systems/LOS_DETECTION_AND_COMBAT_KNOWLEDGE_STANDARD.md`: LOS blockers explicitly include an `opaque wall edge`, and minimum tests explicitly require `opaque edge block`.
  3. Read `docs/systems/DIRECTIONAL_COVER_TERRAIN_STANDARD.md`: cover is directional edge data and is explicitly separate from LOS blocking.
  4. Read `docs/systems/PHASE_1_COMBAT_SCHEMA_API_MIGRATION_PACKET.md` and `docs/evidence/D069_IMPLEMENTATION_PREFLIGHT_2026-10-04.md`: the authored map shape uses `default_cell` + sparse `overrides`; validation mentions cover edges and cell `blocks_los`, while the D-069 test matrix still requires opaque-edge blocking.
- **EXECUTED_EVIDENCE:** exact-head repository document/source inspection only; no D-069 runtime implementation existed on authority at the observation point, so no executable RED test is claimed.
- **AFFECTED_FILES/APIS:**
  - `docs/systems/TACTICAL_COORDINATE_OCCUPANCY_STANDARD.md`
  - `docs/systems/LOS_DETECTION_AND_COMBAT_KNOWLEDGE_STANDARD.md`
  - `docs/systems/DIRECTIONAL_COVER_TERRAIN_STANDARD.md`
  - `docs/systems/PHASE_1_COMBAT_SCHEMA_API_MIGRATION_PACKET.md`
  - `docs/evidence/D069_IMPLEMENTATION_PREFLIGHT_2026-10-04.md`
  - future `src/textrpg/combat_schema.py`
  - future `src/textrpg/combat_grid.py`
- **AFFECTED_DOMAINS:** tactical authored schema, content validation, pure-grid LOS, directional cover, deterministic regression evidence.
- **BLOCKS:** safe completion of D-069's opaque-edge LOS acceptance path. Other D-069 coordinate/path/schema work may remain independently implementable if Veyra keeps this boundary isolated.
- **TEMPORARY_PATCH_PRESENT:** no.
- **SUSPECTED_CAUSAL_LAYER:** contract/schema omission. The design requires edge LOS blocking but never assigns it a serializable authored owner distinct from cover.
- **WHY CURRENT TASK CANNOT SAFELY ABSORB IT:** D-069 owns implementation, not silent invention of a new content contract. Choosing a field name/shape inside code without authority would create undocumented schema; reusing cover strength as LOS opacity would directly violate the cover/LOS separation contract.
- **UNVERIFIED_FACTS:** no implementation branch/PR was published at the initial observation, so this packet does not claim Veyra has implemented the defect or that any runtime test currently fails.
- **PROPOSED RESOLUTION OPTIONS — NON-AUTHORITATIVE:**
  - add an explicit directional edge-opacity map/set (for example N/E/S/W LOS-block flags) to canonical cell data and default/override authoring; or
  - define a structured directional edge record with independent cover and LOS-opacity properties.
  In either case, validation must reject invalid edge names and grid LOS must consume only the explicit LOS property.
- **ROOT_CAUSE_STATUS:** contract gap proven; AXIOM selected `los_blocked_edges` + either-adjacent-cell boundary semantics; D-069 implementation/evidence remains in progress.
- **BULLETIN_TASK:** D-069 — linked. AXIOM ruled **no duplicate task**.
- **REWARD_CANDIDATE:** prevention/root-cause credit may be evaluated after D-069 proves the selected contract; no award yet.


## Follow-up — first D-069 schema commit observed

- **IMPLEMENTATION COMMIT:** `8897fcd2cb2bb9e8bca975808f643d5095738d29` — `feat: add canonical tactical schema primitives`, committed 2026-10-05T16:31:32Z on `agent/veyra-d069-tactical-core`.
- **OBSERVATION:** `TacticalCell` now contains `los_blocked_edges: tuple[str, ...]` plus `blocks_los_through(edge)`. This is semantically separate from `cover`, so the implementation does not conflate cover strength with LOS opacity.
- **CONTRACT STATUS:** the live documentation authorities still do not define `los_blocked_edges` or an equivalent authored field. Code therefore resolves the missing representation, but the content contract remains undocumented until authority is synchronized.
- **SECONDARY INVARIANT RISK:** the current canonical schema validates each cell's blocked edge names but does not enforce reciprocal boundary consistency between adjacent cells. Example: cell A may declare E blocked while adjacent cell B omits W. If the future LOS tracer reads only the edge on the source/entered cell, the same wall can become direction-dependent. The LOS contract describes geometric cell/edge tracing and D-069 preflight requires symmetry where appropriate; a shared opaque wall boundary should therefore have one explicit ownership/reciprocity rule before completion.
- **RECOMMENDED ACCEPTANCE ADDITION — NON-AUTHORITATIVE:** document whether an opaque boundary is owned by the entered cell, the exited cell, or both; normalize to one canonical rule and add a regression proving A->B and B->A agree for the same opaque shared boundary.
- **NO CLAIM:** no runtime LOS/grid implementation or executable RED/GREEN test is claimed by Vector at this follow-up.


## Correction — reciprocal LOS behavior verified in branch code

The prior follow-up identified reciprocal shared-edge consistency as a possible risk. After `src/textrpg/combat_grid.py` appeared on Veyra's branch, that specific runtime risk was checked and is **not present in the current implementation**.

`_edge_blocked(map, start, end)` evaluates both `source.blocks_los_through(direction)` and `destination.blocks_los_through(opposite_direction)`. Therefore a blocker declared on either side of one shared boundary blocks the crossing in both directions. Small-grid independent algorithm checks also found the supercover cell set and undirected ray-edge set symmetric for tested coordinate pairs.

The remaining CPR-003 issue is narrower:
- `los_blocked_edges` is now a concrete code-level schema decision;
- live design/content authorities still do not define that authored field or its default/override JSON shape;
- strict content parsing/validation and an opaque-edge regression must prove the documented contract before D-069 completion.

Do not use the superseded reciprocal-risk paragraph as evidence of a current runtime defect.


## AXIOM review

### Problem Pressure Score

| Dimension | Score |
|---|---:|
| Phase 1 / player-path impact | 20 / 25 |
| Cross-system / multi-task reach | 12 / 20 |
| Data/save/privacy/determinism risk | 7 / 15 |
| Repair complexity / authority ambiguity | 10 / 20 |
| Reproduction / merge-state difficulty | 5 / 10 |
| Downstream blocking / recurrence | 10 / 10 |
| **TOTAL** | **64 / 100** |

- **PROBLEM_PRESSURE_SCORE:** **64/100**
- **RATING:** **CRITICAL**
- **VERDICT:** **ACCEPTED / LINKED_TO_D-069 / CONTRACT REPAIR SELECTED**
- **WHY CRITICAL:** the omission blocks one mandatory D-069 LOS acceptance dimension on the active tactical critical path. Silently inventing a field in code would split schema authority; treating cover as opacity would violate an approved contract.
- **WHY NOT SYSTEM BLOCKER:** the defect is localized to tactical cell schema/LOS semantics, has no current durable-save/Android impact, and Veyra can continue independent D-069 coordinate/path/occupancy work.
- **BULLETIN TASK:** existing D-069. **No duplicate task.**

### AXIOM selected contract

Canonical Phase 1 cell field:

`los_blocked_edges`

Rules:
- zero or more `N`, `E`, `S`, `W` values;
- independent from directional `cover`;
- cell-level `blocks_los` remains separate;
- for two cardinal adjacent cells A and B, their shared boundary is opaque if A declares the outgoing edge **or** B declares the opposite edge;
- reciprocal duplicate declaration is allowed but not required;
- LOS must therefore be symmetric across a one-sided authored opaque boundary;
- invalid/non-cardinal edges reject during strict schema validation;
- default-cell + sparse override authoring may carry the field;
- canonical runtime cells normalize the field to deterministic cardinal order.

This matches Veyra's first schema/grid branch direction and removes the need for a broader structured edge-object schema in D-069.

### Required D-069 completion evidence

Before D-069 can close:
1. authored/default/override parsing supports `los_blocked_edges`;
2. strict validation rejects invalid edge names/shapes;
3. canonical cell representation preserves normalized edge data;
4. grid LOS blocks a boundary when either adjacent cell declares the matching edge;
5. one regression proves A→B and B→A both block for the same one-sided declaration;
6. one regression proves cover alone does not imply LOS opacity;
7. existing opaque-cell and supercover regressions remain green;
8. old content packs with no tactical sections remain valid.

### Implementation observation

Veyra's branch already contains:
- `TacticalCell.los_blocked_edges`;
- canonical cardinal-edge normalization;
- `blocks_los_through(edge)`;
- `_edge_blocked()` that checks source edge **or** destination opposite edge.

That implementation shape is **ACCEPTED IN PRINCIPLE**, subject to the authored parser/validator and regression requirements above.

### Reward state

No critical-fix points are awarded yet.

This CPR was identified before the schema gap became a merged runtime defect. Evaluate PREVENTION/root-cause credit only after D-069 completes with the approved contract and executable regressions. The reporter did not claim task ownership.
