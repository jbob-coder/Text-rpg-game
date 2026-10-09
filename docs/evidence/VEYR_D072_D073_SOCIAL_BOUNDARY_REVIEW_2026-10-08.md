# Veyr — D-072/D-073 NPC/Social Boundary Review

Status: Non-owning documentation review only; no task claim, canon promotion, implementation or test-execution claim.
Date: 2026-10-08 AST.
Reviewer: PLAYER_VEYR, session SESSION_VEYR_20261008T1747-0400_S02.
Source authority: docs/master-game-development-program, at 7ddf7220103075350e9d4d7ddf6e7c6d5811e13b.

## Evidence and boundaries

The injury/aftermath standard requires a validated plan, complete durable-state snapshot and all-or-nothing rollback. Combat session and combat knowledge remain encounter-local. The D-069 migration packet resolves persistent NPC references against GameState.npcs after state construction. The OR-034 Gate Twelve provisional fixture identifies CONTACT_SERVICE_FORK_A/B as encounter-only contacts without persistent_ref. The social.ensure_npc helper can create NPC shells, so a tactical contact identifier cannot safely be passed into it as if it were an approved durable identity. The Android bridge requires player-safe projected output, never raw NPC knowledge, memories or goals. P14 separates occurrence, observer knowledge, public publication, passive qualification and player disclosure.

These are existing standards, not new defects. CPR-004 already addresses unknown persistent references at content load. No D-072 implementation or CI tests were verified in this pass.

## Future negative test matrix — none executed

- VA-01: provisional contact A/B resolves with no permanent NPC or relationship record.
- VA-02: unknown persistent_ref rejects without any durable mutation.
- VA-03: one authorized Tamsin aftermath observation does not publish reputation.
- VA-04: injected late failure restores entire GameState snapshot, including NPC memory, conditions, quest, flags, time and history.
- VA-05: retry or save/load does not duplicate aftermath credit.
- VA-06: visible but unidentified tactical contact reveals no hidden identity or AI intent.
- VA-07: private learned NPC rumor is not player-visible public truth.
- VA-08: D-075 cooperative and secret Tamsin routes retain proven player-safe choice divergence, without unlocking a social passive.
- VA-09: unsupported provisional condition cannot partially persist NPC injury.
- VA-10: bridge output omits NPC-private goals, memories, knowledge maps and hidden Status qualification counters.

Suggested test entry points: tests/test_social.py, tests/test_phase1_quest_branch_world_consequence.py, tests/test_android_bridge.py. The actual D-072 aftermath test file should be selected from the owning change, not guessed.

## Handoff

D-072 remains Silex-owned. D-073 remains blocked until D-072 DONE. This is a checklist for a later reviewer, not permission to alter Silex's work or declare an integration pass. Proposed Gate Twelve conditions and knowledge IDs remain provisional. Escalate to AXIOM only with a concrete new reproducible regression. No code, tests, CI, devices or runtime were executed.


## Second documentation pass — verification ownership and failure classification

The authority Bulletin was re-read on 2026-10-08 AST after the first document commit: still zero READY tasks; D-072 is IN_PROGRESS under Silex and D-073 is BLOCKED. This appendix is review-support evidence, not a fresh claim or permission to implement the blocked dependency.

### Exact source/fixture starting points

| Review seam | Existing starting point | What is not yet proven by that source alone |
|---|---|---|
| Tactical identity | `docs/systems/PHASE_1_COMBAT_SCHEMA_API_MIGRATION_PACKET.md` §7.1; `src/textrpg/combat_state.py` | A production D-072 aftermath-to-durable actor adapter has passed validation. |
| Temporary contact | `docs/systems/GATE_TWELVE_PHASE1_TACTICAL_ENCOUNTER_PACKET.md` §24A | Provisional contact A/B should be permanent NPCs or canonically named opponents. |
| NPC mutation | `src/textrpg/social.py::ensure_npc`; `tests/test_social.py` | The social creator validates tactical actor legitimacy. It does not. |
| Branch/social persistence | `tests/test_phase1_quest_branch_world_consequence.py`, including `COOPERATIVE_ROUTE`, `SOLO_ROUTE`, `branch_fingerprint` and `durable_branch_fingerprint` | Tamsin's approved private memory constitutes public reputation or an unlocked passive. |
| Transaction policy | `docs/systems/INJURY_CONDITION_AFTERMATH_STANDARD.md` §8 | Runtime late-failure rollback is already proven for the not-yet-verified D-072 merge state. |
| Combat disclosure | `docs/systems/LOS_DETECTION_AND_COMBAT_KNOWLEDGE_STANDARD.md` §§8,11; `src/textrpg/combat_knowledge.py` | A visible contact is necessarily identified; or a bridge projection may copy encounter internals. |
| Social publication | `docs/systems/status/SOCIAL_PASSIVE_EVIDENCE_PUBLICATION_QUALIFICATION_CONTRACT_P14.md` §§2-7 | Any existing approved publication authority, UEV-style SOCIAL qualifier, save field or passive-list DTO. |
| Player-safe consumer | `src/textrpg/android_bridge.py::_view_for`; `tests/test_android_bridge.py` | Android is authorized to derive NPC-private beliefs or passive unlocks from raw state. |

### Reviewer runbook for an eventual D-072 merge candidate

1. **Identify evidence first.** Capture owning PR, tested head, authority/base head, exact diff, selected fixture set and workflow-run ID. A green test on an earlier commit is not a tested current merge state.
2. **Classify the actor.** For each encounter participant, record encounter-local actor ID, whether a `persistent_ref` exists, and whether it resolves to a pre-existing durable `GameState.npcs` identity. Unknown references must reject; absence of a ref never implies a new NPC.
3. **Record the pre-state fingerprint.** Capture a deep serializable `GameState` snapshot plus the player-safe bridge view and the sorted durable NPC/relationship identity keys. Do not copy these internal fingerprints into player-facing payloads.
4. **Inject one fault after an otherwise valid intermediate planned write.** Specifically compare state after a late failure to the complete pre-state, including world time and appended history. A rollback assertion limited to player health would not be sufficient.
5. **Rerun the same authored event/retry path and reload from save.** Establish whether the owning implementation has stable transaction identity/deduplication; do not backfill a fabricated ID into legacy history merely to pass the check.
6. **Audit the consumer projection separately.** Compare legitimate player-safe consequences with the private internal state. A missing private record from one UI screen alone is insufficient if another endpoint serializes the same prohibited information.
7. **Document RESULT as PASS / FAIL / BLOCKED / NOT RUN per check.** Treat VA-03, VA-07 and VA-08 as social design/visibility safeguards unless the claimant's approved integration explicitly exercises those paths. Keep the total Phase 1 acceptance gate honest.

### Failure classification to prevent false defect reports

- **NOT YET IMPLEMENTED:** D-072 merge candidate, SOC publication or passive qualification runtime is absent; do not treat the absence of an approved future feature as a new regression.
- **AUTHORED PROVISIONAL:** OR-034 fixture IDs and proposed injury/knowledge records are used in a bounded integration test with clear provisional tagging; not equivalent to canon approval.
- **TRUE REGRESSION CANDIDATE:** A demonstrated unknown persistent ref creates a durable shell; fault-injected partial aftermath survives; or prohibited NPC-private state enters an actually returned player-safe payload. Capture exact evidence and coordinate before CPR filing.
- **OUT OF SCOPE:** An alternate combat AI strategy, NPC-wide reputation model, new named rival, social-passive thresholds, or a new world publisher. Each requires its own approved owner and dependency gate.

**Review result at this checkpoint:** source-backed test-design guidance only; no Python test execution, live D-072 diff review, Android/CI run, task claim, source modification or canonical world decision. Do not mark VA-01..VA-10 PASS until an actual test run establishes the claim.
