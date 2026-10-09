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
| `tests/test_combat_state.py::test_transient_session_does_not_mutate_game_state` (blob `784a8756dc9df27bf0eeb04d51a56a836c083b5b`) | Captures `durable.snapshot()`, advances a separate `CombatSession`, and asserts that durable snapshot and absence of combat fields are unchanged. | Protects transient separation. It does not exercise any permitted post-combat aftermath write. |
| `tests/test_combat_scheduling.py::test_all_commits_roll_back_even_after_event_was_appended` (blob `a516c51fbc767d6b21e93e3ee0a500215faa09ea`) | Injects `_append_event` failure across move/sprint/prepare/consume/end and compares transient `session.__dict__`. | Proves the authored **test checks** in-session atomicity, not a late failure after durable GameState/social/quest mutation. |
| `tests/test_combat_objectives.py::test_post_append_failures_restore_objective_departure_and_detection_state` (blob `6a37bf48dbfb972dcba88df41d2bd503fd9a6b08`) | Fault injection on interact/retreat/detect/move; compares session internals, objective status and observer contacts after exception. | Covers encounter resolution invariants; not an after-encounter persistent transaction. |
| `tests/test_combat_knowledge.py::test_los_does_not_reveal_an_unknown_actor_or_private_state` and `test_detection_is_observer_specific_and_does_not_identify` (blob `ddb0642fa0f30e240b0b08a12912785fc7df885f`) | No raw hidden actor/faction in untouched observer view; detection creates a DETECTED contact without identity, and a second observer remains unaware. | Confirms an existing encounter-local observer-view test contract, not a later Android aftermath payload or public social propagation. |
| `tests/test_social.py::test_multi_recipient_leak_rolls_back_when_later_recipient_is_invalid` (blob `9a5257c734600492f96cc43dfa805be15fb11b7d`) | An invalid later NPC recipient raises `RuleError`; NPCs, relationships, history and earlier-recipient learned knowledge compare equal to pre-state. | Strong social-local failure proof; not a full encounter+injury+quest+time rollback. |
| `tests/test_social.py::test_leak_eligibility_query_does_not_create_missing_npcs` (same blob) | The query may return `NPC_MISSING` as a *candidate* while not creating its NPC/relationship record. | Important distinction: **candidate eligibility is not approved durable identity nor successful execution**. Future aftermath must validate a real persistent ID before calling the mutating helper. |
| `tests/test_phase1_quest_branch_world_consequence.py::test_dead_relay_resolutions_persist_and_create_player_safe_divergence` (blob `07d2c52892e989d51abe7fa6b6f630b3571c00cc`) | Cooperative and solo paths are saved/reloaded; authorized Tamsin-specific choice differs, while a private memory ID and raw `memories` key stay out of the player-safe payload. | Does not imply a public reputation publisher, combat-to-social causal credit, or `SOC_0007/SOC_0010` qualification. |
| `tests/test_android_bridge.py::test_new_session_returns_player_safe_scene_and_status` (blob `bd389dc04ae19990d7049f65818a3e8f843869d6`) | Expects explicit eight-key current bridge view and no keys in `FORBIDDEN_AUTHORED_KEYS`. | Baseline noncombat projection, not authorization for a raw combat/session or hidden aftermath DTO. |
| `tests/test_android_bridge.py::test_load_failure_does_not_replace_current_state` (same blob) | Unsupported save-schema load raises `LOAD_ERROR`; current GameState snapshot is unchanged. | A failed load is not a simulated partial D-072 aftermath commit or proof of future session loading migration behavior. |

### Suggested minimal owner-executable verification sequence

This is **test design only**, and the names below are check identifiers rather than existing test functions.

1. **VA-01/02: durable identity isolation.** At a valid pre-combat checkpoint, obtain a real known NPC ID set. Resolve A/B as transient contacts (no `persistent_ref`) and separately try a syntactically valid but absent NPC ref. Compare the deep post-run NPC identity set and relationship keys to pre-run values; the invalid-ref variant must be rejected before mutation.
2. **VA-04: whole-state rollback.** Use one valid planned aftermath effect and inject failure at a later phase after a first durable mutation has been attempted. Compare a *deep* `GameState.snapshot()`, including `npcs`, `relationships`, `knowledge`, `quests`, `flags`, `history`, `player.conditions` and world time. Record the exact exception and test head.
3. **VA-05: duplicate credit.** After one committed approved result, replay the same specific transaction and then save/reload before replaying it again. Assert no extra authored consequence. A valid deduplication test depends on the D-072 owner's real transaction-identity contract; do not invent this field in documentation.
4. **VA-06/07/10: disclosure.** Compare an identified authorized contact, an unidentified detected contact and a wholly unseen contact; add a deliberately private NPC-held assertion and check the *returned bridge projection*, not only encounter knowledge view. No accidental public rumor/passive inference.
5. **VA-03/08/09: regression sweep.** Rerun established Tamsin branch/save/reload and social rollback tests after aftermath integration; combine provisional condition invalidation with the same all-or-nothing state fingerprint. Mark unrelated proposed status/passive features NOT IMPLEMENTED rather than FAIL.

### Remaining limits and owner instructions

- The reviewed existing tests express coverage assertions. This pass did not run the Python interpreter, CI, Gradle, emulator, or device. Do not report their result as PASS.
- Existing test coverage should not be misrepresented as missing merely because it lives in another domain. The **unproven seam** is the *cross-domain durable commit + player-safe disclosure* on the actual D-072/D-073 implementation candidate.
- D-072 claimant Silex controls implementation and final evidence; this PR #82 is a draft documentation review only. D-073 remains BLOCKED until the Bulletin independently records D-072 DONE.


## P16/P17/P18 post-aftermath consumer audit — non-owning continuation (2026-10-08 AST)

**Reason for this pass:** Wave-4 P16/D-045, P17/D-026 and P18/D-046 are now completed **documentation children**. Their cross-domain contracts could be mistaken for implemented destinations when Silex completes D-072 and D-073 eventually integrates combat. Source review shows they are future-facing; this review protects the current transaction boundary rather than redefining their owners.

**Authority checked:** live Bulletin blob `26998093f487d7ed6a3b045fb99750eea0fdc6f9` (no READY tasks, D-072 `IN_PROGRESS / Silex`, D-073 `BLOCKED`); source:
- `docs/systems/GATE_TWELVE_PROGRESSION_PROOF_PACKET.md` (blob `6b7314983ff7a59ebf9ff26a991f4752a2a6541c`) §§8.4, 9.4, 11: current Trace Chamber evidence does **not** instantiate a mentor/evaluator or create social status/reputation. Future mentor capability requires a real durable NPC, authored capability, location/schedule and specific consuming rule. Player-known next training requirements do not reveal hidden thresholds or private evaluator logic.
- `docs/android/P17_D026_PERSISTENT_ADVERSARY_INTEL_PROJECTION_MIGRATION_2026-10-08.md` (blob `1d3338e2fd595d688fed5f402125800b26ca52ee`) §§2–4: persistent V09 nested adversary state and `adversary_intel` DTO are **not implemented**. Proposed intel requires player-known observer evidence and a public contact token. A combat-only transient contact or raw `npc_id` is not a reveal license; unseen injury and unseen position do not become current intel.
- `docs/systems/status/P18_D046_PLAYER_SAFE_PASSIVE_LIST_PROJECTION_CONTRACT.md` (blob `9420354bb96677e331da94c9d86d09ece1f15810`) §§3–9: acquired passive, qualifying evidence and authorized viewer reveal are distinct; `status.passives` and `projection_version=1` are **candidate wire fields only**, not live Status/Android. NPC rumor, casualty, training or observed ability cannot automatically grant or reveal `PASSIVE_SOC_0007`, `PASSIVE_SOC_0010` or any other passive.
- P14 provenance contract (blob `9c8281c7a893c4a8839914aedaf36b586161c229`) already separates occurrence, observer knowledge, publication, qualification and disclosure. OR-034 allows `PROVISIONAL_INTEGRATION` combat fixture contacts but no permanent faction/NPC promotion or raw/private tactical data crossing the player-safe bridge.

### A. Domain consequence/visibility integration matrix — DESIGN TEST ONLY

| D-072 event / observer situation | Durable authority that MAY decide a consequence | Player-safe result permitted **now** | Forbidden implicit cascade |
|---|---|---|---|
| Provisional encounter contact retreats or is defeated | Tactical encounter resolution plus separately approved durable GameState aftermath owner | Existing approved quest/story/Status-safe projection only | Generate `GameState.npcs` shell, V09 permanent adversary, `adversary_intel` public token, canon affiliation |
| A known NPC witnesses a real injury | Approved aftermath condition/memory transaction; social owner maintains NPC-private knowledge | None from NPC witness alone; additional player observation/knowledge permission needed | Leak injury severity, observer identity, relationship/private memory, faction rank |
| Jack performs authored training or combat technique | Existing progress/ability domain for specific allowed actions; future D-045 progression authority if approved | Existing D-066 ability and authored current training evidence only | Automatically award a class, `MENTOR_CAP_*`, profession grade, social reputation, known next secret requirement |
| A social consequence makes a private NPC impression | `social.py` owns relationship/memory and separate publication eligibility | Player-known outcome when explicitly authored; no globally public fact by default | Publish town consensus, qualify social passive, reveal `source_summary` or a private publication ledger |
| A passive already affects a current visible stat | Existing `state.perks` math + safe Status inspection | Approved stat contribution, with hidden attribution anonymized | Emit a new `status.passives` list, reverse-engineer hidden ID from numeric effect, invent hidden progress |
| Encounter produces no authoritative viewer observation | Encounter observer-local contact state only | No new player intel or hidden map marker | Use raw `CombatSession` or `state.npcs` as player knowledge or sneak new Kotlin DTO keys into current payload |

These are review rules inferred from the cited contracts, **not observed executions** of a D-072 implementation. Current absence of these target domains means a good D-072 implementation can legitimately do nothing in P16/P17/P18; that alone must not fail D-072 acceptance.

### B. Future non-owning regression suggestions (X-01..X-06)

1. **X-01 — transient-to-durable identity:** take OR-034 contact without `persistent_ref`, commit an otherwise valid aftermath and assert the persistent NPC ID set does not grow; a syntactically valid but absent permanent ref is rejected without mutation.
2. **X-02 — no automatic progressed role:** ordinary Trace Chamber or combat achievement cannot create `MENTOR_CAP_*`, `EVAL_CAP_*`, `PROF_*`, new class or civic reputation in durable records without a separately approved producer. Existing actual progress must remain unaffected.
3. **X-03 — observer-gated intel:** ensure observer A's legitimate detection does not reveal the enemy, its current hidden movement, condition or true faction to observer B/player; do not fabricate future `adversary_intel` domain.
4. **X-04 — separate passive reveal:** change only NPC-private social evidence; public/Status projection and passive list (currently absent) do not change; hidden `PERK_*` attribution stays `unidentified_modifier` even after save/load.
5. **X-05 — cross-owner late failure:** inject after a permitted durable side effect but before transaction completion; compare deep saved snapshot across player injury, quests, history, relationships, NPC memory, flags and time. No partial public safe view may survive.
6. **X-06 — future protocol evolution:** when P17/P18 are *actually* implemented, test unsupported `meta.projection_versions.adversary_intel` and proposed nested passive-domain version independently, with fail-closed behavior. Their current **proposed** version locations are different; only the future D-026/Android owner may choose the final shared negotiation/error policy.

### C. Explicit review verdict

- **CONSISTENT AT DESIGN LAYER:** each Wave-4 packet forbids treating a mere encounter, training signal, private knowledge, or rules-owned modifier as general permission to mint durable actors, titles, passives or public intel.
- **FUTURE DECISION, NOT VERIFIED DEFECT:** P17 proposes `meta.projection_versions.adversary_intel` while P18 sketches a nested `status.passives.projection_version`. Both are nonimplemented. Coordinate a single accepted compatibility/error model with the Android migration owner; do **not** file a CPR solely because the proposals differ.
- **NO CLAIMED TEST RESULT:** X-01..X-06 are candidate tests, not run tests or D-072 acceptance. No implementation branch/PR was found by the scoped `D-072`/`aftermath` PR and branch discovery checks; that is not proof Silex has no local work. Do not take over Silex's D-072 task.


### P11 / CPR-006 live-owner compatibility checkpoint (read-only)

This review's **cross-domain** aftermath plan must not assume the current Android session bridge is already publication-atomic. On the inspected authority source, `src/textrpg/android_bridge.py` (blob `73aa4c59edb18ef4c413976d5a71cdd2879a399e`) constructs the session with `self.state = content.state` and its `load()` performs `self.state = load_state(...); return self.scene_view()`. That is the already-reported CPR-006 state/publication issue; this review does **not** file a duplicate defect or repair it.

The live Bulletin's `Parallel P11 — D-076 precondition / CPR-006` entry remains **IN_PROGRESS / Nodus**, with [draft PR #80](https://github.com/jbob-coder/Text-rpg-game/pull/80) still **OPEN / unmerged** at this checkpoint. The normal task-row parser that matches only `TASK_REF: D-###` can miss P11's compound `D-076 PRECONDITION / CPR-006` task ref; account for this before saying D-072 is the only active work. Nodus's required RED/GREEN and merge-state acceptance control the fix, not any VA/X suggestions here.

**Future integration reviewer check:** verify the resolved P11 candidate's candidate-first validation and detached `AndroidGameSession.state` ownership at its *actual merged HEAD*, then separately verify D-072's all-or-nothing durable aftermath and its viewer-safe handoff. A successful tactical-session rollback does not prove Android load atomicity, and a fixed Android load does not prove D-072 aftermath rollback. Neither contract may be credited to this unexecuted documentation review.

**Editorial correction:** escaped Markdown backticks in the prior source-to-test matrix have been replaced by normal inline code delimiters; no test/source assertions, task owner, acceptance state or code were changed.
