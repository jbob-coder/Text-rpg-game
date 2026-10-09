# Character, Equipment, Item, and Actor Asset Provenance — 2026-10-03

Status: **ACTIVE / D-029 CHILD LEDGER / SOURCE-GROUNDED PARTIAL**  
Repository: `jbob-coder/Text-rpg-game`  
Inspected implementation baseline: `docs/master-game-development-program@2ad50d7aff6f153b90036f8e0f61043242a09765`  
Parent: [Asset Family Provenance Index](ASSET_FAMILY_PROVENANCE_INDEX_2026-10-03.md)

## 1. Scope

This ledger covers the character-facing visual families that currently exist or have exact branch evidence:

- player body/base;
- player hair placeholder;
- character staging;
- current item icons;
- current equipment paper-doll layers;
- equipment slot icons;
- item-quality frames;
- opening-story actors;
- Jack approved visual reference relationship;
- portrait status;
- divergent/deferred held-prop family where it affects character composition.

It does not make gameplay authority visual. Equipment state remains engine-owned; these assets only render player-safe projected state.

## 2. Current runtime chain

Verified current implementation:

`authoritative projected inventory/equipment -> PixelAssetCatalog -> PixelRasterCatalog when bound -> PixelComponents / CharacterSection -> Compose`

For player/equipment/item assets, PNG-backed rasters are preferred when a binding exists. The Kotlin sprite is the source-native fallback.

Current source files:

- `android/app/src/main/java/com/thegame/rpg/ui/PixelAssetCatalog.kt` — blob `dc6f1d553dbb8abbccecef728ee67bbf54bad3c2`.
- `android/app/src/main/java/com/thegame/rpg/ui/PixelRasterCatalog.kt` — blob `6bfc11c88df1d2edb473ed8b3cd3293e7f2822d8`.
- `android/app/src/main/java/com/thegame/rpg/ui/PixelCharacterStagingCatalog.kt` — blob `b21a8a15913da87764b524c3b0d8fd22a55de48a`.
- `android/app/src/main/java/com/thegame/rpg/ui/PixelEquipmentSlotCatalog.kt` — blob `f274a970ba4cba6c9917441a387784e546efe263`.
- `android/app/src/main/java/com/thegame/rpg/ui/PixelItemQualityFrameCatalog.kt` — blob `6da86938167c63cc2fb361f603ec1abdf96248a1`.
- `android/app/src/main/java/com/thegame/rpg/ui/PixelStoryActorCatalog.kt` — blob `8714a2f1aa5aed497bd6a71f3d50acc0ac980783`.

Primary current consumers inspected:

- `PixelComponents.kt` — blob `c07a0cc784b9b49171bc44ce16485d0f3348c17a`;
- `CharacterSection.kt` — blob `5fb30a6044c71a27c206cc4c67c3b21eb45528e7`;
- `SceneIllustration.kt` — blob `619c9cf5f6610f9ab9e118b8cab3ab3a875031f4`.

## 3. Player base and hair family

### 3.1 Asset IDs

- `PLAYER_GAMEPLAY_FRONT_BASE`
- `PLAYER_HAIR_TECH_PLACEHOLDER`

### 3.2 Source/code master

Current program-branch source-native fallback geometry lives in `PixelAssetCatalog.kt`.

Historical family root: PR #7, `feature/pixel-asset-wave-a@a3970de6597c77939afccb5f30d6040bdf3d608d`.

### 3.3 Raster exports

Current bound PNGs:

- `android/app/src/main/res/drawable-nodpi/pixel_player_gameplay_front_base.png`
  - Git blob: `d7cb5cd57a5e75dead06dd0db002a9e5894ffbeb`
  - native size: 32x48
  - SHA-256 recorded in `docs/evidence/raster_bindings_2026-10-02.json`: `ba7ba95e041db5d8a5b7519386e809525a9ad46950a63dc5d1e1db772def5baa`
- `android/app/src/main/res/drawable-nodpi/pixel_player_hair_tech_placeholder.png`
  - Git blob: `2cc4da04af11acfb332318c1e58df7b846530799`
  - native size: 32x48
  - SHA-256: `8170cff7377a8375e1a4ec81a80182b690f42e6810dde66f1daed6f7753087f7`

Raster delivery root: inherited PR #19, `feature/png-pixel-art-runtime-a@c11133122d47009abc71e8c6e91c08aedbe91ae2`.

### 3.4 Runtime consumer and precedence

`PlayerAvatarPanel` in `PixelComponents.kt` requests raster sprites for both IDs. If a raster exists it is drawn; otherwise the Kotlin sprite is drawn.

This means changing the Kotlin fallback alone does not necessarily change the visible player.

### 3.5 Integration/stage

- current runtime: **INTEGRATED**
- source-native code: **CODE_PRESENT**
- PNG: **RASTER_PRESENT**
- canon/final Jack identity: **NOT ESTABLISHED**
- hair asset: explicitly a technical placeholder, not a production-final identity asset

Current stage:

`RASTER_PRESENT + CODE_PRESENT + INTEGRATED`

Do **not** promote to `CANON_APPROVED`.

### 3.6 QA evidence

Current test source:

`PixelAssetCatalogTest.kt` — blob `9974215642f0cacf87ade9218f2d7e4dace548c7`

Relevant tests include:

- exact native dimensions/palette keys;
- rig anchors and readable current loadout;
- explicit technical-hair-placeholder classification.

Historical CI: PR #19 workflow run 36823014708 succeeded for the raster-delivery head. This documentation slice did not rerun runtime tests.

### 3.7 Missing work / risk

Missing:

- production Jack front/base identity art;
- non-placeholder hair/face identity;
- side/back/animation family if later required;
- explicit source-authoring lineage for the PNG export;
- owner visual approval;
- device-scale QA.

Risk:

- editing only `PixelAssetCatalog` can be visually hidden by the existing PNG binding.

## 4. Current item icon family

### 4.1 Asset IDs

- `ITEM_DEPOT_JACKET_ICON`
- `ITEM_WORK_GLOVES_ICON`
- `ITEM_SIGNAL_RING_ICON`
- `ITEM_COURIER_NECKTAG_ICON`
- `ITEM_MAINTENANCE_SEAL_ICON`
- `ITEM_DEAD_RELAY_ICON`
- `ITEM_DEAD_RELAY_OPENED`
- `ITEM_DEAD_RELAY_DAMAGED`
- `ITEM_DEAD_RELAY_SIGNAL_LOST`

The dead-relay family contains state variants and must remain semantically separate from the generic base item icon.

### 4.2 Source and raster

Source-native fallbacks: `PixelAssetCatalog.kt`.

All IDs above are bound by `PixelRasterCatalog.sprite(assetId)` to PNG resources delivered on the inherited raster line.

Per-file blob, SHA-256, dimensions, resource name, and catalog binding are already recorded in:

- `docs/assets/RASTER_DELIVERY_EVIDENCE_2026-10-02.md`
- `docs/evidence/raster_bindings_2026-10-02.json`

This child ledger does not duplicate those exact hash rows.

### 4.3 Runtime consumer

`PixelItemIcon` in `PixelComponents.kt`:

1. resolves the item sprite from `PixelAssetCatalog.itemIcon(itemId)`;
2. resolves raster through `PixelRasterCatalog.sprite(sprite.assetId)`;
3. draws raster if present;
4. otherwise draws source-native sprite;
5. draws an optional quality frame separately.

### 4.4 Reuse rule

An item icon may be reused only for the same semantic item/state or a documented derivative. Do not reuse the dead-relay state variants as generic electronics icons.

### 4.5 Stage

`RASTER_PRESENT + CODE_PRESENT + INTEGRATED`

Visual/canon approval remains separate.

## 5. Current equipment paper-doll layer family

### 5.1 Asset IDs

- `ITEM_DEPOT_JACKET_PAPERDOLL`
- `ITEM_WORK_GLOVES_PAPERDOLL`
- `ITEM_SIGNAL_RING_PAPERDOLL`
- `ITEM_COURIER_NECKTAG_PAPERDOLL`

Current exact logical item/slot bindings are maintained by `PixelAssetCatalog.equipmentOverlay(itemId, slot)`.

### 5.2 Raster exports

All four current layers have 32x48 PNG exports bound through `PixelRasterCatalog`.

Example exact raster evidence:

- Depot Jacket paper doll: blob `b877935b3f637e95b863ae9533616d6771bc6e8b`.
- Courier Neck Tag paper doll: blob `325a95cee3165eb96145cec335eff545bd8ab7f8`, SHA-256 `052232579cbffb9cc1e5467f82a1fae399ec302aa67d16ef0508b54949c09498`.
- Work Gloves paper doll: blob `9354066c3149e60e0521509c4f7a38220c54049f`, SHA-256 `1656502a49b905ef469581d8a70d9c02c65977c2e27d048303cdabf2fbe16697`.

Use the raster evidence JSON for the complete exact set.

### 5.3 Runtime consumer

`PlayerAvatarPanel` collects only explicitly mapped equipment overlays and sorts them by `zOrder`.

The source contains an explicit runtime comment that all equipped visuals share the 32x48 rig and that PNG-backed layers are preferred while source-native sprites remain fallback.

Unmapped equipment remains logically equipped; the UI must not invent geometry for it.

### 5.4 Branch provenance

- root family: PR #7;
- overlay-rig contract: inherited PR #10;
- current program branch retains the same `PixelAssetCatalog.kt` blob inspected above;
- PNG delivery: inherited PR #19.

### 5.5 Stage and migration risk

Stage:

`RASTER_PRESENT + CODE_PRESENT + INTEGRATED`

Missing:

- authored visuals for the rest of the supported equipment slots/items;
- held-object anchor integration;
- final Jack identity alignment;
- physical-device visual QA.

Migration risk:

- slot names, 32x48 origin, z-order, and exact item+slot pairing are structural contracts. Replacing art without preserving those relationships can mis-layer equipment or falsely display unsupported items.

## 6. Equipment slot icon family

### 6.1 IDs

`PixelEquipmentSlotCatalog.kt` defines twelve current presentation IDs:

- `UI_EQUIPMENT_SLOT_HEAD`
- `UI_EQUIPMENT_SLOT_CHEST`
- `UI_EQUIPMENT_SLOT_HANDS`
- `UI_EQUIPMENT_SLOT_LEGS`
- `UI_EQUIPMENT_SLOT_FEET`
- `UI_EQUIPMENT_SLOT_MAIN_HAND`
- `UI_EQUIPMENT_SLOT_OFF_HAND`
- `UI_EQUIPMENT_SLOT_RING_1`
- `UI_EQUIPMENT_SLOT_RING_2`
- `UI_EQUIPMENT_SLOT_NECK`
- `UI_EQUIPMENT_SLOT_ACCESSORY_1`
- `UI_EQUIPMENT_SLOT_ACCESSORY_2`

### 6.2 Form / integration

Current master form: procedural Kotlin code. No PNG export was found for this family on the inspected program branch.

Consumer: Character/equipment UI, including `CharacterSection.kt`.

Stage:

`SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED`

### 6.3 QA

`PixelEquipmentSlotCatalogTest.kt` blob `0f41f652c2c9b0fe8f08b565e039bea0c517e97c` verifies 24x24 production slot grids and one mapping per authoritative equipment slot.

Historical root: PR #7.

## 7. Item-quality frame family

IDs:

- `UI_ITEM_QUALITY_FRAME_STANDARD`
- `UI_ITEM_QUALITY_FRAME_UNCOMMON`

Source:

`PixelItemQualityFrameCatalog.kt` — procedural 32x32 frames.

Consumer:

`PixelItemIcon` in `PixelComponents.kt`.

QA:

`PixelItemQualityFrameCatalogTest.kt` blob `f51c3ff757bcab49c8abc4df83846b98fed261c5` verifies exact 32x32 transparent masters and explicit supported-quality mapping.

Stage:

`SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED`

Missing:

- explicit final quality taxonomy beyond currently supported values;
- final visual approval;
- migration packet if quality semantics change in item/economy redesign.

## 8. Character staging family

Current ID:

- `CHARACTER_GROUND_SHADOW_MEDIUM`

Source:

`PixelCharacterStagingCatalog.kt` — blob `b21a8a15913da87764b524c3b0d8fd22a55de48a`.

Historical introduction/current inherited line: PR #16 `feature/pixel-assets-runtime-expansion@ddbb5f4250e26b99765999d0a8e81f59cb1ea26c`.

Consumer:

`PlayerAvatarPanel` in `PixelComponents.kt`.

QA:

`PixelCharacterStagingCatalogTest.kt` blob `734affa2492f185e15e5c8be9a2b4ff243eab859`.

Stage:

`SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED`

Reuse rule:

The shadow is a staging utility, not character identity art. It may be reused only where scale/origin and presentation semantics match.

## 9. Opening-story actor family

### 9.1 IDs

Current source contains:

- `NPC_TAMSIN_TURNAROUND`
- `SUPPORT_COURIER_01`

Current placements are keyed to player-facing location/scene combinations for the opening sequence.

### 9.2 Source

`PixelStoryActorCatalog.kt` — blob `8714a2f1aa5aed497bd6a71f3d50acc0ac980783`.

Inherited implementation root:

PR #23 `feature/opening-story-actor-pixel-art@9f3cf193619e1db3845c1bc71f4592c7ac62db76`.

### 9.3 Runtime consumer

`SceneIllustration.kt` calls:

`PixelStoryActorCatalog.placements(locationId, sceneId)`

and draws the returned actor sprites into the scene.

This is current presentation behavior, not final actor-state authority.

### 9.4 Authority/migration status

D-030 has documented the target player-safe room-actor projection. That projection is **not implemented**.

Therefore:

- actor sprites: **INTEGRATED**
- actor-presence ownership: **MIGRATION REQUIRED**
- hidden NPC state must not be read by Compose to replace the current heuristic.

### 9.5 QA

`PixelStoryActorCatalogTest.kt` blob `314fb71166ff7f2088022dcf9e54c9be5b5e86fe` verifies:

- defined palettes/scene-scale bounds;
- Tamsin silhouette anchors;
- placements based only on projected scene/location IDs.

### 9.6 Post-D-064 current-state addendum — 2026-10-08

**Temporal correction:** Sections 9.1–9.5 above document the historical PR #23/October-03 state. Their phrases "current placements", `placements(locationId, sceneId)`, and "projection is not implemented" are **not the current authority-branch API/status**. Do not retroactively change the historical blob/QA provenance; use this addendum for present integration.

At inspected authority HEAD `247b1305461194ba97a06e9ae652409c0b242ee9`, `src/textrpg/android_bridge.py::_room_view_for` projects authored visible presence, `GameEngine.kt::GameRoomProjection` / `GameRoomActor` map typed public records, and both Story scene consumers supply `snapshot.room.actors` to `SceneIllustration(roomActors)`. `SceneIllustration.kt` now calls **`PixelStoryActorCatalog.placements(roomActors)`**. `PixelStoryActorCatalog.kt` maps only allowlisted `visualFamily` values and `PixelStoryActorPlacementResolver.resolve(placementKey)` supplies local 128×64 scene-sheet art coordinates; unknown families/keys render no actor. Compose does **not** decide actor presence from scene/location IDs.

The integrated art remains `NPC_TAMSIN_TURNAROUND` and `SUPPORT_COURIER_01` (32×48 each), but current `PixelStoryActorCatalog.kt` blob is `ef559b1248aa389e7fde5aeb3b7e5abab455f56e`, not the historical §9.2 blob. Current `PixelStoryActorCatalogTest.kt` checks projected-only actor lists, unknown-safe omission and equivalence at Platform Nine courier (34,13), Platform Nine Tamsin (62,14), Relay Workbench (90,14), Service Tunnel (76,14); §9.5's scene-ID-based test description is a historical checkpoint.

**Verified implementation evidence:** [D-064 final room/actor projection evidence](../evidence/D064_PLAYER_SAFE_ROOM_ACTOR_PROJECTION_FINAL_2026-10-05.md) documents PR #70 merge `d7ebb7ca439695e256a429a1e5d160daae69a521` and historical workflow run #362 Python/Android/emulator acceptance. This addendum is source review only; those tests were **not rerun here**. D-064 room-presence migration is complete; D-030 broader context-panel/focus/actor interaction extensions are still separate work. Preserve `room` player-safe privacy and the 11-key mapper allowlist. Do not infer NPC identity/presence from artwork, scene name, location, or private social state.

## 10. Jack approved reference and PR #22 clarification

PR #22 current head:

`feature/player-avatar-art-pass@494f2b3f0dedbcb90c202aab7380694c4daf33f3`

Its inherited base ancestor used by PR #23 is:

`2a1c7f59843f0ff248daba97781ca99279829b6c`.

Exact comparison of those two commits shows the three-commit PR #22 tail changes only:

- `docs/assets/README.md`;
- `docs/assets/REFERENCE_REGISTRY.md`;
- `docs/assets/references/UI_REFERENCE_CHARACTER_APPROVED_V1.md`.

Representative runtime files and rasters inspected at the program branch, the inherited ancestor, and PR #22 head are byte-identical:

- `PixelAssetCatalog.kt`;
- `pixel_player_gameplay_front_base.png`;
- `pixel_player_hair_tech_placeholder.png`;
- `pixel_item_depot_jacket_paperdoll.png`.

Decision:

The PR #22 tail is **REFERENCE / DOCUMENTATION EVIDENCE**, not proof of a newer integrated runtime avatar.

Do not claim the approved Jack reference is already the runtime sprite.

## 11. Portrait family status

### VERIFIED CURRENT IMPLEMENTATION

No dedicated canonical character portrait catalog or portrait PNG family was found in the inspected program-branch catalog set.

`PixelTraceStrainCatalog` does generate `FX_TRACE_STRAIN_PORTRAIT_FRAME_*` effect frames, but those are strain-effect presentation assets, not canonical character portraits.

### ESTABLISHED DESIGN

The broader visual program expects character portraits/context panels.

### CURRENT STAGE

`PLANNED / SOURCE MASTER NOT PRESENT`

### Missing work

At minimum:

- Jack canonical portrait master;
- Tamsin portrait master;
- support/named actor portrait policy;
- context-panel crop/framing contract;
- variant/state rules;
- source-to-raster/export lineage;
- runtime consumer;
- owner approval;
- mobile QA.

## 12. Reconstruction instructions

To rebuild this family correctly:

1. restore `PixelAssetCatalog` stable IDs and the 32x48 player rig;
2. restore current PNG files and `PixelRasterCatalog` bindings;
3. preserve raster-first/fallback behavior unless migration explicitly changes it;
4. restore exact item+slot overlay mapping and z-order;
5. restore the twelve equipment slot presentation IDs;
6. restore item-quality frames as separate UI decoration;
7. restore staging separately from identity art;
8. restore actor sprites, but do not treat `PixelStoryActorCatalog` as final actor-presence authority;
9. keep Jack reference documentation separate from runtime-art claims;
10. do not invent portraits that the repository does not contain;
11. run catalog/unit tests and screenshot/device QA before marking replacement assets verified or canon-approved.

## 13. Remaining provenance gaps

- source-authoring lineage for current player/equipment/item PNG exports;
- final Jack sprite production;
- production portrait family;
- non-current equipment visual coverage;
- held-object/prop integration;
- actor projection implementation;
- exact visual QA at the final destination head;
- canon approval.
