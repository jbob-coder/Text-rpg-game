package com.thegame.rpg.ui

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Shapes
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.unit.sp

object PixelColors {
    val Ink = Color(0xFF10151A)
    val Deep = Color(0xFF172128)
    val Panel = Color(0xFF22303A)
    val PanelAlt = Color(0xFF2D3D48)
    val Paper = Color(0xFFE9E2CC)
    val Muted = Color(0xFF9FB0B9)
    val Cyan = Color(0xFF63D8D1)
    val Gold = Color(0xFFE2B65F)
    val Danger = Color(0xFFD66B66)
    // Muted, material-oriented resource accents. Keep the HUD readable without
    // pushing the game's overall presentation toward neon/cyberpunk shorthand.
    val Health = Color(0xFFC96A62)
    val Stamina = Color(0xFF8FAF70)
    val Focus = Color(0xFF6F9FB5)
    val Resolve = Color(0xFFC29A62)
    val Disabled = Color(0xFF59666D)
}

private val PixelColorScheme = darkColorScheme(
    primary = PixelColors.Cyan,
    secondary = PixelColors.Gold,
    background = PixelColors.Ink,
    surface = PixelColors.Deep,
    onPrimary = PixelColors.Ink,
    onSecondary = PixelColors.Ink,
    onBackground = PixelColors.Paper,
    onSurface = PixelColors.Paper,
    error = PixelColors.Danger,
)

@Composable
fun PixelTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = PixelColorScheme,
        shapes = Shapes(),
        typography = MaterialTheme.typography.copy(
            headlineLarge = TextStyle(fontFamily = FontFamily.Monospace, fontSize = 28.sp, lineHeight = 32.sp),
            headlineMedium = TextStyle(fontFamily = FontFamily.Monospace, fontSize = 22.sp, lineHeight = 26.sp),
            titleLarge = TextStyle(fontFamily = FontFamily.Monospace, fontSize = 18.sp, lineHeight = 22.sp),
            bodyLarge = TextStyle(fontFamily = FontFamily.Monospace, fontSize = 18.sp, lineHeight = 27.sp),
            bodyMedium = TextStyle(fontFamily = FontFamily.Monospace, fontSize = 15.sp, lineHeight = 21.sp),
            labelLarge = TextStyle(fontFamily = FontFamily.Monospace, fontSize = 14.sp),
        ),
        content = content,
    )
}

@Composable
fun TheGamePixelTheme(content: @Composable () -> Unit) = PixelTheme(content)
