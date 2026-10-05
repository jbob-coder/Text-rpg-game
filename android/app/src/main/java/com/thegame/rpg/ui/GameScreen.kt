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
    STORY("Story"), CHARACTER("Character"), STATS("Stats"), INVENTORY("Inventory"),
    QUESTS("Quests"), MAP("Map"), MORE("More"),
}

@Composable
fun TheGameRoot(uiState: GameUiState, onChoice: (String) -> Unit, onSave: () -> Unit, onLoad: () -> Unit,
    onNarrate: (String) -> Boolean, onReplayNarration: () -> Boolean, onStopNarration: () -> Unit,
    autoReadNarration: Boolean, onAutoReadChange: (Boolean) -> Unit, narrationRate: Float,
    onNarrationRateChange: (Float) -> Unit, textDelayMs: Int, onTextDelayChange: (Int) -> Unit,
    onCheat: (String) -> Unit, onEquip: (String) -> Unit, onUnequip: (String) -> Unit,
    onInspectStatus: (String) -> Unit, onTravel: (String) -> Unit, onTravelTransitionFinished: (Long) -> Unit) {
    val snapshot = uiState.snapshot
    if (uiState.bootState == BootState.Ready && snapshot != null) {
        Box(Modifier.fillMaxSize()) {
            PixelGameShell(snapshot, uiState.busy, uiState.statInspectionPath, uiState.statInspection,
                uiState.statInspectionBusy, uiState.statInspectionError, onChoice, onSave, onLoad, onNarrate,
                onReplayNarration, onStopNarration, autoReadNarration, onAutoReadChange, narrationRate,
                onNarrationRateChange, textDelayMs, onTextDelayChange, onCheat, onEquip, onUnequip,
                onInspectStatus, onTravel)
            uiState.travelTransition?.let { transition ->
                MapTravelTransitionOverlay(transition, onTravelTransitionFinished, Modifier.fillMaxSize())
            }
        }
    } else PixelBootScreen(uiState.bootState)
}

/** Stable UI contract used by Compose instrumentation tests and preview clients. */
@Composable
fun GameScreen(snapshot: GameSnapshot, busy: Boolean, onChoice: (String) -> Unit, onNavigate: (String) -> Unit) {
    Column(Modifier.fillMaxSize().background(PixelColors.Ink).padding(8.dp)) {
        TopStatusBar(snapshot) { onNavigate("More") }; Spacer(Modifier.height(8.dp))
        Box(Modifier.weight(1f)) { StorySection(snapshot, busy, onChoice, { false }, 0) }
        Spacer(Modifier.height(8.dp)); Row(Modifier.fillMaxWidth().horizontalScroll(rememberScrollState()), horizontalArrangement = Arrangement.spacedBy(4.dp)) {
            listOf("Stats", "Inventory", "Quests", "Map", "More").forEach { PixelNavButton(it, false) { onNavigate(it) } }
        }
    }
}

@Composable private fun PixelBootScreen(state: BootState) {
    Box(Modifier.fillMaxSize().background(PixelColors.Ink).padding(24.dp), contentAlignment = Alignment.Center) {
        PixelPanel { Text("THE GAME", color = PixelColors.Gold, style = MaterialTheme.typography.headlineLarge); Spacer(Modifier.height(10.dp)); Text("[${state.stageId}]", color = PixelColors.Cyan)
            Spacer(Modifier.height(8.dp)); if (state is BootState.Error) Text(state.publicMessage, color = PixelColors.Danger) else Text("Loading world data...", color = PixelColors.Muted) }
    }
}

@Composable private fun PixelGameShell(snapshot: GameSnapshot, busy: Boolean, statInspectionPath: String?, statInspection: GameStatInspection?, statInspectionBusy: Boolean,
    statInspectionError: String?, onChoice: (String) -> Unit, onSave: () -> Unit, onLoad: () -> Unit, onNarrate: (String) -> Boolean,
    onReplayNarration: () -> Boolean, onStopNarration: () -> Unit, autoReadNarration: Boolean, onAutoReadChange: (Boolean) -> Unit,
    narrationRate: Float, onNarrationRateChange: (Float) -> Unit, textDelayMs: Int, onTextDelayChange: (Int) -> Unit, onCheat: (String) -> Unit,
    onEquip: (String) -> Unit, onUnequip: (String) -> Unit, onInspectStatus: (String) -> Unit, onTravel: (String) -> Unit) {
    var section by remember { mutableStateOf(GameSection.STORY) }; var settingsOpen by remember { mutableStateOf(false) }; var lastSceneId by remember { mutableStateOf(snapshot.sceneId) }
    LaunchedEffect(snapshot.sceneId) { if (snapshot.sceneId != lastSceneId) { section = GameSection.STORY; settingsOpen = false; lastSceneId = snapshot.sceneId } }
    LaunchedEffect(snapshot.sceneId, autoReadNarration) { if (autoReadNarration) onNarrate(snapshot.body) }
    Column(Modifier.fillMaxSize().background(PixelColors.Ink).padding(8.dp)) {
        TopStatusBar(snapshot) { settingsOpen = !settingsOpen }; Spacer(Modifier.height(8.dp)); Box(Modifier.weight(1f)) {
            if (settingsOpen) SettingsPanel(snapshot, onSave, onLoad, onReplayNarration, onStopNarration, autoReadNarration, onAutoReadChange, narrationRate, onNarrationRateChange, textDelayMs, onTextDelayChange, onCheat) { settingsOpen = false }
            else when (section) {
                GameSection.STORY -> StorySection(snapshot, busy, onChoice, onNarrate, textDelayMs)
                GameSection.CHARACTER -> CharacterSection(snapshot, busy, onEquip, onUnequip)
                GameSection.STATS -> StatsSection(snapshot, statInspectionPath, statInspection, statInspectionBusy, statInspectionError, onInspectStatus)
                GameSection.INVENTORY -> InventorySection(snapshot, busy, onEquip, onUnequip)
                GameSection.QUESTS -> QuestSection(snapshot); GameSection.MAP -> MapSection(snapshot, busy, onTravel)
                GameSection.MORE -> MorePanel({ section = GameSection.CHARACTER }) { settingsOpen = true }
            }
        }; Spacer(Modifier.height(8.dp)); BottomPixelNav(section) { section = it; settingsOpen = false }
    }
}

@Composable private fun TopStatusBar(snapshot: GameSnapshot, onSettings: () -> Unit) {
    Row(Modifier.fillMaxWidth().background(PixelColors.Deep).border(2.dp, PixelColors.Muted).padding(10.dp, 8.dp), verticalAlignment = Alignment.CenterVertically) {
        Column(Modifier.weight(1f)) { Text(snapshot.location.replace('_', ' '), color = PixelColors.Cyan); Text("TURN ${snapshot.turn}  //  ${formatGameTime(snapshot.timeMinutes)}", color = PixelColors.Muted) }; PixelTextButton("SETTINGS", onSettings)
    }
}

@Composable private fun StorySection(snapshot: GameSnapshot, busy: Boolean, onChoice: (String) -> Unit, onNarrate: (String) -> Boolean, textDelayMs: Int) {
    BoxWithConstraints(Modifier.fillMaxSize()) {
        if (maxWidth >= 720.dp) Row(Modifier.fillMaxSize(), horizontalArrangement = Arrangement.spacedBy(8.dp)) {
            Column(Modifier.weight(.36f).fillMaxHeight()) { PlayerAvatarPanel(snapshot.identity, snapshot.inventory.equipment, snapshot.conditions); Spacer(Modifier.height(8.dp)); ResourcePanel(snapshot) }
            NarrativePanel(snapshot, busy, onChoice, onNarrate, textDelayMs, Modifier.weight(.64f).fillMaxHeight())
        } else Column(Modifier.fillMaxSize(), verticalArrangement = Arrangement.spacedBy(8.dp)) {
            Row(Modifier.fillMaxWidth().height(210.dp).testTag("story-pixel-header"), horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                SceneIllustration(snapshot.location, snapshot.sceneId, snapshot.visuals.relayState, snapshot.room.actors, Modifier.weight(.68f).fillMaxHeight())
                PlayerAvatarPanel(snapshot.identity, snapshot.inventory.equipment, snapshot.conditions, Modifier.weight(.32f).fillMaxHeight(), true, false)
            }; StoryResourceHud(snapshot, Modifier.fillMaxWidth()); NarrativePanel(snapshot, busy, onChoice, onNarrate, textDelayMs, Modifier.fillMaxWidth().weight(1f), false)
        }
    }
}

@Composable private fun NarrativePanel(snapshot: GameSnapshot, busy: Boolean, onChoice: (String) -> Unit, onNarrate: (String) -> Boolean, textDelayMs: Int, modifier: Modifier, showSceneIllustration: Boolean = true) {
    var visibleChars by remember(snapshot.sceneId, snapshot.body, textDelayMs) { mutableStateOf(if (textDelayMs <= 0) snapshot.body.length else 0) }
    LaunchedEffect(snapshot.sceneId, snapshot.body, textDelayMs) { if (textDelayMs <= 0) visibleChars = snapshot.body.length else { visibleChars = 0; while (visibleChars < snapshot.body.length) { delay(textDelayMs.toLong()); visibleChars = (visibleChars + 3).coerceAtMost(snapshot.body.length) } } }
    val scroll = rememberScrollState(); LaunchedEffect(snapshot.sceneId) { scroll.scrollTo(0) }
    PixelPanel(modifier) { Box(Modifier.fillMaxSize()) { Column(Modifier.fillMaxSize().padding(bottom = 22.dp).testTag("narrative-scroll").verticalScroll(scroll)) {
        Text(snapshot.title, color = PixelColors.Cyan, style = MaterialTheme.typography.titleLarge, modifier = Modifier.testTag("scene-title")); if (showSceneIllustration) { Spacer(Modifier.height(8.dp)); SceneIllustration(snapshot.location, snapshot.sceneId, snapshot.visuals.relayState, snapshot.room.actors, Modifier.fillMaxWidth().height(150.dp)); Spacer(Modifier.height(12.dp)) } else Spacer(Modifier.height(8.dp))
        Text(snapshot.body.take(visibleChars), color = PixelColors.Paper, modifier = Modifier.clickable(role = Role.Button) { onNarrate(snapshot.body) }); Spacer(Modifier.height(10.dp)); PixelIconTextButton("READ ALOUD", PixelUiUtilityCatalog.narrationIcon) { onNarrate(snapshot.body) }; Spacer(Modifier.height(18.dp)); Text("DECIDE", color = PixelColors.Gold); Spacer(Modifier.height(8.dp)); snapshot.choices.forEach { PixelChoiceCard(it, busy) { onChoice(it.id) }; Spacer(Modifier.height(8.dp)) }
    }; if (scroll.value < scroll.maxValue) PixelUiIcon(PixelUiUtilityCatalog.scrollMarker, Modifier.align(Alignment.BottomCenter).size(18.dp).background(PixelColors.PanelAlt), testTag = "narrative-scroll-marker") } }
}

@Composable private fun StoryResourceHud(snapshot: GameSnapshot, modifier: Modifier = Modifier) { if (snapshot.resources.isEmpty()) return; Column(modifier.pixelChrome(PixelUiChromeCatalog.statsFrame).padding(8.dp, 6.dp).testTag("story-resource-hud"), verticalArrangement = Arrangement.spacedBy(5.dp)) { snapshot.resources.forEach { r -> val ratio = if (r.max > 0) (r.current/r.max).coerceIn(0.0,1.0) else 0.0; val c = resourceColor(r.id); Row(Modifier.fillMaxWidth(), verticalAlignment = Alignment.CenterVertically) { PixelUiIcon(PixelUiIconCatalog.resource(r.id), Modifier.size(14.dp), c); Spacer(Modifier.width(6.dp)); Text(r.id.uppercase(), color=PixelColors.Muted, modifier=Modifier.width(64.dp)); PixelResourceBar(ratio.toFloat(), c, Modifier.weight(1f)); Spacer(Modifier.width(6.dp)); Text("${r.current.roundToInt()}/${r.max.roundToInt()}", color=PixelColors.Paper) } } } }
@Composable private fun ResourcePanel(snapshot: GameSnapshot) { PixelPanel { Text("RESOURCES", color=PixelColors.Gold); snapshot.resources.forEach { r -> Text("${r.id.uppercase()} ${r.current.roundToInt()}/${r.max.roundToInt()}", color=PixelColors.Paper); PixelResourceBar((if(r.max>0) r.current/r.max else 0.0).toFloat(), resourceColor(r.id), Modifier.fillMaxWidth()); Spacer(Modifier.height(7.dp)) }; if(snapshot.resources.isEmpty()) Text("NO ACTIVE RESOURCES", color=PixelColors.Muted) } }
private fun resourceColor(id:String)=when(id.lowercase()){ "health"->PixelColors.Health;"stamina"->PixelColors.Stamina;"focus"->PixelColors.Focus;"resolve"->PixelColors.Resolve;else->PixelColors.Paper }

@Composable private fun StatsSection(snapshot:GameSnapshot, selectedPath:String?, inspection:GameStatInspection?, inspectionBusy:Boolean, inspectionError:String?, onInspect:(String)->Unit){ var tab by remember{mutableStateOf(StatTab.SUMMARY)}; var path by remember(selectedPath){mutableStateOf(selectedPath.orEmpty())}; Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()),verticalArrangement=Arrangement.spacedBy(8.dp)){ PixelPanel{Text("STATUS // READ-ONLY",color=PixelColors.Gold); Row(horizontalArrangement=Arrangement.spacedBy(6.dp)){StatTab.entries.forEach{t->PixelTextButton(t.label,{tab=t},Modifier.testTag("stats-tab-${t.name.lowercase()}"),t!=tab)}}}; when(tab){StatTab.SUMMARY->StatsSummaryTab(snapshot);StatTab.CONDITIONS->StatsConditionsTab(snapshot);StatTab.INSPECT->StatsInspectTab(path,{path=it},inspection,inspectionBusy,inspectionError){onInspect(path)}} } }
private enum class StatTab(val label:String){SUMMARY("SUMMARY"),CONDITIONS("CONDITIONS"),INSPECT("INSPECT")}
@Composable private fun StatsSummaryTab(s:GameSnapshot){PixelPanel{Text("SUMMARY",color=PixelColors.Cyan);s.resources.forEach{Text("${it.id.uppercase()} ${it.current.roundToInt()}/${it.max.roundToInt()}",color=PixelColors.Paper)};if(s.resources.isEmpty())Text("NO ACTIVE RESOURCES",color=PixelColors.Muted)}}
@Composable private fun StatsConditionsTab(s:GameSnapshot){PixelPanel{Text("CONDITIONS",color=PixelColors.Cyan);s.conditions.forEach{Text("• $it",color=PixelColors.Paper)};if(s.conditions.isEmpty())Text("NONE",color=PixelColors.Muted)}}
@Composable private fun StatsInspectTab(path:String,onPathChange:(String)->Unit,inspection:GameStatInspection?,busy:Boolean,error:String?,onInspect:()->Unit){PixelPanel{Text("INSPECT",color=PixelColors.Cyan);OutlinedTextField(path,onPathChange,label={Text("Stat path")},singleLine=true,modifier=Modifier.fillMaxWidth().testTag("stats-inspect-path"));PixelTextButton(if(busy)"INSPECTING..." else "INSPECT",onInspect,Modifier.testTag("stats-inspect-button"),!busy);if(!error.isNullOrBlank())Text(error,color=PixelColors.Danger);inspection?.let{Text(it.label,color=PixelColors.Gold);Text("${it.value.roundToInt()}  //  ${it.source.uppercase()}",color=PixelColors.Paper);it.description?.takeIf(String::isNotBlank)?.let{d->Text(d,color=PixelColors.Muted)}}}}

@Composable private fun InventorySection(s:GameSnapshot,busy:Boolean,onEquip:(String)->Unit,onUnequip:(String)->Unit){var selected by remember(s.sceneId){mutableStateOf<String?>(null)};Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()),verticalArrangement=Arrangement.spacedBy(8.dp)){PixelPanel{Text("INVENTORY",color=PixelColors.Gold);if(s.inventory.items.isEmpty())Text("PACK EMPTY",color=PixelColors.Muted)else s.inventory.items.forEach{item->InventoryRow(item,item.id in s.inventory.equipment.equippedItemIds,item.id==selected){selected=item.id}}};s.inventory.items.firstOrNull{it.id==selected}?.let{InventoryDetailPanel(it,s.inventory.equipment,busy,onEquip,onUnequip)}}}
@Composable private fun InventoryRow(item:GameInventoryItem,equipped:Boolean,selected:Boolean,onClick:()->Unit){Row(Modifier.fillMaxWidth().background(if(selected)PixelColors.PanelAlt else PixelColors.Panel).border(1.dp,if(selected)PixelColors.Cyan else PixelColors.Muted).clickable(role=Role.Button,onClick=onClick).padding(8.dp).testTag("inventory-item-${item.id}"),verticalAlignment=Alignment.CenterVertically){PixelUiIcon(PixelUiIconCatalog.inventory(item.id),Modifier.size(18.dp),if(equipped)PixelColors.Gold else PixelColors.Paper);Spacer(Modifier.width(8.dp));Column(Modifier.weight(1f)){Text(item.name,color=PixelColors.Paper);Text(item.type.uppercase(),color=PixelColors.Muted)};Text(if(equipped)"EQUIPPED" else "x${item.quantity}",color=if(equipped)PixelColors.Gold else PixelColors.Cyan)}}
@Composable private fun InventoryDetailPanel(item:GameInventoryItem,equipment:GameEquipmentSlot,busy:Boolean,onEquip:(String)->Unit,onUnequip:(String)->Unit){PixelPanel{Text(item.name,color=PixelColors.Cyan);Text(item.description,color=PixelColors.Paper);if(item.equippable){val e=item.id in equipment.equippedItemIds;PixelTextButton(if(e)"UNEQUIP" else "EQUIP",{if(e)onUnequip(item.id)else onEquip(item.id)},Modifier.testTag("inventory-equip-${item.id}"),!busy)}}}
@Composable private fun CharacterSection(s:GameSnapshot,busy:Boolean,onEquip:(String)->Unit,onUnequip:(String)->Unit){Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()),verticalArrangement=Arrangement.spacedBy(8.dp)){PlayerAvatarPanel(s.identity,s.inventory.equipment,s.conditions,Modifier.fillMaxWidth().height(240.dp));EquipmentPanel(s.inventory.items,s.inventory.equipment,busy,onEquip,onUnequip)}}
@Composable private fun QuestSection(s:GameSnapshot){Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState())){PixelPanel{Text("QUESTS",color=PixelColors.Gold);if(s.quests.isEmpty())Text("NO ACTIVE QUESTS",color=PixelColors.Muted)else s.quests.forEach{Text(it.title,color=PixelColors.Cyan);Text(it.summary,color=PixelColors.Paper)}}}}
@Composable private fun MapSection(s:GameSnapshot,busy:Boolean,onTravel:(String)->Unit){Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState())){PixelPanel{Text("MAP",color=PixelColors.Gold);Text("CURRENT // ${s.location.replace('_',' ')}",color=PixelColors.Cyan);s.map.destinations.forEach{d->PixelTextButton(d.label,{onTravel(d.locationId)},Modifier.testTag("map-destination-${d.locationId}"),!busy&&d.available)}}}}

@Composable private fun SettingsPanel(s:GameSnapshot,onSave:()->Unit,onLoad:()->Unit,onReplayNarration:()->Boolean,onStopNarration:()->Unit,autoRead:Boolean,onAutoReadChange:(Boolean)->Unit,rate:Float,onRateChange:(Float)->Unit,delay:Int,onDelayChange:(Int)->Unit,onCheat:(String)->Unit,onClose:()->Unit){var cheat by remember{mutableStateOf("")};Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()),verticalArrangement=Arrangement.spacedBy(8.dp)){PixelPanel{Text("SETTINGS",color=PixelColors.Gold);Row(horizontalArrangement=Arrangement.spacedBy(6.dp)){PixelTextButton("SAVE",onSave,Modifier.testTag("settings-save"));PixelTextButton("LOAD",onLoad,Modifier.testTag("settings-load"));PixelTextButton("CLOSE",onClose)}};PixelPanel{Text("NARRATION",color=PixelColors.Cyan);PixelTextButton(if(autoRead)"AUTO READ: ON" else "AUTO READ: OFF",{onAutoReadChange(!autoRead)});PixelTextButton("REPLAY",{onReplayNarration()});PixelTextButton("STOP",onStopNarration);Text("RATE ${"%.1f".format(rate)}x",color=PixelColors.Paper);Row{listOf(.8f,1f,1.2f).forEach{PixelTextButton("${it}x",{onRateChange(it)})}};Text("TEXT DELAY ${delay}ms",color=PixelColors.Paper);Row{listOf(0,10,25).forEach{PixelTextButton("${it}ms",{onDelayChange(it)})}}};PixelPanel{Text("DEVELOPER",color=PixelColors.Cyan);OutlinedTextField(cheat,{cheat=it},label={Text("Cheat command")},singleLine=true,modifier=Modifier.fillMaxWidth());PixelTextButton("RUN",{onCheat(cheat);cheat=""},enabled=cheat.isNotBlank());Text("SCENE ${s.sceneId}",color=PixelColors.Muted)}}}
@Composable private fun MorePanel(onCharacter:()->Unit,onSettings:()->Unit){PixelPanel{Text("MORE",color=PixelColors.Gold);PixelTextButton("CHARACTER",onCharacter);PixelTextButton("SETTINGS",onSettings)}}
@Composable private fun BottomPixelNav(active:GameSection,onSelect:(GameSection)->Unit){Row(Modifier.fillMaxWidth().horizontalScroll(rememberScrollState()),horizontalArrangement=Arrangement.spacedBy(4.dp)){GameSection.entries.forEach{PixelNavButton(it.label,it==active){onSelect(it)}}}}
@Composable private fun PixelNavButton(label:String,active:Boolean,onClick:()->Unit){PixelTextButton(label.uppercase(),onClick,Modifier.testTag("nav-${label.lowercase()}"),!active)}
@Composable private fun PixelChoiceCard(choice:com.thegame.rpg.engine.GameChoice,busy:Boolean,onClick:()->Unit){PixelTextButton(choice.text,onClick,Modifier.fillMaxWidth().testTag("choice-${choice.id}"),!busy&&choice.enabled)}
@Composable private fun PixelResourceBar(ratio:Float,fillColor:androidx.compose.ui.graphics.Color,modifier:Modifier=Modifier){Canvas(modifier.height(8.dp).border(1.dp,PixelColors.Muted).background(PixelColors.Deep)){drawRect(fillColor,Offset.Zero,androidx.compose.ui.geometry.Size(size.width*ratio.coerceIn(0f,1f),size.height))}}
private fun formatGameTime(totalMinutes:Int):String{val n=((totalMinutes%(24*60))+(24*60))%(24*60);return "%02d:%02d".format(n/60,n%60)}
