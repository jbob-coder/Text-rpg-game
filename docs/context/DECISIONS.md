# Design and Architecture Decisions

This file records accepted, open, conflicting, superseded, and rejected project decisions. It is not an implementation log.

---

## DEC-STAT-001 — Core attribute count and Dexterity split

Status: [CONFLICTING] / OPEN

Existing repository position:
- seven core attributes: `might`, `agility`, `endurance`, `intellect`, `will`, `perception`, `presence`
- current `agility` covers movement, coordination, and reaction

Expanded chat proposal:
- eight core attributes: `STR / CON / AGI / DEX / PER / INT / WIL / PRE`
- separate `DEX` from `AGI`
- use `CON` as dedicated bodily robustness/health-resilience attribute

Reason this is open:
- seven stats reduce UI/balance complexity
- eight stats reduce responsibility overload and can create clearer physical build identity
- changing implemented attributes later may require migration work

Resolution rule:
- evaluate both schemas against combat, stealth, traversal, technical tasks, social play, investigation, injury/recovery, training, powers, and life-simulation decisions before selecting canonical names/responsibilities
- no silent implementation migration before resolution

Related: `CP-2026-09-27-STATS-SCHEMA-01`

---

## DEC-DIR-001 — Slow progression and persistent consequence

Status: [DIRECTION] ACCEPTED

The game is a life-and-decisions text RPG. Slow earned progression, meaningful persistent consequences, and a living stateful world are project-wide direction, not isolated features.

Consequences may affect relationships, knowledge, NPC memory, injuries, inventory/equipment, quests, factions, powers, time, and later scene availability.

Permanent growth should not normally come from trivial or instantaneous actions.

---

## DEC-STATE-001 — Important continuity is structured state

Status: [DIRECTION] ACCEPTED

If later content must react to something, it should normally have structured state and a stable identifier rather than exist only in prose or conversational memory.

Source/tests outrank chat recollection for implementation claims.

---

## DEC-UI-001 — Layered status screen

Status: [DESIGNED] ACTIVE DESIGN

The character/status screen should expose a layered model rather than one power number. Expected sections include identity/progression, core attributes, resources, derived values, abilities, mastery/skills, and active status effects.

Hidden properties may remain undiscovered/locked (`???`) until gameplay reveals them.

The screen must remain readable: deep systems can be expandable rather than placing every internal variable on the primary view.

Exact field names, formulas, layout density, and the seven-vs-eight core-stat schema remain provisional/open where noted in `GAME_DIRECTION_AND_UI.md`.

---

## DEC-MOD-001 — Unified effective-value modifier contract

Status: [DESIGNED] ACCEPTED / [IMPLEMENTED] ON FEATURE BRANCH

Implementation branch: `feature/effective-stat-pipeline`
Inspected tip during this review: `ac49e62affb7458f51fd486e41e46df7860a93af`

Accepted contract:
- permanent/base attributes and skills remain unchanged by temporary/equipment modifiers
- effective values are additive views over base state
- current modifier sources are equipped items, active equipment-set thresholds, perks, and active conditions/injuries
- canonical attribute paths use `attributes.<id>`
- canonical skill paths use `skills.<id>`
- direct derived modifiers use `derived.<id>`
- derived calculations consume effective attributes/skills and then apply direct `derived.*` modifiers exactly once
- per-source provenance must remain inspectable rather than collapsing immediately into an unexplained total
- condition severity is metadata unless authored rules explicitly translate severity into a numeric modifier
- equipment requirements intentionally use permanent/base attributes and skills, preventing circular/order-dependent qualification

Compatibility finding:
- the feature branch adds optional parameters/exports rather than removing the existing public surface
- persistence schema/state shape was not changed by this diff
- legacy equipment modifier helper imports remain available through the existing module/public package surface

Test-state distinction:
- focused tests are present on the feature branch for stacking, set/condition use in rule requirements, derived-stat application, and no double counting
- this chat inspected those tests but did not execute them; passing runtime status is therefore not claimed here

Related checkpoint: `CP-2026-09-27-EFFECTIVE-PIPELINE-03`

---

## DEC-MOD-002 — Effective-value domain validation and floors

Status: [QUESTION] OPEN

Before the effective-value feature is treated as integration-complete, define two authoring/runtime policies:

1. Modifier-path validation
   - decide whether unknown/typo paths such as `attributes.migth` are rejected at content-validation time
   - define the allowed namespace/ID registry for `attributes.*`, `skills.*`, and `derived.*`

2. Derived/resource lower bounds
   - direct `derived.*` modifiers can currently make values such as `max_health`, `max_stamina`, or `carry_capacity` negative
   - decide whether each derived value is unbounded, clamped to a domain floor, or rejected when authored content would cross that floor

UI/debug note:
- `modifier_breakdown()` gives a complete provenance breakdown for player-relative base paths such as attributes/skills
- a future UI that wants to explain a final calculated derived value should expose the formula-derived base plus direct `derived.*` contributions, not present the direct modifier total alone as the full derivation
