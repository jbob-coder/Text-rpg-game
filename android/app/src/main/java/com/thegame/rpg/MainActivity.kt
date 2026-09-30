package com.thegame.rpg

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.compose.runtime.saveable.rememberSaveable
import com.thegame.rpg.audio.NarrationController
import com.thegame.rpg.ui.TheGamePixelTheme
import com.thegame.rpg.ui.TheGameRoot

class MainActivity : ComponentActivity() {
    private val gameViewModel: GameViewModel by viewModels()
    private lateinit var narration: NarrationController

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        narration = NarrationController(this)

        setContent {
            var autoReadNarration by rememberSaveable { mutableStateOf(false) }
            var narrationRate by rememberSaveable { mutableStateOf(0.92f) }
            var textDelayMs by rememberSaveable { mutableStateOf(0) }

            TheGamePixelTheme {
                val uiState by gameViewModel.uiState.collectAsState()
                LaunchedEffect(Unit) { gameViewModel.startIfNeeded() }

                TheGameRoot(
                    uiState = uiState,
                    onChoice = gameViewModel::choose,
                    onSave = gameViewModel::save,
                    onLoad = gameViewModel::load,
                    onNarrate = narration::speak,
                    onReplayNarration = narration::replay,
                    onStopNarration = narration::stop,
                    autoReadNarration = autoReadNarration,
                    onAutoReadChange = { autoReadNarration = it },
                    narrationRate = narrationRate,
                    onNarrationRateChange = {
                        narrationRate = narration.setSpeechRate(it)
                    },
                    textDelayMs = textDelayMs,
                    onTextDelayChange = { textDelayMs = it },
                    onCheat = gameViewModel::applyCheat,
                    onEquip = gameViewModel::equip,
                    onUnequip = gameViewModel::unequip,
                    onInspectStatus = gameViewModel::inspectStatus,
                    onTravel = gameViewModel::travel,
                    onTravelTransitionFinished = gameViewModel::finishTravelTransition,
                )
            }
        }
    }

    override fun onDestroy() {
        narration.shutdown()
        super.onDestroy()
    }
}
