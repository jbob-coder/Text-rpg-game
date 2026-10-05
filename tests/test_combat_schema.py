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
    parse_tactical_map_definition,
)
from textrpg.validation import validate_tactical_content


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

    def test_phase1_transition_rejects_same_z_shortcuts(self) -> None:
        with self.assertRaisesRegex(ValueError, "different z layers"):
            TacticalTransition(
                "TRANSITION_DIAGONAL",
                TacticalCoord(0, 0, 0),
                TacticalCoord(1, 1, 0),
            )

        tactical_maps, actions, archetypes, encounters, world_map = self.authored_bundle()
        tactical_maps["TACTICAL_MAP_TEST"]["transitions"] = {
            "TRANSITION_DIAGONAL": {
                "from": "0,0,0",
                "to": "1,1,0",
                "cost": 1,
                "bidirectional": True,
            }
        }
        errors = validate_tactical_content(
            tactical_maps,
            actions,
            archetypes,
            encounters,
            world_map,
        )
        self.assertTrue(
            any("different z layers" in error for error in errors),
            errors,
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


    def authored_bundle(self):
        tactical_maps = {
            "TACTICAL_MAP_TEST": {
                "map_id": "TACTICAL_MAP_TEST",
                "version": 1,
                "width": 2,
                "height": 2,
                "z_layers": [0],
                "default_cell": {
                    "terrain_id": "TERRAIN_FLOOR",
                    "movement_cost": 1,
                    "blocks_movement": False,
                    "blocks_los": False,
                    "cover": {},
                },
                "overrides": {},
                "transitions": {},
                "deployment_zones": {"ZONE_ENTRY": ["0,0,0"]},
                "objective_anchors": {"OBJECTIVE_TEST": "1,1,0"},
                "exits": {"EXIT_TEST": "0,1,0"},
            }
        }
        combat_actions = {
            "ACTION_MOVE": {
                "action_id": "ACTION_MOVE",
                "category": "move",
                "cost": 1,
                "range_min": 0,
                "range_max": 6,
                "requires_los": False,
                "tags": ["movement"],
            }
        }
        archetypes = {
            "ARCHETYPE_CONTACT": {
                "archetype_id": "ARCHETYPE_CONTACT",
                "action_ids": ["ACTION_MOVE"],
                "footprint": 1,
                "tags": ["contact"],
            }
        }
        encounters = {
            "ENCOUNTER_TEST": {
                "encounter_id": "ENCOUNTER_TEST",
                "map_id": "TACTICAL_MAP_TEST",
                "location_id": "SERVICE_TUNNEL",
                "trigger": {},
                "participants": [
                    {
                        "actor_id": "CONTACT_A",
                        "archetype_id": "ARCHETYPE_CONTACT",
                        "faction_id": "FACTION_CONTACT",
                        "action_ids": ["ACTION_MOVE"],
                        "deployment_zone": "ZONE_ENTRY",
                        "required": True,
                    }
                ],
                "deployment": {},
                "objective_set": {},
                "retreat_policy": {},
                "ai_profiles": {},
                "aftermath_profile": {},
                "time_cost_minutes": 10,
                "canon_status": "PROPOSED",
            }
        }
        world_map = {"nodes": {"SERVICE_TUNNEL": {}}}
        return tactical_maps, combat_actions, archetypes, encounters, world_map

    def test_authored_tactical_bundle_validates_cross_references(self) -> None:
        sections = self.authored_bundle()
        self.assertEqual([], validate_tactical_content(*sections))

        parsed = parse_tactical_map_definition(
            "TACTICAL_MAP_TEST",
            sections[0]["TACTICAL_MAP_TEST"],
        )
        self.assertEqual(4, len(parsed.cells))
        self.assertEqual(
            TacticalCoord(0, 0, 0),
            parsed.deployment_zones[0].cells[0],
        )

    def test_authored_map_rejects_out_of_bounds_override(self) -> None:
        tactical_maps, actions, archetypes, encounters, world_map = self.authored_bundle()
        tactical_maps["TACTICAL_MAP_TEST"]["overrides"] = {
            "2,0,0": {"movement_cost": 2}
        }
        errors = validate_tactical_content(
            tactical_maps,
            actions,
            archetypes,
            encounters,
            world_map,
        )
        self.assertTrue(any("out of bounds" in error for error in errors))

    def test_authored_los_blocked_edges_parse_from_default_and_override(self) -> None:
        tactical_maps, _actions, _archetypes, _encounters, _world_map = self.authored_bundle()
        definition = tactical_maps["TACTICAL_MAP_TEST"]
        definition["default_cell"]["los_blocked_edges"] = ["E"]
        definition["overrides"]["1,0,0"] = {"los_blocked_edges": ["W"]}

        parsed = parse_tactical_map_definition("TACTICAL_MAP_TEST", definition)

        self.assertEqual(
            ("E",),
            parsed.cell_at(TacticalCoord(0, 0, 0)).los_blocked_edges,
        )
        self.assertEqual(
            ("W",),
            parsed.cell_at(TacticalCoord(1, 0, 0)).los_blocked_edges,
        )

    def test_authored_map_rejects_non_cardinal_los_blocked_edge(self) -> None:
        tactical_maps, actions, archetypes, encounters, world_map = self.authored_bundle()
        tactical_maps["TACTICAL_MAP_TEST"]["default_cell"]["los_blocked_edges"] = ["NE"]

        errors = validate_tactical_content(
            tactical_maps,
            actions,
            archetypes,
            encounters,
            world_map,
        )

        self.assertTrue(
            any(
                "los_blocked_edges" in error and "unsupported edges" in error
                for error in errors
            )
        )

    def test_authored_cell_explicit_null_lists_reject(self) -> None:
        for field_name in ("los_blocked_edges", "hazard_ids", "tags"):
            with self.subTest(field_name=field_name):
                tactical_maps, actions, archetypes, encounters, world_map = self.authored_bundle()
                tactical_maps["TACTICAL_MAP_TEST"]["default_cell"][field_name] = None

                errors = validate_tactical_content(
                    tactical_maps,
                    actions,
                    archetypes,
                    encounters,
                    world_map,
                )

                self.assertTrue(
                    any(
                        field_name in error and "must be a list" in error
                        for error in errors
                    ),
                    errors,
                )

    def test_encounter_location_rejects_when_explicit_world_map_has_no_nodes(self) -> None:
        tactical_maps, actions, archetypes, encounters, _world_map = self.authored_bundle()
        errors = validate_tactical_content(
            tactical_maps,
            actions,
            archetypes,
            encounters,
            {"nodes": {}},
        )

        self.assertTrue(
            any("unknown world location" in error for error in errors),
            errors,
        )

    def test_action_and_archetype_unknown_fields_or_refs_reject(self) -> None:
        tactical_maps, actions, archetypes, encounters, world_map = self.authored_bundle()
        actions["ACTION_MOVE"]["mystery_rule"] = True
        archetypes["ARCHETYPE_CONTACT"]["action_ids"] = ["ACTION_MISSING"]

        errors = validate_tactical_content(
            tactical_maps,
            actions,
            archetypes,
            encounters,
            world_map,
        )

        self.assertTrue(any("unsupported fields" in error for error in errors))
        self.assertTrue(any("unknown combat action" in error for error in errors))

    def test_encounter_rejects_unknown_map_archetype_action_and_location(self) -> None:
        tactical_maps, actions, archetypes, encounters, world_map = self.authored_bundle()
        encounter = encounters["ENCOUNTER_TEST"]
        encounter["map_id"] = "TACTICAL_MAP_MISSING"
        encounter["location_id"] = "LOCATION_MISSING"
        encounter["participants"][0]["archetype_id"] = "ARCHETYPE_MISSING"
        encounter["participants"][0]["action_ids"] = ["ACTION_MISSING"]

        errors = validate_tactical_content(
            tactical_maps,
            actions,
            archetypes,
            encounters,
            world_map,
        )

        self.assertTrue(any("unknown tactical map" in error for error in errors))
        self.assertTrue(any("unknown world location" in error for error in errors))
        self.assertTrue(any("unknown combat archetype" in error for error in errors))
        self.assertTrue(any("unknown combat action" in error for error in errors))

    def test_encounter_rejects_unknown_deployment_zone(self) -> None:
        tactical_maps, actions, archetypes, encounters, world_map = self.authored_bundle()
        encounters["ENCOUNTER_TEST"]["participants"][0][
            "deployment_zone"
        ] = "ZONE_MISSING"

        errors = validate_tactical_content(
            tactical_maps,
            actions,
            archetypes,
            encounters,
            world_map,
        )
        self.assertTrue(any("unknown deployment zone" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
