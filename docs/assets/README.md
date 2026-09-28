# THE GAME — Pixel Asset Documentation Index

Read in this order before generating or integrating visual assets:

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
14. [reference_briefs/PLAYER_BODYFRAME_A_TURNAROUND_REFERENCE_BRIEF.md](reference_briefs/PLAYER_BODYFRAME_A_TURNAROUND_REFERENCE_BRIEF.md)
   - identity-neutral six-view player rig generation/selection contract.
15. [reference_briefs/NPC_TAMSIN_TURNAROUND_REFERENCE_BRIEF.md](reference_briefs/NPC_TAMSIN_TURNAROUND_REFERENCE_BRIEF.md)
   - canon-constrained Tamsin six-view generation/selection contract.
16. [CANONICAL_TURNAROUND_GENERATION_PROTOCOL.md](CANONICAL_TURNAROUND_GENERATION_PROTOCOL.md)
   - one-asset-per-image selection protocol, anatomical-side verification, and rejection rules.

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


## Second generated reference record

`REF_BATCH001_CONCEPT_BOARD_B` is preserved in Google Drive and audited in `references/REF_BATCH001_CONCEPT_BOARD_B.md`.

It improves the production-layout/style language over Board A but remains non-canon for player identity, Tamsin geometry where it conflicts with the identity contract, generic NPC identities, unsupported key items, relay-state expansion, and district topology.
