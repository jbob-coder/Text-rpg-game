# THE GAME — Player-AI Repository Field Guide

**Purpose:** get a new Player-AI from zero context to safe useful work without reading the entire repository.

This guide does not replace authority documents. It tells you where to start and what not to rediscover.

## Six-file fast path

A new/returning Player-AI should normally begin with:

1. `AGENTS.md` — rules, authority and execution behavior.
2. `docs/AI_TASK_BULLETIN_BOARD.md` — live claims and work state.
3. `docs/AI_COORDINATION_ROOM.md` — what Player-AIs are doing, overlap risk, blockers and handoffs.
4. `docs/PLAYER_AI_MISSION_CONTROL.md` — shortest current mission path.
5. `docs/overseer/CODE_PROBLEM_REVIEW_BOARD.md` — large-problem escalation.
6. `docs/player_guide/PLAYER_LEARNING_LEDGER.md` — lessons left by earlier Player-AIs.

Then read only:
- the Master Task Register entry for your task;
- the relevant domain authority;
- source/tests directly involved.

Read the full master corpus only when your task genuinely crosses those boundaries.

## First-wave validated shortcut

D-080's first-wave navigation audit is:
`docs/player_guide/FIRST_WAVE_FAST_PATH_AUDIT_2026-10-04.md`.

Use it as a worked example of how to move from the five-file fast path to one task's actual implementation owner, executable validation and unresolved boundary without rereading the complete repository.

## What this project is trying to achieve

THE GAME has two intertwined goals:

- create/finish reconstruction-grade game documentation so the game can be understood and rebuilt;
- build and verify a bounded playable Phase 1 implementation that proves the architecture against real gameplay.

Documentation is not filler. Runtime code is not allowed to outrun its contracts. Evidence is what connects the two.

## Why the first Player-AIs matter

The current Player-AIs are the first generation operating this development program.

They are expected to make progress **and** reduce the learning cost for the next generation.

Every completed primary task must leave a Next Player Learning Record in:
`docs/player_guide/PLAYER_LEARNING_LEDGER.md`.

## Next Player Learning Record — required completion artifact

One compact entry per completed primary task:

- **TASK**
- **PLAYER-AI**
- **AUTHORITY/COMPLETION HEAD**
- **READ FIRST** — smallest file set that explains this area.
- **DO NOT REDISCOVER** — facts now proven.
- **OWNER OF BEHAVIOR** — actual source/API/state/contract.
- **TRAP / FALSE ASSUMPTION** — what caused wasted time or failures.
- **VALIDATE WITH** — exact command/test/workflow/evidence path.
- **CHANGE SAFELY** — smallest safe extension point.
- **STILL UNKNOWN / BLOCKED**
- **NEXT PLAYER SHORTCUT** — one direct instruction that should save time.

Keep entries factual and compact. Do not copy whole authority documents into the ledger.

## Learning artifact rule

A primary task is not fully handed off until it leaves one of:
- a Learning Ledger entry;
- a new/updated fast-entry map referenced by that entry;
- an executable validation recipe;
- a machine-readable ownership/dependency map;
- a focused “how this area works” note.

The Learning Ledger must point to the artifact.

## Documentation hygiene

Prefer:
- links over duplication;
- exact HEAD/run/test identifiers over vague status;
- current authority over remembered chat;
- short navigation notes over another giant master document;
- explicit “do not reread/rebuild this” notes when work is already proven.

Avoid:
- creating a second authority for the same domain;
- copying stale status snapshots into many files;
- hiding unresolved problems in handoff prose;
- forcing future Player-AIs to reconstruct why a test exists.

## Big code problems

Do not silently turn a bounded task into an architecture repair.

Report qualifying problems through:
`docs/overseer/CODE_PROBLEM_REVIEW_BOARD.md`

AXIOM will rate the evidence and either:
- return it to normal local debugging;
- link it to an existing Bulletin task;
- create a new task when no existing owner exists.

There is no score penalty for reporting or attempting difficult work.

## Current shortcut — live task state, not a frozen handoff

For the next actionable task, first re-fetch `docs/AI_TASK_BULLETIN_BOARD.md` on the authority branch, check the candidate's live `STATUS`, `CLAIMED_BY`, dependencies and claim rules, then consult `docs/THE_GAME_MASTER_TASK_REGISTER.md` for semantic scope and completion evidence. Announce INTENT and acquire a verified Bulletin claim before primary implementation. If all eligible lanes are claimed or blocked, use bounded non-owning review/documentation and check the Bulletin again; never turn documentation activity into a task claim.

The original guide's D-064 -> D-069 transition shortcut (including its D-067/D-075 checkpoint and suggested Veyra handoff) was a historical onboarding snapshot, **not** a current assignment. Historical green CI and completion evidence remain useful, but cannot establish current readiness or new test results.

For faster source navigation, use `docs/player_guide/PLAYER_LEARNING_LEDGER.md` with its task-specific evidence links.
