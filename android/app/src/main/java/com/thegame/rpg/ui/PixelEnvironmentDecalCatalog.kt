package com.thegame.rpg.ui

import androidx.compose.ui.graphics.Color

data class PixelSceneDecalPlacement(
    val sprite: PixelSprite,
    val x: Int,
    val y: Int,
)

/**
 * Reusable environment decals for current authored locations.
 *
 * Decals consume only player-facing location IDs. They never decide travel, access, quest,
 * interaction, or hazard state.
 */
object PixelEnvironmentDecalCatalog {
    const val EVACUATION_SIGNAGE_SET_ID = "EVACUATION_SIGNAGE_SET"
    const val DISTRICT_AMBIENT_DECAL_SET_ID = "DISTRICT_AMBIENT_DECAL_SET"

    private val palette = mapOf(
        'D' to Color(0xFF162129),
        'M' to Color(0xFF48535A),
        'L' to Color(0xFF65737A),
        'C' to PixelColors.Cyan,
        'G' to PixelColors.Gold,
        'P' to PixelColors.Paper,
        'R' to PixelColors.Danger,
    )

    private fun pixels(width: Int, height: Int): MutableList<CharArray> =
        MutableList(height) { CharArray(width) { PixelSprite.TRANSPARENT_PIXEL } }

    private fun evacuationSignage(): PixelSprite {
        val width = 24
        val height = 24
        val p = pixels(width, height)

        fun rect(x: Int, y: Int, w: Int, h: Int, key: Char) {
            for (yy in y until y + h) for (xx in x until x + w) {
                if (xx in 0 until width && yy in 0 until height) p[yy][xx] = key
            }
        }

        // Symbol-only emergency sign: framed route arrow plus hazard marker. No baked microtext.
        rect(2, 3, 20, 14, 'M')
        rect(4, 5, 16, 10, 'D')
        rect(6, 9, 9, 3, 'P')
        rect(12, 7, 3, 7, 'P')
        rect(15, 8, 3, 5, 'P')
        rect(18, 18, 4, 4, 'R')
        rect(3, 18, 10, 2, 'G')

        return PixelSprite(
            assetId = EVACUATION_SIGNAGE_SET_ID,
            width = width,
            height = height,
            palette = palette,
            rows = p.map { it.concatToString() },
        )
    }

    private fun ambientDecals(): PixelSprite {
        val width = 32
        val height = 32
        val p = pixels(width, height)

        fun rect(x: Int, y: Int, w: Int, h: Int, key: Char) {
            for (yy in y until y + h) for (xx in x until x + w) {
                if (xx in 0 until width && yy in 0 until height) p[yy][xx] = key
            }
        }

        // Caution stripe cluster, drain plate, utility marking and restrained wear.
        for (x in 2 until 18 step 4) {
            rect(x, 3, 2, 4, 'G')
            rect(x + 2, 3, 2, 4, 'D')
        }
        rect(21, 4, 8, 8, 'M')
        rect(22, 5, 6, 1, 'L')
        rect(22, 8, 6, 1, 'L')
        rect(22, 11, 6, 1, 'L')
        rect(5, 19, 12, 2, 'C')
        rect(4, 22, 6, 2, 'M')
        rect(13, 25, 8, 1, 'L')
        rect(23, 20, 5, 2, 'M')
        rect(25, 23, 3, 1, 'L')

        return PixelSprite(
            assetId = DISTRICT_AMBIENT_DECAL_SET_ID,
            width = width,
            height = height,
            palette = palette,
            rows = p.map { it.concatToString() },
        )
    }

    val evacuationSignage: PixelSprite = evacuationSignage()
    val districtAmbientDecals: PixelSprite = ambientDecals()

    val productionDecals: List<PixelSprite> = listOf(
        evacuationSignage,
        districtAmbientDecals,
    )

    fun placements(locationId: String): List<PixelSceneDecalPlacement> =
        when (locationId) {
            "PLATFORM_NINE" -> listOf(
                PixelSceneDecalPlacement(evacuationSignage, x = 8, y = 12),
                PixelSceneDecalPlacement(districtAmbientDecals, x = 48, y = 30),
            )

            "EVAC_STAIR" -> listOf(
                PixelSceneDecalPlacement(evacuationSignage, x = 88, y = 8),
            )

            "SERVICE_TUNNEL" -> listOf(
                PixelSceneDecalPlacement(districtAmbientDecals, x = 48, y = 30),
            )

            "DISTRICT_PLAZA" -> listOf(
                PixelSceneDecalPlacement(evacuationSignage, x = 10, y = 18),
                PixelSceneDecalPlacement(districtAmbientDecals, x = 66, y = 30),
            )

            else -> emptyList()
        }
}
