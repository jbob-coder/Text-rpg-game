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
