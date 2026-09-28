# THE GAME — Pixel Asset Manifest Schema v1

Every production asset must have a machine-readable manifest entry. The manifest connects game IDs, reference lineage, blueprint rules, native files, state bindings and QA.

## Required fields

```json
{
  "asset_id": "ITEM_DEPOT_JACKET_PAPERDOLL",
  "asset_family": "equipment_layer",
  "status": "PLANNED",
  "canon_status": "provisional",
  "source_game_ids": ["ITEM_DEPOT_JACKET"],
  "source_content_ids": ["CONTENT_VERTICAL_SLICE_01"],
  "native_canvas": {
    "width": 32,
    "height": 48,
    "format": "png",
    "alpha": true
  },
  "palette": {
    "max_colors": 12,
    "colors": []
  },
  "anchors": {},
  "layer_order": 8,
  "variants": [],
  "animation": null,
  "visibility_contract": {
    "player_visible_only": true,
    "spoiler_risk": "none"
  },
  "state_bindings": [],
  "reference_assets": [],
  "blueprint_path": null,
  "production_files": [],
  "integration_targets": [],
  "qa": {
    "native_scale_reviewed": false,
    "android_scale_reviewed": false,
    "anchor_alignment_reviewed": false,
    "palette_reviewed": false,
    "state_binding_reviewed": false
  },
  "checksums": {}
}
```

## Status values

- `PLANNED`
- `BRIEF_LOCKED`
- `REFERENCE_GENERATED`
- `REFERENCE_SELECTED`
- `BLUEPRINTED`
- `PIXEL_MASTER_BUILT`
- `INTEGRATED`
- `VERIFIED`
- `CANON_APPROVED`

## Canon status

Recommended values:

- `technical`: pipeline/UI asset with no story-canon meaning;
- `provisional`: belongs to provisional current content;
- `canon`: explicitly approved final story/identity asset;
- `non_canon_reference`: generated concept/reference only.

Generated reference files must use `non_canon_reference`.

## Asset-family vocabulary

Initial families:

- character_turnaround
- character_base
- character_layer
- character_pose
- character_animation
- portrait
- item_icon
- equipment_layer
- prop
- prop_state
- location_scene
- location_state
- environment_module
- environment_atlas
- environment_overlay
- environment_decal
- ui_icon
- hud_icon
- quest_icon
- map_icon
- fx
- status_fx
- transition

## Native canvas

Do not infer native size from the PNG after the fact. The manifest is the contract.

Examples:

- 16x16 map/status;
- 24x24 navigation;
- 32x32 inventory;
- 32x48 gameplay character/equipment;
- 64x64 portrait/FX;
- 128x64 scene;
- 256x144 map master.

## Palette

Record:

- maximum color count;
- exact approved colors after pixel reconstruction;
- optional material sub-ramps;
- whether PixelColors.Cyan/Gold/Danger is intentionally referenced.

Reference-generation colors do not become palette entries automatically.

## Anchors

Character/equipment example:

```json
{
  "ground": [16, 47],
  "neck": [16, 13],
  "left_shoulder": [10, 15],
  "right_shoulder": [22, 15],
  "main_hand": [27, 31],
  "off_hand": [5, 31]
}
```

Prop example:

```json
{
  "pivot": [16, 31],
  "grip": [5, 18]
}
```

## Layer order

Use the master z-order from `PIXEL_ASSET_MASTER_PLAN.md`.

The manifest may also specify:

- `occludes_layers`;
- `masked_by_layers`;
- `rear_variant`;
- `front_variant`.

## Variants

Variants must represent actual visual states, not arbitrary recolors.

Example:

```json
[
  {
    "variant_id": "relay_opened",
    "game_condition": "authored story state: relay safely opened"
  },
  {
    "variant_id": "relay_signal_lost",
    "game_condition": "visible result of signal-loss outcome"
  }
]
```

## Animation

Example:

```json
{
  "frame_width": 32,
  "frame_height": 48,
  "frame_count": 4,
  "fps": 6,
  "loop": true,
  "frame_anchors_path": "assets/pixel/manifests/PLAYER_IDLE_SHEET.anchors.json"
}
```

Frame count/FPS are design data and must not be hidden inside filename conventions.

## Visibility contract

This protects the player-facing projection boundary.

Fields:

- `player_visible_only`: visual is allowed to depend only on player-safe state;
- `spoiler_risk`: none / low / medium / high;
- `hidden_state_forbidden`: list of raw flags/definitions that must never directly drive this asset.

Example:

```json
{
  "player_visible_only": true,
  "spoiler_risk": "high",
  "hidden_state_forbidden": [
    "raw authored future-scene target",
    "hidden condition definition"
  ]
}
```

## State bindings

State binding maps authoritative projection to visual.

Example:

```json
[
  {
    "source": "inventory.equipment",
    "match": {
      "item_id": "ITEM_DEPOT_JACKET",
      "slot": "body",
      "equipped": true
    },
    "visual_result": "show"
  }
]
```

Map example:

```json
[
  {
    "source": "world_map.nodes[].reachable",
    "value": true,
    "visual_result": "MAP_NODE_REACHABLE"
  }
]
```

## Reference assets

Each reference record includes:

- reference ID;
- generation date if recorded;
- prompt/brief path;
- candidate number;
- selected/rejected;
- rejection reason when applicable;
- file hash if persisted.

Do not store only "approved image" without provenance.

## Blueprint path

Blueprint may be Markdown, JSON, SVG-like coordinate spec, or another inspectable format, but it must describe reconstruction independent of the generated reference.

Suggested:

`assets/blueprints/<family>/<asset_id>.md`

## Production files

List every actual shipped file.

Example:

```json
[
  "assets/pixel/equipment/ITEM_DEPOT_JACKET__paperdoll__front__v01.png"
]
```

No ephemeral chat image path is a production file.

## Integration targets

Examples:

- `android GameScreen / PlayerAvatarPanel replacement`;
- `Character screen portrait`;
- `Inventory item row`;
- `MapSection node renderer`;
- `SceneIllustration replacement loader`.

## QA contract

At minimum:

- native scale reviewed;
- palette reviewed;
- transparent-edge/halo reviewed;
- anchor alignment reviewed when relevant;
- player-safe state binding reviewed;
- Android target-scale reviewed.

Animation adds:

- loop reviewed;
- frame anchors reviewed;
- equipment following reviewed.

Location adds:

- safe crop reviewed;
- state-overlay separation reviewed.

## Checksums

Record SHA-256 for final persisted production files when practical.

This supports:

- accidental corruption detection;
- verifying packaged APK assets;
- confirming that a generated candidate was not silently substituted for the reconstructed master.

## Batch record

Each batch should have its own manifest index:

```json
{
  "batch_id": "BATCH_001",
  "expected_units": 100,
  "assets": [
    "PLAYER_BODYFRAME_A_TURNAROUND",
    "..."
  ]
}
```

The index must fail validation if the asset count differs from the batch contract.

