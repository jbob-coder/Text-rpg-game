package com.thegame.rpg.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.BoxWithConstraints
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.selection.selectable
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.Dialog
import com.thegame.rpg.engine.GameEquipmentSlot
import com.thegame.rpg.engine.GameSnapshot

@Composable
internal fun CharacterSection(
    snapshot: GameSnapshot,
    busy: Boolean,
    onEquip: (String) -> Unit,
    onUnequip: (String) -> Unit,
) {
    var selectedId by rememberSaveable { mutableStateOf<String?>(null) }
    var detailOpen by rememberSaveable { mutableStateOf(false) }
    val slots = snapshot.inventory.equipment
    val selected = slots.firstOrNull { it.slot == selectedId }
    val midpoint = (slots.size + 1) / 2

    BoxWithConstraints(Modifier.fillMaxSize()) {
        val railWidth = if (maxWidth < 380.dp) 56.dp else 72.dp
        val surroundRig = maxWidth >= 300.dp && LocalDensity.current.fontScale <= 1.4f
        Column(
            Modifier.fillMaxSize().verticalScroll(rememberScrollState()).testTag("character-scroll"),
            verticalArrangement = Arrangement.spacedBy(8.dp),
        ) {
            PlayerStatusSummary(snapshot, chrome = PixelPanelChrome.CHARACTER)
            if (surroundRig) {
                Row(Modifier.fillMaxWidth().testTag("character-loadout-board"), horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                    Column(Modifier.width(railWidth), verticalArrangement = Arrangement.spacedBy(6.dp)) {
                        slots.take(midpoint).forEach { slot ->
                            CharacterSlotCard(slot, selectedId == slot.slot) {
                                selectedId = slot.slot
                                detailOpen = true
                            }
                        }
                    }
                    PlayerAvatarPanel(
                        identity = snapshot.identity,
                        equipment = slots,
                        conditions = snapshot.conditions,
                        modifier = Modifier.weight(1f),
                        showSummary = false,
                        panelChrome = PixelPanelChrome.CHARACTER,
                    )
                    Column(Modifier.width(railWidth), verticalArrangement = Arrangement.spacedBy(6.dp)) {
                        slots.drop(midpoint).forEach { slot ->
                            CharacterSlotCard(slot, selectedId == slot.slot) {
                                selectedId = slot.slot
                                detailOpen = true
                            }
                        }
                    }
                }
            } else {
                PlayerAvatarPanel(
                    snapshot.identity,
                    slots,
                    snapshot.conditions,
                    Modifier.fillMaxWidth(),
                    showSummary = false,
                    panelChrome = PixelPanelChrome.CHARACTER,
                )
                slots.chunked(2).forEach { pair ->
                    Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                        pair.forEach { slot ->
                            Box(Modifier.weight(1f)) {
                                CharacterSlotCard(slot, selectedId == slot.slot) {
                                    selectedId = slot.slot
                                    detailOpen = true
                                }
                            }
                        }
                        if (pair.size == 1) Spacer(Modifier.weight(1f))
                    }
                }
            }
            StatusResourceGrid(snapshot, chrome = PixelPanelChrome.CHARACTER)
            PixelPanel(
                Modifier.fillMaxWidth(),
                "Effective attributes",
                chrome = PixelPanelChrome.CHARACTER,
            ) {
                snapshot.attributes.forEach { stat ->
                    Text(
                        "${stat.name}: ${statValue(stat.effective)}",
                        color = if (stat.modified) PixelColors.Cyan else PixelColors.Paper,
                        style = MaterialTheme.typography.bodyMedium,
                    )
                }
            }
        }
    }

    if (detailOpen && selected != null) {
        Dialog(onDismissRequest = { detailOpen = false }) {
            PixelPanel(
                Modifier.fillMaxWidth().fillMaxHeight(0.85f).testTag("character-equipment-detail"),
                equipmentSlotLabel(selected.slot),
                chrome = PixelPanelChrome.CHARACTER,
            ) {
                Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()), verticalArrangement = Arrangement.spacedBy(8.dp)) {
                    if (selected.equipped) {
                        Text(selected.name ?: "Equipped item", color = PixelColors.Paper, style = MaterialTheme.typography.titleLarge)
                        selected.quality?.let {
                            Text(it.replaceFirstChar { c -> c.uppercase() }, color = PixelColors.Gold, style = MaterialTheme.typography.labelLarge)
                        }
                        Text("Equipped", color = PixelColors.Cyan, style = MaterialTheme.typography.bodyMedium)
                        Text("CURRENT ATTRIBUTE & SKILL BONUSES", color = PixelColors.Gold, style = MaterialTheme.typography.labelLarge)
                        val bonuses = buildList {
                            snapshot.attributes.forEach { stat ->
                                stat.contributions.filter { it.kind == "equipment" && it.slot == selected.slot }.forEach {
                                    add("${stat.name}: ${signedStatValue(it.value)}")
                                }
                            }
                            snapshot.skills.forEach { skill ->
                                skill.contributions.filter { it.kind == "equipment" && it.slot == selected.slot }.forEach {
                                    add("${skill.name}: ${signedStatValue(it.value)}")
                                }
                            }
                        }
                        if (bonuses.isEmpty()) Text("No listed attribute or skill bonuses.", color = PixelColors.Muted, style = MaterialTheme.typography.bodyMedium)
                        bonuses.forEach {
                            Text(it, color = PixelColors.Cyan, style = MaterialTheme.typography.bodyMedium)
                        }
                        CharacterActionButton("UNEQUIP", !busy, "character-unequip") { onUnequip(selected.slot) }
                    } else {
                        Text("Empty slot", color = PixelColors.Muted, style = MaterialTheme.typography.bodyMedium)
                    }
                    val candidates = snapshot.inventory.items.filter { it.equippable && it.slot == selected.slot }
                    if (candidates.isNotEmpty()) {
                        Text("FROM YOUR BAG", color = PixelColors.Gold, style = MaterialTheme.typography.labelLarge)
                        candidates.forEach { item ->
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                PixelItemIcon(item.id, item.quality, Modifier.size(40.dp))
                                Spacer(Modifier.width(8.dp))
                                Text(item.name, color = PixelColors.Paper, style = MaterialTheme.typography.bodyMedium, modifier = Modifier.weight(1f))
                            }
                            CharacterActionButton("EQUIP", !busy, "character-equip-${item.id}") { onEquip(item.id) }
                        }
                    } else if (!selected.equipped) {
                        Text("No carried item fits this slot.", color = PixelColors.Muted, style = MaterialTheme.typography.bodyMedium)
                    }
                    CharacterActionButton("CLOSE", true, "character-detail-close") { detailOpen = false }
                }
            }
        }
    }
}

@Composable
private fun CharacterSlotCard(slot: GameEquipmentSlot, active: Boolean, onSelect: () -> Unit) {
    val label = equipmentSlotLabel(slot.slot)
    val description = "$label: ${if (slot.equipped) slot.name ?: "Equipped item" else "Empty"}"
    Column(
        Modifier.fillMaxWidth()
            .background(PixelColors.Panel)
            .border(2.dp, if (active) PixelColors.Gold else if (slot.equipped) PixelColors.Cyan else PixelColors.Muted)
            .selectable(active, role = Role.Button, onClick = onSelect)
            .semantics { contentDescription = description }
            .heightIn(min = 64.dp)
            .padding(4.dp)
            .testTag("character-slot-${slot.slot}"),
        horizontalAlignment = Alignment.CenterHorizontally,
    ) {
        if (slot.equipped && PixelAssetCatalog.itemIcon(slot.itemId ?: "") != null) {
            PixelItemIcon(slot.itemId ?: "", slot.quality, Modifier.size(28.dp))
        } else {
            PixelUiIcon(PixelEquipmentSlotCatalog.slot(slot.slot), Modifier.size(24.dp), tint = PixelColors.Muted)
        }
        Text(label, color = PixelColors.Paper, style = MaterialTheme.typography.labelLarge)
    }
}

@Composable
private fun CharacterActionButton(label: String, enabled: Boolean, tag: String, onClick: () -> Unit) {
    Box(
        Modifier.fillMaxWidth().background(PixelColors.PanelAlt)
            .border(2.dp, if (enabled) PixelColors.Cyan else PixelColors.Disabled)
            .clickable(enabled = enabled, role = Role.Button, onClick = onClick)
            .heightIn(min = 48.dp).padding(12.dp).testTag(tag),
        contentAlignment = Alignment.Center,
    ) {
        Text(label, color = if (enabled) PixelColors.Paper else PixelColors.Disabled, style = MaterialTheme.typography.labelLarge)
    }
}
