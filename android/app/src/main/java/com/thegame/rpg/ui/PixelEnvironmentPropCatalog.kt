package com.thegame.rpg.ui

import androidx.compose.ui.graphics.Color

data class PixelScenePropPlacement(
    val sprite: PixelSprite,
    val x: Int,
    val y: Int,
)

/**
 * Reusable environment props for current named locations.
 *
 * Placement consumes only player-facing location/scene IDs. These props do not decide interaction
 * availability, quest state, or world rules.
 */
object PixelEnvironmentPropCatalog {
    const val ARCHIVE_SHELF_ID = "PROP_ARCHIVE_SHELF"
    const val ARCHIVE_TERMINAL_ID = "PROP_ARCHIVE_TERMINAL"
    const val WORKSHOP_BENCH_ID = "PROP_WORKSHOP_BENCH"
    const val DISTRICT_NOTICE_BOARD_ID = "PROP_DISTRICT_NOTICE_BOARD"
    const val RELAY_WORKBENCH_ID = "PROP_RELAY_WORKBENCH"
    const val GATE_TWELVE_DOOR_ID = "PROP_GATE_TWELVE_DOOR"
    const val TUNNEL_PIPE_SET_ID = "PROP_TUNNEL_PIPE_SET"
    const val TUNNEL_CABLE_SET_ID = "PROP_TUNNEL_CABLE_SET"
    const val TRACE_CHAMBER_APPARATUS_ID = "PROP_TRACE_CHAMBER_APPARATUS"

    private val palette = mapOf(
        'D' to Color(0xFF162129),
        'M' to Color(0xFF48535A),
        'L' to Color(0xFF65737A),
        'S' to Color(0xFF6A5941),
        'C' to PixelColors.Cyan,
        'G' to PixelColors.Gold,
        'P' to PixelColors.Paper,
        'R' to PixelColors.Danger,
    )

    private fun pixels(width: Int, height: Int): MutableList<CharArray> =
        MutableList(height) { CharArray(width) { PixelSprite.TRANSPARENT_PIXEL } }

    private fun shelf(): PixelSprite {
        val width = 32
        val height = 48
        val p = pixels(width, height)

        fun rect(x: Int, y: Int, w: Int, h: Int, key: Char) {
            for (yy in y until y + h) for (xx in x until x + w) {
                if (xx in 0 until width && yy in 0 until height) p[yy][xx] = key
            }
        }

        rect(2, 2, 3, 44, 'M')
        rect(27, 2, 3, 44, 'M')
        rect(4, 2, 24, 3, 'L')
        rect(4, 43, 24, 3, 'L')
        for (y in listOf(10, 18, 26, 34)) {
            rect(4, y, 24, 2, 'M')
        }

        val clusters = listOf(
            Triple(6, 6, 'S'), Triple(14, 6, 'P'), Triple(21, 6, 'S'),
            Triple(7, 13, 'P'), Triple(16, 13, 'S'), Triple(23, 13, 'G'),
            Triple(5, 21, 'S'), Triple(12, 21, 'P'), Triple(20, 21, 'S'),
            Triple(8, 29, 'P'), Triple(17, 29, 'S'), Triple(24, 29, 'P'),
            Triple(6, 37, 'S'), Triple(15, 37, 'G'), Triple(22, 37, 'S'),
        )
        clusters.forEach { (x, y, key) -> rect(x, y, 4, 3, key) }

        return PixelSprite(
            assetId = ARCHIVE_SHELF_ID,
            width = width,
            height = height,
            palette = palette,
            rows = p.map { it.concatToString() },
        )
    }

    private fun terminal(): PixelSprite {
        val width = 32
        val height = 32
        val p = pixels(width, height)

        fun rect(x: Int, y: Int, w: Int, h: Int, key: Char) {
            for (yy in y until y + h) for (xx in x until x + w) {
                if (xx in 0 until width && yy in 0 until height) p[yy][xx] = key
            }
        }

        rect(4, 3, 24, 22, 'M')
        rect(6, 5, 20, 15, 'D')
        rect(8, 7, 16, 10, 'C')
        rect(10, 9, 12, 2, 'P')
        rect(10, 13, 7, 1, 'G')
        rect(12, 25, 8, 3, 'L')
        rect(8, 28, 16, 2, 'M')
        rect(24, 21, 2, 2, 'G')

        return PixelSprite(
            assetId = ARCHIVE_TERMINAL_ID,
            width = width,
            height = height,
            palette = palette,
            rows = p.map { it.concatToString() },
        )
    }

    private fun workshopBench(): PixelSprite {
        val width = 48
        val height = 32
        val p = pixels(width, height)

        fun rect(x: Int, y: Int, w: Int, h: Int, key: Char) {
            for (yy in y until y + h) for (xx in x until x + w) {
                if (xx in 0 until width && yy in 0 until height) p[yy][xx] = key
            }
        }

        rect(3, 11, 42, 5, 'S')
        rect(5, 16, 5, 14, 'M')
        rect(38, 16, 5, 14, 'M')
        rect(9, 20, 29, 3, 'D')
        rect(8, 7, 8, 4, 'C')
        rect(20, 5, 3, 6, 'G')
        rect(27, 8, 12, 3, 'L')
        rect(31, 4, 2, 7, 'R')
        rect(13, 24, 7, 3, 'M')
        rect(27, 24, 8, 3, 'S')

        return PixelSprite(
            assetId = WORKSHOP_BENCH_ID,
            width = width,
            height = height,
            palette = palette,
            rows = p.map { it.concatToString() },
        )
    }

    private fun noticeBoard(): PixelSprite {
        val width = 32
        val height = 48
        val p = pixels(width, height)

        fun rect(x: Int, y: Int, w: Int, h: Int, key: Char) {
            for (yy in y until y + h) for (xx in x until x + w) {
                if (xx in 0 until width && yy in 0 until height) p[yy][xx] = key
            }
        }

        rect(3, 3, 26, 34, 'M')
        rect(5, 5, 22, 30, 'S')
        rect(7, 7, 8, 7, 'P')
        rect(17, 8, 7, 10, 'P')
        rect(8, 18, 15, 6, 'P')
        rect(6, 27, 9, 6, 'P')
        rect(18, 26, 7, 7, 'G')
        rect(7, 9, 8, 1, 'C')
        rect(18, 12, 6, 1, 'R')
        rect(7, 37, 3, 10, 'L')
        rect(22, 37, 3, 10, 'L')

        return PixelSprite(
            assetId = DISTRICT_NOTICE_BOARD_ID,
            width = width,
            height = height,
            palette = palette,
            rows = p.map { it.concatToString() },
        )
    }

    private fun relayWorkbench(): PixelSprite {
        val width = 64
        val height = 32
        val p = pixels(width, height)

        fun rect(x: Int, y: Int, w: Int, h: Int, key: Char) {
            for (yy in y until y + h) for (xx in x until x + w) {
                if (xx in 0 until width && yy in 0 until height) p[yy][xx] = key
            }
        }

        rect(3, 11, 58, 6, 'M')
        rect(6, 17, 6, 13, 'L')
        rect(52, 17, 6, 13, 'L')
        rect(15, 5, 34, 4, 'D')
        rect(20, 6, 8, 2, 'C')
        rect(36, 6, 7, 2, 'G')
        rect(13, 20, 38, 3, 'S')
        rect(26, 17, 12, 4, 'D')

        return PixelSprite(
            assetId = RELAY_WORKBENCH_ID,
            width = width,
            height = height,
            palette = palette,
            rows = p.map { it.concatToString() },
        )
    }

    private fun gateTwelveDoor(): PixelSprite {
        val width = 64
        val height = 48
        val p = pixels(width, height)

        fun rect(x: Int, y: Int, w: Int, h: Int, key: Char) {
            for (yy in y until y + h) for (xx in x until x + w) {
                if (xx in 0 until width && yy in 0 until height) p[yy][xx] = key
            }
        }

        rect(4, 3, 56, 43, 'M')
        rect(9, 7, 46, 39, 'D')
        rect(12, 10, 18, 34, 'L')
        rect(34, 10, 18, 34, 'L')
        rect(31, 8, 2, 36, 'G')
        rect(15, 16, 10, 3, 'C')
        rect(39, 16, 10, 3, 'C')
        rect(14, 35, 12, 4, 'M')
        rect(38, 35, 12, 4, 'M')

        return PixelSprite(
            assetId = GATE_TWELVE_DOOR_ID,
            width = width,
            height = height,
            palette = palette,
            rows = p.map { it.concatToString() },
        )
    }

    private fun tunnelPipeSet(): PixelSprite {
        val width = 32
        val height = 32
        val p = pixels(width, height)

        fun rect(x: Int, y: Int, w: Int, h: Int, key: Char) {
            for (yy in y until y + h) for (xx in x until x + w) {
                if (xx in 0 until width && yy in 0 until height) p[yy][xx] = key
            }
        }

        rect(3, 3, 5, 26, 'M')
        rect(8, 5, 18, 5, 'L')
        rect(24, 8, 5, 20, 'M')
        rect(10, 18, 14, 4, 'L')
        rect(4, 12, 4, 3, 'G')
        rect(24, 14, 5, 3, 'C')
        rect(14, 17, 5, 6, 'D')

        return PixelSprite(
            assetId = TUNNEL_PIPE_SET_ID,
            width = width,
            height = height,
            palette = palette,
            rows = p.map { it.concatToString() },
        )
    }

    private fun tunnelCableSet(): PixelSprite {
        val width = 32
        val height = 32
        val p = pixels(width, height)

        fun rect(x: Int, y: Int, w: Int, h: Int, key: Char) {
            for (yy in y until y + h) for (xx in x until x + w) {
                if (xx in 0 until width && yy in 0 until height) p[yy][xx] = key
            }
        }

        rect(3, 5, 26, 4, 'M')
        rect(5, 10, 22, 2, 'C')
        rect(5, 14, 22, 2, 'G')
        rect(5, 18, 22, 2, 'L')
        rect(8, 21, 4, 8, 'D')
        rect(20, 21, 4, 8, 'D')
        rect(7, 24, 6, 3, 'M')
        rect(19, 24, 6, 3, 'M')

        return PixelSprite(
            assetId = TUNNEL_CABLE_SET_ID,
            width = width,
            height = height,
            palette = palette,
            rows = p.map { it.concatToString() },
        )
    }

    private fun traceChamberApparatus(): PixelSprite {
        val width = 48
        val height = 48
        val p = pixels(width, height)

        fun rect(x: Int, y: Int, w: Int, h: Int, key: Char) {
            for (yy in y until y + h) for (xx in x until x + w) {
                if (xx in 0 until width && yy in 0 until height) p[yy][xx] = key
            }
        }

        rect(19, 4, 10, 40, 'M')
        rect(10, 14, 28, 20, 'D')
        rect(13, 17, 22, 14, 'C')
        rect(16, 20, 16, 8, 'D')
        rect(21, 15, 6, 18, 'G')
        rect(6, 35, 36, 4, 'L')
        rect(10, 39, 6, 7, 'M')
        rect(32, 39, 6, 7, 'M')
        rect(4, 22, 6, 3, 'C')
        rect(38, 22, 6, 3, 'C')

        return PixelSprite(
            assetId = TRACE_CHAMBER_APPARATUS_ID,
            width = width,
            height = height,
            palette = palette,
            rows = p.map { it.concatToString() },
        )
    }

    val archiveShelf: PixelSprite = shelf()
    val archiveTerminal: PixelSprite = terminal()
    val workshopBench: PixelSprite = workshopBench()
    val districtNoticeBoard: PixelSprite = noticeBoard()
    val relayWorkbench: PixelSprite = relayWorkbench()
    val gateTwelveDoor: PixelSprite = gateTwelveDoor()
    val tunnelPipeSet: PixelSprite = tunnelPipeSet()
    val tunnelCableSet: PixelSprite = tunnelCableSet()
    val traceChamberApparatus: PixelSprite = traceChamberApparatus()

    val productionProps: List<PixelSprite> = listOf(
        archiveShelf,
        archiveTerminal,
        workshopBench,
        districtNoticeBoard,
        relayWorkbench,
        gateTwelveDoor,
        tunnelPipeSet,
        tunnelCableSet,
        traceChamberApparatus,
    )

    fun placements(locationId: String, sceneId: String?): List<PixelScenePropPlacement> =
        when (locationId) {
            "RELAY_WORKBENCH" -> listOf(
                PixelScenePropPlacement(relayWorkbench, x = 32, y = 28),
            )

            "GATE_TWELVE" -> listOf(
                PixelScenePropPlacement(gateTwelveDoor, x = 32, y = 9),
            )

            "SERVICE_TUNNEL" -> listOf(
                PixelScenePropPlacement(tunnelPipeSet, x = 5, y = 8),
                PixelScenePropPlacement(tunnelCableSet, x = 48, y = 5),
                PixelScenePropPlacement(tunnelPipeSet, x = 91, y = 8),
            )

            "TRACE_CHAMBER" -> listOf(
                PixelScenePropPlacement(traceChamberApparatus, x = 40, y = 10),
            )

            "DISTRICT_ARCHIVE" -> listOf(
                PixelScenePropPlacement(archiveShelf, x = 7, y = 8),
                PixelScenePropPlacement(archiveShelf, x = 89, y = 8),
                PixelScenePropPlacement(archiveTerminal, x = 48, y = 20),
            )

            "WORKSHOP_ROW" -> listOf(
                PixelScenePropPlacement(workshopBench, x = 40, y = 27),
            )

            "DISTRICT_PLAZA" ->
                if (sceneId == "DISTRICT_HUB") {
                    listOf(PixelScenePropPlacement(districtNoticeBoard, x = 88, y = 9))
                } else {
                    emptyList()
                }

            else -> emptyList()
        }
}
