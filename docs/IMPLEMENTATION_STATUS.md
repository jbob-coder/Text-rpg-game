# Implementation Status — Foundation Slice

## CURRENT_OBJECTIVE

Create the non-AI authored RPG foundation: persistent choices, stats, NPC memory, hidden information, equipment/perks, earned power progression, deterministic checks, save compatibility, simulation time, training, recovery, and pixel-art consistency rules.

Current sub-objective: harden the effective-value pipeline before closure: reject invalid modifier paths, define safe domains for derived capacities, and expose enough provenance for RulesEngine/UI to explain final effective and derived values without mutating base stats or double counting.

## VERIFIED_STATE

Repository: `jbob-coder/Text-rpg-game`

Foundation branch: `foundation/text-rpg-systems`

Current implementation branch: `feature/effective-stat-pipeline`

Current review/evolution branch: `review/effective-stat-contract-hardening`

The original `main` branch is not modified by this work.

## COMPLETED

Foundation systems already present before this feature branch:

- Deterministic authored scene engine.
- Persistent player state and history.
- Visible vs hidden vs locked choices.
- Four-degree checks: critical success, success, failure, critical failure.
- Relationship-gated options.
- Player knowledge-gated options.
- NPC knowledge-gated options.
- Party-member-gated options.
- Inventory requirements and item consumption.
- Quest-stage effects.
- NPC personality drift with bounded values.
- Ability mastery XP and rank progression.
- Technique requirements that can depend on rank, mastery, knowledge, and perks.
- Versioned JSON save/load layer with explicit schema rejection.
- Static content validation for stable IDs, duplicate choices, unsupported rules, and invalid scene references.
- Canonical seven-attribute catalog and grouped skill catalog.
- Explicit derived-stat formulas for health, stamina, focus, resolve, initiative, accuracy, evasion, guard, and carry capacity.
- Resource initialization and bounded recovery.
- Timed conditions/injuries with severity, source, tags, modifiers, and expiration through world time.
- Time-based skill training with stamina/focus cost, mentor bonus, and diminishing returns.
- Slow core-attribute training so permanent stats cannot be gained from a single trivial action.
- Equipment slot definitions, requirements, provenance, tags, set IDs, active/passive references, and threshold set bonuses.
- NPC memory records with importance, tags, time, and contextual data.
- NPC-owned private knowledge with confidence, truth state, secrecy, and source.
- Explicit character-to-character knowledge sharing.
- Deterministic leak-candidate evaluation based on authored social networks and NPC personality; no generative gossip.
- Pixel visual consistency specification.
- Abstract reference extraction notes that avoid copying source story content.
- Systems catalog documenting the stat/training/equipment/social contract.

Implemented on `feature/effective-stat-pipeline`:

- One additive modifier aggregation layer for equipment, equipment-set thresholds, perks, and active conditions/injuries.
- Canonical modifier paths for attributes, skills, and direct derived values.
- Per-source modifier breakdown suitable for debugging and future status-screen explanations/tooltips.
- Rules-engine stat requirements/checks now use the unified effective value and can receive set definitions.
- Derived stats now use effective attributes/skills and direct `derived.*` bonuses.
- Resource maxima now inherit effective derived values.
- Recovery and training accept set-definition context so resource maxima remain consistent when set bonuses are active.
- Equipment requirement checks deliberately remain based on permanent/base values to avoid circular/order-dependent gear qualification.
- Condition severity remains metadata; authored modifier magnitudes are not silently multiplied by severity.
- New targeted tests cover stacking, set-aware choice requirements, condition penalties, direct derived modifiers, repeated calculations, and base-stat immutability.

Implemented on the review/evolution branch but **not yet promoted back to the feature branch**:
- Central stat/schema registry shared by calculation and validation code.
- Canonical modifier-path validation for attributes, skills, and derived values.
- Invalid equipment/condition/perk/set modifier paths are rejected at their authoring/runtime boundaries instead of being silently ignored.
- Scene validation checks stat requirement/check paths and perk modifier maps.
- Capacity-style derived values have explicit zero floors; contest-style scores remain allowed to go negative.
- Derived formulas are centralized as data.
- `derived_stat_breakdown()` explains formula constants, effective weighted inputs, direct modifiers, floor adjustment, and final total.
- `RulesEngine.explain_player_value()` exposes one player-value explanation API for attributes/skills and fully calculated derived values.

## TESTS_RUN

Parent foundation verification previously recorded:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Parent-branch result: **29 tests passed, 0 failed**.

For the new effective-stat feature, a targeted branch-equivalent reconstruction was executed against the new modifier/check/derived-stat behavior. Result: **targeted modifier-pipeline verification passed**.

Verified by that targeted run:
- base + equipment + set + perk + condition stacking
- exact per-source total
- base-stat immutability
- stat requirement enabled/disabled state after effective modifiers
- condition penalties affecting derived stats
- direct `derived.*` bonuses
- repeated derived calculations do not accumulate modifiers
- resource maxima use the effective derived result

The complete repository test suite has **not yet been re-run against the new feature branch**, so the feature branch is implemented but not yet fully VERIFIED as a whole.

The review/evolution branch adds further tests for path validation, invalid equipment/condition/set definitions, derived-value floors, and explanation payloads. Those repository tests have been written and inspected but have **not** been executed against an actual branch checkout by this workstream yet.

A branch-equivalent reconstructed execution of the reviewed hardening logic was performed separately and passed the targeted semantic scenarios (stacking/provenance, derived formula + direct modifier, capacity floors, signed contest score, invalid-path rejection). This is supporting evidence only; it does **not** replace execution of the repository test suite.

Do not treat the review branch as fully VERIFIED or merge-ready solely because the authored tests and reconstructed scenarios pass.

No GitHub Actions workflow was added; verification does not consume hosted CI minutes.

Detailed hardening review evidence: `docs/EFFECTIVE_STAT_HARDENING_REVIEW.md`.

## NEXT_ACTION

1. Execute the complete repository suite against `review/effective-stat-contract-hardening`, fix regressions, and compare behavior with the parent feature branch.
2. Review the new path/floor/explainability contract and promote it back to `feature/effective-stat-pipeline` only after verification.
3. Re-run the full suite again on the final promoted feature tip and record the exact command/result.
4. Add power resource costs, cooldowns, technique stages, drawbacks, and evolution prerequisites.
3. Add explicit NPC goal/story-state transitions and multidimensional relationship utilities.
4. Add quest graph definitions, branching objectives, failure states, and content-pack validation.
5. Add deterministic information propagation events that execute authored leak rules rather than only listing candidates.
6. Define the first original playable vertical slice and its canon opening scenario.
7. Add character visual identity records that can drive consistent pixel portrait/sprite generation.
8. Connect the rules layer to the chosen pixel-art presentation runtime after the client technology is deliberately selected.

## BLOCKERS

The rules core is not blocked.

Full-branch verification is still pending because the current connected repository workflow can inspect and modify remote files but does not provide a normal local Git checkout by itself. Targeted reconstructed execution is available and has been used without hosted CI billing.

The visual/runtime implementation should not be hard-wired yet because the final client technology has not been established in the repository. Keeping rules separate avoids throwing away work if the presentation target changes.

## IMPORTANT_DECISIONS

- Runtime generative AI is not a dependency.
- Important continuity lives in save state and stable IDs, not chat memory.
- Core attributes progress slowly; skills and mastery can progress faster.
- Powers require earned progression rather than instant button unlocks.
- Information and conversations are first-class gameplay state.
- Important NPCs use multidimensional relationships instead of one friendship score.
- Secret propagation remains deterministic, inspectable, and authored.
- Effective-value modifiers are additive in the current contract and must be applied through one pipeline.
- Equipment/set/perk/condition modifiers do not rewrite the player’s permanent base values.
- Equipment requirements use permanent/base attributes and skills to avoid circular equipment dependencies.
- Art generation must obey a canonical visual identity sheet before an asset becomes game canon.

## KNOWN_RISKS

- Too many stats can create unreadable UI and redundant mechanics. Every stat needs a distinct rule purpose.
- Excessive branching can cause content explosion. Recombining branches around durable state is preferred over writing a completely separate story for every choice.
- Hidden information must be scoped to the correct character/player knowledge stores or secrets can leak accidentally.
- Progression and recovery numbers are provisional until a playable loop provides balancing evidence.
- Set-definition context must be supplied consistently anywhere set bonuses are expected; a later runtime/service layer should centralize this content context so callers cannot accidentally omit it.
- The current modifier contract is additive only. Multiplicative/capped/override stacking must be deliberately designed before introduction rather than patched ad hoc.
