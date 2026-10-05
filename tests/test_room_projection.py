from __future__ import annotations
import unittest
from textrpg.room_projection import RoomProjectionError, build_room_projection

class RoomProjectionTests(unittest.TestCase):
    def test_projects_only_player_safe_actor_fields(self):
        scene = {"actors": [{
            "presentation_id": "NPC_TAMSIN",
            "actor_id": "NPC_TAMSIN",
            "public_name": "Tamsin",
            "visual_family": "NPC_TAMSIN",
            "placement_key": "PLATFORM_NINE_TAMSIN_RIGHT",
            "pose_key": "front",
            "inspectable": True,
            "private_note": "must not cross bridge",
        }]}
        room = build_room_projection(scene, location_id="PLATFORM_NINE")
        self.assertEqual(1, room["projection_version"])
        self.assertEqual("PLATFORM_NINE", room["location_id"])
        self.assertEqual([{
            "presentation_id": "NPC_TAMSIN",
            "known_actor_id": "NPC_TAMSIN",
            "display_name": "Tamsin",
            "visual_family": "NPC_TAMSIN",
            "placement_key": "PLATFORM_NINE_TAMSIN_RIGHT",
            "pose_key": "front",
            "outfit_key": None,
            "visible_tags": [],
            "inspectable": True,
            "dialogue_available": False,
            "actions": [],
        }], room["actors"])
        self.assertNotIn("private_note", room["actors"][0])

    def test_rejects_duplicate_presentation_ids(self):
        actor = {
            "presentation_id": "SUPPORT_COURIER_01",
            "public_name": "Wounded courier",
            "visual_family": "SUPPORT_COURIER_01",
            "placement_key": "PLATFORM_NINE_COURIER_LEFT",
        }
        with self.assertRaises(RoomProjectionError):
            build_room_projection({"actors": [actor, dict(actor)]}, location_id="PLATFORM_NINE")

    def test_rejects_raw_pixel_coordinates(self):
        actor = {
            "presentation_id": "NPC_TAMSIN",
            "public_name": "Tamsin",
            "visual_family": "NPC_TAMSIN",
            "placement_key": "PLATFORM_NINE_TAMSIN_RIGHT",
            "x": 62,
        }
        with self.assertRaises(RoomProjectionError):
            build_room_projection({"actors": [actor]}, location_id="PLATFORM_NINE")

    def test_missing_actor_list_is_empty_migration_compatible_room(self):
        self.assertEqual({
            "projection_version": 1,
            "location_id": "PLATFORM_NINE",
            "actors": [],
            "active_speaker_presentation_id": None,
        }, build_room_projection({}, location_id="PLATFORM_NINE"))

if __name__ == "__main__":
    unittest.main()
