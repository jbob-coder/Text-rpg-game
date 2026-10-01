package com.thegame.rpg.ui

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
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
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
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
import com.thegame.rpg.engine.GameCondition
import com.thegame.rpg.engine.GameEquipmentSlot
import com.thegame.rpg.engine.GameIdentity
import kotlinx.coroutines.delay

@Composable
fun PixelPanel(
    modifier: Modifier = Modifier,
    title: String? = null,
    chrome: PixelPanelChrome = PixelPanelChrome.STORY,
    content: @Composable () -> Unit,
) {
    Column(
        modifier = modifier
            .pixelChrome(PixelUiChromeCatalog.panel(chrome))
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
    val chrome = if (enabled) {
        PixelUiChromeCatalog.choiceEnabled
    } else {
        PixelUiChromeCatalog.choiceDisabled
    }

    Column(
        modifier = Modifier
            .fillMaxWidth()
            .testTag("choice-${choice.id}")
            .pixelChrome(chrome)
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
    conditions: List<GameCondition> = emptyList(),
    modifier: Modifier = Modifier,
    compact: Boolean = false,
    showSummary: Boolean = true,
    panelChrome: PixelPanelChrome = PixelPanelChrome.STORY,
) {
    val equippedOverlays = equipment
        .filter { it.equipped }
        .associateBy { it.slot }
        .values
        .mapNotNull { slot -> PixelAssetCatalog.equipmentOverlay(slot.itemId, slot.slot) }
        .sortedBy { it.zOrder }
    val traceStrainFrames = PixelTraceStrainCatalog.avatarForConditions(
        conditions.map { it.id }.toSet()
    )
    var traceStrainFrameIndex by remember(traceStrainFrames != null) { mutableStateOf(0) }

    LaunchedEffect(traceStrainFrames) {
        if (traceStrainFrames.isNullOrEmpty()) {
            traceStrainFrameIndex = 0
            return@LaunchedEffect
        }

        traceStrainFrameIndex = 0
        while (true) {
            delay(220L)
            traceStrainFrameIndex = (traceStrainFrameIndex + 1) % traceStrainFrames.size
        }
    }

    PixelPanel(
        modifier = modifier.testTag("player-avatar"),
        title = identity.name ?: "Player",
        chrome = panelChrome,
    ) {
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .then(
                    if (compact) Modifier.height(150.dp)
                    else Modifier.aspectRatio(0.82f)
                )
                .background(PixelColors.Deep)
                .border(2.dp, PixelColors.Cyan)
                .then(
                    if (equippedOverlays.isNotEmpty()) Modifier.testTag("avatar-visible-gear")
                    else Modifier
                ),
            contentAlignment = Alignment.Center,
        ) {
            Canvas(
                modifier = (
                    if (compact) {
                        Modifier.height(134.dp).aspectRatio(0.67f)
                    } else {
                        Modifier.fillMaxWidth(0.78f).aspectRatio(0.67f)
                    }
                ).testTag(
                    if (traceStrainFrames != null) "player-avatar-canvas-trace-strain"
                    else "player-avatar-canvas"
                )
            ) {
                val px = floor(minOf(size.width / 32f, size.height / 48f)).coerceAtLeast(1f)
                val ox = floor((size.width - 32f * px) / 2f)
                val oy = floor((size.height - 48f * px) / 2f)

                // Asset 192: bottom-anchor the 32x16 staging shadow so its last source
                // row aligns with the shared player ground pivot at y=47.
                drawPixelSprite(
                    sprite = PixelCharacterStagingCatalog.mediumGroundShadow,
                    pixelSize = px,
                    originX = ox,
                    originY = oy + 32f * px,
                )

                drawPixelSprite(PixelAssetCatalog.playerFrontBase, px, ox, oy)
                drawPixelSprite(PixelAssetCatalog.playerHairTechnicalPlaceholder, px, ox, oy)

                // Every equipped visual is a transparent 32x48 paper-doll overlay aligned to
                // the same body origin. Unmapped equipment remains logically equipped but receives
                // no invented placeholder geometry.
                equippedOverlays.forEach { overlay ->
                    drawPixelSprite(overlay.sprite, px, ox, oy)
                }

                traceStrainFrames?.getOrNull(traceStrainFrameIndex)?.let { strainFx ->
                    drawPixelSprite(strainFx, px, ox, oy)
                }
            }
        }

        if (showSummary) {
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

            val visibleGear = equippedOverlays
                .map { overlay -> slotDisplayNameForAvatar(overlay.slot) }
            if (visibleGear.isNotEmpty()) {
                Spacer(modifier = Modifier.height(4.dp))
                Text(
                    text = "VISIBLE GEAR // " + visibleGear.joinToString(" • "),
                    color = PixelColors.Gold,
                    style = MaterialTheme.typography.labelLarge,
                )
            }
        }
    }
}

@Composable
fun PixelUiIcon(
    sprite: PixelSprite?,
    modifier: Modifier = Modifier,
    tint: Color? = null,
    testTag: String? = null,
) {
    val taggedModifier = if (testTag != null) modifier.testTag(testTag) else modifier

    Canvas(taggedModifier) {
        if (sprite == null) return@Canvas
        val px = floor(
            minOf(size.width / sprite.width.toFloat(), size.height / sprite.height.toFloat())
        ).coerceAtLeast(1f)
        val ox = floor((size.width - sprite.width * px) / 2f)
        val oy = floor((size.height - sprite.height * px) / 2f)
        drawPixelSprite(
            sprite = sprite,
            pixelSize = px,
            originX = ox,
            originY = oy,
            tint = tint,
        )
    }
}

@Composable
fun PixelItemIcon(
    itemId: String,
    quality: String? = null,
    modifier: Modifier = Modifier,
) {
    val sprite = PixelAssetCatalog.itemIcon(itemId)
    val qualityFrame = PixelItemQualityFrameCatalog.forQuality(quality)
    Box(
        modifier = modifier
            .background(PixelColors.Deep)
            .border(1.dp, PixelColors.Muted)
            .testTag("item-icon-$itemId"),
        contentAlignment = Alignment.Center,
    ) {
        if (sprite != null) {
            Canvas(Modifier.fillMaxSize()) {
                val px = floor(minOf(size.width / sprite.width, size.height / sprite.height)).coerceAtLeast(1f)
                val ox = floor((size.width - sprite.width * px) / 2f)
                val oy = floor((size.height - sprite.height * px) / 2f)
                drawPixelSprite(sprite, px, ox, oy)
            }
            qualityFrame?.let { frame ->
                Canvas(
                    Modifier
                        .fillMaxSize()
                        .testTag("item-quality-frame-${quality?.lowercase()}")
                ) {
                    val px = floor(
                        minOf(size.width / frame.width, size.height / frame.height)
                    ).coerceAtLeast(1f)
                    val ox = floor((size.width - frame.width * px) / 2f)
                    val oy = floor((size.height - frame.height * px) / 2f)
                    drawPixelSprite(frame, px, ox, oy)
                }
            }
        } else {
            Text(
                text = "?",
                color = PixelColors.Muted,
                style = MaterialTheme.typography.labelLarge,
            )
        }
    }
}

internal fun DrawScope.drawPixelSprite(
    sprite: PixelSprite,
    pixelSize: Float,
    originX: Float,
    originY: Float,
    tint: Color? = null,
) {
    sprite.rows.forEachIndexed { y, row ->
        row.forEachIndexed { x, key ->
            val color = if (key == PixelSprite.TRANSPARENT_PIXEL) null else tint ?: sprite.palette[key]
            if (color != null) {
                drawRect(
                    color = color,
                    topLeft = Offset(originX + x * pixelSize, originY + y * pixelSize),
                    size = Size(pixelSize, pixelSize),
                )
            }
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
