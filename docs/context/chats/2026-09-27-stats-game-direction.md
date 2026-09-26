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

[SUPERSEDED] A temporary attempt to move directly into integrating equipment-set and condition modifiers into runtime checks was stopped after the user clarified the actual shared task.

[DIRECTION] Current priority is design of the stat schema and game-system architecture. Runtime integration work should follow after the relevant design decisions are deliberately resolved.

## Documentation work completed in this chat

[VERIFIED] Added/established:
- `docs/context/README.md`
- `docs/context/CONTEXT_SYNC_PROTOCOL.md`
- `docs/context/CHECKPOINTS.md`
- `docs/context/DECISIONS.md`
- `docs/context/GAME_DIRECTION_AND_UI.md`
- this per-chat record

## Tests

No runtime tests were executed by this chat for the design/documentation work.

The repository status document reports historical passing tests, but this chat does not claim fresh execution.

## Open decisions

1. Seven core attributes vs eight.
2. Whether Dexterity should be a separate core stat or remain under Agility/skills.
3. Final naming of physical durability: `endurance` vs `constitution` and exact responsibility boundary.
4. Whether overall character Level/EXP remains a visible top-level progression system or whether progression is primarily distributed across skills/abilities/masteries.
5. Which derived values deserve persistent UI exposure versus internal calculation only.
6. Final status-screen information density and navigation.

## Next design work

- test both stat schemas against concrete gameplay scenarios
- define clean ownership for every candidate attribute
- expand the complete system catalog beyond stats without duplicating responsibilities
- map each visible status-screen field to an authoritative underlying state source
- record final resolutions in `DECISIONS.md` before changing implementation
