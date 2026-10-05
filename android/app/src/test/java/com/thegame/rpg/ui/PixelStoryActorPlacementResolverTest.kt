package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Test

class PixelStoryActorPlacementResolverTest {
    @Test
    fun `semantic placement keys preserve established opening coordinates`() {
        assertEquals(
            PixelStoryActorStagePoint(34, 13),
            PixelStoryActorPlacementResolver.resolve("PLATFORM_NINE_COURIER_LEFT"),
        )
        assertEquals(
            PixelStoryActorStagePoint(62, 14),
            PixelStoryActorPlacementResolver.resolve("PLATFORM_NINE_TAMSIN_RIGHT"),
        )
        assertEquals(
            PixelStoryActorStagePoint(90, 14),
            PixelStoryActorPlacementResolver.resolve("RELAY_WORKBENCH_TAMSIN_RIGHT"),
        )
        assertEquals(
            PixelStoryActorStagePoint(76, 14),
            PixelStoryActorPlacementResolver.resolve("SERVICE_TUNNEL_TAMSIN_RIGHT"),
        )
    }

    @Test
    fun `unknown placement key cannot invent presentation coordinates`() {
        assertNull(PixelStoryActorPlacementResolver.resolve("UNKNOWN_STAGE_POINT"))
    }
}
