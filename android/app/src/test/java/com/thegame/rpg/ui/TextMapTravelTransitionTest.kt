package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Test

/** Pure-string route formatting; no frame generator or authored art dependency. */
class TextMapTravelTransitionTest {
    @Test
    fun transitionUsesReadableLocationNamesWithoutAssetCatalog() {
        assertEquals(
            "DISTRICT PLAZA → DISTRICT ARCHIVE",
            travelRouteLabel("DISTRICT_PLAZA", "DISTRICT_ARCHIVE"),
        )
    }

    @Test
    fun transitionDoesNotChangeOrInventDestination() {
        assertEquals("GATE TWELVE → SERVICE TUNNEL",
            travelRouteLabel("GATE_TWELVE", "SERVICE_TUNNEL"))
        assertEquals("A → A", travelRouteLabel("A", "A"))
    }
}
