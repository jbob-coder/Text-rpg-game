package com.thegame.rpg.engine

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class BridgeInventoryMapperTest {
    private fun basePayload(inventory: Map<String, Any?>): Map<String, Any?> =
        mapOf(
            "scene" to mapOf(
                "id" to "OPENING_DEPOT_BLACKOUT",
                "title" to "Platform Nine",
                "body" to "The relay is waiting.",
                "choices" to emptyList<Any>(),
            ),
            "status" to mapOf(
                "resources" to emptyList<Any>(),
            ),
            "inventory" to inventory,
            "visuals" to mapOf("relay_state" to "opened"),
            "meta" to mapOf(
                "turn" to 2,
                "time_minutes" to 0,
                "location" to "PLATFORM_NINE",
            ),
        )

    @Test
    fun phase1InventoryAndEquipmentProjectionMapsToTypedAndroidState() {
        val payload = basePayload(
            mapOf(
                "items" to listOf(
                    mapOf(
                        "id" to "ITEM_DEAD_RELAY",
                        "name" to "Dead relay",
                        "quantity" to 1,
                        "equippable" to false,
                        "slot" to null,
                        "quality" to null,
                    ),
                    mapOf(
                        "id" to "ITEM_SIGNAL_RING",
                        "name" to "Signal ring",
                        "quantity" to 1,
                        "equippable" to true,
                        "slot" to "ring_1",
                        "quality" to "uncommon",
                    ),
                ),
                "equipment" to listOf(
                    mapOf(
                        "slot" to "body",
                        "equipped" to true,
                        "item_id" to "ITEM_DEPOT_JACKET",
                        "name" to "Depot utility jacket",
                        "quality" to "standard",
                    ),
                    mapOf(
                        "slot" to "ring_2",
                        "equipped" to false,
                        "item_id" to null,
                        "name" to null,
                        "quality" to null,
                    ),
                ),
            )
        )

        val snapshot = BridgeSnapshotMapper.fromMap(payload)

        assertEquals(2, snapshot.inventory.items.size)
        val relay = snapshot.inventory.items.first { it.id == "ITEM_DEAD_RELAY" }
        assertEquals(1, relay.quantity)
        assertFalse(relay.equippable)
        assertNull(relay.slot)
        assertNull(relay.quality)

        val ring = snapshot.inventory.items.first { it.id == "ITEM_SIGNAL_RING" }
        assertTrue(ring.equippable)
        assertEquals("ring_1", ring.slot)
        assertEquals("uncommon", ring.quality)

        val body = snapshot.inventory.equipment.first { it.slot == "body" }
        assertTrue(body.equipped)
        assertEquals("ITEM_DEPOT_JACKET", body.itemId)
        assertEquals("Depot utility jacket", body.name)
        assertEquals("standard", body.quality)

        val ringTwo = snapshot.inventory.equipment.first { it.slot == "ring_2" }
        assertFalse(ringTwo.equipped)
        assertNull(ringTwo.itemId)

        assertEquals("opened", snapshot.visuals.relayState)
    }

    @Test
    fun missingInventoryPayloadRemainsBackwardCompatible() {
        val snapshot = BridgeSnapshotMapper.fromMap(basePayload(emptyMap()))

        assertTrue(snapshot.inventory.items.isEmpty())
        assertTrue(snapshot.inventory.equipment.isEmpty())
    }
}
