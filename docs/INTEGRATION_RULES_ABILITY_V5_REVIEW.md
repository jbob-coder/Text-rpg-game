# Rules + Ability Integration V5 Review

Status: **IN PROGRESS — NOT MERGE-READY**

Active integration branch: `integration/rules-ability-v5`

## Why V5 exists

The foundation workstream continued advancing while V2/V3/V4 integration branches were being reviewed. V5 was created directly from a newer `foundation/text-rpg-systems` state and the integration-specific rules/stat/status work was re-applied selectively rather than force-moving older refs.

The temporary sync PR for V4 was closed without merge because it was conflictful and had already become stale.

## Integration strategy

V5 follows this rule:

1. use a recent foundation snapshot as the executable base
2. port only integration work that foundation has not replaced
3. preserve newer foundation systems explicitly
4. do not force-merge stale branches
5. compare again before promotion

Because another chat is actively changing foundation, "0 behind" is not treated as a durable property during active development. The promotion comparison must happen after the implementation pass stabilizes.

## Integrated systems currently present

### Effective-value hardening

- canonical modifier-path registry
- equipment / set / perk / condition aggregation
- source provenance
- effective attribute and skill values
- derived formula registry
- derived-value explainability
- capacity floors
- finite-number validation
- compatibility between `equipment_sets=` and `set_definitions=`

### Rules engine hardening

- validated equipment-set context
- `explain_player_value()`
- atomic choice execution with rollback on effect failure
- choice time/next-scene preflight
- effective-value gating
- support retained for current foundation conditions including:
  - `technique_discoverable`
  - `technique_stage_min`
  - `has_perk`
  - `not_has_perk`
- support retained for current foundation effects including:
  - ability/technique operations
  - power recovery
  - `skill_train`
  - `recover_resources`

### Ability progression

- ability discovery
- ability-specific resource initialization/recovery
- technique discovery requirements
- technique practice
- technique activation
- mastery/rank progression
- evolution
- effective-stat prerequisites
- equipment-set-aware prerequisite checks
- finite numeric validation
- atomic progression-state checks
- canonical modifier validation for drawbacks/evolution perks
- restricted spendable technique-cost paths

### Status / player projection

- `build_status_view()`
- `inspect_status_value()`
- player-safe ability view
- hidden evolution filtering
- hidden condition filtering
- no raw quest/NPC/relationship internals in normal status inspection
- authoritative base/effective/derived explanations

## Cross-system atomicity rule

The integration architecture now uses:

```text
validate authored definition
-> validate persistent state
-> evaluate availability
-> compute/preflight mutation
-> commit mutation
-> append durable event
```

Where a scene choice performs multiple effects, the RulesEngine transaction layer restores the pre-choice snapshot if a later effect fails.

## Foundation features explicitly preserved during V5 port

During the V5 reconstruction, integration code was checked against newly added foundation behavior and retained:

- authored technique discovery gates
- stable content registries
- technique-stage conditions
- negative perk gate (`not_has_perk`)
- authored skill training effects
- authored normal-resource recovery effects
- current Trace Echo / Directional Trace vertical-slice routes
- current save/resume route expectations

## Files added or materially integrated

- `src/textrpg/modifiers.py`
- `src/textrpg/schema.py`
- `src/textrpg/status.py`
- `src/textrpg/core.py`
- `src/textrpg/equipment.py`
- `src/textrpg/powers.py`
- `src/textrpg/progression.py`
- `src/textrpg/simulation.py`
- `src/textrpg/stats.py`
- `src/textrpg/validation.py`
- package exports and corresponding tests

## Test coverage present

The branch contains coverage for:

- effective modifier stacking/provenance
- modifier path validation
- set validation
- derived formulas/floors
- resource normalization
- equipment requirements
- training bounds
- choice rollback/preflight
- technique discovery gates
- technique-stage and perk-negative gates
- skill-training/recovery scene effects
- ability resource lifecycle
- practice/use/evolution progression
- atomic rejection of invalid power definitions/state
- player-safe ability disclosure
- status projection and deep inspection
- persistence of ability visibility/discovery state
- stable content registry cross-references

## Verification status

No byte-for-byte checkout of V5 has been executed by this chat.

The repository connector permits precise source inspection and mutation, but no repository-local execution environment is registered and no hosted workflow is being added solely for this review.

Therefore:
- source changes are implemented
- tests are authored
- cross-branch static review has been performed
- **runtime regression verification is still pending**

## Concurrent-foundation drift

Foundation is actively changing in another workstream. At one comparison during this V5 pass, foundation had already advanced beyond the V5 merge-base again.

This is not treated as an error in V5 itself. It means the final sync must happen as a deliberate promotion gate after both workstreams reach a checkpoint.

Do not keep rewriting V5 every few minutes merely to report "0 behind"; that creates integration churn and risks overwriting reviewed work.

## Open design decisions unaffected by this branch

- seven vs eight core attributes
- final overall character Level/EXP model
- final ability-specific modifier namespaces
- final derived-stat balance coefficients
- final UI layout/typography
- final canonical floor policy where still marked provisional

## Promotion gate

Before promotion:

1. freeze/identify the intended foundation commit
2. compare V5 against that exact commit
3. integrate any parent-only source/content changes deliberately
4. execute the complete test suite on exact integrated source
5. fix regressions
6. verify save/resume routes
7. verify status/ability hidden-data boundaries
8. verify modifier contributions are applied exactly once
9. update shared checkpoint with exact commit IDs and test result
10. only then consider merge/promotion
