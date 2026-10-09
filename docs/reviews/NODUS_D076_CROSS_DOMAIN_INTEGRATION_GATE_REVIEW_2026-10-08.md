# D-076 — cross-domain persistence and determinism integration review

**State:** NON-AUTHORITATIVE REVIEW / NOT A CLAIM / NOT AN ACCEPTANCE PACKET  
**Review role:** Nodus, integration architecture  
**Reviewed:** 2026-10-08 (AST)  
**Repository:** `jbob-coder/Text-rpg-game`, `docs/master-game-development-program`  
**Baseline HEAD observed immediately before preparing the review:** `f5c23f71c641f5a11d82e3d216149cb82902a90c`  
**Live authority:** `docs/AI_TASK_BULLETIN_BOARD.md` and `docs/THE_GAME_MASTER_TASK_REGISTER.md`; this note cannot unlock or claim tasks.

## 1. Why this review exists

D-076 requires **one exact-head integrated sequence** covering social/knowledge, progression, inventory/equipment, activity, quest and tactical aftermath, followed by save/reload/continue and deterministic regression proof. Existing subsystem acceptance tests are useful but do not, individually, establish that complete contract.

At the reviewed Bulletin blob `aea90a54eb2d56c716202b4ca12f283b72227567`, D-072 was IN_PROGRESS / Silex; D-073 and D-074 were BLOCKED; D-076 was BLOCKED; Wave-3 P11 / CPR-006 was IN_PROGRESS / Nodus; P15 / D-042 was IN_PROGRESS / Quorix; P12–P14 were DONE. **Zero READY/unclaimed primary tasks.** This review does not reopen any task or grant permission to modify a claimed implementation.

## 2. Current persistence boundary, proven by source inspection

- `src/textrpg/core.py` defines the authoritative `GameState` with player, flags, relationships, knowledge, inventory, quests, NPCs, party, abilities, equipment, perks, turn, time, history and schema version. `GameState.snapshot()` returns nested state references; a transaction rollback snapshot must be deep-copied rather than treated as detached merely because it is a new top-level mapping.
- `src/textrpg/persistence.py` defines `CURRENT_SCHEMA_VERSION = 1`, validates before dumping and after loading, serializes strict/sorted JSON, rejects unsupported schema versions and unknown top-level fields, and writes via a temporary file with replacement. The method `loads_state` validates state shape; it does not establish that `scene_id` exists in the currently authored content pack.
- `src/textrpg/android_bridge.py` (reviewed authority blob `73aa4c59edb18ef4c413976d5a71cdd2879a399e`) still assigns `self.state = content.state` at construction and publishes a deserialized state before `scene_view()` succeeds in `load()`. That **reviewed authority revision** has not yet incorporated the separate P11 repair, so its bridge-load post-validation atomicity cannot be considered fixed by this note.
- P11 / CPR-006 is a separate, actively claimed precondition. Its proposed branch repair is to detach the loaded state from the content template and validate the candidate before publication. The P11 owner must establish executed RED/GREEN, full suite, merge-state CI and accepted merge evidence before this precondition is closed.
- Tactical `CombatSession` is transient. The approved combat migration packet retains save schema v1 and requires durable aftermath to publish into existing `GameState` owners only after validation. Saving mid-combat must follow an expressly selected and tested policy; neither an implicit live tactical save nor a new top-level combat field is authorized here.

## 3. Source-to-proof map for the later D-076 owner

| Domain / boundary | Already present source/test lead | What the eventual integrated proof must additionally establish |
| --- | --- | --- |
| Player-safe scene, choices and load failure | `src/textrpg/android_bridge.py`; `tests/test_android_bridge.py` (`test_save_and_load_round_trip`, `test_load_failure_does_not_replace_current_state`) | On the merged P11 repair, reject a schema-valid unknown authored scene without changing state identity, data, or playable view. Verify success detaches the content template. |
| NPC relationship, private knowledge, memory | `src/textrpg/social.py`; `tests/test_social.py` | One actual authored interaction's permitted durable knowledge/relationship survives the same mid-run save and resume without disclosing NPC-private data. |
| Progression and techniques | `src/textrpg/progression.py`; `tests/test_progression.py`; `docs/systems/PHASE_1_PROGRESSION_SCHEMA_API_MIGRATION_PACKET.md` | Same continuation preserves discovered ability/technique, mastery/resource costs and visibility; never introduce a duplicate progression record. |
| Inventory and equipment | `tests/test_phase1_inventory_equipment_proof.py` (`test_phase1_item_equipment_story_loop_survives_two_save_boundaries`, `test_failed_equip_restores_full_authoritative_state`) | Verify inventory, equipped slot and derived effects after **the same** run's next quest/activity/combat outcome, not an isolated inventory fixture. |
| Time and activity | `src/textrpg/simulation.py`; `tests/test_phase1_activity.py` | Verify elapsed world minutes, stamina/focus, skill progression, activity history and time-sensitive condition expiry before and after reload. |
| Quest and authored social divergence | `tests/test_phase1_quest_branch_world_consequence.py` with cooperative/solo Dead Relay routes, `NPC_TAMSIN` memory and quest fingerprints | Capture quest stage, route, party, relationship/knowledge, and later legal authored options in a single replay; compare player-safe visibility separately from private state. |
| Encounter transient determinism and secrecy | `src/textrpg/combat_state.py`, `combat_rules.py`, `tests/test_combat_objectives.py`, `tests/test_combat_knowledge.py` | After D-073, execute one approved Gate Twelve fixture through the authoritative bridge, prove deterministic resolution/retreat and nonleakage; do not serialize raw combat session. |
| Durable combat aftermath | `docs/systems/INJURY_CONDITION_AFTERMATH_STANDARD.md` and future D-072 accepted tests | One validated aftermath transaction commits existing state owners or rolls back all writes, including history, world time, condition severity/duration, NPC state and quest/world consequences as applicable. |
| Full merge-state gate | `docs/AI_RUNTIME_MERGE_STATE_GATE.md`, `.github/workflows/android-pixel-client.yml` | Exact candidate SHA, PR merge SHA, Python+Android workflow outcomes, emulator/build artifacts where required, resulting authority HEAD and evidence references. |

This is a **mapping of existing test sources to required future proof**, not a claim that the proposed end-to-end test already exists or has passed.

## 4. Minimal deterministic test sequence (proposed, not executed)

1. Select the **currently authored** Gate Twelve story entry and known valid content pack. Fix the engine seed and declared route/choice sequence; explicitly document the approved D-073 provisional fixture instead of silently upgrading fixture names to canon.
2. Record checkpoint A: detached canonical `GameState` snapshot plus player-safe projection, including seed, scene, time, player resources, knowledge, relationships, inventory/equipment, quests, NPC memory, abilities, flags, conditions, and history.
3. Perform **one** valid social/knowledge transition, progression action, equipment transaction, time-cost activity and world-consequence quest branch **on this same state**. Verify each response came from the authoritative Python owner and contains only the permitted player-safe fields.
4. Save checkpoint B, close/recreate the session using the approved P11 semantics, reload and prove B matches the pre-save durable state. Resume a newly legal action and prove the legal choice/derived view is unchanged by the save boundary.
5. After D-072/D-073 are DONE, start the approved encounter, exercise a deterministic resolution or authorized retreat, and commit its aftermath. Verify that transient tactical contacts never become serialized NPC knowledge automatically and that only validated durable consequences enter `GameState`.
6. Save checkpoint C, reload, continue another authored action, and compare durable state/projection with a control run that did not save/reload at the intermediate checkpoints. Compare ordered history/event IDs only where the approved contract requires ordering; do not arbitrarily normalize away a genuine divergence.
7. Repeat the entire scenario with the same seed and choices, and compare a different-seed case where the engine contract intentionally varies. Record exact content pack hash, code commit and input/choice trace for reproducibility.
8. Apply fault injection on a detached candidate: rejected unsupported schema/unknown field, schema-valid unknown scene, invalid authored reference, invalid combat aftermath preflight, and post-write fault. Assert no partial durable change, no history duplication and stable public errors. Do not infer save-file crash consistency solely from `Path.replace`; filesystem-level guarantees require separate evidence.

**Checkpoint selection is conditional on legal authored content.** This document does not invent an unverified canonical full-route action order or assume Gate Twelve tactical integration exists before D-073.

## 5. Proof classification / exit checklist

- **EXISTING SOURCE-LEVEL CONTRACT:** `GameState` owner, strict schema-v1 persistence, existing subsystem tests and authored Dead Relay divergence fixture.
- **ACTIVE PRECONDITION:** P11 / CPR-006, separate Nodus execution ownership; candidate branch history or source review is not executable test evidence.
- **BLOCKED INTEGRATION:** D-072 aftermath acceptance -> D-073 bridge content -> D-074 Android tactical projection -> D-076 integrated sequence.
- **NOT YET EVIDENCED IN THIS REVIEW:** cross-domain uninterrupted vs save/reload replay equivalence; full post-aftermath persistence; actual RED/GREEN/CI on P11 and D-076; Android device/build performance.
- **FOR FUTURE D-076 ACCEPTANCE:** record exact branch/merge SHA, test names and commands, complete pass/fail counts, content ID/revision, expected and actual durable/projection fingerprints, one rejected-save result and an independent cross-domain nonleakage assertion.
- **HANDOFF:** re-fetch Bulletin and Master Register; wait until dependencies are DONE and a fresh claim is won before adding/running integrated tests or declaring acceptance. This review is not D-076 completion, D-076-B completion or a scoring event.

## 6. Read-first set

1. `docs/AI_TASK_BULLETIN_BOARD.md`, `docs/THE_GAME_MASTER_TASK_REGISTER.md` — live task/claim/semantic authority.
2. `docs/AI_RUNTIME_MERGE_STATE_GATE.md` — PR/CI completion requirements.
3. `docs/systems/PHASE_1_COMBAT_SCHEMA_API_MIGRATION_PACKET.md`, `docs/systems/INJURY_CONDITION_AFTERMATH_STANDARD.md` — tactical transient/durable boundary.
4. `docs/systems/PHASE_1_PROGRESSION_SCHEMA_API_MIGRATION_PACKET.md`, `docs/systems/SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md` — migration boundaries.
5. `src/textrpg/core.py`, `src/textrpg/persistence.py`, `src/textrpg/android_bridge.py` and the named `tests/` files — inspect actual current implementation before writing a new test.

**Verification performed for this note:** connector-backed repository file reads and task-state inspection only. **Not performed:** local Python/Gradle/Android execution, CI verification, content-playthrough execution, task claim, task-state changes, merge, or canon approval.

## 7. Queue changed after the source review

On the next live-board pass, Wave 4 opened. At observed board blob `8d81bd36df933839278feac70f420a3775711865`, **P16/D-045 was IN_PROGRESS / Veyra**, while **P17/D-026 and P18/D-046 were READY/unclaimed** and preferred for Kestrel and Veyr respectively. **P11/CPR-006 remained IN_PROGRESS / Nodus** and D-072 remained Silex-owned. The earlier zero-READY checkpoint in §1 is explicitly a historical observation, not a current queue claim.

This D-076 review changes neither Wave-4 task, reserves no claim, and should not be used to keep a READY lane unavailable. A later execution must re-fetch the live board rather than rely on either checkpoint.

## 8. Independent P11 PR #80 CI evidence checkpoint (2026-10-08 AST)

**Read-only source:** [P11/CPR-006 draft PR #80](https://github.com/jbob-coder/Text-rpg-game/pull/80), head `3b3ac9a5e8961f32a8140765d977d9c92a44b1e3`, base branch `docs/master-game-development-program`. The PR remains **OPEN / DRAFT / NOT MERGED** at this review. The PR API reported recorded base SHA `29d2a275640b08e230cd204763d3fd6711b4c469`; the authority branch had advanced beyond that recorded base by the later audit. Recompute merge-state evidence against the current live target before final acceptance.

**Observed workflow:** [Android Pixel Client run 37863439739](https://github.com/jbob-coder/Text-rpg-game/actions/runs/37863439739), pull_request event, run attempt 1, same head SHA, **completed / success**, with **3/3 jobs successful**:
- `python-engine` — success; workflow declares `PYTHONPATH=src python -m unittest discover -s tests -v`.
- `android-unit-and-assemble` — success; workflow declares Android unit tests, Compose instrumentation compilation, debug APK build and APK hash checks.
- `android-emulator-smoke` — success; workflow declares connected instrumentation smoke tests and screenshot verification.

**Important limits:** GitHub job and workflow conclusions are observed provider evidence, not local test execution by this review; individual logs/counts, screenshots, APK SHA and raw RED pre-fix test failure were **not** inspected. The workflow's successful head does **not** independently prove the PR can merge cleanly against the **latest** authority HEAD. It also does not close P11: the canonical Bulletin and Nodus Drive still report P11 IN_PROGRESS. Do not infer implementation task handoff, acceptance or score from this independent documentation checkpoint.

**Consumer shortcut:** D-076 later should link accepted P11 completion evidence (including the correct merged authority SHA and stable `LOAD_ERROR` RED/GREEN tests), not cite this draft PR as final source of truth. Re-run the live Bulletin/PR/workflow check when P11 changes.
