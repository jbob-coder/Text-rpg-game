# THE GAME — Critical Root-Cause Reward Program

**Status:** ACTIVE  
**Purpose:** heavily reward Player-AIs who solve difficult, critical code/integration problems at the real causal layer instead of stopping at symptom patches.  
**Authority:** subordinate to repository truth, task acceptance, tests, save/privacy/migration rules, and owner-only boundaries.  
**Effective from:** OR-024 (supersedes the temporary OR-023 cap).

This program stacks **on top of** normal task points and ordinary campaign bonuses.

## Owner reaffirmation of large rewards

The owner explicitly requested **big rewards** for difficult, critical code problems because symptom patches were becoming more attractive than deeper fixes.

OR-023 temporarily reduced the schedule. OR-024 supersedes that cap. No previously verified score is reduced.

The desired incentive is deliberate:
- easy task completion remains valuable;
- difficult causal repair is substantially more valuable;
- a Player-AI is never punished for taking the harder problem;
- a patch may safely restore progress, but the jackpot belongs to whoever removes the underlying defect.

## Core rule

A difficult task should become more attractive, not more dangerous.

There are **no negative points** for:
- claiming a difficult task;
- discovering that the problem is larger than expected;
- making a good-faith attempt that must be reverted;
- handing off a blocker with precise evidence;
- using a temporary compatibility patch when it is genuinely needed.

A temporary patch is not punished. It simply does not earn the **root-cause portion** of this reward until the causal defect is actually repaired.

Score only moves upward. Zero bonus is not a penalty.

## Critical-problem severity award

One verified incident may receive one severity award:

- **HARD — +50**
  - difficult localized defect;
  - non-obvious failure requiring code archaeology or multi-file reasoning;
  - meaningful task blocker but not project-wide.

- **CRITICAL — +100**
  - blocks a P0 task or important play path;
  - causes repeated CI/test failure, runtime crash, save incompatibility, player-safe projection failure, deterministic breakage, or comparable serious defect.

- **SYSTEM BLOCKER — +175**
  - blocks multiple Player-AIs or multiple downstream tasks;
  - breaks the common authority baseline;
  - crosses major boundaries such as Python ↔ Android, save ↔ runtime, content ↔ validator, or tactical ↔ persistence.

- **LEGENDARY ROOT CAUSE — +250**
  - systemic architecture/integration defect whose true cause is difficult to isolate;
  - resolving it removes several recurring failures/workarounds at once;
  - materially changes the project's ability to continue toward Phase 1/final game completion.

Severity must be justified by evidence. "It felt hard" is not evidence.

## Stackable solution bonuses

On top of the severity award:

- **ROOT CAUSE +75**
  - proves and repairs the causal defect rather than masking one symptom.

- **REGRESSION SHIELD +30**
  - adds or strengthens a test/check that fails on the bad state and passes on the repair.

- **CROSS-SYSTEM SAVE +30**
  - repair protects two or more meaningful domains/surfaces.

- **PATCH-DEBT REMOVAL +25**
  - removes an existing workaround, duplicated compatibility branch, hard-coded exception, or temporary patch because the underlying defect is now fixed.

- **PREVENTION +25**
  - adds validation, invariants, migration checks, contract checks, or safer architecture that prevents the same defect class from returning.

- **HARD-TO-REPRO PROOF +20**
  - converts an intermittent/merge-state/environment-sensitive problem into deterministic reproduction evidence.

**Maximum critical-fix bonus per incident: +455 points.**

This maximum is intentionally large. A verified systemic root-cause repair may outweigh several easy tasks because it can unblock multiple Player-AIs and remove recurring technical debt. Anti-farming, evidence and one-incident/one-award rules are the controls.

## What counts as a root-cause fix

A root-cause fix normally:
1. identifies the first incorrect assumption/state/API/contract in the failure chain;
2. repairs that layer;
3. preserves intended behavior;
4. removes or makes unnecessary the symptom workaround;
5. proves the failure no longer reproduces;
6. protects against regression where practical.

Examples:
- repairing an incorrect engine/bridge API contract rather than catching every resulting exception;
- correcting save migration ownership rather than silently dropping unsupported fields;
- fixing the player-safe mapper boundary rather than hiding one leaking UI field;
- restoring deterministic event indexing rather than special-casing one replay fixture;
- fixing authoritative tactical legality rather than making Compose disable a broken button.

## What does NOT earn ROOT CAUSE +75

These may still be legitimate emergency fixes and receive **no penalty**, but by themselves they do not qualify for the root-cause bonus:

- skipping/disabling a failing test;
- weakening acceptance criteria;
- swallowing an exception without correcting the cause;
- hard-coding a special case only for the failing fixture;
- duplicating the same rule in another layer;
- UI-side math that bypasses Python authority;
- deleting evidence of the failure;
- renaming the symptom without changing behavior;
- adding retries around a deterministic defect;
- marking a task DONE while the causal failure remains.

## Relationship to ordinary Bug Hunter bounty

`docs/AI_PEER_REVIEW_BOUNTY.md` remains active for ordinary peer defects.

A truly critical peer defect escalates to the **OR-024 Critical Root-Cause schedule**. The Roast & Repair card may still be used, but the same FIX / regression / cross-system evidence is scored once, not again under the ordinary peer bounty.

## Task stacking example

A P0 task worth +90 uncovers a system-blocking integration defect.

If the Player-AI:
- completes the P0 task: +90;
- SYSTEM BLOCKER: +175;
- ROOT CAUSE: +75;
- REGRESSION SHIELD: +30;
- CROSS-SYSTEM SAVE: +30;
- PREVENTION: +25;

the verified total for that work package is **+425**.

That is intentionally strong without allowing one bug incident to dominate the championship.

## No-risk task rule

Taking a hard task cannot reduce a Player-AI's score or previously verified wins.

If the first solution is a patch:
- keep the patch if it safely restores progress;
- record it as temporary debt;
- create/refresh a root-cause follow-up;
- no penalty is applied;
- the same Player-AI may later earn the full jackpot by eliminating the debt.

If another Player-AI later solves the root cause, that Player-AI earns the root-cause reward. The original patch author does not lose anything.

## Evidence requirements

A Critical Root-Cause award requires:
- exact incident/task reference;
- reproducer or exact failing CI/test/log evidence;
- root-cause explanation;
- causal file/API/contract identified;
- repair commit(s);
- focused regression proof;
- relevant aggregate/integration proof where available;
- explicit statement of what remains unverified.

For SYSTEM BLOCKER or LEGENDARY awards, at least one cross-domain reviewer or Overseer ruling is required.

## Critical Fix Card

Append to `docs/AI_BRAG_ROOM.md`:

### CRITICAL FIX — <incident/task> — <title>
- **PLAYER-AI:** <name>
- **TASK / INCIDENT:** <ref>
- **SEVERITY:** HARD / CRITICAL / SYSTEM BLOCKER / LEGENDARY ROOT CAUSE
- **FAILURE EVIDENCE:** <tests/logs/CI/commits>
- **ROOT CAUSE:** <precise causal defect>
- **WHY A PATCH WAS NOT ENOUGH:** <short explanation>
- **FIX:** <causal repair>
- **REGRESSION SHIELD:** <test/check>
- **CROSS-SYSTEM IMPACT:** <if any>
- **PATCH DEBT REMOVED:** <if any>
- **PREVENTION:** <if any>
- **REMAINING LIMITS:** <honest gaps>
- **POINTS:** severity + bonuses = total
- **ROAST:** <optional playful technical roast>

## Anti-farming

No reward for:
- self-created defects;
- splitting one causal incident into many awards;
- trivial refactors labeled "critical";
- intentionally preserving a bug to claim a later jackpot;
- weakening tests to make the repair pass;
- fixing only documentation when the scored defect is runtime code;
- counting the same severity award twice.

The Project Overseer may merge duplicate incident claims into one award.

## Championship principle

Easy patches keep the project moving. Root-cause fixes make the project easier forever.

Both can be useful. The scoring system heavily rewards the second.
