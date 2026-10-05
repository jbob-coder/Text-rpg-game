package com.thegame.rpg.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
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
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.unit.dp
import com.thegame.rpg.engine.GameSnapshot
import com.thegame.rpg.engine.GameStatInspection

@Composable
internal fun StatsSection(
    snapshot: GameSnapshot,
    selectedPath: String? = null,
    inspection: GameStatInspection? = null,
    inspectionBusy: Boolean = false,
    inspectionError: String? = null,
    onInspect: ((String) -> Unit)? = null,
) {
    var localPath by rememberSaveable { mutableStateOf<String?>(null) }
    val path = selectedPath ?: localPath ?: snapshot.attributes.firstOrNull()?.let { "attributes.${it.id}" }
    val selected = snapshot.attributes.firstOrNull { "attributes.${it.id}" == path }
    val selectedSkill = snapshot.skills.firstOrNull { "skills.${it.id}" == path }
    val selectedName = selected?.name ?: selectedSkill?.name
    val selectedBase = selected?.base ?: selectedSkill?.base
    val selectedEffective = selected?.effective ?: selectedSkill?.effective
    val matchingInspection = inspection?.takeIf { it.path == path }

    Column(
        Modifier.fillMaxSize().verticalScroll(rememberScrollState()).testTag("stats-scroll"),
        verticalArrangement = Arrangement.spacedBy(8.dp),
    ) {
        PlayerStatusSummary(snapshot)
        StatusResourceGrid(snapshot)
        Text("CORE ATTRIBUTES", color = PixelColors.Gold, style = MaterialTheme.typography.titleLarge)
        BoxWithConstraints(Modifier.fillMaxWidth()) {
            val columns = if (maxWidth < 300.dp || LocalDensity.current.fontScale > 1.4f) 1 else 2
            Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                snapshot.attributes.chunked(columns).forEach { group ->
                    Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                        group.forEach { stat ->
                            val active = selected?.id == stat.id
                            Column(
                                Modifier.weight(1f)
                                    .background(if (active) PixelColors.PanelAlt else PixelColors.Panel)
                                    .border(2.dp, if (active) PixelColors.Gold else PixelColors.Muted)
                                    .selectable(active, enabled = !inspectionBusy, role = Role.Button) {
                                        localPath = "attributes.${stat.id}"
                                        onInspect?.invoke("attributes.${stat.id}")
                                    }
                                    .heightIn(min = 72.dp)
                                    .padding(10.dp)
                                    .testTag("stats-attribute-${stat.id}"),
                            ) {
                                Text(stat.name, color = PixelColors.Paper, style = MaterialTheme.typography.bodyMedium)
                                Text(
                                    statValue(stat.effective),
                                    color = if (stat.modified) PixelColors.Cyan else PixelColors.Paper,
                                    style = MaterialTheme.typography.headlineMedium,
                                )
                                if (stat.contributions.isNotEmpty()) {
                                    Text(
                                        "Base ${statValue(stat.base)} • ${signedStatValue(stat.delta)} net",
                                        color = PixelColors.Muted,
                                        style = MaterialTheme.typography.labelLarge,
                                    )
                                }
                            }
                        }
                        if (group.size < columns) Spacer(Modifier.weight(1f))
                    }
                }
            }
        }
        if (selectedName != null && selectedBase != null && selectedEffective != null) {
            PixelPanel(
                Modifier.fillMaxWidth().testTag("stats-attribute-detail"),
                selectedName,
                chrome = PixelPanelChrome.STATS,
            ) {
                Text(
                    "Effective ${statValue(matchingInspection?.total ?: selectedEffective)} • Base ${statValue(selectedBase)}",
                    color = PixelColors.Paper,
                    style = MaterialTheme.typography.titleLarge,
                )
                selected?.role?.takeIf { it.isNotBlank() }?.let {
                    Spacer(Modifier.height(8.dp))
                    Text(it, color = PixelColors.Muted, style = MaterialTheme.typography.bodyMedium)
                }
                Spacer(Modifier.height(8.dp))
                Text("CONTRIBUTIONS", color = PixelColors.Gold, style = MaterialTheme.typography.labelLarge)
                val contributions = if (matchingInspection != null) {
                    matchingInspection.contributions
                        .filter { it.source !in setOf("base", "total") && it.value != 0.0 }
                        .map { contribution ->
                            val source = contribution.source
                            val label = when {
                                source == "unidentified_modifier" -> "Unidentified modifier"
                                source.startsWith("equipment:") -> {
                                    val slot = source.substringAfter(':')
                                    snapshot.inventory.equipment.firstOrNull { it.slot == slot && it.equipped }?.name
                                        ?: equipmentSlotLabel(slot)
                                }
                                source.startsWith("condition:") -> snapshot.conditions.firstOrNull { it.id == source.substringAfter(':') }?.name ?: "Condition"
                                source.startsWith("perk:") -> source.substringAfter(':').removePrefix("PERK_").lowercase().replace('_', ' ').replaceFirstChar { it.uppercase() }
                                source.startsWith("set:") -> "Equipment set bonus"
                                else -> "Modifier"
                            }
                            label to contribution.value
                        }
                } else {
                    (selected?.contributions ?: selectedSkill?.contributions ?: emptyList()).map { it.label to it.value }
                }
                if (inspectionBusy) {
                    Text("Loading detail…", color = PixelColors.Muted, style = MaterialTheme.typography.bodyMedium)
                } else if (inspectionError != null) {
                    Text(inspectionError, color = PixelColors.Danger, style = MaterialTheme.typography.bodyMedium)
                } else if (contributions.isEmpty()) {
                    Text("No listed modifiers.", color = PixelColors.Muted, style = MaterialTheme.typography.bodyMedium)
                } else {
                    contributions.forEach { (label, value) ->
                        Text(
                            "$label: ${signedStatValue(value)}",
                            color = if (value < 0) PixelColors.Danger else PixelColors.Cyan,
                            style = MaterialTheme.typography.bodyMedium,
                        )
                    }
                }
            }
        }
        SkillsMatrix(
            snapshot = snapshot,
            selectedPath = path,
            inspectionBusy = inspectionBusy,
            onSelect = { skillPath ->
                localPath = skillPath
                onInspect?.invoke(skillPath)
            },
        )
        if (snapshot.abilities.isNotEmpty()) {
            PixelPanel(
                Modifier.fillMaxWidth().testTag("abilities-panel"),
                "Abilities",
                chrome = PixelPanelChrome.STATS,
            ) {
                snapshot.abilities.forEach { ability ->
                    Column(
                        Modifier
                            .fillMaxWidth()
                            .testTag("ability-${ability.id}"),
                    ) {
                        Text(
                            ability.name,
                            color = PixelColors.Paper,
                            style = MaterialTheme.typography.titleLarge,
                        )
                        Text(
                            "Rank ${ability.rank} • ${ability.masteryStage} • ${statValue(ability.masteryXp)} mastery",
                            color = PixelColors.Muted,
                            style = MaterialTheme.typography.bodyMedium,
                        )
                        ability.resource?.let { resource ->
                            val max = resource.max?.let { "/${statValue(it)}" } ?: ""
                            Text(
                                "${resource.label}: ${statValue(resource.current)}$max",
                                color = PixelColors.Cyan,
                                style = MaterialTheme.typography.bodyMedium,
                            )
                        }
                        ability.techniques.forEach { technique ->
                            Text(
                                "${technique.name}: ${technique.stage} • ${statValue(technique.masteryXp)} mastery",
                                color = PixelColors.Paper,
                                style = MaterialTheme.typography.bodyMedium,
                                modifier = Modifier.testTag("ability-${ability.id}-technique-${technique.id}"),
                            )
                        }
                    }
                    Spacer(Modifier.height(8.dp))
                }
            }
        }
        PixelPanel(
            Modifier.fillMaxWidth(),
            "Derived",
            chrome = PixelPanelChrome.STATS,
        ) {
            snapshot.derived.forEach { stat ->
                Text("${stat.name}: ${statValue(stat.value)}", color = PixelColors.Paper, style = MaterialTheme.typography.bodyMedium)
                stat.role?.takeIf { it.isNotBlank() }?.let {
                    Text(it, color = PixelColors.Muted, style = MaterialTheme.typography.labelLarge)
                }
                Spacer(Modifier.height(8.dp))
            }
        }
        if (snapshot.conditions.isNotEmpty()) {
            PixelPanel(
                Modifier.fillMaxWidth(),
                "Conditions",
                chrome = PixelPanelChrome.STATS,
            ) {
                snapshot.conditions.forEach { condition ->
                    Text("${condition.name} • Severity ${condition.severity}", color = PixelColors.Danger, style = MaterialTheme.typography.bodyMedium)
                }
            }
        }
    }
}


@Composable
private fun SkillsMatrix(
    snapshot: GameSnapshot,
    selectedPath: String?,
    inspectionBusy: Boolean,
    onSelect: (String) -> Unit,
) {
    PixelPanel(
        Modifier.fillMaxWidth().testTag("skills-matrix"),
        "Skills",
        chrome = PixelPanelChrome.STATS,
    ) {
        if (snapshot.skills.isEmpty()) {
            Text(
                "No player-facing skills are available.",
                color = PixelColors.Muted,
                style = MaterialTheme.typography.bodyMedium,
            )
            return@PixelPanel
        }

        snapshot.skills.groupBy { it.category }.forEach { (category, skills) ->
            val categoryColor = when (category.lowercase()) {
                "combat" -> PixelColors.Health
                "physical" -> PixelColors.Stamina
                "technical" -> PixelColors.Focus
                "social" -> PixelColors.Resolve
                "knowledge" -> PixelColors.Gold
                else -> PixelColors.Paper
            }

            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .background(PixelColors.Deep)
                    .border(1.dp, categoryColor)
                    .padding(horizontal = 8.dp, vertical = 6.dp)
                    .testTag("skills-category-${category.lowercase()}"),
            ) {
                Text(
                    "[${category.uppercase()}]",
                    color = categoryColor,
                    style = MaterialTheme.typography.labelLarge,
                    modifier = Modifier.weight(1f),
                )
                Text(
                    "${skills.size} SKILLS",
                    color = PixelColors.Muted,
                    style = MaterialTheme.typography.labelLarge,
                )
            }
            Spacer(Modifier.height(6.dp))

            BoxWithConstraints(Modifier.fillMaxWidth()) {
                val columns = if (maxWidth < 300.dp || LocalDensity.current.fontScale > 1.4f) 1 else 2
                Column(verticalArrangement = Arrangement.spacedBy(6.dp)) {
                    skills.chunked(columns).forEach { group ->
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.spacedBy(6.dp),
                        ) {
                            group.forEach { skill ->
                                val skillPath = "skills.${skill.id}"
                                val active = selectedPath == skillPath
                                val progress = (skill.effective / 100.0)
                                    .coerceIn(0.0, 1.0)
                                    .toFloat()

                                Column(
                                    modifier = Modifier
                                        .weight(1f)
                                        .background(if (active) PixelColors.PanelAlt else PixelColors.Panel)
                                        .border(
                                            2.dp,
                                            when {
                                                active -> PixelColors.Gold
                                                skill.modified -> categoryColor
                                                else -> PixelColors.Muted
                                            },
                                        )
                                        .selectable(
                                            selected = active,
                                            enabled = !inspectionBusy,
                                            role = Role.Button,
                                        ) {
                                            onSelect(skillPath)
                                        }
                                        .heightIn(min = 96.dp)
                                        .padding(8.dp)
                                        .testTag("skill-row-${skill.id}"),
                                ) {
                                    Text(
                                        skill.name,
                                        color = PixelColors.Paper,
                                        style = MaterialTheme.typography.bodyMedium,
                                    )
                                    Text(
                                        statValue(skill.effective),
                                        color = if (skill.modified) categoryColor else PixelColors.Paper,
                                        style = MaterialTheme.typography.titleLarge,
                                    )
                                    Box(
                                        modifier = Modifier
                                            .fillMaxWidth()
                                            .height(6.dp)
                                            .background(PixelColors.Ink)
                                            .border(1.dp, PixelColors.Muted),
                                    ) {
                                        Box(
                                            modifier = Modifier
                                                .fillMaxHeight()
                                                .fillMaxWidth(progress)
                                                .background(categoryColor),
                                        )
                                    }
                                    Spacer(Modifier.height(4.dp))
                                    Text(
                                        if (skill.modified) {
                                            "BASE ${statValue(skill.base)}  ${signedStatValue(skill.delta)}"
                                        } else {
                                            "BASE ${statValue(skill.base)}"
                                        },
                                        color = PixelColors.Muted,
                                        style = MaterialTheme.typography.labelLarge,
                                    )
                                }
                            }
                            if (group.size < columns) Spacer(Modifier.weight(1f))
                        }
                    }
                }
            }

            Spacer(Modifier.height(10.dp))
        }
    }
}
