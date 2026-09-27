package com.thegame.rpg.save

import android.content.Context
import com.thegame.rpg.boot.BootState
import com.thegame.rpg.engine.EngineStartException
import com.thegame.rpg.engine.GameEngine
import com.thegame.rpg.engine.GameSnapshot
import kotlinx.coroutines.runBlocking
import org.junit.Assert.assertArrayEquals
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Rule
import org.junit.Test
import org.junit.rules.TemporaryFolder

class SaveRepositoryTest {
    @get:Rule
    val temporaryFolder = TemporaryFolder()

    @Test
    fun missingSaveDoesNotCallEngineLoad() = runBlocking {
        val engine = FakeEngine()
        val saveFile = temporaryFolder.root.resolve("saves/slot-0.json")
        val repository = SaveRepository(saveFile, engine)

        val result = repository.continueGame()

        assertTrue(result is ContinueResult.Missing)
        assertEquals(0, engine.loadCalls)
        assertFalse(repository.hasSave())
    }

    @Test
    fun validSaveReturnsLoadedSnapshot() = runBlocking {
        val engine = FakeEngine(loadResult = Result.success(snapshot()))
        val saveFile = createSave("{\"schema_version\":1}")
        val repository = SaveRepository(saveFile, engine)

        val result = repository.continueGame()

        assertTrue(result is ContinueResult.Loaded)
        assertEquals("SCENE_SAVE", (result as ContinueResult.Loaded).snapshot.sceneId)
        assertEquals(1, engine.loadCalls)
        assertTrue(repository.hasSave())
    }

    @Test
    fun corruptSaveFailurePreservesOriginalBytes() = runBlocking {
        val failure = EngineStartException(
            stageId = "LOAD_ERROR",
            publicMessage = "The saved game could not be loaded.",
            technicalDetail = "invalid JSON",
        )
        val engine = FakeEngine(loadResult = Result.failure(failure))
        val saveFile = createSave("not-json")
        val before = saveFile.readBytes()
        val repository = SaveRepository(saveFile, engine)

        val result = repository.continueGame()

        assertTrue(result is ContinueResult.Failed)
        assertEquals("LOAD_ERROR", (result as ContinueResult.Failed).error.stageId)
        assertArrayEquals(before, saveFile.readBytes())
        assertTrue(saveFile.exists())
    }

    @Test
    fun unsupportedSchemaFailurePreservesOriginalBytes() = runBlocking {
        val failure = EngineStartException(
            stageId = "LOAD_ERROR",
            publicMessage = "The saved game could not be loaded.",
            technicalDetail = "unsupported schema_version 99",
        )
        val engine = FakeEngine(loadResult = Result.failure(failure))
        val saveFile = createSave("{\"schema_version\":99,\"scene_id\":\"SCENE_SAVE\"}")
        val before = saveFile.readBytes()
        val repository = SaveRepository(saveFile, engine)

        val result = repository.continueGame()

        assertTrue(result is ContinueResult.Failed)
        assertEquals("LOAD_ERROR", (result as ContinueResult.Failed).error.stageId)
        assertArrayEquals(before, saveFile.readBytes())
    }

    private fun createSave(text: String) = temporaryFolder.root.resolve("saves/slot-0.json").also {
        it.parentFile!!.mkdirs()
        it.writeText(text)
    }

    private fun snapshot() = GameSnapshot(
        sceneId = "SCENE_SAVE",
        title = "Saved Scene",
        body = "Recovered safely.",
        choices = emptyList(),
        resources = emptyList(),
        turn = 2,
        timeMinutes = 15,
        location = "CITY_GATE",
    )

    private class FakeEngine(
        private val loadResult: Result<GameSnapshot> = Result.failure(IllegalStateException("load should not be called")),
    ) : GameEngine {
        var loadCalls = 0

        override suspend fun start(context: Context, onStage: (BootState) -> Unit): Result<GameSnapshot> =
            Result.failure(UnsupportedOperationException("not used"))

        override suspend fun choose(choiceId: String): Result<GameSnapshot> =
            Result.failure(UnsupportedOperationException("not used"))

        override suspend fun save(): Result<Unit> = Result.success(Unit)

        override suspend fun load(): Result<GameSnapshot> {
            loadCalls += 1
            return loadResult
        }

        override suspend fun applyCheat(code: String): Result<GameSnapshot> =
            Result.failure(UnsupportedOperationException("not used"))
    }
}
