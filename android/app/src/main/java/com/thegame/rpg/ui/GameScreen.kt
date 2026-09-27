package com.thegame.rpg.ui

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
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.unit.dp
import com.thegame.rpg.GameUiState
import com.thegame.rpg.boot.BootState
import com.thegame.rpg.engine.GameSnapshot
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
) {
    val snapshot = uiState.snapshot
    if (uiState.bootState == BootState.Ready && snapshot != null) {
        PixelGameShell(snapshot, uiState.busy, onChoice, onSave, onLoad)
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
            StorySection(snapshot, busy, onChoice)
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
) {
    var section by remember { mutableStateOf(GameSection.STORY) }
    var settingsOpen by remember { mutableStateOf(false) }

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
                SettingsPanel(snapshot, onSave, onLoad) { settingsOpen = false }
            } else {
                when (section) {
                    GameSection.STORY -> StorySection(snapshot, busy, onChoice)
                    GameSection.CHARACTER -> CharacterSection(snapshot)
                    GameSection.STATS -> StatsSection(snapshot)
                    GameSection.INVENTORY -> ComingPanel(
                        "Inventory",
                        "Inventory is engine-owned. The item and equipment browser will render authoritative inventory state here.",
                    )
                    GameSection.QUESTS -> ComingPanel(
                        "Quests",
                        "Main, side, optional, and lore quest categories will render from a player-safe quest projection.",
                    )
                    GameSection.MAP -> ComingPanel(
                        "World Map",
                        "The interactive pixel map will use authored location IDs and routes, never a second UI-owned world state.",
                    )
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
private fun StorySection(snapshot: GameSnapshot, busy: Boolean, onChoice: (String) -> Unit) {
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
    modifier: Modifier,
) {
    PixelPanel(modifier = modifier, title = snapshot.title) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .testTag("narrative-scroll")
                .verticalScroll(rememberScrollState()),
        ) {
            Text(snapshot.body, color = PixelColors.Paper, style = MaterialTheme.typography.bodyLarge)
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
        Row(
            modifier = Modifier
                .fillMaxSize()
                .horizontalScroll(rememberScrollState()),
            horizontalArrangement = Arrangement.spacedBy(8.dp),
        ) {
            PlayerAvatarPanel(snapshot.identity, Modifier.width(if (maxWidth > 700.dp) 320.dp else 260.dp))
            PixelPanel(Modifier.width(if (maxWidth > 700.dp) 420.dp else 320.dp), "Character") {
                LabeledValue("Name", snapshot.identity.name ?: "Unassigned")
                LabeledValue("Level", snapshot.identity.level?.toString() ?: "—")
                LabeledValue("Path", snapshot.identity.path ?: "—")
                LabeledValue("Origin", snapshot.identity.origin ?: "—")
                LabeledValue("Background", snapshot.identity.background ?: "—")
                Spacer(Modifier.height(12.dp))
                Text("EQUIPMENT SLOTS", color = PixelColors.Gold, style = MaterialTheme.typography.titleLarge)
                Spacer(Modifier.height(6.dp))
                listOf(
                    "HEAD", "CHEST", "HANDS", "LEGS", "FEET", "MAIN HAND",
                    "OFF HAND", "RING I", "RING II", "NECK", "ACCESSORY",
                ).chunked(2).forEach { row ->
                    Text(row.joinToString("   "), color = PixelColors.Muted, style = MaterialTheme.typography.bodyMedium)
                    Spacer(Modifier.height(4.dp))
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
                "Tap-to-narrate, auto-read, voice, and text-delay controls are next in the native TTS slice.",
                color = PixelColors.Muted,
                style = MaterialTheme.typography.bodyMedium,
            )
        }
        PixelPanel(title = "Session") {
            LabeledValue("Content", snapshot.contentId ?: "—")
            LabeledValue("Canon", snapshot.canonStatus ?: "—")
            LabeledValue("Scene", snapshot.sceneId)
            LabeledValue("Turn", snapshot.turn.toString())
        }
        PixelPanel(title = "Developer") {
            Text(
                "Developer and cheat commands will be isolated here and routed through validated Python commands.",
                color = PixelColors.Muted,
                style = MaterialTheme.typography.bodyMedium,
            )
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

private fun formatGameTime(minutes: Int): String {
    val days = minutes / (24 * 60)
    val withinDay = minutes % (24 * 60)
    val hours = withinDay / 60
    val mins = withinDay % 60
    return if (days > 0) "D${days + 1} %02d:%02d".format(hours, mins) else "%02d:%02d".format(hours, mins)
}

private fun signed(value: Double): String =
    if (value >= 0) "+${value.roundToInt()}" else value.roundToInt().toString()
