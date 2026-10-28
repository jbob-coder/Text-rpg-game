package com.thegame.rpg.ui

import androidx.compose.foundation.Canvas
import androidx.compose.foundation.clickable
import androidx.compose.foundation.gestures.detectTapGestures
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.unit.dp
import com.thegame.rpg.GameUiState
import com.thegame.rpg.boot.BootState
import com.thegame.rpg.engine.GameMapNode
import com.thegame.rpg.engine.GameSnapshot
import com.thegame.rpg.engine.GameStatInspection
import kotlinx.coroutines.delay

/**
 * Text-first Android presentation. All rules, choices, movement permissions and
 * mutations remain owned by the Python GameEngine. The map is a navigation aid,
 * not a second world simulator. No sprites, scene images or transition animation.
 */
enum class GameSection(val label: String) {
    STORY("Story"), CHARACTER("Character"), STATS("Stats"),
    INVENTORY("Inventory"), QUESTS("Quests"), MAP("Map"), MORE("More")
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
        // Travel has already committed in Python. Acknowledge immediately:
        // the retired visual travel overlay must not stall the UI.
        LaunchedEffect(uiState.travelTransition?.token) {
            uiState.travelTransition?.let { onTravelTransitionFinished(it.token) }
        }
        TextGameShell(
            snapshot = snapshot, busy = uiState.busy,
            inspection = uiState.statInspection,
            inspectionPath = uiState.statInspectionPath,
            inspectionBusy = uiState.statInspectionBusy,
            inspectionError = uiState.statInspectionError,
            onChoice = onChoice, onSave = onSave, onLoad = onLoad,
            onNarrate = onNarrate, onReplayNarration = onReplayNarration,
            onStopNarration = onStopNarration, autoReadNarration = autoReadNarration,
            onAutoReadChange = onAutoReadChange, narrationRate = narrationRate,
            onNarrationRateChange = onNarrationRateChange,
            textDelayMs = textDelayMs, onTextDelayChange = onTextDelayChange,
            onCheat = onCheat, onEquip = onEquip, onUnequip = onUnequip,
            onInspectStatus = onInspectStatus, onTravel = onTravel,
        )
    } else {
        Column(Modifier.fillMaxSize().padding(24.dp), verticalArrangement = Arrangement.Center) {
            Text("THE GAME", style = MaterialTheme.typography.headlineMedium)
            Text("State: ${uiState.bootState.stageId}")
            if (uiState.bootState is BootState.Error) {
                Text(uiState.bootState.publicMessage, color = MaterialTheme.colorScheme.error)
            } else {
                Text("Loading world data...")
            }
        }
    }
}

/** Small stable story client retained for integration tests and preview consumers. */
@Composable
fun GameScreen(
    snapshot: GameSnapshot,
    busy: Boolean,
    onChoice: (String) -> Unit,
    onNavigate: (String) -> Unit,
) {
    Column(Modifier.fillMaxSize().padding(12.dp)) {
        Text("THE GAME — ${snapshot.location}", style = MaterialTheme.typography.titleLarge)
        Box(Modifier.weight(1f)) {
            TextStory(snapshot, busy, onChoice, onNarrate = { false }, textDelayMs = 0)
        }
        Row(Modifier.fillMaxWidth().horizontalScroll(rememberScrollState())) {
            listOf("Stats", "Inventory", "Quests", "Map", "More").forEach { label ->
                TextButton(onClick = { onNavigate(label) }, modifier = Modifier.testTag("nav-${label.lowercase()}")) {
                    Text(label)
                }
            }
        }
    }
}

@Composable
private fun TextGameShell(
    snapshot: GameSnapshot,
    busy: Boolean,
    inspection: GameStatInspection?,
    inspectionPath: String?,
    inspectionBusy: Boolean,
    inspectionError: String?,
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
    var settings by remember { mutableStateOf(false) }
    LaunchedEffect(snapshot.sceneId) {
        section = GameSection.STORY
        settings = false
    }
    LaunchedEffect(snapshot.sceneId, autoReadNarration) {
        if (autoReadNarration) onNarrate(snapshot.body)
    }
    Column(Modifier.fillMaxSize().padding(12.dp)) {
        Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween) {
            Column {
                Text("THE GAME", style = MaterialTheme.typography.titleLarge)
                Text("Location: ${snapshot.location} · Turn ${snapshot.turn}")
            }
            TextButton(onClick = { settings = true }, modifier = Modifier.testTag("settings")) {
                Text("SETTINGS")
            }
        }
        Box(Modifier.weight(1f)) {
            when {
                settings -> TextSettings(
                    snapshot, onSave, { onLoad(); settings = false },
                    onReplayNarration, onStopNarration, autoReadNarration,
                    onAutoReadChange, narrationRate, onNarrationRateChange,
                    textDelayMs, onTextDelayChange, onCheat,
                    onClose = { settings = false },
                )
                section == GameSection.STORY -> TextStory(snapshot, busy, onChoice, onNarrate, textDelayMs)
                section == GameSection.CHARACTER -> TextCharacter(snapshot, busy, onEquip, onUnequip)
                section == GameSection.STATS -> TextStats(snapshot, inspection, inspectionPath, inspectionBusy, inspectionError, onInspectStatus)
                section == GameSection.INVENTORY -> TextInventory(snapshot, busy, onEquip, onUnequip)
                section == GameSection.QUESTS -> TextQuests(snapshot)
                section == GameSection.MAP -> MapSection(snapshot, busy, onTravel)
                else -> Column(Modifier.verticalScroll(rememberScrollState())) {
                    Text("More", style = MaterialTheme.typography.titleLarge)
                    TextButton(onClick = { section = GameSection.CHARACTER }) { Text("Character") }
                    TextButton(onClick = { settings = true }) { Text("Settings") }
                }
            }
        }
        Row(Modifier.fillMaxWidth().horizontalScroll(rememberScrollState())) {
            GameSection.entries.forEach { tab ->
                OutlinedButton(
                    onClick = { section = tab; settings = false },
                    modifier = Modifier.testTag("nav-${tab.label.lowercase()}"),
                ) { Text(tab.label) }
            }
        }
    }
}

@Composable
private fun TextStory(
    snapshot: GameSnapshot,
    busy: Boolean,
    onChoice: (String) -> Unit,
    onNarrate: (String) -> Boolean,
    textDelayMs: Int,
) {
    var visible by remember(snapshot.sceneId, snapshot.body, textDelayMs) {
        mutableIntStateOf(if (textDelayMs == 0) snapshot.body.length else 0)
    }
    LaunchedEffect(snapshot.sceneId, snapshot.body, textDelayMs) {
        if (textDelayMs <= 0) visible = snapshot.body.length
        else while (visible < snapshot.body.length) {
            delay(textDelayMs.toLong())
            visible = (visible + 3).coerceAtMost(snapshot.body.length)
        }
    }
    Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()).testTag("narrative-scroll")) {
        Text(snapshot.title, modifier = Modifier.testTag("scene-title"), style = MaterialTheme.typography.titleLarge)
        Text(snapshot.body.take(visible), modifier = Modifier.clickable { onNarrate(snapshot.body) }.padding(vertical = 12.dp))
        if (snapshot.room.actors.isNotEmpty()) {
            Text("Present:", style = MaterialTheme.typography.titleMedium)
            snapshot.room.actors.forEach { actor -> Text(actor.displayName) }
        }
        if (snapshot.resources.isNotEmpty()) {
            Text("Status", style = MaterialTheme.typography.titleMedium)
            snapshot.resources.forEach { res -> Text("${res.id}: ${res.current} / ${res.max}") }
        }
        TextButton(onClick = { onNarrate(snapshot.body) }) { Text("READ ALOUD") }
        Text("Decisions", style = MaterialTheme.typography.titleMedium)
        snapshot.choices.forEach { choice ->
            OutlinedButton(
                onClick = { onChoice(choice.id) }, enabled = !busy && choice.enabled,
                modifier = Modifier.fillMaxWidth().testTag("choice-${choice.id}"),
            ) { Text(choice.text + if (choice.enabled) "" else " — ${choice.disabledReason ?: "Locked"}") }
        }
        if (snapshot.choices.isEmpty()) Text("No choices are currently available.")
    }
}

@Composable
private fun TextCharacter(
    snapshot: GameSnapshot, busy: Boolean,
    onEquip: (String) -> Unit, onUnequip: (String) -> Unit,
) {
    var selected by remember { mutableStateOf<String?>(null) }
    Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState())) {
        Text("Character", style = MaterialTheme.typography.titleLarge)
        Text(snapshot.identity.name ?: "Unknown character")
        Text("Origin: ${snapshot.identity.origin ?: "Unknown"}")
        Text("Level: ${snapshot.identity.level ?: 0}")
        Text("Equipment", style = MaterialTheme.typography.titleMedium)
        snapshot.inventory.equipment.forEach { slot ->
            OutlinedButton(
                modifier = Modifier.fillMaxWidth().testTag("character-slot-${slot.slot}"),
                onClick = { selected = slot.slot },
            ) { Text("${slot.slot.replace('_', ' ')}: ${slot.name ?: "Empty slot"}") }
            if (selected == slot.slot) {
                if (slot.equipped) {
                    Button(onClick = { onUnequip(slot.slot) }, enabled = !busy, modifier = Modifier.testTag("character-unequip")) {
                        Text("UNEQUIP")
                    }
                }
                snapshot.inventory.items.filter { it.equippable && (it.slot == null || it.slot == slot.slot) }.forEach { item ->
                    TextButton(
                        enabled = !busy,
                        onClick = { onEquip(item.id) },
                        modifier = Modifier.testTag("character-equip-${item.id}"),
                    ) { Text("Equip ${item.name}") }
                }
            }
        }
    }
}

@Composable
private fun TextStats(
    snapshot: GameSnapshot, inspection: GameStatInspection?,
    path: String?, busy: Boolean, error: String?, onInspect: (String) -> Unit,
) {
    Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState())) {
        Text("Stats", style = MaterialTheme.typography.titleLarge)
        snapshot.attributes.forEach { stat ->
            TextButton(
                enabled = !busy,
                onClick = { onInspect("attributes.${stat.id}") },
                modifier = Modifier.testTag("stats-attribute-${stat.id}"),
            ) { Text("${stat.name}: ${stat.effective} (base ${stat.base})") }
        }
        snapshot.derived.forEach { Text("${it.name}: ${it.value}") }
        Text("Skills", style = MaterialTheme.typography.titleMedium)
        snapshot.skills.forEach { skill ->
            TextButton(onClick = { onInspect("skills.${skill.id}") }, enabled = !busy) {
                Text("${skill.name}: ${skill.effective}")
            }
        }
        snapshot.conditions.forEach { Text("Condition: ${it.name} (severity ${it.severity})") }
        if (busy) Text("Inspecting...")
        if (error != null) Text(error, color = MaterialTheme.colorScheme.error)
        if (path != null && inspection != null) {
            Column(Modifier.testTag("stats-attribute-detail").padding(vertical = 8.dp)) {
                Text("Effective ${inspection.total} • ${inspection.path}")
                inspection.contributions.forEach { Text("${it.source}: ${it.value}") }
            }
        }
    }
}

@Composable
private fun TextInventory(
    snapshot: GameSnapshot, busy: Boolean,
    onEquip: (String) -> Unit, onUnequip: (String) -> Unit,
) {
    Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState())) {
        Text("Inventory", style = MaterialTheme.typography.titleLarge)
        snapshot.inventory.items.forEach { item ->
            Text("${item.name} × ${item.quantity}")
            if (item.equippable) {
                TextButton(onClick = { onEquip(item.id) }, enabled = !busy) { Text("EQUIP ${item.name}") }
            }
        }
        Text("Equipped", style = MaterialTheme.typography.titleMedium)
        snapshot.inventory.equipment.filter { it.equipped }.forEach { slot ->
            Text("${slot.slot}: ${slot.name ?: slot.itemId}")
            TextButton(onClick = { onUnequip(slot.slot) }, enabled = !busy) { Text("UNEQUIP ${slot.slot}") }
        }
    }
}

@Composable
private fun TextQuests(snapshot: GameSnapshot) {
    Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState())) {
        Text("Quests", style = MaterialTheme.typography.titleLarge)
        snapshot.quests.forEach { quest ->
            Text("${quest.title} — ${quest.status}", style = MaterialTheme.typography.titleMedium)
            Text(quest.description)
            Text("Stage: ${quest.stage}")
            quest.objectives.forEach { Text("${it.title}: ${it.status}") }
        }
        if (snapshot.quests.isEmpty()) Text("No quests recorded.")
    }
}

/** Retains the existing player-safe map nodes, links and travel permission. */
@Composable
internal fun MapSection(snapshot: GameSnapshot, busy: Boolean, onTravel: (String) -> Unit) {
    val map = snapshot.worldMap
    var selectedId by remember(map.currentLocation, map.nodes) { mutableStateOf(map.currentLocation) }
    val selected = map.nodes.firstOrNull { it.id == selectedId }
        ?: map.nodes.firstOrNull { it.current }
        ?: map.nodes.firstOrNull()
    val minX = map.nodes.minOfOrNull { it.x } ?: 0.0
    val maxX = map.nodes.maxOfOrNull { it.x } ?: 1.0
    val minY = map.nodes.minOfOrNull { it.y } ?: 0.0
    val maxY = map.nodes.maxOfOrNull { it.y } ?: 1.0
    val dx = (maxX - minX).coerceAtLeast(1.0)
    val dy = (maxY - minY).coerceAtLeast(1.0)
    fun point(node: GameMapNode, width: Float, height: Float): Offset {
        val pad = 26f
        return Offset(
            pad + ((node.x - minX) / dx).toFloat() * (width - pad * 2).coerceAtLeast(0f),
            pad + ((node.y - minY) / dy).toFloat() * (height - pad * 2).coerceAtLeast(0f),
        )
    }
    val nodesById = map.nodes.associateBy { it.id }
    val lineColor = MaterialTheme.colorScheme.outline
    val nodeColor = MaterialTheme.colorScheme.primary
    val hereColor = MaterialTheme.colorScheme.tertiary
    Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState())) {
        Text(map.title, style = MaterialTheme.typography.titleLarge)
        if (map.nodes.isEmpty()) {
            Text("No mapped location has been discovered yet.")
        } else {
            Canvas(
                modifier = Modifier.fillMaxWidth().height(220.dp).testTag("world-map-canvas")
                    .pointerInput(map.nodes) {
                        detectTapGestures { tap ->
                            val nearest = map.nodes.minByOrNull {
                                val p = point(it, size.width.toFloat(), size.height.toFloat())
                                val x = p.x - tap.x
                                val y = p.y - tap.y
                                x * x + y * y
                            }
                            if (nearest != null) {
                                val p = point(nearest, size.width.toFloat(), size.height.toFloat())
                                val x = p.x - tap.x
                                val y = p.y - tap.y
                                if (x * x + y * y <= 36.dp.toPx() * 36.dp.toPx()) selectedId = nearest.id
                            }
                        }
                    },
            ) {
                map.edges.forEach { edge ->
                    val a = nodesById[edge.from]
                    val b = nodesById[edge.to]
                    if (a != null && b != null) {
                        drawLine(lineColor, point(a, size.width, size.height), point(b, size.width, size.height), strokeWidth = 3f)
                    }
                }
                map.nodes.forEach { node ->
                    drawCircle(if (node.current) hereColor else nodeColor, radius = if (node.current) 10f else 7f, center = point(node, size.width, size.height))
                }
            }
            Text("Discovered locations", style = MaterialTheme.typography.titleMedium)
            map.nodes.forEach { node ->
                TextButton(
                    onClick = { selectedId = node.id },
                    modifier = Modifier.testTag("map-node-${node.id}"),
                ) { Text(node.title + if (node.current) " [YOU]" else "") }
            }
            if (selected != null) {
                Text(selected.title, style = MaterialTheme.typography.titleMedium)
                if (selected.description.isNotBlank()) Text(selected.description)
                if (!selected.current) {
                    if (selected.reachable) {
                        Button(
                            onClick = { onTravel(selected.id) },
                            enabled = !busy,
                            modifier = Modifier.testTag("map-travel"),
                        ) { Text(if (busy) "TRAVELING..." else "TRAVEL HERE") }
                    } else Text("NO DIRECT ROUTE FROM CURRENT LOCATION")
                }
            }
        }
    }
}

@Composable
private fun TextSettings(
    snapshot: GameSnapshot,
    onSave: () -> Unit, onLoad: () -> Unit,
    onReplayNarration: () -> Boolean, onStopNarration: () -> Unit,
    autoReadNarration: Boolean, onAutoReadChange: (Boolean) -> Unit,
    narrationRate: Float, onNarrationRateChange: (Float) -> Unit,
    textDelayMs: Int, onTextDelayChange: (Int) -> Unit,
    onCheat: (String) -> Unit, onClose: () -> Unit,
) {
    var cheatCode by remember { mutableStateOf("") }
    Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState())) {
        Text("Settings", style = MaterialTheme.typography.titleLarge)
        Button(onClick = onSave) { Text("SAVE GAME") }
        Button(onClick = onLoad) { Text("LOAD / CONTINUE") }
        TextButton(onClick = onClose) { Text("CLOSE") }
        Text("Narration", style = MaterialTheme.typography.titleMedium)
        TextButton(onClick = { onReplayNarration() }) { Text("REPLAY NARRATION") }
        TextButton(onClick = { onAutoReadChange(!autoReadNarration) }) {
            Text(if (autoReadNarration) "AUTO-READ // ON" else "AUTO-READ // OFF")
        }
        Text("VOICE SPEED // ${String.format("%.2fx", narrationRate)}")
        Row {
            TextButton(onClick = { onNarrationRateChange((narrationRate - 0.1f).coerceAtLeast(0.5f)) }) { Text("SLOWER") }
            TextButton(onClick = { onNarrationRateChange((narrationRate + 0.1f).coerceAtMost(1.5f)) }) { Text("FASTER") }
        }
        Text("TEXT REVEAL // ${if (textDelayMs <= 0) "INSTANT" else "${textDelayMs} ms"}")
        TextButton(onClick = {
            onTextDelayChange(when (textDelayMs) { 0 -> 15; 15 -> 35; 35 -> 70; else -> 0 })
        }) { Text("CYCLE TEXT SPEED") }
        TextButton(onClick = onStopNarration) { Text("STOP NARRATION") }
        Text("Session: ${snapshot.contentId ?: "—"} / ${snapshot.canonStatus ?: "—"}")
        Text("Developer", style = MaterialTheme.typography.titleMedium)
        TextButton(onClick = { onCheat("DISTRICT") }) { Text("CHEAT // DISTRICT FREE ROAM") }
        TextButton(onClick = { onCheat("FULLRESTORE") }) { Text("CHEAT // FULL RESTORE") }
        TextButton(onClick = { onCheat("DEBUGMAP") }) { Text("CHEAT // DEBUG MAP") }
        OutlinedTextField(
            value = cheatCode, onValueChange = { cheatCode = it.uppercase() },
            label = { Text("CHEAT CODE") }, singleLine = true,
            modifier = Modifier.fillMaxWidth().testTag("cheat-input"),
        )
        TextButton(onClick = {
            if (cheatCode.isNotBlank()) {
                onCheat(cheatCode)
                cheatCode = ""
            }
        }) { Text("APPLY CHEAT") }
    }
}
