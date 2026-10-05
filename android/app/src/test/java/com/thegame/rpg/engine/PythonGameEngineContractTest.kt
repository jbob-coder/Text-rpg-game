package com.thegame.rpg.engine

import com.thegame.rpg.boot.BootState
import kotlinx.coroutines.runBlocking
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class PythonGameEngineContractTest {
    @Test
    fun `generic startup failure maps to ENGINE_ERROR`() {
        val error = PythonGameEngine.classifyFailure(IllegalStateException("python exploded"))

        assertEquals("ENGINE_ERROR", error.stageId)
        assertTrue(error.publicMessage.isNotBlank())
        assertTrue(error.technicalDetail.contains("python exploded"))
    }

    @Test
    fun `content bridge failure maps to CONTENT_ERROR`() {
        val error = PythonGameEngine.classifyFailure(
            IllegalStateException("CONTENT_ERROR: Game content could not be loaded.")
        )

        assertEquals("CONTENT_ERROR", error.stageId)
        assertTrue(error.publicMessage.isNotBlank())
    }

    @Test
    fun `stat inspection bridge failure maps to STAT_INSPECTION_ERROR`() {
        val error = PythonGameEngine.classifyFailure(
            IllegalStateException("STAT_INSPECTION_ERROR: That stat cannot be inspected.")
        )

        assertEquals("STAT_INSPECTION_ERROR", error.stageId)
        assertEquals("That stat could not be inspected.", error.publicMessage)
    }

    @Test
    fun `safe bridge payload maps to snapshot and ignores unknown fields`() {
        val payload = mapOf(
            "scene" to mapOf(
                "id" to "SCENE_START",
                "title" to "Arrival",
                "body" to "The city gate is open.",
                "choices" to listOf(
                    mapOf(
                        "id" to "CHOICE_ENTER",
                        "text" to "Enter the city.",
                        "enabled" to true,
                        "disabled_reason" to null,
                        "secret_authoring_data" to "must not escape",
                    )
                ),
                "raw_outcomes" to mapOf("secret" to true),
            ),
            "status" to mapOf(
                "resources" to listOf(
                    mapOf("id" to "health", "current" to 10.0, "max" to 12.0)
                ),
                "hidden_modifier_source" to "redacted",
            ),
            "meta" to mapOf(
                "turn" to 3,
                "time_minutes" to 45,
                "location" to "CITY_GATE",
            ),
            "unknown_root" to "drop me",
        )

        val snapshot = PlayerSafeSnapshotMapper.fromMap(payload)

        assertEquals("SCENE_START", snapshot.sceneId)
        assertEquals("Arrival", snapshot.title)
        assertEquals("The city gate is open.", snapshot.body)
        assertEquals("CITY_GATE", snapshot.location)
        assertEquals(3, snapshot.turn)
        assertEquals(45, snapshot.timeMinutes)
        assertEquals(1, snapshot.choices.size)
        assertEquals("CHOICE_ENTER", snapshot.choices.single().id)
        assertTrue(snapshot.choices.single().enabled)
        assertEquals(1, snapshot.resources.size)
        assertEquals("health", snapshot.resources.single().id)
        assertEquals(10.0, snapshot.resources.single().current, 0.0)
        assertEquals(12.0, snapshot.resources.single().max, 0.0)
        assertFalse(snapshot.toString().contains("secret_authoring_data"))
        assertFalse(snapshot.toString().contains("raw_outcomes"))
        assertFalse(snapshot.toString().contains("hidden_modifier_source"))
    }

    @Test(expected = IllegalArgumentException::class)
    fun `production snapshot boundary rejects room location mismatch`() {
        val payload = mapOf(
            "scene" to mapOf(
                "id" to "SCENE_START",
                "title" to "Arrival",
                "body" to "The city gate is open.",
                "choices" to emptyList<Any>(),
            ),
            "status" to mapOf("resources" to emptyList<Any>()),
            "room" to mapOf(
                "projection_version" to 1,
                "location_id" to "SERVICE_TUNNEL",
                "actors" to emptyList<Any>(),
                "active_speaker_presentation_id" to null,
            ),
            "meta" to mapOf(
                "turn" to 0,
                "time_minutes" to 0,
                "location" to "PLATFORM_NINE",
            ),
        )

        PlayerSafeSnapshotMapper.fromMap(payload)
    }


    @Test
    fun `engine choose enforces player safe room invariants`() = runBlocking {
        val mismatchedPayload = mapOf(
            "scene" to mapOf(
                "id" to "SCENE_START",
                "title" to "Arrival",
                "body" to "The city gate is open.",
                "choices" to emptyList<Any>(),
            ),
            "status" to mapOf("resources" to emptyList<Any>()),
            "room" to mapOf(
                "projection_version" to 1,
                "location_id" to "SERVICE_TUNNEL",
                "actors" to emptyList<Any>(),
                "active_speaker_presentation_id" to null,
            ),
            "meta" to mapOf(
                "turn" to 0,
                "time_minutes" to 0,
                "location" to "PLATFORM_NINE",
            ),
        )

        val gateway = object : PythonSessionGateway {
            override fun start(
                context: android.content.Context,
                onContentLoading: () -> Unit,
            ): Map<String, Any?> = mismatchedPayload

            override fun choose(choiceId: String): Map<String, Any?> = mismatchedPayload
            override fun save() = Unit
            override fun load(): Map<String, Any?> = mismatchedPayload
            override fun applyCheat(code: String): Map<String, Any?> = mismatchedPayload
            override fun equip(itemId: String): Map<String, Any?> = mismatchedPayload
            override fun unequip(slot: String): Map<String, Any?> = mismatchedPayload
            override fun travel(locationId: String): Map<String, Any?> = mismatchedPayload
            override fun inspectStatus(path: String): Map<String, Any?> = error("not used")
        }

        val result = PythonGameEngine(gateway).choose("CHOICE_TEST")

        assertTrue(result.isFailure)
        val failure = result.exceptionOrNull()
        assertTrue(failure is EngineStartException)
        assertEquals("PROJECTION_ERROR", (failure as EngineStartException).stageId)
        assertEquals("The current game state could not be displayed.", failure.publicMessage)
    }

    @Test
    fun `activity choice delegates exact id and maps authoritative progress`() = runBlocking {
        var requestedChoice: String? = null
        val progressedPayload = mapOf(
            "scene" to mapOf(
                "id" to "TRACE_STABILIZATION_HUB",
                "title" to "Trace Echo Training Ledger",
                "body" to "Training remains authoritative in Python.",
                "choices" to listOf(
                    mapOf(
                        "id" to "TRAIN_POWER_FUNDAMENTALS_TWO_HOURS",
                        "text" to "Train two hours of controlled power fundamentals and measurement.",
                        "enabled" to true,
                    )
                ),
            ),
            "status" to mapOf(
                "resources" to listOf(
                    mapOf("id" to "stamina", "current" to 50.0, "max" to 70.0),
                    mapOf("id" to "focus", "current" to 44.0, "max" to 60.0),
                ),
                "skills" to mapOf(
                    "power" to listOf(
                        mapOf(
                            "id" to "powers",
                            "name" to "Powers",
                            "base" to 2.0,
                            "effective" to 2.0,
                            "delta" to 0.0,
                            "modified" to false,
                            "contributions" to emptyList<Any>(),
                        )
                    )
                ),
            ),
            "meta" to mapOf(
                "turn" to 12,
                "time_minutes" to 777,
                "location" to "TRACE_CHAMBER",
            ),
        )
        val gateway = object : PythonSessionGateway {
            override fun start(
                context: android.content.Context,
                onContentLoading: () -> Unit,
            ): Map<String, Any?> = progressedPayload

            override fun choose(choiceId: String): Map<String, Any?> {
                requestedChoice = choiceId
                return progressedPayload
            }

            override fun save() = Unit
            override fun load(): Map<String, Any?> = progressedPayload
            override fun applyCheat(code: String): Map<String, Any?> = progressedPayload
            override fun equip(itemId: String): Map<String, Any?> = progressedPayload
            override fun unequip(slot: String): Map<String, Any?> = progressedPayload
            override fun travel(locationId: String): Map<String, Any?> = progressedPayload
            override fun inspectStatus(path: String): Map<String, Any?> = error("not used")
        }

        val result = PythonGameEngine(gateway).choose("TRAIN_POWER_FUNDAMENTALS_TWO_HOURS")

        assertTrue(result.isSuccess)
        assertEquals("TRAIN_POWER_FUNDAMENTALS_TWO_HOURS", requestedChoice)
        val snapshot = result.getOrThrow()
        assertEquals(777, snapshot.timeMinutes)
        assertEquals("TRACE_CHAMBER", snapshot.location)
        assertEquals(50.0, snapshot.resources.single { it.id == "stamina" }.current, 0.0)
        assertEquals(44.0, snapshot.resources.single { it.id == "focus" }.current, 0.0)
        assertEquals(2.0, snapshot.skills.single { it.id == "powers" }.base, 0.0)
        assertEquals(2.0, snapshot.skills.single { it.id == "powers" }.effective, 0.0)
    }

    @Test
    fun `engine choose maps a valid player safe snapshot without recursion`() = runBlocking {
        val validPayload = mapOf(
            "scene" to mapOf(
                "id" to "SCENE_START",
                "title" to "Arrival",
                "body" to "The city gate is open.",
                "choices" to emptyList<Any>(),
            ),
            "status" to mapOf("resources" to emptyList<Any>()),
            "meta" to mapOf(
                "turn" to 1,
                "time_minutes" to 5,
                "location" to "CITY_GATE",
            ),
        )

        val gateway = object : PythonSessionGateway {
            override fun start(
                context: android.content.Context,
                onContentLoading: () -> Unit,
            ): Map<String, Any?> = validPayload
            override fun choose(choiceId: String): Map<String, Any?> = validPayload
            override fun save() = Unit
            override fun load(): Map<String, Any?> = validPayload
            override fun applyCheat(code: String): Map<String, Any?> = validPayload
            override fun equip(itemId: String): Map<String, Any?> = validPayload
            override fun unequip(slot: String): Map<String, Any?> = validPayload
            override fun travel(locationId: String): Map<String, Any?> = validPayload
            override fun inspectStatus(path: String): Map<String, Any?> = error("not used")
        }

        val result = PythonGameEngine(gateway).choose("CHOICE_TEST")

        assertTrue(result.isSuccess)
        val snapshot = result.getOrThrow()
        assertEquals("SCENE_START", snapshot.sceneId)
        assertEquals("CITY_GATE", snapshot.location)
        assertEquals(1, snapshot.turn)
        assertEquals(5, snapshot.timeMinutes)
    }

    @Test
    fun `engine startup exception converts to visible boot error`() {
        val failure = EngineStartException(
            stageId = "CONTENT_ERROR",
            publicMessage = "Content could not be loaded.",
            technicalDetail = "missing vertical_slice_01.json",
        )

        val boot = failure.toBootStateError()

        assertTrue(boot is BootState.Error)
        assertEquals("CONTENT_ERROR", boot.stageId)
        assertEquals("Content could not be loaded.", boot.publicMessage)
        assertEquals("missing vertical_slice_01.json", boot.technicalDetail)
    }
}
