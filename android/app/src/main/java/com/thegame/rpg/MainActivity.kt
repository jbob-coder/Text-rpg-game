package com.thegame.rpg

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.foundation.layout.Arrangement
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
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.thegame.rpg.boot.BootState
import com.thegame.rpg.engine.GameSnapshot

class MainActivity : ComponentActivity() {
    private val gameViewModel: GameViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                val uiState by gameViewModel.uiState.collectAsState()
                LaunchedEffect(Unit) {
                    gameViewModel.startIfNeeded()
                }
                GameRoot(
                    uiState = uiState,
                    onChoice = gameViewModel::choose,
                )
            }
        }
    }
}

@Composable
private fun GameRoot(
    uiState: GameUiState,
    onChoice: (String) -> Unit,
) {
    val snapshot = uiState.snapshot
    if (uiState.bootState == BootState.Ready && snapshot != null) {
        ReadyScreen(snapshot = snapshot, busy = uiState.busy, onChoice = onChoice)
    } else {
        BootScreen(uiState.bootState)
    }
}

@Composable
private fun BootScreen(state: BootState) {
    Surface(modifier = Modifier.fillMaxSize()) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(24.dp),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally,
        ) {
            Text(text = "THE GAME", style = MaterialTheme.typography.headlineMedium)
            Spacer(modifier = Modifier.height(12.dp))
            Text(text = state.stageId)
            if (state is BootState.Error) {
                Spacer(modifier = Modifier.height(12.dp))
                Text(text = state.publicMessage)
            }
        }
    }
}

@Composable
private fun ReadyScreen(
    snapshot: GameSnapshot,
    busy: Boolean,
    onChoice: (String) -> Unit,
) {
    Surface(modifier = Modifier.fillMaxSize()) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .verticalScroll(rememberScrollState())
                .padding(20.dp),
        ) {
            Text(text = snapshot.title, style = MaterialTheme.typography.headlineSmall)
            Text(text = snapshot.location, style = MaterialTheme.typography.labelMedium)
            Spacer(modifier = Modifier.height(16.dp))
            Text(text = snapshot.body, style = MaterialTheme.typography.bodyLarge)
            Spacer(modifier = Modifier.height(20.dp))

            snapshot.resources.forEach { resource ->
                Text(text = "${resource.id.uppercase()}: ${resource.current.toInt()} / ${resource.max.toInt()}")
            }

            Spacer(modifier = Modifier.height(20.dp))
            snapshot.choices.forEach { choice ->
                Button(
                    onClick = { onChoice(choice.id) },
                    enabled = choice.enabled && !busy,
                    modifier = Modifier.fillMaxWidth(),
                ) {
                    Text(choice.text)
                }
                if (!choice.enabled && choice.disabledReason != null) {
                    Text(
                        text = choice.disabledReason,
                        style = MaterialTheme.typography.bodySmall,
                    )
                }
                Spacer(modifier = Modifier.height(8.dp))
            }

            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
            ) {
                Text("TURN ${snapshot.turn}")
                Text("TIME ${snapshot.timeMinutes}m")
            }
        }
    }
}
