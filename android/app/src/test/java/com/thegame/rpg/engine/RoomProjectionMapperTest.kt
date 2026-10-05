package com.thegame.rpg.engine

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class RoomProjectionMapperTest {
    private fun basePayload(room: Map<String, Any?>? = null): Map<String, Any?> = mapOf(
        "scene" to mapOf("id" to "PLATFORM_NINE", "title" to "Platform Nine", "body" to "Test", "choices" to emptyList<Any>()),
        "status" to mapOf("resources" to emptyList<Any>()),
        "meta" to mapOf("turn" to 0, "time_minutes" to 0, "location" to "PLATFORM_NINE"),
        "room" to room,
    )

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

    @Test fun mapsVersionedPlayerSafeActorProjection() {
        val snapshot = BridgeSnapshotMapper.fromMap(basePayload(mapOf(
            "projection_version" to 1,
            "location_id" to "PLATFORM_NINE",
            "actors" to listOf(tamsin()),
            "active_speaker_presentation_id" to null,
        )))
        assertEquals(1, snapshot.room.projectionVersion)
        assertEquals("PLATFORM_NINE", snapshot.room.locationId)
        assertEquals("Tamsin", snapshot.room.actors.single().displayName)
        assertEquals("PLATFORM_NINE_TAMSIN_RIGHT", snapshot.room.actors.single().placementKey)
        assertTrue(snapshot.room.actors.single().inspectable)
    }

    @Test fun absentRoomIsMigrationCompatibleEmptyProjection() {
        val snapshot = BridgeSnapshotMapper.fromMap(basePayload())
        assertTrue(snapshot.room.actors.isEmpty())
    }

    @Test(expected = IllegalArgumentException::class) fun rejectsUnknownProjectionVersion() {
        BridgeSnapshotMapper.fromMap(basePayload(mapOf("projection_version" to 2, "location_id" to "PLATFORM_NINE", "actors" to emptyList<Any>())))
    }
}
