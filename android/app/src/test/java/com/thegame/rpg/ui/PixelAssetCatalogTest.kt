package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertSame
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelAssetCatalogTest {
    @Test
    fun batch001ProductionAssetsHaveExactNativeDimensionsAndDefinedPaletteKeys() {
        val expected = mapOf(
            PixelAssetCatalog.PLAYER_FRONT_BASE_ID to (32 to 48),
            PixelAssetCatalog.DEPOT_JACKET_ICON_ID to (32 to 32),
            PixelAssetCatalog.DEPOT_JACKET_LAYER_ID to (32 to 48),
            PixelAssetCatalog.WORK_GLOVES_ICON_ID to (32 to 32),
            PixelAssetCatalog.WORK_GLOVES_LAYER_ID to (32 to 48),
            PixelAssetCatalog.SIGNAL_RING_ICON_ID to (32 to 32),
            PixelAssetCatalog.SIGNAL_RING_LAYER_ID to (32 to 48),
            PixelAssetCatalog.COURIER_NECKTAG_ICON_ID to (32 to 32),
            PixelAssetCatalog.COURIER_NECKTAG_LAYER_ID to (32 to 48),
            PixelAssetCatalog.MAINTENANCE_SEAL_ICON_ID to (32 to 32),
            PixelAssetCatalog.DEAD_RELAY_ICON_ID to (32 to 32),
        )

        assertEquals(
            expected.keys,
            PixelAssetCatalog.batch001ProductionAssets.map { it.assetId }.toSet(),
        )

        PixelAssetCatalog.batch001ProductionAssets.forEach { asset ->
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
    fun currentEquipmentLayersRequireExactItemAndSlotPairs() {
        assertSame(
            PixelAssetCatalog.depotJacketPaperdoll,
            PixelAssetCatalog.equipmentLayer("ITEM_DEPOT_JACKET", "body"),
        )
        assertSame(
            PixelAssetCatalog.workGlovesPaperdoll,
            PixelAssetCatalog.equipmentLayer("ITEM_WORK_GLOVES", "hands"),
        )
        assertSame(
            PixelAssetCatalog.signalRingPaperdoll,
            PixelAssetCatalog.equipmentLayer("ITEM_SIGNAL_RING", "ring_1"),
        )
        assertSame(
            PixelAssetCatalog.courierNeckTagPaperdoll,
            PixelAssetCatalog.equipmentLayer("ITEM_COURIER_NECKTAG", "neck"),
        )

        assertNull(PixelAssetCatalog.equipmentLayer("ITEM_DEPOT_JACKET", "head"))
        assertNull(PixelAssetCatalog.equipmentLayer("ITEM_WORK_GLOVES", "body"))
        assertNull(PixelAssetCatalog.equipmentLayer("ITEM_SIGNAL_RING", "ring_2"))
        assertNull(PixelAssetCatalog.equipmentLayer("ITEM_COURIER_NECKTAG", "accessory_1"))
        assertNull(PixelAssetCatalog.equipmentLayer(null, "body"))
    }

    @Test
    fun currentAuthoredInventoryItemsHaveCatalogIcons() {
        val expected = mapOf(
            "ITEM_DEPOT_JACKET" to PixelAssetCatalog.depotJacketIcon,
            "ITEM_WORK_GLOVES" to PixelAssetCatalog.workGlovesIcon,
            "ITEM_SIGNAL_RING" to PixelAssetCatalog.signalRingIcon,
            "ITEM_COURIER_NECKTAG" to PixelAssetCatalog.courierNeckTagIcon,
            "ITEM_MAINTENANCE_SEAL" to PixelAssetCatalog.maintenanceSealIcon,
            "ITEM_DEAD_RELAY" to PixelAssetCatalog.deadRelayIcon,
        )

        expected.forEach { (itemId, sprite) ->
            assertSame(sprite, PixelAssetCatalog.itemIcon(itemId))
        }

        assertNull(PixelAssetCatalog.itemIcon("ITEM_NOT_AUTHORED"))
    }

    @Test
    fun technicalHairPlaceholderIsExplicitlyOutsideProductionAssetSet() {
        assertEquals(32, PixelAssetCatalog.playerHairTechnicalPlaceholder.width)
        assertEquals(48, PixelAssetCatalog.playerHairTechnicalPlaceholder.height)
        assertTrue(
            PixelAssetCatalog.playerHairTechnicalPlaceholder !in PixelAssetCatalog.batch001ProductionAssets
        )
    }
}
