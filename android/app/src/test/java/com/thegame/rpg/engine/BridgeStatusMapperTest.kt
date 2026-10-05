package com.thegame.rpg.engine

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
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
        assertTrue(snapshot.abilities.isEmpty())
    }

    @Test
    fun playerSafeRoomProjectionMapsSemanticActorPlacement() {
        val payload = mapOf(
            "scene" to mapOf(
                "id" to "SCENE_GATE",
                "title" to "Gate Twelve",
                "body" to "Body",
                "choices" to emptyList<Any>(),
            ),
            "status" to mapOf("resources" to emptyList<Any>()),
            "room" to mapOf(
                "projection_version" to 1,
                "location_id" to "LOC_GATE_TWELVE",
                "actors" to listOf(
                    mapOf(
                        "presentation_id" to "PRES_TAMSIN_GATE",
                        "known_actor_id" to "NPC_TAMSIN",
                        "display_name" to "Tamsin",
                        "visual_family" to "gate_warden",
                        "placement_key" to "right_guard_post",
                        "pose_key" to "watchful",
                        "outfit_key" to "gate_uniform",
                        "visible_tags" to listOf("guard"),
                        "inspectable" to true,
                        "dialogue_available" to true,
                        "actions" to listOf("talk"),
                    )
                ),
                "active_speaker_presentation_id" to null,
            ),
            "meta" to mapOf("turn" to 0, "time_minutes" to 0, "location" to "LOC_GATE_TWELVE"),
        )

        val snapshot = BridgeSnapshotMapper.fromMap(payload)
        val actor = snapshot.room.actors.single()

        assertEquals(1, snapshot.room.projectionVersion)
        assertEquals("LOC_GATE_TWELVE", snapshot.room.locationId)
        assertEquals("PRES_TAMSIN_GATE", actor.presentationId)
        assertEquals("NPC_TAMSIN", actor.knownActorId)
        assertEquals("Tamsin", actor.displayName)
        assertEquals("right_guard_post", actor.placementKey)
        assertEquals(listOf("guard"), actor.visibleTags)
        assertEquals(listOf("talk"), actor.actions)
        assertTrue(actor.inspectable)
        assertTrue(actor.dialogueAvailable)
        assertNull(snapshot.room.activeSpeakerPresentationId)
    }

    @Test
    fun unsupportedRoomProjectionVersionIsRejected() {
        val payload = mapOf(
            "scene" to mapOf(
                "id" to "SCENE_GATE",
                "title" to "Gate Twelve",
                "body" to "Body",
                "choices" to emptyList<Any>(),
            ),
            "status" to mapOf("resources" to emptyList<Any>()),
            "room" to mapOf(
                "projection_version" to 2,
                "location_id" to "LOC_GATE_TWELVE",
                "actors" to emptyList<Any>(),
                "active_speaker_presentation_id" to null,
            ),
            "meta" to mapOf("turn" to 0, "time_minutes" to 0, "location" to "LOC_GATE_TWELVE"),
        )

        val failure = runCatching { BridgeSnapshotMapper.fromMap(payload) }.exceptionOrNull()

        assertTrue(failure is IllegalArgumentException)
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

    @Test
    fun playerSafeAbilityProgressionMapsIntoTypedSnapshot() {
        val payload = mapOf(
            "scene" to mapOf(
                "id" to "SCENE",
                "title" to "Scene",
                "body" to "Body",
                "choices" to emptyList<Any>(),
            ),
            "status" to mapOf(
                "resources" to emptyList<Any>(),
                "abilities" to listOf(
                    mapOf(
                        "id" to "ABILITY_TRACE_ECHO",
                        "name" to "Trace Echo",
                        "rank" to 0,
                        "mastery_stage" to "discovered",
                        "mastery_xp" to 2.8,
                        "form" to "latent_trace",
                        "state" to "ready",
                        "resource" to mapOf(
                            "label" to "Trace Resonance",
                            "current" to 10.0,
                            "max" to 10.0,
                            "recovery_per_hour" to 2.0,
                        ),
                        "techniques" to listOf(
                            mapOf(
                                "technique_id" to "TECHNIQUE_SIGNAL_PULSE",
                                "name" to "Signal Pulse",
                                "stage" to "discovered",
                                "mastery_xp" to 8.0,
                                "uses" to 0,
                                "ready" to true,
                                "cooldown_remaining_minutes" to 0,
                            )
                        ),
                        "completed_evolutions" to emptyList<String>(),
                    )
                ),
            ),
            "meta" to mapOf("turn" to 7, "time_minutes" to 60, "location" to "TRACE_CHAMBER"),
        )

        val ability = BridgeSnapshotMapper.fromMap(payload).abilities.single()

        assertEquals("ABILITY_TRACE_ECHO", ability.id)
        assertEquals("Trace Echo", ability.name)
        assertEquals(2.8, ability.masteryXp, 0.0)
        assertEquals(10.0, ability.resource?.current ?: -1.0, 0.0)
        assertEquals("TECHNIQUE_SIGNAL_PULSE", ability.techniques.single().id)
        assertEquals(8.0, ability.techniques.single().masteryXp, 0.0)
    }

    @Test
    fun malformedAbilityProgressionIsRejected() {
        val payload = mapOf(
            "scene" to mapOf(
                "id" to "SCENE",
                "title" to "Scene",
                "body" to "Body",
                "choices" to emptyList<Any>(),
            ),
            "status" to mapOf(
                "resources" to emptyList<Any>(),
                "abilities" to listOf(
                    mapOf(
                        "id" to "ABILITY_TRACE_ECHO",
                        "name" to "Trace Echo",
                        "rank" to 0,
                        "mastery_stage" to "discovered",
                        "mastery_xp" to -1.0,
                        "state" to "ready",
                    )
                ),
            ),
            "meta" to mapOf("turn" to 0, "time_minutes" to 0, "location" to "CITY"),
        )

        val failure = runCatching { BridgeSnapshotMapper.fromMap(payload) }.exceptionOrNull()

        assertTrue(failure is IllegalArgumentException)
    }

    @Test
    fun authoredAbilityRequirementsCannotCrossTypedBridge() {
        val payload = mapOf(
            "scene" to mapOf(
                "id" to "SCENE",
                "title" to "Scene",
                "body" to "Body",
                "choices" to emptyList<Any>(),
            ),
            "status" to mapOf(
                "resources" to emptyList<Any>(),
                "abilities" to listOf(
                    mapOf(
                        "id" to "ABILITY_TRACE_ECHO",
                        "name" to "Trace Echo",
                        "rank" to 0,
                        "mastery_stage" to "discovered",
                        "mastery_xp" to 0.0,
                        "state" to "ready",
                        "requirements" to mapOf("secret" to true),
                    )
                ),
            ),
            "meta" to mapOf("turn" to 0, "time_minutes" to 0, "location" to "CITY"),
        )

        val failure = runCatching { BridgeSnapshotMapper.fromMap(payload) }.exceptionOrNull()

        assertTrue(failure is IllegalArgumentException)
    }

}
