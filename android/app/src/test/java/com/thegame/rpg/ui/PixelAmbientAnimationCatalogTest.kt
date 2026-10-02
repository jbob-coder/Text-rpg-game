package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelAmbientAnimationCatalogTest {
    @Test
    fun serviceTunnelIsTheOnlyLocationWithAmbientTracksInThisSlice() {
        assertEquals(
            listOf(
                PixelAmbientAnimationCatalog.SERVICE_TUNNEL_FAN_TRACK_ID,
                PixelAmbientAnimationCatalog.SERVICE_TUNNEL_PANEL_TRACK_ID,
                PixelAmbientAnimationCatalog.SERVICE_TUNNEL_DRIP_TRACK_ID,
            ),
            PixelAmbientAnimationCatalog.forLocation("SERVICE_TUNNEL").map { it.trackId },
        )

        listOf(
            "PLATFORM_NINE",
            "RELAY_WORKBENCH",
            "GATE_TWELVE",
            "EVAC_STAIR",
            "TRACE_CHAMBER",
            "DISTRICT_PLAZA",
            "DISTRICT_ARCHIVE",
            "WORKSHOP_ROW",
            "UNKNOWN",
        ).forEach { locationId ->
            assertTrue(PixelAmbientAnimationCatalog.forLocation(locationId).isEmpty())
        }
    }

    @Test
    fun serviceTunnelTracksMatchTheBoundedAnimationBrief() {
        assertEquals(4, PixelAmbientAnimationCatalog.serviceTunnelFan.frames.size)
        assertEquals(220L, PixelAmbientAnimationCatalog.serviceTunnelFan.frameDurationMs)

        assertEquals(3, PixelAmbientAnimationCatalog.serviceTunnelPanel.frames.size)
        assertEquals(450L, PixelAmbientAnimationCatalog.serviceTunnelPanel.frameDurationMs)

        assertEquals(5, PixelAmbientAnimationCatalog.serviceTunnelDrip.frames.size)
        assertEquals(260L, PixelAmbientAnimationCatalog.serviceTunnelDrip.frameDurationMs)
    }

    @Test
    fun ambientFramesStayOnTheSceneGridAndInsideTheirDeclaredMovingBounds() {
        PixelAmbientAnimationCatalog.forLocation("SERVICE_TUNNEL").forEach { track ->
            assertEquals(track.frames.size, track.frames.map { it.rows }.distinct().size)

            track.frames.forEach { frame ->
                assertEquals(128, frame.width)
                assertEquals(64, frame.height)
                assertEquals(64, frame.rows.size)
                assertTrue(frame.rows.all { it.length == 128 })

                var visiblePixels = 0
                frame.rows.forEachIndexed { y, row ->
                    row.forEachIndexed { x, pixel ->
                        if (pixel != PixelSprite.TRANSPARENT_PIXEL) {
                            visiblePixels += 1
                            assertTrue(
                                "${track.trackId} drew ($x,$y) outside ${track.bounds}",
                                track.bounds.contains(x, y),
                            )
                        }
                    }
                }
                assertTrue("${track.trackId} contains an empty frame", visiblePixels > 0)
            }
        }
    }
}
