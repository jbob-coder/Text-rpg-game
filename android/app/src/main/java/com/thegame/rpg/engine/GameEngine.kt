package com.thegame.rpg.engine

import android.content.Context
import com.thegame.rpg.boot.BootState

data class GameChoice(
    val id: String,
    val text: String,
    val enabled: Boolean,
    val disabledReason: String? = null,
)

data class GameResource(
    val id: String,
    val current: Double,
    val max: Double,
)

data class GameSnapshot(
    val sceneId: String,
    val title: String,
    val body: String,
    val choices: List<GameChoice>,
    val resources: List<GameResource>,
    val turn: Int,
    val timeMinutes: Int,
    val location: String,
    val contentId: String? = null,
    val canonStatus: String? = null,
)

class EngineStartException(
    val stageId: String,
    val publicMessage: String,
    val technicalDetail: String,
    cause: Throwable? = null,
) : RuntimeException(publicMessage, cause) {
    fun toBootStateError(): BootState.Error = BootState.Error(
        stageId = stageId,
        publicMessage = publicMessage,
        technicalDetail = technicalDetail,
    )
}

internal class GatewayFailure(
    val stageId: String,
    val publicMessage: String,
    val technicalDetail: String,
    cause: Throwable? = null,
) : RuntimeException(publicMessage, cause)

interface GameEngine {
    suspend fun start(
        context: Context,
        onStage: (BootState) -> Unit = {},
    ): Result<GameSnapshot>

    suspend fun choose(choiceId: String): Result<GameSnapshot>

    suspend fun save(): Result<Unit>

    suspend fun load(): Result<GameSnapshot>
}

internal object BridgeSnapshotMapper {
    fun fromMap(payload: Map<String, Any?>): GameSnapshot {
        val scene = objectMap(payload["scene"], "scene")
        val status = objectMap(payload["status"], "status")
        val meta = objectMap(payload["meta"], "meta")

        val sceneId = text(scene["id"], "scene.id")
        val choices = list(scene["choices"], "scene.choices").mapIndexed { index, item ->
            val choice = objectMap(item, "scene.choices[$index]")
            GameChoice(
                id = text(choice["id"], "scene.choices[$index].id"),
                text = text(choice["text"], "scene.choices[$index].text"),
                enabled = boolean(choice["enabled"], "scene.choices[$index].enabled"),
                disabledReason = optionalText(choice["disabled_reason"]),
            )
        }

        val resources = list(status["resources"], "status.resources").mapIndexed { index, item ->
            val resource = objectMap(item, "status.resources[$index]")
            GameResource(
                id = text(resource["id"], "status.resources[$index].id"),
                current = number(resource["current"], "status.resources[$index].current"),
                max = number(resource["max"], "status.resources[$index].max"),
            )
        }

        return GameSnapshot(
            sceneId = sceneId,
            title = text(scene["title"], "scene.title"),
            body = text(scene["body"], "scene.body"),
            choices = choices,
            resources = resources,
            turn = integer(meta["turn"], "meta.turn"),
            timeMinutes = integer(meta["time_minutes"], "meta.time_minutes"),
            location = optionalText(meta["location"]) ?: sceneId,
            contentId = optionalText(meta["content_id"]),
            canonStatus = optionalText(meta["canon_status"]),
        )
    }

    @Suppress("UNCHECKED_CAST")
    private fun objectMap(value: Any?, label: String): Map<String, Any?> {
        if (value !is Map<*, *>) {
            throw IllegalArgumentException("$label must be an object")
        }
        val output = LinkedHashMap<String, Any?>()
        value.forEach { (key, item) ->
            if (key !is String) {
                throw IllegalArgumentException("$label keys must be text")
            }
            output[key] = item
        }
        return output
    }

    private fun list(value: Any?, label: String): List<*> {
        if (value !is List<*>) {
            throw IllegalArgumentException("$label must be a list")
        }
        return value
    }

    private fun text(value: Any?, label: String): String {
        if (value !is String || value.isBlank()) {
            throw IllegalArgumentException("$label must be non-empty text")
        }
        return value
    }

    private fun optionalText(value: Any?): String? = when (value) {
        null -> null
        is String -> value.takeIf { it.isNotBlank() }
        else -> throw IllegalArgumentException("optional text field has invalid type")
    }

    private fun boolean(value: Any?, label: String): Boolean {
        if (value !is Boolean) {
            throw IllegalArgumentException("$label must be boolean")
        }
        return value
    }

    private fun number(value: Any?, label: String): Double {
        if (value !is Number) {
            throw IllegalArgumentException("$label must be numeric")
        }
        val output = value.toDouble()
        if (!output.isFinite()) {
            throw IllegalArgumentException("$label must be finite")
        }
        return output
    }

    private fun integer(value: Any?, label: String): Int {
        if (value !is Number) {
            throw IllegalArgumentException("$label must be numeric")
        }
        val asLong = value.toLong()
        if (asLong < 0 || asLong > Int.MAX_VALUE || value.toDouble() != asLong.toDouble()) {
            throw IllegalArgumentException("$label must be a non-negative integer")
        }
        return asLong.toInt()
    }
}
