package com.thegame.rpg.ui

import androidx.compose.ui.graphics.Color

/**
 * Reusable ambient Trace Echo effect.
 *
 * The effect is presentation-only. Scene eligibility is derived exclusively from player-facing
 * scene IDs already present in GameSnapshot; this catalog never reads engine flags or rules state.
 */
object PixelTraceFxCatalog {
    const val TRACE_ECHO_AMBIENT_ID = "FX_TRACE_ECHO_AMBIENT"

    private val palette = mapOf(
        'C' to PixelColors.Cyan,
        'c' to Color(0xFF3B9A9A),
    )

    private fun frame(index: Int, radius: Int): PixelSprite {
        val pixels = MutableList(64) { CharArray(64) { PixelSprite.TRANSPARENT_PIXEL } }

        fun plot(x: Int, y: Int, key: Char) {
            if (x in 0 until 64 && y in 0 until 64) {
                pixels[y][x] = key
            }
        }

        val centerX = 32
        val centerY = 32
        val bright = if (index % 2 == 0) 'C' else 'c'

        // Broken cardinal arcs keep the effect readable without forming a solid ring.
        for (offset in -5..5) {
            if (offset !in -1..1) {
                plot(centerX + offset, centerY - radius, bright)
                plot(centerX + offset, centerY + radius, 'c')
                plot(centerX - radius, centerY + offset, 'c')
                plot(centerX + radius, centerY + offset, bright)
            }
        }

        // Sparse diagonals imply a weak echo rather than a hard targeting reticle.
        val diagonal = (radius * 0.70f).toInt()
        listOf(
            centerX - diagonal to centerY - diagonal,
            centerX + diagonal to centerY - diagonal,
            centerX - diagonal to centerY + diagonal,
            centerX + diagonal to centerY + diagonal,
        ).forEach { (x, y) ->
            plot(x, y, 'c')
            plot(x + 1, y, bright)
        }

        // Small center pulse keeps the source readable at every frame.
        plot(centerX, centerY, 'C')
        plot(centerX - 1, centerY, 'c')
        plot(centerX + 1, centerY, 'c')
        plot(centerX, centerY - 1, 'c')
        plot(centerX, centerY + 1, 'c')

        return PixelSprite(
            assetId = "${TRACE_ECHO_AMBIENT_ID}_FRAME_${index + 1}",
            width = 64,
            height = 64,
            palette = palette,
            rows = pixels.map { it.concatToString() },
        )
    }

    val frames: List<PixelSprite> = listOf(
        frame(index = 0, radius = 10),
        frame(index = 1, radius = 15),
        frame(index = 2, radius = 20),
        frame(index = 3, radius = 25),
    )

    fun forScene(sceneId: String?): List<PixelSprite>? =
        when (sceneId) {
            "OPENING_END",
            "POWER_GATE_TWELVE_SIGNAL",
            "POWER_FIRST_LIVE_USE",
            "POWER_TRACE_STRAIN",
            "POWER_FIRST_PRACTICE",
            "POWER_FIRST_PRACTICE_RESULT",
            "TRACE_DIRECTIONAL_DISCOVERY_RESULT" -> frames

            else -> null
        }
}
