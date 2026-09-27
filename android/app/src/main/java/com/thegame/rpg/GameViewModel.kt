package com.thegame.rpg

import android.app.Application
import android.util.Log
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import com.thegame.rpg.boot.BootState
import com.thegame.rpg.engine.EngineStartException
import com.thegame.rpg.engine.GameEngine
import com.thegame.rpg.engine.GameSnapshot
import com.thegame.rpg.engine.PythonGameEngine
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

data class GameUiState(
    val bootState: BootState = BootState.Starting,
    val snapshot: GameSnapshot? = null,
    val busy: Boolean = false,
)

class GameViewModel(application: Application) : AndroidViewModel(application) {
    private val engine: GameEngine = PythonGameEngine()
    private val _uiState = MutableStateFlow(GameUiState())
    val uiState: StateFlow<GameUiState> = _uiState.asStateFlow()
    private var startRequested = false

    fun startIfNeeded() {
        if (startRequested) return
        startRequested = true
        _uiState.update { it.copy(busy = true) }
        viewModelScope.launch {
            engine.start(getApplication()) { stage ->
                _uiState.update { current -> current.copy(bootState = stage, busy = true) }
            }.fold(
                onSuccess = { snapshot ->
                    _uiState.value = GameUiState(BootState.Ready, snapshot, false)
                },
                onFailure = ::publishFailure,
            )
        }
    }

    fun choose(choiceId: String) {
        if (_uiState.value.busy) return
        _uiState.update { it.copy(busy = true) }
        viewModelScope.launch {
            engine.choose(choiceId).fold(
                onSuccess = { snapshot -> _uiState.update { it.copy(bootState = BootState.Ready, snapshot = snapshot, busy = false) } },
                onFailure = ::publishFailure,
            )
        }
    }

    fun save() {
        if (_uiState.value.busy) return
        _uiState.update { it.copy(busy = true) }
        viewModelScope.launch {
            engine.save().fold(
                onSuccess = { _uiState.update { it.copy(busy = false) } },
                onFailure = ::publishFailure,
            )
        }
    }

    fun load() {
        if (_uiState.value.busy) return
        _uiState.update { it.copy(busy = true) }
        viewModelScope.launch {
            engine.load().fold(
                onSuccess = { snapshot -> _uiState.update { it.copy(bootState = BootState.Ready, snapshot = snapshot, busy = false) } },
                onFailure = ::publishFailure,
            )
        }
    }

    fun applyCheat(code: String) {
        if (_uiState.value.busy) return
        _uiState.update { it.copy(busy = true) }
        viewModelScope.launch {
            engine.applyCheat(code).fold(
                onSuccess = { snapshot ->
                    _uiState.update {
                        it.copy(
                            bootState = BootState.Ready,
                            snapshot = snapshot,
                            busy = false,
                        )
                    }
                },
                onFailure = ::publishFailure,
            )
        }
    }

    private fun publishFailure(failure: Throwable) {
        val engineFailure = failure as? EngineStartException ?: PythonGameEngine.classifyFailure(failure)
        Log.e("TheGame", engineFailure.technicalDetail, engineFailure)
        _uiState.update { it.copy(bootState = engineFailure.toBootStateError(), busy = false) }
    }
}
