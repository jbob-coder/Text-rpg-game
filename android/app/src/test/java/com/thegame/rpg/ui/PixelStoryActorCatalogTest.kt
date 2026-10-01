package com.thegame.rpg.ui

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

        // Heavy left fringe.
        assertTrue((9..16).any { x -> sprite.rows[7][x] != PixelSprite.TRANSPARENT_PIXEL })
        // High collar / pale shirt wedge.
        assertTrue((14..19).any { x -> sprite.rows[17][x] == 'P' })
        // Cross-body satchel path and hip mass.
        assertTrue(sprite.rows.any { row -> 'B' in row || 'b' in row })
        // Rolled right sleeve leaves visible skin higher than the left hand.
        assertTrue((25..27).any { x -> sprite.rows[29][x] == 'S' })
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
