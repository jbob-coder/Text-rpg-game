# Project Checkpoints

Append-only checkpoints for reconstructing project state across chats.

---

## CHECKPOINT_ID: CP-2026-09-27-STATS-SCHEMA-01

Repository: `jbob-coder/Text-rpg-game`
Context branch: `shared/game-context`
Implementation branch referenced by existing status docs: `foundation/text-rpg-systems`

### CURRENT_OBJECTIVE

[DIRECTION] Design the game's stat schema and broader system catalog in enough detail that multiple chats can contribute without drifting. The immediate shared task is **design architecture**, not runtime implementation.

### DIRECTION

[DIRECTION] The game is a life-and-decisions text RPG with slow progression, meaningful consequences, persistent world/character state, earned capability, and a world that feels alive because earlier actions alter later states.

[DIRECTION] Progress should not come from trivial or instantaneous gains. Attributes move slowly; narrower skills/mastery can advance faster.

[DIRECTION] Important continuity must live in structured game state and stable IDs, not only prose or chat memory.

### VERIFIED_STATE

[VERIFIED] The shared context branch contains the existing game foundation, implementation-status, systems catalog, reference notes, visual bible, and the new context architecture index.

[IMPLEMENTED] Existing repository files currently define a seven-attribute catalog: `might`, `agility`, `endurance`, `intellect`, `will`, `perception`, `presence`.

[IMPLEMENTED] Existing repository design/code also includes skills, derived values, resources, training, conditions/injuries, recovery, equipment, equipment sets, NPC memory/knowledge, and deterministic secret-propagation support.

### DESIGNED_NOT_IMPLEMENTED

[DESIGNED] This chat proposed an expanded eight-attribute model that separates Agility and Dexterity and uses Constitution as a dedicated robustness attribute:
`STR / CON / AGI / DEX / PER / INT / WIL / PRE`.

[DESIGNED] The intended layer model is:
`core attributes -> resources -> derived statistics -> abilities -> mastery -> techniques -> evolution`.

[DESIGNED] Character level, ability level, mastery, technique progression, and evolution progression should remain separable concepts.

### CONFLICTS

[CONFLICTING] `STAT-ATTR-001`: current repository has seven core attributes; this chat has proposed eight. The key unresolved issue is whether `agility` should continue covering coordination/precision or whether `dexterity` becomes a separate core attribute. Do not change executable code until the design is intentionally resolved.

### COMPLETED

[VERIFIED] Added `docs/context/README.md` defining authority order, state labels, branch roles, anti-drift rules, and canonical reading order.

[VERIFIED] Added `docs/context/CONTEXT_SYNC_PROTOCOL.md` defining markup, checkpoint, handoff, conflict, and compression rules.

### IN_PROGRESS

[DESIGNED] Build a complete, non-redundant stats/system architecture and compare it against the current seven-attribute foundation before selecting the canonical schema.

### NEXT_ACTION

1. Define the responsibility boundary for every candidate core attribute.
2. Test the schema against physical combat, stealth, social play, investigation, technical tasks, injury/recovery, training, powers, and life-simulation decisions.
3. Remove redundant attributes or split overloaded ones.
4. Define which values are core attributes vs skills vs resources vs derived values.
5. Record the resolved schema in `DECISIONS.md` before implementation changes.

### BLOCKERS

[BLOCKER] No implementation blocker. Canonical stat-schema selection is intentionally unresolved.

### RISKS

[RISK] Too many core stats can make the UI and balancing unreadable.
[RISK] Too few core stats can make attributes overloaded and reduce build identity.
[RISK] Renaming or splitting already implemented attributes will require save/schema migration if done after content expands.

### FILES_CHANGED

- `docs/context/README.md`
- `docs/context/CONTEXT_SYNC_PROTOCOL.md`
- `docs/context/CHECKPOINTS.md`

### TESTS_RUN

None by this chat for this design checkpoint.

### TEST_RESULTS

[UNKNOWN] Existing `IMPLEMENTATION_STATUS.md` reports 29 passing tests from earlier branch-equivalent verification. This chat has not rerun them and does not claim fresh verification.

### EVIDENCE

- `docs/GAME_FOUNDATION.md`
- `docs/SYSTEMS_CATALOG.md`
- `docs/IMPLEMENTATION_STATUS.md`
- current conversation direction

---

## CHECKPOINT_ID: CP-2026-09-27-GAME-DIRECTION-UI-02

Repository: `jbob-coder/Text-rpg-game`
Context branch: `shared/game-context`

### CURRENT_OBJECTIVE

[DIRECTION] Preserve in durable project documentation exactly how the user wants the game to feel and how the player-facing status/character screen should represent the underlying systems, while keeping unresolved stat-schema decisions explicit.

### DIRECTION

[DIRECTION] Life-and-decisions RPG first: systems exist to create persistent consequences, long-term character development, and a living world.

[DIRECTION] Slow, earned progression is mandatory project direction. No trivial instant permanent gains.

[DIRECTION] Player/NPC knowledge, memories, relationships, injuries, time, equipment, quests, powers, and prior conversations can persist and influence later content.

[DIRECTION] The status screen must make deep state understandable without turning the game into a constant spreadsheet view.

### VERIFIED_STATE

[VERIFIED] `docs/context/GAME_DIRECTION_AND_UI.md` now records the game direction, progression philosophy, layered player-state model, resource/ability concepts, living-world expectations, and the status-screen reference discussed in this chat.

[VERIFIED] `docs/context/DECISIONS.md` now exists and records accepted direction plus the unresolved seven-vs-eight-attribute decision.

[VERIFIED] `docs/context/chats/2026-09-27-stats-game-direction.md` preserves this workstream's user instructions, designs, correction of scope, open decisions, and next design work.

[VERIFIED] `docs/context/README.md` and `CONTEXT_SYNC_PROTOCOL.md` now require future chats to read the game-direction/UI specification as part of the canonical startup workflow.

### DESIGNED_NOT_IMPLEMENTED

[DESIGNED] Status-screen structure includes:
- identity/progression
- core attributes
- Health/Stamina/Focus/Resolve and relevant power-specific resources
- selected derived/combat values
- ability rank/level/mastery/control/efficiency/techniques where appropriate
- skills/masteries
- active injuries/conditions/status effects
- hidden/undiscovered properties without leaking discovery content

[PROVISIONAL] Exact screen typography, field names, density, overall Level/EXP usage, and final attribute list are not yet canonical.

### CONFLICTS

[CONFLICTING] Seven implemented core attributes versus the eight-attribute design candidate remains unresolved. The UI specification must adapt to whichever schema becomes canonical.

### COMPLETED

- Preserved game direction in a dedicated required-reading document.
- Preserved the status-screen concept as a structural design reference.
- Added a design decision log.
- Added the first per-chat context record.
- Updated canonical reading/synchronization rules so future chats inherit this context.

### IN_PROGRESS

[DESIGNED] Continue developing the stat schema and complete game-system catalog; do not treat the status-screen example or eight-stat proposal as already implemented.

### NEXT_ACTION

1. Stress-test seven-stat and eight-stat schemas against representative gameplay.
2. Decide attribute responsibility boundaries.
3. Decide whether a top-level character Level/EXP is retained.
4. Map every visible status-screen field to its authoritative game-state source.
5. Expand systems catalog while preserving slow progression and persistent consequence as global constraints.

### BLOCKERS

No blocker to design work. Attribute-schema choice remains intentionally open.

### RISKS

[RISK] UI can become overloaded if every internal value is always visible.
[RISK] Hidden information can be accidentally leaked if status UI exposes undiscovered power properties.
[RISK] A stat-schema migration becomes more expensive if delayed until large amounts of authored content depend on old stat names.

### FILES_CHANGED

- `docs/context/GAME_DIRECTION_AND_UI.md`
- `docs/context/DECISIONS.md`
- `docs/context/chats/2026-09-27-stats-game-direction.md`
- `docs/context/README.md`
- `docs/context/CONTEXT_SYNC_PROTOCOL.md`
- `docs/context/CHECKPOINTS.md`

### TESTS_RUN

None. This checkpoint concerns design/documentation, not runtime behavior.

### TEST_RESULTS

No fresh runtime test claim.

### EVIDENCE

- current user direction in this chat
- `docs/GAME_FOUNDATION.md`
- `docs/SYSTEMS_CATALOG.md`
- `docs/context/GAME_DIRECTION_AND_UI.md`
- `docs/context/DECISIONS.md`

---

## CHECKPOINT_ID: CP-2026-09-27-EFFECTIVE-PIPELINE-03

Repository: `jbob-coder/Text-rpg-game`
Context branch: `shared/game-context`
Implementation workstream: `feature/effective-stat-pipeline`
Inspected implementation tip: `ac49e62affb7458f51fd486e41e46df7860a93af`
Foundation base: `e51d8169f629a75c3bf1b0e5d19b318a2bd6d0cb`

### CURRENT_OBJECTIVE

[IMPLEMENTED] Review the unified effective-stat/modifier workstream against the foundation branch, establish the exact authored path contract, and identify incompatibilities/regression risks before treating the integration as complete.

### VERIFIED_STATE

[VERIFIED] Source inspection shows the feature branch is ahead of `foundation/text-rpg-systems` and confines the integration to the systems catalog, package exports, rules engine, equipment helper routing, a new modifier module, simulation resource-context plumbing, derived-stat calculation, and focused modifier tests.

[IMPLEMENTED] `src/textrpg/modifiers.py` centralizes additive modifier sources:
- equipment slots
- active equipment-set thresholds
- perks
- active conditions/injuries

[IMPLEMENTED] `modifier_breakdown()` preserves source provenance (`base`, equipment slot, set threshold, perk ID, condition ID, `total`).

[IMPLEMENTED] `RulesEngine` delegates effective player values to the unified pipeline and accepts optional set definitions.

[IMPLEMENTED] `derived_stats()` now consumes effective attributes/skills and direct `derived.*` modifiers. `initialize_resources()`, `recover()`, and `train()` can receive the same set-definition context.

[IMPLEMENTED] Public package exports add modifier APIs without removing the prior public surface. Legacy equipment helper names remain reachable.

[VERIFIED] The feature branch documents the convention in `docs/SYSTEMS_CATALOG.md` v0.3:
- `attributes.<id>`
- `skills.<id>`
- `derived.<id>`
- base values are not mutated by effective modifiers
- condition severity does not automatically multiply authored modifier magnitude
- equipment requirements use permanent/base values

### COMPATIBILITY_REVIEW

[VERIFIED] No structural persistence migration is introduced by this diff; `GameState`/persistence files are not changed by the feature comparison.

[VERIFIED] Existing call forms remain compatible because new context parameters are optional; no existing required positional API was removed in the inspected diff.

[VERIFIED] Equipment requirement behavior intentionally remains base-stat based to avoid circular/order-dependent equipment qualification.

### TEST_COVERAGE_PRESENT

[IMPLEMENTED] `tests/test_modifiers.py` contains focused tests covering:
- stacking equipment + set + perk + condition once
- preservation of permanent base stat
- per-source breakdown
- rule requirements reacting to set and condition modifiers
- derived stats reacting to effective inputs and direct derived modifiers
- direct set modification of a derived value

### TESTS_RUN

None by this chat.

### TEST_RESULTS

[UNKNOWN] No runtime pass/fail result is claimed by this checkpoint. GitHub combined status for the inspected documentation tip exposed no status checks. Presence of tests is not equivalent to execution.

### OPEN_RISKS

[RISK] Modifier-path validation is not yet an explicit authored-data contract. A typo/unknown path can become an ineffective or misleading modifier unless validation rejects it.

[RISK] Direct `derived.*` modifiers are currently added without domain floors. A sufficiently negative authored modifier can make values such as `max_health`, `max_stamina`, or `carry_capacity` negative; `initialize_resources()` would then trust the resulting resource maximum. The project must define clamp/reject semantics per derived stat.

[RISK] `modifier_breakdown()` fully explains player-relative base values such as attributes/skills, but it does not by itself represent the formula-derived base component of a final derived statistic. A UI tooltip for final derived values will need a derived-calculation breakdown contract if full explainability is required.

### CONFLICTS

None found with persistence/state shape or existing public signatures during this inspection.

The unresolved seven-vs-eight core-stat schema remains a separate design conflict and is not resolved by this pipeline.

### NEXT_ACTION

1. Add/confirm authored-path validation for modifier namespaces and IDs.
2. Decide and test domain-floor semantics for derived/resource maxima.
3. Execute the full test suite on the feature tip and record exact command/result.
4. Add regression tests for existing foundation behavior if the full suite does not already cover all unchanged public entry points.
5. After runtime verification, record merge/readiness state without conflating it with the still-open core-stat schema decision.

### EVIDENCE

- branch comparison `foundation/text-rpg-systems...feature/effective-stat-pipeline`
- `src/textrpg/modifiers.py`
- `src/textrpg/core.py`
- `src/textrpg/stats.py`
- `src/textrpg/simulation.py`
- `src/textrpg/equipment.py`
- `src/textrpg/__init__.py`
- `tests/test_modifiers.py`
- `docs/SYSTEMS_CATALOG.md` v0.3
