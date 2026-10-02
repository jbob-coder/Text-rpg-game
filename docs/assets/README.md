# THE GAME — Pixel Asset Documentation Index

Read in this order before generating or integrating visual assets:

0. [../MASTER_GAME_DEVELOPMENT_PROGRAM.md](../MASTER_GAME_DEVELOPMENT_PROGRAM.md)
   - repository-wide priority, permissions, system volumes and execution gates.
0. [PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md](PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md)
   - runtime composition of environments, props, overlays, room actors, player, equipment, FX and character panels; includes reuse compatibility and migration rules.

1. [PIXEL_ASSET_MASTER_PLAN.md](PIXEL_ASSET_MASTER_PLAN.md)
   - native grids, global pixel rules, character rig, scene/map/item standards, repository paths, lifecycle and quality gates.
2. [CHARACTER_PIXEL_BLUEPRINTS.md](CHARACTER_PIXEL_BLUEPRINTS.md)
   - detailed player paper-doll construction and canonical Tamsin visual blueprint.
3. [ASSET_PRODUCTION_ROADMAP_001-500.md](ASSET_PRODUCTION_ROADMAP_001-500.md)
   - complete v1 production baseline: five exact 100-unit batches, 500 planned asset units total.
4. [ASSET_BATCH_001_001-100.md](ASSET_BATCH_001_001-100.md)
   - current playable slice and first production wave.
5. [ASSET_BATCH_002_101-200.md](ASSET_BATCH_002_101-200.md)
   - character/NPC/customization/animation framework.
6. [ASSET_BATCH_003_201-300.md](ASSET_BATCH_003_201-300.md)
   - equipment, tools/weapons, materials, key items, containers and inventory presentation.
7. [ASSET_BATCH_004_301-400.md](ASSET_BATCH_004_301-400.md)
   - architecture, interiors, world props, environment overlays, map/travel modules.
8. [ASSET_BATCH_005_401-500.md](ASSET_BATCH_005_401-500.md)
   - UI shells, combat/interaction feedback, ability/status FX, transitions, accessibility and developer QA assets.
9. [REFERENCE_TO_BLUEPRINT_PIPELINE.md](REFERENCE_TO_BLUEPRINT_PIPELINE.md)
   - rules for using generated imagery only as reference and reconstructing it into native pixel masters.
10. [ASSET_MANIFEST_SCHEMA.md](ASSET_MANIFEST_SCHEMA.md)
   - machine-readable lineage/state/QA contract for every asset.
11. [REFERENCE_REGISTRY.md](REFERENCE_REGISTRY.md)
   - durable generated-reference provenance and selection/rejection decisions.
12. [production_packets/BATCH_001_WAVE_A_BLUEPRINTS.md](production_packets/BATCH_001_WAVE_A_BLUEPRINTS.md)
   - exact reconstruction packet for assets 001, 002, 018, 021 and 022.
13. [manifests/BATCH_001_WAVE_A.json](manifests/BATCH_001_WAVE_A.json)
   - machine-readable Wave A states, anchors, palettes, bindings and QA gates.

Map-specific application blueprint:
- [GATE_TWELVE_MAP_PIXEL_ASSET_BLUEPRINT.md](GATE_TWELVE_MAP_PIXEL_ASSET_BLUEPRINT.md)
  - binds the existing 256x144 Gate Twelve geometry to textual pixel-art specifications, reusable asset families, current code-present IDs, production order and integration rules.
- [GATE_TWELVE_MAP_ANIMATION_BLUEPRINT.md](GATE_TWELVE_MAP_ANIMATION_BLUEPRINT.md)
  - defines static, ambient-loop and state-driven animation contracts for each Gate Twelve district region, including frame/timing guidance and the first three implementation tasks.

## Current phase

The 500-unit planning baseline is complete. Production Wave A is now in pre-build/reference-selection work; documentation and manifests remain the authority until reconstructed native pixel masters exist.

No new generated visual is considered a production asset until the documentation pipeline advances it through:

`REFERENCE_GENERATED -> REFERENCE_SELECTED -> BLUEPRINTED -> PIXEL_MASTER_BUILT -> INTEGRATED -> VERIFIED`

## Grounded current content

Batch 001 is tied to the current playable slice. Batches 002–005 are technical/non-canon expansion frameworks until authored content binds them:

- NPC_TAMSIN;
- Platform Nine;
- Relay Workbench;
- Service Gate Twelve;
- Service Tunnel;
- Quiet Stair;
- Trace Chamber;
- Depot Plaza;
- Municipal Archive;
- Workshop Row;
- current opening equipment and Dead Relay states;
- current main/side/optional/lore quest categories;
- current health/stamina/focus/resolve resources;
- current Trace Echo / Signal Pulse / Directional Trace visual requirements.

## Do not do

- Do not paste a smooth generated image into the game and call it pixel art.
- Do not regenerate an approved character from memory.
- Do not create equipment art that owns equipment state.
- Do not reveal hidden authored state through visuals.
- Do not build unique flattened location images when a location master plus state overlay is sufficient.
- Do not silently change stable IDs to match filenames.
- Do not mark an asset VERIFIED without checking its real integration.

## Planning verification

The v1 production baseline is mechanically verified as 500 unique continuous catalog units: 001–500, five batches of exactly 100, with no duplicate stable asset IDs.

## Next production step

Now that planning is complete, start generation/reconstruction with Batch 001 items 001, 002, 018 and 021/022:

- player six-view body reference/blueprint;
- player front paper-doll master;
- Tamsin six-view canonical reference/blueprint;
- Depot Jacket icon and chest layer.

This small set validates the entire reference -> blueprint -> pixel master -> paper-doll integration pipeline before mass generation.



## First generated reference record

`REF_BATCH001_CONCEPT_BOARD_A` has been preserved in Google Drive and audited in `references/REF_BATCH001_CONCEPT_BOARD_A.md`.

It is accepted only for broad style direction. Its invented item/NPC/location details are explicitly rejected as canon.


## Verified runtime asset waves

- `manifests/BATCH_001_WAVE_B_CURRENT_LOADOUT_RELAY.json` — current authored loadout and relay-state visuals.
- `manifests/BATCH_001_WAVE_C_CURRENT_SCENES.json` — 9/9 current named-location base masters plus Gate Twelve, tunnel-aftershock and Trace Chamber training overlays.

The Wave C runtime parent `1c7e54e548ab3c28819af0b85ae8cbba53aff827` passed workflow `36384772701`: Python 301/301, Android build/instrumentation gates, and API 35 emulator 10/10. Native-scale art review and physical Galaxy A03 visual QA remain pending.

- [GATE_TWELVE_ASSET_STATUS_AND_PRODUCTION_MATRIX.md](GATE_TWELVE_ASSET_STATUS_AND_PRODUCTION_MATRIX.md)
  - Step-7 evidence matrix for all Batch 001 units plus Gate Twelve per-area asset decomposition, current stage, manifest/code drift, missing exact IDs and open refinement lines.

## Pixel production/reuse ledger

Use [PIXEL_ART_PRODUCTION_AND_REUSE_LEDGER.md](PIXEL_ART_PRODUCTION_AND_REUSE_LEDGER.md) for:
- current-vs-required asset stages;
- Jack/Tamsin production needs;
- room actor + portrait/panel composition;
- overlay/text/signage rules;
- reuse compatibility;
- Gate Twelve per-area production packets.

It supplements, not replaces, the runtime composition standard and exact asset manifests.


## Provenance
- `ASSET_PROVENANCE_REGISTRY.md` — branch-aware source/reference/raster/code provenance, production stage, supersession, compatibility and reconciliation queue.
