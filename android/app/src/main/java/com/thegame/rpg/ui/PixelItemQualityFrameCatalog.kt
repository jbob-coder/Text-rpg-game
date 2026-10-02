package com.thegame.rpg.ui

/**
 * Asset 039: quality frames are visual metadata overlays, never replacements for item art.
 *
 * Only explicit player-safe quality values map to a frame. Unknown or absent qualities render no
 * frame rather than being silently coerced into a rarity.
 */
object PixelItemQualityFrameCatalog {
    const val STANDARD_ID = "UI_ITEM_QUALITY_FRAME_STANDARD"
    const val UNCOMMON_ID = "UI_ITEM_QUALITY_FRAME_UNCOMMON"

    private val palette = mapOf(
        'm' to PixelColors.Muted,
        'c' to PixelColors.Cyan,
        'g' to PixelColors.Gold,
    )

    private fun frame(assetId: String, uncommon: Boolean): PixelSprite {
        val pixels = MutableList(32) { CharArray(32) { PixelSprite.TRANSPARENT_PIXEL } }

        fun plot(x: Int, y: Int, key: Char) {
            if (x in 0 until 32 && y in 0 until 32) pixels[y][x] = key
        }

        fun lineH(x: Int, y: Int, length: Int, key: Char) {
            repeat(length) { plot(x + it, y, key) }
        }

        fun lineV(x: Int, y: Int, length: Int, key: Char) {
            repeat(length) { plot(x, y + it, key) }
        }

        val edge = if (uncommon) 'c' else 'm'
        val cornerLength = if (uncommon) 8 else 6

        lineH(1, 1, cornerLength, edge)
        lineV(1, 1, cornerLength, edge)
        lineH(31 - cornerLength, 1, cornerLength, edge)
        lineV(30, 1, cornerLength, edge)
        lineH(1, 30, cornerLength, edge)
        lineV(1, 31 - cornerLength, cornerLength, edge)
        lineH(31 - cornerLength, 30, cornerLength, edge)
        lineV(30, 31 - cornerLength, cornerLength, edge)

        if (uncommon) {
            // Extra ornament makes uncommon distinguishable by shape as well as color.
            plot(15, 1, 'g')
            plot(16, 1, 'g')
            plot(15, 30, 'g')
            plot(16, 30, 'g')
            plot(1, 15, 'g')
            plot(1, 16, 'g')
            plot(30, 15, 'g')
            plot(30, 16, 'g')
        }

        return PixelSprite(
            assetId = assetId,
            width = 32,
            height = 32,
            palette = palette,
            rows = pixels.map { it.concatToString() },
        )
    }

    val standardFrame: PixelSprite = frame(STANDARD_ID, uncommon = false)
    val uncommonFrame: PixelSprite = frame(UNCOMMON_ID, uncommon = true)

    fun forQuality(quality: String?): PixelSprite? = when (quality?.lowercase()) {
        "standard" -> standardFrame
        "uncommon" -> uncommonFrame
        else -> null
    }
}
