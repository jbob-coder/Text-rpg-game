package com.thegame.rpg.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.unit.dp
import com.thegame.rpg.TravelTransitionUiState
import kotlinx.coroutines.delay

/**
 * Text-only travel notice after an authoritative successful Python travel.
 * No pixel-art sprite, animation frames or additional game-state decisions.
 */
@Composable
fun MapTravelTransitionOverlay(
    transition: TravelTransitionUiState,
    onFinished: (Long) -> Unit,
    modifier: Modifier = Modifier,
) {
    LaunchedEffect(transition.token) {
        delay(150L)
        onFinished(transition.token)
    }

    Box(
        modifier = modifier
            .fillMaxSize()
            .background(PixelColors.Ink)
            .testTag("map-travel-transition"),
        contentAlignment = Alignment.Center,
    ) {
        Column(
            modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.spacedBy(10.dp),
        ) {
            Text("TRAVEL", color = PixelColors.Gold,
                style = MaterialTheme.typography.titleLarge)
            Spacer(Modifier.height(4.dp))
            Text(
                text = "${displayLocation(transition.fromLocation)} → ${displayLocation(transition.toLocation)}",
                color = PixelColors.Paper,
                style = MaterialTheme.typography.bodyLarge,
                modifier = Modifier.testTag("map-travel-transition-route"),
            )
        }
    }
}

private fun displayLocation(locationId: String): String =
    locationId.replace('_', ' ').uppercase()
