package com.thegame.rpg.ui

import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.assertHasClickAction
import androidx.compose.ui.test.junit4.createComposeRule
import androidx.compose.ui.test.onNodeWithTag
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.performClick
import androidx.compose.ui.test.performScrollTo
import com.thegame.rpg.engine.GameChoice
import com.thegame.rpg.engine.GameMapEdge
import com.thegame.rpg.engine.GameMapNode
import com.thegame.rpg.engine.GameResource
import com.thegame.rpg.engine.GameSnapshot
import com.thegame.rpg.engine.GameWorldMap
import org.junit.Assert.assertEquals
import org.junit.Rule
import org.junit.Test

class TextGameScreenTest {
    @get:Rule val composeRule = createComposeRule()

    private val snapshot = GameSnapshot(
        sceneId = "GATE", title = "Old Gate", body = "The guard waits for your answer.",
        choices = listOf(GameChoice("ENTER", "Enter the gate", true), GameChoice("WAIT", "Wait", false, "Not yet")),
        resources = listOf(GameResource("health", 10.0, 12.0)),
        turn = 1, timeMinutes = 30, location = "GATE",
        worldMap = GameWorldMap(
            title = "District",
            currentLocation = "GATE",
            nodes = listOf(
                GameMapNode("GATE", "Old Gate", "", 0.0, 0.0, true, true),
                GameMapNode("ARCHIVE", "Archive", "Records", 8.0, 4.0, false, true),
            ),
            edges = listOf(GameMapEdge("GATE", "ARCHIVE")),
        ),
    )

    @Test fun storyPresentsNarrationAndEnabledChoicesWithoutVisualAssets() {
        var chosen: String? = null
        composeRule.setContent {
            GameScreen(snapshot, busy = false, onChoice = { chosen = it }, onNavigate = {})
        }
        composeRule.onNodeWithTag("narrative-scroll").assertIsDisplayed()
        composeRule.onNodeWithText(snapshot.body).assertIsDisplayed()
        composeRule.onNodeWithTag("choice-ENTER").performScrollTo().assertHasClickAction().performClick()
        composeRule.runOnIdle { assertEquals("ENTER", chosen) }
    }

    @Test fun mapNavigationRemainsAvailableWithoutSprites() {
        var requested: String? = null
        composeRule.setContent {
            GameScreen(snapshot, busy = false, onChoice = {}, onNavigate = { requested = it })
        }
        composeRule.onNodeWithTag("nav-map").assertIsDisplayed().performClick()
        composeRule.runOnIdle { assertEquals("Map", requested) }
    }

    @Test fun mapDrawsRoutesAndRequestsOnlyReachableTravel() {
        var requested: String? = null
        composeRule.setContent {
            MapSection(snapshot, busy = false, onTravel = { requested = it })
        }
        composeRule.onNodeWithTag("world-map-canvas").assertIsDisplayed()
        composeRule.onNodeWithTag("map-node-ARCHIVE").performScrollTo().performClick()
        composeRule.onNodeWithTag("map-travel").performScrollTo().assertIsDisplayed().performClick()
        composeRule.runOnIdle { assertEquals("ARCHIVE", requested) }
    }
}
