# Effective Stat Contract Hardening Review

Status: **IN PROGRESS — NOT MERGE-READY**

Parent: `feature/effective-stat-pipeline`

Purpose: review/evolve the effective-stat pipeline without modifying the other implementation workstream until the hardening changes are verified.

## Scope

This review concentrates on four failure classes:

1. silent modifier-path typos
2. invalid derived/resource domains
3. incomplete value provenance for status/debug UI
4. compatibility regressions introduced while centralizing modifier behavior

## Implemented review changes

### Canonical schema registry

`src/textrpg/schema.py` centralizes:

- core attribute specs
- skill catalog
- resource keys
- derived formula definitions
- derived-stat domain metadata

Existing imports through `textrpg.stats` remain available.

### Modifier path validation

Allowed modifier namespaces are exactly:

- `attributes.<known-id>`
- `skills.<known-id>`
- `derived.<known-id>`

Malformed paths, unknown IDs, and unsupported namespaces raise errors rather than being silently ignored.

Validation is applied to:

- equipment
- conditions
- perks
- equipment-set bonuses
- RulesEngine set definitions
- scene stat requirement/check paths
- add-perk authored effects
- runtime modifier aggregation/breakdown

### Set definition validation

One validator now checks:

- set definition object shape
- threshold object shape
- integer-convertible threshold
- threshold > 0
- bonus object shape
- canonical modifier map

RulesEngine and standalone active-set calculation share that contract.

### Derived value domains

Current review candidate:

Hard floor at zero:
- max_health
- max_stamina
- max_focus
- max_resolve
- carry_capacity

Signed contest-style scores:
- initiative
- accuracy
- evasion
- guard

Reason: capacities cannot be physically negative, while a signed contest score can preserve the magnitude of severe penalties and therefore continue to affect difficulty margins.

This policy is still provisional balancing/architecture and may be revised before promotion.

### Derived formula registry and explainability

Derived formulas are represented as data instead of only inline arithmetic.

`derived_stat_breakdown()` exposes:

- base constant
- effective source inputs
- coefficient/weight for every input
- weighted contribution
- direct `derived.*` source breakdown
- formula subtotal
- raw total
- domain floor
- floor adjustment
- final total

`RulesEngine.explain_player_value()` provides a single rules-facing inspection surface for:

- effective attributes
- effective skills
- full derived values

The UI should call this contract rather than duplicating game formulas.

### Public effective-value behavior

`effective_player_value()` now resolves a full `derived.*` value through the derived formula system when a derived path is requested. This prevents a caller from accidentally treating only the direct derived modifier subtotal as the character's final derived value.

## Tests authored on this branch

New/expanded tests cover:

- equipment + set + perk + condition stacking exactly once
- base-value immutability
- rule choice lock/unlock from effective stats
- derived stat checks in RulesEngine
- direct derived modifiers
- repeated derived calculations without accumulation
- invalid attribute/skill/derived path IDs
- invalid set modifier paths
- malformed set thresholds
- invalid equipment modifier paths
- invalid condition modifier paths
- invalid scene stat/check paths
- check skill namespace enforcement
- capacity floors
- signed contest values
- floor provenance
- RulesEngine explanation payloads
- public derived effective-value resolution
- consistency between derived formula IDs, derived specs, and canonical input paths

## Verification performed by this chat

### Repository inspection

Performed:
- compare review branch against parent feature branch
- inspect changed source and tests
- verify parent branch point
- confirm review branch was ahead and not behind at comparison time
- inspect package exports and persistence impact

### Branch-equivalent reconstructed execution

A local reconstruction of the reviewed effective-value logic was executed outside the repository checkout because the connected GitHub workflow does not provide a free local clone/runtime.

Reconstructed scenarios passed:

- exact base + equipment + set + perk + condition total
- exact provenance breakdown
- derived formula + direct set contribution
- full derived effective value
- zero floors for capacity values
- signed negative initiative
- rejection of typoed/unsupported modifier paths

A broader local reconstruction was then assembled from the current fetched review-branch source/test content and run with:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Observed reconstructed-suite result: **46 tests passed, 0 failed**.

This materially increases confidence in compatibility across core rules, equipment, modifiers, persistence, progression, simulation, social state, stats, and validation. It is still **not equivalent to executing a byte-for-byte checkout of the GitHub branch**, because the connected repository interface does not expose a normal local clone and the reconstruction was assembled from fetched contents.

## Not verified

The following remain unverified:

- import/syntax behavior of the actual remote branch in a Python checkout
- full repository unit test suite on a byte-for-byte checkout of this review tip
- compatibility with every caller outside the current test suite
- save round-trip after normalized numeric modifier values are stored as floats
- performance impact of repeated deep explainability calls in a large content pack
- final balancing correctness of the zero-floor policy

## Compatibility review

No schema-version bump or persistence-file modification is part of this review branch.

Existing public functions are retained. New APIs/metadata are additive.

Intentional behavior tightening:
- invalid modifier paths that previously could be inert/ignored now fail fast
- malformed set thresholds now fail contract validation
- capacity derived values no longer become negative
- `effective_player_value(derived.*)` resolves the full derived value rather than a misleading direct-modifier subtotal

These are deliberate semantic changes and must be covered by full regression execution before promotion.

## Promotion gate

Do **not** merge/promote this review branch until:

1. the actual branch can be executed
2. full test discovery passes
3. any regression is fixed
4. parent feature has not advanced incompatibly
5. the final diff is reviewed again
6. the chosen derived floor policy is accepted as the intended contract
7. the shared context checkpoint is updated with exact test command/results

If parent feature changes before promotion, rebase/compare first instead of force-moving refs.

## Next evolution after verification

Once this infrastructure is verified, use it as support for the larger stat-schema decision rather than treating the current seven-stat names as permanently fixed.

The shared design evaluation currently recommends the eight-stat candidate for long-term architecture, but migration remains a separate explicit decision.
