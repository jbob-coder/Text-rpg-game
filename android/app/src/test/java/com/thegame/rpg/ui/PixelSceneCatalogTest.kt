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
                PixelSceneCatalog.GATE_TWELVE_SCENE_ID,
                PixelSceneCatalog.SERVICE_TUNNEL_SCENE_ID,
                PixelSceneCatalog.EVAC_STAIR_SCENE_ID,
                PixelSceneCatalog.TRACE_CHAMBER_SCENE_ID,
                PixelSceneCatalog.DISTRICT_PLAZA_SCENE_ID,
                PixelSceneCatalog.DISTRICT_ARCHIVE_SCENE_ID,
                PixelSceneCatalog.WORKSHOP_ROW_SCENE_ID,
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
    fun serviceTunnelMasterUsesMutedMunicipalPerspectiveAndRestrainedIndicators() {
        val scene = PixelSceneCatalog.serviceTunnelDefault

        assertEquals(128, scene.width)
        assertEquals(64, scene.height)

        val allPixels = scene.rows.joinToString("")
        assertTrue("Service Tunnel should include structural ribs", allPixels.count { it == 'M' } > 150)
        assertTrue("Service Tunnel should include warm maintenance lighting", allPixels.count { it == 'G' } >= 20)
        assertTrue(
            "Cool indicators must remain restrained instead of becoming a neon environment",
            allPixels.count { it == 'C' } in 1..30,
        )
        assertTrue(
            "Service Tunnel palette must not reuse the bright UI cyan anchor",
            PixelColors.Cyan !in scene.palette.values,
        )

        assertTrue(scene.rows[31].substring(57, 72).any { it == 'B' || it == 'D' || it == 'L' })
        assertTrue(scene.rows[59].substring(15, 113).any { it == 'R' || it == 'L' || it == 'A' })
    }

    @Test
    fun quietStairMasterUsesCenteredDepthWarmUtilityLightAndNoUiCyan() {
        val scene = PixelSceneCatalog.evacStairDefault

        assertEquals(128, scene.width)
        assertEquals(64, scene.height)

        val allPixels = scene.rows.joinToString("")
        assertTrue("Quiet Stair should keep substantial structural mass", allPixels.count { it == 'M' } > 200)
        assertTrue("Quiet Stair should contain warm emergency/utility lighting", allPixels.count { it == 'G' } >= 20)
        assertTrue("Quiet Stair should include highlighted lamp faces", allPixels.count { it == 'H' } >= 20)
        assertTrue(
            "Quiet Stair must not reuse the bright UI cyan anchor",
            PixelColors.Cyan !in scene.palette.values,
        )

        assertTrue(scene.rows[17].substring(57, 71).any { it == 'B' || it == 'M' || it == 'G' })
        assertTrue(scene.rows[57].substring(14, 114).count { it == 'A' || it == 'M' || it == 'L' } > 50)
    }

    @Test
    fun everyCurrentNamedLocationResolvesToItsOwnProductionScene() {
        val expected = mapOf(
            "PLATFORM_NINE" to PixelSceneCatalog.platformNineBlackout,
            "RELAY_WORKBENCH" to PixelSceneCatalog.relayWorkbenchDefault,
            "GATE_TWELVE" to PixelSceneCatalog.gateTwelveSealed,
            "SERVICE_TUNNEL" to PixelSceneCatalog.serviceTunnelDefault,
            "EVAC_STAIR" to PixelSceneCatalog.evacStairDefault,
            "TRACE_CHAMBER" to PixelSceneCatalog.traceChamberIdle,
            "DISTRICT_PLAZA" to PixelSceneCatalog.districtPlazaOpen,
            "DISTRICT_ARCHIVE" to PixelSceneCatalog.districtArchiveDefault,
            "WORKSHOP_ROW" to PixelSceneCatalog.workshopRowDefault,
        )

        expected.forEach { (locationId, scene) ->
            assertSame(scene, PixelSceneCatalog.scene(locationId))
        }
        assertEquals(9, PixelSceneCatalog.productionScenes.size)
        assertNull(PixelSceneCatalog.scene("UNKNOWN_LOCATION"))
    }
}
