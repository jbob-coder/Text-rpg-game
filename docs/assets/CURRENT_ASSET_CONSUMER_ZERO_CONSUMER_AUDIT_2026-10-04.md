# THE GAME — Current Asset Consumer / Zero-Consumer Audit — 2026-10-04

Status: **ACTIVE D-029 EVIDENCE / 24 CURRENT PNG CONSUMERS RESOLVED**  
Repository: `jbob-coder/Text-rpg-game`  
Branch: `docs/master-game-development-program`  
Audited source HEAD: `a785cb0e105b7fbbd0dd61339235f4989aae046f`

Machine-readable companion:

`docs/evidence/current_asset_consumer_audit_2026-10-04.json`

## 1. Purpose

This audit answers the next D-029 question:

> For each current PNG runtime asset, is there a real current consumer path, or is it a zero-consumer deletion candidate?

The audit is deliberately stricter than “the file exists.”

A raster counts as having a consumer only when the current source provides a binding path into a current UI/runtime consumer. Where authored-content reachability matters, current content is also checked.

## 2. Result

For the **24 PNG files currently under `android/app/src/main/res/drawable-nodpi/`**:

- current PNGs audited: **24 / 24**;
- current PNGs with a source consumer path: **24 / 24**;
- current PNG zero-consumer candidates: **0**;
- current PNGs authorized for deletion by this audit: **0**.

Therefore:

**None of the 24 current runtime PNGs may be classified REMOVE on zero-consumer grounds.**

This does not mean all 24 are final canon-approved art. D-029 provenance/promotion rules still apply.

## 3. Current 24-raster consumer map

| Asset ID | Drawable | Consumer path | Authored/current reachability | Result |
| --- | --- | --- | --- | --- |
| `PLAYER_GAMEPLAY_FRONT_BASE` | `pixel_player_gameplay_front_base` | PixelComponents.PlayerAvatarPanel -> rememberPixelRasters -> PixelRasterCatalog.sprite | always requested when player avatar renders | **CONSUMER PRESENT** |
| `PLAYER_HAIR_TECH_PLACEHOLDER` | `pixel_player_hair_tech_placeholder` | PixelComponents.PlayerAvatarPanel -> rememberPixelRasters -> PixelRasterCatalog.sprite | always requested when player avatar renders | **CONSUMER PRESENT** |
| `ITEM_DEPOT_JACKET_ICON` | `pixel_item_depot_jacket_icon` | PixelItemIcon -> PixelAssetCatalog.itemIcon(ITEM_DEPOT_JACKET) -> PixelRasterCatalog.sprite | ITEM_DEPOT_JACKET exists in current registry and initial inventory | **CONSUMER PRESENT** |
| `ITEM_DEPOT_JACKET_PAPERDOLL` | `pixel_item_depot_jacket_paperdoll` | PlayerAvatarPanel -> PixelAssetCatalog.equipmentOverlay(ITEM_DEPOT_JACKET, body) -> rememberPixelRasters | current registry item is equippable and present in initial inventory | **CONSUMER PRESENT** |
| `ITEM_WORK_GLOVES_ICON` | `pixel_item_work_gloves_icon` | PixelItemIcon -> PixelAssetCatalog.itemIcon(ITEM_WORK_GLOVES) -> PixelRasterCatalog.sprite | ITEM_WORK_GLOVES exists in current registry and initial inventory | **CONSUMER PRESENT** |
| `ITEM_WORK_GLOVES_PAPERDOLL` | `pixel_item_work_gloves_paperdoll` | PlayerAvatarPanel -> PixelAssetCatalog.equipmentOverlay(ITEM_WORK_GLOVES, hands) -> rememberPixelRasters | current registry item is equippable and present in initial inventory | **CONSUMER PRESENT** |
| `ITEM_SIGNAL_RING_ICON` | `pixel_item_signal_ring_icon` | PixelItemIcon -> PixelAssetCatalog.itemIcon(ITEM_SIGNAL_RING) -> PixelRasterCatalog.sprite | ITEM_SIGNAL_RING exists in current registry and initial inventory | **CONSUMER PRESENT** |
| `ITEM_SIGNAL_RING_PAPERDOLL` | `pixel_item_signal_ring_paperdoll` | PlayerAvatarPanel -> PixelAssetCatalog.equipmentOverlay(ITEM_SIGNAL_RING, ring_1) -> rememberPixelRasters | current registry item is equippable and present in initial inventory | **CONSUMER PRESENT** |
| `ITEM_COURIER_NECKTAG_ICON` | `pixel_item_courier_necktag_icon` | PixelItemIcon -> PixelAssetCatalog.itemIcon(ITEM_COURIER_NECKTAG) -> PixelRasterCatalog.sprite | ITEM_COURIER_NECKTAG exists in current registry and initial inventory | **CONSUMER PRESENT** |
| `ITEM_COURIER_NECKTAG_PAPERDOLL` | `pixel_item_courier_necktag_paperdoll` | PlayerAvatarPanel -> PixelAssetCatalog.equipmentOverlay(ITEM_COURIER_NECKTAG, neck) -> rememberPixelRasters | current registry item is equippable and present in initial inventory | **CONSUMER PRESENT** |
| `ITEM_MAINTENANCE_SEAL_ICON` | `pixel_item_maintenance_seal_icon` | PixelItemIcon -> PixelAssetCatalog.itemIcon(ITEM_MAINTENANCE_SEAL) -> PixelRasterCatalog.sprite | ITEM_MAINTENANCE_SEAL exists in current registry and initial inventory | **CONSUMER PRESENT** |
| `ITEM_DEAD_RELAY_ICON` | `pixel_item_dead_relay_icon` | PixelItemIcon and SceneIllustration relay state -> PixelAssetCatalog.relayStateSprite(intact) -> PixelRasterCatalog.sprite | ITEM_DEAD_RELAY is authored as an obtainable opening item; intact state exists before destination knowledge/damage flags | **CONSUMER PRESENT** |
| `ITEM_DEAD_RELAY_OPENED` | `pixel_item_dead_relay_opened` | SceneIllustration at RELAY_WORKBENCH -> relayStateSprite(opened) -> PixelRasterCatalog.sprite | opened projection follows KNOW_RELAY_DESTINATION_SERVICE_GATE_12 while relay remains owned | **CONSUMER PRESENT** |
| `ITEM_DEAD_RELAY_DAMAGED` | `pixel_item_dead_relay_damaged` | SceneIllustration at RELAY_WORKBENCH -> relayStateSprite(damaged) -> PixelRasterCatalog.sprite | authored force-casing failure sets relay.casing_damaged=true | **CONSUMER PRESENT** |
| `ITEM_DEAD_RELAY_SIGNAL_LOST` | `pixel_item_dead_relay_signal_lost` | SceneIllustration at RELAY_WORKBENCH -> relayStateSprite(signal_lost) -> PixelRasterCatalog.sprite | authored critical failure sets relay.signal_lost=true | **CONSUMER PRESENT** |
| `PLATFORM_NINE_SCENE` | `pixel_platform_nine_blackout_scene` | SceneIllustration -> PixelRasterCatalog.scene(PLATFORM_NINE) | world-map node exists; authored scenes OPENING_DEPOT_BLACKOUT and OPENING_DECISION use PLATFORM_NINE | **CONSUMER PRESENT** |
| `RELAY_WORKBENCH_SCENE` | `pixel_relay_workbench_default_scene` | SceneIllustration -> PixelRasterCatalog.scene(RELAY_WORKBENCH) | world-map node exists; authored relay/recovery scenes use RELAY_WORKBENCH | **CONSUMER PRESENT** |
| `GATE_TWELVE_SCENE` | `pixel_gate_twelve_sealed_scene` | SceneIllustration -> PixelRasterCatalog.scene(GATE_TWELVE) | world-map node exists; multiple authored Gate Twelve scenes use this location | **CONSUMER PRESENT** |
| `SERVICE_TUNNEL_SCENE` | `pixel_service_tunnel_default_scene` | SceneIllustration -> PixelRasterCatalog.scene(SERVICE_TUNNEL) | world-map node exists; OPENING_TUNNEL and TRACE_DIRECTIONAL_AFTERSHOCK use SERVICE_TUNNEL | **CONSUMER PRESENT** |
| `EVAC_STAIR_SCENE` | `pixel_evac_stair_default_scene` | SceneIllustration -> PixelRasterCatalog.scene(EVAC_STAIR) | world-map node exists; OPENING_SOLO_EXIT uses EVAC_STAIR | **CONSUMER PRESENT** |
| `TRACE_CHAMBER_SCENE` | `pixel_trace_chamber_idle_scene` | SceneIllustration -> PixelRasterCatalog.scene(TRACE_CHAMBER) | world-map node exists; current practice/stabilization scenes use TRACE_CHAMBER | **CONSUMER PRESENT** |
| `DISTRICT_PLAZA_SCENE` | `pixel_district_plaza_open_scene` | SceneIllustration -> PixelRasterCatalog.scene(DISTRICT_PLAZA) | world-map node exists; DISTRICT_HUB uses DISTRICT_PLAZA | **CONSUMER PRESENT** |
| `DISTRICT_ARCHIVE_SCENE` | `pixel_district_archive_default_scene` | SceneIllustration -> PixelRasterCatalog.scene(DISTRICT_ARCHIVE) | world-map node exists; DISTRICT_ARCHIVE scene uses DISTRICT_ARCHIVE | **CONSUMER PRESENT** |
| `WORKSHOP_ROW_SCENE` | `pixel_workshop_row_default_scene` | SceneIllustration -> PixelRasterCatalog.scene(WORKSHOP_ROW) | world-map node exists; DISTRICT_WORKSHOP uses WORKSHOP_ROW | **CONSUMER PRESENT** |

## 4. Why the scene PNGs are not dead assets

The current authored `world_map.nodes` contains exactly these nine location IDs:

- `PLATFORM_NINE`
- `RELAY_WORKBENCH`
- `GATE_TWELVE`
- `SERVICE_TUNNEL`
- `EVAC_STAIR`
- `TRACE_CHAMBER`
- `DISTRICT_PLAZA`
- `DISTRICT_ARCHIVE`
- `WORKSHOP_ROW`

All nine also have authored scene use in `content/vertical_slice_01.json`.

`SceneIllustration` asks `PixelRasterCatalog.scene(locationId)` for the current location and renders the resolved PNG before falling back to the Kotlin source-native scene sprite.

Therefore all nine current scene PNGs have both:

1. a current source consumer; and
2. an authored current location path.

## 5. Why the player/loadout PNGs are not dead assets

`PlayerAvatarPanel` always requests the current player base and technical hair raster IDs.

Its equipment overlay path resolves registered equipped items through `PixelAssetCatalog.equipmentOverlay`.

Current paper-doll raster mappings exist for:

- Courier neck tag / `neck`;
- Depot jacket / `body`;
- Work gloves / `hands`;
- Signal ring / `ring_1`.

All four corresponding items exist in the current authored registry and are present in the opening inventory.

The inventory item renderer resolves current item icons through `PixelAssetCatalog.itemIcon`, so the current icon rasters likewise have an active consumer path.

## 6. Dead relay state-raster reachability

The bridge projects the relay state without exposing raw flags:

- no owned relay -> no relay visual;
- `relay.signal_lost == true` -> `signal_lost`;
- `relay.casing_damaged == true` -> `damaged`;
- destination knowledge present -> `opened`;
- otherwise, while the relay is owned -> `intact`.

The authored vertical slice contains:

- an opening effect that grants `ITEM_DEAD_RELAY`;
- successful relay analysis/recovery paths that grant `KNOW_RELAY_DESTINATION_SERVICE_GATE_12`;
- a failure path setting `relay.casing_damaged = true`;
- a critical-failure path setting `relay.signal_lost = true`.

`SceneIllustration` consumes the projected relay state at `RELAY_WORKBENCH`.

Therefore the intact/opened/damaged/signal-lost raster variants are not zero-consumer placeholders.

## 7. Known deferred zero-consumer or noncurrent candidates

These are intentionally separated from the 24 current PNGs.

### `MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS`

Current D-029 classification:

`PRODUCED_DEFERRED_INTEGRATION`

Prior exact consumer audit found no current main-UI consumer.

PR #28 demonstrates a legitimate optional Service Tunnel composition that reuses it, but that behavior is not current authority.

Decision:

- retain source/provenance;
- do not delete merely because it is currently unconsumed;
- do not call it integrated;
- if selected, reimplement the composition against the destination architecture and then verify.

### PR #9 diagnostic reader icon

Branch evidence only.

No authorized current inventory consumer exists.

Decision:

- retain historical/source provenance;
- do not invent inventory semantics merely to consume the icon;
- no runtime promotion until a domain-owned consumer exists.

### PR #9 held diagnostic-reader master

Branch evidence only.

Current ownership decision: Tamsin actor-presentation art, not player equipment.

Blocked on:

- D-030 runtime actor projection;
- verified Tamsin hand/wrist anchors;
- destination composition/QA.

### PR #31 Service Tunnel ambient animation

Branch evidence only.

No current runtime consumer.

Migration contract exists; implementation remains deferred until a static Service Tunnel parent is selected and reduced-motion behavior is implemented.

## 8. Deletion rule established by this audit

A current asset is not removable merely because a newer candidate exists.

Before a future `REMOVE` classification, require:

1. exact current consumer search;
2. replacement or explicit no-longer-needed decision;
3. stable-ID/manifest/provenance migration where applicable;
4. source/raster precedence review;
5. tests for affected catalogs/consumers;
6. destination screenshot/visual evidence;
7. rollback boundary;
8. only then zero-consumer deletion.

For the current 24 PNGs, step 1 currently fails the deletion case because every raster has a consumer.

## 9. D-029 effect

This closes the **current-raster consumer / zero-consumer** subtask of D-029.

D-029 itself remains open because the following still block completion:

- fresh deterministic 24/24 raster-equivalence execution;
- repair/documentation of any mismatch if execution finds one;
- owner promotion choice for PR #27 Service Tunnel vs current baseline;
- owner promotion choice for PR #30 Quiet Stair vs current baseline;
- final Jack production sprite/portrait family;
- Tamsin/courier portrait production;
- per-family canon approval;
- destination-head visual QA and physical-device QA;
- final machine-readable provenance registry after schema/ID lock.

## 10. Verification boundary

No runtime, content, raster, Kotlin, Python or save file was changed by this audit.

No tests, builds or raster-equivalence command were executed.

The result is static source + authored-content consumer evidence at the audited source HEAD.
