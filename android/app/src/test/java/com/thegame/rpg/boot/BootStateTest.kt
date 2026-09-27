package com.thegame.rpg.boot

import org.junit.Assert.assertEquals
import org.junit.Test

class BootStateTest {
    @Test
    fun startupPhasesExposeStableStageIds() {
        assertEquals("STARTING", BootState.Starting.stageId)
        assertEquals("PYTHON_STARTING", BootState.PythonStarting.stageId)
        assertEquals("CONTENT_LOADING", BootState.ContentLoading.stageId)
        assertEquals("READY", BootState.Ready.stageId)
    }

    @Test
    fun errorSeparatesPublicAndTechnicalMessages() {
        val error = BootState.Error(
            stageId = "ENGINE_ERROR",
            publicMessage = "The game engine could not start.",
            technicalDetail = "traceback: example"
        )

        assertEquals("ENGINE_ERROR", error.stageId)
        assertEquals("The game engine could not start.", error.publicMessage)
        assertEquals("traceback: example", error.technicalDetail)
    }
}
