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

data class PixelPaperDollOverlay(
    val itemId: String,
    val slot: String,
    val zOrder: Int,
    val sprite: PixelSprite,
) {
    init {
        require(sprite.width == 32 && sprite.height == 48) {
            "$itemId/$slot overlay must use the 32x48 player rig canvas"
        }
    }
}

object PixelAssetCatalog {
    const val PLAYER_FRONT_BASE_ID = "PLAYER_GAMEPLAY_FRONT_BASE"
    const val PLAYER_HAIR_PLACEHOLDER_ID = "PLAYER_HAIR_TECH_PLACEHOLDER"
    const val DEPOT_JACKET_ICON_ID = "ITEM_DEPOT_JACKET_ICON"
    const val DEPOT_JACKET_LAYER_ID = "ITEM_DEPOT_JACKET_PAPERDOLL"
    const val WORK_GLOVES_ICON_ID = "ITEM_WORK_GLOVES_ICON"
    const val WORK_GLOVES_LAYER_ID = "ITEM_WORK_GLOVES_PAPERDOLL"
    const val SIGNAL_RING_ICON_ID = "ITEM_SIGNAL_RING_ICON"
    const val SIGNAL_RING_LAYER_ID = "ITEM_SIGNAL_RING_PAPERDOLL"
    const val COURIER_NECKTAG_ICON_ID = "ITEM_COURIER_NECKTAG_ICON"
    const val COURIER_NECKTAG_LAYER_ID = "ITEM_COURIER_NECKTAG_PAPERDOLL"
    const val MAINTENANCE_SEAL_ICON_ID = "ITEM_MAINTENANCE_SEAL_ICON"
    const val DEAD_RELAY_ICON_ID = "ITEM_DEAD_RELAY_ICON"
    const val DEAD_RELAY_OPENED_ID = "ITEM_DEAD_RELAY_OPENED"
    const val DEAD_RELAY_DAMAGED_ID = "ITEM_DEAD_RELAY_DAMAGED"
    const val DEAD_RELAY_SIGNAL_LOST_ID = "ITEM_DEAD_RELAY_SIGNAL_LOST"

    val playerFrontBase = PixelSprite(
        assetId = PLAYER_FRONT_BASE_ID,
        width = 32,
        height = 48,
        palette = mapOf(
            'O' to PixelColors.Ink,
            'S' to Color(0xFFAD7D62),
            's' to Color(0xFF8B5F4B),
            'H' to Color(0xFFC79779),
            'U' to Color(0xFF566564),
            'u' to Color(0xFF343F3E),
            'L' to Color(0xFF7E8B84),
            'T' to Color(0xFF3B4543),
            't' to Color(0xFF27302F),
            'B' to Color(0xFF1F2625),
        ),
        rows = listOf(
        "................................",
        "................................",
        "................................",
        "................................",
        "............OOOOOOOO............",
        "..........OOOOOOOOOOOO..........",
        ".........OSSSSSSSSSSSSO.........",
        ".........OSHHSSSSSSSSSO.........",
        "........OSSSSSSSSSSSSSSO........",
        "........OSSSOSSSSSSOSSSO........",
        "........OSSSSSSSSSSSSSSO........",
        ".........OSSSSSssSSSSSO.........",
        "..........OSSSSOOSSSSO..........",
        "...........OssssssssO...........",
        "..............SSSS..............",
        ".............OssssO.............",
        ".........OOOOOOOOOOOOOO.........",
        "........OOUUUUUUUUUUUUOO........",
        "........OOULUUUuuUUULUOO........",
        "......OOOUUUUUUuuUUUUUUOOO......",
        "......OSOUUUUUUuuUUUUUUOSO......",
        "......OSOUUUUUUuuUUUUUUOSO......",
        "......OSOUUUUUUuuUUUUUUOSO......",
        "......OSOUUUUUUuuUUUUUUOSO......",
        ".....OOSOOUUUUUuuUUUUUOOSOO.....",
        ".....OSSOOUUUUUuuUUUUUOOSSO.....",
        ".....OSSOOUUUUUuuUUUUUOOSSO.....",
        ".....OSSOOUUUUUuuUUUUUOOSSO.....",
        ".....OSSOOUUUUUUUUUUUUOOSSO.....",
        ".....OSOOOUUUUUUUUUUUUOOOSO.....",
        ".....OS..OOuuuuuuuuuuOO..SO.....",
        ".....OSS.OOuuuuuuuuuuOO.SSO.....",
        ".....OSS.OOTTTTTTTTTTOO.SSO.....",
        ".....OSS..OTTTTTTTTTTO..SSO.....",
        ".....OOO..OOOOOOOOOOOO..OOO.....",
        ".........OTTTTO..OTTTTO.........",
        ".........OTTTTO..OTTTTO.........",
        ".........OTTTTO..OTTTTO.........",
        ".........OTTTTO..OTTTTO.........",
        ".........OTTTTO..OTTTTO.........",
        ".........OTtttO..OtttTO.........",
        ".........OTtttO..OtttTO.........",
        ".........OTtttO..OtttTO.........",
        ".........OTtttO..OtttTO.........",
        ".........OTtttO..OtttTO.........",
        "........OBBBBBO..OBBBBBO........",
        "........OOOOOOO..OOOOOOO........",
        "................................"
        ),
    )

    /*/**
     * Temporary technical hair layer. This preserves the current visible-avatar quality
     * while the planned PLAYER_HAIR_LAYER_KIT_A asset is still awaiting its own reference
     * and blueprint pass. It is deliberately not a canonical player identity asset.
     */
    val playerHairTechnicalPlaceholder = PixelSprite(
        assetId = PLAYER_HAIR_PLACEHOLDER_ID,
        width = 32,
        height = 48,
        palette = mapOf(
            'H' to Color(0xFF2C302E),
            'h' to Color(0xFF191C1B),
            'A' to Color(0xFF4A4F4A),
        ),
        rows = listOf(
        "................................",
        "................................",
        "............AAAAAAAA............",
        "..........HHHHHHHHHHHH..........",
        ".........HHHHHHHHHHHHHH.........",
        ".........hhhhhHHHHHHHhh.........",
        ".........hhhHHHHHHHHHHh.........",
        ".........hhhHHH.HHHHHH..........",
        ".........hHHhhH..HHhhh..........",
        ".........hhh........hh..........",
        "..........hh........hh..........",
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
            'D' to Color(0xFF182024),
            'd' to Color(0xFF2B3536),
            'J' to Color(0xFF4E5C59),
            'L' to Color(0xFF6B7770),
            'B' to Color(0xFFB18B55),
            'C' to Color(0xFF6D9A93),
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
        "................................",
        ".............LL..LL.............",
        ".............LLddLL.............",
        ".........DDDDDDDDDDDDDD.........",
        "........DDJJJJJJJJJJJJDD........",
        "........DDJJJJJddJJJJJDD........",
        "......DDDJJJJJJddJJCBJJDDD......",
        "......DJJJJJJJJddJJBBJJJJD......",
        "......DJJJLJJJJddJJJJdJJJD......",
        "......DJJJLJJJJddJJJJdJJJD......",
        "......DJJDLJJJJddJJJJdDJJD......",
        "......DJJDLdLLdddJLLddDJJD......",
        "......DJJDLddddddJddddDJJD......",
        "......DJJDLddddddJddddDJJD......",
        "......DJJDLJJJJddJJJJdDJJD......",
        "......DJJDJJJJJddJJJJJDJJD......",
        "......DDDDDJJJJJJJJJJDDDDD......",
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


    val workGlovesIcon = PixelSprite(
        assetId = WORK_GLOVES_ICON_ID,
        width = 32,
        height = 32,
        palette = mapOf(
            'O' to PixelColors.Ink,
            'G' to Color(0xFF45545C),
            'g' to Color(0xFF2B373D),
            'L' to Color(0xFF8DA0A9),
        ),
        rows = listOf(
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        ".........GGG........GGG.........",
        "......GGGGGG........GGGGGG......",
        "......GGGGGG........GGGGGG......",
        ".....GGGGGGGG......GGGGGGGG.....",
        ".....GGGGGGGG......GGGGGGGG.....",
        ".....GGGGGGGG......GGGGGGGG.....",
        "....gggGGGGGG......GGGGGGggg....",
        "....gggGGGGGG......GGGGGGggg....",
        "....gggGGGGGG......GGGGGGggg....",
        "....gggGGGGGG......GGGGGGggg....",
        "....gggGGGGGG......GGGGGGggg....",
        "....gggGGGGGG......GGGGGGggg....",
        "....gggGGGGGG......GGGGGGggg....",
        ".....GGGGGGGG......GGGGGGGG.....",
        ".....GLLLLLLL......LLLLLLLG.....",
        ".....OLLLLLLLO....OLLLLLLLO.....",
        ".....OOOOOOOOO....OOOOOOOOO.....",
        ".....OOOOOOOOO....OOOOOOOOO.....",
        ".....OOOOOOOOO....OOOOOOOOO.....",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................"
        ),
    )

    val workGlovesPaperdoll = PixelSprite(
        assetId = WORK_GLOVES_LAYER_ID,
        width = 32,
        height = 48,
        palette = mapOf(
            'O' to PixelColors.Ink,
            'G' to Color(0xFF46504E),
            'g' to Color(0xFF28302F),
            'L' to Color(0xFF8E978F),
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
        ".....OGGG..............GGGO.....",
        ".....OGGG..............GGGO.....",
        ".....OGGG..............GGGO.....",
        ".....OGGG..............GGGO.....",
        ".....OgLL..............LLgO.....",
        ".....Oggg..............gggO.....",
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

    val signalRingIcon = PixelSprite(
        assetId = SIGNAL_RING_ICON_ID,
        width = 32,
        height = 32,
        palette = mapOf(
            'R' to Color(0xFFE2B65F),
            'G' to Color(0xFF8A734A),
            'C' to PixelColors.Cyan,
            'c' to Color(0xFFB6FFFF),
        ),
        rows = listOf(
        "................................",
        "................................",
        "................................",
        "................................",
        "..............cccc..............",
        ".............CccccC.............",
        ".............CCCCCC.............",
        "............RCCCCCCR............",
        "...........RRCGGGGCRR...........",
        ".........RRRRCGGGGCRRRR.........",
        ".........RR...GGGG...RR.........",
        "........RR............RR........",
        ".......RRR............RRR.......",
        ".......RR..............RR.......",
        ".......RR..............RR.......",
        ".......RR..............RR.......",
        ".......RR..............RR.......",
        ".......RR..............RR.......",
        ".......RR..............RR.......",
        ".......RRR............RRR.......",
        "........RR............RR........",
        ".........RR..........RR.........",
        ".........RRRR......RRRR.........",
        "...........RRRRRRRRRR...........",
        "............RRRRRRRR............",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................"
        ),
    )

    val signalRingPaperdoll = PixelSprite(
        assetId = SIGNAL_RING_LAYER_ID,
        width = 32,
        height = 48,
        palette = mapOf(
            'G' to PixelColors.Gold,
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
        ".....GG.........................",
        ".....GC.........................",
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

    val courierNeckTagIcon = PixelSprite(
        assetId = COURIER_NECKTAG_ICON_ID,
        width = 32,
        height = 32,
        palette = mapOf(
            'O' to PixelColors.Ink,
            'S' to Color(0xFF8A734A),
            'T' to Color(0xFFB08C55),
            'G' to PixelColors.Gold,
            'L' to Color(0xFFC9B57F),
        ),
        rows = listOf(
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "........S..............S........",
        ".........S............S.........",
        "..........S..........S..........",
        "...........S........S...........",
        "............S......S............",
        ".............S....S.............",
        "..............S..S..............",
        "...............SS...............",
        ".............SSSSSS.............",
        ".............SSSSSS.............",
        "...........OOOOOOOOOO...........",
        "...........OTTTTTTTTO...........",
        "...........OTLTTTTLTO...........",
        "...........OTTGGGGTTO...........",
        "...........OTTGGGGTTO...........",
        "...........OTTGGGGTTO...........",
        "...........OTTGGGGTTO...........",
        "...........OTTTTTTTTO...........",
        "...........OTLTTTTLTO...........",
        "...........OTTTTTTTTO...........",
        "...........OOOOOOOOOO...........",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................"
        ),
    )

    val courierNeckTagPaperdoll = PixelSprite(
        assetId = COURIER_NECKTAG_LAYER_ID,
        width = 32,
        height = 48,
        palette = mapOf(
            'S' to Color(0xFF7E6A4C),
            'T' to Color(0xFFAB8F5E),
            'B' to Color(0xFFD3B470),
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
        "................................",
        "................................",
        "................................",
        "..............S..S..............",
        "..............S..S..............",
        "...............SS...............",
        "...............SS...............",
        "...............TT...............",
        "...............TB...............",
        "...............TT...............",
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

    val maintenanceSealIcon = PixelSprite(
        assetId = MAINTENANCE_SEAL_ICON_ID,
        width = 32,
        height = 32,
        palette = mapOf(
            'M' to Color(0xFF8C7650),
            'm' to Color(0xFFB99A63),
            'K' to Color(0xFF53656E),
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
        ".............MMMMMM.............",
        "...........MMMMMMMMMM...........",
        "..........MMMmmmmmmMMM..........",
        ".........MMMmmmmmmmmMMM.........",
        "........MMMmmmKKKKmmmMMM........",
        "........MMmmm.KKKK.mmmMM........",
        ".......MMmmm..KKKK..mmmMM.......",
        ".......MMmmKKKCCCCKKKmmMM.......",
        ".......MMmmKKKCCCCKKKmmMM.......",
        ".......MMmmKKKCCCCKKKmmMM.......",
        ".......MMmmKKKCCCCKKKmmMM.......",
        ".......MMmmm..KKKK..mmmMM.......",
        "........MMmmm.KKKK.mmmMM........",
        "........MMMmmmKKKKmmmMMM........",
        ".........MMMmmmmmmmmMMM.........",
        "..........MMMmmmmmmMMM..........",
        "...........MMMMMMMMMM...........",
        ".............MMMMMM.............",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................"
        ),
    )

    val deadRelayIcon = PixelSprite(
        assetId = DEAD_RELAY_ICON_ID,
        width = 32,
        height = 32,
        palette = mapOf(
            'O' to PixelColors.Ink,
            'D' to Color(0xFF36454C),
            'd' to Color(0xFF53656E),
            'C' to PixelColors.Cyan,
            'c' to Color(0xFFB6FFFF),
            'L' to Color(0xFF9FB0B9),
        ),
        rows = listOf(
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "........OOOOOOOOOOOOOOOO........",
        "........ODDDDDDDDDDDDDDO........",
        "........ODDDDDDDDDDDDDDO........",
        "........ODDddddddddddDDO........",
        "........ODDdCCCCCCCCdDDO........",
        "......OOODDdCCCCCCCCdDDOOO......",
        "......OOODDdCCCCCCCCdDDOOO......",
        "......OOODDdCCCCCCCCdDDOOO......",
        "......OOODDddddddddddDDOOO......",
        "......OOODDDDDDDDDDDDDDOOO......",
        "......OOODDDDDDDDDDDDDDOOO......",
        "......OOODDddddddddddDDOOO......",
        "......OOODDddddddddddDDOOO......",
        "......OOODDddccccccddDDOOO......",
        "......OOODDddccccccddDDOOO......",
        "......OOODDddccccccddDDOOO......",
        "......OOODDddccccccddDDOOO......",
        "......OOODDddddddddddDDOOO......",
        "........ODDddddddddddDDO........",
        "........ODDDDDDDDDDDDDDO........",
        "........ODDDLLLDDLLLDDDO........",
        "........ODDDLLLDDLLLDDDO........",
        "........OOOOLLLOOLLLOOOO........",
        "................................",
        "................................",
        "................................",
        "................................"
        ),
    )


    val deadRelayOpened = PixelSprite(
        assetId = DEAD_RELAY_OPENED_ID,
        width = 32,
        height = 32,
        palette = mapOf(
            'O' to PixelColors.Ink,
            'D' to Color(0xFF36454C),
            'd' to Color(0xFF53656E),
            'I' to Color(0xFF26363E),
            'C' to PixelColors.Cyan,
            'c' to Color(0xFF72AEB3),
            'L' to Color(0xFFB6FFFF),
            'H' to Color(0xFF8C7650),
        ),
        rows = listOf(
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        ".......HHH............HHH.......",
        ".......HHH.dddddddddd.HHH.......",
        ".....OOHHH.dIIIIIIIId.HHHOO.....",
        ".....ODDDDDdICCCCCCIdDDDDDO.....",
        ".....ODDDDDdICCCCCCIdDDDDDO.....",
        ".....ODDDDDdICCCCCCIdDDDDDO.....",
        ".....ODDDDDdICCCCCCIdDDDDDO.....",
        ".....ODDDDDdIIIIIIIIdDDDDDO.....",
        ".....ODDDDDdIIILLccIdDDDDDO.....",
        ".....ODDDDDdIccIIccIdDDDDDO.....",
        ".....ODDDDDdIccIIccIdDDDDDO.....",
        ".....ODDDDDdIccIIccIdDDDDDO.....",
        ".....ODDDDDdIccLLccIdDDDDDO.....",
        ".....ODDDDDdIccIIccIdDDDDDO.....",
        ".....ODDDDDdIccIIccIdDDDDDO.....",
        ".....ODDDDDdIccIIccIdDDDDDO.....",
        ".....ODDDDDdIccLLccIdDDDDDO.....",
        ".....ODDDDDdIIIIIccIdDDDDDO.....",
        ".....ODDDDDdIIIIIIIIdDDDDDO.....",
        ".....OOOOO.dIIIIIIIId.OOOOO.....",
        "...........dddddddddd...........",
        "................................",
        "................................",
        "................................",
        "................................",
        "................................"
        ),
    )

    val deadRelayDamaged = PixelSprite(
        assetId = DEAD_RELAY_DAMAGED_ID,
        width = 32,
        height = 32,
        palette = mapOf(
            'O' to PixelColors.Ink,
            'D' to Color(0xFF36454C),
            'd' to Color(0xFF53656E),
            'C' to PixelColors.Cyan,
            'c' to Color(0xFF72AEB3),
            'X' to PixelColors.Danger,
        ),
        rows = listOf(
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "........OOOOOOOOOOOOOOOO........",
        "........ODDDDDDDDDDDDDDO........",
        "........ODXDDDDDDDDDDXDO........",
        "........OXDddddddddddDXO........",
        "........XDDdCCCCCCCCdDDO........",
        "........ODDdCCCCCCCCdDDX........",
        "........ODDdCCCCCCCCdDDO........",
        "........ODDdCCCCCCCCdDDO........",
        "........ODDddddddddddDDO........",
        "........ODXDDDDDDDDDXDDO........",
        ".......XODDXDDDDDDDXDDDO........",
        "........XDDddddddddddDDO........",
        "........ODDddddddddddDDOX.......",
        "........ODDddccccccddDDX........",
        "........ODDddccccccddDDO........",
        "........ODDddccccccddDDO........",
        "........ODDddccccccddDDO........",
        "........ODDddddddddddDDO........",
        "........ODDddddXdddddDDO........",
        "........ODDDDDXDDDDDDDXO........",
        "........OXDDDDDDDDDDDXDO........",
        "........ODXDDDDDDDDDDDDO........",
        "........OOOOOOOOOOOOOOOO........",
        "................................",
        "................................",
        "................................",
        "................................"
        ),
    )

    val deadRelaySignalLost = PixelSprite(
        assetId = DEAD_RELAY_SIGNAL_LOST_ID,
        width = 32,
        height = 32,
        palette = mapOf(
            'O' to PixelColors.Ink,
            'D' to Color(0xFF2B3439),
            'd' to Color(0xFF48535A),
            'K' to Color(0xFF111A20),
            'X' to PixelColors.Danger,
        ),
        rows = listOf(
        "................................",
        "................................",
        "................................",
        "................................",
        "................................",
        "........OOOOOOOOOOOOOOOO........",
        "........ODDDDDDDDDDDDDDO........",
        "........ODXDDDDDDDDDDXDO........",
        "........OXDddddddddddDXO........",
        "........XDDdKKKKKKKKdDDO........",
        "........ODDdKKKKKKKKdDDX........",
        "........ODDdKKKKKKKKdDDO........",
        "........ODDdKKKKKKKKdDDO........",
        "........ODDddddddddddDDO........",
        "........ODXDDDDDDDDDXDDO........",
        ".......XODDXDDDDDDDXDDDO........",
        "........XDDddddddddddDDO........",
        "........ODDddddddddddDDOX.......",
        "........ODDddKKKKKKddDDX........",
        "........ODDddKKKKKKddDDO........",
        "........ODDddKKKKKKddDDO........",
        "........ODDddKKKKKKddDDO........",
        "........ODDddddddddddDDO........",
        "........ODDddddXdddddDDO........",
        "........ODDDDDXDDDDDDDXO........",
        "........OXDDDDDDDDDDDXDO........",
        "........ODXDDDDDDDDDDDDO........",
        "........OOOOOOOOOOOOOOOO........",
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

    val batch001ProductionAssets: List<PixelSprite> = waveAProductionAssets + listOf(
        workGlovesIcon,
        workGlovesPaperdoll,
        signalRingIcon,
        signalRingPaperdoll,
        courierNeckTagIcon,
        courierNeckTagPaperdoll,
        maintenanceSealIcon,
        deadRelayIcon,
        deadRelayOpened,
        deadRelayDamaged,
        deadRelaySignalLost,
    )

    /**
     * Exact paper-doll overlays for the front-facing 32x48 player rig.
     *
     * Every layer shares the body's coordinate space and ground pivot. The UI must render
     * only entries from this registry; equipped items without a registered overlay remain
     * logically equipped but do not receive invented placeholder geometry.
     */
    val equipmentOverlays: List<PixelPaperDollOverlay> = listOf(
        PixelPaperDollOverlay(
            itemId = "ITEM_COURIER_NECKTAG",
            slot = "neck",
            zOrder = 10,
            sprite = courierNeckTagPaperdoll,
        ),
        PixelPaperDollOverlay(
            itemId = "ITEM_DEPOT_JACKET",
            slot = "body",
            zOrder = 20,
            sprite = depotJacketPaperdoll,
        ),
        PixelPaperDollOverlay(
            itemId = "ITEM_WORK_GLOVES",
            slot = "hands",
            zOrder = 30,
            sprite = workGlovesPaperdoll,
        ),
        PixelPaperDollOverlay(
            itemId = "ITEM_SIGNAL_RING",
            slot = "ring_1",
            zOrder = 40,
            sprite = signalRingPaperdoll,
        ),
    )

    fun equipmentOverlay(itemId: String?, slot: String): PixelPaperDollOverlay? =
        equipmentOverlays.firstOrNull { overlay ->
            overlay.itemId == itemId && overlay.slot == slot
        }

    fun equipmentLayer(itemId: String?, slot: String): PixelSprite? =
        equipmentOverlay(itemId, slot)?.sprite

    fun relayStateSprite(relayState: String?): PixelSprite? =
        when (relayState) {
            "intact" -> deadRelayIcon
            "opened" -> deadRelayOpened
            "damaged" -> deadRelayDamaged
            "signal_lost" -> deadRelaySignalLost
            else -> null
        }

    fun itemIcon(itemId: String): PixelSprite? =
        when (itemId) {
            "ITEM_DEPOT_JACKET" -> depotJacketIcon
            "ITEM_WORK_GLOVES" -> workGlovesIcon
            "ITEM_SIGNAL_RING" -> signalRingIcon
            "ITEM_COURIER_NECKTAG" -> courierNeckTagIcon
            "ITEM_MAINTENANCE_SEAL" -> maintenanceSealIcon
            "ITEM_DEAD_RELAY" -> deadRelayIcon
            else -> null
        }
}
