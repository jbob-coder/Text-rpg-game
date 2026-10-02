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
    fun roadAndTrackTextureOnlyRecolorsExistingNeutralSurfaces() {
        val map = PixelMapArtCatalog.gateTwelveDistrictBase

        assertTrue(map.rows.any { 'r' in it })
        assertEquals('L', map.rows[7][0])    // Perimeter street center strip.
        assertEquals('L', map.rows[78][157]) // Authored service-route center line outside landmark footprints.
        assertEquals('L', map.rows[69][21])  // Platform Nine track sleeper drawn over wear.
    }


    @Test
    fun workshopAndGateMaterialDetailsStayInsideExistingLandmarkFootprints() {
        val map = PixelMapArtCatalog.gateTwelveDistrictBase

        // Workshop Row keeps the same outer frame while gaining internal material seams.
        assertEquals('I', map.rows[8][49])
        assertEquals('S', map.rows[10][52])
        assertEquals('S', map.rows[17][54])

        // Gate Twelve keeps the same outer frame and center seam while receiving internal jamb detail.
        assertEquals('I', map.rows[56][119])
        assertEquals('S', map.rows[64][127])
        assertEquals('I', map.rows[62][133])
        assertEquals('Y', map.rows[65][136])
    }


    @Test
    fun plazaAndArchiveDetailsStayWithinTheirExistingFootprints() {
        val map = PixelMapArtCatalog.gateTwelveDistrictBase

        // Depot Plaza retains its authored paved bounds while gaining internal paver accents.
        assertEquals('P', map.rows[8][105])
        assertEquals('H', map.rows[9][111])
        assertEquals('S', map.rows[16][106])

        // Municipal Archive keeps the same shell and only gains internal institutional seams.
        assertEquals('I', map.rows[6][151])
        assertEquals('S', map.rows[8][155])
        assertEquals('I', map.rows[15][164])
        assertEquals('S', map.rows[30][154])
    }


    @Test
    fun remainingLandmarkMaterialDetailsStayInsideExistingFootprints() {
        val map = PixelMapArtCatalog.gateTwelveDistrictBase

        // Platform Nine.
        assertEquals('I', map.rows[37][20])
        assertEquals('S', map.rows[39][23])
        assertEquals('I', map.rows[40][31])

        // Relay Workbench.
        assertEquals('I', map.rows[31][75])
        assertEquals('S', map.rows[34][78])
        assertEquals('S', map.rows[37][82])

        // Quiet Stair.
        assertEquals('I', map.rows[89][88])
        assertEquals('S', map.rows[93][91])
        assertEquals('I', map.rows[96][94])

        // Service Tunnel.
        assertEquals('I', map.rows[78][161])
        assertEquals('S', map.rows[85][168])
        assertEquals('I', map.rows[87][170])
        assertEquals('L', map.rows[85][172])

        // Trace Chamber.
        assertEquals('I', map.rows[40][194])
        assertEquals('S', map.rows[43][198])
        assertEquals('S', map.rows[45][202])
        assertEquals('L', map.rows[49][205])
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
