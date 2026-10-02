package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelEnvironmentModuleCatalogTest {
    @Test
    fun sceneModulesUseExact128By64Masters() {
        assertEquals(
            setOf(
                PixelEnvironmentModuleCatalog.DEPOT_FACADE_EXTERIOR_ID,
                PixelEnvironmentModuleCatalog.MAINTENANCE_CORRIDOR_CONNECTOR_ID,
                PixelEnvironmentModuleCatalog.MUNICIPAL_ARCHIVE_EXTERIOR_ID,
            ),
            PixelEnvironmentModuleCatalog.productionModules.map { it.assetId }.toSet(),
        )

        PixelEnvironmentModuleCatalog.productionModules.forEach { module ->
            assertEquals(128, module.width)
            assertEquals(64, module.height)
            assertEquals(64, module.rows.size)
            assertTrue(module.rows.all { it.length == 128 })

            val used = module.rows
                .flatMap { it.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()
            assertTrue(used.all { it in module.palette })
        }
    }

    @Test
    fun infrastructureAtlasContainsFourReusable32By32Tiles() {
        val atlas = PixelEnvironmentModuleCatalog.infrastructureTileAtlas

        assertEquals(
            PixelEnvironmentModuleCatalog.MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS_ID,
            atlas.assetId,
        )
        assertEquals(4, atlas.tiles.size)
        assertEquals(4, atlas.tiles.map { it.assetId }.toSet().size)

        atlas.tiles.forEach { tile ->
            assertEquals(32, tile.width)
            assertEquals(32, tile.height)
            assertEquals(32, tile.rows.size)
            assertTrue(tile.rows.all { it.length == 32 })
            assertTrue(
                tile.assetId.startsWith(
                    PixelEnvironmentModuleCatalog.MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS_ID,
                ),
            )

            val used = tile.rows
                .flatMap { it.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()
            assertTrue(used.all { it in tile.palette })
        }
    }
    @Test
    fun arrivalPreviewsUseOnlyExactAuthoredLocationBindings() {
        assertEquals(
            PixelEnvironmentModuleCatalog.DEPOT_FACADE_EXTERIOR_ID,
            PixelEnvironmentModuleCatalog.arrivalPreview("DISTRICT_PLAZA")?.assetId,
        )
        assertEquals(
            PixelEnvironmentModuleCatalog.MUNICIPAL_ARCHIVE_EXTERIOR_ID,
            PixelEnvironmentModuleCatalog.arrivalPreview("DISTRICT_ARCHIVE")?.assetId,
        )
        assertEquals(PixelEnvironmentModuleCatalog.MAINTENANCE_CORRIDOR_CONNECTOR_ID, PixelEnvironmentModuleCatalog.arrivalPreview("SERVICE_TUNNEL")?.assetId)
        assertEquals(null, PixelEnvironmentModuleCatalog.arrivalPreview("UNKNOWN_LOCATION"))
    }


}
