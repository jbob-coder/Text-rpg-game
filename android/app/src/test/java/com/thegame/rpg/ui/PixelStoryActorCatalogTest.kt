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
            val usedKeys = sprite.rows
                .flatMap { it.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()
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

    @Test
    fun projectedActorsAloneDeterminePresenceAndPlacement() {
        val actors = listOf(
            actor("courier", "SUPPORT_WOUNDED_COURIER", "PLATFORM_NINE_COURIER_LEFT"),
            actor("tamsin", "NPC_TAMSIN", "PLATFORM_NINE_TAMSIN_RIGHT"),
        )

        val placements = PixelStoryActorCatalog.placements(actors)

        assertEquals(
            listOf(
                PixelStoryActorCatalog.SUPPORT_COURIER_ID,
                PixelStoryActorCatalog.TAMSIN_TURNAROUND_ID,
            ),
            placements.map { it.sprite.assetId },
        )
        assertEquals(listOf(34, 62), placements.map { it.x })
        assertEquals(listOf(13, 14), placements.map { it.y })
        assertTrue(PixelStoryActorCatalog.placements(emptyList()).isEmpty())
    }

    @Test
    fun projectedTamsinKeepsOpeningScenePlacementEquivalence() {
        val relay = PixelStoryActorCatalog.placements(
            listOf(actor("tamsin-relay", "NPC_TAMSIN", "RELAY_WORKBENCH_TAMSIN_RIGHT")),
        )
        val tunnel = PixelStoryActorCatalog.placements(
            listOf(actor("tamsin-tunnel", "NPC_TAMSIN", "SERVICE_TUNNEL_TAMSIN_RIGHT")),
        )

        assertEquals(listOf(PixelStoryActorCatalog.TAMSIN_TURNAROUND_ID), relay.map { it.sprite.assetId })
        assertEquals(listOf(90), relay.map { it.x })
        assertEquals(listOf(14), relay.map { it.y })
        assertEquals(listOf(PixelStoryActorCatalog.TAMSIN_TURNAROUND_ID), tunnel.map { it.sprite.assetId })
        assertEquals(listOf(76), tunnel.map { it.x })
        assertEquals(listOf(14), tunnel.map { it.y })
    }

    @Test
    fun unknownProjectedPresentationCannotInventVisualOrCoordinates() {
        assertTrue(
            PixelStoryActorCatalog.placements(
                listOf(actor("unknown", "UNKNOWN_FAMILY", "PLATFORM_NINE_TAMSIN_RIGHT")),
            ).isEmpty(),
        )
        assertTrue(
            PixelStoryActorCatalog.placements(
                listOf(actor("tamsin", "NPC_TAMSIN", "UNKNOWN_PLACEMENT")),
            ).isEmpty(),
        )
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
}