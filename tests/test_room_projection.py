from __future__ import annotations

import unittest

from textrpg.core import RuleError
from textrpg.room_projection import build_room_projection


def _tamsin() -> dict:
    return {
        "presentation_id": "NPC_TAMSIN",
        "actor_id": "NPC_TAMSIN",
        "public_name": "Tamsin",
        "visual_family": "NPC_TAMSIN",
        "placement_key": "PLATFORM_NINE_TAMSIN_RIGHT",
        "pose_key": "front",
        "outfit_key": "default",
        "visible_tags": [],
        "inspectable": True,
        "dialogue_available": False,
        "actions": [],
    }


class RoomProjectionTests(unittest.TestCase):
    def test_room_projection_is_versioned_detached_and_player_safe(self) -> None:
        scene = {"location_id": "PLATFORM_NINE", "actors": [_tamsin()]}

        projected = build_room_projection(scene, "PLATFORM_NINE")

        self.assertEqual(
            projected,
            {
                "projection_version": 1,
                "location_id": "PLATFORM_NINE",
                "actors": [
                    {
                        "presentation_id": "NPC_TAMSIN",
                        "known_actor_id": "NPC_TAMSIN",
                        "display_name": "Tamsin",
                        "visual_family": "NPC_TAMSIN",
                        "placement_key": "PLATFORM_NINE_TAMSIN_RIGHT",
                        "pose_key": "front",
                        "outfit_key": "default",
                        "visible_tags": [],
                        "inspectable": True,
                        "dialogue_available": False,
                        "actions": [],
                    }
                ],
                "active_speaker_presentation_id": None,
            },
        )
        scene["actors"][0]["public_name"] = "Changed later"
        self.assertEqual(projected["actors"][0]["display_name"], "Tamsin")

    def test_room_projection_orders_presentations_deterministically(self) -> None:
        tamsin = _tamsin()
        courier = {
            "presentation_id": "SUPPORT_WOUNDED_COURIER",
            "public_name": "Wounded courier",
            "visual_family": "SUPPORT_WOUNDED_COURIER",
            "placement_key": "PLATFORM_NINE_COURIER_LEFT",
        }

        projected = build_room_projection(
            {"location_id": "PLATFORM_NINE", "actors": [tamsin, courier]},
            "PLATFORM_NINE",
        )

        self.assertEqual(
            [actor["presentation_id"] for actor in projected["actors"]],
            ["NPC_TAMSIN", "SUPPORT_WOUNDED_COURIER"],
        )

    def test_room_projection_rejects_duplicate_presentations(self) -> None:
        scene = {"location_id": "PLATFORM_NINE", "actors": [_tamsin(), _tamsin()]}

        with self.assertRaisesRegex(RuleError, "duplicate room actor presentation_id"):
            build_room_projection(scene, "PLATFORM_NINE")

    def test_room_projection_rejects_location_mismatch(self) -> None:
        with self.assertRaisesRegex(RuleError, "location does not match"):
            build_room_projection(
                {"location_id": "PLATFORM_NINE", "actors": []},
                "SERVICE_TUNNEL",
            )

    def test_room_projection_rejects_private_or_presentation_only_fields(self) -> None:
        for forbidden_field in (
            "personality",
            "knowledge",
            "memories",
            "goals",
            "story_state",
            "x",
            "y",
        ):
            with self.subTest(forbidden_field=forbidden_field):
                actor = _tamsin()
                actor[forbidden_field] = (
                    {} if forbidden_field not in {"x", "y"} else 12
                )

                with self.assertRaisesRegex(RuleError, "unsupported fields"):
                    build_room_projection(
                        {"location_id": "PLATFORM_NINE", "actors": [actor]},
                        "PLATFORM_NINE",
                    )

    def test_room_projection_rejects_malformed_actor_contract(self) -> None:
        actor = _tamsin()
        actor["inspectable"] = "yes"

        with self.assertRaisesRegex(RuleError, "inspectable must be boolean"):
            build_room_projection(
                {"location_id": "PLATFORM_NINE", "actors": [actor]},
                "PLATFORM_NINE",
            )


if __name__ == "__main__":
    unittest.main()
