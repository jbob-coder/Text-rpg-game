package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelUiUtilityCatalogTest {
    @Test
    fun scrollMarkerUsesExact16By16Master() {
        val sprite = PixelUiUtilityCatalog.scrollMarker

        assertEquals(PixelUiUtilityCatalog.SCROLL_MARKER_ID, sprite.assetId)
        assertEquals(16, sprite.width)
        assertEquals(16, sprite.height)
        assertTrue(sprite.rows.all { it.length == 16 })
    }

    @Test
    fun narrationIconUsesExact24By24MasterAndShapePixels() {
        val sprite = PixelUiUtilityCatalog.narrationIcon

        assertEquals(PixelUiUtilityCatalog.AUDIO_NARRATION_ICON_ID, sprite.assetId)
        assertEquals(24, sprite.width)
        assertEquals(24, sprite.height)
        assertTrue(sprite.rows.all { it.length == 24 })

        val used = sprite.rows
            .flatMap { it.toList() }
            .filter { it != PixelSprite.TRANSPARENT_PIXEL }
            .toSet()
        assertTrue(used.containsAll(setOf('C', 'P', 'G')))
        assertTrue(used.all { it in sprite.palette })
    }
}
