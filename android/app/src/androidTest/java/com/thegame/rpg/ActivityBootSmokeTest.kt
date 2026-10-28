package com.thegame.rpg

import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.hasText
import androidx.compose.ui.test.hasTestTag
import androidx.compose.ui.test.junit4.createAndroidComposeRule
import androidx.compose.ui.test.onNodeWithTag
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.performClick
import androidx.compose.ui.test.performScrollTo
import org.junit.Rule
import org.junit.Test

/** Real Python/Chaquopy boot and text-only UI regression. */
class ActivityBootSmokeTest {
    @get:Rule val rule = createAndroidComposeRule<MainActivity>()

    private fun waitFor(text: String) {
        rule.waitUntil(timeoutMillis = 60_000) {
            rule.onAllNodes(hasText(text)).fetchSemanticsNodes().isNotEmpty()
        }
    }

    @Test fun engineStartsAndAcceptsAuthoredTextChoice() {
        rule.waitUntil(timeoutMillis = 60_000) { rule.onAllNodes(hasTestTag("choice-TAKE_DEAD_RELAY")).fetchSemanticsNodes().isNotEmpty() }
        rule.onNodeWithTag("choice-TAKE_DEAD_RELAY")
            .performScrollTo().assertIsDisplayed().performClick()
        waitFor("A Case That Should Be Empty")
        rule.onNodeWithText("A Case That Should Be Empty").assertIsDisplayed()
    }

    @Test fun mapNavigationAndTextOnlyTravelRemainFunctional() {
        waitFor("SETTINGS")
        rule.onNodeWithText("SETTINGS").performClick()
        rule.onNodeWithText("CHEAT // DISTRICT FREE ROAM").performScrollTo().performClick()
        waitFor("The District Opens Up")
        rule.onNodeWithTag("nav-map").performScrollTo().performClick()
        rule.onNodeWithTag("world-map-canvas").assertIsDisplayed()
        rule.onNodeWithTag("map-node-DISTRICT_ARCHIVE")
            .performScrollTo().performClick()
        rule.onNodeWithTag("map-travel").performScrollTo().performClick()
        waitFor("The Municipal Archive")
    }
}
