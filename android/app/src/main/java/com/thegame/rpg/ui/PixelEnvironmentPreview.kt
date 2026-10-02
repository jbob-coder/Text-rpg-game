package com.thegame.rpg.ui

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.unit.dp
import kotlin.math.floor

/**
 * Map-facing arrival/exterior preview using only exact authored location bindings.
 *
 * This component is deliberately read-only. It cannot infer travel availability or replace a
 * named-location scene master.
 */
@Composable
fun PixelEnvironmentArrivalPreview(
    locationId: String,
    modifier: Modifier = Modifier,
) {
    val sprite = PixelEnvironmentModuleCatalog.arrivalPreview(locationId) ?: return
    val detailTiles = PixelEnvironmentModuleCatalog.arrivalDetailTiles(locationId)
    val detailWidth = detailTiles.sumOf { it.width }
    val detailHeight = detailTiles.maxOfOrNull { it.height } ?: 0
    val compositionWidth = maxOf(sprite.width, detailWidth)
    val compositionHeight = sprite.height + detailHeight

    Canvas(
        modifier = modifier
            .background(PixelColors.Deep)
            .border(2.dp, PixelColors.Muted)
            .testTag("map-arrival-preview-$locationId"),
    ) {
        val px = floor(
            minOf(
                size.width / compositionWidth.toFloat(),
                size.height / compositionHeight.toFloat(),
            ),
        ).coerceAtLeast(1f)
        val ox = floor((size.width - compositionWidth * px) / 2f)
        val oy = floor((size.height - compositionHeight * px) / 2f)
        val spriteOx = ox + floor((compositionWidth - sprite.width) * px / 2f)

        drawPixelSprite(
            sprite = sprite,
            pixelSize = px,
            originX = spriteOx,
            originY = oy,
        )

        if (detailTiles.isNotEmpty()) {
            var tileX = ox + floor((compositionWidth - detailWidth) * px / 2f)
            val tileY = oy + sprite.height * px
            detailTiles.forEach { tile ->
                drawPixelSprite(
                    sprite = tile,
                    pixelSize = px,
                    originX = tileX,
                    originY = tileY,
                )
                tileX += tile.width * px
            }
        }
    }
}
