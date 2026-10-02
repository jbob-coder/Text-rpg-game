package com.thegame.rpg.ui

import androidx.compose.ui.graphics.Color

data class PixelEnvironmentTileAtlas(
    val assetId: String,
    val tiles: List<PixelSprite>,
)

/**
 * Reusable district/depot environment modules.
 *
 * These assets are presentation infrastructure only. They never decide travel, access,
 * interaction, quest, or hazard state.
 */
object PixelEnvironmentModuleCatalog {
    const val DEPOT_FACADE_EXTERIOR_ID = "DEPOT_FACADE_EXTERIOR"
    const val MAINTENANCE_CORRIDOR_CONNECTOR_ID = "MAINTENANCE_CORRIDOR_CONNECTOR"
    const val MUNICIPAL_ARCHIVE_EXTERIOR_ID = "MUNICIPAL_ARCHIVE_EXTERIOR"
    const val MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS_ID = "MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS"

    private val palette = mapOf(
        'B' to Color(0xFF111A20),
        'D' to Color(0xFF162129),
        'A' to Color(0xFF303E45),
        'M' to Color(0xFF48535A),
        'L' to Color(0xFF65737A),
        'S' to Color(0xFF6A5941),
        'C' to PixelColors.Cyan,
        'G' to PixelColors.Gold,
        'R' to PixelColors.Danger,
        'P' to PixelColors.Paper,
    )

    private fun pixels(width: Int, height: Int): MutableList<CharArray> =
        MutableList(height) { CharArray(width) { PixelSprite.TRANSPARENT_PIXEL } }

    private fun module(
        assetId: String,
        draw: ((Int, Int, Int, Int, Char) -> Unit) -> Unit,
    ): PixelSprite {
        val width = 128
        val height = 64
        val p = pixels(width, height)
        val rect: (Int, Int, Int, Int, Char) -> Unit = { x, y, w, h, key ->
            for (yy in y until y + h) for (xx in x until x + w) {
                if (xx in 0 until width && yy in 0 until height) p[yy][xx] = key
            }
        }
        draw(rect)
        return PixelSprite(
            assetId = assetId,
            width = width,
            height = height,
            palette = palette,
            rows = p.map { it.concatToString() },
        )
    }

    val depotFacadeExterior: PixelSprite = module(DEPOT_FACADE_EXTERIOR_ID) { rect ->
        rect(0, 0, 128, 64, 'B')
        rect(5, 10, 118, 42, 'M')
        rect(10, 16, 24, 20, 'D')
        rect(39, 14, 22, 28, 'A')
        rect(66, 14, 22, 28, 'A')
        rect(94, 16, 24, 20, 'D')
        rect(48, 18, 4, 20, 'G')
        rect(75, 18, 4, 20, 'G')
        rect(14, 20, 16, 4, 'C')
        rect(98, 20, 16, 4, 'C')
        rect(0, 52, 128, 7, 'L')
        for (x in 8..116 step 18) rect(x, 55, 8, 2, 'R')
    }

    val maintenanceCorridorConnector: PixelSprite = module(MAINTENANCE_CORRIDOR_CONNECTOR_ID) { rect ->
        rect(0, 0, 128, 64, 'B')
        rect(0, 8, 128, 8, 'M')
        rect(0, 48, 128, 8, 'L')
        rect(8, 16, 10, 32, 'A')
        rect(110, 16, 10, 32, 'A')
        rect(22, 20, 84, 24, 'D')
        rect(28, 24, 72, 4, 'M')
        rect(28, 34, 72, 3, 'M')
        for (x in 32..92 step 15) rect(x, 29, 5, 2, 'C')
        rect(4, 25, 4, 12, 'G')
        rect(120, 25, 4, 12, 'G')
    }

    val municipalArchiveExterior: PixelSprite = module(MUNICIPAL_ARCHIVE_EXTERIOR_ID) { rect ->
        rect(0, 0, 128, 64, 'B')
        rect(12, 8, 104, 45, 'M')
        rect(18, 14, 24, 18, 'D')
        rect(86, 14, 24, 18, 'D')
        rect(48, 14, 32, 34, 'A')
        rect(58, 19, 12, 24, 'D')
        rect(62, 19, 4, 24, 'G')
        rect(20, 18, 20, 3, 'C')
        rect(88, 18, 20, 3, 'C')
        rect(18, 37, 92, 4, 'S')
        rect(0, 53, 128, 7, 'L')
        rect(22, 46, 12, 3, 'P')
        rect(94, 46, 12, 3, 'P')
    }

    private fun tile(
        assetId: String,
        draw: ((Int, Int, Int, Int, Char) -> Unit) -> Unit,
    ): PixelSprite {
        val width = 32
        val height = 32
        val p = pixels(width, height)
        val rect: (Int, Int, Int, Int, Char) -> Unit = { x, y, w, h, key ->
            for (yy in y until y + h) for (xx in x until x + w) {
                if (xx in 0 until width && yy in 0 until height) p[yy][xx] = key
            }
        }
        draw(rect)
        return PixelSprite(
            assetId = assetId,
            width = width,
            height = height,
            palette = palette,
            rows = p.map { it.concatToString() },
        )
    }

    val infrastructureWallTile = tile("${MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS_ID}_WALL") { rect ->
        rect(0, 0, 32, 32, 'D')
        rect(0, 0, 32, 3, 'M')
        rect(0, 15, 32, 2, 'A')
        rect(8, 4, 2, 10, 'L')
        rect(22, 18, 2, 11, 'L')
    }

    val infrastructureFloorTile = tile("${MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS_ID}_FLOOR") { rect ->
        rect(0, 0, 32, 32, 'A')
        for (y in 4..28 step 8) rect(0, y, 32, 2, 'M')
        for (x in 6..26 step 10) rect(x, 0, 2, 32, 'D')
        rect(2, 27, 8, 2, 'G')
    }

    val infrastructurePanelTile = tile("${MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS_ID}_PANEL") { rect ->
        rect(1, 1, 30, 30, 'M')
        rect(4, 4, 24, 18, 'D')
        rect(7, 7, 18, 3, 'C')
        rect(7, 13, 10, 2, 'L')
        rect(20, 13, 5, 5, 'G')
        rect(8, 25, 16, 3, 'A')
    }

    val infrastructureRailVentTile = tile("${MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS_ID}_RAIL_VENT") { rect ->
        rect(0, 0, 32, 32, 'D')
        rect(3, 5, 26, 5, 'M')
        rect(5, 6, 22, 2, 'L')
        rect(4, 17, 24, 11, 'M')
        for (x in 7..25 step 6) rect(x, 19, 2, 7, 'D')
    }

    val infrastructureTileAtlas = PixelEnvironmentTileAtlas(
        assetId = MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS_ID,
        tiles = listOf(
            infrastructureWallTile,
            infrastructureFloorTile,
            infrastructurePanelTile,
            infrastructureRailVentTile,
        ),
    )


    /**
     * Player-safe arrival/exterior previews for map inspection.
     *
     * Only exact authored location IDs are mapped. Unmapped locations intentionally return
     * null instead of borrowing unrelated environment art.
     */
    fun arrivalPreview(locationId: String): PixelSprite? = when (locationId) {
        "DISTRICT_PLAZA" -> depotFacadeExterior
        "DISTRICT_ARCHIVE" -> municipalArchiveExterior
        "SERVICE_TUNNEL" -> maintenanceCorridorConnector
        else -> null
    }


    val productionModules: List<PixelSprite> = listOf(
        depotFacadeExterior,
        maintenanceCorridorConnector,
        municipalArchiveExterior,
    )
}
