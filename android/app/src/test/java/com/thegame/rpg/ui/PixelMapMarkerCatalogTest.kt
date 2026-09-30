package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertSame
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelMapMarkerCatalogTest {
    @Test
    fun productionMarkersUseExact16By16GridAndDefinedPaletteKeys() {
        assertEquals(
            setOf(
                PixelMapMarkerCatalog.PLAYER_MARKER_ID,
                PixelMapMarkerCatalog.DISCOVERED_MARKER_ID,
                PixelMapMarkerCatalog.CURRENT_MARKER_ID,
                PixelMapMarkerCatalog.REACHABLE_MARKER_ID,
                PixelMapMarkerCatalog.UNAVAILABLE_MARKER_ID,
            ),
            PixelMapMarkerCatalog.productionMarkers.map { it.assetId }.toSet(),
        )

        PixelMapMarkerCatalog.productionMarkers.forEach { marker ->
            assertEquals(16, marker.width)
            assertEquals(16, marker.height)
            assertEquals(16, marker.rows.size)
            assertTrue(marker.rows.all { it.length == 16 })

            val usedKeys = marker.rows
                .flatMap { row -> row.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()

            assertTrue(
                "${marker.assetId} contains an unmapped palette key",
                usedKeys.all { it in marker.palette },
            )
        }
    }

    @Test
    fun mapStateOverlayUsesOnlyProjectedCurrentAndReachableFlags() {
        assertSame(
            PixelMapMarkerCatalog.currentMarker,
            PixelMapMarkerCatalog.stateOverlay(current = true, reachable = false),
        )
        assertSame(
            PixelMapMarkerCatalog.currentMarker,
            PixelMapMarkerCatalog.stateOverlay(current = true, reachable = true),
        )
        assertSame(
            PixelMapMarkerCatalog.reachableMarker,
            PixelMapMarkerCatalog.stateOverlay(current = false, reachable = true),
        )
        assertSame(
            PixelMapMarkerCatalog.unavailableMarker,
            PixelMapMarkerCatalog.stateOverlay(current = false, reachable = false),
        )
    }
}
