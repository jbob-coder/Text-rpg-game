package com.thegame.rpg.ui

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.unit.dp

@Composable
fun SceneIllustration(
    locationId: String,
    modifier: Modifier = Modifier,
) {
    Canvas(
        modifier = modifier
            .testTag("scene-illustration")
            .background(PixelColors.Deep)
            .border(2.dp, PixelColors.Muted),
    ) {
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
