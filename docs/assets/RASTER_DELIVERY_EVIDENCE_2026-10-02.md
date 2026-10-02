# Raster delivery evidence — 2026-10-02

Baseline `4d596bcd27b6e2f8ef9ce3a93b9dab22f5f4812e`. All 24 tracked PNGs parsed for dimensions, hashed and matched to literal resource bindings. Catalog binding is static source evidence; this batch does not claim decoded-device rendering, source/raster pixel equality, later-branch provenance or art approval.

[Machine-readable evidence](../evidence/raster_bindings_2026-10-02.json).

| Raster | Dimensions | Asset symbol | Location |
| --- | --- | --- | --- |
| `pixel_district_archive_default_scene` | 128×64 | `PixelSceneCatalog.DISTRICT_ARCHIVE_SCENE_ID` | DISTRICT_ARCHIVE |
| `pixel_district_plaza_open_scene` | 128×64 | `PixelSceneCatalog.DISTRICT_PLAZA_SCENE_ID` | DISTRICT_PLAZA |
| `pixel_evac_stair_default_scene` | 128×64 | `PixelSceneCatalog.EVAC_STAIR_SCENE_ID` | EVAC_STAIR |
| `pixel_gate_twelve_sealed_scene` | 128×64 | `PixelSceneCatalog.GATE_TWELVE_SCENE_ID` | GATE_TWELVE |
| `pixel_item_courier_necktag_icon` | 32×32 | `PixelAssetCatalog.COURIER_NECKTAG_ICON_ID` | item/player family |
| `pixel_item_courier_necktag_paperdoll` | 32×48 | `PixelAssetCatalog.COURIER_NECKTAG_LAYER_ID` | item/player family |
| `pixel_item_dead_relay_damaged` | 32×32 | `PixelAssetCatalog.DEAD_RELAY_DAMAGED_ID` | item/player family |
| `pixel_item_dead_relay_icon` | 32×32 | `PixelAssetCatalog.DEAD_RELAY_ICON_ID` | item/player family |
| `pixel_item_dead_relay_opened` | 32×32 | `PixelAssetCatalog.DEAD_RELAY_OPENED_ID` | item/player family |
| `pixel_item_dead_relay_signal_lost` | 32×32 | `PixelAssetCatalog.DEAD_RELAY_SIGNAL_LOST_ID` | item/player family |
| `pixel_item_depot_jacket_icon` | 32×32 | `PixelAssetCatalog.DEPOT_JACKET_ICON_ID` | item/player family |
| `pixel_item_depot_jacket_paperdoll` | 32×48 | `PixelAssetCatalog.DEPOT_JACKET_LAYER_ID` | item/player family |
| `pixel_item_maintenance_seal_icon` | 32×32 | `PixelAssetCatalog.MAINTENANCE_SEAL_ICON_ID` | item/player family |
| `pixel_item_signal_ring_icon` | 32×32 | `PixelAssetCatalog.SIGNAL_RING_ICON_ID` | item/player family |
| `pixel_item_signal_ring_paperdoll` | 32×48 | `PixelAssetCatalog.SIGNAL_RING_LAYER_ID` | item/player family |
| `pixel_item_work_gloves_icon` | 32×32 | `PixelAssetCatalog.WORK_GLOVES_ICON_ID` | item/player family |
| `pixel_item_work_gloves_paperdoll` | 32×48 | `PixelAssetCatalog.WORK_GLOVES_LAYER_ID` | item/player family |
| `pixel_platform_nine_blackout_scene` | 128×64 | `PixelSceneCatalog.PLATFORM_NINE_SCENE_ID` | PLATFORM_NINE |
| `pixel_player_gameplay_front_base` | 32×48 | `PixelAssetCatalog.PLAYER_FRONT_BASE_ID` | item/player family |
| `pixel_player_hair_tech_placeholder` | 32×48 | `PixelAssetCatalog.PLAYER_HAIR_PLACEHOLDER_ID` | item/player family |
| `pixel_relay_workbench_default_scene` | 128×64 | `PixelSceneCatalog.RELAY_WORKBENCH_SCENE_ID` | RELAY_WORKBENCH |
| `pixel_service_tunnel_default_scene` | 128×64 | `PixelSceneCatalog.SERVICE_TUNNEL_SCENE_ID` | SERVICE_TUNNEL |
| `pixel_trace_chamber_idle_scene` | 128×64 | `PixelSceneCatalog.TRACE_CHAMBER_SCENE_ID` | TRACE_CHAMBER |
| `pixel_workshop_row_default_scene` | 128×64 | `PixelSceneCatalog.WORKSHOP_ROW_SCENE_ID` | WORKSHOP_ROW |

## Remaining work

Compare each source master with its exported PNG; trace source-authoring commits; inspect later PR variant consumers; add canonical approval/evidence separately. The front/hair placeholder remains provisional. Room actors are Kotlin source art at this baseline and are not among these 24 rasters. The ninth scene/location binding includes Quiet Stair under EVAC_STAIR; stable IDs remain unchanged.
