package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertSame
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelSceneCatalogTest {
    @Test
    fun productionScenesHaveExact128By64NativeGridAndDefinedPaletteKeys() {
        assertEquals(
            setOf(
                PixelSceneCatalog.PLATFORM_NINE_SCENE_ID,
                PixelSceneCatalog.RELAY_WORKBENCH_SCENE_ID,
            ),
            PixelSceneCatalog.productionScenes.map { it.assetId }.toSet(),
        )

        PixelSceneCatalog.productionScenes.forEach { scene ->
            assertEquals(128, scene.width)
            assertEquals(64, scene.height)
            assertEquals(64, scene.rows.size)
            assertTrue(scene.rows.all { it.length == 128 })

            val usedKeys = scene.rows
                .flatMap { row -> row.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()

            assertTrue(
                "${scene.assetId} contains an unmapped palette key",
                usedKeys.all { it in scene.palette },
            )
        }
    }

    @Test
    fun namedLocationsResolveOnlyToTheirOwnProductionScene() {
        assertSame(
            PixelSceneCatalog.platformNineBlackout,
            PixelSceneCatalog.scene("PLATFORM_NINE"),
        )
        assertSame(
            PixelSceneCatalog.relayWorkbenchDefault,
            PixelSceneCatalog.scene("RELAY_WORKBENCH"),
        )
        assertNull(PixelSceneCatalog.scene("GATE_TWELVE"))
        assertNull(PixelSceneCatalog.scene("UNKNOWN_LOCATION"))
    }
}
