from __future__ import annotations

import unittest

from textrpg.combat_schema import (
    COVER_PARTIAL,
    COVER_STRONG,
    TacticalAnchor,
    TacticalCell,
    TacticalCoord,
    TacticalMap,
    TacticalTransition,
    TacticalZone,
)


def cell(x: int, y: int, z: int = 0, **kwargs) -> TacticalCell:
    return TacticalCell(TacticalCoord(x, y, z), **kwargs)


class TacticalSchemaTests(unittest.TestCase):
    def test_coordinate_key_round_trip(self) -> None:
        coord = TacticalCoord(7, 3, -1)
        self.assertEqual("7,3,-1", coord.key)
        self.assertEqual(coord, TacticalCoord.from_key(coord.key))

    def test_coordinate_rejects_bool_axis(self) -> None:
        with self.assertRaisesRegex(ValueError, "coord.x must be an integer"):
            TacticalCoord(True, 0, 0)

    def test_cell_canonicalizes_cover_and_los_edges(self) -> None:
        tactical_cell = cell(
            0,
            0,
            cover=(("W", COVER_STRONG), ("N", COVER_PARTIAL)),
            los_blocked_edges=("S", "N"),
        )
        self.assertEqual(
            (("N", COVER_PARTIAL), ("W", COVER_STRONG)),
            tactical_cell.cover,
        )
        self.assertEqual(("N", "S"), tactical_cell.los_blocked_edges)
        self.assertEqual(COVER_STRONG, tactical_cell.cover_rating("W"))
        self.assertEqual(0, tactical_cell.cover_rating("E"))

    def test_cell_rejects_bad_cover_edge_and_rating(self) -> None:
        with self.assertRaisesRegex(ValueError, "unsupported edges"):
            cell(0, 0, cover=(("NE", COVER_PARTIAL),))
        with self.assertRaisesRegex(ValueError, "must be 0, 1, or 2"):
            cell(0, 0, cover=(("N", 3),))

    def test_map_rejects_duplicate_and_out_of_bounds_cells(self) -> None:
        with self.assertRaisesRegex(ValueError, "duplicate tactical cell"):
            TacticalMap(
                "MAP_TEST",
                1,
                2,
                2,
                (0,),
                (cell(0, 0), cell(0, 0)),
            )
        with self.assertRaisesRegex(ValueError, "out of bounds"):
            TacticalMap(
                "MAP_TEST",
                1,
                2,
                2,
                (0,),
                (cell(2, 0),),
            )

    def test_map_rejects_transition_to_unknown_or_blocked_cell(self) -> None:
        with self.assertRaisesRegex(ValueError, "unknown cell 0,0,1"):
            TacticalMap(
                "MAP_TEST",
                1,
                1,
                1,
                (0, 1),
                (cell(0, 0, 0),),
                (
                    TacticalTransition(
                        "TRANSITION_UP",
                        TacticalCoord(0, 0, 0),
                        TacticalCoord(0, 0, 1),
                    ),
                ),
            )

        with self.assertRaisesRegex(ValueError, "blocked cell 0,0,1"):
            TacticalMap(
                "MAP_TEST",
                1,
                1,
                1,
                (0, 1),
                (cell(0, 0, 0), cell(0, 0, 1, blocks_movement=True)),
                (
                    TacticalTransition(
                        "TRANSITION_UP",
                        TacticalCoord(0, 0, 0),
                        TacticalCoord(0, 0, 1),
                    ),
                ),
            )

    def test_map_validates_deployment_objective_and_exit_anchors(self) -> None:
        tactical_map = TacticalMap(
            "MAP_TEST",
            1,
            2,
            1,
            (0,),
            (cell(0, 0), cell(1, 0)),
            deployment_zones=(
                TacticalZone("ZONE_PLAYER", (TacticalCoord(0, 0),)),
            ),
            objective_anchors=(
                TacticalAnchor("OBJECTIVE_RELAY", TacticalCoord(1, 0)),
            ),
            exits=(TacticalAnchor("EXIT_WEST", TacticalCoord(0, 0)),),
        )
        self.assertEqual("ZONE_PLAYER", tactical_map.deployment_zones[0].zone_id)

        with self.assertRaisesRegex(ValueError, "references blocked cell"):
            TacticalMap(
                "MAP_BAD",
                1,
                1,
                1,
                (0,),
                (cell(0, 0, blocks_movement=True),),
                exits=(TacticalAnchor("EXIT_BAD", TacticalCoord(0, 0)),),
            )

    def test_transition_targets_are_explicit_and_deterministic(self) -> None:
        tactical_map = TacticalMap(
            "MAP_TEST",
            1,
            2,
            1,
            (0, 1),
            (
                cell(0, 0, 0),
                cell(1, 0, 0),
                cell(0, 0, 1),
            ),
            (
                TacticalTransition(
                    "TRANSITION_UP",
                    TacticalCoord(0, 0, 0),
                    TacticalCoord(0, 0, 1),
                    cost=2,
                ),
            ),
        )
        self.assertEqual(
            ((TacticalCoord(0, 0, 1), 2),),
            tactical_map.transition_targets(TacticalCoord(0, 0, 0)),
        )
        self.assertEqual(
            ((TacticalCoord(0, 0, 0), 2),),
            tactical_map.transition_targets(TacticalCoord(0, 0, 1)),
        )


if __name__ == "__main__":
    unittest.main()
