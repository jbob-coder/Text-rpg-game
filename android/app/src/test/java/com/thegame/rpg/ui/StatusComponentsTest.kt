package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Test

class StatusComponentsTest {
    @Test
    fun fractionalStatBonusesRemainVisibleInsteadOfBeingRoundedAway() {
        assertEquals("35", statValue(35.0))
        assertEquals("35.25", statValue(35.25))
        assertEquals("+0.5", signedStatValue(0.5))
        assertEquals("-0.5", signedStatValue(-0.5))
        assertEquals("0", signedStatValue(0.0))
    }
}
