package com.thegame.rpg

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
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
            TheGamePixelTheme {
                val uiState by gameViewModel.uiState.collectAsState()
                LaunchedEffect(Unit) { gameViewModel.startIfNeeded() }

                TheGameRoot(
                    uiState = uiState,
                    onChoice = gameViewModel::choose,
                    onSave = gameViewModel::save,
                    onLoad = gameViewModel::load,
                    onNarrate = narration::speak,
                    onStopNarration = narration::stop,
                    onCheat = gameViewModel::applyCheat,
                    onEquip = gameViewModel::equip,
                    onUnequip = gameViewModel::unequip,
                    onTravel = gameViewModel::travel,
                )
            }
        }
    }

    override fun onDestroy() {
        narration.shutdown()
        super.onDestroy()
    }
}
