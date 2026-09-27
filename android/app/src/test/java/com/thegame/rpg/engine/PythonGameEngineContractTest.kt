package com.thegame.rpg.engine

import com.thegame.rpg.boot.BootState
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

        val snapshot = BridgeSnapshotMapper.fromMap(payload)

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
