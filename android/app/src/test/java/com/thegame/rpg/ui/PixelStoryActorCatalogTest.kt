package com.thegame.rpg.ui

import com.thegame.rpg.engine.GameRoomActor
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelStoryActorCatalogTest {
    @Test
    fun productionActorsUseDefinedPalettesAndSceneScaleBounds() {
        assertEquals(
            setOf(
                PixelStoryActorCatalog.TAMSIN_TURNAROUND_ID,
                PixelStoryActorCatalog.SUPPORT_COURIER_ID,
            ),
            PixelStoryActorCatalog.productionActors.map { it.assetId }.toSet(),
        )
        PixelStoryActorCatalog.productionActors.forEach { sprite ->
            assertEquals(32, sprite.width)
            assertEquals(48, sprite.height)
            val usedKeys = sprite.rows.flatMap { it.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }.toSet()
            assertTrue(usedKeys.all { it in sprite.palette })
        }
    }

    @Test
    fun tamsinKeepsSourceBackedSilhouetteAnchorsAtSceneScale() {
        val sprite = PixelStoryActorCatalog.tamsinFront
        assertTrue((9..16).any { x -> sprite.rows[7][x] != PixelSprite.TRANSPARENT_PIXEL })
        assertTrue((14..19).any { x -> sprite.rows[17][x] == 'P' })
        assertTrue(sprite.rows.any { row -> 'B' in row || 'b' in row })
        assertTrue((25..27).any { x -> sprite.rows[29][x] == 'S' })
    }

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

    @Test
    fun projectedActorsAloneDeterminePresenceAndPlacement() {
        val actors = listOf(
            actor("SUPPORT_WOUNDED_COURIER", "SUPPORT_WOUNDED_COURIER", "PLATFORM_NINE_COURIER_LEFT"),
            actor("NPC_TAMSIN", "NPC_TAMSIN", "PLATFORM_NINE_TAMSIN_RIGHT"),
        )

        val placements = PixelStoryActorCatalog.placements(actors)

        assertEquals(
            listOf(PixelStoryActorCatalog.SUPPORT_COURIER_ID, PixelStoryActorCatalog.TAMSIN_TURNAROUND_ID),
            placements.map { it.sprite.assetId },
        )
        assertEquals(listOf(34 to 13, 62 to 14), placements.map { it.x to it.y })
        assertTrue(PixelStoryActorCatalog.placements(emptyList()).isEmpty())
    }

    @Test
    fun unknownProjectedPresentationCannotInventVisualOrCoordinates() {
        val unknownVisual = actor("UNKNOWN", "UNKNOWN_FAMILY", "PLATFORM_NINE_TAMSIN_RIGHT")
        val unknownPlacement = actor("NPC_TAMSIN", "NPC_TAMSIN", "UNKNOWN_STAGE_POINT")

        assertTrue(PixelStoryActorCatalog.placements(listOf(unknownVisual)).isEmpty())
        assertTrue(PixelStoryActorCatalog.placements(listOf(unknownPlacement)).isEmpty())
    }
}
