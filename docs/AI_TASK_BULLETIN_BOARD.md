# AI Task Bulletin Board — THE GAME

**Status:** ACTIVE  
**Repository:** `jbob-coder/Text-rpg-game`  
**Authority branch:** `docs/master-game-development-program`  
**Campaign:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md`  
**Brag room:** `docs/AI_BRAG_ROOM.md`  
**Purpose:** repository-native work queue, claim coordination, completion handoff and continuous AI work loop.

This board controls **task claiming and handoff**, not program semantics.  
`docs/THE_GAME_MASTER_TASK_REGISTER.md` remains the semantic authority for task scope/state. The campaign document owns the detailed rank, execution description, bonus and acceptance intent for D-060 through D-079.

## Mandatory agent loop

Every AI agent that connects to this repository must:

1. Read `AGENTS.md`, this board, the master task register and the relevant task/domain authorities.
2. Fetch live HEAD.
3. Re-fetch this board immediately before claiming.
4. Select the **highest-ranked READY task** whose dependencies are actually satisfied.
5. Claim it by setting `IN_PROGRESS`, `CLAIMED_BY`, `CLAIMED_AT`, and `CLAIM_HEAD`.
6. Commit the claim before substantial work and re-fetch the board. First valid committed claim wins.
7. Execute from live evidence. Do not invent implementation, test results, canon or device evidence.
8. Before completion, run required verification and synchronize affected authoritative records.
9. Mark the task `DONE` only when its acceptance criteria are genuinely met. Record completion HEAD and evidence.
10. Append a **Brag Card** to `docs/AI_BRAG_ROOM.md` before claiming another primary task.
11. If operating in an interactive ChatGPT conversation, also post a concise Brag Card in that active chat. Repository Brag Room remains canonical when chat posting is unavailable.
12. Re-evaluate blocked dependents and change them to `READY` only when every dependency is satisfied.
13. **Create or refresh the next evidence-backed task before moving on.**
    - If the ranked next task already exists, revalidate its source/dependencies/acceptance against the new HEAD and mark `NEXT_TASK_CREATED_OR_REFRESHED: yes`.
    - If completed work reveals a genuinely new required task, register it in `THE_GAME_MASTER_TASK_REGISTER.md` first, then add it to this board after D-079 or as a clearly justified repair task.
    - Never manufacture filler work.
14. Claim a **different** highest-ranked eligible task and repeat.

## Concurrency rules

- One primary task has one active claimant.
- Re-fetch this file immediately before claim, completion, unlock or queue edits.
- Never overwrite a newer claim or use a stale blob SHA.
- If another agent wins a claim, choose another READY task.
- If live HEAD moves, inspect drift before finalizing.
- Shared authority writes must be reconciled, not blindly overwritten.
- Multiple agents may work concurrently only on distinct dependency-safe tasks.
- A lower-ranked task may be taken before a higher-ranked one only when the higher-ranked task is not READY; record the reason.

## Status vocabulary

- `READY` — dependency-safe and eligible to claim.
- `IN_PROGRESS` — actively claimed.
- `BLOCKED` — waiting on a dependency or owner boundary.
- `DONE` — authoritative task complete and synchronized.
- `SUPERSEDED` — replaced by a newer task/authority; include replacement.

## Bonus rule

Every campaign primary task has one related bonus.
- Bonus unlocks only after its parent primary task is DONE.
- Bonus is optional and worth visibility/brag credit only.
- Bonus never substitutes for primary acceptance.
- Do not perform a bonus if a higher-ranked P0/P0-CRITICAL primary task is READY and the bonus would delay it.
- Record completed bonus evidence in `docs/AI_BRAG_ROOM.md`.

## Brag-before-next rule

A completed task is not considered fully handed off until its Brag Card exists.

The card must state:
- agent/session;
- claim HEAD and completion HEAD;
- what shipped;
- bugs/gaps resolved;
- tests/builds/audits actually observed;
- key files/artifacts;
- Phase 1/program impact;
- bonus result;
- unverified/blockers;
- next AI unlock/challenge.

Bragging is encouraged; fabrication is forbidden.

## Ranked queue — 20 primary tasks

### Rank 1 — D-060 — Exact-revision corpus inventory and quota recalibration
- **TASK_REF:** `D-060`
- **PRIORITY:** `P0-CRITICAL`
- **IMPORTANCE:** `100/100`
- **STATUS:** `IN_PROGRESS`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** D-058 DONE; D-059 DONE.
- **ACCEPTANCE:** Immutable-revision inventory, regression tests, persisted evidence, D-058/D-019 consistency check, ranked second-pass backlog.
- **BONUS:** `D-060-B` — inventory delta evidence.
- **CLAIMED_BY:** Nodus
- **CLAIMED_AT:** 2026-10-04T20:20:00-04:00
- **CLAIM_HEAD:** `8d3d5e80c2c3a346575b3f12e156ee77a649a421`
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

### Rank 2 — D-061 — Progression schema/API migration child
- **TASK_REF:** `D-061`
- **PRIORITY:** `P0`
- **IMPORTANCE:** `99/100`
- **STATUS:** `BLOCKED`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** D-060 DONE.
- **ACCEPTANCE:** Implementation-ready progression migration packet and D-032 synchronization.
- **BONUS:** `D-061-B` — machine-readable migration fixtures.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

### Rank 3 — D-062 — Broader social schema/API migration child
- **TASK_REF:** `D-062`
- **PRIORITY:** `P0`
- **IMPORTANCE:** `98/100`
- **STATUS:** `BLOCKED`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** D-060 DONE.
- **ACCEPTANCE:** Implementation-ready social/memory/knowledge/privacy/save/projection migration packet.
- **BONUS:** `D-062-B` — Tamsin privacy fixtures.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

### Rank 4 — D-063 — Items/economy schema/API migration child
- **TASK_REF:** `D-063`
- **PRIORITY:** `P0`
- **IMPORTANCE:** `97/100`
- **STATUS:** `BLOCKED`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** D-060 DONE.
- **ACCEPTANCE:** Implementation-ready current inventory/equipment/item migration packet; D-032 reassessed.
- **BONUS:** `D-063-B` — item/equipment compatibility matrix.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

### Rank 5 — D-064 — Player-safe room/actor projection runtime slice
- **TASK_REF:** `D-064`
- **PRIORITY:** `P0`
- **IMPORTANCE:** `96/100`
- **STATUS:** `BLOCKED`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** D-060 DONE; D-030 contract/migration map.
- **ACCEPTANCE:** Versioned authoritative room/actor projection with strict mapping, equivalence and privacy tests.
- **BONUS:** `D-064-B` — actor equivalence/redaction evidence.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

### Rank 6 — D-065 — Tamsin durable-memory reactive proof
- **TASK_REF:** `D-065`
- **PRIORITY:** `P0`
- **IMPORTANCE:** `95/100`
- **STATUS:** `BLOCKED`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** D-062 DONE.
- **ACCEPTANCE:** Prior interaction creates durable Tamsin state; later content reacts; save/load and privacy tests pass.
- **BONUS:** `D-065-B` — negative projection leak regression.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

### Rank 7 — D-066 — Phase 1 progression proof
- **TASK_REF:** `D-066`
- **PRIORITY:** `P0`
- **IMPORTANCE:** `94/100`
- **STATUS:** `BLOCKED`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** D-061 DONE.
- **ACCEPTANCE:** Meaningful authoritative progression change persists through save/load and projects safely.
- **BONUS:** `D-066-B` — deterministic progression replay.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

### Rank 8 — D-067 — Phase 1 inventory/equipment exact-head proof
- **TASK_REF:** `D-067`
- **PRIORITY:** `P0`
- **IMPORTANCE:** `93/100`
- **STATUS:** `BLOCKED`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** D-063 DONE.
- **ACCEPTANCE:** Requirement #6 proven across Python state, persistence and Android presentation on exact HEAD.
- **BONUS:** `D-067-B` — invalid-equip rollback tests.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

### Rank 9 — D-068 — Phase 1 activity exact-head proof
- **TASK_REF:** `D-068`
- **PRIORITY:** `P0`
- **IMPORTANCE:** `92/100`
- **STATUS:** `BLOCKED`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** D-060 DONE; V10 contracts.
- **ACCEPTANCE:** Selected activity proves legality, cost/time, persistent result, save/load and available Android path.
- **BONUS:** `D-068-B` — interruption/atomicity regression.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

### Rank 10 — D-069 — Tactical schemas, validators and pure grid core
- **TASK_REF:** `D-069`
- **PRIORITY:** `P0`
- **IMPORTANCE:** `91/100`
- **STATUS:** `BLOCKED`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** D-060 DONE; D-032 combat packet.
- **ACCEPTANCE:** Backward-compatible tactical schemas plus deterministic coordinate/occupancy/path/LOS/cover tests.
- **BONUS:** `D-069-B` — grid/visibility invariants.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

### Rank 11 — D-070 — Tactical transient state, turn and action engine
- **TASK_REF:** `D-070`
- **PRIORITY:** `P0`
- **IMPORTANCE:** `90/100`
- **STATUS:** `BLOCKED`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** D-069 DONE.
- **ACCEPTANCE:** Headless transient encounter executes deterministic turns/actions without GameState tactical schema expansion.
- **BONUS:** `D-070-B` — deterministic transcript/replay hash.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

### Rank 12 — D-071 — Tactical awareness, cover, objectives, retreat and bounded AI
- **TASK_REF:** `D-071`
- **PRIORITY:** `P0`
- **IMPORTANCE:** `89/100`
- **STATUS:** `BLOCKED`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** D-070 DONE.
- **ACCEPTANCE:** Knowledge-correct objective/retreat encounter behavior with bounded deterministic AI and no hidden-state leak.
- **BONUS:** `D-071-B` — developer AI diagnostics.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

### Rank 13 — D-072 — Tactical aftermath, injury and world consequence
- **TASK_REF:** `D-072`
- **PRIORITY:** `P0`
- **IMPORTANCE:** `88/100`
- **STATUS:** `BLOCKED`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** D-071 DONE.
- **ACCEPTANCE:** Atomic validated aftermath persists injury/world/quest/social/time consequences with rollback before commit.
- **BONUS:** `D-072-B` — fault-injection atomicity tests.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

### Rank 14 — D-073 — Gate Twelve tactical content and Python bridge
- **TASK_REF:** `D-073`
- **PRIORITY:** `P0`
- **IMPORTANCE:** `87/100`
- **STATUS:** `BLOCKED`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** D-072 DONE.
- **ACCEPTANCE:** One bounded encounter starts/plays/resolves/retreats through authoritative player-safe Python bridge.
- **BONUS:** `D-073-B` — combat projection redaction audit.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

### Rank 15 — D-074 — Android tactical DTO/mapper/ViewModel/Compose surface
- **TASK_REF:** `D-074`
- **PRIORITY:** `P0`
- **IMPORTANCE:** `86/100`
- **STATUS:** `BLOCKED`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** D-073 DONE.
- **ACCEPTANCE:** Typed Android tactical surface operates the encounter without duplicating gameplay authority.
- **BONUS:** `D-074-B` — tactical accessibility checks.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

### Rank 16 — D-075 — Phase 1 quest branch and world-consequence proof
- **TASK_REF:** `D-075`
- **PRIORITY:** `P0/P1`
- **IMPORTANCE:** `84/100`
- **STATUS:** `BLOCKED`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** D-060 DONE; quest/world contracts.
- **ACCEPTANCE:** Two meaningful quest outcomes persist and create intended later scene/actor/world divergence.
- **BONUS:** `D-075-B` — branch-difference fixture.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

### Rank 17 — D-076 — Integrated Phase 1 save/load and deterministic regression gate
- **TASK_REF:** `D-076`
- **PRIORITY:** `P0`
- **IMPORTANCE:** `83/100`
- **STATUS:** `BLOCKED`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** Relevant D-065 through D-075 proof tasks DONE.
- **ACCEPTANCE:** One exact-head integrated sequence survives save/reload/continue with deterministic authoritative outcomes.
- **BONUS:** `D-076-B` — corrupted/unsupported-save fixture.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

### Rank 18 — D-077 — Android Phase 1 consumer/test-gap closure
- **TASK_REF:** `D-077`
- **PRIORITY:** `P0/P1`
- **IMPORTANCE:** `80/100`
- **STATUS:** `BLOCKED`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** D-064, D-067, D-068, D-074, D-075, D-076 as relevant.
- **ACCEPTANCE:** Known D-021/D-026 field/render/action gaps closed with exact-head Android evidence.
- **BONUS:** `D-077-B` — screen/projection/owner/test matrix.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

### Rank 19 — D-078 — Low-end performance profiling and bounded budgets
- **TASK_REF:** `D-078`
- **PRIORITY:** `P0/P1`
- **IMPORTANCE:** `78/100`
- **STATUS:** `BLOCKED`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** D-077 DONE; integrated measurable slice.
- **ACCEPTANCE:** Repeatable performance budgets/evidence with emulator/device distinction and no unsupported compatibility claim.
- **BONUS:** `D-078-B` — worst-case bounded performance ledger.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

### Rank 20 — D-079 — Phase 1 integrated acceptance candidate + APK provenance
- **TASK_REF:** `D-079`
- **PRIORITY:** `P0-CRITICAL FINAL GATE`
- **IMPORTANCE:** `100/100 final`
- **STATUS:** `BLOCKED`
- **SOURCE_OF_WORK:** `docs/AI_20_TASK_EXECUTION_CAMPAIGN_2026-10-04.md` + matching master-register task.
- **DEPENDENCIES:** All required Phase 1 proof tasks through D-078.
- **ACCEPTANCE:** Exact-head exit-gate PASS or precise failing gate; test/build evidence and debug/test APK provenance when supported.
- **BONUS:** `D-079-B` — reconstruction handoff bundle.
- **CLAIMED_BY:** —
- **CLAIMED_AT:** —
- **CLAIM_HEAD:** —
- **COMPLETION_HEAD:** —
- **EVIDENCE:** pending
- **BRAG_CARD:** pending
- **NEXT_TASK_CREATED_OR_REFRESHED:** no

## Queue maintenance

D-060 is the only initial READY campaign task. Completing agents unlock direct dependents by evidence, not by rank alone.

If all ranked tasks are DONE, use live evidence to create the next program task only if real work remains. If all remaining work requires owner input, record the exact owner decision and stop instead of fabricating a task.
