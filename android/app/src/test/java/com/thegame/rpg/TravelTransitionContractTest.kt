package com.thegame.rpg

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Test

class TravelTransitionContractTest {
    @Test
    fun transitionRequiresKnownOriginAndChangedConfirmedDestination() {
        assertNull(
            confirmedTravelTransition(
                fromLocation = null,
                toLocation = "DISTRICT_ARCHIVE",
                token = 1L,
            )
        )
        assertNull(
            confirmedTravelTransition(
                fromLocation = "DISTRICT_PLAZA",
                toLocation = "DISTRICT_PLAZA",
                token = 2L,
            )
        )

        val transition = confirmedTravelTransition(
            fromLocation = "DISTRICT_PLAZA",
            toLocation = "DISTRICT_ARCHIVE",
            token = 3L,
        )

        requireNotNull(transition)
        assertEquals(3L, transition.token)
        assertEquals("DISTRICT_PLAZA", transition.fromLocation)
        assertEquals("DISTRICT_ARCHIVE", transition.toLocation)
    }
}
