package com.thegame.rpg.ui

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.unit.dp
import kotlinx.coroutines.delay
import kotlin.math.floor

@Composable
fun SceneIllustration(
    locationId: String,
    sceneId: String? = null,
    relayState: String? = null,
    modifier: Modifier = Modifier,
) {
    val traceFxFrames = PixelTraceFxCatalog.directionalTraceForScene(sceneId) ?: PixelTraceFxCatalog.signalPulseForScene(sceneId) ?: PixelTraceFxCatalog.forScene(sceneId)
    val sceneRaster = rememberPixelRaster(PixelRasterCatalog.scene(locationId))
    var traceFxFrameIndex by remember(sceneId) { mutableStateOf(0) }

    LaunchedEffect(sceneId, traceFxFrames) {
        if (traceFxFrames.isNullOrEmpty()) {
            traceFxFrameIndex = 0
            return@LaunchedEffect
        }

        traceFxFrameIndex = 0
        while (true) {
            delay(180L)
            traceFxFrameIndex = (traceFxFrameIndex + 1) % traceFxFrames.size
        }
    }

    Canvas(
        modifier = modifier
            .testTag("scene-illustration")
            .background(PixelColors.Deep)
            .border(2.dp, PixelColors.Muted),
    ) {
        PixelSceneCatalog.scene(locationId)?.let { scene ->
            val scenePixel = floor(
                minOf(size.width / scene.width.toFloat(), size.height / scene.height.toFloat())
            ).coerceAtLeast(1f)
            val sceneOriginX = floor((size.width - scene.width * scenePixel) / 2f)
            val sceneOriginY = floor((size.height - scene.height * scenePixel) / 2f)

            if (sceneRaster != null) {
                drawPixelRaster(
                    image = sceneRaster,
                    sourceWidth = scene.width,
                    sourceHeight = scene.height,
                    pixelSize = scenePixel,
                    originX = sceneOriginX,
                    originY = sceneOriginY,
                )
            } else {
                drawPixelSprite(
                    sprite = scene,
                    pixelSize = scenePixel,
                    originX = sceneOriginX,
                    originY = sceneOriginY,
                )
            }

            PixelSceneOverlayCatalog.forScene(sceneId)?.let { overlay ->
                drawPixelSprite(
                    sprite = overlay,
                    pixelSize = scenePixel,
                    originX = sceneOriginX,
                    originY = sceneOriginY,
                )
            }

            PixelSceneOverlayCatalog.forVisualState(
                locationId = locationId,
                relayState = relayState,
            )?.let { overlay ->
                drawPixelSprite(
                    sprite = overlay,
                    pixelSize = scenePixel,
                    originX = sceneOriginX,
                    originY = sceneOriginY,
                )
            }

            PixelEnvironmentDecalCatalog.placements(locationId).forEach { placement ->
                drawPixelSprite(
                    sprite = placement.sprite,
                    pixelSize = scenePixel,
                    originX = floor(sceneOriginX + placement.x * scenePixel),
                    originY = floor(sceneOriginY + placement.y * scenePixel),
                )
            }

            PixelEnvironmentPropCatalog.placements(
                locationId = locationId,
                sceneId = sceneId,
            ).forEach { placement ->
                drawPixelSprite(
                    sprite = placement.sprite,
                    pixelSize = scenePixel,
                    originX = floor(sceneOriginX + placement.x * scenePixel),
                    originY = floor(sceneOriginY + placement.y * scenePixel),
                )
            }

            traceFxFrames?.getOrNull(traceFxFrameIndex)?.let { fx ->
                val fxOriginX = floor(
                    sceneOriginX + (scene.width - fx.width) * scenePixel / 2f
                )
                val fxOriginY = floor(
                    sceneOriginY + (scene.height - fx.height) * scenePixel / 2f
                )
                drawPixelSprite(
                    sprite = fx,
                    pixelSize = scenePixel,
                    originX = fxOriginX,
                    originY = fxOriginY,
                )
            }

            if (locationId == "RELAY_WORKBENCH") {
                PixelAssetCatalog.relayStateSprite(relayState)?.let { relay ->
                    val relayPixel = floor(scenePixel / 2f).coerceAtLeast(1f)
                    val relayWidth = relay.width * relayPixel
                    val relayOriginX = floor(sceneOriginX + 64f * scenePixel - relayWidth / 2f)
                    val relayOriginY = floor(sceneOriginY + 25f * scenePixel)
                    drawPixelSprite(
                        sprite = relay,
                        pixelSize = relayPixel,
                        originX = relayOriginX,
                        originY = relayOriginY,
                    )
                }
            }
            return@Canvas
        }

        val cell = minOf(size.width / 64f, size.height / 32f)
        val ox = (size.width - cell * 64f) / 2f
        val oy = (size.height - cell * 32f) / 2f

        fun block(x: Int, y: Int, w: Int, h: Int, color: Color) {
            drawRect(
                color = color,
                topLeft = Offset(ox + x * cell, oy + y * cell),
                size = Size(w * cell, h * cell),
            )
        }

        fun frame() {
            block(0, 0, 64, 32, Color(0xFF111A20))
            block(0, 24, 64, 8, Color(0xFF1B252C))
            block(0, 23, 64, 1, Color(0xFF53616A))
        }

        frame()

        when (locationId) {
            "PLATFORM_NINE" -> {
                block(3, 4, 58, 2, Color(0xFF394850))
                block(6, 7, 18, 12, Color(0xFF26363E))
                block(8, 9, 14, 6, Color(0xFF17242B))
                block(28, 8, 30, 13, Color(0xFF344750))
                block(31, 11, 8, 5, Color(0xFF162129))
                block(42, 11, 8, 5, Color(0xFF162129))
                block(2, 25, 60, 2, PixelColors.Danger)
                for (x in 4..58 step 8) block(x, 2, 4, 1, PixelColors.Paper)
            }
            "RELAY_WORKBENCH" -> {
                block(7, 17, 50, 4, Color(0xFF48535A))
                block(10, 21, 4, 7, Color(0xFF2B3439))
                block(50, 21, 4, 7, Color(0xFF2B3439))
                block(24, 11, 16, 6, Color(0xFF273A42))
                block(27, 12, 10, 3, PixelColors.Cyan)
                block(8, 6, 48, 2, Color(0xFF303E45))
                block(11, 8, 2, 7, PixelColors.Gold)
                block(50, 8, 2, 7, PixelColors.Gold)
            }
            "GATE_TWELVE" -> {
                block(10, 5, 44, 20, Color(0xFF3A4449))
                block(16, 8, 32, 17, Color(0xFF151E23))
                block(19, 10, 26, 15, Color(0xFF263238))
                block(31, 10, 2, 15, PixelColors.Gold)
                block(13, 3, 38, 2, Color(0xFF54636B))
                block(8, 25, 48, 2, PixelColors.Cyan)
            }
            "SERVICE_TUNNEL" -> {
                block(0, 4, 64, 3, Color(0xFF39474D))
                block(0, 9, 64, 2, Color(0xFF263238))
                block(5, 11, 4, 12, Color(0xFF47565D))
                block(55, 11, 4, 12, Color(0xFF47565D))
                block(16, 13, 32, 10, Color(0xFF11191D))
                for (x in 18..46 step 7) block(x, 15, 3, 1, PixelColors.Cyan)
                block(0, 27, 64, 2, Color(0xFF576168))
            }
            "EVAC_STAIR" -> {
                for (step in 0..7) {
                    block(9 + step * 5, 25 - step * 3, 20, 3, Color(0xFF47545B))
                }
                block(5, 3, 3, 22, PixelColors.Gold)
                block(56, 5, 3, 18, PixelColors.Cyan)
            }
            "TRACE_CHAMBER" -> {
                block(10, 5, 44, 20, Color(0xFF1D2A31))
                block(30, 10, 4, 12, PixelColors.Cyan)
                block(26, 12, 12, 8, Color(0xFF2E5960))
                block(22, 14, 20, 4, Color(0xFF28444C))
                block(18, 15, 28, 2, Color(0xFF20353C))
                block(8, 26, 48, 2, PixelColors.Gold)
            }
            "DISTRICT_PLAZA" -> {
                // Depot facade and the emergency-lit public square.
                block(2, 8, 20, 15, Color(0xFF34444C))
                block(5, 11, 5, 6, Color(0xFF17242B))
                block(13, 11, 5, 6, Color(0xFF17242B))
                block(26, 5, 34, 18, Color(0xFF3A4C55))
                block(30, 9, 8, 8, Color(0xFF1B2A31))
                block(43, 9, 8, 8, Color(0xFF1B2A31))
                block(54, 11, 3, 12, PixelColors.Gold)
                block(0, 25, 64, 2, Color(0xFF57636A))
                block(6, 27, 52, 1, PixelColors.Cyan)
                block(8, 21, 2, 4, PixelColors.Danger)
                block(20, 20, 2, 5, PixelColors.Danger)
            }
            "DISTRICT_ARCHIVE" -> {
                // Tall shelving, records terminals and backup lamps.
                block(4, 4, 15, 20, Color(0xFF3D4D54))
                block(22, 4, 15, 20, Color(0xFF3D4D54))
                block(40, 4, 15, 20, Color(0xFF3D4D54))
                for (y in 7..21 step 4) {
                    block(6, y, 11, 2, Color(0xFF6A5941))
                    block(24, y, 11, 2, Color(0xFF6A5941))
                    block(42, y, 11, 2, Color(0xFF6A5941))
                }
                block(18, 18, 23, 4, Color(0xFF2B383E))
                block(24, 16, 10, 2, PixelColors.Cyan)
                block(28, 22, 3, 3, PixelColors.Gold)
                block(0, 26, 64, 2, Color(0xFF56636A))
            }
            "WORKSHOP_ROW" -> {
                // Open repair stalls and salvage benches.
                block(2, 7, 18, 16, Color(0xFF38484F))
                block(23, 5, 18, 18, Color(0xFF415159))
                block(44, 8, 17, 15, Color(0xFF35454C))
                block(4, 9, 14, 3, Color(0xFF18262C))
                block(25, 8, 14, 3, Color(0xFF18262C))
                block(46, 10, 13, 3, Color(0xFF18262C))
                block(6, 18, 50, 4, Color(0xFF5A5548))
                block(10, 15, 4, 3, PixelColors.Cyan)
                block(28, 14, 5, 4, PixelColors.Gold)
                block(48, 15, 4, 3, PixelColors.Danger)
                block(0, 26, 64, 2, Color(0xFF57636A))
            }
            else -> {
                block(7, 9, 9, 14, Color(0xFF33444D))
                block(19, 5, 12, 18, Color(0xFF3B4B53))
                block(35, 11, 8, 12, Color(0xFF2C3B43))
                block(47, 7, 10, 16, Color(0xFF405159))
                block(0, 26, 64, 2, PixelColors.Cyan)
            }
        }
    }
}
