package com.thegame.rpg

import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.hasClickAction
import androidx.compose.ui.test.hasText
import androidx.compose.ui.test.junit4.createAndroidComposeRule
import androidx.compose.ui.test.onNodeWithTag
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.performClick
import androidx.compose.ui.test.performScrollTo
import org.junit.Rule
import org.junit.Test

class ActivityBootSmokeTest {
    @get:Rule
    val composeRule = createAndroidComposeRule<MainActivity>()

    private fun waitForText(text: String, timeoutMillis: Long = 60_000) {
        composeRule.waitUntil(timeoutMillis = timeoutMillis) {
            composeRule.onAllNodes(hasText(text)).fetchSemanticsNodes().isNotEmpty()
        }
    }

    private fun waitForClickableText(text: String, timeoutMillis: Long = 30_000) {
        composeRule.waitUntil(timeoutMillis = timeoutMillis) {
            composeRule.onAllNodes(hasText(text) and hasClickAction())
                .fetchSemanticsNodes()
                .isNotEmpty()
        }
    }

    private fun scrollToChoiceAndClick(choiceId: String, timeoutMillis: Long = 30_000) {
        composeRule.waitUntil(timeoutMillis = timeoutMillis) {
            composeRule.onAllNodes(
                androidx.compose.ui.test.hasTestTag("choice-$choiceId")
            ).fetchSemanticsNodes().isNotEmpty()
        }
        composeRule.onNodeWithTag("choice-$choiceId")
            .performScrollTo()
            .assertIsDisplayed()
            .performClick()
    }

    @Test
    fun realActivityBootsAndAppliesFirstPythonChoice() {
        composeRule.waitUntil(timeoutMillis = 60_000) {
            composeRule.onAllNodes(
                androidx.compose.ui.test.hasTestTag("player-avatar")
            ).fetchSemanticsNodes().isNotEmpty()
        }

        composeRule.onNodeWithTag("player-avatar").assertIsDisplayed()
        composeRule.onNodeWithTag("scene-illustration").assertIsDisplayed()
        scrollToChoiceAndClick("TAKE_DEAD_RELAY")

        waitForText("A Case That Should Be Empty", timeoutMillis = 30_000)

        composeRule.onNodeWithText("A Case That Should Be Empty").assertIsDisplayed()
        composeRule.onNodeWithTag("choice-USE_MAINTENANCE_SEAL").assertIsDisplayed()
    }

    @Test
    fun realActivitySaveLoadRoundTripRestoresPythonScene() {
        composeRule.waitUntil(timeoutMillis = 60_000) {
            composeRule.onAllNodes(
                androidx.compose.ui.test.hasTestTag("choice-TAKE_DEAD_RELAY")
            ).fetchSemanticsNodes().isNotEmpty()
        }

        scrollToChoiceAndClick("TAKE_DEAD_RELAY")
        waitForText("A Case That Should Be Empty", timeoutMillis = 30_000)

        waitForClickableText("SETTINGS")
        composeRule.onNodeWithText("SETTINGS").performClick()
        waitForClickableText("SAVE GAME")
        composeRule.onNodeWithText("SAVE GAME").performClick()

        // Saving is asynchronous. The Close action remains present while the
        // ViewModel completes the Python persistence call, so wait for Compose
        // to settle before returning to the story and attempting another choice.
        composeRule.waitForIdle()
        composeRule.onNodeWithText("CLOSE").performClick()
        waitForClickableText("Use the maintenance seal to open the casing without damaging it.")
        scrollToChoiceAndClick("USE_MAINTENANCE_SEAL")
        waitForText("Gate Twelve", timeoutMillis = 30_000)

        composeRule.onNodeWithText("SETTINGS").performClick()
        waitForClickableText("LOAD / CONTINUE")
        composeRule.onNodeWithText("LOAD / CONTINUE").performClick()

        waitForText("A Case That Should Be Empty", timeoutMillis = 30_000)
        composeRule.onNodeWithTag("choice-USE_MAINTENANCE_SEAL").assertIsDisplayed()
    }
}
