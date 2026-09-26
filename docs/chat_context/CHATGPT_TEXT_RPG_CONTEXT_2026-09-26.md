# ChatGPT Text RPG Context — 2026-09-26

## CURRENT_OBJECTIVE

Keep the Text RPG project and its cross-chat knowledge synchronized without treating chat memory as authoritative implementation state.

## AUTHORITY ORDER

1. Current repository files and executable verification evidence.
2. Explicit project decisions recorded by Jack in repository documentation.
3. Current-chat observations verified against repository state.
4. Prior-chat summaries and recollection.
5. External reference material.

When chat recollection conflicts with repository files, the repository wins. The conflict must be recorded rather than silently merged.

## CONFIRMED

- Shared context branch: `shared/game-context`.
- Base architecture branch: `foundation/text-rpg-systems`.
- Game direction: authored, stateful choice-driven RPG with deterministic rules, persistent consequences, NPC memory/knowledge, earned progression, equipment, conditions, training, and pixel-art presentation kept separate from the rules layer.
- Runtime generative AI is not required for gameplay.
- Important continuity belongs in stable IDs and save state, not in prose-only chat memory.
- Reference novels are research material only; they are not game canon and must not be copied into the original IP.

## DIRECTION

- Every chat working on this project should leave a separate context record under `docs/chat_context/`.
- Shared decisions should be promoted into canonical docs only after repository verification and, when needed, Jack's explicit decision.
- Complex work should use checkpoints, markouts, decision records, conflict records, and handoffs so another chat can reconstruct the project state.
- Work should continue on the game itself rather than stopping after documentation maintenance.

## CURRENT_GAME_STATE

The repository documentation states that the foundation slice includes deterministic scene resolution, persistent state/history, hidden/locked choices, four-degree checks, relationship/knowledge gates, inventory requirements, quest-stage effects, bounded NPC personality drift, equipment/perk modifiers, ability mastery, versioned saves, validation, seven core attributes, derived stats, recovery, timed conditions, training, equipment sets, NPC memory/private knowledge, deterministic leak-candidate evaluation, and visual consistency rules.

The latest recorded verification in `docs/IMPLEMENTATION_STATUS.md` reports 29 tests passing on a branch-equivalent reconstruction. That evidence is historical until re-run against the exact current branch state.

## NEXT_GAME_WORK

Highest-priority technical follow-up from the current repository status:

1. Integrate condition modifiers and equipment-set bonuses into the effective stat/check pipeline without double-counting.
2. Add explicit power resource costs, cooldowns, drawbacks, technique stages, and evolution prerequisites.
3. Expand NPC goals/story-state transitions and multidimensional relationship utilities.
4. Add quest graph definitions and validation.
5. Execute deterministic authored information-propagation events rather than only listing eligible leak targets.
6. Define the first original playable vertical slice and opening scenario.

## CONFLICT RULE

If another chat reports implementation that is absent from the branch, label it `UNVERIFIED` until the files/tests prove it. If the repository contains newer behavior than this record, this record is stale and must be updated or superseded.

## HANDOFF

A new chat should first read:

- `docs/chat_context/README.md`
- `docs/ARCHITECTURE_MARKOUTS.md`
- `docs/CHECKPOINTS.md`
- `docs/IMPLEMENTATION_STATUS.md`
- `docs/GAME_FOUNDATION.md`
- `docs/SYSTEMS_CATALOG.md`

Then inspect the current source and tests before making implementation claims.
