package com.thegame.rpg.engine

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class RoomProjectionMapperTest {
    private fun tamsin() = mapOf<String, Any?>(
        "presentation_id" to "NPC_TAMSIN",
        "known_actor_id" to "NPC_TAMSIN",
        "display_name" to "Tamsin",
        "visual_family" to "NPC_TAMSIN",
        "placement_key" to "PLATFORM_NINE_TAMSIN_RIGHT",
        "pose_key" to "front",
        "visible_tags" to emptyList<String>(),
        "inspectable" to true,
        "dialogue_available" to false,
        "actions" to emptyList<String>(),
    )

    @Test
    fun mapsVersionedPlayerSafeActorProjection() {
        val room = RoomProjectionMapper.fromMap(
            mapOf(
                "projection_version" to 1,
                "location_id" to "PLATFORM_NINE",
                "actors" to listOf(tamsin()),
                "active_speaker_presentation_id" to null,
            ),
            "PLATFORM_NINE",
        )

        assertEquals(1, room.projectionVersion)
        assertEquals("PLATFORM_NINE", room.locationId)
        assertEquals("Tamsin", room.actors.single().displayName)
        assertEquals("PLATFORM_NINE_TAMSIN_RIGHT", room.actors.single().placementKey)
        assertTrue(room.actors.single().inspectable)
    }

    @Test
    fun absentRoomIsMigrationCompatibleEmptyProjection() {
        val room = RoomProjectionMapper.fromMap(null, "PLATFORM_NINE")
        assertEquals("PLATFORM_NINE", room.locationId)
        assertTrue(room.actors.isEmpty())
    }

    @Test(expected = IllegalArgumentException::class)
    fun rejectsRoomLocationMismatch() {
        RoomProjectionMapper.fromMap(
            mapOf(
                "projection_version" to 1,
                "location_id" to "SERVICE_TUNNEL",
                "actors" to emptyList<Any>(),
            ),
            "PLATFORM_NINE",
        )
    }

    @Test(expected = IllegalArgumentException::class)
    fun rejectsDuplicatePresentationIds() {
        RoomProjectionMapper.fromMap(
            mapOf(
                "projection_version" to 1,
                "location_id" to "PLATFORM_NINE",
                "actors" to listOf(tamsin(), tamsin()),
            ),
            "PLATFORM_NINE",
        )
    }

    @Test(expected = IllegalArgumentException::class)
    fun rejectsUnknownProjectionVersion() {
        RoomProjectionMapper.fromMap(
            mapOf(
                "projection_version" to 2,
                "location_id" to "PLATFORM_NINE",
                "actors" to emptyList<Any>(),
            ),
            "PLATFORM_NINE",
        )
    }
}
