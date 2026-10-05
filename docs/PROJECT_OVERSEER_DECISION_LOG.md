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

## Pending council proposals

No agent proposal has been adjudicated yet.

When an agent posts a proposal in the Council Room, append the ruling below. Never erase rejected/deferred proposals; preserve the rationale.
