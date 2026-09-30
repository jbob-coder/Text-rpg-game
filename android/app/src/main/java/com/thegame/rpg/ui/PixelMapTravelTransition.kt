package com.thegame.rpg.ui

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.aspectRatio
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.unit.dp
import com.thegame.rpg.TravelTransitionUiState
import kotlinx.coroutines.delay
import kotlin.math.floor

/**
 * Asset 100: short route-preserving travel sequence.
 *
 * The sequence is presentation-only. It is rendered only from a TravelTransitionUiState which is
 * created after authoritative travel succeeds and a new player-facing location has been returned.
 */
object PixelMapTravelTransitionCatalog {
    const val ASSET_ID = "UI_MAP_TRAVEL_TRANSITION"
    const val WIDTH = 128
    const val HEIGHT = 64
    const val FRAME_COUNT = 8

    private val palette = mapOf(
        'i' to PixelColors.Ink,
        'd' to PixelColors.Deep,
        'm' to PixelColors.Muted,
        'c' to PixelColors.Cyan,
        'g' to PixelColors.Gold,
        'p' to PixelColors.Paper,
    )

    private fun frame(index: Int): PixelSprite {
        require(index in 0 until FRAME_COUNT)
        val pixels = MutableList(HEIGHT) { CharArray(WIDTH) { PixelSprite.TRANSPARENT_PIXEL } }

        fun plot(x: Int, y: Int, key: Char) {
            if (x in 0 until WIDTH && y in 0 until HEIGHT) pixels[y][x] = key
        }

        fun rect(x: Int, y: Int, w: Int, h: Int, key: Char) {
            for (yy in y until y + h) {
                for (xx in x until x + w) plot(xx, yy, key)
            }
        }

        rect(4, 5, 120, 2, 'd')
        rect(4, 57, 120, 2, 'd')
        rect(12, 31, 104, 2, 'm')

        rect(10, 27, 8, 10, 'g')
        rect(12, 29, 4, 6, 'i')
        rect(110, 27, 8, 10, 'c')
        rect(112, 29, 4, 6, 'i')

        val progressX = 18 + ((index + 1) * 90 / FRAME_COUNT)
        rect(18, 31, (progressX - 18).coerceAtLeast(1), 2, 'c')
        rect(progressX - 2, 28, 5, 8, 'p')
        rect(progressX - 1, 29, 3, 6, 'g')

        for (streak in 0 until 7) {
            val rawX = 24 + streak * 16 - index * 5
            val x = ((rawX % 112) + 112) % 112 + 8
            val y = 13 + (streak % 3) * 12
            rect(x, y, 6, 1, if ((streak + index) % 3 == 0) 'c' else 'd')
            rect((WIDTH - 1 - x).coerceAtLeast(0), 48 - (streak % 3) * 9, 4, 1, 'd')
        }

        val inset = 2 + index.coerceAtMost(4)
        rect(5 + inset, 8, 10, 1, 'm')
        rect(113 - inset, 54, 10, 1, 'm')

        return PixelSprite(
            assetId = "${ASSET_ID}_FRAME_${index + 1}",
            width = WIDTH,
            height = HEIGHT,
            palette = palette,
            rows = pixels.map { it.concatToString() },
        )
    }

    val frames: List<PixelSprite> = List(FRAME_COUNT) { frame(it) }
}

@Composable
fun MapTravelTransitionOverlay(
    transition: TravelTransitionUiState,
    onFinished: (Long) -> Unit,
    modifier: Modifier = Modifier,
) {
    var frameIndex by remember(transition.token) { mutableIntStateOf(0) }

    LaunchedEffect(transition.token) {
        frameIndex = 0
        for (next in 1 until PixelMapTravelTransitionCatalog.frames.size) {
            delay(75L)
            frameIndex = next
        }
        delay(125L)
        onFinished(transition.token)
    }

    Box(
        modifier = modifier
            .fillMaxSize()
            .background(PixelColors.Ink)
            .testTag("map-travel-transition"),
        contentAlignment = Alignment.Center,
    ) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .padding(horizontal = 16.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
        ) {
            Text(
                text = "TRAVEL",
                color = PixelColors.Gold,
                style = MaterialTheme.typography.titleLarge,
            )
            Spacer(Modifier.height(10.dp))
            Canvas(
                modifier = Modifier
                    .fillMaxWidth()
                    .aspectRatio(2f)
                    .background(PixelColors.Deep)
                    .border(2.dp, PixelColors.Cyan)
                    .testTag("map-travel-transition-canvas"),
            ) {
                val sprite = PixelMapTravelTransitionCatalog.frames[frameIndex]
                val px = floor(
                    minOf(size.width / sprite.width.toFloat(), size.height / sprite.height.toFloat())
                ).coerceAtLeast(1f)
                val ox = floor((size.width - sprite.width * px) / 2f)
                val oy = floor((size.height - sprite.height * px) / 2f)
                drawPixelSprite(sprite, px, ox, oy)
            }
            Spacer(Modifier.height(10.dp))
            Text(
                text = "${displayLocation(transition.fromLocation)} → ${displayLocation(transition.toLocation)}",
                color = PixelColors.Paper,
                style = MaterialTheme.typography.bodyMedium,
                modifier = Modifier.testTag("map-travel-transition-route"),
            )
        }
    }
}

private fun displayLocation(locationId: String): String =
    locationId.replace('_', ' ').uppercase()
