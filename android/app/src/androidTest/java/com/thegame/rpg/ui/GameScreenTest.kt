package com.thegame.rpg.ui

import androidx.compose.ui.test.assert
import androidx.compose.ui.test.assertHasClickAction
import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.hasScrollAction
import androidx.compose.ui.test.junit4.createComposeRule
import androidx.compose.ui.test.onNodeWithTag
import androidx.compose.ui.test.onNodeWithText
import com.thegame.rpg.engine.GameChoice
import com.thegame.rpg.engine.GameResource
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
}
