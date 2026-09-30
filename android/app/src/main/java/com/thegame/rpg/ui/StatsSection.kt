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

@Composable
internal fun StatsSection(snapshot: GameSnapshot) {
    var selectedId by rememberSaveable { mutableStateOf<String?>(null) }
    val selected = snapshot.attributes.firstOrNull { it.id == selectedId }
        ?: snapshot.attributes.firstOrNull()

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
                                    .selectable(active, role = Role.Button) { selectedId = stat.id }
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
        if (selected != null) {
            PixelPanel(Modifier.fillMaxWidth().testTag("stats-attribute-detail"), selected.name) {
                Text(
                    "Effective ${statValue(selected.effective)} • Base ${statValue(selected.base)}",
                    color = PixelColors.Paper,
                    style = MaterialTheme.typography.titleLarge,
                )
                selected.role?.takeIf { it.isNotBlank() }?.let {
                    Spacer(Modifier.height(8.dp))
                    Text(it, color = PixelColors.Muted, style = MaterialTheme.typography.bodyMedium)
                }
                Spacer(Modifier.height(8.dp))
                Text("CONTRIBUTIONS", color = PixelColors.Gold, style = MaterialTheme.typography.labelLarge)
                if (selected.contributions.isEmpty()) {
                    Text("No listed modifiers.", color = PixelColors.Muted, style = MaterialTheme.typography.bodyMedium)
                } else {
                    selected.contributions.forEach { contribution ->
                        Text(
                            "${contribution.label}: ${signedStatValue(contribution.value)}",
                            color = if (contribution.value < 0) PixelColors.Danger else PixelColors.Cyan,
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
