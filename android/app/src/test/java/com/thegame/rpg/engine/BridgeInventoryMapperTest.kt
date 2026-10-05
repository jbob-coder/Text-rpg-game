package com.thegame.rpg.engine

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class BridgeInventoryMapperTest {
    private fun payload(inventory: Map<String, Any?>): Map<String, Any?> = mapOf(
        "scene" to mapOf(
            "id" to "SCENE",
            "title" to "Scene",
            "body" to "Body",
            "choices" to emptyList<Any>(),
        ),
        "status" to mapOf("resources" to emptyList<Any>()),
        "inventory" to inventory,
        "meta" to mapOf(
            "turn" to 0,
            "time_minutes" to 0,
            "location" to "PLATFORM_NINE",
        ),
    )

    @Test
    fun validInventoryAndEquipmentProjectionMaps() {
        val snapshot = BridgeSnapshotMapper.fromMap(
            payload(
                mapOf(
                    "items" to listOf(
                        mapOf(
                            "id" to "ITEM_DEPOT_JACKET",
                            "name" to "Depot Jacket",
                            "quantity" to 1,
                            "equippable" to true,
                            "slot" to "body",
                            "quality" to "standard",
                        )
                    ),
                    "equipment" to listOf(
                        mapOf("slot" to "body", "equipped" to false),
                        mapOf(
                            "slot" to "neck",
                            "equipped" to true,
                            "item_id" to "ITEM_COURIER_NECKTAG",
                            "name" to "Courier Necktag",
                            "quality" to "standard",
                        ),
                    ),
                )
            )
        )

        assertEquals(1, snapshot.inventory.items.single().quantity)
        assertTrue(snapshot.inventory.items.single().equippable)
        assertEquals("body", snapshot.inventory.items.single().slot)
        assertFalse(snapshot.inventory.equipment.first().equipped)
        assertEquals("ITEM_COURIER_NECKTAG", snapshot.inventory.equipment.last().itemId)
    }

    @Test
    fun nonPositiveInventoryQuantityIsRejected() {
        for (quantity in listOf(0, -1)) {
            val failure = runCatching {
                BridgeSnapshotMapper.fromMap(
                    payload(
                        mapOf(
                            "items" to listOf(
                                mapOf(
                                    "id" to "ITEM_X",
                                    "name" to "Item X",
                                    "quantity" to quantity,
                                )
                            )
                        )
                    )
                )
            }.exceptionOrNull()

            assertTrue(failure is IllegalArgumentException)
        }
    }

    @Test
    fun equippableInventoryItemRequiresSlot() {
        val failure = runCatching {
            BridgeSnapshotMapper.fromMap(
                payload(
                    mapOf(
                        "items" to listOf(
                            mapOf(
                                "id" to "ITEM_X",
                                "name" to "Item X",
                                "quantity" to 1,
                                "equippable" to true,
                            )
                        )
                    )
                )
            )
        }.exceptionOrNull()

        assertTrue(failure is IllegalArgumentException)
    }

    @Test
    fun equippedSlotRequiresItemIdentity() {
        val failure = runCatching {
            BridgeSnapshotMapper.fromMap(
                payload(
                    mapOf(
                        "equipment" to listOf(
                            mapOf("slot" to "body", "equipped" to true)
                        )
                    )
                )
            )
        }.exceptionOrNull()

        assertTrue(failure is IllegalArgumentException)
    }

    @Test
    fun unequippedSlotCannotExposeItemIdentity() {
        val failure = runCatching {
            BridgeSnapshotMapper.fromMap(
                payload(
                    mapOf(
                        "equipment" to listOf(
                            mapOf(
                                "slot" to "body",
                                "equipped" to false,
                                "item_id" to "ITEM_HIDDEN",
                                "name" to "Hidden Item",
                            )
                        )
                    )
                )
            )
        }.exceptionOrNull()

        assertTrue(failure is IllegalArgumentException)
    }
}
