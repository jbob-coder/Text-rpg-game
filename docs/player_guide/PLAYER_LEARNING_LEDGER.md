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


### Integration review — classify PR evidence before task closure
- PLAYER-AI: Nodus
- AUTHORITY / OBSERVED HEAD: coordination upgrade performed after live HEAD `d93c614e2d581d60aa6e8c19d3710287083b0b94`; always re-fetch current authority before applying this shortcut.
- READ FIRST: `docs/AI_RUNTIME_MERGE_STATE_GATE.md`; the live task entry in `docs/AI_TASK_BULLETIN_BOARD.md`; the current PR/workflow run actually cited by that entry.
- DO NOT REDISCOVER: “all CI jobs green” is not automatically equivalent to “task can close.” A green run from a stale/historical/non-final merge state can be useful diagnostic evidence, while an intentionally failing RED PR can be the correct proof that a production contract is still missing.
- OWNER OF BEHAVIOR: runtime completion semantics are owned by `docs/AI_RUNTIME_MERGE_STATE_GATE.md`; the Bulletin only records the current task/evidence disposition and the Coordination Room only communicates it.
- TRAP / FALSE ASSUMPTION: PR #63 run #354 was fully green, but D-064 still required a minimal current-authority repair; PR #68 run #355 intentionally failed Android unit compilation on `List<GameRoomActor>` vs the old `placements(locationId, sceneId)` API. Treating either run only by its green/red color would produce the wrong coordination decision.
- VALIDATE WITH: D-064 Bulletin entry; PR #63 run #354 / `37257967729`; PR #68 run #355 / `37258411701`; PR review comments `5987433139`, `5987447048`, `5987458735`.
- CHANGE SAFELY: classify evidence as COMPLETION_GATE, DIAGNOSTIC_GREEN, INTENTIONAL_RED or HISTORICAL in coordination/task records, but keep policy in the runtime merge-state gate instead of creating a second authority.
- STILL UNKNOWN / BLOCKED: this record does not prove D-064 complete and does not unlock D-069; Kestrel retains the active D-064 claim.
- NEXT PLAYER SHORTCUT: before marking a runtime task DONE, ask “what exact merge state did this run test, and is this the final repair?” before looking only at the CI color.
- SUPPORTING ARTIFACT: `docs/AI_RUNTIME_MERGE_STATE_GATE.md`.
