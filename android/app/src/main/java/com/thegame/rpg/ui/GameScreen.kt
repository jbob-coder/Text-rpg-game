package com.thegame.rpg.ui

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
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
import androidx.compose.foundation.layout.width
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
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.unit.dp
import com.thegame.rpg.GameUiState
import com.thegame.rpg.boot.BootState
import com.thegame.rpg.engine.GameSnapshot
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
    onTravel: (String) -> Unit,
) {
    val snapshot = uiState.snapshot
    if (uiState.bootState == BootState.Ready && snapshot != null) {
        PixelGameShell(
            snapshot,
            uiState.busy,
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
            onTravel,
        )
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
    onTravel: (String) -> Unit,
) {
    var section by remember { mutableStateOf(GameSection.STORY) }
    var settingsOpen by remember { mutableStateOf(false) }

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
                    GameSection.CHARACTER -> CharacterSection(snapshot)
                    GameSection.STATS -> StatsSection(snapshot)
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
                    PlayerAvatarPanel(snapshot.identity)
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
                PlayerAvatarPanel(
                    identity = snapshot.identity,
                    modifier = Modifier
                        .fillMaxWidth()
                        .weight(0.42f),
                )
                NarrativePanel(
                    snapshot = snapshot,
                    busy = busy,
                    onChoice = onChoice,
                    onNarrate = onNarrate,
                    textDelayMs = textDelayMs,
                    modifier = Modifier
                        .fillMaxWidth()
                        .weight(0.58f),
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

    PixelPanel(modifier = modifier) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .testTag("narrative-scroll")
                .verticalScroll(rememberScrollState()),
        ) {
            Text(
                text = snapshot.title,
                color = PixelColors.Cyan,
                style = MaterialTheme.typography.titleLarge,
                modifier = Modifier.testTag("scene-title"),
            )
            Spacer(Modifier.height(8.dp))
            SceneIllustration(
                locationId = snapshot.location,
                modifier = Modifier
                    .fillMaxWidth()
                    .height(150.dp),
            )
            Spacer(Modifier.height(12.dp))
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
    }
}

@Composable
private fun ResourcePanel(snapshot: GameSnapshot) {
    PixelPanel(title = "Resources") {
        snapshot.resources.forEach { resource ->
            val percent = if (resource.max > 0.0) {
                ((resource.current / resource.max) * 100.0).coerceIn(0.0, 100.0).roundToInt()
            } else 0
            Text(
                "${resource.id.uppercase().padEnd(8)} ${resource.current.roundToInt()} / ${resource.max.roundToInt()} [$percent%]",
                color = when {
                    percent <= 25 -> PixelColors.Danger
                    percent <= 50 -> PixelColors.Gold
                    else -> PixelColors.Paper
                },
                style = MaterialTheme.typography.labelLarge,
            )
            Spacer(Modifier.height(4.dp))
        }
    }
}

@Composable
private fun CharacterSection(snapshot: GameSnapshot) {
    BoxWithConstraints(Modifier.fillMaxSize()) {
        val wideCharacterPanel = maxWidth > 700.dp
        Row(
            modifier = Modifier
                .fillMaxSize()
                .horizontalScroll(rememberScrollState()),
            horizontalArrangement = Arrangement.spacedBy(8.dp),
        ) {
            PlayerAvatarPanel(snapshot.identity, Modifier.width(if (wideCharacterPanel) 320.dp else 260.dp))
            PixelPanel(Modifier.width(if (wideCharacterPanel) 420.dp else 320.dp), "Character") {
                LabeledValue("Name", snapshot.identity.name ?: "Unassigned")
                LabeledValue("Level", snapshot.identity.level?.toString() ?: "—")
                LabeledValue("Path", snapshot.identity.path ?: "—")
                LabeledValue("Origin", snapshot.identity.origin ?: "—")
                LabeledValue("Background", snapshot.identity.background ?: "—")
                Spacer(Modifier.height(12.dp))
                Text("EQUIPMENT SLOTS", color = PixelColors.Gold, style = MaterialTheme.typography.titleLarge)
                Spacer(Modifier.height(6.dp))
                snapshot.inventory.equipment.forEach { slot ->
                    val itemName = if (slot.equipped) slot.name ?: slot.itemId ?: "EQUIPPED" else "—"
                    LabeledValue(slotDisplayName(slot.slot), itemName)
                }
            }
        }
    }
}

@Composable
private fun StatsSection(snapshot: GameSnapshot) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState()),
        verticalArrangement = Arrangement.spacedBy(8.dp),
    ) {
        PixelPanel(title = "Resources") {
            snapshot.resources.forEach { resource ->
                LabeledValue(resource.id, "${resource.current.roundToInt()} / ${resource.max.roundToInt()}")
            }
        }
        PixelPanel(title = "Core Attributes") {
            snapshot.attributes.forEach { stat ->
                val bonus = if (stat.delta == 0.0) "" else " (${signed(stat.delta)})"
                Text(
                    "${stat.name.padEnd(14)} ${stat.effective.roundToInt()}$bonus",
                    color = if (stat.modified) PixelColors.Cyan else PixelColors.Paper,
                    style = MaterialTheme.typography.bodyMedium,
                )
            }
        }
        PixelPanel(title = "Derived") {
            snapshot.derived.forEach { stat ->
                Text(
                    "${stat.name.padEnd(18)} ${stat.value.roundToInt()}",
                    color = PixelColors.Paper,
                    style = MaterialTheme.typography.bodyMedium,
                )
            }
        }
        PixelPanel(title = "Skills") {
            snapshot.skills.groupBy { it.category }.forEach { (category, skills) ->
                Text("[${category.uppercase()}]", color = PixelColors.Gold, style = MaterialTheme.typography.labelLarge)
                skills.forEach { skill ->
                    val bonus = if (skill.delta == 0.0) "" else " (${signed(skill.delta)})"
                    Text(
                        "${skill.name.padEnd(18)} ${skill.effective.roundToInt()}$bonus",
                        color = if (skill.modified) PixelColors.Cyan else PixelColors.Paper,
                        style = MaterialTheme.typography.bodyMedium,
                    )
                }
                Spacer(Modifier.height(6.dp))
            }
        }
        if (snapshot.conditions.isNotEmpty()) {
            PixelPanel(title = "Conditions") {
                snapshot.conditions.forEach { condition ->
                    Text(
                        "${condition.name} // SEV ${condition.severity}",
                        color = PixelColors.Danger,
                        style = MaterialTheme.typography.bodyMedium,
                    )
                }
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
        PixelPanel(title = "Settings") {
            Text("Game settings live outside the narrative HUD.", color = PixelColors.Paper, style = MaterialTheme.typography.bodyLarge)
            Spacer(Modifier.height(12.dp))
            PixelTextButton("SAVE GAME", onSave)
            Spacer(Modifier.height(8.dp))
            PixelTextButton("LOAD / CONTINUE", onLoad)
            Spacer(Modifier.height(8.dp))
            PixelTextButton("CLOSE", onClose)
        }
        PixelPanel(title = "Narration") {
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
        PixelPanel(title = "Session") {
            LabeledValue("Content", snapshot.contentId ?: "—")
            LabeledValue("Canon", snapshot.canonStatus ?: "—")
            LabeledValue("Scene", snapshot.sceneId)
            LabeledValue("Turn", snapshot.turn.toString())
        }
        PixelPanel(title = "Developer") {
            var cheatCode by remember { mutableStateOf("") }
            Text(
                "Cheats are validated by the Python game layer. Available test codes: FULLRESTORE, CLEARCONDITIONS, GIVE_RELAY, MAXATTR, DEBUGMAP.",
                color = PixelColors.Muted,
                style = MaterialTheme.typography.bodyMedium,
            )
            Spacer(Modifier.height(8.dp))
            OutlinedTextField(
                value = cheatCode,
                onValueChange = { cheatCode = it.uppercase() },
                label = { Text("CHEAT CODE") },
                singleLine = true,
                modifier = Modifier.fillMaxWidth(),
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
private fun InventorySection(
    snapshot: GameSnapshot,
    busy: Boolean,
    onEquip: (String) -> Unit,
    onUnequip: (String) -> Unit,
) {
    Column(
        modifier = Modifier.fillMaxSize().verticalScroll(rememberScrollState()),
        verticalArrangement = Arrangement.spacedBy(8.dp),
    ) {
        PixelPanel(title = "Equipment") {
            snapshot.inventory.equipment.forEach { slot ->
                val item = if (slot.equipped) {
                    buildString {
                        append(slot.name ?: slot.itemId ?: "EQUIPPED")
                        if (!slot.quality.isNullOrBlank()) append(" // ").append(slot.quality.uppercase())
                    }
                } else {
                    "EMPTY"
                }
                LabeledValue(slotDisplayName(slot.slot), item)
                if (slot.equipped) {
                    PixelTextButton(if (busy) "WORKING..." else "UNEQUIP") {
                        if (!busy) onUnequip(slot.slot)
                    }
                    Spacer(Modifier.height(6.dp))
                }
            }
        }

        PixelPanel(title = "Inventory") {
            if (snapshot.inventory.items.isEmpty()) {
                Text("No carried items.", color = PixelColors.Muted, style = MaterialTheme.typography.bodyMedium)
            } else {
                snapshot.inventory.items.forEach { item ->
                    LabeledValue(item.name, "x${item.quantity}")
                    if (item.equippable) {
                        PixelTextButton(
                            label = if (busy) {
                                "WORKING..."
                            } else {
                                "EQUIP // ${slotDisplayName(item.slot ?: "")}"
                            },
                            onClick = {
                                if (!busy) onEquip(item.id)
                            },
                        )
                        Spacer(Modifier.height(6.dp))
                    }
                }
            }
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
            PixelPanel(title = "Quests") {
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
                    PixelPanel(title = category) {
                        quests.forEach { quest ->
                            Text(quest.title, color = PixelColors.Gold, style = MaterialTheme.typography.titleLarge)
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
private fun MapSection(
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
        PixelPanel(title = map.title) {
            if (map.nodes.isEmpty()) {
                Text(
                    "No mapped location has been discovered yet.",
                    color = PixelColors.Muted,
                    style = MaterialTheme.typography.bodyLarge,
                )
            } else {
                Canvas(
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(220.dp)
                        .background(PixelColors.Deep)
                        .border(2.dp, PixelColors.Muted),
                ) {
                    fun point(id: String): Offset? {
                        val node = map.nodes.firstOrNull { it.id == id } ?: return null
                        return Offset(
                            x = (node.x.coerceIn(0.0, 100.0) / 100.0 * size.width).toFloat(),
                            y = (node.y.coerceIn(0.0, 100.0) / 100.0 * size.height).toFloat(),
                        )
                    }
                    map.edges.forEach { edge ->
                        val from = point(edge.from)
                        val to = point(edge.to)
                        if (from != null && to != null) drawLine(PixelColors.Muted, from, to, strokeWidth = 5f)
                    }
                    map.nodes.forEach { node ->
                        val p = point(node.id) ?: return@forEach
                        val nodeSize = if (node.current) 18f else 13f
                        drawRect(
                            color = if (node.current) PixelColors.Gold else PixelColors.Cyan,
                            topLeft = Offset(p.x - nodeSize / 2f, p.y - nodeSize / 2f),
                            size = androidx.compose.ui.geometry.Size(nodeSize, nodeSize),
                        )
                    }
                }

                Spacer(Modifier.height(10.dp))
                Text("DISCOVERED LOCATIONS", color = PixelColors.Gold, style = MaterialTheme.typography.labelLarge)
                Spacer(Modifier.height(6.dp))
                map.nodes.forEach { node ->
                    PixelTextButton(
                        label = if (node.current) "> ${node.title} [YOU]" else node.title,
                        onClick = { selectedId = node.id },
                    )
                    Spacer(Modifier.height(6.dp))
                }

                if (selected != null) {
                    Spacer(Modifier.height(8.dp))
                    Text(selected.title, color = PixelColors.Cyan, style = MaterialTheme.typography.titleLarge)
                    if (selected.description.isNotBlank()) {
                        Text(selected.description, color = PixelColors.Paper, style = MaterialTheme.typography.bodyMedium)
                    }
                    if (!selected.current) {
                        Spacer(Modifier.height(8.dp))
                        PixelTextButton(
                            label = if (busy) "TRAVELING..." else "TRAVEL HERE",
                            onClick = {
                                if (!busy) onTravel(selected.id)
                            },
                        )
                    }
                }
            }
        }
    }
}

@Composable
private fun MorePanel(onCharacter: () -> Unit, onSettings: () -> Unit) {
    PixelPanel(modifier = Modifier.fillMaxSize(), title = "More") {
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
        modifier = Modifier
            .background(if (active) PixelColors.Cyan else PixelColors.Deep)
            .border(2.dp, if (active) PixelColors.Paper else PixelColors.Muted)
            .clickable(role = Role.Tab, onClick = onClick)
            .padding(horizontal = 12.dp, vertical = 10.dp),
    ) {
        Text(
            text = label,
            color = if (active) PixelColors.Ink else PixelColors.Paper,
            style = MaterialTheme.typography.labelLarge,
        )
    }
}

@Composable
private fun PixelTextButton(label: String, onClick: () -> Unit) {
    Box(
        modifier = Modifier
            .background(PixelColors.PanelAlt)
            .border(2.dp, PixelColors.Cyan)
            .clickable(role = Role.Button, onClick = onClick)
            .padding(horizontal = 12.dp, vertical = 8.dp),
    ) {
        Text(label, color = PixelColors.Paper, style = MaterialTheme.typography.labelLarge)
    }
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
