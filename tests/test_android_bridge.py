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

        self.assertEqual({"scene", "status", "inventory", "quests", "map", "visuals", "meta"}, set(view))
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

    def test_relay_visual_projection_tracks_player_visible_story_state(self):
        session = create_session(CONTENT)

        initial = session.scene_view()
        self.assertIsNone(initial["visuals"]["relay_state"])

        intact = session.choose("TAKE_DEAD_RELAY")
        self.assertEqual("intact", intact["visuals"]["relay_state"])

        opened = session.choose("USE_MAINTENANCE_SEAL")
        self.assertEqual("opened", opened["visuals"]["relay_state"])

        damaged_session = create_session(CONTENT)
        damaged_session.choose("TAKE_DEAD_RELAY")
        damaged_session.state.flags["relay.casing_damaged"] = True
        damaged = damaged_session.scene_view()
        self.assertEqual("damaged", damaged["visuals"]["relay_state"])

        damaged_session.state.flags["relay.signal_lost"] = True
        lost = damaged_session.scene_view()
        self.assertEqual("signal_lost", lost["visuals"]["relay_state"])

        self.assertNotIn("flags", lost)
        self.assertNotIn("relay.casing_damaged", set(walk_keys(lost)))
        self.assertNotIn("relay.signal_lost", set(walk_keys(lost)))

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

    def test_inventory_projection_exposes_items_slots_and_explicit_quality_without_modifiers(self):
        session = create_session(CONTENT)

        view = session.scene_view()

        maintenance_seal = next(
            item for item in view["inventory"]["items"]
            if item["id"] == "ITEM_MAINTENANCE_SEAL"
        )
        signal_ring = next(
            item for item in view["inventory"]["items"]
            if item["id"] == "ITEM_SIGNAL_RING"
        )
        self.assertEqual(1, maintenance_seal["quantity"])
        self.assertIsNone(maintenance_seal["quality"])
        self.assertEqual("uncommon", signal_ring["quality"])
        self.assertTrue(all("modifiers" not in entry for entry in view["inventory"]["equipment"]))
        self.assertTrue(all("modifiers" not in entry for entry in view["inventory"]["items"]))

    def test_stat_inspection_reports_player_safe_equipment_contributions(self):
        session = create_session(CONTENT)
        session.equip("ITEM_DEPOT_JACKET")
        session.equip("ITEM_WORK_GLOVES")
        before = deepcopy(session.state.snapshot())

        endurance = session.inspect_status("attributes.endurance")
        technical = session.inspect_status("skills.technical_systems")

        self.assertEqual("attributes.endurance", endurance["path"])
        self.assertEqual(37.0, endurance["total"])
        self.assertEqual(35.0, endurance["breakdown"]["base"])
        self.assertEqual(2.0, endurance["breakdown"]["equipment:body"])
        self.assertEqual("skills.technical_systems", technical["path"])
        self.assertEqual(26.0, technical["total"])
        self.assertEqual(1.0, technical["breakdown"]["equipment:hands"])
        self.assertEqual(before, session.state.snapshot())
        leaked = FORBIDDEN_AUTHORED_KEYS.intersection(set(walk_keys(endurance)))
        self.assertEqual(set(), leaked)

    def test_stat_inspection_rejects_non_status_paths_without_mutation(self):
        session = create_session(CONTENT)
        before = deepcopy(session.state.snapshot())

        with self.assertRaises(AndroidBridgeError) as caught:
            session.inspect_status("quests.QUEST_DEAD_RELAY")

        self.assertEqual("STAT_INSPECTION_ERROR", caught.exception.code)
        self.assertEqual(before, session.state.snapshot())

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


    def test_free_roam_nodes_unlock_and_travel_changes_scene(self):
        session = create_session(CONTENT)
        session.state.scene_id = "DISTRICT_HUB"
        session.state.flags["world.free_roam_unlocked"] = True

        before = session.scene_view()
        nodes = {node["id"]: node for node in before["map"]["nodes"]}

        self.assertEqual("DISTRICT_PLAZA", before["map"]["current_location"])
        self.assertTrue(nodes["DISTRICT_ARCHIVE"]["reachable"])
        self.assertTrue(nodes["WORKSHOP_ROW"]["reachable"])

        after = session.travel("DISTRICT_ARCHIVE")

        self.assertEqual("DISTRICT_ARCHIVE", session.state.scene_id)
        self.assertEqual("DISTRICT_ARCHIVE", after["map"]["current_location"])
        self.assertEqual("The Municipal Archive", after["scene"]["title"])

    def test_archive_lore_choice_changes_narrative_state_without_stat_reward(self):
        session = create_session(CONTENT)
        session.state.scene_id = "DISTRICT_ARCHIVE"
        session.state.flags["world.free_roam_unlocked"] = True
        attributes_before = deepcopy(session.state.player.get("attributes", {}))

        view = session.choose("READ_PLATFORM_NINE_RECORDS")

        self.assertIn("KNOW_PLATFORM_NINE_EVAC_PROTOCOL", session.state.knowledge)
        self.assertEqual(attributes_before, session.state.player.get("attributes", {}))
        lore = next(
            quest for quest in view["quests"]
            if quest["id"] == "QUEST_PLATFORM_NINE_RECORDS"
        )
        self.assertEqual("lore", lore["category"])
        self.assertEqual("completed", lore["status"])

    def test_directional_branch_continues_into_free_roam_hub(self):
        session = create_session(CONTENT)
        session.state.scene_id = "TRACE_DIRECTIONAL_SESSION_END"

        view = session.choose("END_DIRECTIONAL_TRACE_PROTOTYPE")

        self.assertEqual("DISTRICT_HUB", session.state.scene_id)
        self.assertTrue(session.state.flags["world.free_roam_unlocked"])
        self.assertEqual("DISTRICT_PLAZA", view["map"]["current_location"])


    def test_opening_can_detour_into_district_and_resume_trace_quest(self):
        session = create_session(CONTENT)
        session.state.scene_id = "OPENING_END"

        district = session.choose("RETURN_TO_DISTRICT_BEFORE_TRACE")

        self.assertEqual("DISTRICT_HUB", session.state.scene_id)
        self.assertTrue(session.state.flags["world.free_roam_unlocked"])
        self.assertFalse(session.state.flags["world.trace_echo_quest_started"])
        resume = next(
            choice for choice in district["scene"]["choices"]
            if choice["id"] == "RESUME_GATE_TWELVE_INVESTIGATION"
        )
        self.assertTrue(resume["enabled"])

        resumed = session.choose("RESUME_GATE_TWELVE_INVESTIGATION")

        self.assertEqual("POWER_GATE_TWELVE_SIGNAL", session.state.scene_id)
        self.assertTrue(session.state.flags["world.trace_echo_quest_started"])
        self.assertIn("QUEST_GATE_TWELVE_ECHO", session.state.quests)
        self.assertEqual("A Signal With No Receiver", resumed["scene"]["title"])


    def test_workshop_rumor_unlocks_delayed_archive_investigation(self):
        session = create_session(CONTENT)
        session.state.flags["world.free_roam_unlocked"] = True
        session.state.scene_id = "DISTRICT_WORKSHOP"

        session.choose("ASK_WORKERS_ABOUT_GATE_TWELVE")
        self.assertTrue(session.state.flags["world.workshop_rumor_heard"])

        session.state.scene_id = "DISTRICT_ARCHIVE"
        archive = session.scene_view()
        choices = {choice["id"] for choice in archive["scene"]["choices"]}
        self.assertIn("CROSSCHECK_GATE_TWELVE_WORKSHOP_RUMOR", choices)

        result = session.choose("CROSSCHECK_GATE_TWELVE_WORKSHOP_RUMOR")

        self.assertIn("KNOW_GATE_TWELVE_CREW_WITHDRAWAL", session.state.knowledge)
        self.assertEqual("DISTRICT_ARCHIVE", result["map"]["current_location"])


    def test_district_cheat_is_explicit_and_player_safe(self):
        session = create_session(CONTENT)

        view = session.apply_cheat("district")

        self.assertEqual("DISTRICT_HUB", session.state.scene_id)
        self.assertTrue(session.state.flags["world.free_roam_unlocked"])
        self.assertEqual("The District Opens Up", view["scene"]["title"])
        node_ids = {node["id"] for node in view["map"]["nodes"]}
        self.assertIn("DISTRICT_ARCHIVE", node_ids)
        self.assertIn("WORKSHOP_ROW", node_ids)
