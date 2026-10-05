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
- **ROOT_CAUSE_STATUS:** contract gap proven by authority comparison; runtime manifestation not yet implemented.
- **BULLETIN_TASK:** D-069 already owns the eventual implementation; do not create a duplicate task unless AXIOM rules the contract repair must be separated.
- **REWARD_CANDIDATE:** none claimed by reporter.


## Follow-up — first D-069 schema commit observed

- **IMPLEMENTATION COMMIT:** `8897fcd2cb2bb9e8bca975808f643d5095738d29` — `feat: add canonical tactical schema primitives`, committed 2026-10-05T16:31:32Z on `agent/veyra-d069-tactical-core`.
- **OBSERVATION:** `TacticalCell` now contains `los_blocked_edges: tuple[str, ...]` plus `blocks_los_through(edge)`. This is semantically separate from `cover`, so the implementation does not conflate cover strength with LOS opacity.
- **CONTRACT STATUS:** the live documentation authorities still do not define `los_blocked_edges` or an equivalent authored field. Code therefore resolves the missing representation, but the content contract remains undocumented until authority is synchronized.
- **SECONDARY INVARIANT RISK:** the current canonical schema validates each cell's blocked edge names but does not enforce reciprocal boundary consistency between adjacent cells. Example: cell A may declare E blocked while adjacent cell B omits W. If the future LOS tracer reads only the edge on the source/entered cell, the same wall can become direction-dependent. The LOS contract describes geometric cell/edge tracing and D-069 preflight requires symmetry where appropriate; a shared opaque wall boundary should therefore have one explicit ownership/reciprocity rule before completion.
- **RECOMMENDED ACCEPTANCE ADDITION — NON-AUTHORITATIVE:** document whether an opaque boundary is owned by the entered cell, the exited cell, or both; normalize to one canonical rule and add a regression proving A->B and B->A agree for the same opaque shared boundary.
- **NO CLAIM:** no runtime LOS/grid implementation or executable RED/GREEN test is claimed by Vector at this follow-up.
