package com.thegame.rpg.ui

import androidx.compose.foundation.layout.size
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.toPixelMap
import androidx.compose.ui.test.captureToImage
import androidx.compose.ui.test.junit4.createComposeRule
import androidx.compose.ui.test.onNodeWithTag
import androidx.compose.ui.unit.dp
import org.junit.Assert.assertTrue
import org.junit.Rule
import org.junit.Test

class SceneIllustrationAmbientAnimationTest {
    @get:Rule
    val composeRule = createComposeRule()

    @Test
    fun serviceTunnelAmbientLoopAdvancesWithoutStoryState() {
        composeRule.mainClock.autoAdvance = false
        try {
            composeRule.setContent {
                PixelTheme {
                    SceneIllustration(
                        locationId = "SERVICE_TUNNEL",
                        sceneId = null,
                        modifier = Modifier.size(256.dp, 128.dp),
                    )
                }
            }

            val before = composeRule.onNodeWithTag("scene-illustration")
                .captureToImage()
                .toPixelMap()

            composeRule.mainClock.advanceTimeBy(300L)
            composeRule.waitForIdle()

            val after = composeRule.onNodeWithTag("scene-illustration")
                .captureToImage()
                .toPixelMap()

            var changedPixels = 0
            for (y in 0 until before.height) {
                for (x in 0 until before.width) {
                    if (before[x, y] != after[x, y]) {
                        changedPixels += 1
                    }
                }
            }

            assertTrue(
                "Expected the Service Tunnel ambient loop to change visible pixels",
                changedPixels > 0,
            )
        } finally {
            composeRule.mainClock.autoAdvance = true
        }
    }
}
