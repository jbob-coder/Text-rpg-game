package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertSame
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelTraceFxCatalogTest {
    @Test
    fun traceEchoFramesUseExact64By64TransparentGridAndDefinedPaletteKeys() {
        assertEquals(4, PixelTraceFxCatalog.frames.size)
        assertEquals(4, PixelTraceFxCatalog.frames.map { it.assetId }.toSet().size)

        PixelTraceFxCatalog.frames.forEach { frame ->
            assertTrue(frame.assetId.startsWith(PixelTraceFxCatalog.TRACE_ECHO_AMBIENT_ID))
            assertEquals(64, frame.width)
            assertEquals(64, frame.height)
            assertEquals(64, frame.rows.size)
            assertTrue(frame.rows.all { it.length == 64 })

            val usedKeys = frame.rows
                .flatMap { row -> row.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()

            assertTrue(
                "${frame.assetId} contains an unmapped palette key",
                usedKeys.all { it in frame.palette },
            )
        }
    }

    @Test
    fun ambientTraceFxMapsOnlyToPlayerFacingTraceScenes() {
        listOf(
            "OPENING_END",
            "POWER_GATE_TWELVE_SIGNAL",
            "POWER_FIRST_LIVE_USE",
            "POWER_TRACE_STRAIN",
            "POWER_FIRST_PRACTICE",
            "POWER_FIRST_PRACTICE_RESULT",
            "TRACE_DIRECTIONAL_DISCOVERY_RESULT",
        ).forEach { sceneId ->
            assertSame(PixelTraceFxCatalog.frames, PixelTraceFxCatalog.forScene(sceneId))
        }

        assertNull(PixelTraceFxCatalog.forScene("OPENING_DECISION"))
        assertNull(PixelTraceFxCatalog.forScene("TRACE_STABILIZATION_HUB"))
        assertNull(PixelTraceFxCatalog.forScene("TRACE_DIRECTIONAL_SESSION_END"))
        assertNull(PixelTraceFxCatalog.forScene(null))
        assertNull(PixelTraceFxCatalog.forScene("UNKNOWN_SCENE"))
    }

    @Test
    fun signalPulseFramesUseSixExact64By64FramesAndOnlyMapToLiveUse() {
        assertEquals(6, PixelTraceFxCatalog.signalPulseFrames.size)
        assertEquals(
            6,
            PixelTraceFxCatalog.signalPulseFrames.map { it.assetId }.toSet().size,
        )

        PixelTraceFxCatalog.signalPulseFrames.forEach { frame ->
            assertTrue(frame.assetId.startsWith(PixelTraceFxCatalog.SIGNAL_PULSE_ID))
            assertEquals(64, frame.width)
            assertEquals(64, frame.height)
            assertEquals(64, frame.rows.size)
            assertTrue(frame.rows.all { it.length == 64 })

            val usedKeys = frame.rows
                .flatMap { row -> row.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()

            assertTrue(
                "${frame.assetId} contains an unmapped palette key",
                usedKeys.all { it in frame.palette },
            )
        }

        assertSame(
            PixelTraceFxCatalog.signalPulseFrames,
            PixelTraceFxCatalog.signalPulseForScene("POWER_FIRST_LIVE_USE"),
        )
        assertNull(PixelTraceFxCatalog.signalPulseForScene("POWER_TRACE_STRAIN"))
        assertNull(PixelTraceFxCatalog.signalPulseForScene("POWER_GATE_TWELVE_SIGNAL"))
        assertNull(PixelTraceFxCatalog.signalPulseForScene(null))
    }

    @Test
    fun directionalTraceFramesUseSixExact64By64FramesAndOnlyMapToFirstUse() {
        assertEquals(6, PixelTraceFxCatalog.directionalTraceFrames.size)
        assertEquals(
            6,
            PixelTraceFxCatalog.directionalTraceFrames.map { it.assetId }.toSet().size,
        )

        PixelTraceFxCatalog.directionalTraceFrames.forEach { frame ->
            assertTrue(frame.assetId.startsWith(PixelTraceFxCatalog.DIRECTIONAL_TRACE_ID))
            assertEquals(64, frame.width)
            assertEquals(64, frame.height)
            assertEquals(64, frame.rows.size)
            assertTrue(frame.rows.all { it.length == 64 })

            val usedKeys = frame.rows
                .flatMap { row -> row.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()

            assertTrue(
                "${frame.assetId} contains an unmapped palette key",
                usedKeys.all { it in frame.palette },
            )
        }

        assertSame(
            PixelTraceFxCatalog.directionalTraceFrames,
            PixelTraceFxCatalog.directionalTraceForScene("TRACE_DIRECTIONAL_DISCOVERY_RESULT"),
        )
        assertNull(PixelTraceFxCatalog.directionalTraceForScene("TRACE_DIRECTIONAL_AFTERSHOCK"))
        assertNull(PixelTraceFxCatalog.directionalTraceForScene("TRACE_DIRECTIONAL_SESSION_END"))
        assertNull(PixelTraceFxCatalog.directionalTraceForScene(null))
    }
}
