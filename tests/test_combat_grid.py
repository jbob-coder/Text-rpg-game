from __future__ import annotations

import unittest

from textrpg.combat_grid import (
    TacticalOccupant,
    cardinal_neighbors,
    cover_rating,
    find_path,
    has_line_of_sight,
    incoming_cover_edge,
    occupancy_by_coord,
    supercover_line,
)
from textrpg.combat_schema import (
    COVER_PARTIAL,
    COVER_STRONG,
    TacticalCell,
    TacticalCoord,
    TacticalMap,
    TacticalTransition,
)


def open_cell(
    x: int,
    y: int,
    z: int = 0,
    *,
    movement_cost: int = 1,
    blocks_movement: bool = False,
    blocks_los: bool = False,
    los_blocked_edges: tuple[str, ...] = (),
    cover: tuple[tuple[str, int], ...] = (),
) -> TacticalCell:
    return TacticalCell(
        TacticalCoord(x, y, z),
        movement_cost=movement_cost,
        blocks_movement=blocks_movement,
        blocks_los=blocks_los,
        los_blocked_edges=los_blocked_edges,
        cover=cover,
    )


def rectangular_map(
    width: int,
    height: int,
    *,
    overrides: dict[tuple[int, int, int], dict] | None = None,
    z_layers: tuple[int, ...] = (0,),
    transitions: tuple[TacticalTransition, ...] = (),
) -> TacticalMap:
    overrides = overrides or {}
    cells = []
    for z in z_layers:
        for y in range(height):
            for x in range(width):
                cells.append(open_cell(x, y, z, **overrides.get((x, y, z), {})))
    return TacticalMap(
        "MAP_TEST",
        1,
        width,
        height,
        z_layers,
        tuple(cells),
        transitions,
    )


class TacticalGridTests(unittest.TestCase):
    def test_cardinal_neighbors_are_north_east_south_west(self) -> None:
        self.assertEqual(
            (
                TacticalCoord(4, 2, 1),
                TacticalCoord(5, 3, 1),
                TacticalCoord(4, 4, 1),
                TacticalCoord(3, 3, 1),
            ),
            cardinal_neighbors(TacticalCoord(4, 3, 1)),
        )

    def test_occupancy_rejects_two_solid_actors_on_one_cell(self) -> None:
        coord = TacticalCoord(1, 1)
        with self.assertRaisesRegex(ValueError, "solid occupancy conflict"):
            occupancy_by_coord(
                (
                    TacticalOccupant("ALLY_A", "FACTION_A", coord),
                    TacticalOccupant("ALLY_B", "FACTION_A", coord),
                )
            )

    def test_path_has_stable_equal_cost_tie(self) -> None:
        tactical_map = rectangular_map(3, 3)
        expected = (
            TacticalCoord(0, 0),
            TacticalCoord(1, 0),
            TacticalCoord(2, 0),
            TacticalCoord(2, 1),
            TacticalCoord(2, 2),
        )
        first = find_path(tactical_map, TacticalCoord(0, 0), TacticalCoord(2, 2))
        second = find_path(tactical_map, TacticalCoord(0, 0), TacticalCoord(2, 2))
        self.assertEqual(expected, first)
        self.assertEqual(first, second)

    def test_path_uses_destination_movement_cost(self) -> None:
        tactical_map = rectangular_map(
            3,
            2,
            overrides={(1, 0, 0): {"movement_cost": 9}},
        )
        path = find_path(tactical_map, TacticalCoord(0, 0), TacticalCoord(2, 0))
        self.assertEqual(
            (
                TacticalCoord(0, 0),
                TacticalCoord(0, 1),
                TacticalCoord(1, 1),
                TacticalCoord(2, 1),
                TacticalCoord(2, 0),
            ),
            path,
        )

    def test_path_rejects_blocked_destination_and_enemy_pass_through(self) -> None:
        blocked_map = rectangular_map(
            3,
            1,
            overrides={(2, 0, 0): {"blocks_movement": True}},
        )
        self.assertIsNone(
            find_path(blocked_map, TacticalCoord(0, 0), TacticalCoord(2, 0))
        )

        tactical_map = rectangular_map(3, 1)
        enemy = TacticalOccupant(
            "ENEMY",
            "FACTION_B",
            TacticalCoord(1, 0),
        )
        self.assertIsNone(
            find_path(
                tactical_map,
                TacticalCoord(0, 0),
                TacticalCoord(2, 0),
                occupants=(enemy,),
                moving_actor_id="PLAYER",
                moving_faction_id="FACTION_A",
                allow_allies_through=True,
            )
        )

    def test_ally_pass_through_is_explicit_and_endpoint_stays_blocked(self) -> None:
        tactical_map = rectangular_map(3, 1)
        ally = TacticalOccupant(
            "ALLY",
            "FACTION_A",
            TacticalCoord(1, 0),
        )
        self.assertIsNone(
            find_path(
                tactical_map,
                TacticalCoord(0, 0),
                TacticalCoord(2, 0),
                occupants=(ally,),
                moving_actor_id="PLAYER",
                moving_faction_id="FACTION_A",
                allow_allies_through=False,
            )
        )
        self.assertEqual(
            (
                TacticalCoord(0, 0),
                TacticalCoord(1, 0),
                TacticalCoord(2, 0),
            ),
            find_path(
                tactical_map,
                TacticalCoord(0, 0),
                TacticalCoord(2, 0),
                occupants=(ally,),
                moving_actor_id="PLAYER",
                moving_faction_id="FACTION_A",
                allow_allies_through=True,
            ),
        )

        occupied_goal = TacticalOccupant(
            "ALLY_GOAL",
            "FACTION_A",
            TacticalCoord(2, 0),
        )
        self.assertIsNone(
            find_path(
                tactical_map,
                TacticalCoord(0, 0),
                TacticalCoord(2, 0),
                occupants=(occupied_goal,),
                moving_actor_id="PLAYER",
                moving_faction_id="FACTION_A",
                allow_allies_through=True,
            )
        )

    def test_vertical_path_requires_explicit_transition(self) -> None:
        no_transition = rectangular_map(1, 1, z_layers=(0, 1))
        self.assertIsNone(
            find_path(no_transition, TacticalCoord(0, 0, 0), TacticalCoord(0, 0, 1))
        )

        transition = TacticalTransition(
            "STAIRS_UP",
            TacticalCoord(0, 0, 0),
            TacticalCoord(0, 0, 1),
            cost=2,
        )
        tactical_map = rectangular_map(
            1,
            1,
            z_layers=(0, 1),
            transitions=(transition,),
        )
        self.assertEqual(
            (TacticalCoord(0, 0, 0), TacticalCoord(0, 0, 1)),
            find_path(
                tactical_map,
                TacticalCoord(0, 0, 0),
                TacticalCoord(0, 0, 1),
            ),
        )

    def test_transition_maps_use_optimal_dijkstra_route(self) -> None:
        transitions = (
            TacticalTransition(
                "TRANSITION_SHORTCUT_UP",
                TacticalCoord(0, 1, 0),
                TacticalCoord(4, 0, 1),
                cost=1,
            ),
            TacticalTransition(
                "TRANSITION_SHORTCUT_DOWN",
                TacticalCoord(4, 0, 1),
                TacticalCoord(4, 0, 0),
                cost=1,
            ),
        )
        tactical_map = rectangular_map(
            5,
            2,
            z_layers=(0, 1),
            transitions=transitions,
        )

        self.assertEqual(
            (
                TacticalCoord(0, 0, 0),
                TacticalCoord(0, 1, 0),
                TacticalCoord(4, 0, 1),
                TacticalCoord(4, 0, 0),
            ),
            find_path(
                tactical_map,
                TacticalCoord(0, 0, 0),
                TacticalCoord(4, 0, 0),
            ),
        )

    def test_supercover_includes_corner_touch_cells_in_stable_order(self) -> None:
        self.assertEqual(
            (
                TacticalCoord(0, 0),
                TacticalCoord(1, 0),
                TacticalCoord(0, 1),
                TacticalCoord(1, 1),
                TacticalCoord(2, 1),
                TacticalCoord(1, 2),
                TacticalCoord(2, 2),
            ),
            supercover_line(TacticalCoord(0, 0), TacticalCoord(2, 2)),
        )

    def test_same_cell_los_is_true_even_when_cell_is_opaque(self) -> None:
        tactical_map = rectangular_map(
            1,
            1,
            overrides={(0, 0, 0): {"blocks_los": True}},
        )
        coord = TacticalCoord(0, 0)

        self.assertTrue(has_line_of_sight(tactical_map, coord, coord))

    def test_corner_touch_opaque_cell_blocks_los(self) -> None:
        clear_map = rectangular_map(3, 3)
        self.assertTrue(
            has_line_of_sight(clear_map, TacticalCoord(0, 0), TacticalCoord(2, 2))
        )

        blocked_map = rectangular_map(
            3,
            3,
            overrides={(1, 0, 0): {"blocks_los": True}},
        )
        self.assertFalse(
            has_line_of_sight(blocked_map, TacticalCoord(0, 0), TacticalCoord(2, 2))
        )

    def test_movement_blocker_does_not_automatically_block_los(self) -> None:
        tactical_map = rectangular_map(
            3,
            1,
            overrides={(1, 0, 0): {"blocks_movement": True}},
        )
        self.assertTrue(
            has_line_of_sight(tactical_map, TacticalCoord(0, 0), TacticalCoord(2, 0))
        )

    def test_opaque_edge_blocks_los(self) -> None:
        tactical_map = rectangular_map(
            3,
            1,
            overrides={(1, 0, 0): {"los_blocked_edges": ("E",)}},
        )
        self.assertFalse(
            has_line_of_sight(tactical_map, TacticalCoord(0, 0), TacticalCoord(2, 0))
        )

    def test_one_sided_opaque_edge_blocks_los_in_both_directions(self) -> None:
        tactical_map = rectangular_map(
            2,
            1,
            overrides={(0, 0, 0): {"los_blocked_edges": ("E",)}},
        )
        left = TacticalCoord(0, 0)
        right = TacticalCoord(1, 0)

        self.assertFalse(has_line_of_sight(tactical_map, left, right))
        self.assertFalse(has_line_of_sight(tactical_map, right, left))

    def test_cover_alone_does_not_block_los(self) -> None:
        tactical_map = rectangular_map(
            2,
            1,
            overrides={(1, 0, 0): {"cover": (("W", COVER_STRONG),)}},
        )
        left = TacticalCoord(0, 0)
        right = TacticalCoord(1, 0)

        self.assertTrue(has_line_of_sight(tactical_map, left, right))
        self.assertTrue(has_line_of_sight(tactical_map, right, left))

    def test_opaque_endpoint_cell_blocks_los_symmetrically(self) -> None:
        tactical_map = rectangular_map(
            2,
            1,
            overrides={(0, 0, 0): {"blocks_los": True}},
        )
        opaque = TacticalCoord(0, 0)
        clear = TacticalCoord(1, 0)

        self.assertFalse(has_line_of_sight(tactical_map, opaque, clear))
        self.assertFalse(has_line_of_sight(tactical_map, clear, opaque))

    def test_incoming_cover_edge_and_rating_are_deterministic(self) -> None:
        tactical_map = rectangular_map(
            3,
            3,
            overrides={
                (2, 2, 0): {
                    "cover": (
                        ("N", COVER_STRONG),
                        ("W", COVER_PARTIAL),
                    )
                }
            },
        )
        self.assertEqual(
            "N",
            incoming_cover_edge(TacticalCoord(0, 0), TacticalCoord(2, 2)),
        )
        self.assertEqual(
            COVER_STRONG,
            cover_rating(tactical_map, TacticalCoord(0, 0), TacticalCoord(2, 2)),
        )
        self.assertEqual(
            "W",
            incoming_cover_edge(TacticalCoord(0, 2), TacticalCoord(2, 2)),
        )
        self.assertEqual(
            COVER_PARTIAL,
            cover_rating(tactical_map, TacticalCoord(0, 2), TacticalCoord(2, 2)),
        )


    def test_los_is_symmetric_and_stable_for_static_geometry(self) -> None:
        tactical_map = rectangular_map(
            4,
            3,
            overrides={(2, 1, 0): {"blocks_los": True}},
        )
        start = TacticalCoord(0, 0)
        end = TacticalCoord(3, 2)

        forward_first = has_line_of_sight(tactical_map, start, end)
        forward_second = has_line_of_sight(tactical_map, start, end)
        reverse = has_line_of_sight(tactical_map, end, start)

        self.assertEqual(forward_first, forward_second)
        self.assertEqual(forward_first, reverse)

    def test_preview_queries_do_not_mutate_occupancy(self) -> None:
        tactical_map = rectangular_map(3, 2)
        occupants = (
            TacticalOccupant("PLAYER", "FACTION_A", TacticalCoord(0, 0)),
            TacticalOccupant("ALLY", "FACTION_A", TacticalCoord(1, 0)),
        )
        before = occupants

        path = find_path(
            tactical_map,
            TacticalCoord(0, 0),
            TacticalCoord(2, 0),
            occupants=occupants,
            moving_actor_id="PLAYER",
            moving_faction_id="FACTION_A",
            allow_allies_through=True,
        )
        los = has_line_of_sight(
            tactical_map,
            TacticalCoord(0, 0),
            TacticalCoord(2, 0),
        )

        self.assertIsNotNone(path)
        self.assertTrue(los)
        self.assertEqual(before, occupants)
        self.assertEqual(
            TacticalCoord(1, 0),
            occupants[1].coord,
        )


if __name__ == "__main__":
    unittest.main()
