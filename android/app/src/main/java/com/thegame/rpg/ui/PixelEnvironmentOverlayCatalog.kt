package com.thegame.rpg.ui

import androidx.compose.ui.graphics.Color

/**
 * Reusable environment-state overlays.
 *
 * These assets are presentation-only building blocks. They contain no gameplay state and are
 * selected by higher-level scene/state catalogs which already receive player-safe projection data.
 */
object PixelEnvironmentOverlayCatalog {
    const val EMERGENCY_LIGHT_OVERLAY_ID = "EMERGENCY_LIGHT_OVERLAY"
    const val BLACKOUT_SHADOW_OVERLAY_ID = "BLACKOUT_SHADOW_OVERLAY"

    private fun emptyPixels(): MutableList<CharArray> =
        MutableList(64) { CharArray(128) { PixelSprite.TRANSPARENT_PIXEL } }

    private fun emergencyLightOverlay(): PixelSprite {
        val pixels = emptyPixels()

        fun plot(x: Int, y: Int, key: Char) {
            if (x in 0 until 128 && y in 0 until 64) pixels[y][x] = key
        }

        fun rect(x: Int, y: Int, width: Int, height: Int, key: Char) {
            for (yy in y until y + height) {
                for (xx in x until x + width) plot(xx, yy, key)
            }
        }

        // Reusable emergency-route strips. Kept sparse so architecture remains readable.
        for (x in 8..116 step 18) {
            rect(x, 50, 8, 2, 'R')
            rect(x + 2, 52, 4, 1, 'G')
        }

        // Small backup-power indicators can sit on scene landmarks without baking text.
        for (x in 16..112 step 24) {
            rect(x, 18 + (x / 24 % 2) * 4, 3, 2, 'G')
        }

        return PixelSprite(
            assetId = EMERGENCY_LIGHT_OVERLAY_ID,
            width = 128,
            height = 64,
            palette = mapOf(
                'R' to PixelColors.Danger,
                'G' to PixelColors.Gold,
            ),
            rows = pixels.map { it.concatToString() },
        )
    }

    private fun blackoutShadowOverlay(): PixelSprite {
        val pixels = emptyPixels()

        fun rect(x: Int, y: Int, width: Int, height: Int, key: Char) {
            for (yy in y until y + height) {
                for (xx in x until x + width) {
                    if (xx in 0 until 128 && yy in 0 until 64) pixels[yy][xx] = key
                }
            }
        }

        // Clustered shadow regions preserve interactable silhouettes instead of applying a flat
        // fullscreen black tint.
        rect(0, 0, 128, 10, 'D')
        rect(4, 10, 36, 16, 'd')
        rect(52, 8, 68, 18, 'd')
        rect(0, 26, 18, 12, 'd')
        rect(104, 26, 24, 12, 'd')

        return PixelSprite(
            assetId = BLACKOUT_SHADOW_OVERLAY_ID,
            width = 128,
            height = 64,
            palette = mapOf(
                'D' to Color(0xCC10151A),
                'd' to Color(0x99172128),
            ),
            rows = pixels.map { it.concatToString() },
        )
    }

    val emergencyLights: PixelSprite = emergencyLightOverlay()
    val blackoutShadows: PixelSprite = blackoutShadowOverlay()

    val productionOverlays: List<PixelSprite> = listOf(
        emergencyLights,
        blackoutShadows,
    )

    /**
     * Compose same-sized transparent pixel layers in order; later non-transparent pixels win.
     */
    fun compose(assetId: String, vararg layers: PixelSprite): PixelSprite {
        require(layers.isNotEmpty()) { "At least one layer is required" }
        val width = layers.first().width
        val height = layers.first().height
        require(layers.all { it.width == width && it.height == height }) {
            "Environment overlay layers must share dimensions"
        }

        val pixels = MutableList(height) { CharArray(width) { PixelSprite.TRANSPARENT_PIXEL } }
        val palette = linkedMapOf<Char, Color>()

        layers.forEach { layer ->
            palette.putAll(layer.palette)
            layer.rows.forEachIndexed { y, row ->
                row.forEachIndexed { x, key ->
                    if (key != PixelSprite.TRANSPARENT_PIXEL) pixels[y][x] = key
                }
            }
        }

        return PixelSprite(
            assetId = assetId,
            width = width,
            height = height,
            palette = palette,
            rows = pixels.map { it.concatToString() },
        )
    }
}
