package com.thegame.rpg.ui

import androidx.compose.ui.graphics.Color

data class PixelAnimationBounds(
    val left: Int,
    val top: Int,
    val right: Int,
    val bottom: Int,
) {
    init {
        require(left >= 0 && top >= 0)
        require(right >= left && bottom >= top)
    }

    fun contains(x: Int, y: Int): Boolean =
        x in left..right && y in top..bottom
}

data class PixelAmbientAnimationTrack(
    val trackId: String,
    val frameDurationMs: Long,
    val bounds: PixelAnimationBounds,
    val frames: List<PixelSprite>,
) {
    init {
        require(trackId.isNotBlank())
        require(frameDurationMs >= 80L)
        require(frames.size >= 2)
        val first = frames.first()
        require(frames.all { it.width == first.width && it.height == first.height }) {
            "$trackId frames must share one native grid"
        }
    }
}

/**
 * Presentation-only environmental motion.
 *
 * Ambient tracks are selected only from the visible location ID. They must never encode hidden
 * quest/rules state. Story-state animation belongs in the player-safe scene/visual overlay path.
 */
object PixelAmbientAnimationCatalog {
    const val SERVICE_TUNNEL_FAN_TRACK_ID = "SERVICE_TUNNEL_AMBIENT_FAN"
    const val SERVICE_TUNNEL_PANEL_TRACK_ID = "SERVICE_TUNNEL_AMBIENT_PANEL"
    const val SERVICE_TUNNEL_DRIP_TRACK_ID = "SERVICE_TUNNEL_AMBIENT_DRIP"

    private const val WIDTH = 128
    private const val HEIGHT = 64

    private val ambientPalette = mapOf(
        'm' to Color(0xFF66747B),
        'd' to Color(0xFF344147),
        'c' to Color(0xFF3B9A9A),
        'C' to PixelColors.Cyan,
    )

    private fun frame(
        assetId: String,
        draw: (plot: (Int, Int, Char) -> Unit) -> Unit,
    ): PixelSprite {
        val pixels = MutableList(HEIGHT) {
            CharArray(WIDTH) { PixelSprite.TRANSPARENT_PIXEL }
        }

        fun plot(x: Int, y: Int, key: Char) {
            if (x in 0 until WIDTH && y in 0 until HEIGHT) {
                pixels[y][x] = key
            }
        }

        draw(::plot)

        return PixelSprite(
            assetId = assetId,
            width = WIDTH,
            height = HEIGHT,
            palette = ambientPalette,
            rows = pixels.map { it.concatToString() },
        )
    }

    private fun fanFrame(index: Int): PixelSprite =
        frame("${SERVICE_TUNNEL_FAN_TRACK_ID}_FRAME_${index + 1}") { plot ->
            val cx = 85
            val cy = 21
            plot(cx, cy, 'C')

            when (index) {
                0 -> {
                    for (x in cx - 3..cx + 3) plot(x, cy, 'm')
                    for (y in cy - 3..cy + 3) plot(cx, y, 'm')
                    plot(cx, cy, 'C')
                    plot(cx, cy - 3, 'c')
                }
                1 -> {
                    for (delta in -3..3) {
                        plot(cx + delta, cy + delta, 'm')
                        plot(cx + delta, cy - delta, 'm')
                    }
                    plot(cx, cy, 'C')
                    plot(cx + 3, cy - 3, 'c')
                }
                2 -> {
                    for (x in cx - 3..cx + 3) plot(x, cy, 'm')
                    for (y in cy - 3..cy + 3) plot(cx, y, 'm')
                    plot(cx, cy, 'C')
                    plot(cx + 3, cy, 'c')
                }
                else -> {
                    for (delta in -3..3) {
                        plot(cx + delta, cy + delta, 'm')
                        plot(cx + delta, cy - delta, 'm')
                    }
                    plot(cx, cy, 'C')
                    plot(cx + 3, cy + 3, 'c')
                }
            }
        }

    private fun panelFrame(index: Int): PixelSprite =
        frame("${SERVICE_TUNNEL_PANEL_TRACK_ID}_FRAME_${index + 1}") { plot ->
            for (x in 40..44) {
                plot(x, 31, 'd')
                plot(x, 33, 'd')
            }
            plot(40, 32, 'd')
            plot(44, 32, 'd')

            val indicators = listOf(41, 42, 43)
            indicators.forEachIndexed { indicatorIndex, x ->
                plot(x, 32, if (indicatorIndex == index) 'C' else 'c')
            }
        }

    private fun dripFrame(index: Int): PixelSprite =
        frame("${SERVICE_TUNNEL_DRIP_TRACK_ID}_FRAME_${index + 1}") { plot ->
            val x = 117
            val y = 36 + index
            plot(x, y, if (index < 4) 'c' else 'C')
            if (index == 4) {
                plot(x - 1, y + 1, 'c')
                plot(x + 1, y + 1, 'c')
            }
        }

    val serviceTunnelFan = PixelAmbientAnimationTrack(
        trackId = SERVICE_TUNNEL_FAN_TRACK_ID,
        frameDurationMs = 220L,
        bounds = PixelAnimationBounds(left = 82, top = 18, right = 88, bottom = 24),
        frames = List(4) { fanFrame(it) },
    )

    val serviceTunnelPanel = PixelAmbientAnimationTrack(
        trackId = SERVICE_TUNNEL_PANEL_TRACK_ID,
        frameDurationMs = 450L,
        bounds = PixelAnimationBounds(left = 40, top = 31, right = 44, bottom = 33),
        frames = List(3) { panelFrame(it) },
    )

    val serviceTunnelDrip = PixelAmbientAnimationTrack(
        trackId = SERVICE_TUNNEL_DRIP_TRACK_ID,
        frameDurationMs = 260L,
        bounds = PixelAnimationBounds(left = 116, top = 36, right = 118, bottom = 41),
        frames = List(5) { dripFrame(it) },
    )

    private val serviceTunnelTracks = listOf(
        serviceTunnelFan,
        serviceTunnelPanel,
        serviceTunnelDrip,
    )

    fun forLocation(locationId: String): List<PixelAmbientAnimationTrack> =
        when (locationId) {
            "SERVICE_TUNNEL" -> serviceTunnelTracks
            else -> emptyList()
        }
}
