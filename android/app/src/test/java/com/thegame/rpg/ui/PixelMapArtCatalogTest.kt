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
        assertEquals(256, map.width)
        assertEquals(144, map.height)
        assertEquals(144, map.rows.size)
        assertTrue(map.rows.all { it.length == 256 })

        val usedKeys = map.rows.flatMap { it.toList() }.toSet()
        assertTrue(usedKeys.all { it in map.palette })
    }


    @Test
    fun gateTwelveDistrictUsesLayeredStaticMaterialTextureWithoutMovingLandmarks() {
        val map = PixelMapArtCatalog.gateTwelveDistrictBase

        assertTrue(map.rows.take(48).any { 'c' in it })
        assertTrue(map.rows.slice(48..94).any { 's' in it })
        assertTrue(map.rows.drop(95).any { 'm' in it })

        // Representative landmark anchors remain authored by the geometry pass that follows
        // the texture layer.
        assertEquals('I', map.rows[8][49])   // Workshop Row outer frame.
        assertEquals('Y', map.rows[65][136]) // Gate Twelve center indicator.
        assertEquals('I', map.rows[87][170]) // Service Tunnel support rib.
    }

    @Test
    fun authoredMapViewportUsesIntegerPixelScaleAndSharedPercentageCoordinates() {
        val viewport = PixelMapArtCatalog.viewport(
            mapTitle = "Gate Twelve District",
            canvasWidth = 300f,
            canvasHeight = 220f,
        )
        assertEquals(1f, viewport.pixelSize, 0.001f)
        assertEquals(22f, viewport.originX, 0.001f)
        assertEquals(38f, viewport.originY, 0.001f)
        assertEquals(256f, viewport.width, 0.001f)
        assertEquals(144f, viewport.height, 0.001f)

        val platform = viewport.point(18.0, 36.0)
        assertEquals(68.08f, platform.x, 0.01f)
        assertEquals(89.84f, platform.y, 0.01f)
    }

    @Test
    fun unknownMapViewportPreservesLegacyFullCanvasProjection() {
        val viewport = PixelMapArtCatalog.viewport(
            mapTitle = "Unknown District",
            canvasWidth = 300f,
            canvasHeight = 220f,
        )
        assertEquals(0f, viewport.originX, 0.001f)
        assertEquals(0f, viewport.originY, 0.001f)
        assertEquals(300f, viewport.width, 0.001f)
        assertEquals(220f, viewport.height, 0.001f)
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
