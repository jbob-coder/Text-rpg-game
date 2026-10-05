import copy
import json
import tempfile
import unittest
from pathlib import Path

from textrpg import RuleError, content_pack_from_mapping, load_content_pack, inspect_status_value


ROOT = Path(__file__).resolve().parents[1]
SLICE = ROOT / "content" / "vertical_slice_01.json"


class ContentPackTests(unittest.TestCase):
    def test_perk_registry_visibility_reaches_status_without_extra_client_context(self):
        data = self.data()
        data["registries"]["perks"]["PERK_TRACE_TOLERANCE"]["player_visible"] = False
        data["initial_state"]["perks"] = {
            "PERK_TRACE_TOLERANCE": {"modifiers": {"attributes.will": 3}},
        }
        pack = content_pack_from_mapping(data)
        view = inspect_status_value(pack.state, pack.engine, "attributes.will")
        self.assertNotIn("PERK_TRACE_TOLERANCE", repr(view))
        self.assertEqual(view["breakdown"]["unidentified_modifier"], 3.0)

    def test_file_loader_rejects_non_finite_numbers_in_metadata(self):
        data = self.data()
        data["metadata"] = {"probe": None}
        raw = json.dumps(data)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "content.json"
            for token in ("NaN", "Infinity", "-Infinity", "1e400", "-1e400"):
                with self.subTest(token=token):
                    path.write_text(raw.replace('"probe": null', '"probe": ' + token), encoding="utf-8")
                    with self.assertRaisesRegex(RuleError, "strict JSON"):
                        load_content_pack(path)
            path.write_text(raw.replace('"probe": null', '"probe": 1.25'), encoding="utf-8")
            self.assertEqual(load_content_pack(path).raw["metadata"]["probe"], 1.25)

    def data(self):
        return json.loads(SLICE.read_text(encoding="utf-8"))

    def test_load_vertical_slice_builds_state_and_engine(self):
        pack = load_content_pack(SLICE)
        self.assertEqual(pack.content_id, "CONTENT_VERTICAL_SLICE_01")
        self.assertEqual(pack.canon_status, "provisional_canon")
        self.assertEqual(pack.state.scene_id, "OPENING_DEPOT_BLACKOUT")
        choices = {choice["id"] for choice in pack.engine.available_choices(pack.state)}
        self.assertIn("TAKE_DEAD_RELAY", choices)
        self.assertIn("ABILITY_TRACE_ECHO", pack.engine.power_definitions)
        self.assertIn("KNOW_TRACE_ECHO_PATTERN_STABLE", pack.registries["knowledge"])
        self.assertIn("COND_ECHO_STRAIN", pack.registries["conditions"])

    def test_world_map_remains_optional_for_content_packs(self):
        data = self.data()
        del data["world_map"]
        pack = content_pack_from_mapping(data)
        self.assertEqual(pack.state.scene_id, "OPENING_DEPOT_BLACKOUT")

    def test_world_map_scene_destination_must_exist(self):
        data = self.data()
        data["world_map"]["nodes"]["DISTRICT_ARCHIVE"]["scene_id"] = "SCENE_MISSING"
        with self.assertRaisesRegex(RuleError, "unknown scene"):
            content_pack_from_mapping(data)

    def test_world_map_edges_must_reference_known_nodes(self):
        data = self.data()
        data["world_map"]["edges"].append(
            {"from": "DISTRICT_PLAZA", "to": "MISSING_LOCATION"}
        )
        with self.assertRaisesRegex(RuleError, "unknown node"):
            content_pack_from_mapping(data)

    def test_world_map_travel_minutes_must_be_non_negative_integer(self):
        data = self.data()
        data["world_map"]["edges"][0]["travel_minutes"] = -1
        with self.assertRaisesRegex(RuleError, "travel_minutes"):
            content_pack_from_mapping(data)

    def test_unknown_initial_scene_is_rejected(self):
        data = self.data()
        data["initial_state"]["scene_id"] = "SCENE_MISSING"
        with self.assertRaises(RuleError):
            content_pack_from_mapping(data)

    def test_invalid_initial_attribute_is_rejected(self):
        data = self.data()
        data["initial_state"]["player"]["attributes"]["might"] = 150
        with self.assertRaises(RuleError):
            content_pack_from_mapping(data)

    def test_invalid_character_visual_record_is_rejected(self):
        data = self.data()
        del data["characters"]["NPC_TAMSIN"]["hair"]
        with self.assertRaises(RuleError):
            content_pack_from_mapping(data)

    def test_unknown_initial_state_field_is_rejected(self):
        data = self.data()
        data["initial_state"]["mystery_runtime_field"] = True
        with self.assertRaises(RuleError):
            content_pack_from_mapping(data)


    def test_unknown_initial_inventory_registry_id_is_rejected(self):
        data = self.data()
        data["initial_state"]["inventory"]["ITEM_UNREGISTERED"] = 1
        with self.assertRaises(RuleError):
            content_pack_from_mapping(data)


    def test_invalid_initial_player_container_is_rejected_cleanly(self):
        data = self.data()
        data["initial_state"]["player"] = []
        with self.assertRaises(RuleError):
            content_pack_from_mapping(data)

    def test_invalid_initial_knowledge_container_is_rejected_cleanly(self):
        data = self.data()
        data["initial_state"]["knowledge"] = []
        with self.assertRaises(RuleError):
            content_pack_from_mapping(data)

    def test_invalid_initial_turn_type_is_rejected_cleanly(self):
        data = self.data()
        data["initial_state"]["turn"] = True
        with self.assertRaises(RuleError):
            content_pack_from_mapping(data)


    def test_tactical_sections_are_optional_and_empty_by_default(self):
        pack = content_pack_from_mapping(self.data())
        self.assertEqual({}, pack.tactical_maps)
        self.assertEqual({}, pack.combat_actions)
        self.assertEqual({}, pack.combat_actor_archetypes)
        self.assertEqual({}, pack.encounters)
        self.assertFalse(hasattr(pack.state, "tactical"))
        self.assertFalse(hasattr(pack.state, "combat"))

    def test_minimal_tactical_bundle_loads_without_mutating_game_state(self):
        data = self.data()
        data["tactical_maps"] = {
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
                "overrides": {
                    "1,0,0": {
                        "movement_cost": 2,
                        "cover": {"W": 1},
                    }
                },
                "transitions": {},
                "deployment_zones": {
                    "ZONE_PLAYER": ["0,0,0"],
                },
                "objective_anchors": {
                    "OBJECTIVE_TEST": "1,1,0",
                },
                "exits": {
                    "EXIT_TEST": "0,1,0",
                },
            }
        }
        data["combat_actions"] = {
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
        data["combat_actor_archetypes"] = {
            "ARCHETYPE_CONTACT": {
                "archetype_id": "ARCHETYPE_CONTACT",
                "action_ids": ["ACTION_MOVE"],
                "footprint": 1,
                "tags": ["contact"],
            }
        }
        data["encounters"] = {
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
                        "deployment_zone": "ZONE_PLAYER",
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

        before_state = copy.deepcopy(data["initial_state"])
        pack = content_pack_from_mapping(data)

        tactical_map = pack.tactical_maps["TACTICAL_MAP_TEST"]
        self.assertEqual(2, tactical_map.width)
        self.assertEqual(2, tactical_map.cell_at(
            __import__("textrpg").TacticalCoord(1, 0, 0)
        ).movement_cost)
        self.assertEqual(before_state, pack.state.snapshot())
        self.assertEqual("ACTION_MOVE", pack.combat_actions["ACTION_MOVE"]["action_id"])

    def test_tactical_section_roots_must_be_objects(self):
        for field_name in (
            "tactical_maps",
            "combat_actions",
            "combat_actor_archetypes",
            "encounters",
        ):
            with self.subTest(field_name=field_name):
                data = self.data()
                data[field_name] = []
                with self.assertRaisesRegex(RuleError, field_name):
                    content_pack_from_mapping(data)


if __name__ == "__main__":
    unittest.main()
