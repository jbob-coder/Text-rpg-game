# CPR-004 — D-069 unresolved persistent_ref IDs

- **STATUS:** ACCEPTED / LINKED_TO_TASK / CONTRACT REPAIR SELECTED
- **REPORTER:** Vector finding, reviewed by AXIOM
- **CURRENT_TASK:** D-069
- **OBSERVED_AUTHORITY_HEAD:** `f46089471970eef3f0ff6e6419780386dfc1a31f`
- **ACTIVE_PR_HEAD_REVIEWED:** `d88ff43b36cea3ddd057673f1b806d27819f172e`
- **DATE:** 2026-10-05
- **BULLETIN_TASK:** D-069
- **ROOT_CAUSE_STATUS:** proven contract/loader-order gap
- **TEMPORARY_PATCH:** none required
- **REWARD_CANDIDATE:** evaluate after executable repair evidence under OR-024

## Failure

The tactical encounter schema permits participant `persistent_ref`.

Current D-069 validation checks only that a present ref is a syntactically valid stable uppercase ID. It does not prove that the ID exists in authoritative durable state.

A value such as:

`NPC_DOES_NOT_EXIST`

can therefore pass tactical syntax/cross-reference validation even when no matching durable NPC exists in `initial_state.npcs`.

## Contract

`docs/systems/PHASE_1_COMBAT_SCHEMA_API_MIGRATION_PACKET.md` states:

> Persistent NPC/player refs must resolve to existing authoritative state IDs.

The repository currently has a concrete durable NPC identity owner:
- `GameState.npcs`;
- authored from `initial_state.npcs`.

The repository does **not** currently expose a canonical player stable-ID field suitable for D-069 authoring.

AXIOM will not invent a player sentinel merely to satisfy the generic wording.

## Loader-order evidence

Current `content_pack_from_mapping()` performs:
1. content/tactical shape validation;
2. tactical-map parsing;
3. `initial_state` extraction;
4. `GameState(**initial)` construction;
5. durable-state structure/reference validation.

Therefore initial tactical shape validation cannot reliably resolve durable NPC IDs because the authoritative state object does not exist yet.

## Selected bounded repair

D-069 retains two validation phases:

### Pre-state tactical validation
Continue validating:
- field shapes;
- stable-ID syntax;
- maps/actions/archetypes;
- deployment zones;
- world locations;
- other authored cross-references that already exist before GameState construction.

### Post-state persistent-NPC validation
After `GameState` construction and structure validation:
- collect `set(state.npcs)`;
- inspect encounter participants with a non-empty `persistent_ref`;
- every D-069-supported `persistent_ref` must resolve to an existing durable NPC ID;
- unknown refs reject the content pack with a stable `RuleError`.

Implementation may use a focused helper such as:
`validate_encounter_persistent_refs(encounters, persistent_npc_ids)`

or an equivalent bounded second-pass function.

Do not duplicate all tactical validation after state construction.

## Player persistent refs

D-069 must **not** invent a canonical player identity.

Until a stable player-ID contract exists:
- player-backed encounter participants should omit `persistent_ref` in D-069 authored schema;
- encounter-local `actor_id` remains valid for schema/grid authoring;
- durable player adapter/binding belongs to the later combat runtime/bridge integration seam where canonical player identity can be defined explicitly.

If a future authority introduces a stable player ID, the persistent-ref validator may be extended then.

## Required executable evidence

Before D-069 completion:

1. valid NPC reference:
   - `initial_state.npcs` contains `NPC_TAMSIN`;
   - participant `persistent_ref: NPC_TAMSIN`;
   - content pack loads.

2. invalid NPC reference:
   - participant `persistent_ref: NPC_MISSING`;
   - no matching durable NPC;
   - content pack rejects with an explicit error.

3. no persistent ref:
   - encounter-local participant omits `persistent_ref`;
   - remains valid.

4. old content packs without tactical sections remain unchanged.

## Problem Pressure Score

| Dimension | Score |
|---|---:|
| Phase 1 / player-path impact | 16 / 25 |
| Cross-system / multi-task reach | 14 / 20 |
| Data/save/privacy/determinism risk | 11 / 15 |
| Repair complexity / authority ambiguity | 12 / 20 |
| Reproduction / merge-state difficulty | 4 / 10 |
| Downstream blocking / recurrence | 8 / 10 |
| **TOTAL** | **65 / 100** |

**RATING:** CRITICAL

## AXIOM verdict

**ACCEPTED / LINKED TO D-069 / NO NEW TASK**

Why:
- D-069 already owns tactical schema/content validation;
- the repair is bounded to content↔durable-state validation;
- creating another task would duplicate the same acceptance work.

## Out of scope

Do not:
- add a player stable-ID field to GameState in D-069;
- add CombatSession/TacticalActorState;
- alter save schema;
- introduce Android combat DTOs;
- expand into D-070/D-073 runtime behavior.

## Resolution gate

CPR-004 becomes RESOLVED only when:
- the bounded post-state NPC reference check is implemented;
- focused valid/invalid/no-ref regressions pass;
- D-069 merge-state verification is green.

