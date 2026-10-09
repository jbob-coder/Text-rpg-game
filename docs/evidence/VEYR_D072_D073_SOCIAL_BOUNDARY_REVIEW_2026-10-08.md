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


## Source-to-test coverage audit — continuation pass, 2026-10-08 AST

**Method:** read the named test definitions through the GitHub source connector on the current authority branch; the presence of an assertion is **static coverage evidence**, not proof it passes on today's HEAD. This section does not execute tests and is not a D-072 compliance ruling.

| Existing exact test and source blob | Assertion actually inspected | Coverage limit / future cross-domain test |
|---|---|---|
| \`tests/test_combat_state.py::test_transient_session_does_not_mutate_game_state\` (blob \`784a8756dc9df27bf0eeb04d51a56a836c083b5b\`) | Captures \`durable.snapshot()\`, advances a separate \`CombatSession\`, and asserts that durable snapshot and absence of combat fields are unchanged. | Protects transient separation. It does not exercise any permitted post-combat aftermath write. |
| \`tests/test_combat_scheduling.py::test_all_commits_roll_back_even_after_event_was_appended\` (blob \`a516c51fbc767d6b21e93e3ee0a500215faa09ea\`) | Injects \`_append_event\` failure across move/sprint/prepare/consume/end and compares transient \`session.__dict__\`. | Proves the authored **test checks** in-session atomicity, not a late failure after durable GameState/social/quest mutation. |
| \`tests/test_combat_objectives.py::test_post_append_failures_restore_objective_departure_and_detection_state\` (blob \`6a37bf48dbfb972dcba88df41d2bd503fd9a6b08\`) | Fault injection on interact/retreat/detect/move; compares session internals, objective status and observer contacts after exception. | Covers encounter resolution invariants; not an after-encounter persistent transaction. |
| \`tests/test_combat_knowledge.py::test_los_does_not_reveal_an_unknown_actor_or_private_state\` and \`test_detection_is_observer_specific_and_does_not_identify\` (blob \`ddb0642fa0f30e240b0b08a12912785fc7df885f\`) | No raw hidden actor/faction in untouched observer view; detection creates a DETECTED contact without identity, and a second observer remains unaware. | Confirms an existing encounter-local observer-view test contract, not a later Android aftermath payload or public social propagation. |
| \`tests/test_social.py::test_multi_recipient_leak_rolls_back_when_later_recipient_is_invalid\` (blob \`9a5257c734600492f96cc43dfa805be15fb11b7d\`) | An invalid later NPC recipient raises \`RuleError\`; NPCs, relationships, history and earlier-recipient learned knowledge compare equal to pre-state. | Strong social-local failure proof; not a full encounter+injury+quest+time rollback. |
| \`tests/test_social.py::test_leak_eligibility_query_does_not_create_missing_npcs\` (same blob) | The query may return \`NPC_MISSING\` as a *candidate* while not creating its NPC/relationship record. | Important distinction: **candidate eligibility is not approved durable identity nor successful execution**. Future aftermath must validate a real persistent ID before calling the mutating helper. |
| \`tests/test_phase1_quest_branch_world_consequence.py::test_dead_relay_resolutions_persist_and_create_player_safe_divergence\` (blob \`07d2c52892e989d51abe7fa6b6f630b3571c00cc\`) | Cooperative and solo paths are saved/reloaded; authorized Tamsin-specific choice differs, while a private memory ID and raw \`memories\` key stay out of the player-safe payload. | Does not imply a public reputation publisher, combat-to-social causal credit, or \`SOC_0007/SOC_0010\` qualification. |
| \`tests/test_android_bridge.py::test_new_session_returns_player_safe_scene_and_status\` (blob \`bd389dc04ae19990d7049f65818a3e8f843869d6\`) | Expects explicit eight-key current bridge view and no keys in \`FORBIDDEN_AUTHORED_KEYS\`. | Baseline noncombat projection, not authorization for a raw combat/session or hidden aftermath DTO. |
| \`tests/test_android_bridge.py::test_load_failure_does_not_replace_current_state\` (same blob) | Unsupported save-schema load raises \`LOAD_ERROR\`; current GameState snapshot is unchanged. | A failed load is not a simulated partial D-072 aftermath commit or proof of future session loading migration behavior. |

### Suggested minimal owner-executable verification sequence

This is **test design only**, and the names below are check identifiers rather than existing test functions.

1. **VA-01/02: durable identity isolation.** At a valid pre-combat checkpoint, obtain a real known NPC ID set. Resolve A/B as transient contacts (no \`persistent_ref\`) and separately try a syntactically valid but absent NPC ref. Compare the deep post-run NPC identity set and relationship keys to pre-run values; the invalid-ref variant must be rejected before mutation.
2. **VA-04: whole-state rollback.** Use one valid planned aftermath effect and inject failure at a later phase after a first durable mutation has been attempted. Compare a *deep* \`GameState.snapshot()\`, including \`npcs\`, \`relationships\`, \`knowledge\`, \`quests\`, \`flags\`, \`history\`, \`player.conditions\` and world time. Record the exact exception and test head.
3. **VA-05: duplicate credit.** After one committed approved result, replay the same specific transaction and then save/reload before replaying it again. Assert no extra authored consequence. A valid deduplication test depends on the D-072 owner's real transaction-identity contract; do not invent this field in documentation.
4. **VA-06/07/10: disclosure.** Compare an identified authorized contact, an unidentified detected contact and a wholly unseen contact; add a deliberately private NPC-held assertion and check the *returned bridge projection*, not only encounter knowledge view. No accidental public rumor/passive inference.
5. **VA-03/08/09: regression sweep.** Rerun established Tamsin branch/save/reload and social rollback tests after aftermath integration; combine provisional condition invalidation with the same all-or-nothing state fingerprint. Mark unrelated proposed status/passive features NOT IMPLEMENTED rather than FAIL.

### Remaining limits and owner instructions

- The reviewed existing tests express coverage assertions. This pass did not run the Python interpreter, CI, Gradle, emulator, or device. Do not report their result as PASS.
- Existing test coverage should not be misrepresented as missing merely because it lives in another domain. The **unproven seam** is the *cross-domain durable commit + player-safe disclosure* on the actual D-072/D-073 implementation candidate.
- D-072 claimant Silex controls implementation and final evidence; this PR #82 is a draft documentation review only. D-073 remains BLOCKED until the Bulletin independently records D-072 DONE.
