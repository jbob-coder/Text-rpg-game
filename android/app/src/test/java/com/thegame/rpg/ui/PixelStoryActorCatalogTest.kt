package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelStoryActorCatalogTest {
    @Test
    fun productionActorsUseDefinedPalettesAndSceneScaleBounds() {
        assertEquals(
            setOf(
                PixelStoryActorCatalog.TAMSIN_SCENE_ACTOR_ID,
                PixelStoryActorCatalog.WOUNDED_COURIER_SCENE_ACTOR_ID,
            ),
            PixelStoryActorCatalog.productionActors.map { it.assetId }.toSet(),
        )

        PixelStoryActorCatalog.productionActors.forEach { sprite ->
            assertTrue(sprite.width in 1..32)
            assertTrue(sprite.height in 1..32)
            val usedKeys = sprite.rows
                .flatMap { it.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()
            assertTrue(usedKeys.all { it in sprite.palette })
        }
    }

    @Test
    fun tamsinKeepsSourceBackedSilhouetteAnchorsAtSceneScale() {
        val sprite = PixelStoryActorCatalog.tamsin

        // Heavy left fringe.
        assertTrue((3..9).any { x -> sprite.rows[6][x] != PixelSprite.TRANSPARENT_PIXEL })
        // High collar / pale shirt wedge.
        assertTrue((8..11).any { x -> sprite.rows[15][x] == 'P' })
        // Cross-body satchel path and hip mass.
        assertTrue(sprite.rows.any { row -> 'B' in row || 'b' in row })
        // Rolled right sleeve leaves visible skin higher than the left hand.
        assertTrue((16..17).any { x -> sprite.rows[23][x] == 'S' })
    }

    @Test
    fun storyActorPlacementUsesOnlyProjectedSceneAndLocationIds() {
        val opening = PixelStoryActorCatalog.placements(
            locationId = "PLATFORM_NINE",
            sceneId = "OPENING_DEPOT_BLACKOUT",
        )
        assertEquals(
            listOf(
                PixelStoryActorCatalog.WOUNDED_COURIER_SCENE_ACTOR_ID,
                PixelStoryActorCatalog.TAMSIN_SCENE_ACTOR_ID,
            ),
            opening.map { it.sprite.assetId },
        )

        assertEquals(
            listOf(PixelStoryActorCatalog.TAMSIN_SCENE_ACTOR_ID),
            PixelStoryActorCatalog.placements("PLATFORM_NINE", "OPENING_DECISION")
                .map { it.sprite.assetId },
        )
        assertEquals(
            listOf(PixelStoryActorCatalog.TAMSIN_SCENE_ACTOR_ID),
            PixelStoryActorCatalog.placements("RELAY_WORKBENCH", "OPENING_RECOVERY")
                .map { it.sprite.assetId },
        )
        assertEquals(
            listOf(PixelStoryActorCatalog.TAMSIN_SCENE_ACTOR_ID),
            PixelStoryActorCatalog.placements("SERVICE_TUNNEL", "OPENING_TUNNEL")
                .map { it.sprite.assetId },
        )

        assertTrue(
            PixelStoryActorCatalog.placements("PLATFORM_NINE", "UNRELATED_SCENE").isEmpty()
        )
        assertTrue(
            PixelStoryActorCatalog.placements("DISTRICT_ARCHIVE", "OPENING_DEPOT_BLACKOUT")
                .isEmpty()
        )
    }
}
