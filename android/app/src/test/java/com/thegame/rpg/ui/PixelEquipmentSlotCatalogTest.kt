package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertSame
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelEquipmentSlotCatalogTest {
    @Test
    fun productionSlotIconsUseExact24By24GridAndDefinedPaletteKeys() {
        assertEquals(12, PixelEquipmentSlotCatalog.productionSlots.size)
        assertEquals(12, PixelEquipmentSlotCatalog.productionSlots.map { it.assetId }.toSet().size)

        PixelEquipmentSlotCatalog.productionSlots.forEach { icon ->
            assertEquals(24, icon.width)
            assertEquals(24, icon.height)
            assertEquals(24, icon.rows.size)
            assertTrue(icon.rows.all { it.length == 24 })

            val used = icon.rows
                .flatMap { row -> row.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()

            assertTrue(
                "${icon.assetId} contains an unmapped palette key",
                used.all { it in icon.palette },
            )
        }
    }

    @Test
    fun everyAuthoritativeEquipmentSlotMapsToItsOwnIcon() {
        val expected = mapOf(
            "head" to PixelEquipmentSlotCatalog.head,
            "body" to PixelEquipmentSlotCatalog.body,
            "hands" to PixelEquipmentSlotCatalog.hands,
            "legs" to PixelEquipmentSlotCatalog.legs,
            "feet" to PixelEquipmentSlotCatalog.feet,
            "main_hand" to PixelEquipmentSlotCatalog.mainHand,
            "off_hand" to PixelEquipmentSlotCatalog.offHand,
            "ring_1" to PixelEquipmentSlotCatalog.ring1,
            "ring_2" to PixelEquipmentSlotCatalog.ring2,
            "neck" to PixelEquipmentSlotCatalog.neck,
            "accessory_1" to PixelEquipmentSlotCatalog.accessory1,
            "accessory_2" to PixelEquipmentSlotCatalog.accessory2,
        )

        expected.forEach { (slotId, icon) ->
            assertSame(icon, PixelEquipmentSlotCatalog.slot(slotId))
        }
        assertEquals(expected.values.toSet().size, expected.size)
        assertNull(PixelEquipmentSlotCatalog.slot("unknown_slot"))
    }
}
