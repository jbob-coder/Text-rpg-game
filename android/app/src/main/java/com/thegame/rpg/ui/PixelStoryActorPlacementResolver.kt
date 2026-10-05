package com.thegame.rpg.ui

/**
 * Resolves player-safe semantic room placement keys into presentation coordinates.
 *
 * Presence is intentionally not decided here. The authoritative room projection decides
 * which actors exist; this resolver only translates an already-projected placement key.
 */
data class PixelStoryActorStagePoint(
    val x: Int,
    val y: Int,
)

object PixelStoryActorPlacementResolver {
    const val PLATFORM_NINE_COURIER_LEFT = "PLATFORM_NINE_COURIER_LEFT"
    const val PLATFORM_NINE_TAMSIN_RIGHT = "PLATFORM_NINE_TAMSIN_RIGHT"
    const val RELAY_WORKBENCH_TAMSIN_RIGHT = "RELAY_WORKBENCH_TAMSIN_RIGHT"
    const val SERVICE_TUNNEL_TAMSIN_RIGHT = "SERVICE_TUNNEL_TAMSIN_RIGHT"

    private val points = mapOf(
        PLATFORM_NINE_COURIER_LEFT to PixelStoryActorStagePoint(x = 34, y = 13),
        PLATFORM_NINE_TAMSIN_RIGHT to PixelStoryActorStagePoint(x = 62, y = 14),
        RELAY_WORKBENCH_TAMSIN_RIGHT to PixelStoryActorStagePoint(x = 90, y = 14),
        SERVICE_TUNNEL_TAMSIN_RIGHT to PixelStoryActorStagePoint(x = 76, y = 14),
    )

    fun resolve(placementKey: String): PixelStoryActorStagePoint? = points[placementKey]
}
