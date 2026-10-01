package com.thegame.rpg.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.BoxWithConstraints
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
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
            PixelPanel(Modifier.fillMaxWidth().testTag("stats-attribute-detail"), selectedName) {
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
        PixelPanel(Modifier.fillMaxWidth(), "Skills") {
            snapshot.skills.groupBy { it.category }.forEach { (category, skills) ->
                Text(category.uppercase(), color = PixelColors.Gold, style = MaterialTheme.typography.labelLarge)
                skills.forEach { skill ->
                    Text(
                        "${skill.name}: ${statValue(skill.effective)}",
                        color = if (skill.modified) PixelColors.Cyan else PixelColors.Paper,
                        style = MaterialTheme.typography.bodyMedium,
                        modifier = Modifier.fillMaxWidth().heightIn(min = 48.dp)
                            .selectable(path == "skills.${skill.id}", enabled = !inspectionBusy, role = Role.Button) {
                                localPath = "skills.${skill.id}"
                                onInspect?.invoke("skills.${skill.id}")
                            }.testTag("skill-row-${skill.id}"),
                    )
                    skill.contributions.forEach { contribution ->
                        Text(
                            "${contribution.label}: ${signedStatValue(contribution.value)}",
                            color = PixelColors.Muted,
                            style = MaterialTheme.typography.labelLarge,
                        )
                    }
                }
                Spacer(Modifier.height(8.dp))
            }
        }
        PixelPanel(Modifier.fillMaxWidth(), "Derived") {
            snapshot.derived.forEach { stat ->
                Text("${stat.name}: ${statValue(stat.value)}", color = PixelColors.Paper, style = MaterialTheme.typography.bodyMedium)
                stat.role?.takeIf { it.isNotBlank() }?.let {
                    Text(it, color = PixelColors.Muted, style = MaterialTheme.typography.labelLarge)
                }
                Spacer(Modifier.height(8.dp))
            }
        }
        if (snapshot.conditions.isNotEmpty()) {
            PixelPanel(Modifier.fillMaxWidth(), "Conditions") {
                snapshot.conditions.forEach { condition ->
                    Text("${condition.name} • Severity ${condition.severity}", color = PixelColors.Danger, style = MaterialTheme.typography.bodyMedium)
                }
            }
        }
    }
}
