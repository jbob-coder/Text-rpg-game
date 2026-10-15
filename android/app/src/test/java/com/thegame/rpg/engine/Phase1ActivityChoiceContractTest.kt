package com.thegame.rpg.engine

import android.content.Context
import kotlinx.coroutines.runBlocking
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class Phase1ActivityChoiceContractTest {
    private companion object {
        const val ACTIVITY_ID = "TRAIN_POWER_FUNDAMENTALS_TWO_HOURS"
    }

    @Test
    fun `authored Phase 1 activity choice maps and forwards unchanged to Python gateway`() = runBlocking {
        var receivedChoiceId: String? = null
        val payload = mapOf(
            "scene" to mapOf(
                "id" to "TRACE_STABILIZATION_HUB",
                "title" to "Trace Echo Training Ledger",
                "body" to "Progress is measured in sessions, recovery, and reproducible results.",
                "choices" to listOf(
                    mapOf(
                        "id" to ACTIVITY_ID,
                        "text" to "Train two hours of controlled power fundamentals and measurement.",
                        "enabled" to true,
                    )
                ),
            ),
            "status" to mapOf(
                "resources" to listOf(
                    mapOf("id" to "stamina", "current" to 32.0, "max" to 100.0),
                    mapOf("id" to "focus", "current" to 24.0, "max" to 100.0),
                ),
            ),
            "meta" to mapOf(
                "turn" to 10,
                "time_minutes" to 180,
                "location" to "TRACE_CHAMBER",
            ),
        )
        val gateway = object : PythonSessionGateway {
            override fun start(
                context: Context,
                onContentLoading: () -> Unit,
            ): Map<String, Any?> = payload

            override fun choose(choiceId: String): Map<String, Any?> {
                receivedChoiceId = choiceId
                return payload
            }

            override fun save() = Unit
            override fun load(): Map<String, Any?> = payload
            override fun applyCheat(code: String): Map<String, Any?> = payload
            override fun equip(itemId: String): Map<String, Any?> = payload
            override fun unequip(slot: String): Map<String, Any?> = payload
            override fun travel(locationId: String): Map<String, Any?> = payload
            override fun inspectStatus(path: String): Map<String, Any?> = error("not used")
        }

        val result = PythonGameEngine(gateway).choose(ACTIVITY_ID)

        assertTrue(result.isSuccess)
        assertEquals(ACTIVITY_ID, receivedChoiceId)
        assertEquals(ACTIVITY_ID, result.getOrThrow().choices.single().id)
        assertEquals("TRACE_CHAMBER", result.getOrThrow().location)
    }
}
