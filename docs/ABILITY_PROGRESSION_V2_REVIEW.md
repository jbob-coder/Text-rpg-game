# Ability Progression V2 Review

Status: **IN PROGRESS — NOT MERGE-READY**

Parent workstream: `foundation/text-rpg-systems`

Purpose: evolve the existing power runtime toward the documented ability/status architecture without silently changing the canonical core-stat schema.

## Why V2 exists

The first ability work branch was created while `foundation/text-rpg-systems` continued advancing. Before further work, the branch was compared against the parent and found behind. Rather than pretending the stale branch was current, V2 was created from the newer foundation and the ability-only changes were ported forward.

At the latest comparison performed during this workstream:
- V2 contains only ability-facing changes in `powers.py`, package exports, and power tests.
- The parent foundation has one later unrelated `tests/test_stats.py` commit not yet in V2.
- No known source conflict was observed from that parent-only test change.
- Final promotion still requires another parent comparison.

## Implemented on V2

### Player-safe ability projection

Added `ability_player_view()`.

It exposes only player-appropriate ability state:
- display name
- rank
- mastery stage / mastery XP
- form/state
- optional control and efficiency
- configured current/max ability resource
- discovered techniques only
- cooldown remaining for discovered techniques
- explicitly visible evolution entries only
- completed evolution IDs

It does **not** dump the raw authored ability definition.

Hidden evolutions remain hidden even if the authored definition contains their name or requirements.

Hinted evolution entries can use player-state hint/label information without exposing authored hidden prerequisites.

Known/satisfied evolution entries can expose a player-visible name and only the requirements explicitly recorded as known in player state.

### Definition validation before mutation

Added:
- `validate_technique_definition()`
- `validate_evolution_definition()`

Validation happens before technique/evolution mutation.

Technique validation covers:
- structure
- minimum stage
- rank/mastery requirements
- attributes/skills/items/flags/knowledge/perks shapes
- non-negative costs
- cooldown
- mastery gains
- drawback shape
- condition ID
- severity
- duration
- drawback modifier numeric values

Evolution validation covers:
- requirement structure
- numeric minima
- technique stage requirements
- result structure
- rank floor
- tags
- consumed item quantities
- granted perk structure/modifiers/tags

This reduces partial-mutation risk from malformed authored data.

### Numeric safety

Boolean values are no longer accepted as valid numeric power resources.

This prevents Python's `bool` subclassing of `int` from allowing `True` or `False` to act as ability-resource amounts.

### Effective stat requirements

Technique/evolution attribute and skill requirements now read effective values through the existing stat pipeline.

That means direct:
- equipment modifiers
- perks
- active conditions

can affect power prerequisites.

When authored equipment-set definitions are supplied to the power API, reached set thresholds also participate.

The new parameters are optional keyword arguments, so existing call forms remain compatible.

## Tests added

New tests cover:
- player view exposes only discovered techniques
- hidden evolution stays hidden
- known evolution does not leak raw authored requirement dictionaries
- ability resource projection
- control/efficiency projection
- cooldown remaining without advancing time
- boolean numeric rejection
- malformed technique definition rejected before resource spend/use mutation
- malformed evolution definition rejected before item/form/perk mutation
- effective attribute requirement using equipment + perk + condition + set contributions
- evolution requirement using effective stat contributions

## Existing foundation behavior retained

The branch continues to use the existing foundation implementation for:
- ability mastery and rank
- technique discovery
- technique mastery stages
- resource costs
- world-time cooldowns
- authored condition drawbacks
- evolution items/perks/forms/rank floors
- save state through `GameState.abilities`
- deterministic authored rules

## Not changed

This branch does not:
- migrate seven core attributes to the eight-stat candidate
- add an overall character Level/EXP decision
- invent a universal mana system
- make hidden evolution requirements player-visible
- change persistence schema version
- merge the separate effective-stat hardening review branch
- finalize balancing thresholds

## Verification state

The parent foundation document reports a prior branch-equivalent run of **58 tests passed, 0 failed**.

That result predates the V2 additions and is not claimed as verification of V2.

The new V2 tests exist in the repository, but this workstream has not executed a byte-for-byte checkout of V2. Therefore:

**V2 is implemented and statically reviewed, but not fully VERIFIED or merge-ready.**

## Promotion gate

Before promotion:
1. compare against the latest foundation again
2. resolve any parent divergence
3. execute the full suite on the exact V2-equivalent source
4. inspect player-view output for hidden-data leakage
5. confirm optional effective-stat/set integration does not double count
6. verify save round-trip with the additional ability-state fields used by the player view
7. update shared checkpoints with exact evidence
