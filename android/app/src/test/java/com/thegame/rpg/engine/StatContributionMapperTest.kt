package com.thegame.rpg.engine

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class StatContributionMapperTest {
    private fun payload(contributions: Any? = null): Map<String, Any?> = mapOf(
        "scene" to mapOf("id" to "SCENE", "title" to "Scene", "body" to "Body", "choices" to emptyList<Any>()),
        "status" to mapOf(
            "resources" to emptyList<Any>(),
            "attributes" to listOf(mapOf(
                "id" to "endurance", "name" to "Endurance", "base" to 35,
                "effective" to 37, "delta" to 2, "modified" to true, "contributions" to contributions,
            )),
            "skills" to mapOf("technical" to listOf(mapOf(
                "id" to "technical_systems", "name" to "Technical Systems", "base" to 25,
                "effective" to 26, "delta" to 1, "modified" to true,
                "contributions" to listOf(mapOf("kind" to "equipment", "label" to "Insulated work gloves", "value" to 1, "slot" to "hands")),
            ))),
        ),
        "meta" to mapOf("turn" to 0, "time_minutes" to 0, "location" to "PLATFORM_NINE"),
    )

    @Test
    fun finitePlayerSafeContributionsAreMappedWithoutCalculatingTotals() {
        val snapshot = BridgeSnapshotMapper.fromMap(payload(listOf(
            mapOf("kind" to "equipment", "label" to "Depot utility jacket", "value" to 2, "slot" to "body"),
            mapOf("kind" to "unidentified", "label" to "Unidentified modifier", "value" to -0.5),
        )))
        assertEquals("body", snapshot.attributes.single().contributions.first().slot)
        assertEquals(-0.5, snapshot.attributes.single().contributions.last().value, 0.0)
        // Totals are engine-owned; the mapper does not recompute them from display entries.
        assertEquals(37.0, snapshot.attributes.single().effective, 0.0)
        assertEquals("hands", snapshot.skills.single().contributions.single().slot)
    }

    @Test
    fun olderSnapshotsWithoutContributionsRemainCompatible() {
        assertTrue(BridgeSnapshotMapper.fromMap(payload()).attributes.single().contributions.isEmpty())
    }

    @Test
    fun malformedContributionKindsNumbersAndEquipmentSlotsAreRejected() {
        val valid = mapOf<String, Any?>("kind" to "equipment", "label" to "Jacket", "value" to 2, "slot" to "body")
        val malformed = listOf(
            valid + ("kind" to "raw_hidden_flag"),
            valid + ("value" to Double.NaN),
            valid + ("value" to Double.POSITIVE_INFINITY),
            valid + ("value" to true),
            valid + ("slot" to null),
            valid + ("kind" to "unidentified"),
        )
        malformed.forEach { entry ->
            assertTrue(runCatching { BridgeSnapshotMapper.fromMap(payload(listOf(entry))) }.exceptionOrNull() is IllegalArgumentException)
        }
    }
}
