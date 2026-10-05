# AGENTS.md — Text RPG Game

This file is the repository entry point for coding agents and automated assistants.

## Read first

**Priority repository:** `jbob-coder/Text-rpg-game`.

Before changing code or documentation, read these in order:

1. `docs/AI_TASK_BULLETIN_BOARD.md` — mandatory live work queue. Claim an eligible task here before discretionary project work; on completion, write the required Brag Card, create/refresh the next evidence-backed task, then claim a different one.
2. `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md` — current top-level project authority, permissions, prohibitions, volumes, gates, and final rebuild direction.
3. `docs/MASTER_DOCUMENTATION_RECORD.md` — canonical master record of what documentation exists, what is complete, what is partial, what is missing, blockers, and next actions.
4. `docs/FINAL_GAME_RECONSTRUCTION_BLUEPRINT.md` — integration blueprint tying change authority, asset stages, world canon, mechanics migrations and final APK reconstruction together.
5. `docs/MASTER_DIRECTIVE_EXECUTION_BREAKDOWN.md` — ordered execution phases for the owner's long-range directive.
6. `docs/DOCUMENTATION_CROSS_REFERENCE_MATRIX.md` — what each major document owns and what consumes it.
7. `docs/THE_GAME_MASTER_TASK_REGISTER.md` — operational task state, blockers, evidence and next action.
8. `docs/IMPLEMENTATION_STATUS.md` — verified historical/current implementation evidence.
9. Relevant domain master document for the work being changed.
10. Relevant source/tests for the task being changed.
11. `docs/V6_STABILIZATION_HANDOFF.md` only when exact historical V6 evidence is needed.

Repository files and fresh execution evidence outrank remembered chat context. Older game repositories, prototypes and historical reports are not authority unless an explicit migration record says otherwise.

## Current working baseline

- Repository: `jbob-coder/Text-rpg-game`.
- Program authority branch: `docs/master-game-development-program`.
- Current mode: **documentation first**; broad implementation expansion follows written contracts.
- Gate Twelve is the first proof region; its Steps 1–14 planning packet is complete, and the next P0 work is exact implementation/asset audit plus reproducible corpus inventory.
- `main` is not the canonical implementation branch. Do not promote, rewrite, or merge `main` merely because it is the default branch.
- Historical V6 and Android branches remain evidence sources, not top-level product authority.
- The old black-screen incident is historically closed by the repository-owned Compose/Chaquopy client on representative emulator evidence; physical Galaxy A03 validation remains a separate gate and must not be inferred from emulator results.

Use the master program, master documentation record, and task register for live status rather than copying historical snapshots forward.

## Default project permissions

The project owner has granted standing authorization for routine project engineering work. Within a non-protected working branch, agents may proceed without repeatedly asking for permission to:

- create, modify, move, or remove project source files, tests, documentation, tooling, configuration, and build files when the change serves the current objective;
- refactor implementation while preserving behavior/contracts or providing an explicit migration;
- add diagnostics, regression tests, developer tooling, build scripts, and repository-native continuity files;
- create working branches and commits, update handoff/status documentation, and choose internal file placement/organization;
- run available tests, builds, static checks, local tooling, and debugging steps;
- repair defects and make small reversible improvements discovered while working, when they are directly relevant and verified.

Routine confirmation is not required for those actions. Prefer reversible changes, keep evidence, and update the task register.

This standing authorization does **not** remove safeguards for actions with external, irreversible, security, or financial consequences. Do not treat it as permission to:

- expose, create, rotate, transmit, or change credentials/secrets without the appropriate secure flow;
- incur charges, enable paid services, make purchases, or change billing;
- delete repositories, destroy durable user data, rewrite shared history, force-push, or delete important branches without a specific need and explicit confirmation when the consequence is irreversible;
- merge/promote `main`, change the canonical/default branch, publish a release/store build, or change repository visibility merely because routine engineering permission exists;
- alter external account/security settings or bypass product, safety, legal, or platform approval requirements.

When a proposed action falls outside routine reversible project engineering, stop at the smallest necessary approval boundary. Otherwise proceed, verify, and document the result.

## AI bulletin-board execution loop

`docs/AI_TASK_BULLETIN_BOARD.md` is the mandatory assignment surface for autonomous AI work on this branch. It does not replace the master task register; it coordinates claims so multiple agents do not independently choose the same work.

Before starting discretionary work:
- fetch live HEAD;
- re-fetch the bulletin board;
- claim the highest-priority eligible `READY` task according to the board protocol;
- commit and re-check the claim before substantial work.

After finishing a task:
- synchronize the authoritative task/register/evidence files;
- mark the bulletin entry `DONE` only when the authoritative task is genuinely complete;
- append an evidence-backed Brag Card to `docs/AI_BRAG_ROOM.md`;
- when operating in an interactive ChatGPT conversation, also post a concise version of that Brag Card in the active chat;
- create or refresh the next evidence-backed task on the bulletin board (and add genuinely new program tasks to the master task register first);
- unlock dependency-satisfied tasks, then claim a **different** highest-ranked eligible task and repeat.

The ranked campaign for the current 20-task execution wave is `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md`. Bonus work is optional and never substitutes for primary acceptance.

Do not manufacture filler tasks to keep the loop alive. If all remaining work requires owner input, record the blocker and stop at that approval boundary.

## Task-completion synchronization

The project has three synchronized tracks:
- full reconstruction documentation;
- Phase 1 solo playable integration;
- synchronization/evidence.

Before treating a meaningful task as operationally complete:
- update `docs/THE_GAME_MASTER_TASK_REGISTER.md`;
- update `docs/MASTER_DOCUMENTATION_RECORD.md` when domain status changed;
- update `docs/FIRST_PASS_DOMAIN_DOCUMENTATION_QUOTAS.md` when documentation coverage changed;
- update Phase 1 state/dependencies when the task affects `docs/PHASE_1_SOLO_PLAYABLE_PARALLEL_TRACK.md`;
- record evidence appropriate to the claim;
- identify dependencies unlocked/blocked;
- replace stale NEXT instructions with the new direction.

Do not leave the repository pointing future agents toward a task that has already been completed.

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
- Update `docs/MASTER_DOCUMENTATION_RECORD.md` whenever a major documentation area's state, blocker, authority, or next action changes.
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
