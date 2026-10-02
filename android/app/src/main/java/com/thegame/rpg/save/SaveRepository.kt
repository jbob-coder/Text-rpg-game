package com.thegame.rpg.save

import com.thegame.rpg.engine.EngineStartException
import com.thegame.rpg.engine.GameEngine
import com.thegame.rpg.engine.GameSnapshot
import com.thegame.rpg.engine.PythonGameEngine
import java.io.File

sealed interface ContinueResult {
    data object Missing : ContinueResult

    data class Loaded(
        val snapshot: GameSnapshot,
    ) : ContinueResult

    data class Failed(
        val error: EngineStartException,
    ) : ContinueResult
}

class SaveRepository(
    private val saveFile: File,
    private val engine: GameEngine,
) {
    fun hasSave(): Boolean = saveFile.isFile

    suspend fun continueGame(): ContinueResult {
        if (!hasSave()) {
            return ContinueResult.Missing
        }

        val before = try {
            saveFile.readBytes()
        } catch (failure: Throwable) {
            return ContinueResult.Failed(
                EngineStartException(
                    stageId = "LOAD_ERROR",
                    publicMessage = "The saved game could not be loaded.",
                    technicalDetail = failure.stackTraceToString(),
                    cause = failure,
                )
            )
        }

        return engine.load().fold(
            onSuccess = { snapshot ->
                ContinueResult.Loaded(snapshot)
            },
            onFailure = { failure ->
                // A failed load must never rewrite, migrate, rename, or delete the
                // user's only save. Verify that our boundary did not alter it.
                val after = runCatching { saveFile.readBytes() }.getOrNull()
                if (after == null || !before.contentEquals(after)) {
                    return@fold ContinueResult.Failed(
                        EngineStartException(
                            stageId = "LOAD_ERROR",
                            publicMessage = "The saved game could not be loaded safely.",
                            technicalDetail = "Save bytes changed during failed load; recovery is required.",
                            cause = failure,
                        )
                    )
                }

                val error = failure as? EngineStartException
                    ?: PythonGameEngine.classifyFailure(failure)
                ContinueResult.Failed(error)
            },
        )
    }
}
