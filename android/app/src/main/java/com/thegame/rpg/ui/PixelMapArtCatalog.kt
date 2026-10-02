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
 * discovery, reachability, travel and tap hit-testing. This catalog supplies the visual
 * district surface and never owns world-state decisions.
 */
object PixelMapArtCatalog {
    const val GATE_TWELVE_DISTRICT_BASE_ID = "MAP_GATE_TWELVE_DISTRICT_BASE"

    // The asset master plan requires district/world maps to be at least 256x144.
    private const val WIDTH = 256
    private const val HEIGHT = 144

    private val palette = mapOf(
        'I' to Color(0xFF101417),
        'D' to Color(0xFF1B2425),
        'G' to Color(0xFF2B3331),
        'S' to Color(0xFF48504A),
        'R' to Color(0xFF5C594F),
        'L' to Color(0xFF7A7462),
        'B' to Color(0xFF30383A),
        'W' to Color(0xFF4F5856),
        'A' to Color(0xFF6A5A4C),
        'P' to Color(0xFF8B8068),
        'V' to Color(0xFF44543D),
        'v' to Color(0xFF2C382D),
        'T' to Color(0xFF765344),
        'Y' to Color(0xFFC6A363),
        'H' to Color(0xFFB6B09B),
        'K' to Color(0xFF202729),
        // Static material accents. These are deliberately close to their parent surfaces so
        // they read as texture at 1x instead of becoming a second geometry layer.
        'c' to Color(0xFF343C39),
        's' to Color(0xFF222C2D),
        'm' to Color(0xFF171D1F),
        'r' to Color(0xFF514F48),
    )

    private fun pixels(): MutableList<CharArray> =
        MutableList(HEIGHT) { CharArray(WIDTH) { 'D' } }

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

        fun outline(x: Int, y: Int, w: Int, h: Int, fill: Char, border: Char = 'I', t: Int = 2) {
            rect(p, x, y, w, h, border)
            rect(p, x + t, y + t, w - 2 * t, h - 2 * t, fill)
        }
        fun windows(x: Int, y: Int, count: Int, spacing: Int = 6) {
            repeat(count) { index -> rect(p, x + index * spacing, y, 3, 2, 'Y') }
        }
        fun tree(x: Int, y: Int) {
            rect(p, x, y + 5, 2, 4, 'A')
            rect(p, x - 2, y + 1, 6, 6, 'v')
            rect(p, x - 1, y, 4, 4, 'V')
        }
        fun lamp(x: Int, y: Int) {
            rect(p, x, y, 1, 6, 'S')
            rect(p, x - 1, y - 1, 3, 2, 'Y')
        }
        fun surfaceTexture(
            x: Int,
            y: Int,
            w: Int,
            h: Int,
            base: Char,
            accent: Char,
            cellWidth: Int,
            cellHeight: Int,
        ) {
            for (yy in y until y + h) {
                for (xx in x until x + w) {
                    if (xx !in 0 until WIDTH || yy !in 0 until HEIGHT || p[yy][xx] != base) continue
                    val localX = xx - x
                    val localY = yy - y
                    val row = localY / cellHeight
                    val horizontalJoint =
                        localY % cellHeight == cellHeight - 1 &&
                            ((localX / cellWidth) + row) % 2 == 0
                    val verticalJoint =
                        localX % cellWidth == cellWidth - 1 &&
                            localY % cellHeight in 2 until (cellHeight - 2)
                    if (horizontalJoint || verticalJoint) p[yy][xx] = accent
                }
            }
        }
        fun linearWear(
            x: Int,
            y: Int,
            w: Int,
            h: Int,
            base: Char,
            accent: Char,
            xStep: Int,
            yStep: Int,
        ) {
            for (yy in y until y + h step yStep) {
                for (xx in x until x + w step xStep) {
                    if (xx !in 0 until WIDTH || yy !in 0 until HEIGHT) continue
                    if (p[yy][xx] == base) p[yy][xx] = accent
                    if (xx + 1 in 0 until WIDTH && p[yy][xx + 1] == base) p[yy][xx + 1] = accent
                }
            }
        }

        // Surface civic district, depot/service belt, then darker maintenance infrastructure.
        rect(p, 0, 0, WIDTH, 48, 'G')
        rect(p, 0, 48, WIDTH, 47, 'D')
        rect(p, 0, 95, WIDTH, 49, 'K')

        // First static texture pass. It is stamped before roads and landmarks so authored
        // geometry always wins when layers overlap.
        surfaceTexture(0, 0, WIDTH, 48, 'G', 'c', cellWidth = 16, cellHeight = 8)
        surfaceTexture(0, 48, WIDTH, 47, 'D', 's', cellWidth = 20, cellHeight = 12)
        surfaceTexture(0, 95, WIDTH, 49, 'K', 'm', cellWidth = 24, cellHeight = 10)

        // Perimeter streets.
        rect(p, 0, 5, WIDTH, 7, 'R')
        rect(p, 0, 7, WIDTH, 2, 'L')
        rect(p, 0, 126, WIDTH, 8, 'R')
        rect(p, 0, 128, WIDTH, 2, 'L')

        // Upper boulevard: Workshop Row -> Depot Plaza -> Municipal Archive.
        line(p, 70, 23, 123, 26, 'R', 9)
        line(p, 123, 26, 169, 23, 'R', 9)
        line(p, 70, 23, 123, 26, 'L', 2)
        line(p, 123, 26, 169, 23, 'L', 2)

        // Depot/service routes mirror the authored graph without owning route state.
        listOf(
            intArrayOf(46, 52, 87, 45),
            intArrayOf(46, 52, 136, 69),
            intArrayOf(46, 52, 102, 101),
            intArrayOf(136, 69, 179, 88),
            intArrayOf(136, 69, 210, 56),
            intArrayOf(179, 88, 210, 56),
        ).forEach { route ->
            line(p, route[0], route[1], route[2], route[3], 'R', 7)
            line(p, route[0], route[1], route[2], route[3], 'L', 1)
        }

        // Neutral asphalt/service-road wear. This only recolors already-authored road pixels;
        // it cannot create, extend, enable, or disable a route.
        linearWear(0, 0, WIDTH, HEIGHT, 'R', 'r', xStep = 13, yStep = 9)

        // Workshop Row: attached practical shops rather than a single abstract block.
        outline(49, 8, 54, 22, 'A')
        listOf(53, 65, 77, 89).forEach { x ->
            outline(x, 12, 10, 13, 'B', t = 1)
            rect(p, x + 2, 19, 6, 4, 'W')
            rect(p, x + 3, 14, 4, 2, 'Y')
            // Static workshop-bay material cues stay inside the authored bay box.
            rect(p, x + 1, 17, 8, 1, 'S')
            rect(p, x + 1, 24, 8, 1, 'I')
        }
        // Shared service canopy/utility seam: visual identity only, no footprint change.
        rect(p, 52, 10, 48, 1, 'S')
        rect(p, 48, 28, 56, 3, 'S')

        // Depot Plaza paving and civic frontage.
        rect(p, 105, 8, 39, 32, 'P')
        for (y in 12..38 step 6) rect(p, 109, y, 31, 1, 'L')
        for (x in 110..140 step 7) rect(p, x, 12, 1, 24, 'L')
        outline(108, 31, 33, 13, 'B')
        windows(113, 35, 4, 6)
        tree(108, 16)
        tree(142, 16)
        lamp(118, 14)
        lamp(134, 14)

        // Municipal Archive frontage/courtyard.
        outline(151, 6, 46, 28, 'A')
        rect(p, 157, 10, 34, 5, 'P')
        listOf(159, 167, 175, 183).forEach { x ->
            rect(p, x, 16, 4, 12, 'W')
            rect(p, x + 1, 18, 2, 7, 'H')
        }
        rect(p, 154, 30, 40, 3, 'S')
        tree(148, 18)
        tree(200, 18)

        // Platform Nine depot, platform roof and visible tram/maintenance tracks.
        outline(20, 37, 64, 36, 'B')
        rect(p, 25, 42, 54, 10, 'W')
        windows(29, 45, 7, 7)
        rect(p, 27, 56, 50, 5, 'S')
        rect(p, 18, 69, 68, 3, 'R')
        rect(p, 18, 75, 68, 3, 'R')
        linearWear(18, 68, 68, 11, 'R', 'r', xStep = 11, yStep = 3)
        for (x in 21..84 step 8) rect(p, x, 68, 2, 11, 'L')

        // Relay Workbench annex.
        outline(75, 31, 31, 28, 'B')
        rect(p, 80, 36, 21, 9, 'W')
        rect(p, 83, 39, 15, 3, 'Y')
        rect(p, 80, 49, 21, 6, 'A')
        rect(p, 84, 51, 13, 2, 'H')

        // Service Gate Twelve.
        outline(119, 56, 36, 30, 'B')
        rect(p, 125, 62, 24, 16, 'W')
        // Reinforced jamb strips and bolt clusters stay within the sealed-gate rectangle.
        rect(p, 127, 64, 2, 12, 'S')
        rect(p, 145, 64, 2, 12, 'S')
        listOf(66, 71).forEach { y ->
            rect(p, 130, y, 1, 1, 'H')
            rect(p, 143, y, 1, 1, 'H')
        }
        rect(p, 133, 62, 8, 16, 'I')
        rect(p, 136, 65, 2, 10, 'Y')
        rect(p, 121, 82, 32, 3, 'S')

        // Quiet Stair utility shaft.
        outline(88, 89, 31, 35, 'B')
        rect(p, 94, 95, 19, 22, 'W')
        listOf(98, 102, 106, 110, 114).forEach { y -> rect(p, 97, y, 13, 2, 'L') }
        rect(p, 91, 120, 25, 2, 'S')

        // Service Tunnel plant and access ribs.
        outline(161, 78, 39, 31, 'B')
        rect(p, 167, 84, 27, 18, 'W')
        for (x in 170..193 step 6) rect(p, x, 87, 2, 12, 'I')
        rect(p, 164, 105, 33, 2, 'S')

        // Trace Chamber remains grounded municipal infrastructure; no neon world palette.
        outline(194, 40, 44, 32, 'B')
        rect(p, 201, 47, 30, 18, 'W')
        rect(p, 208, 51, 16, 10, 'I')
        rect(p, 212, 54, 8, 4, 'H')
        rect(p, 198, 68, 36, 2, 'S')

        // Street furniture, sparse vegetation and material breakup.
        listOf(
            intArrayOf(12, 21), intArrayOf(32, 20), intArrayOf(215, 20),
            intArrayOf(238, 22), intArrayOf(11, 91), intArrayOf(242, 88),
            intArrayOf(145, 104), intArrayOf(67, 105),
        ).forEach { tree(it[0], it[1]) }
        listOf(
            intArrayOf(16, 28), intArrayOf(42, 29), intArrayOf(214, 30),
            intArrayOf(240, 31), intArrayOf(112, 53), intArrayOf(158, 63),
        ).forEach { lamp(it[0], it[1]) }

        for (x in 4..250 step 13) rect(p, x, 116 + (x % 4), 6, 1, 'S')
        for (x in 7..248 step 17) rect(p, x, 135 + (x % 3), 8, 2, 'G')
        listOf(
            intArrayOf(57, 33), intArrayOf(66, 34), intArrayOf(224, 78),
            intArrayOf(231, 82), intArrayOf(12, 112),
        ).forEach {
            rect(p, it[0], it[1], 7, 3, 'A')
            rect(p, it[0] + 1, it[1] + 1, 5, 1, 'P')
        }

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
