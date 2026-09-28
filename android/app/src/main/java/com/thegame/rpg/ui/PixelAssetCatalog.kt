package com.thegame.rpg.ui

import androidx.compose.ui.graphics.Color

/**
 * Versioned native-pixel definitions for Wave A.
 *
 * These maps are the production source of truth. They intentionally stay text-based so
 * every pixel change is reviewable in Git, reproducible, and exportable to PNG later.
 */
data class PixelSprite(
    val assetId: String,
    val width: Int,
    val height: Int,
    val palette: Map<Char, Color>,
    val rows: List<String>,
) {
    init {
        require(width > 0 && height > 0) { "$assetId must have positive dimensions" }
        require(rows.size == height) {
            "$assetId expected $height rows, found ${rows.size}"
        }
        require(rows.all { it.length == width }) {
            "$assetId contains a row which is not $width pixels wide"
        }
        val used = rows.asSequence()
            .flatMap { it.asSequence() }
            .filter { it != TRANSPARENT_PIXEL }
            .toSet()
        val missing = used - palette.keys
        require(missing.isEmpty()) {
            "$assetId uses unmapped palette keys: $missing"
        }
    }

    companion object {
        const val TRANSPARENT_PIXEL: Char = '.'
    }
}

object PixelAssetCatalog {
    const val PLAYER_FRONT_BASE_ID = "PLAYER_GAMEPLAY_FRONT_BASE"
    const val PLAYER_HAIR_PLACEHOLDER_ID = "PLAYER_HAIR_TECH_PLACEHOLDER"
    const val DEPOT_JACKET_ICON_ID = "ITEM_DEPOT_JACKET_ICON"
    const val DEPOT_JACKET_LAYER_ID = "ITEM_DEPOT_JACKET_PAPERDOLL"

    val playerFrontBase = PixelSprite(
        assetId = PLAYER_FRONT_BASE_ID,
        width = 32,
        height = 48,
        palette = mapOf(
            'O' to PixelColors.Ink,
            'S' to Color(0xFFAD7D62),
            's' to Color(0xFF8B5F4B),
            'U' to Color(0xFF33434C),
            'u' to Color(0xFF263B44),
        ),
        rows = listOf(
        "................................",
        "................................",
        "................................",
        "............OOOOOOOO............",
        "...........OSSSSSSSSO...........",
        "..........OSSSSSSSSSSO..........",
        "..........SSSSSSSSSSSS..........",
        "..........SSSSSSSSSSSS..........",
        "..........SssSSSSSSssS..........",
        "..........OssSSSSSSssO..........",
        "...........OSsSSSSsSO...........",
        "..............SSSS..............",
        "..............SSSS..............",
        "..............ssss..............",
        "..............ssss..............",
        ".........OUUUUUUUUUUUUO.........",
        ".........OUUUUUUUUUUUUO.........",
        ".......OSSUUUUUUUUUUUUSSO.......",
        ".......OSSUUUUUUUUUUUUSSO.......",
        ".......OSSUUUUUUUUUUUUSSO.......",
        ".......OSSUUUUUUUUUUUUSSO.......",
        ".......OSSUUUUUUUUUUUUSSO.......",
        ".......OSSUUUUUUUUUUUUSSO.......",
        "......OSSSuuUUUUUUUUuuSSSO......",
        "......OSSuuuUUUUUUUUuuuSSO......",
        "......OSSuuuUUUUUUUUuuuSSO......",
        "......OSSuuuUUUUUUUUuuuSSO......",
        "......OSSuuuuuuuuuuuuuuSSO......",
        "......OSS..OuuuuuuuuO..SSO......",
        "......OSS..OuuuuuuuuO..SSO......",
        "......OSS..OuuuuuuuuO..SSO......",
        ".....OSSO.OUUUUOOOUUUUOOSSO.....",
        ".....OSSO.OUUUUO.OUUUUOOSSO.....",
        ".....OSSO.OUUUUO.OUUUUOOSSO.....",
        ".....OOOO.OUUUUO.OUUUUOOOOO.....",
        "..........OUUUUO.OUUUUO.........",
        "..........OUUUUO.OUUUUO.........",
        ".........OuuuuOO.OOuuuuO........",
        ".........OuuuuOO.OOuuuuO........",
        ".........OuuuuO...OuuuuO........",
        ".........OuuuuO...OuuuuO........",
        ".........OuuuuO...OuuuuO........",
        ".........OuuuuO...OuuuuO........",
        ".........OuuuuO...OuuuuO........",
        "........OuuuuuO...OuuuuuO.......",
        "........OuuuuuO...OuuuuuO.......",
        "........OOOOOOO...OOOOOOO.......",
        "................................"
        ),
    )

    /**
     * Temporary technical hair layer. This preserves the current visible-avatar quality
     * while the planned PLAYER_HAIR_LAYER_KIT_A asset is still awaiting its own reference
     * and blueprint pass. It is deliberately not a canonical player identity asset.
     */
    val playerHairTechnicalPlaceholder = PixelSprite(
        assetId = PLAYER_HAIR_PLACEHOLDER_ID,
        width = 32,
        height = 48,
        palette = mapOf(
            'H' to Color(0xFF20262B),
            'h' to Color(0xFF161C20),
        ),
        rows = listOf(
        "................................",
        "................................",
        "...........HHHHHHHHHH...........",
        ".........HhhhhHHHHHHHHH.........",
        ".........HhhhhHHHHHHhhh.........",
        "........HHhhhhHHHHHHhhhH........",
        "........HhhhHhhhhhhHhhhH........",
        "........HhhhhHHHHHHhHHHH........",
        ".........hhhH......HHHH.........",
        ".........HHHH......HHHH.........",
        ".........HHHH......HHHH.........",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................"
        ),
    )

    val depotJacketPaperdoll = PixelSprite(
        assetId = DEPOT_JACKET_LAYER_ID,
        width = 32,
        height = 48,
        palette = mapOf(
            'D' to Color(0xFF172128),
            'd' to Color(0xFF2A414A),
            'J' to Color(0xFF3B5963),
            'L' to Color(0xFF53656E),
            'C' to PixelColors.Cyan,
        ),
        rows = listOf(
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        ".............JJ..JJ.............",
        ".............JJCCJJ.............",
        "........DJJJJJJJJJJJJJJD........",
        "........DJJJJJJddJJJJJJD........",
        ".......DJJJJCCCddCCCJJJJD.......",
        ".......DJJJJJJCddCJJJJJJD.......",
        ".......DJJddJJJddJJJddJJD.......",
        ".......DJJddJJJddJJJddJJD.......",
        ".......DJJddLLddddLLddJJD.......",
        ".......DJJddddddddddddJJD.......",
        ".......DDDddddddddddddDDD.......",
        ".........dddddddddddddd.........",
        ".........dddJJJddJJJddd.........",
        ".........dddJJJddJJJddd.........",
        ".........dDJJJJJJJJJJDd.........",
        "..........DJJJJJJJJJJD..........",
        "..........DDDDDDDDDDDD..........",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................"
        ),
    )

    val depotJacketIcon = PixelSprite(
        assetId = DEPOT_JACKET_ICON_ID,
        width = 32,
        height = 32,
        palette = mapOf(
            'D' to Color(0xFF172128),
            'd' to Color(0xFF2A414A),
            'J' to Color(0xFF3B5963),
            'L' to Color(0xFF53656E),
            'C' to PixelColors.Cyan,
        ),
        rows = listOf(
        "................................",
        "................................",
        "................................",
        "................................",
        ".............DD..DD.............",
        ".............DD..DD.............",
        ".............DDCCDD.............",
        ".......DDDDDDDDDDDDDDDDDD.......",
        ".......DDJJJJJJJJJJJJJJDD.......",
        ".....DDDDJJJJJJddJJJJJJDDDD.....",
        ".....DJJJJJJJJJddJJJJJJJJJD.....",
        ".....DJJJJJJCCCddCCCJJJJJJD.....",
        ".....DJJJJJJJJJddJJJJJJJJJD.....",
        ".....DJJJJJJJJJddJJJJJJJJJD.....",
        ".....DJJJJJJJJJddJJJJJJJJJD.....",
        ".....DJJJJJJJJJddJJJJJJJJJD.....",
        ".....DJJJJJJJJJddJJJJJJJJJD.....",
        ".....DJJJdddLLddddLLdddJJJD.....",
        ".....DJJJddddddddddddddJJJD.....",
        ".....DDDDddddddddddddddDDDD.....",
        ".........dddddddddddddd.........",
        ".........dddJJJddJJJddd.........",
        ".........dddJJJddJJJddd.........",
        ".........dddJJJddJJJddd.........",
        ".........DJJJJJJJJJJJJD.........",
        ".........DJJJJJJJJJJJJD.........",
        ".........DDDDDDDDDDDDDD.........",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................"
        ),
    )

    val waveAProductionAssets: List<PixelSprite> = listOf(
        playerFrontBase,
        depotJacketIcon,
        depotJacketPaperdoll,
    )

    fun equipmentLayer(itemId: String?, slot: String): PixelSprite? =
        when {
            itemId == "ITEM_DEPOT_JACKET" && slot == "body" -> depotJacketPaperdoll
            else -> null
        }

    fun itemIcon(itemId: String): PixelSprite? =
        when (itemId) {
            "ITEM_DEPOT_JACKET" -> depotJacketIcon
            else -> null
        }
}
