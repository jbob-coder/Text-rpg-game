package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelEnvironmentOverlayCatalogTest {
    @Test
    fun reusableEnvironmentOverlaysUseExact128By64TransparentMasters() {
        assertEquals(2, PixelEnvironmentOverlayCatalog.productionOverlays.size)
        assertEquals(
            setOf(
                PixelEnvironmentOverlayCatalog.EMERGENCY_LIGHT_OVERLAY_ID,
                PixelEnvironmentOverlayCatalog.BLACKOUT_SHADOW_OVERLAY_ID,
            ),
            PixelEnvironmentOverlayCatalog.productionOverlays.map { it.assetId }.toSet(),
        )

        PixelEnvironmentOverlayCatalog.productionOverlays.forEach { overlay ->
            assertEquals(128, overlay.width)
            assertEquals(64, overlay.height)
            assertEquals(64, overlay.rows.size)
            assertTrue(overlay.rows.all { it.length == 128 })

            val used = overlay.rows
                .flatMap { it.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()
            assertTrue(used.all { it in overlay.palette })
        }
    }

    @Test
    fun plazaBlackoutCompositeContainsBothReusableLayerFamilies() {
        val composite = PixelEnvironmentOverlayCatalog.compose(
            assetId = "TEST_COMPOSITE",
            PixelEnvironmentOverlayCatalog.blackoutShadows,
            PixelEnvironmentOverlayCatalog.emergencyLights,
        )

        assertEquals(128, composite.width)
        assertEquals(64, composite.height)
        assertTrue('D' in composite.palette)
        assertTrue('d' in composite.palette)
        assertTrue('R' in composite.palette)
        assertTrue('G' in composite.palette)

        val used = composite.rows
            .flatMap { it.toList() }
            .filter { it != PixelSprite.TRANSPARENT_PIXEL }
            .toSet()
        assertTrue('D' in used || 'd' in used)
        assertTrue('R' in used)
        assertTrue('G' in used)
    }
}
