package com.thegame.rpg.ui

/**
 * Source-native semantic equipment-slot icons.
 *
 * Slot identity is presentation-only. Equipment ownership, compatibility and equipped state
 * remain authoritative in the Python engine and its player-safe Android projection.
 */
object PixelEquipmentSlotCatalog {
    const val HEAD_ID = "UI_EQUIPMENT_SLOT_HEAD"
    const val BODY_ID = "UI_EQUIPMENT_SLOT_CHEST"
    const val HANDS_ID = "UI_EQUIPMENT_SLOT_HANDS"
    const val LEGS_ID = "UI_EQUIPMENT_SLOT_LEGS"
    const val FEET_ID = "UI_EQUIPMENT_SLOT_FEET"
    const val MAIN_HAND_ID = "UI_EQUIPMENT_SLOT_MAIN_HAND"
    const val OFF_HAND_ID = "UI_EQUIPMENT_SLOT_OFF_HAND"
    const val RING_1_ID = "UI_EQUIPMENT_SLOT_RING_1"
    const val RING_2_ID = "UI_EQUIPMENT_SLOT_RING_2"
    const val NECK_ID = "UI_EQUIPMENT_SLOT_NECK"
    const val ACCESSORY_1_ID = "UI_EQUIPMENT_SLOT_ACCESSORY_1"
    const val ACCESSORY_2_ID = "UI_EQUIPMENT_SLOT_ACCESSORY_2"

    private val palette = mapOf(
        'P' to PixelColors.Paper,
        'C' to PixelColors.Cyan,
        'G' to PixelColors.Gold,
    )

    val head = PixelSprite(
        assetId = HEAD_ID,
        width = 24,
        height = 24,
        palette = palette,
        rows = listOf(
        "........................",
        "........................",
        "........................",
        "........................",
        ".......PPPPPPPPPP.......",
        ".......PPPPPPPPPP.......",
        ".......PPPPPPPPPP.......",
        "......PP........PP......",
        "......P..........P......",
        ".....PP..........PP.....",
        ".....PPP........PPP.....",
        ".....PPP........PPP.....",
        "......PP........PP......",
        "......PP........PP......",
        "......PPP......PPP......",
        "......PPPPP..PPPPP......",
        ".........PPPPPP.........",
        ".........PPPPPP.........",
        ".........PPPPPP.........",
        "........................",
        "........................",
        "........................",
        "........................",
        "........................"
        ),
    )

    val body = PixelSprite(
        assetId = BODY_ID,
        width = 24,
        height = 24,
        palette = palette,
        rows = listOf(
        "........................",
        "........................",
        "........................",
        "........................",
        "........PPPPPPPP........",
        ".......PPPPPPPPPP.......",
        "......P.PPPPPPPP.P......",
        "......PPPPPPPPPPPP......",
        ".....PPPPPPPPPPPPPP.....",
        "....P.PPPP....PPPP.P....",
        "......PPPP....PPPP......",
        "......PPPP....PPPP......",
        "......PPPP....PPPP......",
        "......PPPP....PPPP......",
        "......PPPP....PPPP......",
        "......PPPP....PPPP......",
        "......PPPPPPPPPPPP......",
        "......PPPPPPPPPPPP......",
        "......PPPPPPPPPPPP......",
        ".........PPPPPP.........",
        ".........PPPPPP.........",
        "........................",
        "........................",
        "........................"
        ),
    )

    val hands = PixelSprite(
        assetId = HANDS_ID,
        width = 24,
        height = 24,
        palette = palette,
        rows = listOf(
        "........................",
        "........................",
        "........................",
        "........................",
        ".......PP......PP.......",
        "....PP.PP......PP.PP....",
        "....PP.PP......PP.PP....",
        "....PP.PP......PP.PP....",
        "...PPPPPPP....PPPPPPP...",
        "...PPPPPPP....PPPPPPP...",
        "...PPPPPPP....PPPPPPP...",
        "...PPPPPPP....PPPPPPP...",
        "...PPPPPPP....PPPPPPP...",
        "...PPPPPPP....PPPPPPP...",
        "...PPPPPPP....PPPPPPP...",
        "...PPPPPPP....PPPPPPP...",
        "...PPPPPPP....PPPPPPP...",
        "...PPPPPPP....PPPPPPP...",
        "...PPPPPPP....PPPPPPP...",
        "...PPPPPPP....PPPPPPP...",
        "........................",
        "........................",
        "........................",
        "........................"
        ),
    )

    val legs = PixelSprite(
        assetId = LEGS_ID,
        width = 24,
        height = 24,
        palette = palette,
        rows = listOf(
        "........................",
        "........................",
        "........................",
        "........................",
        "......PPPPPPPPPPPP......",
        "......PPPPPPPPPPPP......",
        "......PPPPPPPPPPPP......",
        "......PPPPPPPPPPPP......",
        "......PPPPPPPPPPPP......",
        "......PPPP....PPPP......",
        "......PPPP....PPPP......",
        "......PPPP....PPPP......",
        "......PPPP....PPPP......",
        "......PPPPP..PPPPP......",
        "......PPPPP..PPPPP......",
        "......PPPPP..PPPPP......",
        "......PPPPP..PPPPP......",
        "......PPPPP..PPPPP......",
        "......PPPPP..PPPPP......",
        "......PPPPP..PPPPP......",
        "........................",
        "........................",
        "........................",
        "........................"
        ),
    )

    val feet = PixelSprite(
        assetId = FEET_ID,
        width = 24,
        height = 24,
        palette = palette,
        rows = listOf(
        "........................",
        "........................",
        "........................",
        "........................",
        "........................",
        "........................",
        "........................",
        "........................",
        "........................",
        "...PPPPPPP....PPPPPPP...",
        "...PPPPPPP....PPPPPPP...",
        "...PPPPPPP....PPPPPPP...",
        "...PPPPPPP....PPPPPPP...",
        "...PPPPPPP....PPPPPPP...",
        "...PPPPPPP....PPPPPPP...",
        "..PPPPPPPPP..PPPPPPPPP..",
        "..PPPPPPPPP..PPPPPPPPP..",
        "..PPPPPPPPP..PPPPPPPPP..",
        "..PPPPPPPPP..PPPPPPPPP..",
        "...PPPPPPPP..PPPPPPPPP..",
        "...PPPPPPPP..PPPPPPPPP..",
        "........................",
        "........................",
        "........................"
        ),
    )

    val mainHand = PixelSprite(
        assetId = MAIN_HAND_ID,
        width = 24,
        height = 24,
        palette = palette,
        rows = listOf(
        "........................",
        "........................",
        "........................",
        "........................",
        "................PPPP....",
        "................PPPP....",
        "................PPPP....",
        "................PPPP....",
        "...............P.P......",
        "..............P.P.......",
        ".............P.P........",
        "............P.P.........",
        "...........P.P..........",
        "..........P.P...........",
        ".........P.P............",
        "....P...P.P.............",
        "...P.P.P.P..............",
        "....P.P.P...............",
        ".....P.P................",
        "...PPPPPP...............",
        "...PPPPP.P..............",
        "........P...............",
        "........................",
        "........................"
        ),
    )

    val offHand = PixelSprite(
        assetId = OFF_HAND_ID,
        width = 24,
        height = 24,
        palette = palette,
        rows = listOf(
        "........................",
        "........................",
        "........................",
        "...........PPP..........",
        ".........PP...PP........",
        ".......PP.......PP......",
        ".....PP...........PP....",
        ".....P.............P....",
        ".....P....PPPP.....P....",
        ".....P....PPPP.....P....",
        ".....P....PPPP.....P....",
        "......P...PPPP....P.....",
        "......P...PPPP....P.....",
        "......P...PPPP....P.....",
        "......P...PPPP....P.....",
        "......P...PPPP....P.....",
        ".......P.........P......",
        "........P.......P.......",
        ".........P.....P........",
        "..........P...P.........",
        "...........P.P..........",
        "............P...........",
        "........................",
        "........................"
        ),
    )

    val ring1 = PixelSprite(
        assetId = RING_1_ID,
        width = 24,
        height = 24,
        palette = palette,
        rows = listOf(
        "........................",
        "........................",
        "........................",
        "..........CCCC..........",
        ".........PCCCCP.........",
        ".........PPPPPP.........",
        ".........PPPPPP.........",
        ".......PPPPPPPPPP.......",
        ".......PP......PP.......",
        "......PP........PP......",
        "......P..........P......",
        ".....PP..........PP.....",
        ".....PP..........PP.....",
        ".....PP..........PP.....",
        "......P..........P......",
        "......PP........PP......",
        ".......PP......PP.......",
        ".......PPPP..PPPP.......",
        ".........PPPPPP.........",
        "........................",
        "........................",
        "........................",
        "........................",
        "........................"
        ),
    )

    val ring2 = PixelSprite(
        assetId = RING_2_ID,
        width = 24,
        height = 24,
        palette = palette,
        rows = listOf(
        "........................",
        "........................",
        "..........GGGG..........",
        "..........GCCG..........",
        "........PPGGGGPP........",
        "........PPGGGGPP........",
        "........PPPPPPPP........",
        ".......PPPP..PPPP.......",
        ".......PP......PP.......",
        "......PP........PP......",
        "......P..........P......",
        ".....PP..........PP.....",
        ".....PP..........PP.....",
        ".....PP..........PP.....",
        "......P..........P......",
        "......PP........PP......",
        ".......PP......PP.......",
        ".......PPPP..PPPP.......",
        ".........PPPPPP.........",
        "........................",
        "........................",
        "........................",
        "........................",
        "........................"
        ),
    )

    val neck = PixelSprite(
        assetId = NECK_ID,
        width = 24,
        height = 24,
        palette = palette,
        rows = listOf(
        "........................",
        "........................",
        "........................",
        "........................",
        ".....P............P.....",
        "......P..........P......",
        ".......P........P.......",
        ".......P........P.......",
        "........P......P........",
        ".........P....P.........",
        "..........P..P..........",
        "..........P..P..........",
        "...........PP...........",
        ".........PPPPPP.........",
        ".........P....P.........",
        ".........P.GG.P.........",
        ".........P.GG.P.........",
        ".........P....P.........",
        ".........PPPPPP.........",
        "........................",
        "........................",
        "........................",
        "........................",
        "........................"
        ),
    )

    val accessory1 = PixelSprite(
        assetId = ACCESSORY_1_ID,
        width = 24,
        height = 24,
        palette = palette,
        rows = listOf(
        "........................",
        "........................",
        "........................",
        "........PPPPPPPP........",
        "........PPPCCPPP........",
        "........PPPCCPPP........",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PP..........PP.....",
        ".....PP..........PP.....",
        ".....PP..........PP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPP......PPPP.....",
        ".....PPPP......PPPP.....",
        ".....PPPP......PPPP.....",
        ".....PPPP......PPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        "........................",
        "........................",
        "........................",
        "........................"
        ),
    )

    val accessory2 = PixelSprite(
        assetId = ACCESSORY_2_ID,
        width = 24,
        height = 24,
        palette = palette,
        rows = listOf(
        "........................",
        "........................",
        "........................",
        "............P...........",
        "............P...........",
        "............P...........",
        "............P...........",
        "..........PPPPP.........",
        "........PPP...PPP.......",
        "........PP.....PP.......",
        ".......PP.......PP......",
        ".......P.........P......",
        ".......P....G....P......",
        ".......P.........P......",
        ".......PP.......PP......",
        "........PP.....PP.......",
        "........PPP...PPP.......",
        "..........PPPPP.........",
        "...........P.P..........",
        "..........P...P.........",
        ".........P.....P........",
        "........P.......P.......",
        "........................",
        "........................"
        ),
    )

    val productionSlots: List<PixelSprite> = listOf(
        head,
        body,
        hands,
        legs,
        feet,
        mainHand,
        offHand,
        ring1,
        ring2,
        neck,
        accessory1,
        accessory2,
    )

    fun slot(slotId: String): PixelSprite? = when (slotId) {
        "head" -> head
        "body" -> body
        "hands" -> hands
        "legs" -> legs
        "feet" -> feet
        "main_hand" -> mainHand
        "off_hand" -> offHand
        "ring_1" -> ring1
        "ring_2" -> ring2
        "neck" -> neck
        "accessory_1" -> accessory1
        "accessory_2" -> accessory2
        else -> null
    }
}
