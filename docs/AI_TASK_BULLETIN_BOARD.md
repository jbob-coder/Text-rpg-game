# AI Task Bulletin Board — THE GAME

**Status:** ACTIVE  
**Repository:** `jbob-coder/Text-rpg-game`  
**Authority branch:** `docs/master-game-development-program`  
**Purpose:** repository-native work queue for AI agents.

This board controls **agent task claiming and handoff**, not program semantics.  
`docs/THE_GAME_MASTER_TASK_REGISTER.md` remains the authority for task scope, priority, dependencies, evidence, and completion state.

## Mandatory agent loop

Every AI agent that connects to this repository must use this loop before starting discretionary project work:

1. Read `AGENTS.md`.
2. Read this bulletin board.
3. Fetch the live HEAD of `docs/master-game-development-program`.
4. Re-fetch this board immediately before claiming a task.
5. Select the highest-priority task whose status is `READY`, whose dependencies are satisfied, and whose owner boundary does not block autonomous work.
6. Claim it by changing only that task's bulletin entry to:
   - `IN_PROGRESS`
   - `CLAIMED_BY: <agent/session identifier>`
   - `CLAIMED_AT: <timestamp or NOT_RECORDED>`
   - `CLAIM_HEAD: <exact commit SHA>`
7. Commit the claim before doing substantial work.
8. Re-fetch the board after the claim commit. If another agent won the claim or the entry changed incompatibly, do **not** work that task; choose a different eligible task.
9. Execute the task from live repository evidence. Follow the task register, relevant authorities, source, tests, and migration contracts.
10. Before declaring completion:
    - run the verification required by the task;
    - update the master task register and every affected authority;
    - record exact evidence and exact HEAD where applicable.
11. Mark the bulletin entry `DONE` only when the authoritative task is genuinely complete. Record:
    - completion HEAD;
    - files changed;
    - tests/verification actually executed;
    - unresolved evidence or owner decisions.
12. **Before taking another task, create or publish the next evidence-backed task on this board.**
    - If the next task already exists in `THE_GAME_MASTER_TASK_REGISTER.md`, add/refresh its bulletin entry.
    - If a genuinely new program task is required, add it to the master task register first, then add the same task reference here.
    - The new task must come from an observed dependency, gap, failing test, migration need, reconstruction gap, or explicit program direction.
    - Do not manufacture filler work merely to keep the loop running.
13. After publishing the next task, claim a **different eligible task** and repeat the loop.

## Concurrency rules

- One bulletin task may have only one active claimant.
- Re-fetch this file immediately before every claim or completion write.
- Never overwrite a newer claim.
- Do not use a stale blob SHA for updates.
- If two agents race for the same task, the first committed valid claim wins.
- A losing agent must select another `READY` task.
- Agents may inspect the same repository state in parallel, but shared authority files must be reconciled rather than blindly overwritten.
- If live HEAD changes during work, inspect the drift before finalizing.
- If another agent already completed the intended task, audit it instead of duplicating it, then publish/claim the next real task.

## Status vocabulary

- `READY` — eligible to claim now.
- `IN_PROGRESS` — actively claimed by one agent.
- `BLOCKED` — cannot proceed until the recorded dependency/owner decision is resolved.
- `DONE` — authoritative task completed and synchronized.
- `SUPERSEDED` — replaced by a newer task or authority; include the replacement reference.

## Task creation standard

Every new bulletin task must contain:

- `TASK_REF` — normally the matching `D-xxx` master-register task.
- `TITLE`
- `PRIORITY`
- `STATUS`
- `SOURCE_OF_WORK` — exact evidence that created the task.
- `DEPENDENCIES`
- `ACCEPTANCE` — observable completion conditions.
- `CLAIMED_BY`
- `CLAIMED_AT`
- `CLAIM_HEAD`
- `COMPLETION_HEAD`
- `EVIDENCE`
- `NEXT_TASK_CREATED`

A task is not valid merely because an agent thinks it would be interesting.

## Current queue

### D-060 — Execute fresh corpus inventory and second-pass quota recalibration

- **TASK_REF:** `D-060`
- **TITLE:** Execute fresh corpus inventory and second-pass quota recalibration
- **PRIORITY:** `P0`
- **STATUS:** `READY`
- **SOURCE_OF_WORK:** `docs/THE_GAME_MASTER_TASK_REGISTER.md` records D-060 as the live next program-control action after D-058/D-059 first-pass closure.
- **DEPENDENCIES:** D-058 `DONE`; D-059 `DONE`.
- **ACCEPTANCE:**
  1. inventory measures an immutable Git revision rather than arbitrary working-tree contents;
  2. untracked files cannot alter the measured revision's totals;
  3. uncommitted edits cannot alter the measured revision's blob/content totals;
  4. different committed revisions produce appropriately different inventories;
  5. output records the exact measured revision;
  6. regression tests protect these boundaries;
  7. fresh inventory evidence is recorded;
  8. D-058 counting is checked against the exact-revision inventory without blindly redoing D-058;
  9. second-pass/depth backlog and Phase 1 dependency impact are ranked from evidence;
  10. affected master/control records are synchronized.
- **KNOWN CHECKPOINT:** previous live HEAD observed at bulletin creation: `0648fb8e081bd9bef5f71fcacef591e62afef82b`. This is historical context only; claimant must fetch live HEAD.
- **KNOWN PRIOR EVIDENCE:** a prior interrupted execution reported 316 Python tests passing and raster verification 24/24, but those results must remain tied to the revision on which they were actually executed and must not be relabeled as proof for a newer HEAD.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **NEXT_TASK_CREATED:** no

## Queue maintenance rule

There should normally be at least one evidence-backed `READY` task whenever safe autonomous project work remains.

If the queue becomes empty:

1. inspect the master task register;
2. inspect Phase 1 unmet requirements;
3. inspect unresolved migration/test/evidence gaps;
4. publish the single strongest safe next task;
5. then claim it.

If all remaining work requires an owner decision, do not invent a replacement task. Mark the relevant entries `BLOCKED`, record the exact owner decision required, and stop at that boundary.
