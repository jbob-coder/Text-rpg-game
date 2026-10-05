package com.thegame.rpg.ui

import com.thegame.rpg.engine.GameRoomActor
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelStoryActorCatalogTest {
    private fun actor(
        presentationId: String,
        visualFamily: String,
        placementKey: String,
    ) = GameRoomActor(
        presentationId = presentationId,
        knownActorId = null,
        displayName = presentationId,
        visualFamily = visualFamily,
        placementKey = placementKey,
        poseKey = null,
        outfitKey = null,
        visibleTags = emptyList(),
        inspectable = false,
        dialogueAvailable = false,
        actions = emptyList(),
    )

    @Test fun rendersProjectedCourierAtPlatformPlacement() {
        val placements = PixelStoryActorCatalog.placements(listOf(actor("COURIER", "SUPPORT_WOUNDED_COURIER", "PLATFORM_NINE_COURIER_LEFT")))
        assertEquals(1, placements.size)
        assertEquals(34, placements.single().x)
        assertEquals(13, placements.single().y)
    }

    @Test fun rendersProjectedTamsinAtPlatformPlacement() {
        val placements = PixelStoryActorCatalog.placements(listOf(actor("TAMSIN", "NPC_TAMSIN", "PLATFORM_NINE_TAMSIN_RIGHT")))
        assertEquals(1, placements.size)
        assertEquals(62, placements.single().x)
        assertEquals(14, placements.single().y)
    }

    @Test fun rendersProjectedTamsinAtRelayPlacement() {
        val placements = PixelStoryActorCatalog.placements(listOf(actor("TAMSIN", "NPC_TAMSIN", "RELAY_WORKBENCH_TAMSIN_RIGHT")))
        assertEquals(1, placements.size)
        assertEquals(90, placements.single().x)
        assertEquals(14, placements.single().y)
    }

    @Test fun rendersProjectedTamsinAtTunnelPlacement() {
        val placements = PixelStoryActorCatalog.placements(listOf(actor("TAMSIN", "NPC_TAMSIN", "SERVICE_TUNNEL_TAMSIN_RIGHT")))
        assertEquals(1, placements.size)
        assertEquals(76, placements.single().x)
        assertEquals(14, placements.single().y)
    }

    @Test fun emptyProjectionRendersNoActors() {
        assertTrue(PixelStoryActorCatalog.placements(emptyList()).isEmpty())
    }

    @Test fun unknownVisualFamilyRendersNothing() {
        assertTrue(PixelStoryActorCatalog.placements(listOf(actor("UNKNOWN", "PRIVATE_UNKNOWN", "PLATFORM_NINE_TAMSIN_RIGHT"))).isEmpty())
    }

    @Test fun unknownPlacementKeyRendersNothing() {
        assertTrue(PixelStoryActorCatalog.placements(listOf(actor("TAMSIN", "NPC_TAMSIN", "PRIVATE_COORDINATE"))).isEmpty())
    }
}
