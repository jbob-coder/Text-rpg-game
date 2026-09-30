package com.thegame.rpg.ui

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.BoxWithConstraints
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.unit.dp
import com.thegame.rpg.engine.GameSnapshot
import java.math.BigDecimal

internal fun statValue(value: Double): String =
    BigDecimal.valueOf(value).stripTrailingZeros().toPlainString()

internal fun signedStatValue(value: Double): String =
    if (value > 0) "+${statValue(value)}" else statValue(value)

internal fun equipmentSlotLabel(slot: String): String = when (slot) {
    "body" -> "Chest"
    "ring_1" -> "Ring I"
    "ring_2" -> "Ring II"
    "accessory_1" -> "Accessory I"
    "accessory_2" -> "Accessory II"
    else -> slot.replace('_', ' ').replaceFirstChar { it.uppercase() }
}

@Composable
internal fun PlayerStatusSummary(snapshot: GameSnapshot) {
    PixelPanel(Modifier.fillMaxWidth().testTag("player-status-summary")) {
        Text(
            snapshot.identity.name ?: "Player",
            color = PixelColors.Paper,
            style = MaterialTheme.typography.titleLarge,
        )
        val details = listOfNotNull(
            snapshot.identity.level?.let { "Level $it" },
            snapshot.identity.path,
            snapshot.identity.origin,
            snapshot.identity.background,
        ).joinToString(" • ")
        if (details.isNotBlank()) {
            Text(details, color = PixelColors.Muted, style = MaterialTheme.typography.bodyMedium)
        }
    }
}

@Composable
internal fun StatusResourceGrid(snapshot: GameSnapshot) {
    BoxWithConstraints(Modifier.fillMaxWidth()) {
        val columns = if (maxWidth < 300.dp || LocalDensity.current.fontScale > 1.4f) 1 else 2
        Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
            snapshot.resources.chunked(columns).forEach { pair ->
                Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                    pair.forEach { resource ->
                        PixelPanel(Modifier.weight(1f)) {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                PixelUiIcon(
                                    sprite = PixelUiIconCatalog.resource(resource.id),
                                    modifier = Modifier.size(16.dp),
                                    tint = PixelColors.Cyan,
                                )
                                Spacer(Modifier.width(6.dp))
                                Text(
                                    resource.id.replaceFirstChar { it.uppercase() },
                                    color = PixelColors.Muted,
                                    style = MaterialTheme.typography.labelLarge,
                                )
                            }
                            Spacer(Modifier.height(4.dp))
                            Text(
                                "${statValue(resource.current)} / ${statValue(resource.max)}",
                                color = PixelColors.Paper,
                                style = MaterialTheme.typography.titleLarge,
                                modifier = Modifier.testTag("status-resource-${resource.id}"),
                            )
                        }
                    }
                    if (pair.size < columns) Spacer(Modifier.weight(1f))
                }
            }
        }
    }
}
