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
