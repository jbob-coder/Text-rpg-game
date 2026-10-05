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
    BoxWithConstraints(Modifier.fillMaxSize()) {
        if (maxWidth >= 720.dp) {
            Row(
                modifier = Modifier.fillMaxSize(),
                horizontalArrangement = Arrangement.spacedBy(8.dp),
            ) {
                Column(Modifier.weight(0.36f).fillMaxHeight()) {
                    PlayerAvatarPanel(
                        identity = snapshot.identity,
                        equipment = snapshot.inventory.equipment,
                        conditions = snapshot.conditions,
                    )
                    Spacer(Modifier.height(8.dp))
                    ResourcePanel(snapshot)
                }
                NarrativePanel(
                    snapshot = snapshot,
                    busy = busy,
                    onChoice = onChoice,
                    onNarrate = onNarrate,
                    textDelayMs = textDelayMs,
                    modifier = Modifier.weight(0.64f).fillMaxHeight(),
                )
            }
        } else {
            Column(
                modifier = Modifier.fillMaxSize(),
                verticalArrangement = Arrangement.spacedBy(8.dp),
            ) {
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(210.dp)
                        .testTag("story-pixel-header"),
                    horizontalArrangement = Arrangement.spacedBy(8.dp),
                ) {
                    SceneIllustration(
                        locationId = snapshot.location,
                        sceneId = snapshot.sceneId,
                        relayState = snapshot.visuals.relayState,
                        roomActors = snapshot.room.actors,
                        modifier = Modifier
                            .weight(0.68f)
                            .fillMaxHeight(),
                    )
                    PlayerAvatarPanel(
                        identity = snapshot.identity,
                        equipment = snapshot.inventory.equipment,
                        conditions = snapshot.conditions,
                        modifier = Modifier
                            .weight(0.32f)
                            .fillMaxHeight(),
                        compact = true,
                        showSummary = false,
                    )
                }
                StoryResourceHud(
                    snapshot = snapshot,
                    modifier = Modifier.fillMaxWidth(),
                )
                NarrativePanel(
                    snapshot = snapshot,
                    busy = busy,
                    onChoice = onChoice,
                    onNarrate = onNarrate,
                    textDelayMs = textDelayMs,
                    modifier = Modifier
                        .fillMaxWidth()
                        .weight(1f),
                    showSceneIllustration = false,
                )
            }
        }
    }
}

@Composable
private fun NarrativePanel(
    snapshot: GameSnapshot,
    busy: Boolean,
    onChoice: (String) -> Unit,
    onNarrate: (String) -> Boolean,
    textDelayMs: Int,
    modifier: Modifier,
    showSceneIllustration: Boolean = true,
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
                if (showSceneIllustration) {
                    Spacer(Modifier.height(8.dp))
                    SceneIllustration(
                        locationId = snapshot.location,
                        sceneId = snapshot.sceneId,
                        relayState = snapshot.visuals.relayState,
                        roomActors = snapshot.room.actors,
                        modifier = Modifier
                            .fillMaxWidth()
                            .height(150.dp),
                    )
                    Spacer(Modifier.height(12.dp))
                } else {
                    Spacer(Modifier.height(8.dp))
                }
                Text(
                    text = visibleBody,
                    color = PixelColors.Paper,
                    style = MaterialTheme.typography.bodyLarge,
                    modifier = Modifier.clickable(role = Role.Button) { onNarrate(snapshot.body) },
                )
                Spacer(Modifier.height(10.dp))
                PixelIconTextButton(
                    label = "READ ALOUD",
                    icon = PixelUiUtilityCatalog.narrationIcon,
                ) {
                    onNarrate(snapshot.body)
                }
                Spacer(Modifier.height(18.dp))
                Text("DECIDE", color = PixelColors.Gold, style = MaterialTheme.typography.titleLarge)
                Spacer(Modifier.height(8.dp))
                snapshot.choices.forEach { choice ->
                    PixelChoiceCard(choice, busy) { onChoice(choice.id) }
                    Spacer(Modifier.height(8.dp))
                }
            }

            if (narrativeScroll.value < narrativeScroll.maxValue) {
                PixelUiIcon(
                    sprite = PixelUiUtilityCatalog.scrollMarker,
                    modifier = Modifier
                        .align(Alignment.BottomCenter)
                        .size(18.dp)
                        .background(PixelColors.PanelAlt),
                    testTag = "narrative-scroll-marker",
                )
            }
        }
    }
}

@Composable
private fun StoryResourceHud(
    snapshot: GameSnapshot,
    modifier: Modifier = Modifier,
) {
    if (snapshot.resources.isEmpty()) return

    Column(
        modifier = modifier
            .pixelChrome(PixelUiChromeCatalog.statsFrame)
            .padding(horizontal = 8.dp, vertical = 6.dp)
            .testTag("story-resource-hud"),
        verticalArrangement = Arrangement.spacedBy(5.dp),
    ) {
        snapshot.resources.forEach { resource ->
            val ratio = if (resource.max > 0.0) {
                (resource.current / resource.max).coerceIn(0.0, 1.0)
            } else {
                0.0
            }
            val resourceColor = when (resource.id.lowercase()) {
                "health" -> PixelColors.Health
                "stamina" -> PixelColors.Stamina
                "focus" -> PixelColors.Focus
                "resolve" -> PixelColors.Resolve
                else -> PixelColors.Paper
            }

            Row(
                modifier = Modifier.fillMaxWidth(),
                verticalAlignment = Alignment.CenterVertically,
            ) {
                PixelUiIcon(
                    sprite = PixelUiIconCatalog.resource(resource.id),
                    modifier = Modifier.size(14.dp),
                    tint = resourceColor,
                )
                Spacer(Modifier.width(6.dp))
                Text(
                    resource.id.uppercase(),
                    color = PixelColors.Muted,
                    style = MaterialTheme.typography.labelSmall,
                    modifier = Modifier.width(64.dp),
                )
                PixelResourceBar(
                    ratio = ratio.toFloat(),
                    fillColor = resourceColor,
                    modifier = Modifier.weight(1f),
                )
                Spacer(Modifier.width(6.dp))
                Text(
                    "${resource.current.roundToInt()}/${resource.max.roundToInt()}",
                    color = PixelColors.Paper,
                    style = MaterialTheme.typography.labelSmall,
                )
            }
        }
    }
}

@Composable
private fun ResourcePanel(snapshot: GameSnapshot) {
    PixelPanel {
        Text("RESOURCES", color = PixelColors.Gold, style = MaterialTheme.typography.titleMedium)
        Spacer(Modifier.height(6.dp))
        snapshot.resources.forEach { resource ->
            val ratio = if (resource.max > 0.0) {
                (resource.current / resource.max).coerceIn(0.0, 1.0)
            } else {
                0.0
            }
            val resourceColor = when (resource.id.lowercase()) {
                "health" -> PixelColors.Health
                "stamina" -> PixelColors.Stamina
                "focus" -> PixelColors.Focus
                "resolve" -> PixelColors.Resolve
                else -> PixelColors.Paper
            }
            Text(
                "${resource.id.uppercase()} ${resource.current.roundToInt()}/${resource.max.roundToInt()}",
                color = PixelColors.Paper,
                style = MaterialTheme.typography.bodyMedium,
            )
            Spacer(Modifier.height(4.dp))
            PixelResourceBar(
                ratio = ratio.toFloat(),
                fillColor = resourceColor,
                modifier = Modifier.fillMaxWidth(),
            )
            Spacer(Modifier.height(7.dp))
        }
        if (snapshot.resources.isEmpty()) {
            Text("NO ACTIVE RESOURCES", color = PixelColors.Muted)
        }
    }
}

@Composable
private fun StatsSection(
    snapshot: GameSnapshot,
    selectedPath: String?,
    inspection: GameStatInspection?,
    inspectionBusy: Boolean,
    inspectionError: String?,
    onInspect: (String) -> Unit,
) {
    var selectedTab by remember { mutableStateOf(StatTab.SUMMARY) }
    var inspectionPath by remember(selectedPath) { mutableStateOf(selectedPath.orEmpty()) }
    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState()),
        verticalArrangement = Arrangement.spacedBy(8.dp),
    ) {
        PixelPanel {
            Text("STATUS // READ-ONLY", color = PixelColors.Gold, style = MaterialTheme.typography.titleLarge)
            Spacer(Modifier.height(6.dp))
            Row(horizontalArrangement = Arrangement.spacedBy(6.dp)) {
                StatTab.entries.forEach { tab ->
                    PixelTextButton(
                        label = tab.label,
                        onClick = { selectedTab = tab },
                        modifier = Modifier.testTag("stats-tab-${tab.name.lowercase()}"),
                        enabled = tab != selectedTab,
                    )
                }
            }
        }

        when (selectedTab) {
            StatTab.SUMMARY -> StatsSummaryTab(snapshot)
            StatTab.CONDITIONS -> StatsConditionsTab(snapshot)
            StatTab.INSPECT -> StatsInspectTab(
                path = inspectionPath,
                onPathChange = { inspectionPath = it },
                inspection = inspection,
                busy = inspectionBusy,
                error = inspectionError,
                onInspect = { onInspect(inspectionPath) },
            )
        }
    }
}

private enum class StatTab(val label: String) {
    SUMMARY("SUMMARY"),
    CONDITIONS("CONDITIONS"),
    INSPECT("INSPECT"),
}

@Composable
private fun StatsSummaryTab(snapshot: GameSnapshot) {
    PixelPanel {
        Text("SUMMARY", color = PixelColors.Cyan, style = MaterialTheme.typography.titleMedium)
        Spacer(Modifier.height(6.dp))
        snapshot.resources.forEach { resource ->
            Text(
                "${resource.id.uppercase()} ${resource.current.roundToInt()}/${resource.max.roundToInt()}",
                color = PixelColors.Paper,
                style = MaterialTheme.typography.bodyMedium,
            )
        }
        if (snapshot.resources.isEmpty()) {
            Text("NO ACTIVE RESOURCES", color = PixelColors.Muted)
        }
    }
}

@Composable
private fun StatsConditionsTab(snapshot: GameSnapshot) {
    PixelPanel {
        Text("CONDITIONS", color = PixelColors.Cyan, style = MaterialTheme.typography.titleMedium)
        Spacer(Modifier.height(6.dp))
        snapshot.conditions.forEach { condition ->
            Text("• $condition", color = PixelColors.Paper, style = MaterialTheme.typography.bodyMedium)
        }
        if (snapshot.conditions.isEmpty()) {
            Text("NONE", color = PixelColors.Muted)
        }
    }
}

@Composable
private fun StatsInspectTab(
    path: String,
    onPathChange: (String) -> Unit,
    inspection: GameStatInspection?,
    busy: Boolean,
    error: String?,
    onInspect: () -> Unit,
) {
    PixelPanel {
        Text("INSPECT", color = PixelColors.Cyan, style = MaterialTheme.typography.titleMedium)
        Spacer(Modifier.height(6.dp))
        OutlinedTextField(
            value = path,
            onValueChange = onPathChange,
            label = { Text("Stat path") },
            singleLine = true,
            modifier = Modifier
                .fillMaxWidth()
                .testTag("stats-inspect-path"),
        )
        Spacer(Modifier.height(6.dp))
        PixelTextButton(
            label = if (busy) "INSPECTING..." else "INSPECT",
            onClick = onInspect,
            enabled = !busy,
            modifier = Modifier.testTag("stats-inspect-button"),
        )
        if (!error.isNullOrBlank()) {
            Spacer(Modifier.height(6.dp))
            Text(error, color = PixelColors.Danger, style = MaterialTheme.typography.bodySmall)
        }
        inspection?.let { result ->
            Spacer(Modifier.height(8.dp))
            Text(result.label, color = PixelColors.Gold, style = MaterialTheme.typography.titleSmall)
            Text(
                "${result.value.roundToInt()}  //  ${result.source.uppercase()}",
                color = PixelColors.Paper,
                style = MaterialTheme.typography.bodyLarge,
            )
            result.description?.takeIf { it.isNotBlank() }?.let { description ->
                Spacer(Modifier.height(4.dp))
                Text(description, color = PixelColors.Muted, style = MaterialTheme.typography.bodySmall)
            }
        }
    }
}

@Composable
private fun InventorySection(
    snapshot: GameSnapshot,
    busy: Boolean,
    onEquip: (String) -> Unit,
    onUnequip: (String) -> Unit,
) {
    var selectedItemId by remember(snapshot.sceneId) { mutableStateOf<String?>(null) }
    val selectedItem = snapshot.inventory.items.firstOrNull { it.id == selectedItemId }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState()),
        verticalArrangement = Arrangement.spacedBy(8.dp),
    ) {
        PixelPanel {
            Text("INVENTORY", color = PixelColors.Gold, style = MaterialTheme.typography.titleLarge)
            Spacer(Modifier.height(6.dp))
            if (snapshot.inventory.items.isEmpty()) {
                Text("PACK EMPTY", color = PixelColors.Muted)
            } else {
                snapshot.inventory.items.forEach { item ->
                    InventoryRow(
                        item = item,
                        equipped = item.id in snapshot.inventory.equipment.equippedItemIds,
                        selected = item.id == selectedItemId,
                        onClick = { selectedItemId = item.id },
                    )
                    Spacer(Modifier.height(4.dp))
                }
            }
        }
        selectedItem?.let { item ->
            InventoryDetailPanel(
                item = item,
                equipment = snapshot.inventory.equipment,
                busy = busy,
                onEquip = onEquip,
                onUnequip = onUnequip,
            )
        }
    }
}

@Composable
private fun InventoryRow(
    item: GameInventoryItem,
    equipped: Boolean,
    selected: Boolean,
    onClick: () -> Unit,
) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .background(if (selected) PixelColors.PanelAlt else PixelColors.Panel)
            .border(1.dp, if (selected) PixelColors.Cyan else PixelColors.Muted)
            .clickable(role = Role.Button, onClick = onClick)
            .padding(8.dp)
            .testTag("inventory-item-${item.id}"),
        verticalAlignment = Alignment.CenterVertically,
    ) {
        PixelUiIcon(
            sprite = PixelUiIconCatalog.inventory(item.id),
            modifier = Modifier.size(18.dp),
            tint = if (equipped) PixelColors.Gold else PixelColors.Paper,
        )
        Spacer(Modifier.width(8.dp))
        Column(Modifier.weight(1f)) {
            Text(item.name, color = PixelColors.Paper, style = MaterialTheme.typography.bodyLarge)
            Text(item.type.uppercase(), color = PixelColors.Muted, style = MaterialTheme.typography.labelSmall)
        }
        Text(
            if (equipped) "EQUIPPED" else "x${item.quantity}",
            color = if (equipped) PixelColors.Gold else PixelColors.Cyan,
            style = MaterialTheme.typography.labelLarge,
        )
    }
}

@Composable
private fun InventoryDetailPanel(
    item: GameInventoryItem,
    equipment: GameEquipmentSlot,
    busy: Boolean,
    onEquip: (String) -> Unit,
    onUnequip: (String) -> Unit,
) {
    PixelPanel {
        Text(item.name, color = PixelColors.Cyan, style = MaterialTheme.typography.titleMedium)
        Spacer(Modifier.height(4.dp))
        Text(item.description, color = PixelColors.Paper, style = MaterialTheme.typography.bodyMedium)
        Spacer(Modifier.height(8.dp))
        if (item.equippable) {
            val equipped = item.id in equipment.equippedItemIds
            PixelTextButton(
                label = if (equipped) "UNEQUIP" else "EQUIP",
                onClick = { if (equipped) onUnequip(item.id) else onEquip(item.id) },
                enabled = !busy,
                modifier = Modifier.testTag("inventory-equip-${item.id}"),
            )
        }
    }
}

@Composable
private fun CharacterSection(
    snapshot: GameSnapshot,
    busy: Boolean,
    onEquip: (String) -> Unit,
    onUnequip: (String) -> Unit,
) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState()),
        verticalArrangement = Arrangement.spacedBy(8.dp),
    ) {
        PlayerAvatarPanel(
            identity = snapshot.identity,
            equipment = snapshot.inventory.equipment,
            conditions = snapshot.conditions,
            modifier = Modifier
                .fillMaxWidth()
                .height(240.dp),
            compact = false,
        )
        EquipmentPanel(
            inventory = snapshot.inventory.items,
            equipment = snapshot.inventory.equipment,
            busy = busy,
            onEquip = onEquip,
            onUnequip = onUnequip,
        )
    }
}

@Composable
private fun QuestSection(snapshot: GameSnapshot) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState()),
        verticalArrangement = Arrangement.spacedBy(8.dp),
    ) {
        PixelPanel {
            Text("QUESTS", color = PixelColors.Gold, style = MaterialTheme.typography.titleLarge)
            Spacer(Modifier.height(6.dp))
            if (snapshot.quests.isEmpty()) {
                Text("NO ACTIVE QUESTS", color = PixelColors.Muted)
            } else {
                snapshot.quests.forEach { quest ->
                    Text(quest.title, color = PixelColors.Cyan, style = MaterialTheme.typography.titleMedium)
                    Text(quest.summary, color = PixelColors.Paper, style = MaterialTheme.typography.bodyMedium)
                    Spacer(Modifier.height(8.dp))
                }
            }
        }
    }
}

@Composable
private fun MapSection(snapshot: GameSnapshot, busy: Boolean, onTravel: (String) -> Unit) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState()),
        verticalArrangement = Arrangement.spacedBy(8.dp),
    ) {
        PixelPanel {
            Text("MAP", color = PixelColors.Gold, style = MaterialTheme.typography.titleLarge)
            Spacer(Modifier.height(6.dp))
            Text(
                "CURRENT // ${snapshot.location.replace('_', ' ')}",
                color = PixelColors.Cyan,
                style = MaterialTheme.typography.bodyLarge,
            )
            Spacer(Modifier.height(8.dp))
            snapshot.map.destinations.forEach { destination ->
                PixelTextButton(
                    label = destination.label,
                    onClick = { onTravel(destination.locationId) },
                    enabled = !busy && destination.available,
                    modifier = Modifier.testTag("map-destination-${destination.locationId}"),
                )
                Spacer(Modifier.height(4.dp))
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
    var cheatInput by remember { mutableStateOf("") }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState()),
        verticalArrangement = Arrangement.spacedBy(8.dp),
    ) {
        PixelPanel {
            Text("SETTINGS", color = PixelColors.Gold, style = MaterialTheme.typography.titleLarge)
            Spacer(Modifier.height(8.dp))
            Row(horizontalArrangement = Arrangement.spacedBy(6.dp)) {
                PixelTextButton("SAVE", onSave, modifier = Modifier.testTag("settings-save"))
                PixelTextButton("LOAD", onLoad, modifier = Modifier.testTag("settings-load"))
                PixelTextButton("CLOSE", onClose)
            }
        }

        PixelPanel {
            Text("NARRATION", color = PixelColors.Cyan, style = MaterialTheme.typography.titleMedium)
            Spacer(Modifier.height(6.dp))
            PixelTextButton(
                label = if (autoReadNarration) "AUTO READ: ON" else "AUTO READ: OFF",
                onClick = { onAutoReadChange(!autoReadNarration) },
            )
            Spacer(Modifier.height(6.dp))
            PixelTextButton("REPLAY", { onReplayNarration() })
            Spacer(Modifier.height(4.dp))
            PixelTextButton("STOP", onStopNarration)
            Spacer(Modifier.height(6.dp))
            Text("RATE ${"%.1f".format(narrationRate)}x", color = PixelColors.Paper)
            Row(horizontalArrangement = Arrangement.spacedBy(4.dp)) {
                listOf(0.8f, 1.0f, 1.2f).forEach { rate ->
                    PixelTextButton("${rate}x", { onNarrationRateChange(rate) })
                }
            }
            Spacer(Modifier.height(6.dp))
            Text("TEXT DELAY ${textDelayMs}ms", color = PixelColors.Paper)
            Row(horizontalArrangement = Arrangement.spacedBy(4.dp)) {
                listOf(0, 10, 25).forEach { delay ->
                    PixelTextButton("${delay}ms", { onTextDelayChange(delay) })
                }
            }
        }

        PixelPanel {
            Text("DEVELOPER", color = PixelColors.Cyan, style = MaterialTheme.typography.titleMedium)
            Spacer(Modifier.height(6.dp))
            OutlinedTextField(
                value = cheatInput,
                onValueChange = { cheatInput = it },
                label = { Text("Cheat command") },
                singleLine = true,
                modifier = Modifier.fillMaxWidth(),
            )
            Spacer(Modifier.height(6.dp))
            PixelTextButton(
                "RUN",
                {
                    onCheat(cheatInput)
                    cheatInput = ""
                },
                enabled = cheatInput.isNotBlank(),
            )
            Spacer(Modifier.height(6.dp))
            Text(
                "SCENE ${snapshot.sceneId}",
                color = PixelColors.Muted,
                style = MaterialTheme.typography.labelSmall,
            )
        }
    }
}

@Composable
private fun MorePanel(onCharacter: () -> Unit, onSettings: () -> Unit) {
    PixelPanel {
        Text("MORE", color = PixelColors.Gold, style = MaterialTheme.typography.titleLarge)
        Spacer(Modifier.height(8.dp))
        PixelTextButton("CHARACTER", onCharacter)
        Spacer(Modifier.height(6.dp))
        PixelTextButton("SETTINGS", onSettings)
    }
}

@Composable
private fun BottomPixelNav(active: GameSection, onSelect: (GameSection) -> Unit) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .horizontalScroll(rememberScrollState()),
        horizontalArrangement = Arrangement.spacedBy(4.dp),
    ) {
        GameSection.entries.forEach { section ->
            PixelNavButton(section.label, section == active) { onSelect(section) }
        }
    }
}

@Composable
private fun PixelNavButton(label: String, active: Boolean, onClick: () -> Unit) {
    PixelTextButton(
        label = label.uppercase(),
        onClick = onClick,
        modifier = Modifier.testTag("nav-${label.lowercase()}"),
        enabled = !active,
    )
}

@Composable
private fun PixelChoiceCard(choice: com.thegame.rpg.engine.GameChoice, busy: Boolean, onClick: () -> Unit) {
    PixelTextButton(
        label = choice.text,
        onClick = onClick,
        enabled = !busy && choice.enabled,
        modifier = Modifier
            .fillMaxWidth()
            .testTag("choice-${choice.id}"),
    )
}

@Composable
private fun PixelResourceBar(ratio: Float, fillColor: androidx.compose.ui.graphics.Color, modifier: Modifier = Modifier) {
    Canvas(
        modifier = modifier
            .height(8.dp)
            .border(1.dp, PixelColors.Muted)
            .background(PixelColors.Deep),
    ) {
        val clamped = ratio.coerceIn(0f, 1f)
        drawRect(
            color = fillColor,
            topLeft = Offset.Zero,
            size = androidx.compose.ui.geometry.Size(size.width * clamped, size.height),
        )
    }
}

private fun formatGameTime(totalMinutes: Int): String {
    val normalized = ((totalMinutes % (24 * 60)) + (24 * 60)) % (24 * 60)
    val hours = normalized / 60
    val minutes = normalized % 60
    return "%02d:%02d".format(hours, minutes)
}
