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
import androidx.compose.ui.graphics.drawscope.DrawScope
import kotlin.math.floor
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
                    Modifier.height(134.dp).aspectRatio(0.67f)
                } else {
                    Modifier.fillMaxWidth(0.78f).aspectRatio(0.67f)
                }
            ) {
                val px = floor(minOf(size.width / 32f, size.height / 48f)).coerceAtLeast(1f)
                val ox = floor((size.width - 32f * px) / 2f)
                val oy = floor((size.height - 48f * px) / 2f)

                fun block(x: Int, y: Int, w: Int, h: Int, color: Color) {
                    drawRect(
                        color = color,
                        topLeft = Offset(ox + x * px, oy + y * px),
                        size = Size(w * px, h * px),
                    )
                }

                // Grounding shadow is a presentation layer rather than part of the body asset.
                block(8, 46, 17, 2, Color(0xFF0A0E11))

                drawPixelSprite(PixelAssetCatalog.playerFrontBase, px, ox, oy)
                drawPixelSprite(PixelAssetCatalog.playerHairTechnicalPlaceholder, px, ox, oy)

                // Wave A: the Depot Jacket is the first production equipment layer driven by
                // exact item ID + authoritative equipped slot. Other slots keep temporary
                // coordinate overlays until their own catalog assets replace them.
                equippedSlots["body"]?.let { bodySlot ->
                    PixelAssetCatalog.equipmentLayer(bodySlot.itemId, bodySlot.slot)?.let { sprite ->
                        drawPixelSprite(sprite, px, ox, oy)
                    }
                }

                if ("hands" in equippedSlots) {
                    block(5, 30, 4, 5, Color(0xFF27343B))
                    block(23, 30, 4, 5, Color(0xFF27343B))
                    block(5, 33, 4, 2, Color(0xFF53656E))
                    block(23, 33, 4, 2, Color(0xFF53656E))
                }
                if ("head" in equippedSlots) {
                    block(10, 2, 12, 4, Color(0xFF4A5960))
                    block(11, 1, 10, 2, Color(0xFF36454C))
                    block(10, 6, 3, 3, Color(0xFF4A5960))
                    block(19, 6, 3, 3, Color(0xFF4A5960))
                }
                if ("legs" in equippedSlots) {
                    block(10, 29, 6, 14, Color(0xFF3D4D55))
                    block(17, 29, 6, 14, Color(0xFF3D4D55))
                    block(15, 31, 2, 3, PixelColors.Cyan)
                }
                if ("feet" in equippedSlots) {
                    block(8, 43, 7, 4, Color(0xFF20282D))
                    block(18, 43, 7, 4, Color(0xFF20282D))
                    block(8, 46, 7, 1, PixelColors.Gold)
                    block(18, 46, 7, 1, PixelColors.Gold)
                }
                if ("neck" in equippedSlots) {
                    block(15, 13, 2, 2, PixelColors.Gold)
                    block(15, 15, 2, 2, Color(0xFF7E6A42))
                }
                if ("ring_1" in equippedSlots) {
                    block(5, 33, 1, 1, PixelColors.Gold)
                }
                if ("ring_2" in equippedSlots) {
                    block(26, 33, 1, 1, PixelColors.Cyan)
                }
                if ("accessory_1" in equippedSlots) {
                    block(10, 27, 12, 2, Color(0xFF6B5942))
                    block(21, 28, 4, 7, Color(0xFF554632))
                }
                if ("accessory_2" in equippedSlots) {
                    block(7, 19, 1, 14, PixelColors.Gold)
                    block(24, 19, 1, 14, PixelColors.Gold)
                }
                if ("main_hand" in equippedSlots) {
                    block(27, 22, 2, 18, PixelColors.Gold)
                    block(26, 22, 4, 3, PixelColors.Gold)
                }
                if ("off_hand" in equippedSlots) {
                    block(2, 22, 3, 14, Color(0xFF4B6773))
                    block(2, 21, 5, 3, PixelColors.Cyan)
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

private fun DrawScope.drawPixelSprite(
    sprite: PixelSprite,
    pixelSize: Float,
    originX: Float,
    originY: Float,
) {
    sprite.rows.forEachIndexed { y, row ->
        row.forEachIndexed { x, key ->
            val color = sprite.palette[key] ?: return@forEachIndexed
            drawRect(
                color = color,
                topLeft = Offset(originX + x * pixelSize, originY + y * pixelSize),
                size = Size(pixelSize, pixelSize),
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
