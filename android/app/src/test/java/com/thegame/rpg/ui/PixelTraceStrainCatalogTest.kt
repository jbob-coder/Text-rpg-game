package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertSame
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelTraceStrainCatalogTest {
    @Test
    fun avatarAndPortraitMastersUseExactCanvasAndMappedPaletteKeys() {
        assertEquals(4, PixelTraceStrainCatalog.avatarFrames.size)
        assertEquals(4, PixelTraceStrainCatalog.portraitFrames.size)

        PixelTraceStrainCatalog.avatarFrames.forEach { frame ->
            assertTrue(frame.assetId.startsWith(PixelTraceStrainCatalog.TRACE_STRAIN_ID))
            assertEquals(32, frame.width)
            assertEquals(48, frame.height)
            assertEquals(48, frame.rows.size)
            assertTrue(frame.rows.all { it.length == 32 })
            val used = frame.rows
                .flatMap { it.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()
            assertTrue(used.all { it in frame.palette })
        }

        PixelTraceStrainCatalog.portraitFrames.forEach { frame ->
            assertTrue(frame.assetId.startsWith(PixelTraceStrainCatalog.TRACE_STRAIN_ID))
            assertEquals(64, frame.width)
            assertEquals(64, frame.height)
            assertEquals(64, frame.rows.size)
            assertTrue(frame.rows.all { it.length == 64 })
            val used = frame.rows
                .flatMap { it.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()
            assertTrue(used.all { it in frame.palette })
        }
    }

    @Test
    fun strainFxMapsOnlyFromProjectedEchoStrainConditionId() {
        val visible = setOf(PixelTraceStrainCatalog.ECHO_STRAIN_CONDITION_ID)
        assertSame(
            PixelTraceStrainCatalog.avatarFrames,
            PixelTraceStrainCatalog.avatarForConditions(visible),
        )
        assertSame(
            PixelTraceStrainCatalog.portraitFrames,
            PixelTraceStrainCatalog.portraitForConditions(visible),
        )

        assertNull(PixelTraceStrainCatalog.avatarForConditions(emptySet()))
        assertNull(PixelTraceStrainCatalog.avatarForConditions(setOf("COND_MINOR_INJURY")))
        assertNull(PixelTraceStrainCatalog.portraitForConditions(setOf("UNKNOWN_CONDITION")))
    }
}
