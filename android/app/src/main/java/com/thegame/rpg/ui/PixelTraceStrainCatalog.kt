package com.thegame.rpg.ui

import androidx.compose.ui.graphics.Color

/**
 * Player-visible Trace strain presentation.
 *
 * Eligibility is supplied only from projected condition IDs. This catalog does not query engine
 * condition registries, hidden flags, or ability state.
 */
object PixelTraceStrainCatalog {
    const val TRACE_STRAIN_ID = "FX_TRACE_STRAIN"
    const val ECHO_STRAIN_CONDITION_ID = "COND_ECHO_STRAIN"

    private val palette = mapOf(
        'D' to PixelColors.Danger,
        'C' to PixelColors.Cyan,
        'm' to Color(0xFF7A4D55),
    )

    private fun avatarFrame(index: Int): PixelSprite {
        val pixels = MutableList(48) { CharArray(32) { PixelSprite.TRANSPARENT_PIXEL } }

        fun plot(x: Int, y: Int, key: Char) {
            if (x in 0 until 32 && y in 0 until 48) pixels[y][x] = key
        }

        val jitter = index % 2
        val opposite = 1 - jitter

        // Edge noise around the head and shoulders communicates sensory strain without altering body art.
        listOf(
            8 + jitter to 5,
            23 - jitter to 7,
            6 + opposite to 14,
            25 - opposite to 15,
            5 + jitter to 25,
            26 - jitter to 27,
            8 + opposite to 39,
            23 - opposite to 40,
        ).forEachIndexed { pointIndex, (x, y) ->
            plot(x, y, if ((pointIndex + index) % 3 == 0) 'D' else 'm')
            plot(x + if (x < 16) 1 else -1, y, 'C')
        }

        // Short offset streaks create a restrained pulse/noise cue around the silhouette.
        for (step in 0..3) {
            plot(3 + step + jitter, 18 + step * 5, 'm')
            plot(28 - step - jitter, 19 + step * 5, if (step == index % 4) 'D' else 'm')
        }

        return PixelSprite(
            assetId = "${TRACE_STRAIN_ID}_AVATAR_FRAME_${index + 1}",
            width = 32,
            height = 48,
            palette = palette,
            rows = pixels.map { it.concatToString() },
        )
    }

    private fun portraitFrame(index: Int): PixelSprite {
        val pixels = MutableList(64) { CharArray(64) { PixelSprite.TRANSPARENT_PIXEL } }

        fun plot(x: Int, y: Int, key: Char) {
            if (x in 0 until 64 && y in 0 until 64) pixels[y][x] = key
        }

        // Portrait master remains reusable until a dedicated portrait surface is introduced.
        val offset = index % 3
        for (i in 0..7) {
            plot(8 + i * 6, 10 + ((i + offset) % 3), if (i % 3 == 0) 'D' else 'm')
            plot(9 + i * 6, 52 - ((i + offset) % 3), 'C')
        }
        for (i in 0..5) {
            plot(8 + ((i + offset) % 3), 16 + i * 6, 'm')
            plot(55 - ((i + offset) % 3), 17 + i * 6, if (i % 2 == 0) 'D' else 'm')
        }

        return PixelSprite(
            assetId = "${TRACE_STRAIN_ID}_PORTRAIT_FRAME_${index + 1}",
            width = 64,
            height = 64,
            palette = palette,
            rows = pixels.map { it.concatToString() },
        )
    }

    val avatarFrames: List<PixelSprite> = List(4) { avatarFrame(it) }
    val portraitFrames: List<PixelSprite> = List(4) { portraitFrame(it) }

    fun avatarForConditions(conditionIds: Collection<String>): List<PixelSprite>? =
        if (ECHO_STRAIN_CONDITION_ID in conditionIds) avatarFrames else null

    fun portraitForConditions(conditionIds: Collection<String>): List<PixelSprite>? =
        if (ECHO_STRAIN_CONDITION_ID in conditionIds) portraitFrames else null
}
