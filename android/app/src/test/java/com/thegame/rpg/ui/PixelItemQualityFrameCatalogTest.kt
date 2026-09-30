package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertSame
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelItemQualityFrameCatalogTest {
    @Test
    fun standardAndUncommonFramesUseExact32By32TransparentMasters() {
        val frames = listOf(
            PixelItemQualityFrameCatalog.standardFrame,
            PixelItemQualityFrameCatalog.uncommonFrame,
        )

        assertEquals(2, frames.map { it.assetId }.toSet().size)
        frames.forEach { frame ->
            assertEquals(32, frame.width)
            assertEquals(32, frame.height)
            assertEquals(32, frame.rows.size)
            assertTrue(frame.rows.all { it.length == 32 })

            val used = frame.rows
                .flatMap { it.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()
            assertTrue(used.all { it in frame.palette })
        }
    }

    @Test
    fun qualityMappingRequiresExplicitSupportedValue() {
        assertSame(
            PixelItemQualityFrameCatalog.standardFrame,
            PixelItemQualityFrameCatalog.forQuality("standard"),
        )
        assertSame(
            PixelItemQualityFrameCatalog.uncommonFrame,
            PixelItemQualityFrameCatalog.forQuality("UNCOMMON"),
        )
        assertNull(PixelItemQualityFrameCatalog.forQuality(null))
        assertNull(PixelItemQualityFrameCatalog.forQuality("legendary"))
        assertNull(PixelItemQualityFrameCatalog.forQuality(""))
    }
}
