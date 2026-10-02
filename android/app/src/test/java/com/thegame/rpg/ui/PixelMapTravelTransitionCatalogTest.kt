package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelMapTravelTransitionCatalogTest {
    @Test
    fun transitionUsesEightExact128By64FramesWithMappedPaletteKeys() {
        val frames = PixelMapTravelTransitionCatalog.frames
        assertEquals(8, frames.size)
        assertEquals(8, frames.map { it.assetId }.toSet().size)

        frames.forEach { frame ->
            assertTrue(frame.assetId.startsWith(PixelMapTravelTransitionCatalog.ASSET_ID))
            assertEquals(128, frame.width)
            assertEquals(64, frame.height)
            assertEquals(64, frame.rows.size)
            assertTrue(frame.rows.all { it.length == 128 })

            val usedKeys = frame.rows
                .flatMap { it.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()
            assertTrue(usedKeys.all { it in frame.palette })
        }
    }
}
