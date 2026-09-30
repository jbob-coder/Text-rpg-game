package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelHeldPropCatalogTest {
    @Test
    fun diagnosticReaderMastersUseDocumentedNativeDimensionsAndPaletteKeys() {
        val expected = mapOf(
            PixelHeldPropCatalog.DIAGNOSTIC_READER_ICON_MASTER_ID to (32 to 32),
            PixelHeldPropCatalog.DIAGNOSTIC_READER_HELD_FRONT_MASTER_ID to (32 to 48),
        )

        assertEquals(
            expected.keys,
            PixelHeldPropCatalog.productionMasters.map { it.assetId }.toSet(),
        )

        PixelHeldPropCatalog.productionMasters.forEach { sprite ->
            val dimensions = expected.getValue(sprite.assetId)
            assertEquals(dimensions.first, sprite.width)
            assertEquals(dimensions.second, sprite.height)
            assertEquals(sprite.height, sprite.rows.size)
            assertTrue(sprite.rows.all { it.length == sprite.width })

            val usedKeys = sprite.rows
                .flatMap { it.toList() }
                .filter { it != PixelSprite.TRANSPARENT_PIXEL }
                .toSet()

            assertTrue(usedKeys.all { it in sprite.palette })
        }
    }

    @Test
    fun heldFrontMasterStaysTransparentOutsideTheReaderGeometry() {
        val sprite = PixelHeldPropCatalog.diagnosticReaderHeldFrontMaster

        assertTrue(sprite.rows.take(18).all { row ->
            row.all { it == PixelSprite.TRANSPARENT_PIXEL }
        })
        assertTrue(sprite.rows.drop(36).all { row ->
            row.all { it == PixelSprite.TRANSPARENT_PIXEL }
        })
        sprite.rows.subList(18, 36).forEach { row ->
            assertTrue(row.take(17).all { it == PixelSprite.TRANSPARENT_PIXEL })
            assertTrue(row.drop(27).all { it == PixelSprite.TRANSPARENT_PIXEL })
        }
    }
}
