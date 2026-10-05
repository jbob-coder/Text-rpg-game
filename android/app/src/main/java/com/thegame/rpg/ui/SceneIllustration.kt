package com.thegame.rpg.ui

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.border
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
import com.thegame.rpg.engine.GameRoomActor
import kotlinx.coroutines.delay
import kotlin.math.floor

@Composable
fun SceneIllustration(
    locationId: String,
    sceneId: String? = null,
    relayState: String? = null,
    roomActors: List<GameRoomActor> = emptyList(),
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
                drawPixelSprite(overlay, scenePixel, sceneOriginX, sceneOriginY)
            }
            PixelSceneOverlayCatalog.forVisualState(locationId, relayState)?.let { overlay ->
                drawPixelSprite(overlay, scenePixel, sceneOriginX, sceneOriginY)
            }
            PixelEnvironmentDecalCatalog.placements(locationId).forEach { placement ->
                drawPixelSprite(placement.sprite, scenePixel, floor(sceneOriginX + placement.x * scenePixel), floor(sceneOriginY + placement.y * scenePixel))
            }
            PixelEnvironmentPropCatalog.placements(locationId, sceneId).forEach { placement ->
                drawPixelSprite(placement.sprite, scenePixel, floor(sceneOriginX + placement.x * scenePixel), floor(sceneOriginY + placement.y * scenePixel))
            }
            PixelStoryActorCatalog.placements(roomActors).forEach { placement ->
                drawPixelSprite(placement.sprite, scenePixel, floor(sceneOriginX + placement.x * scenePixel), floor(sceneOriginY + placement.y * scenePixel))
            }

            traceFxFrames?.getOrNull(traceFxFrameIndex)?.let { fx ->
                val fxOriginX = floor(sceneOriginX + (scene.width - fx.width) * scenePixel / 2f)
                val fxOriginY = floor(sceneOriginY + (scene.height - fx.height) * scenePixel / 2f)
                drawPixelSprite(fx, scenePixel, fxOriginX, fxOriginY)
            }

            if (locationId == "RELAY_WORKBENCH") {
                PixelAssetCatalog.relayStateSprite(relayState)?.let { relay ->
                    val relayPixel = floor(scenePixel / 2f).coerceAtLeast(1f)
                    val relayWidth = relay.width * relayPixel
                    val relayOriginX = floor(sceneOriginX + 64f * scenePixel - relayWidth / 2f)
                    val relayOriginY = floor(sceneOriginY + 25f * scenePixel)
                    drawPixelSprite(relay, relayPixel, relayOriginX, relayOriginY)
                }
            }
            return@Canvas
        }

        val cell = minOf(size.width / 64f, size.height / 32f)
        val ox = (size.width - cell * 64f) / 2f
        val oy = (size.height - cell * 32f) / 2f
        fun block(x: Int, y: Int, w: Int, h: Int, color: Color) {
            drawRect(color, Offset(ox + x * cell, oy + y * cell), Size(w * cell, h * cell))
        }
        block(0, 0, 64, 32, Color(0xFF111A20))
        block(0, 24, 64, 8, Color(0xFF1B252C))
        block(0, 23, 64, 1, Color(0xFF53616A))
        when (locationId) {
            "PLATFORM_NINE" -> { block(3,4,58,2,Color(0xFF394850)); block(6,7,18,12,Color(0xFF26363E)); block(28,8,30,13,Color(0xFF344750)); block(2,25,60,2,PixelColors.Danger) }
            "RELAY_WORKBENCH" -> { block(7,17,50,4,Color(0xFF48535A)); block(24,11,16,6,Color(0xFF273A42)); block(27,12,10,3,PixelColors.Cyan) }
            "GATE_TWELVE" -> { block(10,5,44,20,Color(0xFF3A4449)); block(16,8,32,17,Color(0xFF151E23)); block(31,10,2,15,PixelColors.Gold) }
            "SERVICE_TUNNEL" -> { block(0,4,64,3,Color(0xFF39474D)); block(16,13,32,10,Color(0xFF11191D)); block(0,27,64,2,Color(0xFF576168)) }
            else -> { block(7,9,9,14,Color(0xFF33444D)); block(19,5,12,18,Color(0xFF3B4B53)); block(0,26,64,2,PixelColors.Cyan) }
        }
    }
}
