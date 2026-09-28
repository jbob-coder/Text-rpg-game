package com.thegame.rpg.ui

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.aspectRatio
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.drawscope.translate
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.unit.dp
import com.thegame.rpg.engine.GameChoice
import com.thegame.rpg.engine.GameEquipmentSlot
import com.thegame.rpg.engine.GameIdentity

@Composable
fun PixelPanel(
    modifier: Modifier = Modifier,
    title: String? = null,
    content: @Composable () -> Unit,
) {
    Column(
        modifier = modifier
            .background(PixelColors.Panel)
            .border(2.dp, PixelColors.Muted)
            .padding(12.dp),
    ) {
        if (title != null) {
            Text(text = title.uppercase(), color = PixelColors.Cyan, style = MaterialTheme.typography.labelLarge)
            Spacer(modifier = Modifier.height(8.dp))
        }
        content()
    }
}

@Composable
fun PixelChoiceCard(choice: GameChoice, busy: Boolean, onClick: () -> Unit) {
    val enabled = choice.enabled && !busy
    val border = if (enabled) PixelColors.Cyan else PixelColors.Disabled
    val background = if (enabled) PixelColors.PanelAlt else PixelColors.Deep

    Column(
        modifier = Modifier
            .fillMaxWidth()
            .testTag("choice-${choice.id}")
            .background(background)
            .border(2.dp, border)
            .clickable(enabled = enabled, role = Role.Button, onClick = onClick)
            .padding(horizontal = 14.dp, vertical = 12.dp),
    ) {
        Text(
            text = if (enabled) "> ${choice.text}" else "× ${choice.text}",
            color = if (enabled) PixelColors.Paper else PixelColors.Muted,
            style = MaterialTheme.typography.bodyMedium,
        )
        if (!choice.enabled && choice.disabledReason != null) {
            Spacer(modifier = Modifier.height(4.dp))
            Text(text = choice.disabledReason, color = PixelColors.Muted, style = MaterialTheme.typography.labelLarge)
        }
    }
}

@Composable
fun PlayerAvatarPanel(
    identity: GameIdentity,
    equipment: List<GameEquipmentSlot> = emptyList(),
    modifier: Modifier = Modifier,
    compact: Boolean = false,
) {
    val equippedSlots = equipment
        .filter { it.equipped }
        .associateBy { it.slot }

    PixelPanel(modifier = modifier.testTag("player-avatar"), title = identity.name ?: "Player") {
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .then(
                    if (compact) Modifier.height(150.dp)
                    else Modifier.aspectRatio(0.82f)
                )
                .background(PixelColors.Deep)
                .border(2.dp, PixelColors.Cyan),
            contentAlignment = Alignment.Center,
        ) {
            Canvas(
                modifier = if (compact) {
                    Modifier.height(134.dp).aspectRatio(0.62f)
                } else {
                    Modifier.fillMaxWidth(0.78f).aspectRatio(0.62f)
                }
            ) {
                val px = minOf(size.width / 18f, size.height / 30f)
                fun block(x: Int, y: Int, w: Int, h: Int, color: Color) {
                    drawRect(color, Offset(x * px, y * px), Size(w * px, h * px))
                }

                val ox = ((size.width / px - 18f) / 2f).coerceAtLeast(0f)
                translate(left = ox * px) {
                    // Grounding shadow.
                    block(4, 28, 10, 2, Color(0xFF0A0E11))

                    // Base body. Equipment is drawn over this layer and never owns state.
                    block(5, 20, 3, 7, Color(0xFF27333C))
                    block(10, 20, 3, 7, Color(0xFF27333C))
                    block(4, 26, 4, 2, Color(0xFF161C20))
                    block(10, 26, 4, 2, Color(0xFF161C20))
                    block(4, 10, 10, 10, Color(0xFF33434C))
                    block(7, 14, 4, 4, Color(0xFF263B44))
                    block(2, 11, 2, 8, Color(0xFF9C725B))
                    block(14, 11, 2, 8, Color(0xFF9C725B))
                    block(6, 3, 6, 7, Color(0xFFAD7D62))
                    block(5, 2, 8, 3, Color(0xFF20262B))
                    block(5, 4, 2, 3, Color(0xFF20262B))
                    block(7, 6, 1, 1, PixelColors.Paper)
                    block(10, 6, 1, 1, PixelColors.Paper)

                    // Equipment paper-doll layers, driven only by player-safe equipped slots.
                    if ("body" in equippedSlots) {
                        block(3, 10, 12, 10, Color(0xFF3B5963))
                        block(5, 11, 8, 2, PixelColors.Cyan)
                        block(3, 15, 2, 4, Color(0xFF2A414A))
                        block(13, 15, 2, 4, Color(0xFF2A414A))
                    }
                    if ("hands" in equippedSlots) {
                        block(2, 16, 2, 4, Color(0xFF27343B))
                        block(14, 16, 2, 4, Color(0xFF27343B))
                        block(1, 18, 2, 2, Color(0xFF53656E))
                        block(15, 18, 2, 2, Color(0xFF53656E))
                    }
                    if ("head" in equippedSlots) {
                        block(5, 2, 8, 3, Color(0xFF4A5960))
                        block(6, 1, 6, 2, Color(0xFF36454C))
                        block(5, 5, 2, 2, Color(0xFF4A5960))
                        block(11, 5, 2, 2, Color(0xFF4A5960))
                    }
                    if ("legs" in equippedSlots) {
                        block(4, 19, 4, 7, Color(0xFF3D4D55))
                        block(10, 19, 4, 7, Color(0xFF3D4D55))
                        block(8, 20, 2, 2, PixelColors.Cyan)
                    }
                    if ("feet" in equippedSlots) {
                        block(3, 25, 5, 3, Color(0xFF20282D))
                        block(10, 25, 5, 3, Color(0xFF20282D))
                        block(3, 27, 5, 1, PixelColors.Gold)
                        block(10, 27, 5, 1, PixelColors.Gold)
                    }
                    if ("neck" in equippedSlots) {
                        block(8, 9, 2, 1, PixelColors.Gold)
                        block(8, 10, 2, 2, Color(0xFF7E6A42))
                    }
                    if ("ring_1" in equippedSlots) {
                        block(1, 19, 1, 1, PixelColors.Gold)
                    }
                    if ("ring_2" in equippedSlots) {
                        block(16, 19, 1, 1, PixelColors.Cyan)
                    }
                    if ("accessory_1" in equippedSlots) {
                        block(4, 18, 10, 2, Color(0xFF6B5942))
                        block(12, 19, 3, 5, Color(0xFF554632))
                    }
                    if ("accessory_2" in equippedSlots) {
                        block(3, 12, 1, 9, PixelColors.Gold)
                        block(14, 12, 1, 9, PixelColors.Gold)
                    }
                    if ("main_hand" in equippedSlots) {
                        block(16, 13, 1, 12, PixelColors.Gold)
                        block(15, 13, 3, 2, PixelColors.Gold)
                    }
                    if ("off_hand" in equippedSlots) {
                        block(0, 13, 2, 9, Color(0xFF4B6773))
                        block(0, 12, 3, 2, PixelColors.Cyan)
                    }
                }
            }
        }

        Spacer(modifier = Modifier.height(8.dp))
        val descriptor = listOfNotNull(
            identity.path,
            identity.level?.let { "LV $it" },
            identity.origin,
        ).joinToString(" • ")
        Text(
            text = descriptor.ifBlank { "ADVENTURER // LOADOUT ACTIVE" },
            color = PixelColors.Muted,
            style = MaterialTheme.typography.labelLarge,
        )

        val visibleGear = equipment
            .filter { it.equipped }
            .map { slotDisplayNameForAvatar(it.slot) }
        if (visibleGear.isNotEmpty()) {
            Spacer(modifier = Modifier.height(4.dp))
            Text(
                text = "VISIBLE GEAR // " + visibleGear.joinToString(" • "),
                color = PixelColors.Gold,
                style = MaterialTheme.typography.labelLarge,
                modifier = Modifier.testTag("avatar-visible-gear"),
            )
        }
    }
}

private fun slotDisplayNameForAvatar(slot: String): String = when (slot) {
    "body" -> "CHEST"
    "ring_1" -> "RING I"
    "ring_2" -> "RING II"
    "accessory_1" -> "ACCESSORY I"
    "accessory_2" -> "ACCESSORY II"
    else -> slot.replace('_', ' ').uppercase()
}
