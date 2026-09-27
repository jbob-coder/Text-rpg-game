from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from textrpg.android_bridge import AndroidBridgeError, create_session


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "vertical_slice_01.json"
FORBIDDEN_AUTHORED_KEYS = {"requires", "visible_if", "outcomes", "effects"}


def walk_keys(value):
    if isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from walk_keys(item)
    elif isinstance(value, list):
        for item in value:
            yield from walk_keys(item)


class AndroidBridgeTests(unittest.TestCase):
    def test_new_session_returns_player_safe_scene_and_status(self):
        session = create_session(CONTENT)

        view = session.scene_view()

        self.assertEqual({"scene", "status", "inventory", "quests", "map", "meta"}, set(view))
        self.assertIn("id", view["scene"])
        self.assertIn("title", view["scene"])
        self.assertIn("body", view["scene"])
        self.assertIn("choices", view["scene"])
        self.assertIn("resources", view["status"])
        self.assertEqual(0, view["meta"]["turn"])
        self.assertEqual(0, view["meta"]["time_minutes"])
        self.assertEqual("PLATFORM_NINE", view["map"]["current_location"])
        self.assertEqual(["PLATFORM_NINE"], [node["id"] for node in view["map"]["nodes"]])
        self.assertEqual([], view["quests"])

        leaked = FORBIDDEN_AUTHORED_KEYS.intersection(set(walk_keys(view)))
        self.assertEqual(set(), leaked)

    def test_quest_projection_exposes_category_without_authored_effects(self):
        session = create_session(CONTENT)
        session.choose("TAKE_DEAD_RELAY")

        view = session.scene_view()

        self.assertEqual(1, len(view["quests"]))
        quest = view["quests"][0]
        self.assertEqual("QUEST_DEAD_RELAY", quest["id"])
        self.assertEqual("The Dead Relay", quest["title"])
        self.assertEqual("main", quest["category"])
        self.assertEqual("active", quest["status"])
        leaked = FORBIDDEN_AUTHORED_KEYS.intersection(set(walk_keys(quest)))
        self.assertEqual(set(), leaked)

    def test_map_projection_discovers_locations_from_history(self):
        session = create_session(CONTENT)
        session.choose("TAKE_DEAD_RELAY")

        view = session.scene_view()
        node_ids = {node["id"] for node in view["map"]["nodes"]}

        self.assertEqual("RELAY_WORKBENCH", view["map"]["current_location"])
        self.assertIn("PLATFORM_NINE", node_ids)
        self.assertIn("RELAY_WORKBENCH", node_ids)
        self.assertNotIn("TRACE_CHAMBER", node_ids)



    def test_map_travel_requires_discovered_adjacent_route_and_advances_time(self):
        session = create_session(CONTENT)
        session.choose("TAKE_DEAD_RELAY")
        before_scene = session.state.scene_id
        before_time = session.state.time_minutes

        view = session.travel("PLATFORM_NINE")

        self.assertEqual(before_scene, session.state.scene_id)
        self.assertEqual(before_time + 5, session.state.time_minutes)
        self.assertEqual("PLATFORM_NINE", view["map"]["current_location"])
        self.assertEqual("map_travel", session.state.history[-1]["type"])

    def test_map_travel_rejects_undiscovered_destination_without_mutation(self):
        session = create_session(CONTENT)
        before = deepcopy(session.state.snapshot())

        with self.assertRaises(AndroidBridgeError) as caught:
            session.travel("TRACE_CHAMBER")

        self.assertEqual("TRAVEL_ERROR", caught.exception.code)
        self.assertEqual(before, session.state.snapshot())

    def test_inventory_projection_exposes_items_and_slots_without_modifiers(self):
        session = create_session(CONTENT)

        view = session.scene_view()

        maintenance_seal = next(
            item for item in view["inventory"]["items"]
            if item["id"] == "ITEM_MAINTENANCE_SEAL"
        )
        self.assertEqual(1, maintenance_seal["quantity"])
        self.assertTrue(all("modifiers" not in entry for entry in view["inventory"]["equipment"]))

    def test_validated_cheats_mutate_only_through_whitelist(self):
        session = create_session(CONTENT)
        session.state.player["resources"]["stamina"] = 1

        restored = session.apply_cheat("fullrestore")

        stamina = next(resource for resource in restored["status"]["resources"] if resource["id"] == "stamina")
        self.assertEqual(stamina["max"], stamina["current"])
        self.assertEqual("FULLRESTORE", session.state.history[-1]["code"])

    def test_unknown_cheat_rolls_back_without_mutation(self):
        session = create_session(CONTENT)
        before = deepcopy(session.state.snapshot())

        with self.assertRaises(AndroidBridgeError) as caught:
            session.apply_cheat("MAKE_ME_A_GOD")

        self.assertEqual("CHEAT_ERROR", caught.exception.code)
        self.assertEqual(before, session.state.snapshot())

    def test_debug_map_cheat_reveals_authored_nodes_without_scene_mutation(self):
        session = create_session(CONTENT)
        before_scene = session.state.scene_id

        view = session.apply_cheat("DEBUGMAP")

        self.assertEqual(before_scene, session.state.scene_id)
        self.assertGreaterEqual(len(view["map"]["nodes"]), 6)


    def test_invalid_choice_is_controlled_and_does_not_mutate_state(self):
        session = create_session(CONTENT)
        before = deepcopy(session.state.snapshot())

        with self.assertRaises(AndroidBridgeError) as caught:
            session.choose("CHOICE_DOES_NOT_EXIST")

        self.assertEqual("CHOICE_ERROR", caught.exception.code)
        self.assertEqual(before, session.state.snapshot())

    def test_choose_returns_updated_player_safe_view(self):
        session = create_session(CONTENT)
        initial = session.scene_view()
        enabled = [choice for choice in initial["scene"]["choices"] if choice["enabled"]]
        self.assertTrue(enabled)

        updated = session.choose(enabled[0]["id"])

        self.assertEqual(1, updated["meta"]["turn"])
        leaked = FORBIDDEN_AUTHORED_KEYS.intersection(set(walk_keys(updated)))
        self.assertEqual(set(), leaked)

    def test_save_and_load_round_trip(self):
        with TemporaryDirectory() as directory:
            save_path = Path(directory) / "save.json"
            session = create_session(CONTENT, save_path=save_path)
            initial = session.scene_view()
            enabled = [choice for choice in initial["scene"]["choices"] if choice["enabled"]]
            session.choose(enabled[0]["id"])
            expected = session.scene_view()
            session.save()

            restored = create_session(CONTENT, save_path=save_path)
            loaded = restored.load()

            self.assertEqual(expected, loaded)
            self.assertEqual(expected, restored.scene_view())

    def test_load_failure_does_not_replace_current_state(self):
        with TemporaryDirectory() as directory:
            save_path = Path(directory) / "save.json"
            save_path.write_text('{"schema_version":999}', encoding="utf-8")
            session = create_session(CONTENT, save_path=save_path)
            before = deepcopy(session.state.snapshot())

            with self.assertRaises(AndroidBridgeError) as caught:
                session.load()

            self.assertEqual("LOAD_ERROR", caught.exception.code)
            self.assertEqual(before, session.state.snapshot())

    def test_authored_equipment_can_be_equipped_and_unequipped_transactionally(self):
        session = create_session(CONTENT)
        before = session.scene_view()
        gear = next(
            item for item in before["inventory"]["items"]
            if item.get("equippable")
        )
        starting_quantity = gear["quantity"]

        equipped = session.equip(gear["id"])
        slot = gear["slot"]
        equipped_slot = next(
            item for item in equipped["inventory"]["equipment"]
            if item["slot"] == slot
        )
        self.assertTrue(equipped_slot["equipped"])
        remaining = next(
            (
                item["quantity"]
                for item in equipped["inventory"]["items"]
                if item["id"] == gear["id"]
            ),
            0,
        )
        self.assertEqual(starting_quantity - 1, remaining)

        restored = session.unequip(slot)
        restored_quantity = next(
            item["quantity"]
            for item in restored["inventory"]["items"]
            if item["id"] == gear["id"]
        )
        self.assertEqual(starting_quantity, restored_quantity)
        empty_slot = next(
            item for item in restored["inventory"]["equipment"]
            if item["slot"] == slot
        )
        self.assertFalse(empty_slot["equipped"])
