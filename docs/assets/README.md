# THE GAME — Pixel Asset Documentation Index

Read in this order before generating or integrating visual assets:

1. [PIXEL_ASSET_MASTER_PLAN.md](PIXEL_ASSET_MASTER_PLAN.md)
   - native grids, global pixel rules, character rig, scene/map/item standards, repository paths, lifecycle and quality gates.
2. [CHARACTER_PIXEL_BLUEPRINTS.md](CHARACTER_PIXEL_BLUEPRINTS.md)
   - detailed player paper-doll construction and canonical Tamsin visual blueprint.
3. [ASSET_BATCH_001_001-100.md](ASSET_BATCH_001_001-100.md)
   - exact first production batch of 100 documented units with game use and production notes.
4. [REFERENCE_TO_BLUEPRINT_PIPELINE.md](REFERENCE_TO_BLUEPRINT_PIPELINE.md)
   - rules for using generated imagery only as reference and reconstructing it into native pixel masters.
5. [ASSET_MANIFEST_SCHEMA.md](ASSET_MANIFEST_SCHEMA.md)
   - machine-readable lineage/state/QA contract for every asset.

## Current phase

Documentation and planning are the authority.

No new generated visual is considered a production asset until the documentation pipeline advances it through:

`REFERENCE_GENERATED -> REFERENCE_SELECTED -> BLUEPRINTED -> PIXEL_MASTER_BUILT -> INTEGRATED -> VERIFIED`

## Grounded current content

Batch 001 is tied to the current playable slice:

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

## Next production step

When asset production begins, start with Batch 001 items 001, 002, 018 and 021/022:

- player six-view body reference/blueprint;
- player front paper-doll master;
- Tamsin six-view canonical reference/blueprint;
- Depot Jacket icon and chest layer.

This small set validates the entire reference -> blueprint -> pixel master -> paper-doll integration pipeline before mass generation.

