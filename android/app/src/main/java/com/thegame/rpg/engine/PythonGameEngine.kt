package com.thegame.rpg.engine

import android.content.Context
import com.chaquo.python.PyException
import com.chaquo.python.PyObject
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform
import com.thegame.rpg.boot.BootState
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import org.json.JSONArray
import org.json.JSONObject
import java.io.File

class PythonGameEngine internal constructor(
    private val gateway: PythonSessionGateway,
) : GameEngine {
    constructor() : this(ChaquopySessionGateway())
    override suspend fun start(
        context: Context,
        onStage: (BootState) -> Unit,
    ): Result<GameSnapshot> {
        onStage(BootState.PythonStarting)
        return withContext(Dispatchers.IO) {
            try {
                val payload = gateway.start(context.applicationContext) {
                    onStage(BootState.ContentLoading)
                }
                Result.success(BridgeSnapshotMapper.fromMap(payload))
            } catch (failure: Throwable) {
                Result.failure(classifyFailure(failure))
            }
        }
    }

    override suspend fun choose(choiceId: String): Result<GameSnapshot> =
        withContext(Dispatchers.IO) {
            try {
                Result.success(BridgeSnapshotMapper.fromMap(gateway.choose(choiceId)))
            } catch (failure: Throwable) {
                Result.failure(classifyFailure(failure))
            }
        }

    override suspend fun save(): Result<Unit> = withContext(Dispatchers.IO) {
        try {
            gateway.save()
            Result.success(Unit)
        } catch (failure: Throwable) {
            Result.failure(classifyFailure(failure))
        }
    }

    override suspend fun load(): Result<GameSnapshot> = withContext(Dispatchers.IO) {
        try {
            Result.success(BridgeSnapshotMapper.fromMap(gateway.load()))
        } catch (failure: Throwable) {
            Result.failure(classifyFailure(failure))
        }
    }

    companion object {
        private val knownCodes = listOf(
            "CONTENT_ERROR",
            "VIEW_ERROR",
            "PROJECTION_ERROR",
            "LOAD_ERROR",
            "SAVE_ERROR",
            "SAVE_PATH_REQUIRED",
            "CHOICE_ERROR",
            "ENGINE_ERROR",
        )

        fun classifyFailure(failure: Throwable): EngineStartException {
            if (failure is EngineStartException) return failure
            if (failure is GatewayFailure) {
                return EngineStartException(
                    stageId = failure.stageId,
                    publicMessage = failure.publicMessage,
                    technicalDetail = failure.technicalDetail,
                    cause = failure,
                )
            }

            val detail = failure.stackTraceToString()
            val message = failure.message.orEmpty()
            val code = knownCodes.firstOrNull { message.contains(it) } ?: "ENGINE_ERROR"
            val publicMessage = when (code) {
                "CONTENT_ERROR" -> "Game content could not be loaded."
                "VIEW_ERROR", "PROJECTION_ERROR" -> "The current game state could not be displayed."
                "LOAD_ERROR" -> "The saved game could not be loaded."
                "SAVE_ERROR", "SAVE_PATH_REQUIRED" -> "The game could not be saved."
                "CHOICE_ERROR" -> "That choice is not available."
                else -> "The game engine could not start."
            }
            return EngineStartException(
                stageId = code,
                publicMessage = publicMessage,
                technicalDetail = detail,
                cause = failure,
            )
        }
    }
}

internal interface PythonSessionGateway {
    fun start(context: Context, onContentLoading: () -> Unit): Map<String, Any?>
    fun choose(choiceId: String): Map<String, Any?>
    fun save()
    fun load(): Map<String, Any?>
}

private class ChaquopySessionGateway : PythonSessionGateway {
    private var session: PyObject? = null
    private var jsonModule: PyObject? = null

    override fun start(
        context: Context,
        onContentLoading: () -> Unit,
    ): Map<String, Any?> {
        try {
            if (!Python.isStarted()) {
                val platform = AndroidPlatform(context)
                platform.redirectStdioToLogcat()
                Python.start(platform)
            }
        } catch (failure: Throwable) {
            throw GatewayFailure(
                stageId = "ENGINE_ERROR",
                publicMessage = "The game engine could not start.",
                technicalDetail = failure.stackTraceToString(),
                cause = failure,
            )
        }

        onContentLoading()

        val contentFile = try {
            installContent(context)
        } catch (failure: Throwable) {
            throw GatewayFailure(
                stageId = "CONTENT_ERROR",
                publicMessage = "Game content could not be loaded.",
                technicalDetail = failure.stackTraceToString(),
                cause = failure,
            )
        }

        val saveFile = File(context.filesDir, "saves/slot-0.json")
        try {
            val python = Python.getInstance()
            val bridge = python.getModule("textrpg.android_bridge")
            jsonModule = python.getModule("json")
            session = bridge.callAttr(
                "create_session",
                contentFile.absolutePath,
                saveFile.absolutePath,
            )
            return viewToMap(requireSession().callAttr("scene_view"))
        } catch (failure: Throwable) {
            throw classifyPythonBoundaryFailure(
                failure = failure,
                fallbackCode = "CONTENT_ERROR",
                fallbackMessage = "Game content could not be loaded.",
            )
        }
    }

    override fun choose(choiceId: String): Map<String, Any?> {
        try {
            return viewToMap(requireSession().callAttr("choose", choiceId))
        } catch (failure: Throwable) {
            throw classifyPythonBoundaryFailure(
                failure = failure,
                fallbackCode = "CHOICE_ERROR",
                fallbackMessage = "That choice is not available.",
            )
        }
    }

    override fun save() {
        try {
            requireSession().callAttr("save")
        } catch (failure: Throwable) {
            throw classifyPythonBoundaryFailure(
                failure = failure,
                fallbackCode = "SAVE_ERROR",
                fallbackMessage = "The game could not be saved.",
            )
        }
    }

    override fun load(): Map<String, Any?> {
        try {
            return viewToMap(requireSession().callAttr("load"))
        } catch (failure: Throwable) {
            throw classifyPythonBoundaryFailure(
                failure = failure,
                fallbackCode = "LOAD_ERROR",
                fallbackMessage = "The saved game could not be loaded.",
            )
        }
    }

    private fun requireSession(): PyObject =
        session ?: throw GatewayFailure(
            stageId = "ENGINE_ERROR",
            publicMessage = "The game engine is not ready.",
            technicalDetail = "Android requested a session operation before start completed.",
        )

    private fun installContent(context: Context): File {
        val directory = File(context.filesDir, "content")
        if (!directory.exists() && !directory.mkdirs()) {
            throw IllegalStateException("Could not create content directory: $directory")
        }

        val target = File(directory, "vertical_slice_01.json")
        val temp = File(directory, "vertical_slice_01.json.tmp")
        context.assets.open("vertical_slice_01.json").use { input ->
            temp.outputStream().use { output -> input.copyTo(output) }
        }
        if (target.exists() && !target.delete()) {
            temp.delete()
            throw IllegalStateException("Could not replace packaged content: $target")
        }
        if (!temp.renameTo(target)) {
            temp.copyTo(target, overwrite = true)
            temp.delete()
        }
        return target
    }

    private fun viewToMap(view: PyObject?): Map<String, Any?> {
        val nonNullView = view ?: throw GatewayFailure(
            stageId = "PROJECTION_ERROR",
            publicMessage = "The current game state could not be displayed.",
            technicalDetail = "Python returned None for a player-facing view.",
        )
        val json = jsonModule ?: throw GatewayFailure(
            stageId = "ENGINE_ERROR",
            publicMessage = "The game engine is not ready.",
            technicalDetail = "Python JSON module was not initialized.",
        )
        val raw = json.callAttr("dumps", nonNullView).toString()
        return jsonObjectToMap(JSONObject(raw))
    }

    private fun jsonObjectToMap(value: JSONObject): Map<String, Any?> {
        val output = LinkedHashMap<String, Any?>()
        val keys = value.keys()
        while (keys.hasNext()) {
            val key = keys.next()
            output[key] = jsonValue(value.get(key))
        }
        return output
    }

    private fun jsonArrayToList(value: JSONArray): List<Any?> =
        List(value.length()) { index -> jsonValue(value.get(index)) }

    private fun jsonValue(value: Any?): Any? = when (value) {
        null, JSONObject.NULL -> null
        is JSONObject -> jsonObjectToMap(value)
        is JSONArray -> jsonArrayToList(value)
        is String, is Boolean, is Number -> value
        else -> throw IllegalArgumentException("Unsupported JSON value: ${value::class.java.name}")
    }

    private fun classifyPythonBoundaryFailure(
        failure: Throwable,
        fallbackCode: String,
        fallbackMessage: String,
    ): GatewayFailure {
        if (failure is GatewayFailure) return failure
        val detail = failure.stackTraceToString()
        val message = when (failure) {
            is PyException -> failure.message.orEmpty()
            else -> failure.message.orEmpty()
        }
        val known = listOf(
            "CONTENT_ERROR",
            "VIEW_ERROR",
            "LOAD_ERROR",
            "SAVE_ERROR",
            "SAVE_PATH_REQUIRED",
            "CHOICE_ERROR",
        ).firstOrNull { message.contains(it) }

        val code = known ?: fallbackCode
        val public = when (code) {
            "CONTENT_ERROR" -> "Game content could not be loaded."
            "VIEW_ERROR" -> "The current game state could not be displayed."
            "LOAD_ERROR" -> "The saved game could not be loaded."
            "SAVE_ERROR", "SAVE_PATH_REQUIRED" -> "The game could not be saved."
            "CHOICE_ERROR" -> "That choice is not available."
            else -> fallbackMessage
        }
        return GatewayFailure(code, public, detail, failure)
    }
}
