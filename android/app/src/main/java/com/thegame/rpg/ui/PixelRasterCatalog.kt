package com.thegame.rpg.ui

import android.graphics.BitmapFactory
import androidx.annotation.DrawableRes
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.graphics.FilterQuality
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.graphics.drawscope.DrawScope
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.IntSize
import com.thegame.rpg.R
import kotlin.math.roundToInt

/**
 * Raster delivery layer for authored pixel masters.
 *
 * Kotlin PixelSprite definitions remain the reviewable source/fallback. Exported PNGs are the
 * runtime-preferred delivery format once they exist. Missing raster entries deliberately fall
 * back to the source-native sprite instead of inventing replacement geometry.
 */
object PixelRasterCatalog {
    @DrawableRes
    fun sprite(assetId: String): Int? = when (assetId) {
        PixelAssetCatalog.PLAYER_FRONT_BASE_ID -> R.drawable.pixel_player_gameplay_front_base
        PixelAssetCatalog.PLAYER_HAIR_PLACEHOLDER_ID -> R.drawable.pixel_player_hair_tech_placeholder
        PixelAssetCatalog.DEPOT_JACKET_ICON_ID -> R.drawable.pixel_item_depot_jacket_icon
        PixelAssetCatalog.DEPOT_JACKET_LAYER_ID -> R.drawable.pixel_item_depot_jacket_paperdoll
        PixelAssetCatalog.WORK_GLOVES_ICON_ID -> R.drawable.pixel_item_work_gloves_icon
        PixelAssetCatalog.WORK_GLOVES_LAYER_ID -> R.drawable.pixel_item_work_gloves_paperdoll
        PixelAssetCatalog.SIGNAL_RING_ICON_ID -> R.drawable.pixel_item_signal_ring_icon
        PixelAssetCatalog.SIGNAL_RING_LAYER_ID -> R.drawable.pixel_item_signal_ring_paperdoll
        PixelSceneCatalog.PLATFORM_NINE_SCENE_ID -> R.drawable.pixel_platform_nine_blackout_scene
        else -> null
    }

    @DrawableRes
    fun scene(locationId: String): Int? = when (locationId) {
        "PLATFORM_NINE" -> R.drawable.pixel_platform_nine_blackout_scene
        else -> null
    }
}

@Composable
internal fun rememberPixelRaster(@DrawableRes resId: Int?): ImageBitmap? {
    val context = LocalContext.current
    return remember(resId) {
        resId?.let { id ->
            BitmapFactory.decodeResource(context.resources, id)?.asImageBitmap()
        }
    }
}

@Composable
internal fun rememberPixelRasters(assetIds: List<String>): Map<String, ImageBitmap> {
    val context = LocalContext.current
    return remember(assetIds) {
        assetIds.distinct().mapNotNull { assetId ->
            val resId = PixelRasterCatalog.sprite(assetId) ?: return@mapNotNull null
            val bitmap = BitmapFactory.decodeResource(context.resources, resId)?.asImageBitmap()
                ?: return@mapNotNull null
            assetId to bitmap
        }.toMap()
    }
}

internal fun DrawScope.drawPixelRaster(
    image: ImageBitmap,
    sourceWidth: Int,
    sourceHeight: Int,
    pixelSize: Float,
    originX: Float,
    originY: Float,
) {
    drawImage(
        image = image,
        dstOffset = IntOffset(originX.roundToInt(), originY.roundToInt()),
        dstSize = IntSize(
            (sourceWidth * pixelSize).roundToInt(),
            (sourceHeight * pixelSize).roundToInt(),
        ),
        filterQuality = FilterQuality.None,
    )
}
