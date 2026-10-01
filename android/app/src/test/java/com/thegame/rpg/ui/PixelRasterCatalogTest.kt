package com.thegame.rpg.ui

import org.junit.Assert.assertNotNull
import org.junit.Assert.assertNull
import org.junit.Test

class PixelRasterCatalogTest {
    @Test
    fun openingSceneAndCurrentVisibleLoadoutHaveRasterMappings() {
        assertNotNull(PixelRasterCatalog.scene("PLATFORM_NINE"))
        assertNotNull(PixelRasterCatalog.sprite(PixelAssetCatalog.PLAYER_FRONT_BASE_ID))
        assertNotNull(PixelRasterCatalog.sprite(PixelAssetCatalog.PLAYER_HAIR_PLACEHOLDER_ID))
        assertNotNull(PixelRasterCatalog.sprite(PixelAssetCatalog.DEPOT_JACKET_LAYER_ID))
        assertNotNull(PixelRasterCatalog.sprite(PixelAssetCatalog.DEPOT_JACKET_ICON_ID))
        assertNotNull(PixelRasterCatalog.sprite(PixelAssetCatalog.WORK_GLOVES_LAYER_ID))
        assertNotNull(PixelRasterCatalog.sprite(PixelAssetCatalog.WORK_GLOVES_ICON_ID))
        assertNotNull(PixelRasterCatalog.sprite(PixelAssetCatalog.SIGNAL_RING_LAYER_ID))
        assertNotNull(PixelRasterCatalog.sprite(PixelAssetCatalog.SIGNAL_RING_ICON_ID))
    }

    @Test
    fun unexportedRasterStillFallsBackToSourceNativeSprite() {
        assertNull(PixelRasterCatalog.scene("GATE_TWELVE"))
        assertNull(PixelRasterCatalog.sprite(PixelAssetCatalog.COURIER_NECKTAG_LAYER_ID))
    }
}
