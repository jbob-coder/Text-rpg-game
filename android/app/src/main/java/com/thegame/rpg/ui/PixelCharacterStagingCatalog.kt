package com.thegame.rpg.ui

import androidx.compose.ui.graphics.Color

/**
 * Reusable character staging assets from the documented v1 asset plan.
 *
 * Staging assets never own character state. They only provide deterministic pixel geometry
 * around an already-projected character.
 */
object PixelCharacterStagingCatalog {
    const val MEDIUM_GROUND_SHADOW_ID = "CHARACTER_GROUND_SHADOW_MEDIUM"

    val mediumGroundShadow: PixelSprite = run {
        val width = 32
        val height = 16
        val pixels = MutableList(height) {
            CharArray(width) { PixelSprite.TRANSPARENT_PIXEL }
        }

        fun rect(x: Int, y: Int, w: Int, h: Int, key: Char) {
            for (yy in y until y + h) {
                for (xx in x until x + w) {
                    if (xx in 0 until width && yy in 0 until height) {
                        pixels[yy][xx] = key
                    }
                }
            }
        }

        // Bottom-anchored, deliberately hard-edged shadow. The sprite is drawn with its
        // 16-pixel staging canvas ending at the player's shared y=47 ground pivot.
        rect(11, 11, 10, 1, 'L')
        rect(8, 12, 16, 1, 'L')
        rect(6, 13, 20, 2, 'S')
        rect(9, 15, 14, 1, 'D')

        PixelSprite(
            assetId = MEDIUM_GROUND_SHADOW_ID,
            width = width,
            height = height,
            palette = mapOf(
                'L' to Color(0xFF182126),
                'S' to Color(0xFF11181D),
                'D' to Color(0xFF0A0E11),
            ),
            rows = pixels.map { it.concatToString() },
        )
    }
}
