package com.thegame.rpg.ui

import androidx.compose.ui.graphics.Color

/**
 * Source-native UI identity icons for player-facing projected state.
 *
 * These sprites never calculate navigation, resources, quests, or map state. They only
 * decorate values already present in the Compose presentation model.
 */
object PixelUiIconCatalog {
    const val NAV_STORY_ID = "UI_NAV_STORY_ICON"
    const val NAV_CHARACTER_ID = "UI_NAV_CHARACTER_ICON"
    const val NAV_STATS_ID = "UI_NAV_STATS_ICON"
    const val NAV_INVENTORY_ID = "UI_NAV_INVENTORY_ICON"
    const val NAV_QUESTS_ID = "UI_NAV_QUESTS_ICON"
    const val NAV_MAP_ID = "UI_NAV_MAP_ICON"
    const val NAV_MORE_ID = "UI_NAV_MORE_SETTINGS_ICON"
    const val RESOURCE_HEALTH_ID = "UI_RESOURCE_HEALTH_ICON"
    const val RESOURCE_STAMINA_ID = "UI_RESOURCE_STAMINA_ICON"
    const val RESOURCE_FOCUS_ID = "UI_RESOURCE_FOCUS_ICON"
    const val RESOURCE_RESOLVE_ID = "UI_RESOURCE_RESOLVE_ICON"
    const val QUEST_MAIN_ID = "UI_QUEST_MAIN_ICON"
    const val QUEST_SIDE_ID = "UI_QUEST_SIDE_ICON"
    const val QUEST_OPTIONAL_ID = "UI_QUEST_OPTIONAL_ICON"
    const val QUEST_LORE_ID = "UI_QUEST_LORE_ICON"

    private val palette = mapOf(
        'P' to PixelColors.Paper,
        'C' to PixelColors.Cyan,
        'G' to PixelColors.Gold,
        'M' to PixelColors.Muted,
        'R' to PixelColors.Danger,
    )

    val navStory = PixelSprite(
        assetId = NAV_STORY_ID,
        width = 24,
        height = 24,
        palette = palette,
        rows = listOf(
        "........................",
        "........................",
        "........................",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PP..........PP.....",
        ".....PP..........PP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PP........PPPP.....",
        ".....PP........PPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PP..........PP.....",
        ".....PP..........PP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PP......PPPPPP.....",
        ".....PP......PPPPPPP....",
        ".....PPPPPPPPPPPPPPP....",
        ".....PPPPPPPPPPPPPPP....",
        ".....PPPPPPPPPPPPPPP....",
        ".....PPPPPPPPPPPPPP.....",
        ".................PP.....",
        "........................",
        "........................"
        ),
    )

    val navCharacter = PixelSprite(
        assetId = NAV_CHARACTER_ID,
        width = 24,
        height = 24,
        palette = palette,
        rows = listOf(
        "........................",
        "........................",
        "........................",
        ".........PPPPPP.........",
        ".........PPPPPP.........",
        ".........PPPPPP.........",
        ".........PPPPPP.........",
        ".........PPPPPP.........",
        ".........PPPPPP.........",
        ".......PPPPPPPPPP.......",
        ".......PPPPPPPPPP.......",
        ".......PPPPPPPPPP.......",
        ".......PPPPPPPPPP.......",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        "..PPPPPPPPPPPPPPPPPPPP..",
        "..PPPPPPPPPPPPPPPPPPPP..",
        "..PPPPPPPPPPPPPPPPPPPP..",
        "..PPPPPPPPPPPPPPPPPPPP..",
        "..PPPPP..........PPPPP..",
        "........................",
        "........................",
        "........................"
        ),
    )

    val navStats = PixelSprite(
        assetId = NAV_STATS_ID,
        width = 24,
        height = 24,
        palette = palette,
        rows = listOf(
        "........................",
        "........................",
        "........................",
        "........................",
        "................PPP.....",
        "................PPP.....",
        "................PPP.....",
        "................PPP.....",
        "................PPP.....",
        "..........PPP...PPP.....",
        "..........PPP...PPP.....",
        "..........PPP...PPP.....",
        "..........PPP...PPP.....",
        "..........PPP...PPP.....",
        "....PPP...PPP...PPP.....",
        "....PPP...PPP...PPP.....",
        "....PPP...PPP...PPP.....",
        "....PPP...PPP...PPP.....",
        "....PPP...PPP...PPP.....",
        "....PPP...PPP...PPP.....",
        "...PPPPPPPPPPPPPPPPP....",
        "...PPPPPPPPPPPPPPPPP....",
        "........................",
        "........................"
        ),
    )

    val navInventory = PixelSprite(
        assetId = NAV_INVENTORY_ID,
        width = 24,
        height = 24,
        palette = palette,
        rows = listOf(
        "........................",
        "........................",
        "........................",
        "........................",
        "........PPPPPPPP........",
        "........PPPPPPPP........",
        "........PPPPPPPP........",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPP........PPP.....",
        ".....PPP........PPP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PP....PP....PP.....",
        ".....PP....PP....PP.....",
        ".....PP....PP....PP.....",
        ".....PP....PP....PP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        "........................",
        "........................",
        "........................",
        "........................"
        ),
    )

    val navQuests = PixelSprite(
        assetId = NAV_QUESTS_ID,
        width = 24,
        height = 24,
        palette = palette,
        rows = listOf(
        "........................",
        "........................",
        "........................",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPP........PPP.....",
        ".....PPP........PPP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPP........PPP.....",
        ".....PPP........PPP.....",
        ".....PPPPPPPPPPPPPP..P..",
        ".....PPPPPPPPPPPPPP.P...",
        ".....PPP.....PPPPPP.P...",
        ".....PPP.....PPPPPPP....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        ".....PPPPPPPPPPPPPP.....",
        "........................",
        "........................",
        "........................"
        ),
    )

    val navMap = PixelSprite(
        assetId = NAV_MAP_ID,
        width = 24,
        height = 24,
        palette = palette,
        rows = listOf(
        "........................",
        "........................",
        "........................",
        "........PP..............",
        "......PP.PPP.......PP...",
        "....PP...P..PP...PP.P...",
        "....P....P....PPP...P...",
        "....P....P.....P....P...",
        "....P....P.....P....P...",
        "....P....P.....P....P...",
        "....P....P..C..P....P...",
        "....P....P...C.P....P...",
        "....P....P....CP....P...",
        "....P....P.....P....P...",
        "....P....P.....P....P...",
        "....P....P.....P....P...",
        "....P....P.....P....P...",
        "....P...PP.....P....P...",
        "....P.PP..PP...P...PP...",
        "....PP......PP.P.PP.....",
        "..............PPP.......",
        "........................",
        "........................",
        "........................"
        ),
    )

    val navMore = PixelSprite(
        assetId = NAV_MORE_ID,
        width = 24,
        height = 24,
        palette = palette,
        rows = listOf(
        "........................",
        "........................",
        "........................",
        "...........PP...........",
        "...........PP...........",
        ".....PP..........PP.....",
        ".....PP..........PP.....",
        "..........PPPP..........",
        "........PPPPPPPP........",
        "........PP....PP........",
        ".......PP.PPPP.PP.......",
        "...PP..PP.PPPP.PP..PP...",
        "...PP..PP.PPPP.PP..PP...",
        ".......PP.PPPP.PP.......",
        "........PP....PP........",
        "........PPPPPPPP........",
        "..........PPPP..........",
        ".....PP..........PP.....",
        ".....PP..........PP.....",
        "...........PP...........",
        "...........PP...........",
        "........................",
        "........................",
        "........................"
        ),
    )

    val resourceHealth = PixelSprite(
        assetId = RESOURCE_HEALTH_ID,
        width = 16,
        height = 16,
        palette = palette,
        rows = listOf(
        "................",
        "................",
        "................",
        "................",
        "...PPPP..PPPP...",
        "...PPPP..PPPP...",
        "..PPPPPPPPPPPP..",
        "..PPPPPPPPPPPP..",
        "..PPPPPPPPPPPP..",
        "....PPPPPPPP....",
        "....PPPPPPPP....",
        "......PPPP......",
        "......PPPP......",
        ".......PP.......",
        "................",
        "................"
        ),
    )

    val resourceStamina = PixelSprite(
        assetId = RESOURCE_STAMINA_ID,
        width = 16,
        height = 16,
        palette = palette,
        rows = listOf(
        "................",
        "................",
        "..........P.....",
        ".........PP.....",
        "........PP......",
        ".......P.P......",
        ".......PP.......",
        "......P.PPPPP...",
        ".....PPPPP.P....",
        "........P.P.....",
        "........PP......",
        ".......P.P......",
        ".......PP.......",
        "......PP........",
        "......P.........",
        "................"
        ),
    )

    val resourceFocus = PixelSprite(
        assetId = RESOURCE_FOCUS_ID,
        width = 16,
        height = 16,
        palette = palette,
        rows = listOf(
        "................",
        "................",
        ".....PPPPPP.....",
        "....PP....PP....",
        "...PP......PP...",
        "..PP..PPPP..PP..",
        "..P..PP..PP..P..",
        "..P..P.PP.P..P..",
        "..P..P.PP.P..P..",
        "..P..PP..PP..P..",
        "..PP..PPPP..PP..",
        "...PP......PP...",
        "....PP....PP....",
        ".....PPPPPP.....",
        "................",
        "................"
        ),
    )

    val resourceResolve = PixelSprite(
        assetId = RESOURCE_RESOLVE_ID,
        width = 16,
        height = 16,
        palette = palette,
        rows = listOf(
        "................",
        "................",
        "................",
        "....PPPPPPPP....",
        "....P......P....",
        "...P........P...",
        "...P........P...",
        "...P........P...",
        "...P........P...",
        "....P......P....",
        "....P......P....",
        ".....P....P.....",
        ".....P....P.....",
        "......PP.P......",
        "........P.......",
        "................"
        ),
    )

    val questMain = PixelSprite(
        assetId = QUEST_MAIN_ID,
        width = 16,
        height = 16,
        palette = palette,
        rows = listOf(
        "................",
        "................",
        "........P.......",
        ".......P.P......",
        "......P...P.....",
        ".....P.PP..P....",
        "....P..PP...P...",
        "...P...PP....P..",
        "....P..PP...P...",
        ".....P.PP..P....",
        ".....P....P.....",
        "......PPP.P.....",
        ".......PPP......",
        "........P.......",
        "................",
        "................"
        ),
    )

    val questSide = PixelSprite(
        assetId = QUEST_SIDE_ID,
        width = 16,
        height = 16,
        palette = palette,
        rows = listOf(
        "................",
        "................",
        "...PPP..........",
        "...PPP....PPP...",
        "...PPP....PPP...",
        "....P.....PPP...",
        "....P......P....",
        "....PPPPPPPP....",
        "....P......P....",
        "....P......P....",
        "....P.....PPP...",
        "....P.....PPP...",
        "....P.....PPP...",
        "................",
        "................",
        "................"
        ),
    )

    val questOptional = PixelSprite(
        assetId = QUEST_OPTIONAL_ID,
        width = 16,
        height = 16,
        palette = palette,
        rows = listOf(
        "................",
        "................",
        "........P.......",
        "........PP......",
        ".......P.P......",
        ".......P..P.....",
        "..PPPPP...PPPPP.",
        "...P.........P..",
        "....P.......P...",
        ".....P.....P....",
        ".....P.....P....",
        ".....P..PP..P...",
        "....P.PP..PPP...",
        "....PP......P...",
        "................",
        "................"
        ),
    )

    val questLore = PixelSprite(
        assetId = QUEST_LORE_ID,
        width = 16,
        height = 16,
        palette = palette,
        rows = listOf(
        "................",
        "................",
        "...PPPPPPPCCC...",
        "...PPPPPPPCCC...",
        "...PP.....CCC...",
        "...PP......PP...",
        "...PPPPPPPPPP...",
        "...PP......PP...",
        "...PPPPPPPPPP...",
        "...PPPPPPPPPP...",
        "...PP....PPPP...",
        "...PPPPPPPPPP...",
        "...PPPPPPPPPP...",
        "...PPPPPPPPPP...",
        "................",
        "................"
        ),
    )

    val productionIcons: List<PixelSprite> = listOf(
        navStory,
        navCharacter,
        navStats,
        navInventory,
        navQuests,
        navMap,
        navMore,
        resourceHealth,
        resourceStamina,
        resourceFocus,
        resourceResolve,
        questMain,
        questSide,
        questOptional,
        questLore,
    )

    fun navigation(label: String): PixelSprite? = when (label.lowercase()) {
        "story" -> navStory
        "character" -> navCharacter
        "stats" -> navStats
        "inventory" -> navInventory
        "quests" -> navQuests
        "map" -> navMap
        "more", "settings" -> navMore
        else -> null
    }

    fun resource(resourceId: String): PixelSprite? = when (resourceId.lowercase()) {
        "health" -> resourceHealth
        "stamina" -> resourceStamina
        "focus" -> resourceFocus
        "resolve" -> resourceResolve
        else -> null
    }

    fun quest(category: String): PixelSprite? = when (category.lowercase()) {
        "main" -> questMain
        "side" -> questSide
        "optional" -> questOptional
        "lore" -> questLore
        else -> null
    }
}
