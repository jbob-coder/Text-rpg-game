# AGENTS.md — Text RPG Game

This file is the repository entry point for coding agents and automated assistants.

## Read first

Before changing code or documentation, read these in order:

1. `docs/THE_GAME_MASTER_TASK_REGISTER.md` — current objective, task queue, blockers, completion timestamps, Android black-screen status, and cross-chat continuity.
2. `docs/IMPLEMENTATION_STATUS.md` — verified engine/repository state.
3. `docs/V6_STABILIZATION_HANDOFF.md` — exact V6 stabilization evidence, runtime defects, repairs, and verification boundaries.
4. Relevant source/tests for the task you are actually changing.

Repository files and fresh execution evidence outrank remembered chat context.

## Current working baseline

- Repository: `jbob-coder/Text-rpg-game`
- Stabilization branch at the time this entry point was added: `fix/v6-runtime-boundaries`
- Parent V6 line: `integration/rules-ability-v6-reconcile`
- `main` is not the canonical implementation branch. Do not promote, rewrite, or merge `main` merely because it is the default branch.
- The Android test APK has a user-reported black-screen startup defect. Do not claim Android is fixed until a rebuilt package is tested on a representative Android runtime/device.

Use `docs/THE_GAME_MASTER_TASK_REGISTER.md` for the live status rather than copying this snapshot forward.

## Engineering rules

- Inspect current files/HEAD before repository-specific claims.
- Prefer the smallest reversible change that solves the root cause.
- Keep authoritative gameplay state in the engine; presentation clients consume player-safe projections.
- Do not duplicate stat/equipment/rules calculations inside UI code.
- Preserve stable IDs and save compatibility unless an explicit migration is designed and tested.
- Do not expose hidden authored rules or secret provenance through player-facing projections.
- Add/update regression tests for behavior changes when practical.
- Never say tests/builds pass unless they were executed and observed for the exact code being claimed.
- When Android behavior is involved, Python unit tests alone are not sufficient evidence.
- Avoid unrelated broad refactors while fixing a focused defect.

## Task bookkeeping

For meaningful work, update `docs/THE_GAME_MASTER_TASK_REGISTER.md`:

- State: `PENDING`, `IN_PROGRESS`, `BLOCKED`, or `DONE`.
- A `DONE` task must include `COMPLETED_AT` using `America/Puerto_Rico` time.
- Record files changed, tests/commands actually run, results, blockers, and any changed assumptions.
- Do not invent historical completion times; use `NOT_RECORDED` if the exact time was never captured.

## Verification commands

Engine suite:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

The repository currently contains prior verification evidence under `docs/verification/v6/`, but historical logs are not a substitute for rerunning tests after new runtime changes.

## Handoff standard

Before ending a substantial coding session, leave enough repository-native evidence that the next agent can answer:

- What is the current objective?
- What exact HEAD/branch was worked on?
- What changed?
- What was actually tested?
- What failed or remains unverified?
- What is the next action?
- What must not be assumed?

Do not rely on private chain-of-thought or ephemeral chat history for continuity.
