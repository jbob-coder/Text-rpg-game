package com.thegame.rpg.engine

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class RoomProjectionMapperTest {
    private fun basePayload(
        room: Map<String, Any?>? = null,
        location: String = "PLATFORM_NINE",
    ): Map<String, Any?> = mapOf(
        "scene" to mapOf("id" to "PLATFORM_NINE", "title" to "Platform Nine", "body" to "Test", "choices" to emptyList<Any>()),
        "status" to mapOf("resources" to emptyList<Any>()),
        "meta" to mapOf("turn" to 0, "time_minutes" to 0, "location" to location),
        "room" to room,
    )

    private fun tamsin(presentationId: String = "NPC_TAMSIN") = mapOf<String, Any?>(
        "presentation_id" to presentationId,
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

    private fun actor(presentationId: String = "NPC_TAMSIN") = GameRoomActor(
        presentationId = presentationId,
        knownActorId = "NPC_TAMSIN",
        displayName = "Tamsin",
        visualFamily = "NPC_TAMSIN",
        placementKey = "PLATFORM_NINE_TAMSIN_RIGHT",
        poseKey = "front",
        outfitKey = null,
        visibleTags = emptyList(),
        inspectable = true,
        dialogueAvailable = false,
        actions = emptyList(),
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

    @Test(expected = IllegalArgumentException::class) fun contractRejectsRoomLocationThatDoesNotMatchSnapshotLocation() {
        RoomProjectionContract.validate(
            "PLATFORM_NINE",
            GameRoomProjection(locationId = "SERVICE_TUNNEL"),
        )
    }

    @Test(expected = IllegalArgumentException::class) fun contractRejectsDuplicatePresentationIds() {
        RoomProjectionContract.validate(
            "PLATFORM_NINE",
            GameRoomProjection(locationId = "PLATFORM_NINE", actors = listOf(actor(), actor())),
        )
    }

    @Test(expected = IllegalArgumentException::class) fun contractRejectsActiveSpeakerOutsideProjectedActors() {
        RoomProjectionContract.validate(
            "PLATFORM_NINE",
            GameRoomProjection(
                locationId = "PLATFORM_NINE",
                actors = listOf(actor()),
                activeSpeakerPresentationId = "NPC_NOT_PROJECTED",
            ),
        )
    }
}
