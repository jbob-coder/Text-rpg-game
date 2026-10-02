package com.thegame.rpg.audio

import android.content.Context
import android.speech.tts.TextToSpeech
import java.util.Locale

class NarrationController(
    context: Context,
) : TextToSpeech.OnInitListener {
    private val tts = TextToSpeech(context.applicationContext, this)
    @Volatile
    private var ready = false
    @Volatile
    private var speechRate = 0.92f
    @Volatile
    private var lastText = ""

    override fun onInit(status: Int) {
        if (status != TextToSpeech.SUCCESS) {
            ready = false
            return
        }

        val embeddedVoice = tts.voices
            ?.filter { !it.isNetworkConnectionRequired }
            ?.firstOrNull { it.locale.language == Locale.US.language }
            ?: tts.voices?.firstOrNull { !it.isNetworkConnectionRequired }

        if (embeddedVoice != null) {
            tts.voice = embeddedVoice
        } else {
            tts.language = Locale.US
        }

        tts.setSpeechRate(speechRate)
        tts.setPitch(1.0f)
        ready = true
    }

    fun speak(text: String): Boolean {
        val clean = text.trim()
        if (!ready || clean.isEmpty()) return false
        lastText = clean
        val result = tts.speak(
            clean,
            TextToSpeech.QUEUE_FLUSH,
            null,
            "the-game-narration",
        )
        return result == TextToSpeech.SUCCESS
    }

    fun replay(): Boolean {
        val previous = lastText
        if (previous.isBlank()) return false
        return speak(previous)
    }

    fun setSpeechRate(rate: Float): Float {
        val applied = rate.coerceIn(0.5f, 1.5f)
        speechRate = applied
        if (ready) {
            tts.setSpeechRate(applied)
        }
        return applied
    }

    fun stop() {
        tts.stop()
    }

    fun shutdown() {
        ready = false
        tts.stop()
        tts.shutdown()
    }
}
