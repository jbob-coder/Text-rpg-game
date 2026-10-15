package com.thegame.rpg.ui

import androidx.compose.ui.test.assertHasClickAction
import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.junit4.createComposeRule
import androidx.compose.ui.test.onNodeWithTag
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.performClick
import androidx.compose.ui.test.performScrollTo
import com.thegame.rpg.engine.GameChoice
import com.thegame.rpg.engine.GameResource
import com.thegame.rpg.engine.GameSnapshot
import org.junit.Assert.assertEquals
import org.junit.Rule
import org.junit.Test

class Phase1ActivityChoiceTest {
    @get:Rule
    val composeRule = createComposeRule()

    @Test
    fun traceChamberTrainingIsPresentedAsEngineChoiceAndEmitsStableId() {
        val activityId = "TRAIN_POWER_FUNDAMENTALS_TWO_HOURS"
        var requestedChoice: String? = null
        val snapshot = GameSnapshot(
            sceneId = "TRACE_STABILIZATION_HUB",
            title = "Trace Echo Training Ledger",
            body = "Progress is measured in sessions, recovery, and reproducible results.",
            choices = listOf(
                GameChoice(
                    id = activityId,
                    text = "Train two hours of controlled power fundamentals and measurement.",
                    enabled = true,
                )
            ),
            resources = listOf(
                GameResource("stamina", 32.0, 100.0),
                GameResource("focus", 24.0, 100.0),
            ),
            turn = 10,
            timeMinutes = 180,
            location = "TRACE_CHAMBER",
        )

        composeRule.setContent {
            PixelTheme {
                GameScreen(
                    snapshot = snapshot,
                    busy = false,
                    onChoice = { requestedChoice = it },
                    onNavigate = {},
                )
            }
        }

        composeRule.onNodeWithText(
            "Train two hours of controlled power fundamentals and measurement."
        ).performScrollTo().assertIsDisplayed()
        composeRule.onNodeWithTag("choice-$activityId")
            .performScrollTo()
            .assertIsDisplayed()
            .assertHasClickAction()
            .performClick()

        composeRule.runOnIdle {
            assertEquals(activityId, requestedChoice)
        }
    }
}
