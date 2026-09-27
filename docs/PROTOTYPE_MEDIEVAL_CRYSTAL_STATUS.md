# Medieval Crystal Combat Prototype Status

Status: [PROTOTYPE] ISOLATED FROM V6 PROMOTION

Prototype branch: `prototype/medieval-crystal-combat-contracts`

Base V6 SHA: `7f5f104fb839068bdfaf5cec72f37129ae20d463`

Current prototype code/test HEAD before this status refresh: `8092edd4e106b0b44c983c78645a8793e975d444`

## Purpose

This branch proves data/rules contracts for the accepted medieval crystal-beast direction without changing the V6 promotion candidate.

It is not canonical gameplay code yet and must not be merged into V6 until the Stage 3 exact-runtime gate is satisfied and the prototype is then tested in the real repository environment.

## Implemented prototype modules

### `src/textrpg/combat.py`

Prototype positional targeting contract:

- range bands: grapple / close / reach / ranged
- relative facing: front / left flank / right flank / rear
- relative elevation: lower / level / higher
- defender posture
- state tags
- explicitly blocked zones
- body-zone facing/range/elevation/posture constraints
- all/any required battle-state tags
- state-tag blockers
- required/forbidden weapon targeting tags
- deterministic non-mutating reachable-zone query
- debug-only access explanation
- player-safe targeting view that exposes only reachable, visible zones and omits hidden weakness/effect metadata

This establishes the rule that the UI does not independently decide what anatomy can be attacked.

### `src/textrpg/crystals.py`

Prototype crystal contract:

- mine and beast source types
- definition/source compatibility
- stable crystal-instance identity
- source provenance
- grade
- purity
- stability
- integrity
- size
- resonance
- harvest damage
- unknown / partial / known appraisal states
- beast source requires beast ID
- mine source requires deposit ID
- player-safe appraisal projection
- effective integrity after harvest damage
- hidden definition data stays out of player-safe views

This is intentionally a data/projection contract. Crystal effect resolution remains future work; staged weapon compatibility/forge preview now exists in `src/textrpg/forge.py`.

### `src/textrpg/beasts.py`

Prototype persistent-beast contract:

- stable beast/species identity
- level and development XP
- intelligence range 0..5
- social/territorial role
- alive state
- bounded encounter memory
- memory capacity scales with intelligence
- observations include weapons, target zones, ranges, openings, defenses, techniques, traps, party roles, terrain, and retreat
- confidence increases only from actual observations
- low-confidence/old memories can be displaced when capacity is exceeded
- behavioral/tactical/strategic/biological adaptation readiness
- tactical and strategic adaptation are intelligence-gated
- biological adaptation additionally requires elapsed time and resources
- communication tier limited by both intelligence and species capability
- command eligibility uses authored intelligence/level/follower/social requirements instead of equating level with command rank

The adaptation query does not choose or apply a counter. It only proves that sufficient evidence/capability exists for authored adaptation logic to consider one.

### `src/textrpg/weapons.py`

Prototype physical weapon contract:

- sword, dagger, axe, hammer, mace, spear, polearm, staff, bow, crossbow, shield, improvised families
- cutting / piercing / blunt profile
- weight
- physical reach
- handling
- balance
- momentum
- guard
- penetration
- recovery
- stamina burden
- durability
- range bands
- targeting tags
- armor-interaction tags
- crystal socket count
- allowed crystal tags
- forge quality
- weapon condition
- material
- provenance
- integrated crystal-instance IDs
- player-safe weapon view
- targeting adapter consumed directly by the combat rules

The existing V6 `equipment.py` is deliberately untouched. Its slot/modifier pipeline remains the current implementation contract until a later migration/integration pass.

### `src/textrpg/armor.py`

Prototype coverage-based armor contract:

- armor slots aligned to current visible equipment concepts: head / body / hands / legs / feet
- explicit covered body zones
- cutting / piercing / blunt resistance profiles
- weight
- flexibility
- noise
- fatigue burden
- durability
- material
- forge quality
- condition
- crystal sockets and integrated crystal IDs
- zone query that returns only armor layers actually covering the selected target zone
- player-safe armor projection
- internal tuning metadata excluded from player-facing output

Damage resolution is intentionally not hard-coded yet. The armor query returns the authoritative protective layers so later combat rules can resolve penetration/mitigation without duplicating coverage logic.

### `src/textrpg/forge.py`

Prototype staged forge/crystal integration contract:

- canonical forge stage order from material selection through inspection/complete
- serializable work-in-progress forge-job validation
- no skipped/reordered completed stages
- bounded quality inputs
- weapon/crystal socket-capacity check
- weapon allowed-crystal-tag compatibility
- minimum crystal-stability gate
- destroyed-crystal rejection
- non-mutating integration preview

The prototype does not mutate persistent equipment yet. That remains intentionally deferred until the real GameState/save migration is designed after V6 verification.

## Tests authored on prototype branch

- `tests/test_combat_targeting.py` — 11 tests
- `tests/test_crystals.py` — 11 tests
- `tests/test_beasts.py` — 14 tests
- `tests/test_weapons.py` — 12 tests
- `tests/test_armor.py` — 11 tests
- `tests/test_forge.py` — 10 tests

Total new prototype tests: **69**.

## Runtime evidence

[VERIFIED ISOLATED] The six prototype modules were executed together in a local isolated package harness with the same committed module contents and a minimal compatible `RuleError` dependency.

Command form:

`PYTHONPATH=<isolated-prototype> python -m unittest discover -s <isolated-prototype>/tests -v`

Observed result:

- Ran 69 tests
- 69 passed
- 0 failed
- 0 errors

This proves the isolated contract logic exercised by those tests.

[UNKNOWN] Full-repository integration remains unverified.

The local shell could not clone the public repository because DNS resolution for `github.com` failed. Therefore the existing V6 258-test suite plus these 69 prototype tests has not been executed as one exact checkout.

No claim that the full repository is green is permitted.

## Compatibility constraints preserved

- no change to V6 `GameState`
- no schema-version bump
- no save migration
- no change to existing equipment slots
- no seven-to-eight stat migration
- no change to the V6 promotion branch
- no generative-AI runtime dependency
- player-facing views remain separate from hidden/internal rule data

## Next prototype work

1. zone wound/consequence contract
2. beast progression/level advancement policy
3. authored adaptation definitions that consume adaptation readiness
4. deterministic beast voice/bark projection
5. region/territory state and coarse beast-vs-beast simulation
6. one authored hunt scenario connecting weapon -> targeting -> armor -> wound/core exposure -> crystal harvest -> forge preview
7. only after V6 verification: design the real GameState/persistence migration and integration path
