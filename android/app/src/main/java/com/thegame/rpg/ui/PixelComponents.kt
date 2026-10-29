package com.thegame.rpg.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.unit.dp
import com.thegame.rpg.engine.GameChoice

/**
 * Historical panel names stay temporarily source-compatible with the Compose
 * screens. None of the cases selects art, sprites, character portraits or animation.
 */
enum class PixelPanelChrome {
    STORY, CHARACTER, STATS, INVENTORY, QUEST, MAP, SETTINGS, DEVELOPER, MODAL,
}

/** Text layout container; there are no sprite/chrome asset lookups. */
@Composable
fun PixelPanel(
    modifier: Modifier = Modifier,
    title: String? = null,
    chrome: PixelPanelChrome = PixelPanelChrome.STORY,
    content: @Composable () -> Unit,
) {
    Column(
        modifier = modifier
            .background(PixelColors.Panel)
            .border(1.dp, PixelColors.Muted)
            .padding(12.dp),
    ) {
        if (title != null) {
            Text(text = title.uppercase(), color = PixelColors.Cyan,
                style = MaterialTheme.typography.labelLarge)
            Spacer(Modifier.height(8.dp))
        }
        content()
    }
}

/** Choice visibility/enabled state comes exclusively from the engine snapshot. */
@Composable
fun PixelChoiceCard(choice: GameChoice, busy: Boolean, onClick: () -> Unit) {
    val enabled = choice.enabled && !busy
    Column(
        modifier = Modifier
            .fillMaxWidth()
            .testTag("choice-${choice.id}")
            .background(PixelColors.PanelAlt)
            .border(1.dp, if (enabled) PixelColors.Cyan else PixelColors.Disabled)
            .clickable(enabled = enabled, role = Role.Button, onClick = onClick)
            .padding(horizontal = 14.dp, vertical = 12.dp),
    ) {
        Text(
            text = if (enabled) "> ${choice.text}" else "× ${choice.text}",
            color = if (enabled) PixelColors.Paper else PixelColors.Muted,
            style = MaterialTheme.typography.bodyMedium,
        )
        if (!choice.enabled && choice.disabledReason != null) {
            Spacer(Modifier.height(4.dp))
            Text(choice.disabledReason, color = PixelColors.Muted,
                style = MaterialTheme.typography.labelLarge)
        }
    }
}
