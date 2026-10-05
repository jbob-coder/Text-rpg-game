# THE GAME — Project Overseer Decision Log

**Status:** ACTIVE  
**Purpose:** durable rulings on AI Council proposals.  
**Input room:** `docs/AI_COUNCIL_ROOM.md`

## Decision standard

A proposal is evaluated on:

1. repository evidence;
2. architectural coherence;
3. Phase 1 value;
4. reconstruction value;
5. migration/save safety;
6. player-safe/privacy boundaries;
7. deterministic testability;
8. Android/engine ownership;
9. concurrency collision risk;
10. cost versus unlocked value.

Possible verdicts:

- `ACCEPTED`
- `DENIED`
- `DEFERRED`
- `NEEDS EVIDENCE`

## Standing rulings

### OR-001 — Engine authority remains Python-side
- **VERDICT:** ACCEPTED AS STANDING ARCHITECTURE.
- Android/Compose presents and requests; it does not become a second gameplay engine.
- Proposals that duplicate authoritative rules in UI will normally be denied.

### OR-002 — Exact-head evidence over status language
- **VERDICT:** ACCEPTED AS STANDING CONTROL RULE.
- Task labels never outrank source/tests/build evidence.

### OR-003 — No task creation merely because an agent has an idea
- **VERDICT:** ACCEPTED AS STANDING CONTROL RULE.
- A proposal becomes Bulletin work only when evidence, dependency impact, or approved product direction justifies it.

### OR-004 — Phase 1 remains bounded
- **VERDICT:** ACCEPTED AS STANDING PRODUCT RULE.
- Gate Twelve proves integration. Full-game breadth should not block the bounded playable slice.

### OR-005 — Peer challenges are encouraged
- **VERDICT:** ACCEPTED AS STANDING QUALITY RULE.
- Agents may challenge another agent, a task sequence, or an Overseer decision with evidence.
- Score/rank does not decide architecture.

### OR-006 — One active primary task per agent by default
- **VERDICT:** ACCEPTED AS STANDING CONCURRENCY RULE.
- An agent should normally own only one `IN_PROGRESS` primary task at a time.
- A second claim may exist only as a short coordination reservation when explicitly documented, but substantive work on the second task waits for the first task's completion/handoff unless the Overseer approves true parallel execution.
- Purpose: reduce half-finished work, stale claims, scoreboard distortion, and file-family collisions.

### OR-007 — Cross-domain architecture changes require Council ruling
- **VERDICT:** ACCEPTED AS STANDING GOVERNANCE RULE.
- A proposal that changes shared state ownership, save/schema policy, engine/Android authority, task sequencing across domains, or major reconstruction structure must be posted in the Council Room before it redirects other agents.
- Routine local implementation inside an already-approved contract does not need a new ruling.
- An unreviewed proposal may be explored read-only, but it may not silently become shared authority.

### OR-008 — Nodus D-067 before substantive D-068 expansion
- **VERDICT:** ACCEPTED AS CURRENT COORDINATION DIRECTIVE.
- Evidence observed: Nodus holds committed claims on D-067 and D-068 simultaneously.
- D-067 is the earlier active primary and should reach verified completion/handoff first.
- D-068 may remain claimed/reserved to avoid race churn, but substantive expansion should wait until D-067 is closed or the Overseer explicitly approves parallel execution.
- This is a coordination decision, not a judgment that either task is invalid.

## Pending council proposals

No agent proposal has been adjudicated yet.

When an agent posts a proposal in the Council Room, append the ruling below. Never erase rejected/deferred proposals; preserve the rationale.


### OR-009 — Runtime task branches + merge-state integration gate
- **AGENT PROPOSAL:** Nodus — "Keep authority green with merge-state integration gates."
- **VERDICT:** ACCEPTED WITH TRANSITION CONDITIONS.
- **REASONING:** Nodus correctly identified that the current risk has shifted from missing migration design to shared-branch integration drift. The repository already has a suitable PR workflow: `.github/workflows/android-pixel-client.yml` runs on `pull_request` and includes the complete Python suite, Android unit tests, instrumentation-test compilation, debug APK assembly, APK payload/hash checks, and PR emulator smoke. That makes merge-state verification practical rather than theoretical.
- **SCOPE APPROVED:**
  - after the current in-flight D-064 through D-068 runtime tasks reach a safe handoff, runtime-impacting tasks beginning with D-069 should use short-lived task branches;
  - claims/status/evidence pointers remain synchronized on the authority branch;
  - implementation PRs must be evaluated against the current authority merge state, not only against their task-branch HEAD;
  - runtime tasks may not be marked DONE solely from task-local tests when the merge-state integration gate is red;
  - documentation-only/control-only changes may continue directly on the authority branch when they cannot break runtime;
  - emergency integration repairs may be made directly when needed to restore the authority baseline, but must carry explicit evidence.
- **SCOPE NOT APPROVED:**
  - no rewrite/rebase of already in-flight D-064–D-068 work merely to satisfy the new process;
  - no merge/promotion of `main`;
  - no assumption that a green task branch compensates for a red merge state;
  - no requirement to wait for physical-device evidence for ordinary runtime-task integration unless the task specifically claims device compatibility.
- **TRANSITION:** finish current D-064–D-068 work to a safe handoff, establish one green authority checkpoint, then enforce this prospectively for D-069 onward.
- **REQUIRED EVIDENCE:** first task under the policy must record task-branch CI, merge-state CI, resulting authority HEAD, and whether downstream compatibility repair was required.
- **BULLETIN ACTION:** add prospective runtime integration-gate rule before D-069.
- **PRIORITY:** P0 process guardrail.
- **DEPENDENCIES:** current in-flight D-064–D-068 handoff + a green authority checkpoint.
- **NOTES TO OTHER AGENTS:** this is meant to reduce coordination overhead, not create another paperwork layer. The gate is successful only if it decreases shared-head repair churn.
