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
    const val SIGNAL_PULSE_ID = "FX_SIGNAL_PULSE"
    const val DIRECTIONAL_TRACE_ID = "FX_DIRECTIONAL_TRACE"

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

    private fun signalPulseFrame(index: Int, radius: Int): PixelSprite {
        val pixels = MutableList(64) { CharArray(64) { PixelSprite.TRANSPARENT_PIXEL } }

        fun plot(x: Int, y: Int, key: Char) {
            if (x in 0 until 64 && y in 0 until 64) pixels[y][x] = key
        }

        val centerX = 32
        val centerY = 32
        val edge = if (index < 3) 'C' else 'c'

        // Controlled expanding pulse: sparse square-circle hybrid arcs stay crisp at native scale.
        for (offset in -4..4) {
            plot(centerX + offset, centerY - radius, edge)
            plot(centerX + offset, centerY + radius, edge)
            plot(centerX - radius, centerY + offset, edge)
            plot(centerX + radius, centerY + offset, edge)
        }

        val diagonal = (radius * 0.72f).toInt()
        listOf(
            centerX - diagonal to centerY - diagonal,
            centerX + diagonal to centerY - diagonal,
            centerX - diagonal to centerY + diagonal,
            centerX + diagonal to centerY + diagonal,
        ).forEach { (x, y) ->
            plot(x, y, edge)
            plot(x + 1, y, edge)
        }

        // Bright source core peaks early and fades as the ring expands.
        val core = when (index) {
            0, 1 -> 2
            2, 3 -> 1
            else -> 0
        }
        for (y in -core..core) {
            for (x in -core..core) {
                plot(centerX + x, centerY + y, if (index < 4) 'C' else 'c')
            }
        }

        return PixelSprite(
            assetId = "${SIGNAL_PULSE_ID}_FRAME_${index + 1}",
            width = 64,
            height = 64,
            palette = palette,
            rows = pixels.map { it.concatToString() },
        )
    }

    val signalPulseFrames: List<PixelSprite> = listOf(
        signalPulseFrame(index = 0, radius = 4),
        signalPulseFrame(index = 1, radius = 8),
        signalPulseFrame(index = 2, radius = 13),
        signalPulseFrame(index = 3, radius = 19),
        signalPulseFrame(index = 4, radius = 25),
        signalPulseFrame(index = 5, radius = 30),
    )

    fun signalPulseForScene(sceneId: String?): List<PixelSprite>? =
        if (sceneId == "POWER_FIRST_LIVE_USE") signalPulseFrames else null

    private fun directionalTraceFrame(index: Int): PixelSprite {
        val pixels = MutableList(64) { CharArray(64) { PixelSprite.TRANSPARENT_PIXEL } }

        fun plot(x: Int, y: Int, key: Char) {
            if (x in 0 until 64 && y in 0 until 64) pixels[y][x] = key
        }

        val originX = 20
        val originY = 32
        val reach = listOf(8, 13, 18, 24, 30, 36)[index]
        val halfSpread = listOf(9, 8, 6, 5, 3, 1)[index]
        val edge = if (index < 4) 'C' else 'c'

        // The early frames begin as a broad sensing sector and collapse into a directional ray.
        for (dx in 0..reach) {
            val progress = if (reach == 0) 1f else dx.toFloat() / reach.toFloat()
            val spread = ((1f - progress) * halfSpread).toInt()
            val x = originX + dx

            if (spread > 0) {
                plot(x, originY - spread, 'c')
                plot(x, originY + spread, 'c')
            }

            if (index >= 3 || dx % 2 == 0) {
                plot(x, originY, edge)
            }
        }

        // Strong terminal cluster communicates direction without embedding destination data.
        val tipX = (originX + reach).coerceAtMost(63)
        for (dy in -2..2) {
            plot(tipX, originY + dy, edge)
        }
        plot((tipX - 1).coerceAtLeast(0), originY, 'C')
        plot((tipX - 2).coerceAtLeast(0), originY, 'C')

        return PixelSprite(
            assetId = "${DIRECTIONAL_TRACE_ID}_FRAME_${index + 1}",
            width = 64,
            height = 64,
            palette = palette,
            rows = pixels.map { it.concatToString() },
        )
    }

    val directionalTraceFrames: List<PixelSprite> =
        List(6) { index -> directionalTraceFrame(index) }

    fun directionalTraceForScene(sceneId: String?): List<PixelSprite>? =
        if (sceneId == "TRACE_DIRECTIONAL_DISCOVERY_RESULT") directionalTraceFrames else null

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
