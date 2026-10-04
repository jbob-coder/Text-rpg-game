# Text RPG Game

## Current priority program

**Priority repository:** `jbob-coder/Text-rpg-game`.

Repository-wide game development is now documentation-first under [`docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`](docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md). The current objective is to finish the authority/world/visual/system/application contracts before broad implementation expansion or a final APK rebuild. The existing V6 stabilization material remains valid historical engine evidence, but it is not the top-level product objective.

Gate Twelve is the first proof region. Its region plan Steps 1–14 are now complete on the program branch; the next P0 work is exact live implementation/asset reconciliation plus reproducible documentation/world/asset inventory before broad runtime migration.

Start here for current work:

1. [Master Development & Documentation Program](docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md)
2. [Master Documentation Record](docs/MASTER_DOCUMENTATION_RECORD.md)
3. [Final Game Reconstruction Blueprint](docs/FINAL_GAME_RECONSTRUCTION_BLUEPRINT.md)
4. [Documentation Cross-Reference Matrix](docs/DOCUMENTATION_CROSS_REFERENCE_MATRIX.md)
5. [Master Task Register](docs/THE_GAME_MASTER_TASK_REGISTER.md)
6. [Gate Twelve Region Master Plan](docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md)
7. [Pixel Art Runtime Composition Standard](docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md)
8. [World Development Master Index](docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md)
9. [Android APK Rebuild & Evolution Master Plan](docs/android/APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md)
10. [Master Directive Execution Breakdown](docs/MASTER_DIRECTIVE_EXECUTION_BREAKDOWN.md)
11. [Existing-State Rework Decision Matrix](docs/EXISTING_STATE_REWORK_DECISION_MATRIX.md)
12. [Documentation Progress Ledger](docs/DOCUMENTATION_PROGRESS_LEDGER.md)
13. [Pixel Art Production & Reuse Ledger](docs/assets/PIXEL_ART_PRODUCTION_AND_REUSE_LEDGER.md)
14. [World-Scale Documentation Blueprint](docs/world/WORLD_SCALE_DOCUMENTATION_BLUEPRINT.md)
15. [Gameplay System Rebuild Matrix](docs/systems/GAMEPLAY_SYSTEM_REBUILD_MATRIX.md)
16. [Final APK Reconstruction Matrix](docs/android/APK_FINAL_RECONSTRUCTION_MATRIX.md)
17. [Documentation Corpus Architecture](docs/DOCUMENTATION_CORPUS_ARCHITECTURE.md)
18. [World Geography Standard](docs/world/WORLD_GEOGRAPHY_STANDARD.md)
19. [World Political Entities](docs/world/WORLD_POLITICAL_ENTITIES.md)
20. [World Settlement Catalog](docs/world/WORLD_SETTLEMENT_CATALOG.md)
21. [World Travel and Routes](docs/world/WORLD_TRAVEL_AND_ROUTES.md)
22. [Room Actor / Panel / Overlay / Reuse Standard](docs/assets/ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md)
23. [World Ecosystems and Resources](docs/world/WORLD_ECOSYSTEM_AND_RESOURCES.md)
24. [World Beast Zone Standard](docs/world/WORLD_BEAST_ZONE_STANDARD.md)
25. [World Population / Citizen Hierarchy](docs/world/WORLD_POPULATION_AND_CITIZEN_HIERARCHY.md)
26. [World Balance and Level Bands](docs/world/WORLD_BALANCE_AND_LEVEL_BANDS.md)
27. [World Loot Provenance Standard](docs/world/WORLD_LOOT_PROVENANCE_STANDARD.md)
28. [World NPC Population Standard](docs/world/WORLD_NPC_POPULATION_STANDARD.md)
29. [Live Repository State Audit — 2026-10-02](docs/LIVE_REPOSITORY_STATE_AUDIT_2026-10-02.md)
30. [Repository Corpus Inventory Snapshot — 2026-10-02](docs/REPOSITORY_CORPUS_INVENTORY_SNAPSHOT_2026-10-02.md)
31. [Deterministic Documentation Inventory Tool](tools/documentation_inventory.py)
32. [Owner Directive Traceability Matrix — 2026-10-02](docs/OWNER_DIRECTIVE_TRACEABILITY_MATRIX_2026-10-02.md)
33. [Player Activities & Life-Loop Master Plan](docs/systems/PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md)
34. [World Coordinate & Scale Standard](docs/world/WORLD_COORDINATE_AND_SCALE_STANDARD.md)
35. [Asset Provenance Registry](docs/assets/ASSET_PROVENANCE_REGISTRY.md)
36. [Android Consumer & Player-Safe Projection Map](docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md)

The default `main` branch remains a placeholder and is not implementation authority.


A data-driven, authored choice RPG where player decisions, stats, relationships, knowledge, equipment, powers, party composition, and previous conversations persist and alter later scenes.

Current stabilization candidate: `fix/v6-runtime-boundaries`, based on
`integration/rules-ability-v6-reconcile@7f5f104fb839068bdfaf5cec72f37129ae20d463`.
The default `main` branch is still a placeholder; select the candidate branch to run this implementation.

> Coding agents and future sessions: start with [`AGENTS.md`](AGENTS.md), then read [`docs/THE_GAME_MASTER_TASK_REGISTER.md`](docs/THE_GAME_MASTER_TASK_REGISTER.md) for the current objective, blockers, task states, and handoff rules.

## Rules-engine vertical slice

The rules layer is deliberately separated from presentation. The game can later use a pixel-art Android, Godot, desktop, or web client without rebuilding the RPG state model.

- `docs/GAME_FOUNDATION.md` — canonical systems direction.
- `docs/VISUAL_BIBLE.md` — pixel-art and character consistency rules.
- `docs/REFERENCE_NOTES.md` — abstract lessons from supplied reference material; no copied story content.
- `docs/IMPLEMENTATION_STATUS.md` — current objective, verified state, completed work, risks, and next actions.
- `docs/V6_STABILIZATION_HANDOFF.md` — executed baseline, repairs, compatibility boundaries, and verification evidence.
- `docs/THE_GAME_MASTER_TASK_REGISTER.md` — repository-native task queue and continuity index.
- `src/textrpg/core.py` — deterministic scene/choice rules and persistent state.
- `src/textrpg/content.py` — validated JSON content-pack loading into state + engine.
- `src/textrpg/cli.py` — local standard-library terminal client with save/resume support.
- `src/textrpg/progression.py` — earned ability mastery and technique prerequisites.
- `src/textrpg/powers.py` — explicit ability/technique discovery gates, ability-specific resources/recovery, paid practice, costs, cooldowns, drawbacks, mastery stages, and evolution.
- `src/textrpg/quests.py` — authored quest graphs, objective prerequisites, branching/failure routes, and terminal states.
- `src/textrpg/persistence.py` — versioned JSON save/load.
- `src/textrpg/json_contract.py` — shared finite-number JSON decoding for saves and content.
- `src/textrpg/status.py` — player status and inspection projections with hidden condition/perk redaction.
- `src/textrpg/validation.py` — scene/quest/power validation plus stable registry cross-references for knowledge, perks, items, and conditions.
- `src/textrpg/stats.py` — canonical attributes, skills, modifier-aware resources, and derived values.
- `src/textrpg/simulation.py` — world time, conditions, training, and recovery.
- `src/textrpg/equipment.py` — equipment slots, requirements, modifiers, and set bonuses.
- `src/textrpg/social.py` — NPC memory, private knowledge, relationships, goals, story-state transitions, sharing, leak eligibility, and deterministic leak-event execution.
- `src/textrpg/visuals.py` — canonical recurring-character visual identity validation and normalized generation contracts.
- `content/vertical_slice_01.json` — original provisional-canon playable slice: opening branches, NPC state, Gate Twelve power discovery, first live technique use, drawback, and resource recovery.
- `content/sample_scene.json` — non-canon scene showing relationship, knowledge, item, and stat-dependent choices.
- `tests/` — behavior, progression, persistence, content validation, end-to-end route, and save/resume regression tests.

## Play the current local slice

From the repository root:

```bash
PYTHONPATH=src python -m textrpg.cli content/vertical_slice_01.json --save local_save.json
```

The CLI is a development client, not the final presentation layer. It runs authored deterministic content locally and requires no runtime AI or hosted service.

## Run verification

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Observed on Python 3.12.14: **275 tests passed, 0 failures/errors** on the repaired candidate.
The untouched upstream V6 source was first matched against all 45 Git blob hashes and
its complete Git tree, then executed: **258 tests, 1 failure, 12 errors**.
The historical 103-pass foundation result does not describe V6.

Commands, logs, the runtime file manifest, and the remaining promotion work are recorded
in [the stabilization handoff](docs/V6_STABILIZATION_HANDOFF.md).

Player clients should use `engine.build_scene_view(state)`, `engine.available_choices(state)`,
and the status/ability projections. Raw scenes, state, modifier breakdowns, and resolution
history remain engine/developer data and are not player-facing projections.

The prototype uses only the Python standard library. No hosted AI service or GitHub Actions workflow is required.


## 2026-10-02 operational continuation

- [Decision/rebuild execution register](docs/DECISION_AND_REBUILD_EXECUTION_REGISTER.md): decomposed owner requirements, can/will/candidate changes, migration gates and unresolved corpus units.
- [Full baseline document catalog](docs/DOCUMENTATION_CATALOG_2026-10-02.md): every tracked Markdown file, actual headings, words, hashes and literal references; semantic audit remains separate.
- [World canon decision queue](docs/world/WORLD_CANON_DECISION_QUEUE.md): exact nine-node/eight-edge baseline and ordered unresolved geography/politics/ecology/progression decisions.
- [Room composition implementation contract](docs/assets/ROOM_COMPOSITION_IMPLEMENTATION_CONTRACT.md): current actors versus proposed presence projection, focus panels, pixel/text reuse and raster-precedence gates.
- [Raster delivery evidence](docs/assets/RASTER_DELIVERY_EVIDENCE_2026-10-02.md): all 24 baseline PNG dimensions, hashes and catalog bindings.

These supplement existing masters. They do not supersede approved identity references or imply new gameplay APIs.
