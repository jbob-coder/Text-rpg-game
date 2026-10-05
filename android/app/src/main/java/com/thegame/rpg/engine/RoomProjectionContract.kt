package com.thegame.rpg.engine

/** Cross-field invariants shared by player-safe room projection consumers. */
internal object RoomProjectionContract {
    fun validate(snapshotLocation: String, room: GameRoomProjection): GameRoomProjection {
        require(room.locationId == snapshotLocation) {
            "room.location_id must match meta.location"
        }

        val presentationIds = room.actors.map { it.presentationId }
        require(presentationIds.size == presentationIds.toSet().size) {
            "room.actors presentation_id values must be unique"
        }

        room.activeSpeakerPresentationId?.let { activeSpeaker ->
            require(activeSpeaker in presentationIds) {
                "room.active_speaker_presentation_id must reference a projected actor"
            }
        }
        return room
    }
}
