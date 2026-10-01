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

    Canvas(
        modifier = modifier
            .background(PixelColors.Deep)
            .border(2.dp, PixelColors.Muted)
            .testTag("map-arrival-preview-$locationId"),
    ) {
        val px = floor(
            minOf(size.width / sprite.width.toFloat(), size.height / sprite.height.toFloat()),
        ).coerceAtLeast(1f)
        val ox = floor((size.width - sprite.width * px) / 2f)
        val oy = floor((size.height - sprite.height * px) / 2f)
        drawPixelSprite(
            sprite = sprite,
            pixelSize = px,
            originX = ox,
            originY = oy,
        )
    }
}
