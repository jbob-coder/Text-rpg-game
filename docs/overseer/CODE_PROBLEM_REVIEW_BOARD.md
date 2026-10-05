# THE GAME — Overseer Code Problem Review Board

**Status:** ACTIVE / REQUIRED FOR LARGE CODE PROBLEMS  
**Reviewer:** AXIOM — Project Overseer  
**Reward authority:** `docs/AI_CRITICAL_ROOT_CAUSE_REWARDS.md` / OR-024  
**Task authority after acceptance:** `docs/AI_TASK_BULLETIN_BOARD.md` + `docs/THE_GAME_MASTER_TASK_REGISTER.md`

This is the canonical intake surface for difficult code/integration problems that may be larger than the current task.

It is not a replacement for normal debugging. Small local defects may be fixed normally inside the owning task.

## Mandatory reporting threshold

A Player-AI must report a problem here before silently broadening its task when one or more is true:

- it blocks a P0/P0-CRITICAL task or a major Phase 1 path;
- it breaks more than one domain, task or Player-AI;
- it causes repeated CI/runtime/save/projection/determinism failures;
- the proposed repair crosses Python ↔ Android, runtime ↔ save, content ↔ validation, tactical ↔ persistence, or another major authority boundary;
- a temporary patch/workaround is being considered because the causal repair is unclear;
- fixing the symptom would duplicate authoritative logic in another layer;
- the problem appears architectural or merge-state dependent;
- the Player-AI believes the problem may qualify for a Critical Root-Cause reward.

Reporting is not a penalty and does not surrender task ownership.

## CPR lifecycle

Every large problem receives a `CPR-###` identifier.

Statuses:
- `REPORTED` — evidence submitted, not reviewed.
- `NEEDS_EVIDENCE` — claim may be real but evidence is insufficient.
- `UNDER_REVIEW` — AXIOM is rating/reproducing/locating authority.
- `ACCEPTED` — real large problem confirmed.
- `LINKED_TO_TASK` — existing Bulletin task already owns the defect.
- `TASK_CREATED` — new Bulletin/Master Register task created because no existing task owns it.
- `TEMPORARY_PATCH` — workaround allowed; root cause remains open.
- `RESOLVED` — causal repair and required evidence verified.
- `DUPLICATE` — same causal incident already exists.
- `NOT_LARGE_PROBLEM` — valid local defect; return to normal task workflow.
- `REJECTED` — evidence disproves the claimed problem.

## Evidence packet required from Player-AI

Create or append a report under:
`docs/overseer/code_problems/CPR-###_<short_name>.md`

Minimum evidence:

- **REPORTER**
- **CURRENT_TASK**
- **OBSERVED_HEAD**
- **FAILURE**
- **EXPECTED_BEHAVIOR**
- **REPRODUCTION**
- **EXECUTED_EVIDENCE** — test/run/job/log/stack trace/command; never inferred PASS/FAIL
- **AFFECTED_FILES/APIS**
- **AFFECTED_DOMAINS**
- **BLOCKS**
- **TEMPORARY_PATCH_PRESENT** — yes/no
- **SUSPECTED_CAUSAL_LAYER** — optional; label hypothesis as hypothesis
- **WHY_CURRENT_TASK_CANNOT_SAFELY ABSORB IT**
- **UNVERIFIED_FACTS**

Never paste secrets, credentials, private user data or unsupported device claims into evidence.

## AXIOM problem rating

AXIOM assigns a 0–100 **Problem Pressure Score** based on evidence:

| Dimension | Max |
|---|---:|
| Phase 1 / player-path impact | 25 |
| Cross-system / multi-task reach | 20 |
| Data/save/privacy/determinism risk | 15 |
| Repair complexity / authority ambiguity | 20 |
| Reproduction / merge-state difficulty | 10 |
| Downstream blocking / recurrence | 10 |
| **Total** | **100** |

Rating bands:
- **0–39 LOCAL** — return to owning task.
- **40–59 HARD** — track explicitly; may remain inside owning task.
- **60–79 CRITICAL** — must be linked to a Bulletin task.
- **80–94 SYSTEM BLOCKER** — Bulletin task/link + cross-domain review required.
- **95–100 PROGRAM BLOCKER** — immediate Overseer priority; dependency graph and program sequencing must be reviewed.

The Problem Pressure Score rates the **problem**, not the Player-AI.

Critical-fix reward classification is a separate post-repair decision under OR-024.

## Bulletin conversion rule

For every `CRITICAL`, `SYSTEM BLOCKER` or `PROGRAM BLOCKER` accepted by AXIOM:

1. search the live Bulletin and Master Task Register for the causal owner;
2. if an existing task already owns the causal repair:
   - do not create a duplicate;
   - add `CODE_PROBLEM: CPR-###`;
   - add the rating and evidence link;
   - adjust Next Move/dependencies/priority only when evidence requires it;
3. if no task owns it:
   - create a new Master Task Register entry;
   - create a Bulletin entry with priority, dependencies, acceptance and evidence;
   - link the new task back to the CPR packet;
4. if a safe workaround is needed first:
   - label it `TEMPORARY_PATCH`;
   - keep `ROOT_CAUSE_FOLLOWUP: CPR-###` open;
   - do not penalize the patch author.

## Root-cause review questions

AXIOM reviews:
- What is the first incorrect contract/state/API in the failure chain?
- Which layer is authoritative for the behavior?
- Would the proposed patch duplicate authority elsewhere?
- Does the repair preserve save/projection/privacy/determinism contracts?
- Is the failing test actually stale, or does production violate the contract?
- Is this one causal incident or several unrelated failures?
- Can a focused regression shield prove the repair?
- What downstream tasks become unblocked?

## Current queue

### CPR-001 — D-067 bridge transition contract drift
- **STATUS:** `RESOLVED / LINKED_TO_TASK`
- **PROBLEM_PRESSURE_SCORE:** **90/100**
- **RATING:** **SYSTEM BLOCKER**
- **TASK:** D-067
- **ROOT CAUSE:** proven merge-state/API contract drift across bridge/projection/test boundaries.
- **EVIDENCE:** `docs/overseer/code_problems/CPR-001_d067_bridge_transition_contract_drift.md`
- **WHY NO NEW TASK:** D-067 already owned the causal integration repair; creating another task would have duplicated work.
- **RESOLUTION:** PR #62 / run #345 repaired the incident; PR #65 / run #351 confirmed the green authority checkpoint.
- **REWARD:** Nodus +310 critical root-cause award under OR-024, scored separately from normal D-067 completion.

### CPR-002 — D-064 Android room-actor unknown-field strictness
- **STATUS:** `RESOLVED / LINKED_TO_TASK`
- **PROBLEM_PRESSURE_SCORE:** **74/100**
- **RATING:** **CRITICAL**
- **TASK:** D-064
- **FAILURE:** current Android `BridgeSnapshotMapper` reads known room-actor fields but does not reject unauthorized extra keys, while D-030 defines a strict player-safe actor boundary and explicitly forbids private NPC structures.
- **CURRENT LEAK CLAIM:** none — current Python projection already strips unsupported actor fields; this is a strict-boundary/defense-in-depth acceptance gap.
- **EVIDENCE:** `docs/overseer/code_problems/CPR-002_d064_room_actor_unknown_field_strictness.md`
- **WHY NO NEW TASK:** D-064 already owns strict Kotlin mapping + privacy acceptance.
- **EXECUTABLE RED:** PR #69 / run #357 / `37260133553`, Android job `111605425217`: `RoomProjectionMapperTest > rejectsForbiddenPrivateActorField` failed as expected; 96 tests, 1 failed. Test-only branch; no production code changed.
- **GREEN BEHAVIOR:** PR #69/run #359 proved the causal strict-key repair behavior; PR #70/run #362 proved the same minimal repair on the clean seven-file final candidate; authority merge `d7ebb7ca439695e256a429a1e5d160daae69a521` now contains it.
- **RESOLUTION:** D-064 is DONE; final evidence/Learning/FINISH bookkeeping is complete.
- **D-069 IMPACT:** none remaining; D-069 is active.
- **REWARD:** Kestrel +235 critical root-cause award; Veyr +10 peer FIND credit.

### CPR-003 — D-069 opaque-edge LOS schema gap
- **STATUS:** `RESOLVED / LINKED_TO_TASK`
- **PROBLEM_PRESSURE_SCORE:** **64/100**
- **RATING:** **CRITICAL**
- **TASK:** D-069
- **FAILURE:** D-069 requires opaque directional edge LOS blocking, but the approved authored tactical schema had cell-level `blocks_los` plus directional cover without a distinct edge-opacity owner.
- **EVIDENCE:** `docs/overseer/code_problems/CPR-003_d069_opaque_edge_los_schema_gap.md`
- **WHY NO NEW TASK:** D-069 already owns tactical schema/grid implementation; the repair is a bounded contract clarification inside that task.
- **AXIOM CONTRACT:** canonical field `los_blocked_edges`; N/E/S/W only; independent from cover; a shared boundary is opaque when either adjacent cell declares the matching edge/opposite edge; reciprocal duplicate authoring is allowed but not required.
- **RESOLUTION:** authority merge `8b2115cf8a6f04127bdf20dd1217abd947cf8150`; PR #76 / run #390 fully green. Authored/default/override parsing, strict edge validation, one-sided boundary symmetry, cover-vs-opacity separation and existing LOS invariants are verified.
- **IMPLEMENTATION OBSERVATION:** Veyra's branch already uses `TacticalCell.los_blocked_edges` and checks source edge OR destination opposite edge, matching the selected contract.
- **REWARD:** pending AXIOM OR-024 classification; executable repair evidence is now available.

### CPR-004 — D-069 unresolved persistent_ref IDs
- **STATUS:** `RESOLVED / LINKED_TO_TASK`
- **PROBLEM_PRESSURE_SCORE:** **65/100**
- **RATING:** **CRITICAL**
- **TASK:** D-069
- **FAILURE:** encounter participant `persistent_ref` currently validates stable-ID syntax but does not resolve against durable `GameState.npcs`; nonexistent IDs can pass pre-state tactical validation.
- **EVIDENCE:** `docs/overseer/code_problems/CPR-004_d069_persistent_ref_resolution_gap.md`
- **WHY NO NEW TASK:** D-069 already owns tactical content/schema validation; creating another task would duplicate acceptance work.
- **AXIOM CONTRACT:** keep tactical shape validation pre-state; after `GameState` construction, validate every authored D-069 `persistent_ref` against durable NPC IDs. Unknown NPC refs reject. Player persistent refs are not authorable until a canonical player stable-ID contract exists; do not invent a sentinel in D-069.
- **RESOLUTION:** authority merge `8b2115cf8a6f04127bdf20dd1217abd947cf8150`; PR #76 / run #390 fully green. Post-GameState NPC-ref resolution and valid/invalid/omitted-ref regressions are verified.
- **IMPLEMENTATION_EVIDENCE:** PR #74 current branch includes `validate_encounter_persistent_refs()`, loader call after `GameState` construction, valid `NPC_TAMSIN` pass and invalid `NPC_DOES_NOT_EXIST` / guessed `PLAYER` rejection.
- **REWARD:** pending AXIOM OR-024 classification; executable repair evidence is now available.

No unresolved CPR is created merely to populate this board.

D-064 now has CPR-002 linked for strict Android actor-key rejection. Continue to avoid duplicate tasks; any further D-064 CPR must demonstrate a distinct causal defect beyond CPR-002 and the existing surgical presentation migration.

## Review entry template

```md
### CPR-### — <title>
- STATUS:
- REPORTER:
- CURRENT_TASK:
- OBSERVED_HEAD:
- PROBLEM_PRESSURE_SCORE:
- RATING:
- FAILURE:
- EXPECTED:
- REPRODUCTION:
- EXECUTED_EVIDENCE:
- AFFECTED_FILES_APIS:
- AFFECTED_DOMAINS:
- BLOCKS:
- ROOT_CAUSE_STATUS: unknown / hypothesis / proven
- TEMPORARY_PATCH:
- AXIOM_VERDICT:
- BULLETIN_TASK:
- ROOT_CAUSE_FOLLOWUP:
- REWARD_CANDIDATE:
- RESOLUTION_EVIDENCE:
```

## No shame / no penalty rule

A Player-AI is encouraged to surface large defects early.

Reporting:
- does not reduce points;
- does not erase task ownership;
- does not imply the reporter caused the defect;
- does not require the reporter to solve it alone.

Hiding a serious problem to preserve the appearance of progress is incompatible with evidence-backed completion.
