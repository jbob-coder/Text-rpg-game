# Branch Integration Contract

Status: [DESIGNED] / [IN_PROGRESS]

Purpose: prevent independently useful workstreams from breaking each other when they are eventually combined.

## Active workstreams

### `foundation/text-rpg-systems`

Role:
- current baseline rules/content implementation
- authoritative reference for the latest foundation API and repository state
- continues advancing independently

Do not assume a feature/review branch is current merely because it was created from this branch earlier.

### `review/effective-stat-contract-hardening`

Role:
- harden effective-value aggregation
- validate modifier paths and set definitions
- explain effective/derived values
- define safe derived-value domains
- preserve base stats while exposing provenance
- catch malformed numeric/time/condition/equipment contracts

This branch is review/evolution work and is **not yet merge-ready**.

### `feature/ability-progression-v2`

Role:
- player-safe ability projection
- technique/evolution definition validation
- ability mastery numeric hardening
- effective-stat-aware technique/evolution prerequisites
- persistence coverage for ability discovery/evolution visibility

This branch is active ability work and is **not yet merge-ready**.

### `shared/game-context`

Role:
- durable design direction
- architectural contracts
- checkpoints
- cross-chat synchronization
- conflicts/open decisions

This branch does not prove runtime implementation by itself.

## Cross-branch API contract

### Effective player value

Foundation public usage includes:

```python
effective_player_value(
    state,
    "attributes.will",
    equipment_sets=sets,
)
```

The hardening branch introduced the internal name `set_definitions`.

[VERIFIED] A compatibility regression was identified during cross-branch review: replacing `equipment_sets=` with only `set_definitions=` would break existing foundation/ability callers.

[IMPLEMENTED ON HARDENING REVIEW] The hardening branch now accepts both names through a compatibility resolver:

- `set_definitions=`
- `equipment_sets=`

Supplying conflicting values is rejected.

This compatibility rule also applies to the hardened derived-stat/resource APIs where the foundation exposed `equipment_sets=`.

### Ability prerequisite evaluation

Ability V2 uses the effective-value pipeline for attribute/skill requirements.

It deliberately passes equipment-set context through the foundation-compatible `equipment_sets=` keyword.

Therefore, any future integrated effective-stat implementation must preserve that public call form or provide an explicit migration adapter.

## No-double-counting invariant

Equipment, reached set thresholds, perks, and active conditions must contribute exactly once.

Ability prerequisites should ask for the effective value; they must not manually add equipment/perk/condition bonuses again.

Derived formulas should consume effective inputs and then apply direct `derived.*` modifiers exactly once.

UI should consume explanation/projection APIs and must not reconstruct modifier arithmetic itself.

## Permanent vs effective invariant

Permanent/base attributes and skills are durable progression state.

Equipment, set bonuses, perks, and active conditions normally produce effective views.

Power/ability prerequisites may use effective values.

Equipment qualification intentionally uses permanent/base values so one equipped bonus cannot recursively qualify another item.

## Disclosure invariant

Raw ability definitions may contain hidden evolution data.

Normal player UI must consume a player-safe projection, not raw definitions.

The ability V2 projection exposes discovered techniques and only explicitly visible evolution knowledge.

The effective-stat explanation API may expose numeric provenance, but it must not be used as a path to reveal hidden quest, NPC, or ability data.

## Numeric safety invariant

The evolving rule contract rejects:
- booleans masquerading as numbers
- NaN
- infinity
- malformed numeric requirements
- negative values where the domain explicitly forbids them

Capacity-style derived values in the hardening review currently floor at zero.

Contest-style values may remain signed.

The floor policy is still provisional until accepted as canonical.

## Time/state safety invariant

Time is integer minutes in the current simulation contract.

Condition durations, training time, cooldowns, and recovery periods must not accept boolean or malformed values.

Persistent cooldown/evolution/discovery state must survive save/load.

## Known file overlap

Likely manual integration hotspots:

- `src/textrpg/__init__.py`
  - both workstreams add exports
- effective/stat modules vs ability prerequisite calls
  - public keyword/signature compatibility must be preserved
- tests
  - combined suite must include both hardening and ability V2 coverage

Ability V2 currently concentrates implementation changes in:
- `powers.py`
- `progression.py`
- persistence/power/progression tests
- package exports

Hardening currently concentrates implementation changes in:
- `modifiers.py`
- `schema.py`
- `stats.py`
- `equipment.py`
- `simulation.py`
- `validation.py`
- `core.py`
- related tests/exports

This relatively small source overlap is useful, but it does not eliminate semantic integration risk.

## Integration sequence

Do not merge branches by age.

Recommended sequence:

1. Fetch/compare the latest foundation.
2. Identify parent-only changes since each branch point.
3. Recreate or rebase/port feature work onto the current foundation when ancestry is stale.
4. Preserve the foundation public API unless an explicit migration is documented.
5. Apply effective-stat hardening.
6. Apply/port ability V2.
7. Resolve `__init__.py` exports manually.
8. Run focused effective-stat tests.
9. Run focused ability/power tests.
10. Run persistence tests.
11. Run the complete repository suite.
12. Inspect hidden-data/disclosure behavior manually.
13. Record exact commands/results in shared checkpoints.
14. Promote only after the final diff is reviewed.

## Active design conflict not resolved by integration

The seven-vs-eight core-attribute decision remains separate.

Neither hardening nor ability V2 makes the seven-stat schema permanent.

Both workstreams should remain registry/path driven enough that a later atomic stat migration can update:
- registry
- formulas
- validation
- save migration
- authored content
- tests
- status UI metadata

without rewriting unrelated ability progression logic.

## Current promotion state

- hardening review: [IN_PROGRESS] / NOT MERGE-READY
- ability progression V2: [IN_PROGRESS] / NOT MERGE-READY
- shared context: current coordination layer
- foundation: active baseline, still moving

No branch should be labeled complete solely because targeted tests exist.
