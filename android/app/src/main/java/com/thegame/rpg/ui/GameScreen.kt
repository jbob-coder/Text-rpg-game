package com.thegame.rpg.ui

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.gestures.detectTapGestures
import androidx.compose.foundation.horizontalScroll
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
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.layout.widthIn
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.Modifier
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.unit.dp
import com.thegame.rpg.GameUiState
import com.thegame.rpg.boot.BootState
import com.thegame.rpg.engine.GameEquipmentSlot
import com.thegame.rpg.engine.GameInventoryItem
import com.thegame.rpg.engine.GameSnapshot
import com.thegame.rpg.engine.GameStatInspection
import kotlinx.coroutines.delay
import kotlin.math.roundToInt

enum class GameSection(val label: String) {
    STORY("Story"),
    CHARACTER("Character"),
    STATS("Stats"),
    INVENTORY("Inventory"),
    QUESTS("Quests"),
    MAP("Map"),
    MORE("More"),
}

@Composable
fun TheGameRoot(
    uiState: GameUiState,
    onChoice: (String) -> Unit,
    onSave: () -> Unit,
    onLoad: () -> Unit,
    onNarrate: (String) -> Boolean,
    onReplayNarration: () -> Boolean,
    onStopNarration: () -> Unit,
    autoReadNarration: Boolean,
    onAutoReadChange: (Boolean) -> Unit,
    narrationRate: Float,
    onNarrationRateChange: (Float) -> Unit,
    textDelayMs: Int,
    onTextDelayChange: (Int) -> Unit,
    onCheat: (String) -> Unit,
    onEquip: (String) -> Unit,
    onUnequip: (String) -> Unit,
    onInspectStatus: (String) -> Unit,
    onTravel: (String) -> Unit,
    onTravelTransitionFinished: (Long) -> Unit,
) {
    val snapshot = uiState.snapshot
    if (uiState.bootState == BootState.Ready && snapshot != null) {
        Box(Modifier.fillMaxSize()) {
            PixelGameShell(
                snapshot,
                uiState.busy,
                uiState.statInspectionPath,
                uiState.statInspection,
                uiState.statInspectionBusy,
                uiState.statInspectionError,
                onChoice,
                onSave,
                onLoad,
                onNarrate,
                onReplayNarration,
                onStopNarration,
                autoReadNarration,
                onAutoReadChange,
                narrationRate,
                onNarrationRateChange,
                textDelayMs,
                onTextDelayChange,
                onCheat,
                onEquip,
                onUnequip,
                onInspectStatus,
                onTravel,
            )
            uiState.travelTransition?.let { transition ->
                MapTravelTransitionOverlay(
                    transition = transition,
                    onFinished = onTravelTransitionFinished,
                    modifier = Modifier.fillMaxSize(),
                )
            }
        }
    } else {
        PixelBootScreen(uiState.bootState)
    }
}

/** Stable UI contract used by Compose instrumentation tests and preview clients. */
@Composable
fun GameScreen(
    snapshot: GameSnapshot,
    busy: Boolean,
    onChoice: (String) -> Unit,
    onNavigate: (String) -> Unit,
) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(PixelColors.Ink)
            .padding(8.dp),
    ) {
        TopStatusBar(snapshot, onSettings = { onNavigate("More") })
        Spacer(Modifier.height(8.dp))
        Box(modifier = Modifier.weight(1f)) {
            StorySection(
                snapshot = snapshot,
                busy = busy,
                onChoice = onChoice,
                onNarrate = { false },
                textDelayMs = 0,
            )
        }
        Spacer(Modifier.height(8.dp))
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .horizontalScroll(rememberScrollState()),
            horizontalArrangement = Arrangement.spacedBy(4.dp),
        ) {
            listOf("Stats", "Inventory", "Quests", "Map", "More").forEach { label ->
                PixelNavButton(label = label, active = false) { onNavigate(label) }
            }
        }
    }
}

@Composable
private fun PixelBootScreen(state: BootState) {
    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(PixelColors.Ink)
            .padding(24.dp),
        contentAlignment = Alignment.Center,
    ) {
        PixelPanel {
            Text("THE GAME", color = PixelColors.Gold, style = MaterialTheme.typography.headlineLarge)
            Spacer(Modifier.height(10.dp))
            Text("[${state.stageId}]", color = PixelColors.Cyan, style = MaterialTheme.typography.bodyMedium)
            Spacer(Modifier.height(8.dp))
            if (state is BootState.Error) {
                Text(state.publicMessage, color = PixelColors.Danger, style = MaterialTheme.typography.bodyLarge)
            } else {
                Text("Loading world data...", color = PixelColors.Muted, style = MaterialTheme.typography.bodyMedium)
            }
        }
    }
}

@Composable
private fun PixelGameShell(
    snapshot: GameSnapshot,
    busy: Boolean,
    statInspectionPath: String?,
    statInspection: GameStatInspection?,
    statInspectionBusy: Boolean,
    statInspectionError: String?,
    onChoice: (String) -> Unit,
    onSave: () -> Unit,
    onLoad: () -> Unit,
    onNarrate: (String) -> Boolean,
    onReplayNarration: () -> Boolean,
    onStopNarration: () -> Unit,
    autoReadNarration: Boolean,
    onAutoReadChange: (Boolean) -> Unit,
    narrationRate: Float,
    onNarrationRateChange: (Float) -> Unit,
    textDelayMs: Int,
    onTextDelayChange: (Int) -> Unit,
    onCheat: (String) -> Unit,
    onEquip: (String) -> Unit,
    onUnequip: (String) -> Unit,
    onInspectStatus: (String) -> Unit,
    onTravel: (String) -> Unit,
) {
    var section by remember { mutableStateOf(GameSection.STORY) }
    var settingsOpen by remember { mutableStateOf(false) }
    var lastSceneId by remember { mutableStateOf(snapshot.sceneId) }

    LaunchedEffect(snapshot.sceneId) {
        if (snapshot.sceneId != lastSceneId) {
            section = GameSection.STORY
            settingsOpen = false
            lastSceneId = snapshot.sceneId
        }
    }

    LaunchedEffect(snapshot.sceneId, autoReadNarration) {
        if (autoReadNarration) {
            onNarrate(snapshot.body)
        }
    }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(PixelColors.Ink)
            .padding(8.dp),
    ) {
        TopStatusBar(snapshot) { settingsOpen = !settingsOpen }
        Spacer(Modifier.height(8.dp))
        Box(Modifier.weight(1f)) {
            if (settingsOpen) {
                SettingsPanel(
                    snapshot = snapshot,
                    onSave = onSave,
                    onLoad = onLoad,
                    onReplayNarration = onReplayNarration,
                    onStopNarration = onStopNarration,
                    autoReadNarration = autoReadNarration,
                    onAutoReadChange = onAutoReadChange,
                    narrationRate = narrationRate,
                    onNarrationRateChange = onNarrationRateChange,
                    textDelayMs = textDelayMs,
                    onTextDelayChange = onTextDelayChange,
                    onCheat = onCheat,
                    onClose = { settingsOpen = false },
                )
            } else {
                when (section) {
                    GameSection.STORY -> StorySection(
                        snapshot = snapshot,
                        busy = busy,
                        onChoice = onChoice,
                        onNarrate = onNarrate,
                        textDelayMs = textDelayMs,
                    )
                    GameSection.CHARACTER -> CharacterSection(
                        snapshot = snapshot,
                        busy = busy,
                        onEquip = onEquip,
                        onUnequip = onUnequip,
                    )
                    GameSection.STATS -> StatsSection(
                        snapshot = snapshot,
                        selectedPath = statInspectionPath,
                        inspection = statInspection,
                        inspectionBusy = statInspectionBusy,
                        inspectionError = statInspectionError,
                        onInspect = onInspectStatus,
                    )
                    GameSection.INVENTORY -> InventorySection(
                        snapshot = snapshot,
                        busy = busy,
                        onEquip = onEquip,
                        onUnequip = onUnequip,
                    )
                    GameSection.QUESTS -> QuestSection(snapshot)
                    GameSection.MAP -> MapSection(snapshot, busy, onTravel)
                    GameSection.MORE -> MorePanel(
                        onCharacter = { section = GameSection.CHARACTER },
                        onSettings = { settingsOpen = true },
                    )
                }
            }
        }
        Spacer(Modifier.height(8.dp))
        BottomPixelNav(section) {
            section = it
            settingsOpen = false
        }
    }
}

@Composable
private fun TopStatusBar(snapshot: GameSnapshot, onSettings: () -> Unit) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .background(PixelColors.Deep)
            .border(2.dp, PixelColors.Muted)
            .padding(horizontal = 10.dp, vertical = 8.dp),
        verticalAlignment = Alignment.CenterVertically,
    ) {
        Column(Modifier.weight(1f)) {
            Text(
                snapshot.location.replace('_', ' '),
                color = PixelColors.Cyan,
                style = MaterialTheme.typography.labelLarge,
            )
            Text(
                "TURN ${snapshot.turn}  //  ${formatGameTime(snapshot.timeMinutes)}",
                color = PixelColors.Muted,
                style = MaterialTheme.typography.labelLarge,
            )
        }
        PixelTextButton("SETTINGS", onSettings)
    }
}

@Composable
private fun StorySection(
    snapshot: GameSnapshot,
    busy: Boolean,
    onChoice: (String) -> Unit,
    onNarrate: (String) -> Boolean,
    textDelayMs: Int,
) {
    NarrativePanel(
        snapshot = snapshot,
        busy = busy,
        onChoice = onChoice,
        onNarrate = onNarrate,
        textDelayMs = textDelayMs,
        modifier = Modifier.fillMaxSize(),
    )
}

@Composable
private fun NarrativePanel(
    snapshot: GameSnapshot,
    busy: Boolean,
    onChoice: (String) -> Unit,
    onNarrate: (String) -> Boolean,
    textDelayMs: Int,
    modifier: Modifier,
) {
    var visibleChars by remember(snapshot.sceneId, snapshot.body, textDelayMs) {
        mutableStateOf(if (textDelayMs <= 0) snapshot.body.length else 0)
    }
    LaunchedEffect(snapshot.sceneId, snapshot.body, textDelayMs) {
        if (textDelayMs <= 0) {
            visibleChars = snapshot.body.length
        } else {
            visibleChars = 0
            while (visibleChars < snapshot.body.length) {
                delay(textDelayMs.toLong())
                visibleChars = (visibleChars + 3).coerceAtMost(snapshot.body.length)
            }
        }
    }
    val visibleBody = snapshot.body.take(visibleChars)

    val narrativeScroll = rememberScrollState()
    LaunchedEffect(snapshot.sceneId) {
        narrativeScroll.scrollTo(0)
    }

    PixelPanel(modifier = modifier) {
        Box(Modifier.fillMaxSize()) {
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(bottom = 22.dp)
                    .testTag("narrative-scroll")
                    .verticalScroll(narrativeScroll),
            ) {
                Text(
                    text = snapshot.title,
                    color = PixelColors.Cyan,
                    style = MaterialTheme.typography.titleLarge,
                    modifier = Modifier.testTag("scene-title"),
                )
                Spacer(Modifier.height(8.dp))
                Text(
                    text = visibleBody,
                    color = PixelColors.Paper,
                    style = MaterialTheme.typography.bodyLarge,
                    modifier = Modifier.clickable(role = Role.Button) { onNarrate(snapshot.body) },
                )
                Spacer(Modifier.height(10.dp))
                PixelTextButton("READ ALOUD") { onNarrate(snapshot.body) }
                Spacer(Modifier.height(18.dp))
                Text("DECIDE", color = PixelColors.Gold, style = MaterialTheme.typography.titleLarge)
                Spacer(Modifier.height(8.dp))
                snapshot.choices.forEach { choice ->
                    PixelChoiceCard(choice, busy) { onChoice(choice.id) }
                    Spacer(Modifier.height(8.dp))
                }
            }

            if (narrativeScroll.value < narrativeScroll.maxValue) {
                Text(
                    text = "↓",
                    color = PixelColors.Muted,
                    modifier = Modifier.align(Alignment.BottomCenter)
                        .background(PixelColors.PanelAlt)
                        .testTag("narrative-scroll-marker"),
                )
            }
        }
    }
}

@Composable
private fun SettingsPanel(
    snapshot: GameSnapshot,
    onSave: () -> Unit,
    onLoad: () -> Unit,
    onReplayNarration: () -> Boolean,
    onStopNarration: () -> Unit,
    autoReadNarration: Boolean,
    onAutoReadChange: (Boolean) -> Unit,
    narrationRate: Float,
    onNarrationRateChange: (Float) -> Unit,
    textDelayMs: Int,
    onTextDelayChange: (Int) -> Unit,
    onCheat: (String) -> Unit,
    onClose: () -> Unit,
) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState()),
        verticalArrangement = Arrangement.spacedBy(8.dp),
    ) {
        PixelPanel(title = "Settings", chrome = PixelPanelChrome.SETTINGS) {
            Text("Game settings live outside the narrative HUD.", color = PixelColors.Paper, style = MaterialTheme.typography.bodyLarge)
            Spacer(Modifier.height(12.dp))
            PixelTextButton("SAVE GAME", onSave)
            Spacer(Modifier.height(8.dp))
            PixelTextButton("LOAD / CONTINUE") {
                onLoad()
                onClose()
            }
            Spacer(Modifier.height(8.dp))
            PixelTextButton("CLOSE", onClose)
        }
        PixelPanel(title = "Narration", chrome = PixelPanelChrome.SETTINGS) {
            Text(
                "Tap the narrative text or READ ALOUD to use the device's native text-to-speech engine.",
                color = PixelColors.Muted,
                style = MaterialTheme.typography.bodyMedium,
            )
            Spacer(Modifier.height(8.dp))
            PixelTextButton("REPLAY NARRATION") { onReplayNarration() }
            Spacer(Modifier.height(8.dp))
            PixelTextButton(
                if (autoReadNarration) "AUTO-READ // ON" else "AUTO-READ // OFF"
            ) {
                onAutoReadChange(!autoReadNarration)
            }
            Spacer(Modifier.height(8.dp))
            Text(
                "VOICE SPEED // " + String.format("%.2fx", narrationRate),
                color = PixelColors.Paper,
                style = MaterialTheme.typography.bodyMedium,
            )
            Spacer(Modifier.height(6.dp))
            Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                PixelTextButton("SLOWER") {
                    onNarrationRateChange((narrationRate - 0.10f).coerceAtLeast(0.5f))
                }
                PixelTextButton("FASTER") {
                    onNarrationRateChange((narrationRate + 0.10f).coerceAtMost(1.5f))
                }
            }
            Spacer(Modifier.height(8.dp))
            Text(
                "TEXT REVEAL // " + if (textDelayMs <= 0) "INSTANT" else textDelayMs.toString() + " ms",
                color = PixelColors.Paper,
                style = MaterialTheme.typography.bodyMedium,
            )
            Spacer(Modifier.height(6.dp))
            PixelTextButton("CYCLE TEXT SPEED") {
                onTextDelayChange(
                    when (textDelayMs) {
                        0 -> 15
                        15 -> 35
                        35 -> 70
                        else -> 0
                    }
                )
            }
            Spacer(Modifier.height(8.dp))
            PixelTextButton("STOP NARRATION", onStopNarration)
        }
        PixelPanel(title = "Session", chrome = PixelPanelChrome.SETTINGS) {
            LabeledValue("Content", snapshot.contentId ?: "—")
            LabeledValue("Canon", snapshot.canonStatus ?: "—")
            LabeledValue("Scene", snapshot.sceneId)
            LabeledValue("Turn", snapshot.turn.toString())
        }
        PixelPanel(title = "Developer", chrome = PixelPanelChrome.DEVELOPER) {
            var cheatCode by remember { mutableStateOf("") }
            Text(
                "Cheats are validated by the Python game layer. Quick actions and manual codes use the same whitelist.",
                color = PixelColors.Muted,
                style = MaterialTheme.typography.bodyMedium,
            )
            Spacer(Modifier.height(8.dp))
            PixelTextButton("CHEAT // DISTRICT FREE ROAM") { onCheat("DISTRICT") }
            Spacer(Modifier.height(6.dp))
            PixelTextButton("CHEAT // FULL RESTORE") { onCheat("FULLRESTORE") }
            Spacer(Modifier.height(6.dp))
            PixelTextButton("CHEAT // DEBUG MAP") { onCheat("DEBUGMAP") }
            Spacer(Modifier.height(10.dp))
            Text(
                "Manual codes: FULLRESTORE, CLEARCONDITIONS, GIVE_RELAY, MAXATTR, DEBUGMAP, DISTRICT.",
                color = PixelColors.Muted,
                style = MaterialTheme.typography.labelLarge,
            )
            Spacer(Modifier.height(8.dp))
            OutlinedTextField(
                value = cheatCode,
                onValueChange = { cheatCode = it.uppercase() },
                label = { Text("CHEAT CODE") },
                singleLine = true,
                modifier = Modifier
                    .fillMaxWidth()
                    .testTag("cheat-input"),
            )
            Spacer(Modifier.height(8.dp))
            PixelTextButton("APPLY CHEAT") {
                if (cheatCode.isNotBlank()) {
                    onCheat(cheatCode)
                    cheatCode = ""
                }
            }
        }
    }
}

@Composable
internal fun InventorySection(
    snapshot: GameSnapshot,
    busy: Boolean,
    onEquip: (String) -> Unit,
    onUnequip: (String) -> Unit,
) {
    val slots = snapshot.inventory.equipment
    val items = snapshot.inventory.items
    var selectedSlotId by remember(slots) {
        mutableStateOf(slots.firstOrNull { it.equipped }?.slot ?: slots.firstOrNull()?.slot)
    }
    var selectedItemId by remember(items) {
        mutableStateOf(items.firstOrNull()?.id)
    }
    val selectedSlot = slots.firstOrNull { it.slot == selectedSlotId }
    val selectedItem = items.firstOrNull { it.id == selectedItemId }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState())
            .testTag("inventory-scroll"),
        verticalArrangement = Arrangement.spacedBy(8.dp),
    ) {
        PixelPanel(title = "Loadout", chrome = PixelPanelChrome.INVENTORY) {
            Row(
                modifier = Modifier.fillMaxWidth(),
                verticalAlignment = Alignment.CenterVertically,
            ) {
                PixelUiIcon(
                    sprite = PixelUiIconCatalog.navigation(GameSection.INVENTORY.label),
                    modifier = Modifier.size(20.dp),
                    tint = PixelColors.Gold,
                    testTag = "inventory-loadout-icon",
                )
                Spacer(Modifier.width(6.dp))
                Text(
                    "EQUIPPED ${slots.count { it.equipped }} / ${slots.size}",
                    color = PixelColors.Paper,
                    style = MaterialTheme.typography.labelLarge,
                )
            }
            Spacer(Modifier.height(8.dp))

            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .horizontalScroll(rememberScrollState())
                    .testTag("inventory-loadout-strip"),
                horizontalArrangement = Arrangement.spacedBy(6.dp),
            ) {
                slots.forEach { slot ->
                    InventorySlotTile(
                        slot = slot,
                        active = selectedSlotId == slot.slot,
                        modifier = Modifier.width(66.dp),
                    ) {
                        selectedSlotId = slot.slot
                    }
                }
            }

            if (selectedSlot != null) {
                Spacer(Modifier.height(10.dp))
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .background(PixelColors.Deep)
                        .border(2.dp, if (selectedSlot.equipped) PixelColors.Gold else PixelColors.Muted)
                        .padding(8.dp)
                        .testTag("inventory-slot-detail"),
                    verticalAlignment = Alignment.CenterVertically,
                ) {
                    if (selectedSlot.equipped && selectedSlot.itemId != null) {
                        PixelItemIcon(
                            itemId = selectedSlot.itemId,
                            quality = selectedSlot.quality,
                            modifier = Modifier.size(44.dp),
                        )
                    } else {
                        PixelUiIcon(
                            sprite = PixelEquipmentSlotCatalog.slot(selectedSlot.slot),
                            modifier = Modifier.size(40.dp),
                            tint = PixelColors.Muted,
                        )
                    }
                    Spacer(Modifier.width(8.dp))
                    Column(Modifier.weight(1f)) {
                        Text(
                            slotDisplayName(selectedSlot.slot),
                            color = PixelColors.Gold,
                            style = MaterialTheme.typography.labelLarge,
                        )
                        Text(
                            if (selectedSlot.equipped) selectedSlot.name ?: selectedSlot.itemId ?: "Equipped"
                            else "Empty slot",
                            color = if (selectedSlot.equipped) PixelColors.Paper else PixelColors.Muted,
                            style = MaterialTheme.typography.bodyMedium,
                        )
                        if (!selectedSlot.quality.isNullOrBlank()) {
                            Text(
                                selectedSlot.quality.uppercase(),
                                color = PixelColors.Muted,
                                style = MaterialTheme.typography.labelLarge,
                            )
                        }
                    }
                }
                if (selectedSlot.equipped) {
                    Spacer(Modifier.height(6.dp))
                    PixelTextButton(if (busy) "WORKING..." else "UNEQUIP") {
                        if (!busy) onUnequip(selectedSlot.slot)
                    }
                }
            }
        }

        PixelPanel(title = "Bag", chrome = PixelPanelChrome.INVENTORY) {
            Row(
                modifier = Modifier.fillMaxWidth(),
                verticalAlignment = Alignment.CenterVertically,
            ) {
                Text(
                    "CARRIED STACKS",
                    color = PixelColors.Gold,
                    style = MaterialTheme.typography.labelLarge,
                    modifier = Modifier.weight(1f),
                )
                Text(
                    items.size.toString(),
                    color = PixelColors.Paper,
                    style = MaterialTheme.typography.labelLarge,
                )
            }
            Spacer(Modifier.height(8.dp))

            if (items.isEmpty()) {
                Text("No carried items.", color = PixelColors.Muted, style = MaterialTheme.typography.bodyMedium)
            } else {
                if (selectedItem != null) {
                    Row(
                        modifier = Modifier
                            .fillMaxWidth()
                            .background(PixelColors.Deep)
                            .border(2.dp, PixelColors.Gold)
                            .padding(8.dp)
                            .testTag("inventory-item-detail"),
                        verticalAlignment = Alignment.CenterVertically,
                    ) {
                        PixelItemIcon(
                            itemId = selectedItem.id,
                            quality = selectedItem.quality,
                            modifier = Modifier.size(54.dp),
                        )
                        Spacer(Modifier.width(8.dp))
                        Column(Modifier.weight(1f)) {
                            Text(
                                selectedItem.name,
                                color = PixelColors.Paper,
                                style = MaterialTheme.typography.bodyMedium,
                            )
                            Text(
                                "x${selectedItem.quantity}" +
                                    if (!selectedItem.quality.isNullOrBlank()) " // ${selectedItem.quality.uppercase()}" else "",
                                color = PixelColors.Muted,
                                style = MaterialTheme.typography.labelLarge,
                            )
                            if (selectedItem.equippable && !selectedItem.slot.isNullOrBlank()) {
                                Text(
                                    "SLOT ${slotDisplayName(selectedItem.slot ?: "")}",
                                    color = PixelColors.Gold,
                                    style = MaterialTheme.typography.labelLarge,
                                )
                            }
                        }
                    }
                    if (selectedItem.equippable) {
                        Spacer(Modifier.height(6.dp))
                        PixelTextButton(
                            label = if (busy) {
                                "WORKING..."
                            } else {
                                "EQUIP // ${slotDisplayName(selectedItem.slot ?: "")}"
                            },
                            onClick = {
                                if (!busy) onEquip(selectedItem.id)
                            },
                        )
                    }
                    Spacer(Modifier.height(10.dp))
                }

                Text(
                    "ITEMS",
                    color = PixelColors.Muted,
                    style = MaterialTheme.typography.labelLarge,
                )
                Spacer(Modifier.height(6.dp))
                items.chunked(2).forEach { pair ->
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.spacedBy(6.dp),
                    ) {
                        pair.forEach { item ->
                            InventoryItemTile(
                                item = item,
                                active = selectedItemId == item.id,
                                modifier = Modifier.weight(1f),
                            ) {
                                selectedItemId = item.id
                            }
                        }
                        if (pair.size == 1) Spacer(Modifier.weight(1f))
                    }
                    Spacer(Modifier.height(6.dp))
                }
            }
        }
    }
}

@Composable
private fun InventorySlotTile(
    slot: GameEquipmentSlot,
    active: Boolean,
    modifier: Modifier = Modifier,
    onSelect: () -> Unit,
) {
    Column(
        modifier = modifier
            .height(72.dp)
            .background(PixelColors.Deep)
            .border(
                2.dp,
                when {
                    active -> PixelColors.Gold
                    slot.equipped -> PixelColors.Paper
                    else -> PixelColors.Muted
                },
            )
            .clickable(role = Role.Button, onClick = onSelect)
            .padding(4.dp)
            .testTag("inventory-slot-${slot.slot}"),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center,
    ) {
        if (slot.equipped && slot.itemId != null && PixelAssetCatalog.itemIcon(slot.itemId) != null) {
            PixelItemIcon(
                itemId = slot.itemId,
                quality = slot.quality,
                modifier = Modifier.size(34.dp),
            )
        } else {
            PixelUiIcon(
                sprite = PixelEquipmentSlotCatalog.slot(slot.slot),
                modifier = Modifier.size(30.dp),
                tint = PixelColors.Muted,
            )
        }
        Text(
            slotDisplayName(slot.slot),
            color = if (active) PixelColors.Gold else PixelColors.Paper,
            style = MaterialTheme.typography.labelLarge,
        )
    }
}

@Composable
private fun InventoryItemTile(
    item: GameInventoryItem,
    active: Boolean,
    modifier: Modifier = Modifier,
    onSelect: () -> Unit,
) {
    Row(
        modifier = modifier
            .height(76.dp)
            .background(PixelColors.Deep)
            .border(2.dp, if (active) PixelColors.Gold else PixelColors.Muted)
            .clickable(role = Role.Button, onClick = onSelect)
            .padding(6.dp)
            .testTag("inventory-item-${item.id}"),
        verticalAlignment = Alignment.CenterVertically,
    ) {
        PixelItemIcon(
            itemId = item.id,
            quality = item.quality,
            modifier = Modifier.size(42.dp),
        )
        Spacer(Modifier.width(6.dp))
        Column(Modifier.weight(1f)) {
            Text(
                item.name,
                color = PixelColors.Paper,
                style = MaterialTheme.typography.labelLarge,
            )
            Text(
                "x${item.quantity}",
                color = if (active) PixelColors.Gold else PixelColors.Muted,
                style = MaterialTheme.typography.labelLarge,
            )
        }
    }
}

@Composable
private fun QuestSection(snapshot: GameSnapshot) {
    Column(
        modifier = Modifier.fillMaxSize().verticalScroll(rememberScrollState()),
        verticalArrangement = Arrangement.spacedBy(8.dp),
    ) {
        if (snapshot.quests.isEmpty()) {
            PixelPanel(title = "Quests", chrome = PixelPanelChrome.QUEST) {
                Text(
                    "No quest is active yet. Explore the current scene and the quest log will update from authoritative state.",
                    color = PixelColors.Muted,
                    style = MaterialTheme.typography.bodyLarge,
                )
            }
        } else {
            listOf("main", "side", "optional", "lore").forEach { category ->
                val quests = snapshot.quests.filter { it.category == category }
                if (quests.isNotEmpty()) {
                    PixelPanel(title = category, chrome = PixelPanelChrome.QUEST) {
                        quests.forEach { quest ->
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                PixelUiIcon(
                                    sprite = PixelUiIconCatalog.quest(category),
                                    modifier = Modifier.size(16.dp),
                                    tint = when (category) {
                                        "main" -> PixelColors.Gold
                                        "side" -> PixelColors.Cyan
                                        "optional" -> PixelColors.Paper
                                        else -> PixelColors.Muted
                                    },
                                    testTag = "quest-icon-$category",
                                )
                                Spacer(Modifier.width(6.dp))
                                Text(quest.title, color = PixelColors.Gold, style = MaterialTheme.typography.titleLarge)
                            }
                            if (quest.description.isNotBlank()) {
                                Spacer(Modifier.height(4.dp))
                                Text(quest.description, color = PixelColors.Paper, style = MaterialTheme.typography.bodyMedium)
                            }
                            Spacer(Modifier.height(6.dp))
                            Text(
                                "STATUS ${quest.status.uppercase()} // ${quest.stage.replace('_', ' ')}",
                                color = PixelColors.Cyan,
                                style = MaterialTheme.typography.labelLarge,
                            )
                            quest.objectives.forEach { objective ->
                                val stateMark = when (objective.status) {
                                    "completed" -> "[x]"
                                    "failed" -> "[!]"
                                    "active" -> "[ ]"
                                    else -> "[-]"
                                }
                                val optional = if (objective.required) "" else " (optional)"
                                Text(
                                    "$stateMark ${objective.title}$optional",
                                    color = when (objective.status) {
                                        "completed" -> PixelColors.Cyan
                                        "failed" -> PixelColors.Danger
                                        "locked" -> PixelColors.Disabled
                                        else -> PixelColors.Paper
                                    },
                                    style = MaterialTheme.typography.bodyMedium,
                                )
                            }
                            Spacer(Modifier.height(12.dp))
                        }
                    }
                }
            }
        }
    }
}

@Composable
internal fun MapSection(
    snapshot: GameSnapshot,
    busy: Boolean,
    onTravel: (String) -> Unit,
) {
    val map = snapshot.worldMap
    var selectedId by remember(map.currentLocation, map.nodes) { mutableStateOf(map.currentLocation) }
    val selected = map.nodes.firstOrNull { it.id == selectedId }
        ?: map.nodes.firstOrNull { it.current }
        ?: map.nodes.firstOrNull()

    Column(
        modifier = Modifier.fillMaxSize().verticalScroll(rememberScrollState()),
        verticalArrangement = Arrangement.spacedBy(8.dp),
    ) {
        PixelPanel(title = map.title, chrome = PixelPanelChrome.MAP) {
            if (map.nodes.isEmpty()) {
                Text("No mapped location has been discovered yet.",
                    color = PixelColors.Muted, style = MaterialTheme.typography.bodyLarge)
            } else {
                // Coordinate percentages and graph edges come from the authoritative
                // map projection. No illustrated backgrounds, sprites or icons.
                Canvas(
                    modifier = Modifier.fillMaxWidth().height(220.dp)
                        .testTag("world-map-canvas")
                        .background(PixelColors.Deep)
                        .border(1.dp, PixelColors.Muted)
                        .pointerInput(map.nodes) {
                            detectTapGestures { tap ->
                                fun point(x: Double, y: Double): Offset = Offset(
                                    (x.coerceIn(0.0, 100.0) / 100.0 * size.width).toFloat(),
                                    (y.coerceIn(0.0, 100.0) / 100.0 * size.height).toFloat(),
                                )
                                val nearest = map.nodes.minByOrNull { node ->
                                    val p = point(node.x, node.y)
                                    val dx = tap.x - p.x
                                    val dy = tap.y - p.y
                                    dx * dx + dy * dy
                                }
                                if (nearest != null) {
                                    val p = point(nearest.x, nearest.y)
                                    val dx = tap.x - p.x
                                    val dy = tap.y - p.y
                                    val threshold = 30.dp.toPx()
                                    if (dx * dx + dy * dy <= threshold * threshold) {
                                        selectedId = nearest.id
                                    }
                                }
                            }
                        },
                ) {
                    fun point(id: String): Offset? {
                        val node = map.nodes.firstOrNull { it.id == id } ?: return null
                        return Offset(
                            (node.x.coerceIn(0.0, 100.0) / 100.0 * size.width).toFloat(),
                            (node.y.coerceIn(0.0, 100.0) / 100.0 * size.height).toFloat(),
                        )
                    }
                    map.edges.forEach { edge ->
                        val from = point(edge.from)
                        val to = point(edge.to)
                        if (from != null && to != null) {
                            drawLine(PixelColors.Muted, from, to, strokeWidth = 2f)
                        }
                    }
                    map.nodes.forEach { node ->
                        val center = point(node.id) ?: return@forEach
                        val color = when {
                            node.current -> PixelColors.Gold
                            node.reachable -> PixelColors.Cyan
                            else -> PixelColors.Muted
                        }
                        drawCircle(color = color, radius = if (node.current) 8.dp.toPx() else 6.dp.toPx(),
                            center = center)
                    }
                }

                Spacer(Modifier.height(10.dp))
                Text("DISCOVERED LOCATIONS", color = PixelColors.Gold,
                    style = MaterialTheme.typography.labelLarge)
                map.nodes.forEach { node ->
                    PixelTextButton(
                        label = if (node.current) "> ${node.title} [YOU]" else node.title,
                        onClick = { selectedId = node.id },
                        modifier = Modifier.testTag("map-node-${node.id}"),
                    )
                    Spacer(Modifier.height(6.dp))
                }
                if (selected != null) {
                    Text(selected.title, color = PixelColors.Cyan,
                        style = MaterialTheme.typography.titleLarge)
                    if (selected.description.isNotBlank()) {
                        Text(selected.description, color = PixelColors.Paper,
                            style = MaterialTheme.typography.bodyMedium)
                    }
                    if (!selected.current) {
                        if (selected.reachable) {
                            PixelTextButton(
                                label = if (busy) "TRAVELING..." else "TRAVEL HERE",
                                onClick = { if (!busy) onTravel(selected.id) },
                                modifier = Modifier.testTag("map-travel"),
                            )
                        } else {
                            Text("NO DIRECT ROUTE FROM CURRENT LOCATION",
                                color = PixelColors.Disabled,
                                style = MaterialTheme.typography.labelLarge)
                        }
                    }
                }
            }
        }
    }
}

@Composable
private fun MorePanel(onCharacter: () -> Unit, onSettings: () -> Unit) {
    PixelPanel(modifier = Modifier.fillMaxSize(), title = "More", chrome = PixelPanelChrome.SETTINGS) {
        PixelTextButton("CHARACTER / EQUIPMENT", onCharacter)
        Spacer(Modifier.height(8.dp))
        PixelTextButton("SETTINGS / SAVE / AUDIO", onSettings)
        Spacer(Modifier.height(12.dp))
        Text(
            "Developer tools, accessibility, narration, and save management remain separated from the main story surface.",
            color = PixelColors.Muted,
            style = MaterialTheme.typography.bodyMedium,
        )
    }
}

@Composable
private fun ComingPanel(title: String, body: String) {
    PixelPanel(Modifier.fillMaxSize().verticalScroll(rememberScrollState()), title) {
        Text(body, color = PixelColors.Paper, style = MaterialTheme.typography.bodyLarge)
    }
}

@Composable
private fun BottomPixelNav(selected: GameSection, onSelect: (GameSection) -> Unit) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .horizontalScroll(rememberScrollState()),
        horizontalArrangement = Arrangement.spacedBy(4.dp),
    ) {
        GameSection.entries.forEach { section ->
            PixelNavButton(
                label = section.label,
                active = selected == section,
                onClick = { onSelect(section) },
            )
        }
    }
}

@Composable
private fun PixelNavButton(label: String, active: Boolean, onClick: () -> Unit) {
    Box(
        modifier = Modifier.testTag("nav-${label.lowercase()}")
            .background(if (active) PixelColors.PanelAlt else PixelColors.Deep)
            .border(1.dp, if (active) PixelColors.Gold else PixelColors.Muted)
            .clickable(role = Role.Tab, onClick = onClick)
            .padding(horizontal = 10.dp, vertical = 10.dp),
    ) {
        Text(label, color = if (active) PixelColors.Gold else PixelColors.Paper,
            style = MaterialTheme.typography.labelLarge)
    }
}

@Composable
private fun PixelTextButton(
    label: String,
    onClick: () -> Unit,
) = PixelTextButton(
    label = label,
    modifier = Modifier,
    onClick = onClick,
)

@Composable
private fun PixelTextButton(
    label: String,
    modifier: Modifier,
    onClick: () -> Unit,
) {
    Box(
        modifier = modifier
            .background(PixelColors.PanelAlt)
            .border(1.dp, PixelColors.Muted)
            .clickable(role = Role.Button, onClick = onClick)
            .padding(horizontal = 12.dp, vertical = 8.dp),
    ) {
        Text(label, color = PixelColors.Paper, style = MaterialTheme.typography.labelLarge)
    }
}

@Composable
private fun EquipmentSlotValue(
    slotId: String,
    value: String,
) {
    Row(
        modifier = Modifier.fillMaxWidth(),
        verticalAlignment = Alignment.CenterVertically,
    ) {
        PixelUiIcon(
            sprite = PixelEquipmentSlotCatalog.slot(slotId),
            modifier = Modifier.size(24.dp),
            tint = PixelColors.Paper,
            testTag = "equipment-slot-icon-$slotId",
        )
        Spacer(Modifier.width(8.dp))
        Column(Modifier.weight(1f)) {
            Text(
                slotDisplayName(slotId),
                color = PixelColors.Muted,
                style = MaterialTheme.typography.labelLarge,
            )
            Text(
                value,
                color = PixelColors.Paper,
                style = MaterialTheme.typography.bodyMedium,
            )
        }
    }
    Spacer(Modifier.height(6.dp))
}

@Composable
private fun LabeledValue(label: String, value: String) {
    Row(Modifier.fillMaxWidth()) {
        Text(
            label.uppercase(),
            color = PixelColors.Muted,
            style = MaterialTheme.typography.bodyMedium,
            modifier = Modifier.width(130.dp),
        )
        Text(value, color = PixelColors.Paper, style = MaterialTheme.typography.bodyMedium)
    }
    Spacer(Modifier.height(4.dp))
}

private fun slotDisplayName(slot: String): String = when (slot) {
    "body" -> "CHEST"
    "ring_1" -> "RING I"
    "ring_2" -> "RING II"
    "accessory_1" -> "ACCESSORY I"
    "accessory_2" -> "ACCESSORY II"
    else -> slot.replace('_', ' ').uppercase()
}

private fun formatGameTime(minutes: Int): String {
    val days = minutes / (24 * 60)
    val withinDay = minutes % (24 * 60)
    val hours = withinDay / 60
    val mins = withinDay % 60
    return if (days > 0) "D${days + 1} %02d:%02d".format(hours, mins) else "%02d:%02d".format(hours, mins)
}

private fun signed(value: Double): String =
    if (value >= 0) "+${value.roundToInt()}" else value.roundToInt().toString()
