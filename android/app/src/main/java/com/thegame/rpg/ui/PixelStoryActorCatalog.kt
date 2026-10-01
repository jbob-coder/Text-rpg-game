package com.thegame.rpg.ui

import androidx.compose.ui.graphics.Color

data class PixelStoryActorPlacement(
    val sprite: PixelSprite,
    val x: Int,
    val y: Int,
)

/**
 * Scene-scale story actors for already player-facing narrative scenes.
 *
 * These sprites are presentation only. Selection is driven exclusively by projected location
 * and scene IDs; the catalog never reads raw flags, quest internals, or hidden NPC state.
 */
object PixelStoryActorCatalog {
    const val TAMSIN_SCENE_ACTOR_ID = "NPC_TAMSIN_SCENE_ACTOR"
    const val WOUNDED_COURIER_SCENE_ACTOR_ID = "SUPPORT_COURIER_01_SCENE_ACTOR"

    private fun pixels(width: Int, height: Int): MutableList<CharArray> =
        MutableList(height) { CharArray(width) { PixelSprite.TRANSPARENT_PIXEL } }

    private fun rect(
        p: MutableList<CharArray>,
        x: Int,
        y: Int,
        width: Int,
        height: Int,
        key: Char,
    ) {
        for (yy in y until y + height) for (xx in x until x + width) {
            if (yy in p.indices && xx in p[yy].indices) p[yy][xx] = key
        }
    }

    val tamsin: PixelSprite = run {
        val width = 20
        val height = 32
        val p = pixels(width, height)

        // Source-backed palette anchors from the authored Tamsin blueprint:
        // charcoal municipal utility jacket, pale work shirt, dark trousers,
        // medium warm-brown skin, near-black hair, restrained workwear accents.
        val palette = mapOf(
            'O' to Color(0xFF111719),
            'H' to Color(0xFF1E2326),
            'h' to Color(0xFF343B3E),
            'S' to Color(0xFFA8735A),
            's' to Color(0xFF8B5F4B),
            'J' to Color(0xFF30343B),
            'j' to Color(0xFF24282D),
            'P' to Color(0xFFC9C7BE),
            'T' to Color(0xFF24272C),
            'B' to Color(0xFF756047),
            'b' to Color(0xFF4F4032),
            'M' to Color(0xFF8B8D87),
        )

        // Hair: compact crop with heavier left fringe.
        rect(p, 6, 1, 8, 2, 'H')
        rect(p, 4, 3, 11, 2, 'H')
        rect(p, 3, 5, 7, 3, 'H')
        rect(p, 10, 5, 5, 2, 'h')
        rect(p, 3, 7, 4, 2, 'H')

        // Face / ears.
        rect(p, 5, 6, 10, 6, 'S')
        rect(p, 4, 8, 1, 2, 's')
        rect(p, 15, 8, 1, 2, 's')
        rect(p, 7, 8, 2, 1, 'O')
        rect(p, 12, 8, 2, 1, 'O')
        rect(p, 9, 11, 3, 1, 's')
        // Eyebrow notch marker on right side at this scale.
        rect(p, 12, 7, 1, 1, 'S')

        // Neck + pale shirt wedge.
        rect(p, 8, 12, 4, 2, 's')
        rect(p, 8, 14, 4, 3, 'P')

        // High-collar charcoal utility jacket.
        rect(p, 5, 14, 3, 3, 'J')
        rect(p, 12, 14, 3, 3, 'J')
        rect(p, 4, 16, 12, 9, 'J')
        rect(p, 5, 17, 10, 2, 'j')
        rect(p, 9, 16, 2, 8, 'P')
        rect(p, 4, 20, 3, 5, 'j')
        rect(p, 13, 20, 3, 5, 'j')

        // Long forearms; right sleeve rolls higher.
        rect(p, 2, 17, 2, 9, 'J')
        rect(p, 16, 17, 2, 6, 'J')
        rect(p, 2, 25, 2, 3, 'S')
        rect(p, 16, 23, 2, 5, 'S')

        // Badge on left chest.
        rect(p, 5, 18, 2, 1, 'M')

        // Narrow diagonal satchel strap and compact hip satchel.
        for (i in 0..7) {
            val x = 13 - i / 2
            val y = 15 + i
            rect(p, x, y, 1, 1, 'B')
        }
        rect(p, 5, 22, 4, 4, 'b')
        rect(p, 6, 22, 3, 1, 'B')

        // Practical dark trousers and boots.
        rect(p, 6, 25, 3, 5, 'T')
        rect(p, 11, 25, 3, 5, 'T')
        rect(p, 5, 30, 4, 2, 'O')
        rect(p, 11, 30, 4, 2, 'O')

        PixelSprite(
            assetId = TAMSIN_SCENE_ACTOR_ID,
            width = width,
            height = height,
            palette = palette,
            rows = p.map { it.concatToString() },
        )
    }

    val woundedCourier: PixelSprite = run {
        val width = 28
        val height = 14
        val p = pixels(width, height)
        val palette = mapOf(
            'O' to Color(0xFF111719),
            'S' to Color(0xFFAD7D62),
            's' to Color(0xFF8B5F4B),
            'U' to Color(0xFF4B5756),
            'u' to Color(0xFF313B3B),
            'T' to Color(0xFF292F30),
            'R' to Color(0xFF9B5D57),
            'M' to Color(0xFF6B726D),
        )

        // Conscious injured maintenance courier, side-lying/kneeling rather than gore.
        rect(p, 2, 4, 6, 5, 'S')
        rect(p, 1, 3, 6, 2, 'O')
        rect(p, 7, 5, 10, 5, 'U')
        rect(p, 10, 7, 8, 3, 'u')
        rect(p, 17, 8, 6, 3, 'T')
        rect(p, 21, 10, 5, 2, 'T')
        rect(p, 6, 9, 6, 2, 'S')
        rect(p, 14, 5, 2, 2, 'R')
        rect(p, 3, 9, 3, 2, 'M')
        rect(p, 24, 9, 3, 3, 'O')

        PixelSprite(
            assetId = WOUNDED_COURIER_SCENE_ACTOR_ID,
            width = width,
            height = height,
            palette = palette,
            rows = p.map { it.concatToString() },
        )
    }

    val productionActors: List<PixelSprite> = listOf(tamsin, woundedCourier)

    fun placements(locationId: String, sceneId: String?): List<PixelStoryActorPlacement> =
        when (sceneId) {
            "OPENING_DEPOT_BLACKOUT" ->
                if (locationId == "PLATFORM_NINE") {
                    listOf(
                        PixelStoryActorPlacement(woundedCourier, x = 34, y = 45),
                        PixelStoryActorPlacement(tamsin, x = 66, y = 24),
                    )
                } else emptyList()

            "OPENING_DECISION" ->
                if (locationId == "PLATFORM_NINE") {
                    listOf(PixelStoryActorPlacement(tamsin, x = 63, y = 24))
                } else emptyList()

            "OPENING_RECOVERY" ->
                if (locationId == "RELAY_WORKBENCH") {
                    listOf(PixelStoryActorPlacement(tamsin, x = 88, y = 24))
                } else emptyList()

            "OPENING_TUNNEL" ->
                if (locationId == "SERVICE_TUNNEL") {
                    listOf(PixelStoryActorPlacement(tamsin, x = 76, y = 24))
                } else emptyList()

            else -> emptyList()
        }
}
