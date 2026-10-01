package com.thegame.rpg.ui

import androidx.compose.ui.graphics.Color

/**
 * Small reusable UI/accessibility assets which are presentation-only.
 */
object PixelUiUtilityCatalog {
    const val SCROLL_MARKER_ID = "UI_SCROLL_MARKER"
    const val AUDIO_NARRATION_ICON_ID = "ACCESS_AUDIO_NARRATION_ICON"

    private fun blank(width: Int, height: Int): MutableList<CharArray> =
        MutableList(height) { CharArray(width) { PixelSprite.TRANSPARENT_PIXEL } }

    val scrollMarker: PixelSprite = run {
        val width = 16
        val height = 16
        val pixels = blank(width, height)

        fun point(x: Int, y: Int, key: Char) {
            if (x in 0 until width && y in 0 until height) pixels[y][x] = key
        }

        for (i in 0..4) {
            point(3 + i, 5 + i, 'C')
            point(12 - i, 5 + i, 'C')
            point(4 + i, 5 + i, 'P')
            point(11 - i, 5 + i, 'P')
        }
        point(7, 11, 'G')
        point(8, 11, 'G')
        point(7, 12, 'G')
        point(8, 12, 'G')

        PixelSprite(
            assetId = SCROLL_MARKER_ID,
            width = width,
            height = height,
            palette = mapOf(
                'C' to PixelColors.Cyan,
                'P' to PixelColors.Paper,
                'G' to PixelColors.Gold,
            ),
            rows = pixels.map { it.concatToString() },
        )
    }

    val narrationIcon: PixelSprite = run {
        val width = 24
        val height = 24
        val pixels = blank(width, height)

        fun rect(x: Int, y: Int, w: Int, h: Int, key: Char) {
            for (yy in y until y + h) {
                for (xx in x until x + w) {
                    if (xx in 0 until width && yy in 0 until height) {
                        pixels[yy][xx] = key
                    }
                }
            }
        }

        // Speaker body / horn.
        rect(3, 9, 4, 6, 'P')
        rect(7, 7, 3, 10, 'P')
        rect(10, 5, 3, 14, 'C')

        // Three angular sound-wave bands. These are shape-coded, not color-only.
        rect(15, 8, 2, 8, 'C')
        rect(17, 6, 2, 3, 'P')
        rect(17, 15, 2, 3, 'P')
        rect(20, 4, 2, 4, 'G')
        rect(20, 16, 2, 4, 'G')

        PixelSprite(
            assetId = AUDIO_NARRATION_ICON_ID,
            width = width,
            height = height,
            palette = mapOf(
                'C' to PixelColors.Cyan,
                'P' to PixelColors.Paper,
                'G' to PixelColors.Gold,
            ),
            rows = pixels.map { it.concatToString() },
        )
    }
}
