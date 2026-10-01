package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertSame
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelMapArtCatalogTest {
    @Test
    fun gateTwelveDistrictBaseUsesFixedNativePixelGrid() {
        val map = PixelMapArtCatalog.gateTwelveDistrictBase
        assertEquals(PixelMapArtCatalog.GATE_TWELVE_DISTRICT_BASE_ID, map.assetId)
        assertEquals(128, map.width)
        assertEquals(72, map.height)
        assertEquals(72, map.rows.size)
        assertTrue(map.rows.all { it.length == 128 })

        val usedKeys = map.rows.flatMap { it.toList() }.toSet()
        assertTrue(usedKeys.all { it in map.palette })
    }

    @Test
    fun mapArtLookupIsExplicitAndNeverBorrowsUnrelatedArt() {
        assertSame(
            PixelMapArtCatalog.gateTwelveDistrictBase,
            PixelMapArtCatalog.base("Gate Twelve District"),
        )
        assertNull(PixelMapArtCatalog.base("Unknown District"))
    }
}
