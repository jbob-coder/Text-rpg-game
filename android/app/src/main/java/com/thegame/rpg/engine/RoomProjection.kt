package com.thegame.rpg.engine

data class GameRoomActor(
    val presentationId: String,
    val knownActorId: String? = null,
    val displayName: String,
    val visualFamily: String,
    val placementKey: String,
    val poseKey: String? = null,
    val outfitKey: String? = null,
    val visibleTags: List<String> = emptyList(),
    val inspectable: Boolean = false,
    val dialogueAvailable: Boolean = false,
)

data class GameRoom(
    val projectionVersion: Int = 1,
    val locationId: String = "",
    val actors: List<GameRoomActor> = emptyList(),
    val activeSpeakerPresentationId: String? = null,
)

internal object RoomProjectionMapper {
    fun fromMap(payload: Map<String, Any?>?, expectedLocation: String): GameRoom {
        require(expectedLocation.isNotBlank()) { "expected room location must be non-empty" }
        if (payload == null) return GameRoom(locationId = expectedLocation)
        val version = integer(payload["projection_version"], "room.projection_version")
        require(version == 1) { "room.projection_version is unsupported" }
        val location = text(payload["location_id"], "room.location_id")
        require(location == expectedLocation) { "room.location_id must match snapshot location" }
        val actors = list(payload["actors"], "room.actors").mapIndexed { index, raw ->
            val actor = objectMap(raw, "room.actors[$index]")
            val actions = optionalList(actor["actions"], "room.actors[$index].actions")
            require(actions.isEmpty()) { "room.actors[$index].actions is not supported in projection v1" }
            GameRoomActor(
                presentationId = text(actor["presentation_id"], "room.actors[$index].presentation_id"),
                knownActorId = optionalText(actor["known_actor_id"], "room.actors[$index].known_actor_id"),
                displayName = text(actor["display_name"], "room.actors[$index].display_name"),
                visualFamily = text(actor["visual_family"], "room.actors[$index].visual_family"),
                placementKey = text(actor["placement_key"], "room.actors[$index].placement_key"),
                poseKey = optionalText(actor["pose_key"], "room.actors[$index].pose_key"),
                outfitKey = optionalText(actor["outfit_key"], "room.actors[$index].outfit_key"),
                visibleTags = optionalList(actor["visible_tags"], "room.actors[$index].visible_tags").mapIndexed { tagIndex, tag -> text(tag, "room.actors[$index].visible_tags[$tagIndex]") },
                inspectable = optionalBoolean(actor["inspectable"], "room.actors[$index].inspectable") ?: false,
                dialogueAvailable = optionalBoolean(actor["dialogue_available"], "room.actors[$index].dialogue_available") ?: false,
            )
        }
        require(actors.map { it.presentationId }.toSet().size == actors.size) { "room.actors presentation_id values must be unique" }
        val speaker = optionalText(payload["active_speaker_presentation_id"], "room.active_speaker_presentation_id")
        require(speaker == null || actors.any { it.presentationId == speaker }) { "room.active_speaker_presentation_id must reference a projected actor" }
        return GameRoom(version, location, actors, speaker)
    }

    private fun objectMap(value: Any?, label: String): Map<String, Any?> {
        require(value is Map<*, *>) { "$label must be an object" }
        return value.entries.associate { (key, item) -> require(key is String) { "$label keys must be text" }; key to item }
    }
    private fun list(value: Any?, label: String): List<*> { require(value is List<*>) { "$label must be a list" }; return value }
    private fun optionalList(value: Any?, label: String): List<*> = if (value == null) emptyList<Any?>() else list(value, label)
    private fun text(value: Any?, label: String): String { require(value is String && value.isNotBlank()) { "$label must be non-empty text" }; return value }
    private fun optionalText(value: Any?, label: String): String? = when (value) { null -> null; is String -> value.takeIf { it.isNotBlank() } ?: throw IllegalArgumentException("$label must be non-empty text"); else -> throw IllegalArgumentException("$label must be text") }
    private fun integer(value: Any?, label: String): Int { require(value is Number) { "$label must be numeric" }; val long = value.toLong(); require(long >= 0 && long <= Int.MAX_VALUE && value.toDouble() == long.toDouble()) { "$label must be a non-negative integer" }; return long.toInt() }
    private fun optionalBoolean(value: Any?, label: String): Boolean? = when (value) { null -> null; is Boolean -> value; else -> throw IllegalArgumentException("$label must be boolean") }
}
