# THE GAME — Player Learning Ledger

**Status:** ACTIVE / APPEND-ONLY HANDOFF SURFACE  
**Purpose:** preserve task-derived knowledge so later Player-AIs do not repeat repository archaeology.

Do not use this file as semantic authority. Every entry must point back to live authority/source/evidence.

## Required entry format

```md
### <TASK> — <short lesson title>
- PLAYER-AI:
- AUTHORITY / COMPLETION HEAD:
- READ FIRST:
- DO NOT REDISCOVER:
- OWNER OF BEHAVIOR:
- TRAP / FALSE ASSUMPTION:
- VALIDATE WITH:
- CHANGE SAFELY:
- STILL UNKNOWN / BLOCKED:
- NEXT PLAYER SHORTCUT:
- SUPPORTING ARTIFACT:
```

## First-wave backfill

D-080 owns the initial backfill from the first Player-AI generation.

The backfill should cover at minimum one meaningful completed work area from:
- Nodus;
- Veyra;
- Kestrel;
- Veyr.

Do not invent lessons on their behalf. Derive each record from committed task evidence, Brag Cards, source/tests and exact verification.

## Entries

No synthetic entries are added at creation time. Add only evidence-backed lessons.


### D-067 — Inventory/equipment authority and bridge-transition lesson
- PLAYER-AI: Nodus
- AUTHORITY / COMPLETION HEAD: `0fd843a5ece0f87c74a262c7ecb6739d025b0678`; checkpoint PR #65 / run `37253975755`.
- READ FIRST: `docs/evidence/D067_PHASE1_INVENTORY_EQUIPMENT_PROOF_2026-10-04.md`; `docs/evidence/CRITICAL_FIX_D067_BRIDGE_RECONCILIATION_2026-10-04.md`; `src/textrpg/equipment.py`; `tests/test_phase1_inventory_equipment_proof.py`.
- DO NOT REDISCOVER: Phase 1 already proves obtain/possess/equip/use, two save boundaries, player-safe Android inventory/equipment presentation, and invalid-equip full rollback. The transition bridge incident was merge-state/API contract drift, not a reason to invent a second inventory owner.
- OWNER OF BEHAVIOR: `GameState.inventory` / `GameState.equipment`; `src/textrpg/equipment.py::equip_item`; versioned persistence; Android bridge only requests mutation and projects the returned authoritative state.
- TRAP / FALSE ASSUMPTION: stale bridge signatures can make an inventory failure look like an equipment-rule failure. CPR-001 showed obsolete `advance_time` / `equip_item` calls, cheat compatibility, room projection and test-runner drift were one integration incident.
- VALIDATE WITH: evidence above; exact green checkpoint PR #65 / run `37253975755`; repository recipe `PYTHONPATH=src python -m unittest discover -s tests -v` when revalidating current HEAD.
- CHANGE SAFELY: extend authored item definitions and the authoritative equipment API first; keep Compose/Kotlin presentation arithmetic-free; add rollback coverage for new failure modes.
- STILL UNKNOWN / BLOCKED: full economy/vendor/crafting/durability/encumbrance/item-instance systems and physical-device validation are not proven by D-067.
- NEXT PLAYER SHORTCUT: before touching Android inventory/equipment glue, read CPR-001; then inspect `equip_item`'s current signature instead of reconstructing it from old tests.
- SUPPORTING ARTIFACT: `docs/evidence/D067_PHASE1_INVENTORY_EQUIPMENT_PROOF_2026-10-04.md`.

### D-068 — Trace Chamber activity is an authored choice over simulation authority
- PLAYER-AI: Veyra
- AUTHORITY / COMPLETION HEAD: `e883205559c64d2e82614160bd6548c2c9332808`.
- READ FIRST: `docs/evidence/D068_PHASE1_ACTIVITY_PROOF_2026-10-04.md`; `src/textrpg/simulation.py`; `tests/test_phase1_activity.py`; the `TRAIN_POWER_FUNDAMENTALS_TWO_HOURS` choice in `content/vertical_slice_01.json`.
- DO NOT REDISCOVER: Phase 1 requirement #8 already uses the existing Trace Chamber choice. For the proved route, 120 minutes at intensity 1 costs 16 stamina and 10 focus and raises Powers from zero to 2.0; save/load and failure atomicity are covered.
- OWNER OF BEHAVIOR: `src/textrpg/simulation.py::train` owns time/resource/progress arithmetic; `RulesEngine.choose` owns the authored transaction/rollback boundary; Android forwards the choice ID and maps returned values.
- TRAP / FALSE ASSUMPTION: do not create an activity registry or calculate costs in Android merely because the activity is presented as a UI choice. The Phase 1 proof deliberately reuses normal authored-choice dispatch.
- VALIDATE WITH: `tests/test_phase1_activity.py`; PR #59 / run `37252547112` for task-local proof; current-head aggregate verification should use the standard Python/Android gates rather than inferring from that historical run.
- CHANGE SAFELY: add a new authored activity through existing semantic effects when its mechanic matches; change `simulation.py` only when the authoritative rule itself differs.
- STILL UNKNOWN / BLOCKED: full jobs/professions/scheduling, resumable/background/offline activities, activity-specific Android preview UX and physical-device validation remain outside D-068.
- NEXT PLAYER SHORTCUT: use `TRAIN_POWER_FUNDAMENTALS_TWO_HOURS` as the reference path before designing any new activity subsystem.
- SUPPORTING ARTIFACT: `docs/evidence/D068_PHASE1_ACTIVITY_PROOF_2026-10-04.md`.

### Parallel P2 / D-029 — Historical asset absence must stay distinct from current reconstruction tooling
- PLAYER-AI: Kestrel
- AUTHORITY / COMPLETION HEAD: `b4694ab7a103a729780825c40807fba346ffd026` for the completed PR #19 provenance slice.
- READ FIRST: `docs/assets/PR19_RASTER_EXPORTER_PROVENANCE_AUDIT_2026-10-04.md`; `docs/assets/RASTER_EXPORT_AND_SOURCE_CORRESPONDENCE_2026-10-03.md`; `tools/verify_pixel_raster_equivalence.py`; `tests/test_pixel_raster_equivalence_tool.py`.
- DO NOT REDISCOVER: PR #19 head `c11133122d47009abc71e8c6e91c08aedbe91ae2` contains the delivered PNG consumer set but no committed exporter/generator/tool/script. The repository-owned equivalence verifier is a replacement reconstruction tool, not recovered historical tooling.
- OWNER OF BEHAVIOR: current pixel source/raster runtime ownership lives in the Android pixel catalogs/consumers; D-029 provenance documents explain lineage but do not authorize visual promotion or asset replacement.
- TRAP / FALSE ASSUMPTION: “exporter not found” used to sound like an incomplete search. Exact PR-head inspection closed that ambiguity. Do not resume repository archaeology looking for an exporter inside PR #19.
- VALIDATE WITH: `docs/assets/PR19_RASTER_EXPORTER_PROVENANCE_AUDIT_2026-10-04.md` and its exact-head Git evidence. This completed slice was a repository audit, not a runtime/build pass; fresh raster equality must be executed separately when the environment allows it.
- CHANGE SAFELY: retain source/provenance first; trace current consumer/reachability and owner decision before replacing or deleting an asset; use the current deterministic equivalence verifier for reconstruction checks.
- STILL UNKNOWN / BLOCKED: the broader D-029 program remains open for fresh 24/24 equivalence execution, visual owner-promotion decisions, final portraits/actors, destination visual QA and physical-device QA.
- NEXT PLAYER SHORTCUT: stop searching PR #19 for a missing exporter; start with the current lineage record and verifier, and keep historical provenance separate from present-day reconstruction tooling.
- SUPPORTING ARTIFACT: `docs/assets/PR19_RASTER_EXPORTER_PROVENANCE_AUDIT_2026-10-04.md`.

### D-075 — Persistent quest divergence lives beyond quest status
- PLAYER-AI: Veyr
- AUTHORITY / COMPLETION HEAD: `ad5767d312d9e6fef4b34c0f3cfa339c378826a4`; PR #66 / run `37254171985`.
- READ FIRST: `docs/evidence/D075_PHASE1_QUEST_BRANCH_WORLD_CONSEQUENCE_2026-10-04.md`; `tests/test_phase1_quest_branch_world_consequence.py`; `tests/fixtures/d075_dead_relay_branch_diff.json`; relevant `QUEST_DEAD_RELAY` / Tamsin branches in `content/vertical_slice_01.json`.
- DO NOT REDISCOVER: cooperative and solo Dead Relay resolutions both complete the same quest and survive save/load/navigation to the same later checkpoint. Their meaningful divergence is durable route/NPC/social state plus the cooperative-only player-safe `ASK_TAMSIN_ABOUT_SHARED_ENTRY` choice.
- OWNER OF BEHAVIOR: authored branch conditions/effects in `content/vertical_slice_01.json` execute through Python authoritative state; Tamsin knowledge/memory/story/relationship state remains private; the bridge projects only the allowed later consequence.
- TRAP / FALSE ASSUMPTION: comparing quest status/stage alone makes the two resolutions look equivalent. The proof must compare the normalized durable branch fingerprint and separately verify that private memory identifiers never cross the player-safe projection.
- VALIDATE WITH: `tests/test_phase1_quest_branch_world_consequence.py`; fixture `tests/fixtures/d075_dead_relay_branch_diff.json`; PR #66 / run `37254171985` (Python 349 OK, Android unit/build/package PASS, emulator smoke/screenshots PASS).
- CHANGE SAFELY: preserve stable IDs; update authored semantic consequences and the normalized fixture intentionally; keep private NPC state behind engine-owned conditions instead of exposing it for UI branching.
- STILL UNKNOWN / BLOCKED: broader D-076 integrated persistence/determinism and later tactical-chain consequences remain separate work; D-075 does not prove every quest branch in the game.
- NEXT PLAYER SHORTCUT: when changing this quest, compare the cooperative/solo branch fingerprints before and after your edit; do not use terminal quest status as the branch-equivalence test.
- SUPPORTING ARTIFACT: `docs/evidence/D075_PHASE1_QUEST_BRANCH_WORLD_CONSEQUENCE_2026-10-04.md`.


### D-080 — Learning-system handoff is navigation, not authority
- PLAYER-AI: Veyr
- AUTHORITY / COMPLETION HEAD: `9526fcbead1a37f4d1b0faaf8e3500e539efa691`.
- READ FIRST: `docs/player_guide/README.md`; `docs/player_guide/PLAYER_LEARNING_LEDGER.md`; `docs/player_guide/FIRST_WAVE_FAST_PATH_AUDIT_2026-10-04.md`; `AGENTS.md`.
- DO NOT REDISCOVER: the five-file fast path is sufficient to enter most bounded tasks. D-080 already backfilled one evidence-backed lesson each from Nodus, Veyra, Kestrel and Veyr and validated 15/15 task-local links.
- OWNER OF BEHAVIOR: semantic behavior remains owned by each task/domain's actual source and authority. The field guide and Learning Ledger are navigation/handoff surfaces only.
- TRAP / FALSE ASSUMPTION: a useful learning note can accidentally become a second authority if it restates mechanics instead of linking to the owning source/evidence. Keep records compact and explicitly subordinate to live authority.
- VALIDATE WITH: `docs/player_guide/FIRST_WAVE_FAST_PATH_AUDIT_2026-10-04.md`; D-080 acceptance HEAD `9526fcbead1a37f4d1b0faaf8e3500e539efa691`.
- CHANGE SAFELY: append one compact record after a completed primary task; link the smallest authoritative/source/evidence set; correct stale records explicitly rather than copying status into more documents.
- STILL UNKNOWN / BLOCKED: D-080-B machine-readable ownership map was intentionally not added; create it only when a real consumer/consistency check justifies another maintained artifact.
- NEXT PLAYER SHORTCUT: start with `docs/player_guide/README.md`, then search this Ledger for your task/domain before opening master documents.
- SUPPORTING ARTIFACT: `docs/player_guide/FIRST_WAVE_FAST_PATH_AUDIT_2026-10-04.md`.


### Integration review — evidence reuse is not merge-candidate approval
- PLAYER-AI: Nodus
- AUTHORITY / OBSERVED HEAD: refined during the D-064 coordination upgrade; always re-fetch the live Bulletin and task authority before applying this shortcut.
- READ FIRST: `docs/AI_RUNTIME_MERGE_STATE_GATE.md`; OR-019 in `docs/PROJECT_OVERSEER_DECISION_LOG.md`; the live task entry; any task-specific integration manifest.
- DO NOT REDISCOVER: two independent questions exist: **(1) may prior executed evidence be reused?** and **(2) is that PR the patch we should merge?** OR-019 may answer yes to the first while scope/merge hygiene answers no to the second.
- OWNER OF BEHAVIOR: OR-019 owns evidence-reuse conditions; `docs/AI_RUNTIME_MERGE_STATE_GATE.md` owns runtime integration completion; the task's Master Register/Bulletin entry identifies the current merge candidate.
- TRAP / FALSE ASSUMPTION: D-064 PR #63 run #354 is fully green and reusable compatibility evidence because synthetic merge `ee497f2` tested the task against authority `b2849f24...` and later drift is documentation/governance only. It is still **not** the final merge candidate because AXIOM's `D064_LIVE_AUTHORITY_SURGICAL_REBASE_MANIFEST_2026-10-04.md` rejects its unrelated presentation compaction churn. PR #68 is RED contract evidence, not a replacement merge candidate.
- VALIDATE WITH: PR #63 run #354 / `37257967729`; synthetic merge `ee497f2`; compare authority drift after `b2849f24...`; OR-019; `docs/evidence/D064_LIVE_AUTHORITY_SURGICAL_REBASE_MANIFEST_2026-10-04.md`.
- CHANGE SAFELY: record both **EVIDENCE_CLASS** and **PR_ROLE** for multi-PR runtime tasks. Reuse passing behavior evidence when policy permits, but merge only the branch explicitly selected as the current completion candidate.
- STILL UNKNOWN / BLOCKED: D-064 remains IN_PROGRESS until Kestrel's fresh surgical current-authority branch passes merge-state CI and the handoff is synchronized.
- NEXT PLAYER SHORTCUT: before arguing over a green/red PR, ask two questions in order: “Can I reuse this run?” then “Is this the branch we actually want in authority?”
- SUPPORTING ARTIFACT: `docs/evidence/D064_LIVE_AUTHORITY_SURGICAL_REBASE_MANIFEST_2026-10-04.md`.

### Coordination — Multi-PR tasks need explicit evidence roles
- PLAYER-AI: Veyra
- AUTHORITY / COMPLETION HEAD: coordination upgrade observed through live authority `16b6b1830d4d2b6752d281890f65ae594c932963`; this is an operational learning record, not gameplay completion evidence.
- READ FIRST: `docs/AI_TASK_BULLETIN_BOARD.md` current task block; `docs/AI_COORDINATION_ROOM.md` Multi-PR task rule; `docs/AI_RUNTIME_MERGE_STATE_GATE.md`; the owning Mission Control card.
- DO NOT REDISCOVER: one task may legitimately have several PRs with different purposes. D-064 demonstrated three distinct states: PR #68 is expected-RED contract evidence, PR #63 is fully green diagnostic evidence but stale/over-broad, and the actual current-authority merge candidate does not yet exist.
- OWNER OF BEHAVIOR: task ownership/unlock remains the Bulletin; completion semantics remain the Master Task Register + runtime merge-state gate; GitHub PR/run state is evidence, not task authority by itself.
- TRAP / FALSE ASSUMPTION: “green PR = task complete” is false when the PR base is stale, the patch is not the intended minimal merge candidate, or the Bulletin handoff has not occurred. Conversely, an intentional RED contract PR is not necessarily a regression.
- VALIDATE WITH: compare PR base/head to live authority; inspect the owning Bulletin block and Mission card; for D-064 reference PR #63 run #354 / `37257967729` (DIAGNOSTIC_GREEN) and PR #68 run #355 / `37258411701` (INTENTIONAL_RED).
- CHANGE SAFELY: label each relevant PR as RED_CONTRACT_ONLY, DIAGNOSTIC_GREEN, MERGE_CANDIDATE or SUPERSEDED in coordination updates; keep exactly one current next move and one current completion candidate.
- STILL UNKNOWN / BLOCKED: D-064's final merge candidate and completion head are not yet established; do not infer them from #63/#68.
- NEXT PLAYER SHORTCUT: before reading CI details for a multi-PR task, ask “which PR is the merge candidate against current authority?” If the answer is none, the next move is to build one rather than interpret historical PR color as completion.
- SUPPORTING ARTIFACT: `docs/AI_COORDINATION_ROOM.md` Multi-PR task rule; live D-064 Bulletin/Mission entries.

### Coordination correction — PR evidence roles can be reclassified after exact drift audit
- PLAYER-AI: Veyra
- AUTHORITY / COMPLETION HEAD: correction observed at live authority `f8933278d9ae81b6cb8d4c4e337309aaa96efe62`; this corrects the earlier “Multi-PR tasks need explicit evidence roles” note without deleting historical context.
- READ FIRST: `docs/PROJECT_OVERSEER_DECISION_LOG.md` OR-019; `docs/AI_RUNTIME_MERGE_STATE_GATE.md`; current D-064 Bulletin/Mission entries; `docs/AI_COORDINATION_ROOM.md` Multi-PR task rule.
- DO NOT REDISCOVER: PR/evidence classifications are not frozen forever. After the earlier note, D-064 PR #63 was re-audited against a synthetic merge into authority `b2849f248ff3e924653e68df5ddc492b71563a02`; run #354 had already executed the relevant tests green, and later drift was governance/documentation only. That made OR-019 evidence reuse applicable and allowed #63 to become the current D-064 GREEN merge-state candidate even though it had previously been treated as diagnostic-only.
- OWNER OF BEHAVIOR: OR-019 governs evidence reuse; `docs/AI_RUNTIME_MERGE_STATE_GATE.md` governs runtime completion; the Bulletin records current task/evidence disposition.
- TRAP / FALSE ASSUMPTION: “once diagnostic, always diagnostic” is as wrong as “green PR means DONE.” Reclassification is valid only with explicit ancestry, executed-test and implementation/contract-drift proof.
- VALIDATE WITH: OR-019; D-064 Bulletin `EVIDENCE_CLASS`; PR #63 run #354 / `37257967729`; synthetic merge `ee497f2` into authority `b2849f248ff3e924653e68df5ddc492b71563a02`; post-run drift audit recorded on the live D-064 entry.
- CHANGE SAFELY: record PR role separately from evidence class; update current coordination surfaces when proof changes the class; never edit old Coordination Room messages, and correct Learning Ledger notes append-only.
- STILL UNKNOWN / BLOCKED: D-064 is still not DONE until Kestrel completes merge + evidence/Learning/Brag/Scoreboard/Bulletin handoff. D-069 remains blocked until that synchronized handoff.
- NEXT PLAYER SHORTCUT: when a stale-looking green PR is reconsidered, check OR-019 criteria and the runtime/test diff since the tested merge state before demanding a rerun or discarding valid evidence.
- SUPPORTING ARTIFACT: `docs/PROJECT_OVERSEER_DECISION_LOG.md` OR-019; current D-064 Bulletin/Mission entries.



### COORDINATION — Green CI validity and merge acceptability are separate
- PLAYER-AI: Veyr
- AUTHORITY / COMPLETION HEAD: coordination lesson captured during the D-064 Bulletin-area upgrade; use live HEAD rather than this record for task state.
- READ FIRST: `docs/AI_TASK_BULLETIN_BOARD.md` D-064 entry; `docs/AI_RUNTIME_MERGE_STATE_GATE.md`; `docs/evidence/D064_LIVE_AUTHORITY_SURGICAL_REBASE_MANIFEST_2026-10-04.md`.
- DO NOT REDISCOVER: PR #63 run #354 was not a branch-only test. CI checked out synthetic merge `ee497f2`, merging D-064 head `c8268ea...` into authority `b2849f24...`, and all three jobs passed. Later drift from that authority point was documentation/governance-only at audit time, so the run remains valid compatibility evidence under OR-019.
- OWNER OF BEHAVIOR: the Bulletin owns task/claim state; `AI_RUNTIME_MERGE_STATE_GATE.md` owns runtime evidence semantics; the current task evidence/manifest owns the selected merge recipe. The Coordination Room only communicates these facts.
- TRAP / FALSE ASSUMPTION: neither “newest PR number” nor “green CI” tells you which PR should merge. PR #68 is newer but intentional RED evidence. PR #63 is green but carries avoidable compaction churn, so AXIOM selected a fresh surgical branch for final integration.
- VALIDATE WITH: workflow run #354 / `37257967729`; checkout log `HEAD is now at ee497f2 Merge c8268ea... into b2849f24...`; compare authority drift after `b2849f24...`; the live D-064 surgical manifest.
- CHANGE SAFELY: label each open PR by role—completion candidate, compatibility/diagnostic green, intentional RED, or historical—and state separately whether evidence is valid and whether the diff is acceptable to merge.
- STILL UNKNOWN / BLOCKED: D-064 remains IN_PROGRESS until Kestrel's fresh surgical live-authority branch passes merge-state CI and completes the evidence/Learning Ledger handoff.
- NEXT PLAYER SHORTCUT: when several PRs exist for one task, inspect the workflow checkout merge SHA and task manifest before following PR chronology; do not restart a proven repair merely because the latest PR is red.
- SUPPORTING ARTIFACT: `docs/evidence/D064_LIVE_AUTHORITY_SURGICAL_REBASE_MANIFEST_2026-10-04.md`.


### COORDINATION — Surgical file count does not prove a surgical diff
- PLAYER-AI: Nodus
- AUTHORITY / OBSERVED HEAD: `1c8fd61e782ce9f72f1744480cddadda20e76c02` during the D-064 Bulletin-area coordination audit.
- READ FIRST: `docs/AI_TASK_BULLETIN_BOARD.md` D-064; `docs/evidence/D064_LIVE_AUTHORITY_SURGICAL_REBASE_MANIFEST_2026-10-04.md`; `docs/AI_RUNTIME_MERGE_STATE_GATE.md`; `docs/overseer/code_problems/CPR-002_d064_room_actor_unknown_field_strictness.md`.
- DO NOT REDISCOVER: a branch can touch exactly the intended file set and still be unsafe to call “surgical.” `agent/kestrel-d064-surgical-final` at `8a414bccf6a0046a783498a5e2550cba85966e8f` changed the intended five files, but its `GameScreen.kt` diff was 403 additions / 788 deletions when only two projected-actor call-site wires were required.
- OWNER OF BEHAVIOR: the D-064 semantic delta is owned by Kestrel's active task and the surgical manifest; branch names/file counts are coordination metadata, not implementation authority.
- TRAP / FALSE ASSUMPTION: “five-file branch” or a branch named “surgical-final” is not evidence that the diff is minimal. Inspect per-file diff magnitude and semantic anchors before approving a merge candidate.
- VALIDATE WITH: compare the candidate branch to live authority; verify the exact manifest anchors; then use current merge-state CI. Keep compatibility evidence (PR #63/run #354), RED contract evidence (PR #68/runs #355/#356), and final merge-candidate evidence as separate classes.
- CHANGE SAFELY: rebuild from current authority when a supposedly surgical file contains broad formatting/compaction churn; transplant only the semantic changes required by the manifest.
- STILL UNKNOWN / BLOCKED: D-064 remains IN_PROGRESS. `CPR-002` is now **ACCEPTED / LINKED TO D-064 / 74/100 CRITICAL** and requires executable JVM RED -> GREEN before handoff; no current user-visible privacy leak is proven.
- NEXT PLAYER SHORTCUT: before calling any integration branch “surgical,” inspect both the file list and the changed-line footprint; if one file is unexpectedly huge, stop and reconstruct the semantic patch from live authority instead of rebasing the churn.
- CURRENT FOLLOW-UP: Kestrel subsequently corrected the `GameScreen.kt` churn at branch head `9c38bb0df9af9dfc9d376c868883299949fd47dd` (3 additions / 1 deletion versus authority). That correction reinforces the lesson: re-fetch the candidate before repeating an old warning; remaining observed gates are branch freshness, fallback-scene regression coverage, and CPR-002 RED -> GREEN.
- SUPPORTING ARTIFACT: `docs/evidence/D064_LIVE_AUTHORITY_SURGICAL_REBASE_MANIFEST_2026-10-04.md`.

### D-081 — Repository status is a reproducible view, not a second authority
- PLAYER-AI: Nodus
- AUTHORITY / COMPLETION CONTEXT: D-081 owner-directed repository-wide status mapping and tracker.
- READ FIRST: `docs/PROJECT_STATUS_TRACKING_STANDARD.md`; `tools/project_status_tracker.py`; `docs/THE_GAME_MASTER_TASK_REGISTER.md`; D-019 inventory authority.
- DO NOT REDISCOVER: repository counts and completion percentages must be bound to one exact Git commit. The conservative project percentage is DONE task-register entries divided by all registered TASK D-### entries; file/document counts do not prove semantic completion.
- OWNER OF BEHAVIOR: Git owns exact structural state; the Master Task Register owns task state; D-019 owns detailed corpus inventory; D-081 only aggregates those authorities for reporting.
- TRAP / FALSE ASSUMPTION: a dashboard can become a stale competing authority if its numbers are hand-edited or detached from a source HEAD. Another trap is treating 67% task completion as 67% of total game content or remaining engineering effort.
- VALIDATE WITH: `python tools/project_status_tracker.py --revision <SHA> --json-output /tmp/status.json --markdown-output /tmp/status.md`; `tests/test_project_status_tracker.py`; compare source_head to the intended repository revision.
- CHANGE SAFELY: add metrics only when their source authority and exact definition are explicit; keep historical snapshots immutable to their source HEAD; regenerate rather than patching numbers manually.
- STILL UNKNOWN / BLOCKED: task counts are unweighted; they intentionally do not estimate remaining effort. Runtime/build/device health still requires separate exact-head evidence.
- NEXT PLAYER SHORTCUT: when asked “how complete is the project?”, run or reproduce the D-081 tracker first, report the task-register percentage plus Phase 1 percentage and document counts, then separately describe critical blockers from live authority.
- SUPPORTING ARTIFACT: `docs/evidence/D081_PROJECT_STATUS_BASELINE_2026-10-05.json`.


### D-082 — Track every path, and always name the comparison base
- PLAYER-AI: Nodus
- READ FIRST: \`docs/PROJECT_STATUS_TRACKING_STANDARD.md\` §§10–11; \`tools/project_status_tracker.py\`; \`docs/evidence/D082_FULL_REPOSITORY_MANIFEST_2026-10-05.json\`.
- DO NOT REDISCOVER: aggregate counts are not enough for "track everything." The tracker now emits one manifest entry per tracked blob and can compare two exact revisions for file/document additions, removals, changes, task additions/removals, task transitions and completion movement.
- OWNER OF BEHAVIOR: Git revisions own path/blob truth; Master Task Register owns semantic task state; D-019 owns detailed corpus inventory; D-081/D-082 provide reporting views.
- TRAP / FALSE ASSUMPTION: "documents created" is meaningless without a base revision. A path rename is also not automatically semantic continuity; structural comparison sees one removal and one addition unless separately reconciled.
- VALIDATE WITH: \`python tools/project_status_tracker.py --base-revision <OLD> --revision <NEW> --manifest-output /tmp/manifest.json --json-output /tmp/status.json\`; synthetic Git validation and exact connector tree evidence are recorded in the D-082 evidence JSON.
- CHANGE SAFELY: never mutate old snapshots to look current. Generate a new exact-revision report/manifest and compare explicit commits.
- STILL UNKNOWN / BLOCKED: this is structural tracking, not an effort-weighted project forecast. Runtime health still needs fresh test/build/device evidence.
- NEXT PLAYER SHORTCUT: for owner status requests, report current totals first, then use the latest accepted snapshot as the named comparison base to say exactly how many documents/files/tasks changed.
- SUPPORTING ARTIFACT: \`docs/evidence/D082_FULL_REPOSITORY_MANIFEST_2026-10-05.json\`.


### D-064 — Projected room actors replace presentation heuristics
- **PLAYER-AI:** Kestrel
- **AUTHORITY / COMPLETION HEAD:** authority merge `d7ebb7ca439695e256a429a1e5d160daae69a521`; final tested PR head `014e05c9f5e451d8fb9eb552a9ba20e7cd1ed5ff`.
- **READ FIRST:** `docs/evidence/D064_PLAYER_SAFE_ROOM_ACTOR_PROJECTION_FINAL_2026-10-05.md`; `docs/android/PLAYER_SAFE_ROOM_ACTOR_PROJECTION_CONTRACT.md`; `android/app/src/main/java/com/thegame/rpg/engine/GameEngine.kt`; `android/app/src/main/java/com/thegame/rpg/ui/PixelStoryActorCatalog.kt`; `android/app/src/main/java/com/thegame/rpg/ui/SceneIllustration.kt`.
- **DO NOT REDISCOVER:** story-actor presence is no longer inferred from scene/location IDs in the Android catalog. Presence comes from `snapshot.room.actors`; `visualFamily` selects the sprite; `placementKey` selects semantic coordinates. Platform Nine, Relay Workbench and Service Tunnel equivalence are already tested.
- **OWNER OF BEHAVIOR:** Python owns authoritative player-safe room projection; `BridgeSnapshotMapper` owns strict Kotlin mapping; `PixelStoryActorCatalog` owns player-safe visual-family-to-sprite mapping; `PixelStoryActorPlacementResolver` owns semantic placement coordinates.
- **TRAP / FALSE ASSUMPTION:** a green branch is not automatically a good merge candidate. Earlier D-064 PRs passed CI but carried unrelated formatting/compaction churn. The final candidate was rebuilt as a seven-file surgical diff. Another trap: typed extraction is not the same as strict unknown-key rejection; CPR-002 proved Android silently accepted forbidden extra actor keys until the allowlist was added.
- **VALIDATE WITH:** PR #70 / workflow run #362 / `37261943012`; Python 355 tests OK; Android unit/build/package PASS; emulator smoke/screenshots PASS; APK SHA-256 `1d1c974dba2a65ac94d3ac5bfa9b60f8725d360c01eab9b4a36add7f9133bb46`.
- **CHANGE SAFELY:** extend authored/player-safe room actor data in Python first, update the documented actor contract, then update the strict Kotlin allowlist/typed mapper and focused tests. Do not add scene/location presence heuristics back into Compose.
- **STILL UNKNOWN / BLOCKED:** no physical-device acceptance is claimed here. Dynamic world-position authority remains outside D-064; `placementKey` is a presentation adapter, not durable simulation coordinates.
- **NEXT PLAYER SHORTCUT:** if an actor should appear or move, start by asking “is this actor in the player-safe room projection?”—do not patch `PixelStoryActorCatalog` with another scene-ID special case.
- **SUPPORTING ARTIFACT:** `docs/evidence/D064_PLAYER_SAFE_ROOM_ACTOR_PROJECTION_FINAL_2026-10-05.md`; CPR-002 for the strict-key lesson.


### P5 / D-042 — Raster-first presentation changes the migration unit
- **PLAYER-AI:** Quorix
- **AUTHORITY / AUDIT HEAD:** `f5c3731d0c494dd3948f88481a3d5b2d3d0f4138`; P5 evidence accepted as a bounded cross-branch audit, not runtime promotion.
- **READ FIRST:** `docs/evidence/P5_D042_CROSS_BRANCH_SURVIVOR_AUDIT_2026-10-05.md`; `docs/IMPLEMENTATION_PR_7_31_RECONCILIATION_2026-10-02.md`; `android/app/src/main/java/com/thegame/rpg/ui/PixelRasterCatalog.kt`; `android/app/src/main/java/com/thegame/rpg/ui/SceneIllustration.kt`; `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`.
- **DO NOT REDISCOVER:** D-064, D-065/D-068 and D-067 completion heads are in authority ancestry. The still-divergent visual survivor slice is PR #27/#28/#30/#31. #27/#30 static scene source+raster pairs remain D-029 candidates; #28 is a deferred arrival-preview composition; #31 is an ambient-animation candidate that must be reimplemented before migration.
- **OWNER OF BEHAVIOR:** `PixelRasterCatalog.scene(locationId)` owns the primary current scene-raster binding; `SceneIllustration` renders that raster first; `PixelSceneCatalog` is fallback geometry. D-029 owns asset provenance/visual promotion. D-077/later V11 presentation owns future Android consumption where applicable.
- **TRAP / FALSE ASSUMPTION:** changing `PixelSceneCatalog` alone does not necessarily change the visible Service Tunnel or Quiet Stair. Current rendering is raster-first, so a code-only transplant can look integrated while the player still sees the old PNG. Also, PR #31 advances ambient loops but does not implement the required reduced-motion path.
- **VALIDATE WITH:** compare PR heads #27 `d19e6edb...`, #28 `b5cb5104...`, #30 `7adacd47...`, #31 `19807863...` to exact authority; inspect current raster bindings and `SceneIllustration`; parse `docs/evidence/P5_D042_CROSS_BRANCH_SURVIVOR_MATRIX_2026-10-05.json`.
- **CHANGE SAFELY:** migrate a selected static scene as one source-master + raster + binding + tests/provenance unit. Reimplement #31 only after the static survivor is chosen and add explicit reduced-motion/lifecycle evidence. Never merge an old visual branch wholesale because it is newer.
- **STILL UNKNOWN / BLOCKED:** no visual/canon winner is selected by P5; raster equivalence and owner visual approval remain D-029 boundaries. No runtime/build/emulator/device evidence was produced by this audit.
- **NEXT PLAYER SHORTCUT:** before migrating any old presentation branch, ask “what file actually renders first on authority?” and identify the complete migration unit before comparing aesthetics.
- **SUPPORTING ARTIFACT:** `docs/evidence/P5_D042_CROSS_BRANCH_SURVIVOR_AUDIT_2026-10-05.md`; machine-readable companion `docs/evidence/P5_D042_CROSS_BRANCH_SURVIVOR_MATRIX_2026-10-05.json`.

### D-069 — Tactical schemas and pure grid core
- PLAYER-AI: Veyra
- COMPLETION HEAD: `8b2115cf8a6f04127bdf20dd1217abd947cf8150`
- READ FIRST: `docs/evidence/D069_TACTICAL_SCHEMA_GRID_CORE_FINAL_2026-10-05.md`; `docs/evidence/D070_TRANSIENT_COMBAT_PREFLIGHT_2026-10-05.md`; `src/textrpg/combat_schema.py`; `src/textrpg/combat_grid.py`; `tests/test_combat_schema.py`; `tests/test_combat_grid.py`.
- DO NOT REDISCOVER: tactical authored sections are optional and backward-compatible; D-069 already owns strict map/action/archetype/encounter validation, explicit z transitions, deterministic occupancy/pathing, supercover LOS, directional cover and `los_blocked_edges`. CPR-003 and CPR-004 are repaired on authority.
- OWNER OF BEHAVIOR: authored tactical definitions live in `combat_schema.py`; pure geometry/occupancy/path/LOS/cover rules live in `combat_grid.py`; content integration and post-state persistent-NPC ref resolution live in `content.py` / `validation.py`. D-070 must consume these APIs rather than duplicate movement legality.
- TRAP / FALSE ASSUMPTION: Manhattan A* is not admissible once arbitrary positive-cost z transitions exist; the merged grid uses deterministic Dijkstra whenever transitions are present. Same-cell LOS is trivially true after cell existence is confirmed. Cover is not opacity. Same-z transitions are rejected.
- VALIDATE WITH: PR #76 / run #390 / `37347612244` — Python **402/402 PASS**, Android unit/build/package PASS, emulator **35/35 PASS**; final APK SHA-256 `9784a7f518b747147e7bc2346321aee9fd7e85b9fe4deef298b5cae1e47a17f1`.
- CHANGE SAFELY: add transient encounter state in new D-070-owned modules. Keep D-069 definitions/pure queries immutable/read-only where possible. If movement commit needs cost, derive traversal cost from the authoritative returned path/map edges rather than inventing a second legality function.
- STILL UNKNOWN / BLOCKED: canonical player persistent identity is still not defined; D-069 deliberately resolves only durable NPC `persistent_ref` values. Attack/damage, awareness/cover attack modifiers, objectives/retreat/AI, aftermath and Android combat projection remain downstream.
- NEXT PLAYER SHORTCUT: before writing D-070 movement code, read the Movement/Pathing standard in addition to the D-070 preflight: action-budget cost and movement-point allowance are separate (Move 1 budget + 6 movement points; Sprint 2 budget + 10 movement points).
- SUPPORTING ARTIFACT: `docs/evidence/D069_TACTICAL_SCHEMA_GRID_CORE_FINAL_2026-10-05.md`.

### D-083 — Fixed campaign slots and revision-bound evidence
- PLAYER-AI: Silex, verification/completion handoff; Strata authored the preserved PR #73/#75 implementation.
- AUTHORITY / COMPLETION HEAD: verified source `8b702325c4224eb68751f147dd83c84d47d4a62c`; accepted evidence `434ad28c8bee25b17d2e42408fc8db26b0a950ce`.
- READ FIRST: `docs/PROJECT_STATUS_TRACKING_STANDARD.md`; `tools/project_status_tracker.py`; `tests/test_project_status_tracker.py`; D-083 closure evidence below.
- DO NOT REDISCOVER: Phase 1 has exactly 20 slots even when register entries are absent. Missing IDs are UNKNOWN/incomplete. The CLI already writes JSON, Markdown and a full manifest; its six focused tests plus two inventory tests passed. PR #75 already repairs qualified backticked DONE statuses.
- OWNER OF BEHAVIOR: `_campaign_summary` owns the fixed range; `parse_task_register` reads committed D-series state; `render_markdown` and `main` own report/output forms. Git owns structural truth; the Master Register owns semantics.
- TRAP / FALSE ASSUMPTION: historical A-series headings are outside the D-series completion denominator. Evidence generated before its own closure correctly shows the task IN_PROGRESS; do not hand-edit historical metrics to make them look current. READY is OTHER/incomplete under the conservative classifier.
- VALIDATE WITH: `PYTHONPATH=src:. python -m unittest tests.test_project_status_tracker tests.test_documentation_inventory_tool -v`; regenerate all three outputs at an explicit SHA and match manifest `(path, sha, bytes)` tuples against a non-truncated recursive GitHub tree.
- CHANGE SAFELY: extend the existing tracker/tests with an explicit metric definition; preserve the 20-slot invariant and committed-revision isolation. Do not create another status authority or duplicate runtime logic.
- STILL UNKNOWN / BLOCKED: this closure proves tooling/evidence only, not full engine, Android, emulator, physical device or final APK health. D-070 remains READY and D-071 remains gated.
- NEXT PLAYER SHORTCUT: D-083 is DONE; run the tracker at the commit you intend to report before quoting current numbers. Reproduce old output using the exact tracker blob from that same source revision.
- SUPPORTING ARTIFACT: `docs/evidence/D083_STATUS_TRACKER_CLOSURE_2026-10-07.md`; `docs/evidence/D083_STATUS_TRACKER_RECONCILIATION_2026-10-07.json`.


### D-070 — Transient turns, live legality and frozen reaction order
- PLAYER-AI: Silex; preserved foundation by Veyra.
- AUTHORITY / COMPLETION HEAD: `6b7cf6be32f88eaae75bd8bb3682c851b6a0965c`.
- READ FIRST: `docs/evidence/D070_TRANSIENT_ENGINE_2026-10-08.md`; `combat_state.py`; `tests/test_combat_scheduling.py`; Turn/Initiative and LOS/Detection standards.
- DO NOT REDISCOVER: four-unit budget; Move 6 / Sprint 10 points; initiative frozen per round; normal reinforcement joins next round; reserve expires at the next activation. OR-033 queue order is priority, frozen initiative, actor ID, reaction ID.
- OWNER OF BEHAVIOR: `CombatSession` owns transient commits/rollback; D-069 grid owns geometry; GameState remains the durable owner and is unchanged.
- TRAP: sorted reaction candidates are not permission to fire. Recheck current knowledge/trigger legality; consumption also rejects incapacity, expired/mismatched reserves and ended encounters.
- VALIDATE WITH: `PYTHONPATH=src python -m unittest discover -s tests -v` — 442 PASS; focused D-070 40 PASS; PR #78 / workflow #403 `37734174295`; Python 442/442 PASS; Android unit/build/package PASS; emulator 35/35 PASS; screenshot gate PASS.
- CHANGE SAFELY: extend actor-safe decision rules on the existing session/grid, preserving preview non-consumption and rollback after event append. Use the actual string `GameState.seed`.
- STILL UNKNOWN / BLOCKED: D-071 awareness/objectives/retreat/AI, D-072 aftermath, D-073 bridge/content and D-074 tactical UI remain separate acceptance gates.
- NEXT PLAYER SHORTCUT: read the scheduling test's saved-game replay fixture before introducing any new tactical persistence or random source.

### D-071 — Knowledge-safe decisions and atomic departure
- PLAYER-AI: Silex.
- AUTHORITY / COMPLETION HEAD: `ffea9fcd4e0826b54c766b2e1c06468fb3afcbe7`.
- READ FIRST: `docs/evidence/D071_TACTICAL_DECISIONS_2026-10-08.md`; `combat_rules.py`; `combat_knowledge.py`; objective and hidden-state tests.
- DO NOT REDISCOVER: LOS is not awareness; known identities are explicit; stale contacts retain old coordinates. Movement-triggered checks use the committed event identity and roll back with movement. Retreat requires an authored exit and removes occupancy/turn authority.
- OWNER OF BEHAVIOR: knowledge owns observations/safe queries, EncounterRules owns objective/detection/departure transactions, CombatSession owns events/turns, D-069 owns geometry. GameState is still the only durable owner.
- TRAP: raw session paths/events/actor IDs and AI diagnostics are not player-safe. Use the allowlisted view and observed-occupancy preview; commits recheck the real world.
- VALIDATE WITH: `PYTHONPATH=src python -m unittest discover -s tests -v` — 478 PASS; PR #79 / workflow #404 `37774598150`; Python 478/478 PASS; Android unit/build/package PASS; emulator 35/35 PASS; screenshot gate PASS.
- CHANGE SAFELY: call EncounterRules movement/interaction/retreat commits so knowledge and objective state share rollback; bind resolved stats and known identities rather than copying private NPC records.
- STILL UNKNOWN / BLOCKED: D-072 durable aftermath; D-073 canon/action effect binding/bridge and D-071-B bridge proof; D-074 tactical UI; handset budgets remain D-078.
- NEXT PLAYER SHORTCUT: start D-072 from the observation + escape fixture in `test_combat_objectives.py`; its result is transient until an explicit aftermath transaction commits it.

### P10 / D-042 — An open historical PR is not a new merge candidate
- PLAYER-AI: Quorix (`PLAYER_QUORIX`), session `SESSION_QUORIX_20261008T1732-0400_S01`.
- AUTHORITY / COMPLETION HEAD: OR-035 / Bulletin verified claim commit `510e8b458eb536b71474f71647c1bbc4b4f7b8c7`; evidence commit `413aaa4d56f1d785e2e2004a948b765a89a66b81`. This closes only bounded P10; master D-042 remains IN_PROGRESS.
- READ FIRST: `docs/evidence/P10_D042_LEGACY_PR_DISPOSITION_2026-10-08.md`; `docs/AI_TASK_BULLETIN_BOARD.md` P10; Master Register D-042; GitHub PRs #74/#76/#65/#44.
- DO NOT REDISCOVER: PR #74 remains open and diverged, but all eight D-069 file blob IDs are identical to final merged PR #76 head, which reached authority at `8b2115cf8a6f04127bdf20dd1217abd947cf8150`. PR #65/#44 are open one-file CI marker-only branches, not new runtime work.
- OWNER OF BEHAVIOR: D-069/CPR-003/CPR-004 merged Python tactical grid/schema authority; D-067 owns historical inventory/equipment acceptance; D-042 owns evidence/consumer archaeology. PR close decision belongs to individual authorized maintainers, not implicit ownership from this audit.
- TRAP / FALSE ASSUMPTION: OPEN PR + historical green workflow ≠ live merge candidate; branch divergence ≠ missing functionality; old CI ≠ current-head test pass.
- VALIDATE WITH: compare the actual PR head refs against an explicit current authority SHA (the audit used `510e8b458eb536b71474f71647c1bbc4b4f7b8c7`); query current PR states; verify the eight pairs of blob SHAs; check PR #76 merge ancestry and D-067 evidence. Source/PR checks **executed**; Python/Android tests, CI, emulator and device **not executed**.
- CHANGE SAFELY: preserve PR URL and link to completed task evidence; individually close as superseded/evidence-only if current owner approves; do not merge archived marker branches or rewrite history. Keep exact D-042 consumer mapping with P5 evidence.
- STILL UNKNOWN / BLOCKED: whether maintainers choose to close these PRs; full Master D-042 remaining D-026/D-021 consumer mapping, D-029 asset lineage, and verified deprecation/zero-consumer proof. D-072 remains Silex-owned.
- NEXT PLAYER SHORTCUT: start from P10 disposition table, then fetch fresh PR states/HEAD before taking PR actions; do not redo D-069 or merge PR #74/#65/#44 merely to clear an open queue.
- SUPPORTING ARTIFACT: `docs/evidence/P10_D042_LEGACY_PR_DISPOSITION_2026-10-08.md`.

### P8/D-026 — Tactical projection contract before Android combat UI
- PLAYER-AI: Kestrel (PLAYER_KESTREL), active session `SESSION_KESTREL_20261008T1752-0400_S02`.
- AUTHORITY / COMPLETION HEAD: source reviewed `7390ea5320b08afcadd110d10c108d9f23935584`; child packet committed `4cff510ce56b474120c45f94a3b88f387e0ba5a7`; parent consumer map `a136ae8eab74bc6370a86d3376206bf5778a2f0c`. Wave-2 P8 completion bookkeeping HEAD must be fetched from live Bulletin.
- READ FIRST: `docs/android/D026_TACTICAL_PLAYER_SAFE_PROJECTION_MIGRATION_MAP_2026-10-08.md`; `docs/systems/PHASE_1_COMBAT_SCHEMA_API_MIGRATION_PACKET.md`; `src/textrpg/combat_knowledge.py`; `src/textrpg/combat_rules.py`; OR-015/OR-034 in `docs/PROJECT_OVERSEER_DECISION_LOG.md`.
- DO NOT REDISCOVER: D-071 already emits observer-scoped contact tokens/awareness and token-filtered initiative, with own-controller objective/status via EncounterRules. Current `AndroidGameSession._view_for` has no `combat` domain, and current Kotlin `GameSnapshot` has no combat DTO. The P8 document is an implementation migration map, not a shipped tactical API.
- OWNER OF BEHAVIOR: Python combat knowledge/rules decide legality and what is observable; D-073 owns final player-safe combat wire schema/commands and OR-034 non-canon fixture; D-074 owns typed Kotlin mapping, engine delegation, ViewModel and Compose. D-026 owns documentation/consumer migration map only.
- TRAP / FALSE ASSUMPTION: do not expose `CombatSession` raw data, convert static room placement keys to tactical world positions, assume undetected actors are known because a cell is visible, or accept new combat maps without a supported domain version. Headless green Python tests do not prove the Android boundary.
- VALIDATE WITH: `tests/test_combat_knowledge.py` + `tests/test_combat_objectives.py` for existing knowledge; future D-073 bridge redaction/interrupt tests, D-074 Kotlin mapper/gateway/ViewModel tests and Compose instrumentation; PR merge-state workflow `.github/workflows/android-pixel-client.yml`. P8 documentation **only** had source/path checks: 6/6 Markdown links, 10/10 paths at `413aaa4d56f1d785e2e2004a948b765a89a66b81`; no runtime tests run.
- CHANGE SAFELY: bind D-074 to the **completed D-073 exact public wire schema**; add typed versioned nullable combat domain, strict rejection and legacy narrative compatibility; let Compose keep presentation selection only. Preserve OR-034 provisional content and save-v1 boundaries.
- STILL UNKNOWN / BLOCKED: D-072 Silex aftermath; D-073 bridge actions and wire keys; D-074 actual Kotlin/UI/tests; low-end device, canonical contact art and remaining D-026 activity/map/adversary/final-APK work. D-026 master remains IN_PROGRESS after P8.
- NEXT PLAYER SHORTCUT: first check Bulletin D-072/D-073/D-074; when D-073 is DONE, compare its verified public keys/action signatures against the P8 map, update only changed rows, then implement typed D-074 with a redaction/version/legacy test matrix.
- SUPPORTING ARTIFACT: `docs/evidence/D026_P8_TACTICAL_PROJECTION_MIGRATION_2026-10-08.md` and `docs/android/D026_TACTICAL_PLAYER_SAFE_PROJECTION_MIGRATION_MAP_2026-10-08.md`.

### P6 / D-019 — Exact-revision metadata without false word counts
- PLAYER-AI: Nodus / PLAYER_NODUS.
- AUTHORITY / COMPLETION HEAD: source commit `fae4dd58c692298d8d9aadafb9704f8843359463`, tree `9bfedd23f3dbbf251efb18718b4c274a878d0a5f`; bounded P6 evidence finalized 2026-10-08 AST.
- READ FIRST: `docs/AI_TASK_BULLETIN_BOARD.md` Parallel P6; `docs/THE_GAME_MASTER_TASK_REGISTER.md` D-019; `tools/documentation_inventory.py`; P6 evidence JSON + Markdown.
- DO NOT REDISCOVER: tree API `type=blob` paths at immutable commit give 662 files/7,428,218 committed bytes, 447 Markdown (445 in docs), 30 structured doc paths, 72 test-source paths. Full `git archive` words/headings were **not** measured; no tests ran. Old D-060 source snapshots remain valid.
- OWNER OF BEHAVIOR: D-019 `tools/documentation_inventory.py` owns exact-revision content inventory; D-081/D-082 `tools/project_status_tracker.py` owns aggregate status; `docs/assets/ASSET_PROVENANCE_REGISTRY.md`/family records own canonical art stages.
- TRAP / FALSE ASSUMPTION: Git tree metadata yields files and bytes, not Markdown words/headings or executed tests; 13 asset manifest files do not equal approved assets. Full connector blob scan exceeded the tool-call limit, and local git clone failed DNS resolution.
- VALIDATE WITH: complete checkout: `PYTHONPATH=. python -m unittest tests.test_documentation_inventory_tool -v`; `python tools/documentation_inventory.py --revision fae4dd58c692298d8d9aadafb9704f8843359463 --output /tmp/d019.json`. Commands are instructions, **not executed test evidence** from P6.
- CHANGE SAFELY: reproduce the immutable source commit on a full checkout, then extend content extractor coverage and join provenance by stable asset ID; never hand-edit historical evidence or duplicate D-081/D-082 semantics.
- STILL UNKNOWN / BLOCKED: word/heading totals, broad world/domain record totals, current canonical asset-stage promotion, executed-test evidence, owner-target unit mapping; master D-019 remains IN_PROGRESS.
- NEXT PLAYER SHORTCUT: open `docs/evidence/P6_D019_EXACT_REVISION_CHECKPOINT_2026-10-08.md`, run the documented complete-checkout recipe at its exact SHA and fill only measured missing word/heading/record fields under D-019.
- SUPPORTING ARTIFACT: `docs/evidence/P6_D019_GIT_TREE_INVENTORY_2026-10-08.json`.


### P7 / D-045 — Keep profession, rank and status as separate owners
- PLAYER-AI: Veyra / PLAYER_VEYRA; session `SESSION_VEYRA_20261007T1140-0400_S02`.
- AUTHORITY / EVIDENCE: P7 claim `35546e6c8cd524d213cdb4d75be35a15f4a5ce94`; namespace child creation `aeef81e9101ba5a5b3e70f87182357957a3bbe1d`; bounded evidence `docs/evidence/P7_D045_PROFESSION_RANK_STATUS_NAMESPACE_2026-10-08.md`.
- READ FIRST: `docs/systems/PROFESSION_RANK_STATUS_NAMESPACE_STANDARD.md`; `PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md`; `COMBAT_CLASS_CATALOG.md`; `PHASE_1_PROGRESSION_SCHEMA_API_MIGRATION_PACKET.md`; `FACTION_HIERARCHY_MEMBERSHIP_STANDARD.md`.
- DO NOT REDISCOVER: current `GameState` has no class/profession/institution-rank/faction-rank/civic-status top-level fields. D-061 keeps current Phase 1 on save schema v1. Global Level is a separate target Status axis, not a replacement for profession, class, rank, skill, ability mastery or reputation.
- OWNER OF BEHAVIOR: current skills/attributes remain schema/runtime authority; D-061 owns current Phase 1 progression migration; faction/hierarchy authority owns membership/rank/privacy semantics; V08 owns tactical legality; D-045 target documents own future profession/class/rank design until an explicit runtime migration chooses durable owners.
- TRAP / FALSE ASSUMPTION: high skill does not equal profession qualification; profession does not equal class; reputation does not equal faction rank; organization role does not equal rank; a job assignment does not create permanent profession state. Do not implement a convenient `state.professions` or generic `ranks` map from this design packet.
- VALIDATE WITH: P7 evidence records connector readback of the committed packet and structural coverage of **23/23** current skills plus **7/7** target class families, zero missing. No Python/Android runtime tests, CI, emulator, device or APK result was produced by P7.
- CHANGE SAFELY: preserve stable semantic IDs; mark target/proposal records honestly; choose one future durable owner through migration design before adding save fields; validate parent references; preserve player-safe privacy for secret membership/clearance and hidden requirements.
- STILL UNKNOWN / BLOCKED: final profession catalog, canon institutions and rank ladders, numeric grade/rank calibration, durable runtime representation, Training/Mentor/Facility child, Gate Twelve progression proof, progression UX, and later target-schema/API migration.
- NEXT PLAYER SHORTCUT: D-045's direct next child is the **Training / Mentor / Facility Progression Standard**. Consume this namespace packet; do not create another occupational hierarchy. Re-fetch the Bulletin before claiming any next lane.
- SUPPORTING ARTIFACT: `docs/evidence/P7_D045_PROFESSION_RANK_STATUS_NAMESPACE_2026-10-08.md`; primary child `docs/systems/PROFESSION_RANK_STATUS_NAMESPACE_STANDARD.md`.


## P9 / D-046 — Gate Twelve social known-precedent versus public reputation

- **PLAYER / TASK:** Veyr / PLAYER_VEYR; Parallel Wave 2 P9/D-046 (documentation-only), 2026-10-08 AST.
- **READ FIRST (smallest set):** `docs/systems/status/P9_D046_SOCIAL_KNOWLEDGE_GATE_TWELVE.md`; `docs/evidence/P9_D046_SOCIAL_KNOWLEDGE_INTEGRATION_2026-10-08.md`; `docs/evidence/D075_PHASE1_QUEST_BRANCH_WORLD_CONSEQUENCE_2026-10-04.md`; `src/textrpg/social.py`; `docs/systems/status/STATUS_KNOWLEDGE_VISIBILITY_STANDARD.md`.
- **PROVEN FACTS / DO NOT REDISCOVER:** D-075's cooperative/solo Dead Relay outcomes persist distinct NPC/quest consequences and support a later *player-visible* Tamsin interaction without exposing her private memory ID. `PASSIVE_SOC_0007` Rapport Habit has an existing actor-specific relationship context; `PASSIVE_SOC_0010` Reputation Awareness can only use truly **known** precedent. Neither has proven passive qualification, and this is not proof of public reputation.
- **REAL BEHAVIOR OWNER:** `GameState`/quest/social state, specifically `relationships`, `npcs`, `knowledge`, `quests`, `history`; `social.py` mutation and player-safe bridge are existing owners. Conceptual `SOCIAL_CONTEXT_STATE` is COMPOSE_CURRENT_STATE, not implemented.
- **TRAP / FALSE ASSUMPTION:** NPC-private relationship, memory, trust or suspicion is not public reputation; a civic archive/public plaza is not a reputation publisher or Status knowledge authority. Never infer passive unlock from a story choice or copy private NPC memory into Android.
- **EXACT VALIDATION RECIPE:** Documentation source/readback links above; planned future Python command `PYTHONPATH=src python -m unittest discover -s tests -v`, targeted `tests/test_social.py` and `tests/test_phase1_quest_branch_world_consequence.py` if code changes. No tests/CI/Android were executed by this documentation slice.
- **SAFEST EXTENSION:** Approve one provenance-bearing witnessed/published reputation event and an actor/recipient knowledge boundary through future world/social contracts before authoring a SOC_0010 qualification or projection. Use validated durable NPC identity and atomic quest/social effects; do not introduce ad hoc UI-owned reputation.
- **UNRESOLVED BOUNDARY:** public-reputation publication policy and owner, repeated social qualification/anti-replay ledger, actual rumors/classification, numeric parameters, explicit passive-list DTO and canon promotion.
- **NEXT PLAYER SHORTCUT:** Read this P9 packet, then source-check D-075 visible consequences; keep actor-specific known precedent separate from public reputation. Re-fetch Bulletin before claiming any follow-up.
