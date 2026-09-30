package com.thegame.rpg.ui

import androidx.compose.ui.graphics.Color

/**
 * Source-native map markers for the player-safe world-map projection.
 *
 * The neutral discovered marker is drawn first. A current/reachable/unavailable overlay is
 * then selected from GameMapNode.current/reachable. The player marker is drawn only for the
 * current node. These sprites never determine travel or discovery state.
 */
object PixelMapMarkerCatalog {
    const val PLAYER_MARKER_ID = "MAP_PLAYER_MARKER"
    const val DISCOVERED_MARKER_ID = "MAP_NODE_DISCOVERED"
    const val CURRENT_MARKER_ID = "MAP_NODE_CURRENT"
    const val REACHABLE_MARKER_ID = "MAP_NODE_REACHABLE"
    const val UNAVAILABLE_MARKER_ID = "MAP_NODE_UNAVAILABLE"

    private val palette = mapOf(
        'M' to PixelColors.Muted,
        'C' to PixelColors.Cyan,
        'G' to PixelColors.Gold,
        'P' to PixelColors.Paper,
        'R' to PixelColors.Danger,
    )

    val playerMarker = PixelSprite(
        assetId = PLAYER_MARKER_ID,
        width = 16,
        height = 16,
        palette = palette,
        rows = listOf(
        "................",
        "................",
        "................",
        ".......P........",
        "......PPP.......",
        ".....PPPPP......",
        "......GGG.......",
        ".......G........",
        ".......G........",
        ".......G........",
        "................",
        "................",
        "................",
        "................",
        "................",
        "................"
        ),
    )

    val discoveredMarker = PixelSprite(
        assetId = DISCOVERED_MARKER_ID,
        width = 16,
        height = 16,
        palette = palette,
        rows = listOf(
        "................",
        "................",
        ".......C........",
        "......M.M.......",
        ".....M...M......",
        "....M.....M.....",
        "...M.......M....",
        "..C....M....C...",
        "...M.......M....",
        "....M.....M.....",
        ".....M...M......",
        "......M.M.......",
        ".......C........",
        "................",
        "................",
        "................"
        ),
    )

    val currentMarker = PixelSprite(
        assetId = CURRENT_MARKER_ID,
        width = 16,
        height = 16,
        palette = palette,
        rows = listOf(
        "................",
        "................",
        ".......G........",
        ".......G........",
        "................",
        ".......P........",
        "......GGG.......",
        "..GG.PGGGP.GG...",
        "......GGG.......",
        ".......P........",
        "................",
        ".......G........",
        ".......G........",
        "................",
        "................",
        "................"
        ),
    )

    val reachableMarker = PixelSprite(
        assetId = REACHABLE_MARKER_ID,
        width = 16,
        height = 16,
        palette = palette,
        rows = listOf(
        "................",
        "................",
        "................",
        ".......C........",
        "......C.C.......",
        ".......G........",
        "....C.....C.....",
        "...C.G.G.G.C....",
        "....C.....C.....",
        ".......G........",
        "......C.C.......",
        ".......C........",
        "................",
        "................",
        "................",
        "................"
        ),
    )

    val unavailableMarker = PixelSprite(
        assetId = UNAVAILABLE_MARKER_ID,
        width = 16,
        height = 16,
        palette = palette,
        rows = listOf(
        "................",
        "................",
        "................",
        "................",
        "....M.....M.....",
        ".....M...M......",
        "......M.M.......",
        ".......R........",
        "......M.M.......",
        ".....M...M......",
        "....M.....M.....",
        "................",
        "................",
        "................",
        "................",
        "................"
        ),
    )

    val productionMarkers: List<PixelSprite> = listOf(
        playerMarker,
        discoveredMarker,
        currentMarker,
        reachableMarker,
        unavailableMarker,
    )

    fun stateOverlay(current: Boolean, reachable: Boolean): PixelSprite =
        when {
            current -> currentMarker
            reachable -> reachableMarker
            else -> unavailableMarker
        }
}
