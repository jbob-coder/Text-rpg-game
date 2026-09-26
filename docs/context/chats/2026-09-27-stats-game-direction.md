# Chat Record — 2026-09-27 — Stats and Game Direction

## Scope

This chat/workstream is focused on defining what the game should be, especially the player-stat architecture, progression layers, status-screen structure, and the cross-chat context protocol.

## User direction captured

[DIRECTION] The project should feel like a life-and-decisions RPG with slow progression and real consequences.

[DIRECTION] The world should feel alive through persistent state and consequences rather than through disconnected flavor text.

[DIRECTION] Slow progression and persistent consequences are project direction, not a single optional feature.

[DIRECTION] Multiple chats may work separately, but each meaningful chat should write its relevant direction, decisions, checkpoints, conflicts, and handoff state into the shared context branch so future chats can reconstruct the project.

[DIRECTION] The documentation architecture should include markups, checkpoints, handoffs, conflicts, and durable references usable when the project becomes complicated.

[DIRECTION] The shared task between the active chats is currently to define the game-stat schema and broader list of game systems, not to jump ahead into unrelated implementation fixes.

[DIRECTION] The status/character screen discussed in this chat must be preserved as part of the design reference for how the game should communicate player state.

## Designs discussed

[DESIGNED] Proposed eight-stat candidate:
`STR / CON / AGI / DEX / PER / INT / WIL / PRE`.

[DESIGNED] Layered progression/state model:
`core attributes -> resources -> derived statistics -> skills -> abilities -> mastery -> techniques -> evolution`.

[DESIGNED] Character level, ability progression, mastery, techniques, and evolution should not collapse into one universal progression number.

[DESIGNED] Resources include Health, Stamina, Focus, Resolve, and power-specific energy where appropriate.

[DESIGNED] Status screen should have sections for identity/progression, attributes, resources, derived/combat values, ability state, mastery/skills, and status effects/injuries. Hidden information may remain locked/unknown until discovered.

## Existing repository comparison

[IMPLEMENTED] Existing repository currently uses seven core attributes:
`might`, `agility`, `endurance`, `intellect`, `will`, `perception`, `presence`.

[CONFLICTING] The eight-stat proposal is not yet canonical and must not silently replace the current seven-stat implementation.

## Important correction made during this chat

[SUPERSEDED] A temporary attempt by this chat to move directly into integrating equipment-set and condition modifiers into runtime checks was stopped after the user clarified the shared design task.

[DIRECTION] The user then clarified that the other workstream may continue its own implementation task independently while this chat continues design/context synchronization. The two streams must share verified state without conflating their scopes.

## Cross-workstream implementation update

[IMPLEMENTED] A separate implementation workstream now exists on `feature/effective-stat-pipeline`.

[VERIFIED] This chat inspected that branch against `foundation/text-rpg-systems`. The branch implements a unified additive effective-value pipeline covering equipment, equipment-set thresholds, perks, and active conditions/injuries while preserving permanent base values.

[IMPLEMENTED] The branch exposes per-source provenance through `modifier_breakdown()` and routes RulesEngine effective values, derived-stat inputs, resource maxima, recovery, and training context through the shared modifier contract.

[IMPLEMENTED] Canonical modifier namespaces documented on the branch are:
- `attributes.<id>`
- `skills.<id>`
- `derived.<id>`

[IMPLEMENTED] The latest inspected work also resolves `derived.*` paths inside `RulesEngine`, so rule conditions/checks can ask for a calculated derived statistic and unknown derived IDs raise an explicit `RuleError`.

[IMPLEMENTED] Focused modifier-pipeline tests exist. The implementation-status document reports a targeted branch-equivalent verification as passing, but also states the complete repository suite has not yet been rerun on the feature branch.

[UNKNOWN] This chat did not execute the tests itself and therefore does not independently claim the targeted run or full suite result.

[RISK] Remaining review items before integration is considered fully closed:
- validate authored modifier paths/IDs so typos do not silently become ineffective paths
- define lower-bound/clamp/reject behavior for direct `derived.*` modifiers that could make resource maxima or other derived values negative
- if UI must explain final derived values, provide a breakdown that includes the formula-derived base plus direct derived contributions, not only modifier-source totals
- run and record the full repository test suite on the final feature-branch tip

[RELATES_TO:CP-2026-09-27-EFFECTIVE-PIPELINE-03]
[RELATES_TO:DEC-MOD-001]
[RELATES_TO:DEC-MOD-002]

## Documentation work completed in this chat

[VERIFIED] Added/established:
- `docs/context/README.md`
- `docs/context/CONTEXT_SYNC_PROTOCOL.md`
- `docs/context/CHECKPOINTS.md`
- `docs/context/DECISIONS.md`
- `docs/context/GAME_DIRECTION_AND_UI.md`
- this per-chat record

[VERIFIED] Added a durable review checkpoint for the effective-value pipeline and recorded its accepted contract/open validation questions in `DECISIONS.md`.

## Tests

No runtime tests were executed by this chat.

The implementation workstream contains focused tests and reports targeted verification, but this chat distinguishes that reported evidence from tests executed here.

## Open decisions

1. Seven core attributes vs eight.
2. Whether Dexterity should be a separate core stat or remain under Agility/skills.
3. Final naming of physical durability: `endurance` vs `constitution` and exact responsibility boundary.
4. Whether overall character Level/EXP remains a visible top-level progression system or whether progression is primarily distributed across skills/abilities/masteries.
5. Which derived values deserve persistent UI exposure versus internal calculation only.
6. Final status-screen information density and navigation.
7. Modifier-path validation policy.
8. Per-derived-stat lower-bound/clamp/reject policy.
9. Final explainability contract for calculated derived values in UI/debug tooling.

## Next design work

- test both stat schemas against concrete gameplay scenarios
- define clean ownership for every candidate attribute
- expand the complete system catalog beyond stats without duplicating responsibilities
- map each visible status-screen field to an authoritative underlying state source
- preserve the effective-value pipeline as infrastructure without treating it as resolution of the seven-vs-eight attribute design
- record final resolutions in `DECISIONS.md` before changing canonical stat identities
