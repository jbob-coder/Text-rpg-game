package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertSame
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelAssetCatalogTest {
    @Test
    fun waveAProductionAssetsHaveExactNativeDimensionsAndDefinedPaletteKeys() {
        val expected = mapOf(
            PixelAssetCatalog.PLAYER_FRONT_BASE_ID to (32 to 48),
            PixelAssetCatalog.DEPOT_JACKET_ICON_ID to (32 to 32),
            PixelAssetCatalog.DEPOT_JACKET_LAYER_ID to (32 to 48),
        )

        assertEquals(expected.keys, PixelAssetCatalog.waveAProductionAssets.map { it.assetId }.toSet())

        PixelAssetCatalog.waveAProductionAssets.forEach { asset ->
            val dimensions = expected.getValue(asset.assetId)
            assertEquals(dimensions.first, asset.width)
            assertEquals(dimensions.second, asset.height)
            assertEquals(asset.height, asset.rows.size)
            assertTrue(asset.rows.all { it.length == asset.width })

            val usedKeys = asset.rows
                .flatMap { row -> row.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()

            assertTrue(
                "${asset.assetId} contains an unmapped palette key",
                usedKeys.all { it in asset.palette },
            )
        }
    }

    @Test
    fun depotJacketLayerRequiresExactItemAndBodySlot() {
        assertSame(
            PixelAssetCatalog.depotJacketPaperdoll,
            PixelAssetCatalog.equipmentLayer("ITEM_DEPOT_JACKET", "body"),
        )

        assertNull(PixelAssetCatalog.equipmentLayer("ITEM_DEPOT_JACKET", "head"))
        assertNull(PixelAssetCatalog.equipmentLayer("ITEM_WORK_GLOVES", "body"))
        assertNull(PixelAssetCatalog.equipmentLayer(null, "body"))
    }

    @Test
    fun depotJacketIconDoesNotLeakOntoOtherInventoryItems() {
        assertSame(
            PixelAssetCatalog.depotJacketIcon,
            PixelAssetCatalog.itemIcon("ITEM_DEPOT_JACKET"),
        )
        assertNull(PixelAssetCatalog.itemIcon("ITEM_WORK_GLOVES"))
        assertNull(PixelAssetCatalog.itemIcon("ITEM_SIGNAL_RING"))
    }

    @Test
    fun technicalHairPlaceholderIsExplicitlyOutsideProductionAssetSet() {
        assertEquals(32, PixelAssetCatalog.playerHairTechnicalPlaceholder.width)
        assertEquals(48, PixelAssetCatalog.playerHairTechnicalPlaceholder.height)
        assertTrue(
            PixelAssetCatalog.playerHairTechnicalPlaceholder !in PixelAssetCatalog.waveAProductionAssets
        )
    }
}
