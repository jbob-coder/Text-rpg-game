package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelUiChromeCatalogTest {
    @Test
    fun plannedChromeAssetsHaveStableUniqueIds() {
        val assets = PixelUiChromeCatalog.produced

        assertEquals(16, assets.size)
        assertEquals(16, assets.map { it.assetId }.toSet().size)
        assertTrue(assets.all { it.assetId.startsWith("UI_") })
    }

    @Test
    fun panelKindsResolveToTheirDocumentedAssets() {
        assertEquals(
            PixelUiChromeCatalog.STORY_FRAME_ID,
            PixelUiChromeCatalog.panel(PixelPanelChrome.STORY).assetId,
        )
        assertEquals(
            PixelUiChromeCatalog.CHARACTER_FRAME_ID,
            PixelUiChromeCatalog.panel(PixelPanelChrome.CHARACTER).assetId,
        )
        assertEquals(
            PixelUiChromeCatalog.STATS_FRAME_ID,
            PixelUiChromeCatalog.panel(PixelPanelChrome.STATS).assetId,
        )
        assertEquals(
            PixelUiChromeCatalog.INVENTORY_FRAME_ID,
            PixelUiChromeCatalog.panel(PixelPanelChrome.INVENTORY).assetId,
        )
        assertEquals(
            PixelUiChromeCatalog.QUEST_FRAME_ID,
            PixelUiChromeCatalog.panel(PixelPanelChrome.QUEST).assetId,
        )
        assertEquals(
            PixelUiChromeCatalog.MAP_FRAME_ID,
            PixelUiChromeCatalog.panel(PixelPanelChrome.MAP).assetId,
        )
        assertEquals(
            PixelUiChromeCatalog.SETTINGS_FRAME_ID,
            PixelUiChromeCatalog.panel(PixelPanelChrome.SETTINGS).assetId,
        )
        assertEquals(
            PixelUiChromeCatalog.DEVELOPER_FRAME_ID,
            PixelUiChromeCatalog.panel(PixelPanelChrome.DEVELOPER).assetId,
        )
    }

    @Test
    fun enabledDisabledAndTabStatesUseDistinctPresentationMasters() {
        assertNotEquals(
            PixelUiChromeCatalog.choiceEnabled.assetId,
            PixelUiChromeCatalog.choiceDisabled.assetId,
        )
        assertNotEquals(
            PixelUiChromeCatalog.tabActive.assetId,
            PixelUiChromeCatalog.tabInactive.assetId,
        )
        assertNotEquals(
            PixelUiChromeCatalog.buttonPrimary.assetId,
            PixelUiChromeCatalog.buttonDanger.assetId,
        )
    }
}
