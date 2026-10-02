package com.thegame.rpg.ui

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class PixelCharacterStagingCatalogTest {
    @Test
    fun mediumGroundShadowMatchesDocumentedStagingContract() {
        val sprite = PixelCharacterStagingCatalog.mediumGroundShadow

        assertEquals(PixelCharacterStagingCatalog.MEDIUM_GROUND_SHADOW_ID, sprite.assetId)
        assertEquals(32, sprite.width)
        assertEquals(16, sprite.height)
        assertEquals(16, sprite.rows.size)
        assertTrue(sprite.rows.all { it.length == 32 })
        assertTrue(sprite.rows.take(11).all { row ->
            row.all { it == PixelSprite.TRANSPARENT_PIXEL }
        })
        assertTrue(
            sprite.rows
                .flatMap { it.toList() }
                .any { it != PixelSprite.TRANSPARENT_PIXEL },
        )
    }
}
