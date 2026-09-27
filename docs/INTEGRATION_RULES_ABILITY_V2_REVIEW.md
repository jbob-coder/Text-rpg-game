# Rules + Ability Integration V2 Review

Status: **IN PROGRESS — NOT MERGE-READY**

Base: `foundation/text-rpg-systems`

Integrated workstreams:
- `review/effective-stat-contract-hardening-v3`
- current ability progression work ported from `feature/ability-progression-v4`
- player-facing status projection work

## Purpose

This branch is the first current-foundation integration point where:
- effective stats/modifier provenance
- ability progression/runtime
- player-safe ability visibility
- status-screen projection
- deep value explainability

can be reviewed together without forcing either source workstream to be promoted independently.

## Current ancestry state

At the latest comparison performed by this workstream:
- this branch is ahead of `foundation/text-rpg-systems`
- it is not behind foundation
- it contains the hardening V3 changes plus the current V4 ability source/tests
- it supersedes `integration/rules-ability-v1` as the active integration review branch

A fresh comparison remains mandatory before any promotion because foundation is being changed concurrently by other chats.

## Effective-stat integration

The branch contains:
- canonical modifier-path validation
- equipment/set/perk/condition aggregation
- source provenance
- effective attribute/skill values
- derived formula registry
- derived value explanation
- derived capacity floors
- old/new equipment-set API compatibility
- authored content validation hardening

Foundation compatibility is preserved for the `equipment_sets=` keyword while the hardening layer can also use `set_definitions=`.

Conflicting simultaneous values are rejected explicitly.

## Ability integration

The branch contains:
- ability discovery
- ability mastery/rank
- technique discovery/mastery
- costs
- world-time cooldowns
- authored drawbacks
- evolution prerequisites/results
- player-safe ability projection
- technique/evolution definition validation
- finite numeric progression validation
- effective stat requirements
- optional equipment-set-aware power requirements
- save coverage for discovered/evolution visibility state

## Status projection

`build_status_view()` projects authoritative state into a player-facing structure.

It deliberately excludes:
- raw modifier maps
- hidden quest state
- NPC private knowledge
- hidden ability evolution requirements
- arbitrary structured identity data

It includes:
- identity
- base/effective core attributes
- resources and authoritative maxima
- derived values
- grouped skills
- player-safe abilities
- visible conditions

## Deep inspection

`inspect_status_value()` provides the projection layer's safe drill-down path.

Allowed:
- `attributes.<known-id>`
- `skills.<known-id>`
- `derived.<known-id>`

Rejected:
- quest paths
- raw ability paths
- relationship internals
- unknown IDs
- arbitrary nested paths

This lets a future UI show "why is this value 15?" without being given generic raw GameState access.

## Architectural boundary

Target flow:

```text
GameState
  -> RulesEngine / effective-value contract
     -> status / ability player-safe projection
        -> client UI
```

The client should not:
- recalculate modifiers
- evaluate equipment sets
- reconstruct derived formulas
- inspect raw hidden ability requirements
- read NPC hidden knowledge
- mutate permanent stats based on displayed effective values

## Tests authored across the integration

Coverage present includes:
- exact modifier stacking
- provenance
- derived stat explanation
- path validation
- set validation
- malformed authored scene structures
- equipment requirement validation
- resource/capacity floors
- training bounds
- ability progression validation
- hidden evolution non-disclosure
- ability projection numeric safety
- effective-stat power requirements
- ability visibility save round-trip
- non-mutating status projection
- hidden condition filtering
- deep status inspection
- rejection of hidden/raw status paths

## Additional cross-system hardening added during integration review

The integration review exposed mutation hazards that were not obvious while the
systems were inspected separately.

### Spendable resource paths

Technique costs are now restricted to:
- `resources.<id>`
- `power_resources.<id>`

A technique definition can no longer spend an arbitrary player path such as
`attributes.will`. This prevents a malformed authored ability from converting
a temporary activation cost into permanent stat damage.

### Modifier validation before technique/evolution mutation

Technique drawback modifiers are validated against the canonical modifier-path
registry before any cost/cooldown/use mutation.

Evolution-granted perk modifiers are also validated before form, rank, item, or
perk mutation.

This closes a partial-state failure mode where invalid modifiers could otherwise
be discovered only after resources/items or progression state had already changed.

### Requirement ID validation

Technique/evolution attribute and skill requirements now reject unknown IDs at
definition-validation time instead of relying on a later effective-value lookup.

### Atomic mastery mutation

Direct ability and technique mastery progression now validates existing
persistent mastery/rank-floor state and computes the next stage/rank before
writing mutations.

Corrupt/non-finite persistent progression state therefore raises before changing
the stored mastery/stage/rank.

Technique discovery also rejects empty technique IDs and invalid technique
containers.

### Tests added for these integration hazards

New tests cover:
- arbitrary non-resource technique cost paths
- invalid drawback modifier paths before spending resources
- unknown attribute/skill requirement IDs
- invalid evolution perk modifiers before form/item mutation
- corrupt ability mastery before progression mutation
- invalid rank-floor state
- corrupt technique mastery before progression mutation
- invalid technique discovery IDs/containers

## Verification state

No byte-for-byte checkout of this integration branch has been executed by this chat.

GitHub is connected and used for repository work, but there is no repository Actions workflow on the reviewed branch and no Codex execution environment registered in this conversation.

Therefore:
- implementation exists
- tests exist
- static/cross-branch review has been performed
- prior reconstructed executions are supporting evidence
- **exact integration runtime verification remains pending**

Do not label this branch merge-ready until exact execution succeeds.

## Open design items not resolved here

This integration does not decide:
- seven vs eight core attributes
- final overall character Level/EXP model
- final ability-specific modifier namespaces
- final balance coefficients
- final zero-floor policy as immutable canon
- exact player-facing typography/layout

The branch is deliberately registry/path driven so the core-stat decision can still evolve.

At the latest repository comparison performed after this hardening,
`integration/rules-ability-v2` was **42 commits ahead of foundation and 0 behind**.
This is branch-state evidence only, not runtime-test evidence.

## Promotion gate

Before promotion:
1. compare with latest foundation
2. resolve any new divergence
3. execute full test discovery on exact branch source
4. fix all regressions
5. review save round-trip behavior
6. verify no hidden-data leakage in status/ability projection
7. recheck no-double-counting across ability requirements and effective modifiers
8. update shared context with exact command/result
9. decide whether integration is promoted as one unit or split into reviewed source branches
