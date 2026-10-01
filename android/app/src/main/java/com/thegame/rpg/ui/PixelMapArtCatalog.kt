package com.thegame.rpg.ui

import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import kotlin.math.floor
import kotlin.math.min

data class PixelMapViewport(
    val originX: Float,
    val originY: Float,
    val width: Float,
    val height: Float,
    val pixelSize: Float,
) {
    fun point(xPercent: Double, yPercent: Double): Offset = Offset(
        x = originX + (xPercent.coerceIn(0.0, 100.0) / 100.0 * width).toFloat(),
        y = originY + (yPercent.coerceIn(0.0, 100.0) / 100.0 * height).toFloat(),
    )
}


/**
 * Presentation-only pixel map surface for the Gate Twelve district.
 *
 * The authored world-map coordinates/edges remain authoritative for node placement,
 * discovery, reachability, travel and tap hit-testing. This catalog only supplies a
 * coherent pixel-art backdrop so the map no longer reads as geometry on a flat panel.
 */
object PixelMapArtCatalog {
    const val GATE_TWELVE_DISTRICT_BASE_ID = "MAP_GATE_TWELVE_DISTRICT_BASE"

    private const val WIDTH = 128
    private const val HEIGHT = 72

    private val palette = mapOf(
        'I' to Color(0xFF11171A),
        'D' to Color(0xFF1A2427),
        'G' to Color(0xFF263238),
        'S' to Color(0xFF3A4545),
        'R' to Color(0xFF655E4E),
        'L' to Color(0xFF817760),
        'B' to Color(0xFF323C3B),
        'W' to Color(0xFF59615B),
        'A' to Color(0xFF756A52),
        'P' to Color(0xFF9A8D6B),
    )

    private fun pixels(): MutableList<CharArray> =
        MutableList(HEIGHT) { CharArray(WIDTH) { 'I' } }

    private fun rect(
        pixels: MutableList<CharArray>,
        x: Int,
        y: Int,
        width: Int,
        height: Int,
        key: Char,
    ) {
        for (yy in y until y + height) for (xx in x until x + width) {
            if (xx in 0 until WIDTH && yy in 0 until HEIGHT) pixels[yy][xx] = key
        }
    }

    private fun line(
        pixels: MutableList<CharArray>,
        x0: Int,
        y0: Int,
        x1: Int,
        y1: Int,
        key: Char,
        thickness: Int = 1,
    ) {
        var x = x0
        var y = y0
        val dx = kotlin.math.abs(x1 - x0)
        val sx = if (x0 < x1) 1 else -1
        val dy = -kotlin.math.abs(y1 - y0)
        val sy = if (y0 < y1) 1 else -1
        var err = dx + dy
        while (true) {
            rect(pixels, x - thickness / 2, y - thickness / 2, thickness, thickness, key)
            if (x == x1 && y == y1) break
            val e2 = 2 * err
            if (e2 >= dy) {
                err += dy
                x += sx
            }
            if (e2 <= dx) {
                err += dx
                y += sy
            }
        }
    }

    val gateTwelveDistrictBase: PixelSprite = run {
        val p = pixels()

        // Ground/value breakup: practical municipal district, not neon/cyberpunk.
        rect(p, 0, 0, WIDTH, 16, 'D')
        rect(p, 0, 16, WIDTH, 28, 'G')
        rect(p, 0, 44, WIDTH, 28, 'D')
        rect(p, 5, 6, 118, 4, 'S')
        rect(p, 3, 62, 122, 4, 'S')

        // Upper district road linking Workshop Row -> Depot Plaza -> Archive.
        line(p, 28, 13, 61, 13, 'R', 5)
        line(p, 61, 13, 84, 12, 'R', 5)
        line(p, 28, 13, 61, 13, 'L', 1)
        line(p, 61, 13, 84, 12, 'L', 1)

        // Depot/service infrastructure routes mirror the authored graph as visual roads.
        line(p, 23, 26, 44, 22, 'R', 4)
        line(p, 23, 26, 68, 35, 'R', 4)
        line(p, 23, 26, 51, 50, 'R', 4)
        line(p, 68, 35, 90, 44, 'R', 4)
        line(p, 68, 35, 105, 28, 'R', 4)
        line(p, 90, 44, 105, 28, 'R', 4)

        // Municipal blocks/buildings around the node corridors.
        rect(p, 8, 17, 27, 14, 'B')   // depot/platform mass
        rect(p, 12, 20, 19, 8, 'W')
        rect(p, 34, 16, 20, 12, 'B')  // workbench/service annex
        rect(p, 38, 19, 12, 6, 'W')
        rect(p, 55, 26, 25, 17, 'B')  // Gate Twelve service block
        rect(p, 60, 30, 15, 9, 'W')
        rect(p, 82, 38, 24, 15, 'B')  // tunnel/service plant
        rect(p, 87, 42, 14, 7, 'W')
        rect(p, 42, 46, 18, 16, 'B')  // stair/utility block
        rect(p, 46, 50, 10, 8, 'W')
        rect(p, 98, 19, 23, 18, 'B')  // trace chamber
        rect(p, 103, 23, 13, 10, 'W')

        // Upper free-roam district silhouettes.
        rect(p, 20, 4, 19, 11, 'A')   // workshop row
        rect(p, 23, 7, 4, 6, 'P')
        rect(p, 29, 6, 7, 7, 'W')
        rect(p, 53, 3, 18, 13, 'A')   // depot plaza edge / civic frontage
        rect(p, 57, 6, 10, 7, 'P')
        rect(p, 76, 3, 21, 12, 'A')   // archive
        rect(p, 80, 6, 13, 7, 'W')

        // Small material/detail clusters keep the surface authored at native scale.
        for (x in 5..120 step 11) rect(p, x, 39 + (x % 3), 5, 2, 'S')
        for (x in 8..116 step 18) rect(p, x, 57, 8, 2, 'G')

        PixelSprite(
            assetId = GATE_TWELVE_DISTRICT_BASE_ID,
            width = WIDTH,
            height = HEIGHT,
            palette = palette,
            rows = p.map { it.concatToString() },
        )
    }

    fun base(mapTitle: String): PixelSprite? =
        if (mapTitle == "Gate Twelve District") gateTwelveDistrictBase else null

    /**
     * Keeps authored percentage coordinates, map art, route overlays and tap hit-testing
     * inside the same letterboxed native-pixel viewport.
     */
    fun viewport(mapTitle: String, canvasWidth: Float, canvasHeight: Float): PixelMapViewport {
        val safeWidth = canvasWidth.coerceAtLeast(1f)
        val safeHeight = canvasHeight.coerceAtLeast(1f)
        val sprite = base(mapTitle) ?: return PixelMapViewport(
            originX = 0f,
            originY = 0f,
            width = safeWidth,
            height = safeHeight,
            pixelSize = 1f,
        )

        val rawScale = min(
            safeWidth / sprite.width.toFloat(),
            safeHeight / sprite.height.toFloat(),
        )
        val pixelSize = if (rawScale >= 1f) floor(rawScale) else rawScale.coerceAtLeast(0.01f)
        val width = sprite.width * pixelSize
        val height = sprite.height * pixelSize
        return PixelMapViewport(
            originX = (safeWidth - width) / 2f,
            originY = (safeHeight - height) / 2f,
            width = width,
            height = height,
            pixelSize = pixelSize,
        )
    }
}
