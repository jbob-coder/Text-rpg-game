package com.thegame.rpg

import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.junit4.createAndroidComposeRule
import androidx.compose.ui.test.onNodeWithTag
import org.junit.Rule
import org.junit.Test

class ActivityBootSmokeTest {
    @get:Rule
    val composeRule = createAndroidComposeRule<MainActivity>()

    @Test
    fun realActivityReachesPlayablePixelShell() {
        composeRule.waitUntil(timeoutMillis = 60_000) {
            composeRule.onAllNodes(
                androidx.compose.ui.test.hasTestTag("player-avatar")
            ).fetchSemanticsNodes().isNotEmpty()
        }

        composeRule.onNodeWithTag("player-avatar").assertIsDisplayed()
    }
}
