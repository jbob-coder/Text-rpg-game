package com.thegame.rpg

import android.app.Application
import android.util.Log
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import com.thegame.rpg.boot.BootState
import com.thegame.rpg.engine.EngineStartException
import com.thegame.rpg.engine.GameEngine
import com.thegame.rpg.engine.GameSnapshot
import com.thegame.rpg.engine.GameStatInspection
import com.thegame.rpg.engine.PythonGameEngine
import com.thegame.rpg.save.ContinueResult
import com.thegame.rpg.save.SaveRepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

data class TravelTransitionUiState(
    val token: Long,
    val fromLocation: String,
    val toLocation: String,
)

data class GameUiState(
    val bootState: BootState = BootState.Starting,
    val snapshot: GameSnapshot? = null,
    val busy: Boolean = false,
    val travelTransition: TravelTransitionUiState? = null,
    val statInspectionPath: String? = null,
    val statInspection: GameStatInspection? = null,
    val statInspectionBusy: Boolean = false,
    val statInspectionError: String? = null,
)

internal fun confirmedTravelTransition(
    fromLocation: String?,
    toLocation: String,
    token: Long,
): TravelTransitionUiState? =
    if (fromLocation == null || fromLocation == toLocation) {
        null
    } else {
        TravelTransitionUiState(
            token = token,
            fromLocation = fromLocation,
            toLocation = toLocation,
        )
    }

class GameViewModel(application: Application) : AndroidViewModel(application) {
    private val engine: GameEngine = PythonGameEngine()
    private val saveRepository = SaveRepository(
        application.filesDir.resolve("saves/slot-0.json"),
        engine,
    )
    private val _uiState = MutableStateFlow(GameUiState())
    val uiState: StateFlow<GameUiState> = _uiState.asStateFlow()
    private var startRequested = false
    private var travelTransitionToken = 0L

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
                onSuccess = { snapshot ->
                    _uiState.update {
                        it.copy(
                            bootState = BootState.Ready,
                            snapshot = snapshot,
                            busy = false,
                            statInspectionPath = null,
                            statInspection = null,
                            statInspectionBusy = false,
                            statInspectionError = null,
                        )
                    }
                },
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
            when (val result = saveRepository.continueGame()) {
                ContinueResult.Missing -> publishFailure(
                    EngineStartException(
                        stageId = "LOAD_ERROR",
                        publicMessage = "No saved game exists yet.",
                        technicalDetail = "Continue requested but saves/slot-0.json does not exist.",
                    )
                )
                is ContinueResult.Failed -> publishFailure(result.error)
                is ContinueResult.Loaded -> _uiState.update {
                    it.copy(
                        bootState = BootState.Ready,
                        snapshot = result.snapshot,
                        busy = false,
                            statInspectionPath = null,
                            statInspection = null,
                            statInspectionBusy = false,
                            statInspectionError = null,
                    )
                }
            }
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
                            statInspectionPath = null,
                            statInspection = null,
                            statInspectionBusy = false,
                            statInspectionError = null,
                        )
                    }
                },
                onFailure = ::publishFailure,
            )
        }
    }

    fun equip(itemId: String) {
        if (_uiState.value.busy) return
        _uiState.update { it.copy(busy = true) }
        viewModelScope.launch {
            engine.equip(itemId).fold(
                onSuccess = { snapshot ->
                    _uiState.update {
                        it.copy(
                            bootState = BootState.Ready,
                            snapshot = snapshot,
                            busy = false,
                            statInspectionPath = null,
                            statInspection = null,
                            statInspectionBusy = false,
                            statInspectionError = null,
                        )
                    }
                },
                onFailure = ::publishFailure,
            )
        }
    }

    fun unequip(slot: String) {
        if (_uiState.value.busy) return
        _uiState.update { it.copy(busy = true) }
        viewModelScope.launch {
            engine.unequip(slot).fold(
                onSuccess = { snapshot ->
                    _uiState.update {
                        it.copy(
                            bootState = BootState.Ready,
                            snapshot = snapshot,
                            busy = false,
                            statInspectionPath = null,
                            statInspection = null,
                            statInspectionBusy = false,
                            statInspectionError = null,
                        )
                    }
                },
                onFailure = ::publishFailure,
            )
        }
    }

    fun travel(locationId: String) {
        if (_uiState.value.busy) return
        val fromLocation = _uiState.value.snapshot?.location
        _uiState.update { it.copy(busy = true, travelTransition = null) }
        viewModelScope.launch {
            engine.travel(locationId).fold(
                onSuccess = { snapshot ->
                    val candidateToken = travelTransitionToken + 1
                    val transition = confirmedTravelTransition(
                        fromLocation = fromLocation,
                        toLocation = snapshot.location,
                        token = candidateToken,
                    )
                    if (transition != null) {
                        travelTransitionToken = candidateToken
                    }
                    _uiState.update {
                        it.copy(
                            bootState = BootState.Ready,
                            snapshot = snapshot,
                            busy = false,
                            statInspectionPath = null,
                            statInspection = null,
                            statInspectionBusy = false,
                            statInspectionError = null,
                            travelTransition = transition,
                        )
                    }
                },
                onFailure = ::publishFailure,
            )
        }
    }

    fun inspectStatus(path: String) {
        if (path.isBlank() || _uiState.value.statInspectionBusy) return
        _uiState.update {
            it.copy(
                statInspectionPath = path,
                statInspection = null,
                statInspectionBusy = true,
                statInspectionError = null,
            )
        }
        viewModelScope.launch {
            engine.inspectStatus(path).fold(
                onSuccess = { inspection ->
                    _uiState.update { current ->
                        if (current.statInspectionPath == path) {
                            current.copy(
                                statInspection = inspection,
                                statInspectionBusy = false,
                                statInspectionError = null,
                            )
                        } else {
                            current
                        }
                    }
                },
                onFailure = { failure ->
                    val engineFailure = failure as? EngineStartException
                        ?: PythonGameEngine.classifyFailure(failure)
                    Log.e("TheGame", engineFailure.technicalDetail, engineFailure)
                    _uiState.update { current ->
                        if (current.statInspectionPath == path) {
                            current.copy(
                                statInspection = null,
                                statInspectionBusy = false,
                                statInspectionError = engineFailure.publicMessage,
                            )
                        } else {
                            current
                        }
                    }
                },
            )
        }
    }

    fun finishTravelTransition(token: Long) {
        _uiState.update { current ->
            if (current.travelTransition?.token == token) {
                current.copy(travelTransition = null)
            } else {
                current
            }
        }
    }

    private fun publishFailure(failure: Throwable) {
        val engineFailure = failure as? EngineStartException ?: PythonGameEngine.classifyFailure(failure)
        Log.e("TheGame", engineFailure.technicalDetail, engineFailure)
        _uiState.update { it.copy(bootState = engineFailure.toBootStateError(), busy = false) }
    }
}
