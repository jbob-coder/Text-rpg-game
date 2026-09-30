package com.thegame.rpg.ui

import androidx.compose.ui.graphics.Color

/**
 * Source-native masters for held technical props which are not yet bound to character rigs.
 *
 * This catalog is presentation-only. It must not infer inventory, interaction, quest,
 * relationship, or story state.
 */
object PixelHeldPropCatalog {
    const val DIAGNOSTIC_READER_ID = "PROP_DIAGNOSTIC_READER"
    const val DIAGNOSTIC_READER_ICON_MASTER_ID = "PROP_DIAGNOSTIC_READER_ICON_MASTER"
    const val DIAGNOSTIC_READER_HELD_FRONT_MASTER_ID = "PROP_DIAGNOSTIC_READER_HELD_FRONT_MASTER"

    private val palette = mapOf(
        'O' to PixelColors.Ink,
        'D' to Color(0xFF172128),
        'M' to Color(0xFF34454D),
        'L' to Color(0xFF667981),
        'C' to PixelColors.Cyan,
        'G' to PixelColors.Gold,
        'P' to PixelColors.Paper,
    )

    private fun pixels(width: Int, height: Int): MutableList<CharArray> =
        MutableList(height) { CharArray(width) { PixelSprite.TRANSPARENT_PIXEL } }

    private fun sprite(
        assetId: String,
        width: Int,
        height: Int,
        draw: (
            rect: (Int, Int, Int, Int, Char) -> Unit,
            point: (Int, Int, Char) -> Unit,
        ) -> Unit,
    ): PixelSprite {
        val p = pixels(width, height)

        val point: (Int, Int, Char) -> Unit = { x, y, key ->
            if (x in 0 until width && y in 0 until height) {
                p[y][x] = key
            }
        }
        val rect: (Int, Int, Int, Int, Char) -> Unit = { x, y, w, h, key ->
            for (yy in y until y + h) for (xx in x until x + w) {
                point(xx, yy, key)
            }
        }

        draw(rect, point)

        return PixelSprite(
            assetId = assetId,
            width = width,
            height = height,
            palette = palette,
            rows = p.map { it.concatToString() },
        )
    }

    /**
     * 32x32 inventory/reference icon master.
     *
     * The icon depicts a compact municipal diagnostic reader with a cyan display,
     * gold status key, and short sensor crown. It is not an inventory item by itself.
     */
    val diagnosticReaderIconMaster: PixelSprite = sprite(
        assetId = DIAGNOSTIC_READER_ICON_MASTER_ID,
        width = 32,
        height = 32,
    ) { rect, point ->
        rect(11, 5, 10, 22, 'O')
        rect(12, 6, 8, 20, 'M')
        rect(14, 3, 4, 3, 'D')
        point(13, 2, 'L')
        point(18, 2, 'L')

        rect(13, 8, 6, 7, 'D')
        rect(14, 9, 4, 4, 'C')
        point(14, 14, 'L')
        point(17, 14, 'L')

        rect(13, 17, 2, 2, 'G')
        rect(17, 17, 2, 2, 'P')
        rect(13, 21, 6, 2, 'D')

        point(10, 8, 'L')
        point(21, 8, 'L')
        point(10, 23, 'D')
        point(21, 23, 'D')
    }

    /**
     * 32x48 transparent held-prop reference master.
     *
     * The reader geometry is production-ready, but its placement is deliberately only a
     * neutral reference position. Character-specific wrist/hand anchors remain blocked on
     * canonical player/Tamsin geometry and must be authored before runtime binding.
     */
    val diagnosticReaderHeldFrontMaster: PixelSprite = sprite(
        assetId = DIAGNOSTIC_READER_HELD_FRONT_MASTER_ID,
        width = 32,
        height = 48,
    ) { rect, point ->
        rect(18, 22, 8, 14, 'O')
        rect(19, 23, 6, 12, 'M')

        rect(20, 19, 3, 4, 'D')
        point(19, 18, 'L')
        point(23, 18, 'L')

        rect(20, 25, 4, 4, 'D')
        rect(21, 26, 2, 2, 'C')

        point(20, 31, 'G')
        point(23, 31, 'P')
        rect(20, 33, 4, 1, 'D')

        point(17, 24, 'L')
        point(26, 33, 'D')
    }

    val productionMasters: List<PixelSprite> = listOf(
        diagnosticReaderIconMaster,
        diagnosticReaderHeldFrontMaster,
    )
}
