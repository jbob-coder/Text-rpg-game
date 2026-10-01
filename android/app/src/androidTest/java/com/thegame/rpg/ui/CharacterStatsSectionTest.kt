package com.thegame.rpg.ui

import android.graphics.Bitmap
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.size
import androidx.compose.runtime.CompositionLocalProvider
import androidx.compose.runtime.mutableStateOf
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.asAndroidBitmap
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.test.assertCountEquals
import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.assertIsNotEnabled
import androidx.compose.ui.test.captureToImage
import androidx.compose.ui.test.junit4.createComposeRule
import androidx.compose.ui.test.onAllNodesWithTag
import androidx.compose.ui.test.onNodeWithTag
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.performClick
import androidx.compose.ui.test.performScrollTo
import androidx.compose.ui.unit.Density
import androidx.compose.ui.unit.dp
import androidx.test.platform.io.PlatformTestStorageRegistry
import com.thegame.rpg.engine.GameAttribute
import com.thegame.rpg.engine.GameEquipmentSlot
import com.thegame.rpg.engine.GameInventory
import com.thegame.rpg.engine.GameInventoryItem
import com.thegame.rpg.engine.GameResource
import com.thegame.rpg.engine.GameSkill
import com.thegame.rpg.engine.GameSnapshot
import com.thegame.rpg.engine.GameStatusContribution
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Rule
import org.junit.Test

class CharacterStatsSectionTest {
    @get:Rule val composeRule = createComposeRule()

    private val slotIds = listOf("head", "body", "hands", "legs", "feet", "main_hand", "off_hand", "ring_1", "ring_2", "neck", "accessory_1", "accessory_2")
    private val items = mapOf(
        "body" to ("ITEM_DEPOT_JACKET" to "Depot utility jacket"),
        "hands" to ("ITEM_WORK_GLOVES" to "Insulated work gloves"),
        "ring_1" to ("ITEM_SIGNAL_RING" to "Signal ring"),
        "neck" to ("ITEM_COURIER_NECKTAG" to "Courier neck tag"),
    )
    private val snapshot = GameSnapshot(
        sceneId = "OPENING_PLATFORM", title = "Platform Nine", body = "", choices = emptyList(),
        resources = listOf(GameResource("health", 100.0, 144.0), GameResource("stamina", 70.0, 105.0), GameResource("focus", 60.0, 94.0), GameResource("resolve", 50.0, 80.0)),
        attributes = listOf(
            GameAttribute("might", "Might", 30.0, 30.0, 0.0, false, "raw physical force"),
            GameAttribute("agility", "Agility", 35.0, 35.0, 0.0, false, "movement, coordination, reaction"),
            GameAttribute("endurance", "Endurance", 35.0, 37.0, 2.0, true, "fatigue tolerance and resilience", listOf(GameStatusContribution("equipment", "Depot utility jacket", 2.0, "body"))),
            GameAttribute("intellect", "Intellect", 45.0, 45.0, 0.0, false, "reasoning and technical learning"),
            GameAttribute("will", "Will", 40.0, 40.0, 0.0, false, "mental resistance and discipline"),
            GameAttribute("perception", "Perception", 40.0, 41.0, 1.0, true, "awareness, danger, and tells", listOf(GameStatusContribution("equipment", "Signal ring", 1.0, "ring_1"))),
            GameAttribute("presence", "Presence", 30.0, 31.0, 1.0, true, "social force and leadership", listOf(GameStatusContribution("equipment", "Courier neck tag", 1.0, "neck"))),
        ),
        skills = listOf(GameSkill("technical_systems", "Technical Systems", "technical", 25.0, 26.0, 1.0, true, listOf(GameStatusContribution("equipment", "Insulated work gloves", 1.0, "hands")))),
        inventory = GameInventory(equipment = slotIds.map { slot ->
            val item = items[slot]
            GameEquipmentSlot(slot, item != null, item?.first, item?.second)
        }),
        turn = 0, timeMinutes = 0, location = "PLATFORM_NINE",
    )

    private fun saveScreenshot(name: String, tag: String = "qa-phone") {
        // Gradle collects this runner-owned output before completing connected tests.
        PlatformTestStorageRegistry.getInstance().openOutputFile("$name.png").use {
            assertTrue(composeRule.onNodeWithTag(tag).captureToImage().asAndroidBitmap().compress(Bitmap.CompressFormat.PNG, 100, it))
        }
    }

    @Test
    fun allTwelveSlotsAndAvatarFitPhoneWidthAndSelectedGearShowsItsEngineBonus() {
        var unequipped: String? = null
        composeRule.setContent {
            PixelTheme {
                Box(Modifier.size(320.dp, 640.dp).background(PixelColors.Ink).testTag("qa-phone")) {
                    CharacterSection(snapshot, false, {}, { unequipped = it })
                }
            }
        }
        saveScreenshot("character-320dp")
        composeRule.onNodeWithTag("player-avatar").assertIsDisplayed()
        val viewport = composeRule.onNodeWithTag("qa-phone").fetchSemanticsNode().boundsInRoot
        slotIds.forEach { slot ->
            val node = composeRule.onNodeWithTag("character-slot-$slot").performScrollTo().assertIsDisplayed().fetchSemanticsNode()
            assertTrue(node.boundsInRoot.left >= viewport.left - 1)
            assertTrue(node.boundsInRoot.right <= viewport.right + 1)
        }
        composeRule.onNodeWithTag("character-slot-body").performScrollTo().performClick()
        composeRule.onNodeWithTag("character-equipment-detail").assertIsDisplayed()
        composeRule.onNodeWithText("Depot utility jacket").assertIsDisplayed()
        composeRule.onNodeWithText("Endurance: +2").assertIsDisplayed()
        saveScreenshot("equipment-jacket-detail", "character-equipment-detail")
        val detail = composeRule.onNodeWithTag("character-equipment-detail").fetchSemanticsNode().boundsInRoot
        assertTrue("Short equipment details must wrap their content instead of filling the screen", detail.height < viewport.height * 0.75f)
        composeRule.onNodeWithTag("character-unequip").performClick()
        composeRule.runOnIdle { assertEquals("body", unequipped) }
    }

    @Test
    fun emptySlotEquipEmitsItemIdAndBusyStateDisablesMutations() {
        var equipped: String? = null
        val busy = mutableStateOf(false)
        val emptyLoadout = snapshot.copy(inventory = GameInventory(
            equipment = snapshot.inventory.equipment.map { if (it.slot == "body") GameEquipmentSlot("body", false) else it },
            items = listOf(GameInventoryItem("ITEM_DEPOT_JACKET", "Depot utility jacket", 1, true, "body")),
        ))
        composeRule.setContent {
            PixelTheme { Box(Modifier.size(320.dp, 640.dp)) {
                CharacterSection(emptyLoadout, busy.value, { equipped = it }, {})
            } }
        }
        composeRule.onNodeWithTag("character-slot-body").performScrollTo().performClick()
        composeRule.onNodeWithTag("character-equip-ITEM_DEPOT_JACKET").performClick()
        composeRule.runOnIdle { assertEquals("ITEM_DEPOT_JACKET", equipped); busy.value = true }
        composeRule.onNodeWithTag("character-equip-ITEM_DEPOT_JACKET").assertIsNotEnabled()
    }

    @Test
    fun openEquipmentDetailUsesFreshSnapshotAfterUnequip() {
        val state = mutableStateOf(snapshot)
        composeRule.setContent {
            PixelTheme { Box(Modifier.size(320.dp, 640.dp)) {
                CharacterSection(state.value, false, {}, {})
            } }
        }
        composeRule.onNodeWithTag("character-slot-body").performScrollTo().performClick()
        composeRule.onNodeWithText("Endurance: +2").assertIsDisplayed()
        composeRule.runOnIdle {
            state.value = snapshot.copy(inventory = GameInventory(equipment = snapshot.inventory.equipment.map {
                if (it.slot == "body") GameEquipmentSlot("body", false) else it
            }))
        }
        composeRule.onNodeWithText("Empty slot").assertIsDisplayed()
        composeRule.onAllNodesWithTag("character-unequip").assertCountEquals(0)
    }

    @Test
    fun statsUseSevenProjectedAttributesAndOneSelectableDetailWithoutPortrait() {
        composeRule.setContent {
            PixelTheme { Box(Modifier.size(320.dp, 640.dp).background(PixelColors.Ink).testTag("qa-phone")) { StatsSection(snapshot) } }
        }
        saveScreenshot("stats-320dp")
        composeRule.onAllNodesWithTag("player-avatar").assertCountEquals(0)
        composeRule.onAllNodesWithTag("stats-attribute-detail").assertCountEquals(1)
        snapshot.attributes.forEach { stat ->
            composeRule.onNodeWithTag("stats-attribute-${stat.id}").performScrollTo().assertIsDisplayed()
        }
        composeRule.onNodeWithTag("stats-attribute-perception").performScrollTo().performClick()
        composeRule.onNodeWithTag("stats-attribute-detail").performScrollTo().assertIsDisplayed()
        composeRule.onNodeWithText("Effective 41 • Base 40").assertIsDisplayed()
        composeRule.onNodeWithText("Signal ring: +1").assertIsDisplayed()
        saveScreenshot("stats-perception-detail")
    }

    @Test
    fun largeTextStillKeepsEveryAttributeInsidePhoneWidth() {
        composeRule.setContent {
            CompositionLocalProvider(LocalDensity provides Density(LocalDensity.current.density, 1.6f)) {
                PixelTheme { Box(Modifier.size(320.dp, 640.dp).background(PixelColors.Ink).testTag("qa-phone")) { StatsSection(snapshot) } }
            }
        }
        val viewport = composeRule.onNodeWithTag("qa-phone").fetchSemanticsNode().boundsInRoot
        snapshot.attributes.forEach { stat ->
            val bounds = composeRule.onNodeWithTag("stats-attribute-${stat.id}").performScrollTo().assertIsDisplayed().fetchSemanticsNode().boundsInRoot
            assertTrue(bounds.left >= viewport.left - 1 && bounds.right <= viewport.right + 1)
        }
    }
}
