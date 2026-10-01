package com.thegame.rpg.ui

import org.junit.Assert.assertNotNull
import org.junit.Assert.assertNull
import org.junit.Test

class PixelRasterCatalogTest {
    @Test
    fun everyCurrentNamedSceneHasRasterDelivery() {
        listOf(
            "PLATFORM_NINE",
            "RELAY_WORKBENCH",
            "GATE_TWELVE",
            "SERVICE_TUNNEL",
            "EVAC_STAIR",
            "TRACE_CHAMBER",
            "DISTRICT_PLAZA",
            "DISTRICT_ARCHIVE",
            "WORKSHOP_ROW",
        ).forEach { locationId ->
            assertNotNull("Missing raster scene for $locationId", PixelRasterCatalog.scene(locationId))
        }
    }

    @Test
    fun currentPlayerLoadoutAndRelayArtHaveRasterDelivery() {
        listOf(
            PixelAssetCatalog.PLAYER_FRONT_BASE_ID,
            PixelAssetCatalog.PLAYER_HAIR_PLACEHOLDER_ID,
            PixelAssetCatalog.DEPOT_JACKET_LAYER_ID,
            PixelAssetCatalog.DEPOT_JACKET_ICON_ID,
            PixelAssetCatalog.WORK_GLOVES_LAYER_ID,
            PixelAssetCatalog.WORK_GLOVES_ICON_ID,
            PixelAssetCatalog.SIGNAL_RING_LAYER_ID,
            PixelAssetCatalog.SIGNAL_RING_ICON_ID,
            PixelAssetCatalog.COURIER_NECKTAG_LAYER_ID,
            PixelAssetCatalog.COURIER_NECKTAG_ICON_ID,
            PixelAssetCatalog.MAINTENANCE_SEAL_ICON_ID,
            PixelAssetCatalog.DEAD_RELAY_ICON_ID,
            PixelAssetCatalog.DEAD_RELAY_OPENED_ID,
            PixelAssetCatalog.DEAD_RELAY_DAMAGED_ID,
            PixelAssetCatalog.DEAD_RELAY_SIGNAL_LOST_ID,
        ).forEach { assetId ->
            assertNotNull("Missing raster sprite for $assetId", PixelRasterCatalog.sprite(assetId))
        }
    }

    @Test
    fun unknownRasterStillFallsBackToSourceNativePath() {
        assertNull(PixelRasterCatalog.scene("UNKNOWN_LOCATION"))
        assertNull(PixelRasterCatalog.sprite("UNKNOWN_ASSET"))
    }
}
