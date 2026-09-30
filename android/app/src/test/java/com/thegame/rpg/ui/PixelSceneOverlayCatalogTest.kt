package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertSame
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelSceneOverlayCatalogTest {
    @Test
    fun productionOverlaysUseExact128By64TransparentGridAndDefinedPaletteKeys() {
        assertEquals(
            setOf(
                PixelSceneOverlayCatalog.GATE_TWELVE_ECHO_ACTIVE_ID,
                PixelSceneOverlayCatalog.SERVICE_TUNNEL_AFTERSHOCK_ID,
                PixelSceneOverlayCatalog.TRACE_CHAMBER_TRAINING_ID,
                PixelSceneOverlayCatalog.DISTRICT_PLAZA_BLACKOUT_ID,
                PixelSceneOverlayCatalog.RELAY_WORKBENCH_RELAY_OPEN_ID,
            ),
            PixelSceneOverlayCatalog.productionOverlays.map { it.assetId }.toSet(),
        )

        PixelSceneOverlayCatalog.productionOverlays.forEach { overlay ->
            assertEquals(128, overlay.width)
            assertEquals(64, overlay.height)
            assertEquals(64, overlay.rows.size)
            assertTrue(overlay.rows.all { it.length == 128 })

            val usedKeys = overlay.rows
                .flatMap { row -> row.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()

            assertTrue(
                "${overlay.assetId} contains an unmapped palette key",
                usedKeys.all { it in overlay.palette },
            )
        }
    }

    @Test
    fun gateTwelveOverlayMapsOnlyToPlayerFacingGateScenes() {
        listOf(
            "OPENING_END",
            "POWER_GATE_TWELVE_SIGNAL",
            "POWER_FIRST_LIVE_USE",
            "POWER_TRACE_STRAIN",
        ).forEach { sceneId ->
            assertSame(
                PixelSceneOverlayCatalog.gateTwelveEchoActive,
                PixelSceneOverlayCatalog.forScene(sceneId),
            )
        }

        assertNull(PixelSceneOverlayCatalog.forScene("OPENING_DECISION"))
    }

    @Test
    fun tunnelAftershockAndTraceTrainingHaveExactSceneMappings() {
        assertSame(
            PixelSceneOverlayCatalog.serviceTunnelAftershock,
            PixelSceneOverlayCatalog.forScene("TRACE_DIRECTIONAL_AFTERSHOCK"),
        )

        listOf(
            "POWER_FIRST_PRACTICE",
            "POWER_FIRST_PRACTICE_RESULT",
            "TRACE_DIRECTIONAL_DISCOVERY_RESULT",
        ).forEach { sceneId ->
            assertSame(
                PixelSceneOverlayCatalog.traceChamberTraining,
                PixelSceneOverlayCatalog.forScene(sceneId),
            )
        }

        assertNull(PixelSceneOverlayCatalog.forScene("TRACE_STABILIZATION_HUB"))
        assertNull(PixelSceneOverlayCatalog.forScene("TRACE_DIRECTIONAL_SESSION_END"))
        assertNull(PixelSceneOverlayCatalog.forScene(null))
        assertNull(PixelSceneOverlayCatalog.forScene("UNKNOWN_SCENE"))
    }

    @Test
    fun districtHubMapsOnlyToDepotPlazaBlackoutState() {
        assertSame(
            PixelSceneOverlayCatalog.districtPlazaBlackout,
            PixelSceneOverlayCatalog.forScene("DISTRICT_HUB"),
        )
        assertNull(PixelSceneOverlayCatalog.forScene("DISTRICT_ARCHIVE"))
        assertNull(PixelSceneOverlayCatalog.forScene("DISTRICT_WORKSHOP"))
    }


    @Test
    fun relayWorkbenchStateOverlayUsesOnlyProjectedRelayVisualState() {
        listOf("opened", "damaged", "signal_lost").forEach { relayState ->
            assertSame(
                PixelSceneOverlayCatalog.relayWorkbenchRelayOpen,
                PixelSceneOverlayCatalog.forVisualState(
                    locationId = "RELAY_WORKBENCH",
                    relayState = relayState,
                ),
            )
        }

        assertNull(
            PixelSceneOverlayCatalog.forVisualState(
                locationId = "RELAY_WORKBENCH",
                relayState = "intact",
            )
        )
        assertNull(
            PixelSceneOverlayCatalog.forVisualState(
                locationId = "RELAY_WORKBENCH",
                relayState = null,
            )
        )
        assertNull(
            PixelSceneOverlayCatalog.forVisualState(
                locationId = "GATE_TWELVE",
                relayState = "opened",
            )
        )
    }

}
