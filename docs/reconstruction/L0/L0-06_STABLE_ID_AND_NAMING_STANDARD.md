# L0-06 — Stable ID and Naming Standard

Layer: **L0 Foundation**
Depends on: L0-05 (asset unit registry)
Sources: `docs/GAME_FOUNDATION.md` §"Save and compatibility rules"; `docs/assets/ASSET_MANIFEST_SCHEMA.md`

---

## 1. The stability law

> All IDs are stable and never reused for a different meaning.
> — `GAME_FOUNDATION.md`

> Story text may change without renaming stable IDs.
> — `GAME_FOUNDATION.md`

This is the single most important rule in the project and it has three
consequences a rebuild must respect:

1. An ID, once published, means exactly one thing forever.
2. Renaming is prohibited. Fixing a *label* is allowed; changing an *ID* is not.
3. A save file written against an ID must keep working. If meaning changes, a
   migration is required and must be explicit.

### 1.1 Runtime resource filenames are not identity

`pixel_item_depot_jacket_icon.png` is a *resource name*. The stable ID
`ITEM_DEPOT_JACKET_ICON` is the *identity*. Renaming a drawable to match a
filename, or renaming an ID to match a drawable, are both prohibited.

This matters for the corpus: the 24 existing rasters have resource names that
differ from their stable asset IDs, and that is correct, not a defect.

## 2. ID namespaces

| Namespace | Prefix / form | Owner |
| --- | --- | --- |
| Content | `CONTENT_*` | content slice |
| Scene | `SCENE_*` semantic, or authored scene key | content |
| Quest | `QUEST_*` | content |
| Objective | `OBJ_*` | content |
| Knowledge | `KNOW_*` | content |
| Item | `ITEM_*` | registries |
| Equipment slot | `body`, `hands`, `ring_1`, `neck`, … | registries |
| Condition | `COND_*` | registries |
| Perk | `PERK_*` | registries |
| Ability | `ABILITY_*` | powers |
| Technique | `TECHNIQUE_*` | powers |
| Character | `NPC_*` | characters |
| Place | `PLACE_*` / node IDs | world map |
| Asset | `PLAYER_*`, `NPC_*`, `ITEM_*`, `PROP_*`, `FX_*`, `UI_*`, `MAP_*`, `ENV_*` | assets |
| Region | `REGION_*` | world |
| Political | `POLITICAL_*` (schema, unused) | world |
| World flag | `world.*` | state |
| Player flag | `player.*` (schema, unused) | state |
| QA gate | `QA_*` | tests |
| Evidence | `EVID_*` | evidence |

### 2.1 Namespace collision rule

An asset ID may **reuse** a semantic prefix from another namespace when the
combination is unambiguous, and this already happens in canon:

- `ITEM_DEPOT_JACKET` — the **item**;
- `ITEM_DEPOT_JACKET_ICON` — the **asset**;
- `ITEM_DEPOT_JACKET_PAPERDOLL` — the **asset**.

The item is the thing; the `_ICON` and `_PAPERDOLL` suffixes make the asset
unambiguous. This is intentional and must be preserved.

## 3. Naming conventions

Naming is split three ways: identifiers (upper snake), file names (double
underscore separated), and runtime Android resources (single underscore,
`pixel_` prefix).

### 3.1 Style

- **Asset IDs, scene IDs, quest IDs, item IDs, ability IDs:** `UPPER_SNAKE_CASE`.
- **Flags:** `namespace.dotted_name`, lowercase.
- **World map nodes:** `UPPER_SNAKE_CASE` location IDs.
- **Python modules/functions:** `lower_snake_case`.
- **Kotlin types:** `UpperCamelCase`; **objects/constants:** `UPPER_SNAKE_CASE`.
- **Android resources:** `lower_snake_case` with a `pixel_` prefix for pixel art.

### 3.2 File name pattern

```
<stable_id>__<family>__<view_or_state>__vNN.png
```

Examples:

- `NPC_TAMSIN__portrait__focused__v01.png`
- `ITEM_DEPOT_JACKET__paperdoll__front__v01.png`
- `PLATFORM_NINE__scene__blackout__v01.png`

Reference images take the `REF_` prefix and never occupy a production asset
path.

### 3.3 Version suffix

`vNN` is a **production master revision**, not a save-file schema version. It
increments when a production master is rebuilt. It does not increment for
metadata-only changes.

## 4. Asset manifest contract

Every production asset has a machine-readable manifest entry. Required fields
(per `ASSET_MANIFEST_SCHEMA.md`):

```json
{
  "asset_id": "ITEM_DEPOT_JACKET_PAPERDOLL",
  "asset_family": "equipment_layer",
  "status": "PLANNED",
  "canon_status": "provisional",
  "source_game_ids": ["ITEM_DEPOT_JACKET"],
  "source_content_ids": ["CONTENT_VERTICAL_SLICE_01"],
  "native_canvas": { "width": 32, "height": 48, "format": "png", "alpha": true },
  "palette": { "max_colors": 12, "colors": [] },
  "anchors": {},
  "layer_order": 8,
  "variants": [],
  "animation": null,
  "visibility_contract": { "player_visible_only": true, "spoiler_risk": "none" },
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

### 4.1 Native canvas is the contract

> Do not infer native size from the PNG after the fact. The manifest is the
> contract.

The observed PNG dimensions are **evidence**, not specification. A rebuild that
derives intent from file dimensions has inverted the authority order.

### 4.2 Canon status vocabulary

| Value | Meaning |
| --- | --- |
| `technical` | pipeline/UI asset with no story-canon meaning |
| `provisional` | belongs to provisional current content |
| `canon` | explicitly approved final story/identity asset |
| `non_canon_reference` | generated concept/reference only |

Generated reference files **must** use `non_canon_reference`.

### 4.3 Status vocabulary

`PLANNED` → `BRIEF_LOCKED` → `REFERENCE_GENERATED` → `REFERENCE_SELECTED` →
`BLUEPRINTED` → `PIXEL_MASTER_BUILT` → `INTEGRATED` → `VERIFIED` →
`CANON_APPROVED`

The extended provenance vocabulary adds: `SOURCE_MASTER_PRESENT`,
`RASTER_PRESENT`, `CODE_PRESENT`, `OPEN_PR_REFINEMENT`, `QA_PENDING`,
`DEFERRED_INTEGRATION`, `SUPERSEDED`, `REJECTED`.

**A generated reference is never later than `REFERENCE_SELECTED`.**

## 5. Layer ordering constants

Equipment/character layers use the L0-03 §6 z-order. Typical assignments:

| Asset | Layer |
| --- | ---: |
| `PLAYER_GAMEPLAY_FRONT_BASE` | 4–6 (base legs/torso) |
| `ITEM_DEPOT_JACKET_PAPERDOLL` | 8 (chest equipment) |
| `ITEM_WORK_GLOVES_PAPERDOLL` | 14 (hands/gloves) |
| `ITEM_COURIER_NECKTAG_PAPERDOLL` | 10 (neck layer) |
| `ITEM_SIGNAL_RING_PAPERDOLL` | 14 (micro, hand-adjacent) |
| `PLAYER_VISIBLE_STATUS_OVERLAYS` | 18 (status overlay) |
| `PLAYER_HAIR_LAYER_KIT_A` | 3 + 12 (rear + front) |
| `NPC_TAMSIN_UTILITY_JACKET` | 8 |
| `NPC_TAMSIN_SATCHEL` | 2 + 17 (rear + front accessory) |
| `NPC_TAMSIN_SYSTEMS_BADGE` | 8 (on jacket surface) |
| `UI_ITEM_QUALITY_FRAMES` | 10 (icon/chrome, outside icon) |

## 6. State binding vocabulary

An asset's visibility is bound to authoritative state, never asserted by the art:

```json
{
  "source": "inventory.equipment",
  "match": { "item_id": "ITEM_DEPOT_JACKET", "slot": "body", "equipped": true },
  "visual_result": "show"
}
```

Map example:

```json
{
  "source": "world_map.nodes[].reachable",
  "value": true,
  "visual_result": "MAP_NODE_REACHABLE"
}
```

**The art never decides that a jacket is equipped.** This is restated in every
equipment specification because it is the most common integration error.

## 7. Flag naming (as authored)

```
world.free_roam_unlocked
world.district_notices_reviewed
world.workshop_rumor_heard
world.trace_echo_quest_started
```

Four opening flags, all `false` at `CONTENT_VERTICAL_SLICE_01` start. The first
three gate free-roam district content; the fourth gates the Trace Echo quest.

## 8. Provenance identity

When practical, store per asset:

- SHA-256 of source master;
- SHA-256 of runtime export;
- Git blob SHA;
- dimensions.

> Hashes identify bytes, not artistic approval.

A hash match proves the file is unchanged. It never proves the art is correct,
approved, or canon.

## 9. Provenance classification vocabulary

Source-authority classes:

- `OWNER_APPROVED_REFERENCE`
- `REPOSITORY_SOURCE_MASTER`
- `REPOSITORY_GENERATED_WORKING_ART`
- `REPOSITORY_CODE_MASTER`
- `RUNTIME_EXPORT`
- `EXTERNAL_INSPIRATION_ONLY`
- `HISTORICAL/UNVERIFIED`

External inspiration never becomes a runtime source merely because it influenced
design.

## 10. Supersession

When an asset is replaced:

- the old asset becomes `SUPERSEDED`;
- point to the replacement asset ID;
- preserve historical branch/commit;
- remove the runtime consumer only after migration;
- **do not delete evidence merely to simplify the folder.**

Do not infer that the newest PR number is automatically canonical.

## 11. Anti-patterns

| Anti-pattern | Why it is wrong |
| --- | --- |
| Renaming an ID to match a filename | breaks saves and every cross-reference |
| Reusing a retired ID for a new thing | silently corrupts existing content |
| Deriving native size from the PNG | inverts manifest authority |
| Treating a resource name as identity | drawables are renamed freely |
| Dropping historical branches "for tidiness" | destroys provenance evidence |
| Inferring canon from branch recency | PR order ≠ approval |
| Adding a new rarity tier without authority | rarity vocabulary is locked |
| Baking equipment state into art | duplicates engine logic in presentation |