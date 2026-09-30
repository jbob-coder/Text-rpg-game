package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelEnvironmentPropCatalogTest {
    @Test
    fun productionPropsUseDocumentedNativeCanvasesAndMappedPaletteKeys() {
        val expected = mapOf(
            PixelEnvironmentPropCatalog.ARCHIVE_SHELF_ID to (32 to 48),
            PixelEnvironmentPropCatalog.ARCHIVE_TERMINAL_ID to (32 to 32),
            PixelEnvironmentPropCatalog.WORKSHOP_BENCH_ID to (48 to 32),
            PixelEnvironmentPropCatalog.DISTRICT_NOTICE_BOARD_ID to (32 to 48),
            PixelEnvironmentPropCatalog.RELAY_WORKBENCH_ID to (64 to 32),
            PixelEnvironmentPropCatalog.GATE_TWELVE_DOOR_ID to (64 to 48),
            PixelEnvironmentPropCatalog.TUNNEL_PIPE_SET_ID to (32 to 32),
            PixelEnvironmentPropCatalog.TUNNEL_CABLE_SET_ID to (32 to 32),
            PixelEnvironmentPropCatalog.TRACE_CHAMBER_APPARATUS_ID to (48 to 48),
        )

        assertEquals(expected.keys, PixelEnvironmentPropCatalog.productionProps.map { it.assetId }.toSet())

        PixelEnvironmentPropCatalog.productionProps.forEach { prop ->
            val dimensions = requireNotNull(expected[prop.assetId])
            assertEquals(dimensions.first, prop.width)
            assertEquals(dimensions.second, prop.height)
            assertEquals(prop.height, prop.rows.size)
            assertTrue(prop.rows.all { it.length == prop.width })

            val used = prop.rows
                .flatMap { it.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()
            assertTrue(used.all { it in prop.palette })
        }
    }

    @Test
    fun placementsUseOnlyPlayerFacingLocationAndSceneIds() {
        val relay = PixelEnvironmentPropCatalog.placements("RELAY_WORKBENCH", "OPENING_RELAY_CASING")
        assertEquals(listOf(PixelEnvironmentPropCatalog.relayWorkbench), relay.map { it.sprite })

        val gate = PixelEnvironmentPropCatalog.placements("GATE_TWELVE", "POWER_GATE_TWELVE_SIGNAL")
        assertEquals(listOf(PixelEnvironmentPropCatalog.gateTwelveDoor), gate.map { it.sprite })

        val tunnel = PixelEnvironmentPropCatalog.placements("SERVICE_TUNNEL", "OPENING_TUNNEL")
        assertEquals(3, tunnel.size)
        assertEquals(2, tunnel.count { it.sprite === PixelEnvironmentPropCatalog.tunnelPipeSet })
        assertEquals(1, tunnel.count { it.sprite === PixelEnvironmentPropCatalog.tunnelCableSet })

        val chamber = PixelEnvironmentPropCatalog.placements("TRACE_CHAMBER", "POWER_FIRST_PRACTICE")
        assertEquals(
            listOf(PixelEnvironmentPropCatalog.traceChamberApparatus),
            chamber.map { it.sprite },
        )

        val archive = PixelEnvironmentPropCatalog.placements("DISTRICT_ARCHIVE", "DISTRICT_ARCHIVE")
        assertEquals(3, archive.size)
        assertEquals(2, archive.count { it.sprite === PixelEnvironmentPropCatalog.archiveShelf })
        assertEquals(1, archive.count { it.sprite === PixelEnvironmentPropCatalog.archiveTerminal })

        val workshop = PixelEnvironmentPropCatalog.placements("WORKSHOP_ROW", "DISTRICT_WORKSHOP")
        assertEquals(
            listOf(PixelEnvironmentPropCatalog.workshopBench),
            workshop.map { it.sprite },
        )

        val plaza = PixelEnvironmentPropCatalog.placements("DISTRICT_PLAZA", "DISTRICT_HUB")
        assertEquals(
            listOf(PixelEnvironmentPropCatalog.districtNoticeBoard),
            plaza.map { it.sprite },
        )

        assertTrue(PixelEnvironmentPropCatalog.placements("DISTRICT_PLAZA", null).isEmpty())
        assertTrue(PixelEnvironmentPropCatalog.placements("GATE_TWELVE", "POWER_GATE_TWELVE_SIGNAL").isEmpty())
    }
}
