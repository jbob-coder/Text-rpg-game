package com.thegame.rpg.ui

import androidx.compose.ui.graphics.Color
import com.thegame.rpg.engine.GameRoomActor

data class PixelStoryActorPlacement(
    val sprite: PixelSprite,
    val x: Int,
    val y: Int,
)

/**
 * Story-actor presentation assets on the shared 32x48 character grid.
 *
 * Actor presence comes only from the authoritative player-safe room projection. This catalog
 * maps projected visual families to sprites and semantic placement keys to presentation
 * coordinates; it never reads raw flags, quest internals, hidden NPC state, scene IDs or
 * location IDs to invent presence.
 */
object PixelStoryActorCatalog {
    const val TAMSIN_TURNAROUND_ID = "NPC_TAMSIN_TURNAROUND"
    const val SUPPORT_COURIER_ID = "SUPPORT_COURIER_01"

    private const val WIDTH = 32
    private const val HEIGHT = 48

    private fun pixels(): MutableList<CharArray> =
        MutableList(HEIGHT) { CharArray(WIDTH) { PixelSprite.TRANSPARENT_PIXEL } }

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

    /**
     * Front gameplay master produced from planned asset 018, NPC_TAMSIN_TURNAROUND.
     *
     * It preserves the authored identity anchors: slim athletic build, long forearms,
     * compact stance, heavy left fringe, high collar, rolled right sleeve, narrow satchel,
     * left-chest systems badge and warm-brown skin. It is not a generic player reskin.
     */
    val tamsinFront: PixelSprite = run {
        val p = pixels()
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

        // Compact angular crop with heavier left-side fringe.
        rect(p, 12, 2, 9, 2, 'H')
        rect(p, 10, 4, 13, 2, 'H')
        rect(p, 9, 6, 8, 4, 'H')
        rect(p, 17, 6, 6, 2, 'h')
        rect(p, 9, 9, 5, 2, 'H')

        // Face and ears.
        rect(p, 11, 7, 12, 7, 'S')
        rect(p, 10, 10, 1, 2, 's')
        rect(p, 23, 10, 1, 2, 's')
        rect(p, 13, 10, 2, 1, 'O')
        rect(p, 19, 10, 2, 1, 'O')
        rect(p, 16, 13, 3, 1, 's')
        // Right-eyebrow notch cue at gameplay scale.
        rect(p, 20, 9, 1, 1, 'S')

        // Neck and pale work shirt.
        rect(p, 15, 14, 4, 2, 's')
        rect(p, 14, 16, 6, 4, 'P')

        // High-collar charcoal utility jacket.
        rect(p, 11, 16, 3, 4, 'J')
        rect(p, 20, 16, 3, 4, 'J')
        rect(p, 9, 19, 16, 13, 'J')
        rect(p, 11, 20, 12, 2, 'j')
        rect(p, 15, 19, 4, 10, 'P')
        rect(p, 9, 26, 4, 6, 'j')
        rect(p, 21, 26, 4, 6, 'j')

        // Long forearms; right sleeve ends higher because it is rolled.
        rect(p, 6, 20, 3, 13, 'J')
        rect(p, 25, 20, 3, 9, 'J')
        rect(p, 6, 33, 3, 4, 'S')
        rect(p, 25, 29, 3, 8, 'S')

        // Small municipal systems badge on left chest.
        rect(p, 11, 22, 2, 2, 'M')

        // Narrow cross-body strap + compact hip satchel.
        for (i in 0..11) {
            rect(p, 22 - i / 2, 19 + i, 1, 1, 'B')
        }
        rect(p, 10, 29, 6, 5, 'b')
        rect(p, 11, 29, 5, 1, 'B')

        // Dark practical trousers and compact stance.
        rect(p, 12, 32, 4, 12, 'T')
        rect(p, 18, 32, 4, 12, 'T')
        rect(p, 11, 43, 5, 4, 'O')
        rect(p, 18, 43, 5, 4, 'O')

        PixelSprite(
            assetId = TAMSIN_TURNAROUND_ID,
            width = WIDTH,
            height = HEIGHT,
            palette = palette,
            rows = p.map { it.concatToString() },
        )
    }

    /**
     * Guarded injured pose for planned asset 035, SUPPORT_COURIER_01.
     * The pose is non-graphic and keeps the courier visually distinct from Tamsin.
     */
    val woundedCourier: PixelSprite = run {
        val p = pixels()
        val palette = mapOf(
            'O' to Color(0xFF111719),
            'S' to Color(0xFFAD7D62),
            's' to Color(0xFF8B5F4B),
            'U' to Color(0xFF4B5756),
            'u' to Color(0xFF313B3B),
            'T' to Color(0xFF292F30),
            'R' to Color(0xFF9B5D57),
            'M' to Color(0xFF6B726D),
            'G' to Color(0xFFB18B55),
        )

        // Side-lying / braced posture low in the shared 32x48 rig.
        rect(p, 3, 29, 7, 6, 'S')
        rect(p, 2, 27, 7, 3, 'O')
        rect(p, 9, 30, 11, 7, 'U')
        rect(p, 12, 33, 9, 4, 'u')
        rect(p, 20, 35, 6, 4, 'T')
        rect(p, 24, 38, 5, 3, 'T')
        rect(p, 8, 36, 7, 3, 'S')
        rect(p, 17, 30, 2, 3, 'R')
        rect(p, 4, 36, 3, 3, 'M')
        rect(p, 27, 37, 3, 4, 'O')
        // Courier identity plate/strap cue, not readable microtext.
        rect(p, 11, 30, 1, 5, 'G')
        rect(p, 12, 34, 2, 2, 'G')

        PixelSprite(
            assetId = SUPPORT_COURIER_ID,
            width = WIDTH,
            height = HEIGHT,
            palette = palette,
            rows = p.map { it.concatToString() },
        )
    }

    val productionActors: List<PixelSprite> = listOf(tamsinFront, woundedCourier)

    private fun spriteFor(actor: GameRoomActor): PixelSprite? = when (actor.visualFamily) {
        "NPC_TAMSIN" -> tamsinFront
        "SUPPORT_WOUNDED_COURIER" -> woundedCourier
        else -> null
    }

    fun placements(actors: List<GameRoomActor>): List<PixelStoryActorPlacement> =
        actors.mapNotNull { actor ->
            val sprite = spriteFor(actor) ?: return@mapNotNull null
            val point = PixelStoryActorPlacementResolver.resolve(actor.placementKey)
                ?: return@mapNotNull null
            PixelStoryActorPlacement(sprite = sprite, x = point.x, y = point.y)
        }
}
