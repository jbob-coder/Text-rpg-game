package com.thegame.rpg.boot

sealed interface BootState {
    val stageId: String

    data object Starting : BootState {
        override val stageId: String = "STARTING"
    }

    data object PythonStarting : BootState {
        override val stageId: String = "PYTHON_STARTING"
    }

    data object ContentLoading : BootState {
        override val stageId: String = "CONTENT_LOADING"
    }

    data object Ready : BootState {
        override val stageId: String = "READY"
    }

    data class Error(
        override val stageId: String,
        val publicMessage: String,
        val technicalDetail: String,
    ) : BootState
}
