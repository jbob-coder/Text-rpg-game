package com.thegame.rpg

import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.junit4.createAndroidComposeRule
import androidx.compose.ui.test.onNodeWithTag
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.performClick
import org.junit.Rule
import org.junit.Test

class ActivityBootSmokeTest {
    @get:Rule
    val composeRule = createAndroidComposeRule<MainActivity>()

    @Test
    fun realActivityBootsAndAppliesFirstPythonChoice() {
        composeRule.waitUntil(timeoutMillis = 60_000) {
            composeRule.onAllNodes(
                androidx.compose.ui.test.hasTestTag("player-avatar")
            ).fetchSemanticsNodes().isNotEmpty()
        }

        composeRule.onNodeWithTag("player-avatar").assertIsDisplayed()
        composeRule.onNodeWithTag("scene-illustration").assertIsDisplayed()
        composeRule.onNodeWithTag("choice-TAKE_DEAD_RELAY")
            .assertIsDisplayed()
            .performClick()

        composeRule.waitUntil(timeoutMillis = 30_000) {
            composeRule.onAllNodes(
                androidx.compose.ui.test.hasText("A Case That Should Be Empty")
            ).fetchSemanticsNodes().isNotEmpty()
        }

        composeRule.onNodeWithText("A Case That Should Be Empty").assertIsDisplayed()
        composeRule.onNodeWithTag("choice-USE_MAINTENANCE_SEAL").assertIsDisplayed()
    }
}
