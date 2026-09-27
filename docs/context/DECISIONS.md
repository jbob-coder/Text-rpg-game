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

Detailed evaluation: `docs/context/STAT_SCHEMA_EVALUATION.md`
Migration architecture if eight stats are accepted: `docs/context/STAT_SCHEMA_MIGRATION_PLAN.md`

Current design recommendation candidate: eight core attributes, because separating Dexterity from Agility removes a repeated responsibility conflict and Constitution cleanly separates durable bodily resilience from the spendable Stamina resource. This remains [DESIGNED], not canonical, until explicitly accepted and migrated.

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


---

## DEC-MOD-003 — Contract hardening candidates before pipeline closure

Status: [DESIGNED] CANDIDATE / [IMPLEMENTED] ON REVIEW BRANCH / NOT YET VERIFIED

Historical review branch: `review/effective-stat-contract-hardening`
Current integrated review branch: `integration/rules-ability-v5`

[SUPERSEDED] The historical review branch is no longer the active promotion target. Its hardening contract has been carried forward through later hardening/integration branches; current implementation claims must be checked against `integration/rules-ability-v5` (or a newer explicitly recorded successor), not the historical review tip.

This decision records the current evolution candidate without declaring it canonical or complete.

Candidate A — exact modifier-path registry:
- attribute modifiers must use a known `attributes.<id>`
- skill modifiers must use a known `skills.<id>`
- direct derived modifiers must use a known `derived.<id>`
- typoed IDs and unsupported namespaces are rejected at authoring/runtime boundaries rather than silently ignored

Candidate B — derived-value domain policy:
- non-negative capacity values: max Health, max Stamina, max Focus, max Resolve, carry capacity
- signed contest values: initiative, accuracy, evasion, guard may go below zero so severe penalties still affect margins

Candidate C — explainability contract:
- derived formulas are centralized as data
- `derived_stat_breakdown()` exposes weighted inputs, direct modifiers, floor adjustment, and final total
- `RulesEngine.explain_player_value()` is the single rules-facing explanation API intended for debug/status UI

Why this is not closed:
- the current integration tests have not yet been executed by this chat on a byte-for-byte checkout
- the full repository suite has not been executed on the current integration branch
- the parent foundation is changing concurrently and requires a frozen-SHA reconciliation before promotion
- the domain/floor policy is an architecture/balance choice and should remain reversible until verified in play and accepted for promotion

Related: `CP-2026-09-27-EFFECTIVE-HARDENING-04`


---

## DEC-TEST-001 — User is final acceptance tester, not intermediate QA

Status: [DIRECTION] ACCEPTED

The user will not test the game during normal development. Intermediate implementation must not depend on the user launching builds, reproducing defects, checking screens, or running manual regression steps.

Verification responsibility stays inside the development workflow through static inspection, authored automated tests, deterministic simulation, content/schema validation, save/load verification, exact-SHA evidence, and free/local runtime execution where available.

Unexecuted tests must never be described as passing. If exact runtime verification is unavailable, the affected gate remains open and the project must not be promoted by assumption.

The current Stage 3 runtime gate therefore remains mandatory even though the user will not perform intermediate testing.

Do not introduce paid/billing-risk CI solely to obtain test execution without explicit user authorization.

The user should be asked to perform a game check only when a final acceptance/release candidate exists: agreed scope implemented, required automated suite green on the exact candidate SHA, validators clean, applicable save/load/progression/migration paths verified, no known release-blocking defects, documentation synchronized, and a playable/runnable package prepared.

Detailed policy: `docs/context/FINAL_ACCEPTANCE_AND_TESTING_POLICY.md`


---

## DEC-WORLD-001 — Medieval crystal-craft setting

Status: [DIRECTION] ACCEPTED

The game uses a medieval material/technology baseline. Weapons, armor, tools, settlements, mines, roads, and ordinary infrastructure are medieval in character.

Crystal power is the exceptional technology layer and augments forged equipment rather than replacing the setting with modern/cybernetic technology.

Primary crystal sources:
- natural mine deposits;
- crystals biologically integrated beside/around a beast's heart/core.

Mine crystals are generally more stable and standardized. Beast-heart crystals may preserve stronger species/evolution traits but are riskier to acquire intact.

Detailed contract: `docs/context/MEDIEVAL_CRYSTAL_BEAST_SYSTEMS.md`.

---

## DEC-COMBAT-001 — Positional body-zone combat

Status: [DIRECTION] ACCEPTED / [DESIGNED] NOT IMPLEMENTED

Combat must not expose every anatomical target at all times.

Reachable target zones are determined by authoritative combat state including range, relative facing, elevation, posture, weapon reach/type, cover, terrain, grapple/control, stagger/knockdown, body configuration, and battle phase.

Battle-state transitions can reveal or remove target zones. Environment and positioning are therefore part of attack selection, not visual decoration.

Zone damage may create persistent mechanical consequences such as impaired movement, senses, attacks, flight, guard, or crystal-core damage.

The future UI must consume a player-safe targetability projection and must not independently infer reachable zones.

---

## DEC-EQUIP-001 — Forged weapons, coverage armor, and crystal integration

Status: [DIRECTION] ACCEPTED / [DESIGNED] NOT IMPLEMENTED

Weapons are physical rule objects with meaningful differences in reach, handling, balance, momentum, recovery, stamina burden, damage profile, penetration, guard, target access, durability, and crystal integration.

Armor uses internal body-zone coverage and damage-type resistance rather than one universal defense value, while the player-facing equipment UI may remain simpler.

Crystal integration is a staged forge process with compatibility, quality, stability, socket/fusion, maintenance, and provenance.

Direct heart/core attacks can increase lethality while damaging the beast crystal, creating a deliberate kill-speed versus loot-quality tradeoff.

---

## DEC-BEAST-001 — Persistent beast progression, memory, and adaptation

Status: [DIRECTION] ACCEPTED / [DESIGNED] NOT IMPLEMENTED

Important beasts can persist as world entities with stable IDs, level/development, attributes/skills, injuries, crystal/core state, memories, adaptations, territory, social role, followers/rivals, goals, and communication capability.

Retreat does not reset a surviving beast.

A beast may learn from encounters, but adaptation is constrained by what it actually observed, observation confidence, intelligence, memory/learning capacity, biology, time, injuries, and available resources. No arbitrary omniscient counter-buffs are allowed.

Beast level is a progression summary/gate, not the sole source of combat power.

Highly capable social beasts may become chieftains/commanders/territory rulers only when intelligence, social capacity, followers, victories, and territory support that role.

Off-screen beast-versus-beast development should use deterministic coarse regional simulation rather than continuous full combat.

---

## DEC-BEAST-002 — Intelligence-gated beast communication

Status: [DIRECTION] ACCEPTED / [DESIGNED] NOT IMPLEMENTED

Beast communication complexity is constrained by intelligence, species anatomy/language capability, social role, memory, and current encounter state.

Low-capability beasts use vocalizations/signals. Higher-capability beasts may use simple speech, tactical commands, remembered references, negotiation, deception, or long-horizon planning.

Dialogue remains authored/template-driven and state-backed. Runtime generative AI is not required for authoritative gameplay.

---

## DEC-STAGE-002 — Medieval/crystal feature work follows V6 verification

Status: [DECISION] ACCEPTED

The medieval/crystal expansion is now accepted design and backlog scope, but it must not be merged into the current V6 promotion candidate while the Stage 3 exact-runtime gate remains unresolved.

Implementation begins from a verified integration baseline or an explicitly isolated prototype branch that cannot be mistaken for the promotion candidate.

Task source: `docs/context/IMPLEMENTATION_BACKLOG.md`.
