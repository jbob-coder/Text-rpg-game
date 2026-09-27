package com.thegame.rpg.ui

import androidx.compose.ui.test.assert
import androidx.compose.ui.test.assertHasClickAction
import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.hasScrollAction
import androidx.compose.ui.test.junit4.createComposeRule
import androidx.compose.ui.test.onNodeWithTag
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.performClick
import androidx.compose.ui.test.performScrollTo
import com.thegame.rpg.engine.GameChoice
import com.thegame.rpg.engine.GameEquipmentSlot
import com.thegame.rpg.engine.GameInventory
import com.thegame.rpg.engine.GameResource
import com.thegame.rpg.engine.GameMapNode
import com.thegame.rpg.engine.GameWorldMap
import com.thegame.rpg.engine.GameSnapshot
import org.junit.Rule
import org.junit.Test

class GameScreenTest {
    @get:Rule
    val composeRule = createComposeRule()

    private val snapshot = GameSnapshot(
        sceneId = "SCENE_GATE",
        title = "City Gate",
        body = "Rain needles the old stone while the gate guards watch every traveler.",
        choices = listOf(
            GameChoice("ENTER", "Enter the city", true),
            GameChoice("WAIT", "Wait beneath the arch", true),
        ),
        resources = listOf(
            GameResource("health", 10.0, 12.0),
            GameResource("stamina", 8.0, 10.0),
        ),
        turn = 3,
        timeMinutes = 45,
        location = "CITY_GATE",
    )

    @Test
    fun gameplayShellShowsScrollableNarrativeChoicesAvatarAndNavigation() {
        composeRule.setContent {
            PixelTheme {
                GameScreen(
                    snapshot = snapshot,
                    busy = false,
                    onChoice = {},
                    onNavigate = {},
                )
            }
        }

        composeRule.onNodeWithTag("narrative-scroll")
            .assertIsDisplayed()
            .assert(hasScrollAction())
        composeRule.onNodeWithText(snapshot.body).assertIsDisplayed()
        composeRule.onNodeWithTag("player-avatar").assertIsDisplayed()

        snapshot.choices.forEach { choice ->
            composeRule.onNodeWithTag("choice-${choice.id}")
                .assertIsDisplayed()
                .assertHasClickAction()
        }

        listOf("Stats", "Inventory", "Quests", "Map", "More").forEach { label ->
            composeRule.onNodeWithText(label).assertIsDisplayed().assertHasClickAction()
        }
    }

    @Test
    fun mapSectionExposesReachableAuthoredNodeAndTravelAction() {
        val mapSnapshot = snapshot.copy(
            location = "DISTRICT_PLAZA",
            worldMap = GameWorldMap(
                title = "Gate Twelve District",
                currentLocation = "DISTRICT_PLAZA",
                nodes = listOf(
                    GameMapNode(
                        id = "DISTRICT_PLAZA",
                        title = "Depot Plaza",
                        description = "Current location",
                        x = 48.0,
                        y = 18.0,
                        current = true,
                        reachable = true,
                    ),
                    GameMapNode(
                        id = "DISTRICT_ARCHIVE",
                        title = "Municipal Archive",
                        description = "Public records annex",
                        x = 66.0,
                        y = 16.0,
                        current = false,
                        reachable = true,
                    ),
                ),
            ),
        )

        composeRule.setContent {
            PixelTheme {
                GameScreen(
                    snapshot = mapSnapshot,
                    busy = false,
                    onChoice = {},
                    onNavigate = {},
                )
            }
        }

        composeRule.onNodeWithTag("nav-map")
            .performScrollTo()
            .assertIsDisplayed()
            .performClick()
        composeRule.onNodeWithTag("world-map-canvas").assertIsDisplayed()
        composeRule.onNodeWithTag("map-node-DISTRICT_ARCHIVE")
            .performScrollTo()
            .assertIsDisplayed()
            .performClick()
        composeRule.onNodeWithTag("map-travel")
            .performScrollTo()
            .assertIsDisplayed()
            .assertHasClickAction()
    }

    @Test
    fun equippedGearIsReflectedByTheVisibleAvatar() {
        val equippedSnapshot = snapshot.copy(
            inventory = GameInventory(
                equipment = listOf(
                    GameEquipmentSlot(
                        slot = "body",
                        equipped = true,
                        itemId = "ITEM_DEPOT_JACKET",
                        name = "Depot utility jacket",
                    ),
                    GameEquipmentSlot(
                        slot = "ring_1",
                        equipped = true,
                        itemId = "ITEM_SIGNAL_RING",
                        name = "Signal ring",
                    ),
                )
            )
        )

        composeRule.setContent {
            PixelTheme {
                GameScreen(
                    snapshot = equippedSnapshot,
                    busy = false,
                    onChoice = {},
                    onNavigate = {},
                )
            }
        }

        composeRule.onNodeWithTag("avatar-visible-gear").assertIsDisplayed()
        composeRule.onNodeWithText("VISIBLE GEAR // CHEST • RING I").assertIsDisplayed()
    }
}
