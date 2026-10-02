package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertSame
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelUiIconCatalogTest {
    @Test
    fun productionUiIconsUsePlannedNativeDimensionsAndDefinedPaletteKeys() {
        val expected = mapOf(
            PixelUiIconCatalog.NAV_STORY_ID to (24 to 24),
            PixelUiIconCatalog.NAV_CHARACTER_ID to (24 to 24),
            PixelUiIconCatalog.NAV_STATS_ID to (24 to 24),
            PixelUiIconCatalog.NAV_INVENTORY_ID to (24 to 24),
            PixelUiIconCatalog.NAV_QUESTS_ID to (24 to 24),
            PixelUiIconCatalog.NAV_MAP_ID to (24 to 24),
            PixelUiIconCatalog.NAV_MORE_ID to (24 to 24),
            PixelUiIconCatalog.RESOURCE_HEALTH_ID to (16 to 16),
            PixelUiIconCatalog.RESOURCE_STAMINA_ID to (16 to 16),
            PixelUiIconCatalog.RESOURCE_FOCUS_ID to (16 to 16),
            PixelUiIconCatalog.RESOURCE_RESOLVE_ID to (16 to 16),
            PixelUiIconCatalog.QUEST_MAIN_ID to (16 to 16),
            PixelUiIconCatalog.QUEST_SIDE_ID to (16 to 16),
            PixelUiIconCatalog.QUEST_OPTIONAL_ID to (16 to 16),
            PixelUiIconCatalog.QUEST_LORE_ID to (16 to 16),
        )

        assertEquals(expected.keys, PixelUiIconCatalog.productionIcons.map { it.assetId }.toSet())

        PixelUiIconCatalog.productionIcons.forEach { icon ->
            val dimensions = expected.getValue(icon.assetId)
            assertEquals(dimensions.first, icon.width)
            assertEquals(dimensions.second, icon.height)
            assertEquals(icon.height, icon.rows.size)
            assertTrue(icon.rows.all { it.length == icon.width })

            val used = icon.rows
                .flatMap { row -> row.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()

            assertTrue(
                "${icon.assetId} contains an unmapped palette key",
                used.all { it in icon.palette },
            )
        }
    }

    @Test
    fun navigationMappingsArePresentationOnlyAndStable() {
        assertSame(PixelUiIconCatalog.navStory, PixelUiIconCatalog.navigation("Story"))
        assertSame(PixelUiIconCatalog.navCharacter, PixelUiIconCatalog.navigation("Character"))
        assertSame(PixelUiIconCatalog.navStats, PixelUiIconCatalog.navigation("Stats"))
        assertSame(PixelUiIconCatalog.navInventory, PixelUiIconCatalog.navigation("Inventory"))
        assertSame(PixelUiIconCatalog.navQuests, PixelUiIconCatalog.navigation("Quests"))
        assertSame(PixelUiIconCatalog.navMap, PixelUiIconCatalog.navigation("Map"))
        assertSame(PixelUiIconCatalog.navMore, PixelUiIconCatalog.navigation("More"))
        assertSame(PixelUiIconCatalog.navMore, PixelUiIconCatalog.navigation("Settings"))
        assertNull(PixelUiIconCatalog.navigation("Unknown"))
    }

    @Test
    fun resourceAndQuestMappingsUseOnlyProjectedIds() {
        assertSame(PixelUiIconCatalog.resourceHealth, PixelUiIconCatalog.resource("health"))
        assertSame(PixelUiIconCatalog.resourceStamina, PixelUiIconCatalog.resource("stamina"))
        assertSame(PixelUiIconCatalog.resourceFocus, PixelUiIconCatalog.resource("focus"))
        assertSame(PixelUiIconCatalog.resourceResolve, PixelUiIconCatalog.resource("resolve"))
        assertNull(PixelUiIconCatalog.resource("hidden_resource"))

        assertSame(PixelUiIconCatalog.questMain, PixelUiIconCatalog.quest("main"))
        assertSame(PixelUiIconCatalog.questSide, PixelUiIconCatalog.quest("side"))
        assertSame(PixelUiIconCatalog.questOptional, PixelUiIconCatalog.quest("optional"))
        assertSame(PixelUiIconCatalog.questLore, PixelUiIconCatalog.quest("lore"))
        assertNull(PixelUiIconCatalog.quest("unknown"))
    }
}
