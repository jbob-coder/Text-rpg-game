package com.thegame.rpg.engine

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class BridgeStatusMapperTest {
    @Test
    fun playerSafeStatsAreMappedForDedicatedStatsScreen() {
        val payload = mapOf(
            "scene" to mapOf(
                "id" to "SCENE",
                "title" to "Scene",
                "body" to "Body",
                "choices" to emptyList<Any>(),
            ),
            "status" to mapOf(
                "identity" to mapOf("name" to "Jack", "level" to 4),
                "resources" to listOf(mapOf("id" to "health", "current" to 88.0, "max" to 100.0)),
                "attributes" to listOf(
                    mapOf(
                        "id" to "might", "name" to "Might", "base" to 30.0,
                        "effective" to 35.0, "delta" to 5.0, "modified" to true,
                        "role" to "physical force",
                    )
                ),
                "derived" to listOf(mapOf("id" to "max_health", "name" to "Max Health", "value" to 100.0)),
                "skills" to mapOf(
                    "physical" to listOf(
                        mapOf(
                            "id" to "athletics", "name" to "Athletics", "base" to 20.0,
                            "effective" to 20.0, "delta" to 0.0, "modified" to false,
                        )
                    )
                ),
                "conditions" to emptyList<Any>(),
            ),
            "visuals" to mapOf("relay_state" to "damaged"),
            "meta" to mapOf("turn" to 0, "time_minutes" to 0, "location" to "CITY"),
        )

        val snapshot = BridgeSnapshotMapper.fromMap(payload)

        assertEquals("Jack", snapshot.identity.name)
        assertEquals(4, snapshot.identity.level)
        assertEquals(1, snapshot.attributes.size)
        assertEquals(35.0, snapshot.attributes.single().effective, 0.0)
        assertTrue(snapshot.attributes.single().modified)
        assertEquals("physical", snapshot.skills.single().category)
        assertEquals("max_health", snapshot.derived.single().id)
        assertEquals("damaged", snapshot.visuals.relayState)
    }
    @Test
    fun playerSafeStatInspectionMapsContributionSources() {
        val inspection = BridgeSnapshotMapper.statInspectionFromMap(
            mapOf(
                "path" to "attributes.endurance",
                "kind" to "attribute",
                "total" to 37.0,
                "breakdown" to mapOf(
                    "base" to 35.0,
                    "equipment:body" to 2.0,
                ),
            )
        )

        assertEquals("attributes.endurance", inspection.path)
        assertEquals("attribute", inspection.kind)
        assertEquals(37.0, inspection.total, 0.0)
        assertEquals(2, inspection.contributions.size)
        assertEquals("equipment:body", inspection.contributions[1].source)
        assertEquals(2.0, inspection.contributions[1].value, 0.0)
    }

    @Test
    fun unsupportedRelayVisualStateIsRejected() {
        val payload = mapOf(
            "scene" to mapOf(
                "id" to "SCENE",
                "title" to "Scene",
                "body" to "Body",
                "choices" to emptyList<Any>(),
            ),
            "status" to mapOf(
                "resources" to emptyList<Any>(),
            ),
            "visuals" to mapOf("relay_state" to "omniscient_future_state"),
            "meta" to mapOf("turn" to 0, "time_minutes" to 0, "location" to "CITY"),
        )

        val failure = runCatching { BridgeSnapshotMapper.fromMap(payload) }.exceptionOrNull()

        assertTrue(failure is IllegalArgumentException)
    }

}
