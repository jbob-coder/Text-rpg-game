# AGENTS.md — Text RPG Game

This file is the repository entry point for coding agents and automated assistants.

## Read first

**Priority repository:** `jbob-coder/Text-rpg-game`.

Before changing code or documentation, read these in order:

1. `docs/AI_TASK_BULLETIN_BOARD.md` — mandatory live work queue and claim authority.
2. `docs/AI_COORDINATION_ROOM.md` — Player-AI work announcements, overlap checks, help/blocker and finish/next handoffs.
3. `docs/AI_COMMAND_STRUCTURE.md` — Player-AI specializations, review responsibilities and escalation paths.
4. `docs/PLAYER_AI_MISSION_CONTROL.md` — fast-entry mission cards.
5. `docs/overseer/CODE_PROBLEM_REVIEW_BOARD.md` — mandatory escalation for large code/integration problems.
6. `docs/player_guide/README.md` — repository-learning/navigation path.
7. `docs/player_guide/PLAYER_LEARNING_LEDGER.md` — lessons left by completed work.
8. `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md` — top-level program authority.
9. `docs/MASTER_DOCUMENTATION_RECORD.md` — canonical documentation state/blockers.
10. `docs/FINAL_GAME_RECONSTRUCTION_BLUEPRINT.md` — integration/reconstruction blueprint.
11. `docs/MASTER_DIRECTIVE_EXECUTION_BREAKDOWN.md` — ordered execution phases.
12. `docs/DOCUMENTATION_CROSS_REFERENCE_MATRIX.md` — document ownership/consumers.
13. `docs/THE_GAME_MASTER_TASK_REGISTER.md` — semantic task scope/state/evidence.
14. `docs/IMPLEMENTATION_STATUS.md` — verified implementation evidence.
15. Relevant domain master document.
16. Relevant source/tests.
17. `docs/V6_STABILIZATION_HANDOFF.md` only when exact historical V6 evidence is needed.

Coordination room: `docs/AI_COORDINATION_ROOM.md`.  
Overseer area: `docs/overseer/README.md` (AXIOM).  
Large code-problem intake: `docs/overseer/CODE_PROBLEM_REVIEW_BOARD.md`.  
Player learning/navigation: `docs/player_guide/README.md` + `docs/player_guide/PLAYER_LEARNING_LEDGER.md`.  
Peer defect bounties: `docs/AI_PEER_REVIEW_BOUNTY.md`.  
Council/rulings: `docs/AI_COUNCIL_ROOM.md` + `docs/PROJECT_OVERSEER_DECISION_LOG.md`.  
Post-transition runtime integration: `docs/AI_RUNTIME_MERGE_STATE_GATE.md`.

Repository files and fresh execution evidence outrank remembered chat context. Older game repositories, prototypes and historical reports are not authority unless an explicit migration record says otherwise.

## Current working baseline

- Repository: `jbob-coder/Text-rpg-game`.
- Program authority branch: `docs/master-game-development-program`.
- Current mode: **bounded Phase 1 implementation + exact-head verification**, using reconstruction-grade contracts as guardrails.
- Gate Twelve is the first proof region. D-065/D-067/D-068 are DONE and the green authority checkpoint is PASS; D-064 is the sole remaining gate before D-069 tactical core.
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

## Player-AI ♾️ fast-entry mode

When the user sends `♾️` to a Player-AI:
- fetch live HEAD;
- open `docs/PLAYER_AI_MISSION_CONTROL.md`;
- re-fetch the Player-AI's current Bulletin task;
- perform the mission card's **Next Move**;
- verify its **Exit Gate**;
- synchronize task/evidence/Brag/Scoreboard state.

Do not restart repository-wide discovery unless the mission card or live drift requires it.

## Mandatory large-problem report

AXIOM is the Project Overseer identifier for repository problem triage.

A Player-AI must create/update a `CPR-###` evidence packet and submit it through `docs/overseer/CODE_PROBLEM_REVIEW_BOARD.md` when a code/integration problem:
- blocks P0 work or multiple downstream tasks;
- crosses major authority boundaries;
- repeatedly breaks CI/runtime/save/projection/determinism;
- appears architectural or merge-state dependent;
- would require a temporary patch because the causal fix is unclear;
- may qualify for a large root-cause reward.

Report exact HEAD, executed evidence, reproduction, affected files/APIs/domains, what is blocked and what remains unverified.

Do not create a duplicate Bulletin task yourself when an existing task may already own the cause. AXIOM reviews the evidence, rates the problem, then links or creates the task.

Reporting a difficult defect has no score penalty and does not surrender task ownership.

## Next Player Learning Record — primary completion requirement

The first Player-AIs are also responsible for making this repository easier for later Player-AIs to learn.

Before a primary task is fully handed off, append one compact record to:
`docs/player_guide/PLAYER_LEARNING_LEDGER.md`.

The record must identify:
- smallest Read First set;
- proven facts the next agent should not rediscover;
- actual behavior owner (source/API/state/contract);
- one trap or false assumption;
- exact validation command/test/evidence;
- safest extension point;
- unresolved boundary;
- one direct Next Player Shortcut.

A primary task may have passing tests and still be missing its handoff requirement if this learning record is absent.

Do not create documentation bloat: link to existing authorities and evidence instead of copying them.

## Merge-candidate hygiene

Green CI is necessary but not sufficient for a bounded merge candidate.

Before final handoff of a scoped task:
- compare the candidate against live authority;
- verify every changed production file is required by the task/accepted CPR;
- remove unrelated formatting, compaction, comment deletion and refactor churn;
- preserve live-authority behavior outside the accepted semantic delta;
- keep RED/evidence-only PRs separate from the final merge candidate;
- if the final branch content differs materially from previously green evidence, rerun the required merge-state gate.

A broad diff cannot become acceptable merely because tests are green.

For surgical fixes, prefer a small auditable semantic delta over transplanting an older green branch wholesale.

## Critical problem handling

Authority: `docs/AI_CRITICAL_ROOT_CAUSE_REWARDS.md` and OR-024.

When a Player-AI encounters a serious code/integration defect:

1. reproduce and identify the causal layer before broad edits;
2. if an emergency workaround is required, label it `TEMPORARY_PATCH`;
3. record `ROOT_CAUSE_FOLLOWUP` when causal debt remains;
4. never weaken tests or acceptance criteria to make the symptom disappear;
5. prefer repairing the authoritative layer over duplicating rules in presentation/compatibility layers;
6. add regression protection when practical;
7. classify any jackpot claim with exact evidence.

There are **no score penalties** for claiming or attempting hard tasks. Score never decreases because a difficult fix needed a revert or handoff. A temporary patch is permitted; it simply does not earn the ROOT CAUSE portion until the underlying defect is solved.

## AI bulletin-board + coordination execution loop

The Bulletin owns task claims. The Coordination Room owns situational awareness.

Before a new primary:
- fetch live HEAD;
- re-fetch Bulletin + Coordination Room;
- append `INTENT` with candidate task, likely files/domains and overlap risk;
- claim through the Bulletin; INTENT does not reserve work;
- re-fetch the claim;
- if you won, append `START` with claim head, branch/PR, scope, exit gate and reviewer/help request;
- if you lost, append `INTENT WITHDRAWN` or `PIVOT` and choose another eligible task.

During work:
- post only meaningful `UPDATE`, `HELP`, `BLOCKED` or `REVIEW REQUEST` messages;
- coordinate before modifying overlapping authoritative file families;
- large code problems go through AXIOM CPR evidence/rating, not only chat.

After finishing:
- synchronize authoritative task/register/evidence files;
- mark Bulletin DONE only when acceptance is real;
- append Brag Card and update Scoreboard when applicable;
- write the required Next Player Learning Record;
- refresh Mission Control when downstream next moves change;
- append `FINISH` to the Coordination Room with completion head, evidence, changed areas, limits and unlocks;
- append `NEXT` naming the next candidate task;
- choose the highest-value eligible READY task that avoids dependency/file collisions, or briefly justify a lower-ranked choice;
- create new tasks only from genuine evidence-backed work;
- return to INTENT -> CLAIM -> START.

Do not manufacture filler work. If no eligible work exists and owner input is required, record the blocker and stop at that boundary.

### Runtime merge-state gate

Project Overseer ruling OR-009 introduces a prospective integration rule after the current D-064–D-068 transition checkpoint.

Once one green authority checkpoint is established:
- runtime-impacting tasks should use short-lived task branches;
- open/update a PR targeting `docs/master-game-development-program`;
- use the repository's existing pull-request CI as merge-state evidence;
- task-local green is not enough when the merge-state is red;
- do not mark a runtime task DONE until its required merge-state integration gate is green;
- documentation/control-only changes may still write directly to the authority branch;
- emergency direct runtime repairs require explicit evidence and rationale.

D-069 is the first intended task to prove this policy after the transition gate. See `docs/AI_RUNTIME_MERGE_STATE_GATE.md`.

## Player-AI specialization responsibilities

Current Player-AI specialization authority is defined in `docs/AI_COMMAND_STRUCTURE.md`.

- **Nodus:** Player-AI — Integration Architect & Systems Gatekeeper.
- **Veyra:** Player-AI — Gameplay Systems & Tactical Lead.
- **Kestrel:** Player-AI — Player-Safe Projection, Presentation & Asset Lead.
- **Veyr:** Player-AI — NPC, Social & Narrative-State Lead.
- **Fifth Player-AI Seat:** Verification, Red-Team & Performance Lead once filled.

These are Player-AI classes/specializations and accountability/review lanes, not corporate ranks or permanent file ownership.

Before completing cross-domain work, request/reconcile the relevant lead review when practical:
- save/schema/integration -> Nodus;
- gameplay/tactical rules -> Veyra;
- player-safe projection/presentation/assets -> Kestrel;
- NPC/social/privacy -> Veyr;
- final regression/performance/evidence -> Fifth Agent seat once filled.

If lead advice conflicts with task authority or another domain lead, escalate to the Council/Project Overseer rather than silently choosing one interpretation.

## Council and architecture challenges

Agents are allowed to challenge the current plan.

Use `docs/AI_COUNCIL_ROOM.md` when:
- the Project Overseer calls you by name;
- you believe the task order is wrong;
- you see a systemic architecture problem;
- you think an existing contract should be replaced or simplified;
- you need a ruling that affects multiple domains.

Submit evidence, cost/risk and one concrete change. Do not silently redirect the project.

The Project Overseer records the durable verdict in `docs/PROJECT_OVERSEER_DECISION_LOG.md` as `ACCEPTED`, `DENIED`, `DEFERRED`, or `NEEDS EVIDENCE`.

An agent may challenge a verdict later with new evidence. Score/rank never decides architecture.

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
