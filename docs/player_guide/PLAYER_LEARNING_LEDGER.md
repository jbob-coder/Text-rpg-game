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

