package com.thegame.rpg.ui

import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.drawBehind
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.unit.dp

enum class PixelPanelChrome {
    STORY,
    CHARACTER,
    STATS,
    INVENTORY,
    QUEST,
    MAP,
    SETTINGS,
    DEVELOPER,
    MODAL,
}

data class PixelChromeAsset(
    val assetId: String,
    val fill: Color,
    val outer: Color,
    val inner: Color,
    val corner: Color,
    val accent: Color,
)

/**
 * Procedural source-native UI masters for the planned stretchable/9-slice shell assets.
 *
 * Geometry is defined in integer-density pixel bands rather than smooth vector curves. The
 * assets own presentation only; selection/availability still comes from Compose/game state.
 */
object PixelUiChromeCatalog {
    const val STORY_FRAME_ID = "UI_PANEL_STORY_FRAME"
    const val CHARACTER_FRAME_ID = "UI_PANEL_CHARACTER_FRAME"
    const val STATS_FRAME_ID = "UI_PANEL_STATS_FRAME"
    const val INVENTORY_FRAME_ID = "UI_PANEL_INVENTORY_FRAME"
    const val QUEST_FRAME_ID = "UI_PANEL_QUEST_FRAME"
    const val MAP_FRAME_ID = "UI_PANEL_MAP_FRAME"
    const val SETTINGS_FRAME_ID = "UI_PANEL_SETTINGS_FRAME"
    const val DEVELOPER_FRAME_ID = "UI_PANEL_DEVELOPER_FRAME"
    const val MODAL_FRAME_ID = "UI_MODAL_FRAME"
    const val CHOICE_ENABLED_ID = "UI_CHOICE_CARD_ENABLED"
    const val CHOICE_DISABLED_ID = "UI_CHOICE_CARD_DISABLED"
    const val CHOICE_SELECTED_ID = "UI_CHOICE_CARD_SELECTED"
    const val BUTTON_PRIMARY_ID = "UI_BUTTON_PRIMARY"
    const val BUTTON_SECONDARY_ID = "UI_BUTTON_SECONDARY"
    const val BUTTON_DANGER_ID = "UI_BUTTON_DANGER"
    const val TAB_ACTIVE_ID = "UI_TAB_ACTIVE"
    const val TAB_INACTIVE_ID = "UI_TAB_INACTIVE"

    private fun asset(
        id: String,
        fill: Color,
        outer: Color,
        inner: Color,
        corner: Color,
        accent: Color,
    ) = PixelChromeAsset(
        assetId = id,
        fill = fill,
        outer = outer,
        inner = inner,
        corner = corner,
        accent = accent,
    )

    val storyFrame = asset(
        STORY_FRAME_ID,
        PixelColors.Panel,
        PixelColors.Muted,
        PixelColors.Deep,
        PixelColors.Cyan,
        PixelColors.Cyan,
    )
    val characterFrame = asset(
        CHARACTER_FRAME_ID,
        PixelColors.Panel,
        PixelColors.Muted,
        PixelColors.Deep,
        PixelColors.Gold,
        PixelColors.Cyan,
    )
    val statsFrame = asset(
        STATS_FRAME_ID,
        PixelColors.Panel,
        PixelColors.Muted,
        PixelColors.Deep,
        PixelColors.Cyan,
        PixelColors.Gold,
    )
    val inventoryFrame = asset(
        INVENTORY_FRAME_ID,
        PixelColors.Panel,
        PixelColors.Muted,
        PixelColors.Deep,
        PixelColors.Paper,
        PixelColors.Cyan,
    )
    val questFrame = asset(
        QUEST_FRAME_ID,
        PixelColors.Panel,
        PixelColors.Muted,
        PixelColors.Deep,
        PixelColors.Gold,
        PixelColors.Gold,
    )
    val mapFrame = asset(
        MAP_FRAME_ID,
        PixelColors.Panel,
        PixelColors.Muted,
        PixelColors.Deep,
        PixelColors.Cyan,
        PixelColors.Gold,
    )
    val settingsFrame = asset(
        SETTINGS_FRAME_ID,
        PixelColors.Panel,
        PixelColors.Muted,
        PixelColors.Deep,
        PixelColors.Muted,
        PixelColors.Cyan,
    )
    val developerFrame = asset(
        DEVELOPER_FRAME_ID,
        PixelColors.Panel,
        PixelColors.Danger,
        PixelColors.Deep,
        PixelColors.Gold,
        PixelColors.Danger,
    )
    val modalFrame = asset(
        MODAL_FRAME_ID,
        PixelColors.Panel,
        PixelColors.Gold,
        PixelColors.Deep,
        PixelColors.Cyan,
        PixelColors.Gold,
    )

    val choiceEnabled = asset(
        CHOICE_ENABLED_ID,
        PixelColors.PanelAlt,
        PixelColors.Cyan,
        PixelColors.Deep,
        PixelColors.Cyan,
        PixelColors.Gold,
    )
    val choiceDisabled = asset(
        CHOICE_DISABLED_ID,
        PixelColors.Deep,
        PixelColors.Disabled,
        PixelColors.Deep,
        PixelColors.Muted,
        PixelColors.Disabled,
    )
    val choiceSelected = asset(
        CHOICE_SELECTED_ID,
        PixelColors.Deep,
        PixelColors.Gold,
        PixelColors.Cyan,
        PixelColors.Gold,
        PixelColors.Cyan,
    )

    val buttonPrimary = asset(
        BUTTON_PRIMARY_ID,
        PixelColors.PanelAlt,
        PixelColors.Cyan,
        PixelColors.Deep,
        PixelColors.Cyan,
        PixelColors.Gold,
    )
    val buttonSecondary = asset(
        BUTTON_SECONDARY_ID,
        PixelColors.Deep,
        PixelColors.Muted,
        PixelColors.PanelAlt,
        PixelColors.Muted,
        PixelColors.Cyan,
    )
    val buttonDanger = asset(
        BUTTON_DANGER_ID,
        PixelColors.Deep,
        PixelColors.Danger,
        PixelColors.PanelAlt,
        PixelColors.Danger,
        PixelColors.Gold,
    )

    val tabActive = asset(
        TAB_ACTIVE_ID,
        PixelColors.Cyan,
        PixelColors.Paper,
        PixelColors.Ink,
        PixelColors.Gold,
        PixelColors.Paper,
    )
    val tabInactive = asset(
        TAB_INACTIVE_ID,
        PixelColors.Deep,
        PixelColors.Muted,
        PixelColors.Panel,
        PixelColors.Muted,
        PixelColors.Cyan,
    )

    fun panel(kind: PixelPanelChrome): PixelChromeAsset = when (kind) {
        PixelPanelChrome.STORY -> storyFrame
        PixelPanelChrome.CHARACTER -> characterFrame
        PixelPanelChrome.STATS -> statsFrame
        PixelPanelChrome.INVENTORY -> inventoryFrame
        PixelPanelChrome.QUEST -> questFrame
        PixelPanelChrome.MAP -> mapFrame
        PixelPanelChrome.SETTINGS -> settingsFrame
        PixelPanelChrome.DEVELOPER -> developerFrame
        PixelPanelChrome.MODAL -> modalFrame
    }

    val produced: List<PixelChromeAsset> = listOf(
        storyFrame,
        characterFrame,
        statsFrame,
        inventoryFrame,
        questFrame,
        mapFrame,
        settingsFrame,
        developerFrame,
        modalFrame,
        choiceEnabled,
        choiceDisabled,
        choiceSelected,
        buttonPrimary,
        buttonSecondary,
        buttonDanger,
        tabActive,
        tabInactive,
    )
}

/**
 * Draw a hard-edged scalable pixel frame. The corner blocks and center ticks are the
 * procedural equivalent of a small nine-slice master; they do not scale with content.
 */
fun Modifier.pixelChrome(asset: PixelChromeAsset): Modifier = drawBehind {
    drawRect(asset.fill)

    val px = 1.dp.toPx().coerceAtLeast(1f)
    val outerWidth = 2f * px
    val innerInset = 3f * px
    val innerWidth = px
    val corner = 5f * px
    val tick = 8f * px

    drawRect(
        color = asset.outer,
        topLeft = Offset(outerWidth / 2f, outerWidth / 2f),
        size = Size(
            (size.width - outerWidth).coerceAtLeast(0f),
            (size.height - outerWidth).coerceAtLeast(0f),
        ),
        style = Stroke(width = outerWidth),
    )

    if (size.width > innerInset * 2f && size.height > innerInset * 2f) {
        drawRect(
            color = asset.inner,
            topLeft = Offset(innerInset, innerInset),
            size = Size(
                size.width - innerInset * 2f,
                size.height - innerInset * 2f,
            ),
            style = Stroke(width = innerWidth),
        )
    }

    // Four hard corner blocks keep the asset readable when the panel stretches.
    drawRect(asset.corner, Offset.Zero, Size(corner, corner))
    drawRect(asset.corner, Offset(size.width - corner, 0f), Size(corner, corner))
    drawRect(asset.corner, Offset(0f, size.height - corner), Size(corner, corner))
    drawRect(
        asset.corner,
        Offset(size.width - corner, size.height - corner),
        Size(corner, corner),
    )

    // Short center ticks provide a stable accent without consuming text space.
    if (size.width >= tick * 3f) {
        drawRect(
            asset.accent,
            Offset((size.width - tick) / 2f, 0f),
            Size(tick, outerWidth),
        )
        drawRect(
            asset.accent,
            Offset((size.width - tick) / 2f, size.height - outerWidth),
            Size(tick, outerWidth),
        )
    }
}
