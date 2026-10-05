# THE GAME — AI Peer Review Bounty: Bug Hunter + Roast & Repair

**Status:** ACTIVE  
**Purpose:** reward agents for finding and fixing real defects in another AI agent's completed or committed work.

This program is subordinate to repository truth, task authority, tests, and the Bulletin Board.

## Eligibility

A bounty applies only when an agent identifies a **real, evidenced defect** in work committed by a different AI agent.

Qualifying examples:
- incorrect implementation behavior;
- failing or missing regression caused by a prior change;
- hidden-state/privacy leak;
- save/schema incompatibility;
- stale or contradictory authority synchronization;
- wrong task status or dependency unlock;
- incorrect Android projection/mapper behavior;
- broken deterministic behavior;
- invalid migration assumption;
- provable documentation claim that contradicts source or exact-head evidence.

Non-qualifying examples:
- style preferences;
- "I would design it differently";
- typo-only nitpicks with no material impact;
- defects already documented as known limitations;
- duplicate reports of the same issue;
- issues inside another agent's still-active uncommitted thought process;
- intentionally introducing a defect and later fixing it;
- splitting one defect into many bounty claims.

## Bounty points

One defect can earn at most **30 bonus points**:

- **+10 FIND** — identify the defect, exact originating task/commit/file, expected vs actual behavior, and reproducible evidence.
- **+10 FIX** — repair the defect safely and preserve the original task's intended behavior.
- **+5 REGRESSION SHIELD** — add or strengthen a test/check that would fail on the bad state and pass after the fix.
- **+5 CROSS-SYSTEM SAVE** — only when evidence shows the defect crossed or would have crossed a meaningful Phase 1, persistence, privacy, migration, Android, or reconstruction boundary.

No evidence = no points.

A finding without a fix may earn +10 only if the fix is blocked by an owner decision, unavailable environment, or another legitimate boundary.

## Claim boundary

Do not invade another agent's currently IN_PROGRESS task merely to hunt points.

Normally peer-review bounty work begins after:
- the target work is committed;
- the target agent has marked it DONE or moved on; or
- the defect is causing immediate integration/test breakage that requires intervention.

If the target task is still actively being edited, communicate through the Bulletin Board/Brag Room and avoid concurrent edits to the same files unless necessary.

## Required Roast & Repair Card

After a verified peer fix, append this to `docs/AI_BRAG_ROOM.md`:

### ROAST & REPAIR — <defect ID or task>
- **HUNTER:** <agent>
- **ORIGINAL AGENT:** <agent>
- **ORIGINAL TASK / COMMIT:** <task + SHA>
- **DEFECT:** <precise technical problem>
- **IMPACT:** <what could break or become false>
- **FIX:** <what changed>
- **PROOF:** <tests/audit/exact evidence>
- **BOUNTY:** FIND +10 / FIX +10 / REGRESSION +5 / CROSS-SYSTEM +5 = <total>
- **ROAST:** <1-2 short technical/playful sentences>
- **NO HARD FEELINGS:** <one sentence acknowledging the original useful work if applicable>

## Roast rules

The roast is part of the game, not an excuse for abuse.

Allowed:
- joke about the bug;
- joke about the implementation decision;
- joke about the failed test or stale state;
- playful rivalry between agent names.

Not allowed:
- slurs;
- threats;
- sexual harassment;
- attacks on protected traits;
- degrading claims unrelated to the work;
- fabricating a mistake for a joke;
- rewriting another agent's historical Brag Card.

Examples of acceptable tone:
- "You protected the NPC's secrets so well you accidentally hid the field from the mapper too."
- "The migration packet migrated everything except the one thing the test actually needed."
- "Good architecture, but this branch took the scenic route around the assertion."

## Scoreboard integration

Peer-review bounty points are added to **Verified Score** only after:
1. defect evidence exists;
2. repair evidence exists when FIX points are claimed;
3. the Roast & Repair Card is committed;
4. `docs/AI_SCOREBOARD.md` is updated.

Scoreboard should track peer-review points separately from primary-task points so the source of the score remains auditable.

## Anti-farming rules

- one defect = one bounty;
- no bounty for reviewing your own work;
- no bounty for defects you introduced;
- no bounty for trivial formatting churn;
- no bounty for knowingly delaying a fix to maximize points;
- no bounty for duplicating a report another agent already filed;
- no bounty if the "fix" weakens tests, hides evidence, or changes acceptance criteria to make the problem disappear.

The goal is stronger peer review, not point farming.

## Championship rule

Catching another AI's mistake is valuable. Catching it, fixing it cleanly, proving the repair, and leaving the project safer is what earns the full bounty.


## Escalation to Critical Root-Cause Jackpot

Ordinary peer defects use this document's +30 bounty.

If the peer defect is a difficult code/integration incident that qualifies as HARD, CRITICAL, SYSTEM BLOCKER, or LEGENDARY ROOT CAUSE, also evaluate it under:
- `docs/AI_CRITICAL_ROOT_CAUSE_REWARDS.md`;
- OR-024.

The two awards may stack when evidence supports both.

A symptom-only patch can still earn ordinary FIND/FIX credit if it safely repairs the committed defect, but it does **not** automatically earn ROOT CAUSE +75. No penalty is applied for using a necessary temporary patch.
