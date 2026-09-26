# Project Checkpoints

Checkpoints are evidence snapshots. They do not replace source files or tests.

## CP-2026-09-26-A — Shared Context Foundation

Status: CONFIRMED

Repository: `jbob-coder/Text-rpg-game`
Branch: `shared/game-context`
Base lineage: `foundation/text-rpg-systems`

Confirmed artifacts:

- `docs/chat_context/README.md`
- `docs/chat_context/CHATGPT_TEXT_RPG_CONTEXT_2026-09-26.md`
- `docs/ARCHITECTURE_MARKOUTS.md`
- `docs/GAME_FOUNDATION.md`
- `docs/SYSTEMS_CATALOG.md`
- `docs/IMPLEMENTATION_STATUS.md`
- `docs/REFERENCE_NOTES.md`
- `docs/VISUAL_BIBLE.md`

Authority rule: repository files outrank chat recollection. Conflicts are recorded and resolved against current files/tests rather than blended silently.

## Historical verification carried forward

`docs/IMPLEMENTATION_STATUS.md` records a previous branch-equivalent verification of 29 unit tests passing with 0 failures.

Classification: HISTORICAL EVIDENCE, not current-branch proof.

A future checkpoint may promote this to current verified state only after tests are executed against the exact commit being claimed.

## Next checkpoint target

CP-2026-09-26-B should be created after the next game-code change and should include:

- exact commit SHA
- markouts touched
- files changed
- behavior changed
- tests added/updated
- commands actually run
- observed results
- remaining unknowns or blockers
