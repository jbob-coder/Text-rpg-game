package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelEnvironmentDecalCatalogTest {
    @Test
    fun productionDecalsUseDocumentedNativeCanvasesAndMappedPaletteKeys() {
        val expected = mapOf(
            PixelEnvironmentDecalCatalog.EVACUATION_SIGNAGE_SET_ID to (24 to 24),
            PixelEnvironmentDecalCatalog.DISTRICT_AMBIENT_DECAL_SET_ID to (32 to 32),
        )

        assertEquals(expected.keys, PixelEnvironmentDecalCatalog.productionDecals.map { it.assetId }.toSet())

        PixelEnvironmentDecalCatalog.productionDecals.forEach { decal ->
            val dimensions = requireNotNull(expected[decal.assetId])
            assertEquals(dimensions.first, decal.width)
            assertEquals(dimensions.second, decal.height)
            assertEquals(decal.height, decal.rows.size)
            assertTrue(decal.rows.all { it.length == decal.width })

            val used = decal.rows
                .flatMap { it.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()
            assertTrue(used.all { it in decal.palette })
        }
    }

    @Test
    fun placementsDependOnlyOnPlayerFacingLocationIds() {
        val platform = PixelEnvironmentDecalCatalog.placements("PLATFORM_NINE")
        assertEquals(
            listOf(
                PixelEnvironmentDecalCatalog.evacuationSignage,
                PixelEnvironmentDecalCatalog.districtAmbientDecals,
            ),
            platform.map { it.sprite },
        )

        assertEquals(
            listOf(PixelEnvironmentDecalCatalog.evacuationSignage),
            PixelEnvironmentDecalCatalog.placements("EVAC_STAIR").map { it.sprite },
        )
        assertEquals(
            listOf(PixelEnvironmentDecalCatalog.districtAmbientDecals),
            PixelEnvironmentDecalCatalog.placements("SERVICE_TUNNEL").map { it.sprite },
        )
        assertEquals(2, PixelEnvironmentDecalCatalog.placements("DISTRICT_PLAZA").size)
        assertTrue(PixelEnvironmentDecalCatalog.placements("UNKNOWN_LOCATION").isEmpty())
    }
}
