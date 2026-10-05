from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from textrpg import RuleError, content_pack_from_mapping, loads_state
from textrpg.android_bridge import AndroidBridgeError, open_android_session


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "vertical_slice_01.json"


def content_data() -> dict:
    return json.loads(CONTENT.read_text(encoding="utf-8"))


def find_choice(data: dict, choice_id: str) -> dict:
    for scene in data["scenes"].values():
        for choice in scene.get("choices", []):
            if choice.get("id") == choice_id:
                return choice
    raise AssertionError(f"choice not found: {choice_id}")


class Phase1InventoryEquipmentProofTests(unittest.TestCase):
    def test_initial_inventory_quantities_must_be_positive_integers(self) -> None:
        for invalid in (0, -1, True, 1.5, "1"):
            with self.subTest(invalid=invalid):
                data = content_data()
                data["initial_state"]["inventory"]["ITEM_MAINTENANCE_SEAL"] = invalid
                with self.assertRaises(RuleError):
                    content_pack_from_mapping(data)

    def test_item_gate_and_inventory_effect_quantities_are_validated(self) -> None:
        gate_data = content_data()
        seal_choice = find_choice(gate_data, "USE_MAINTENANCE_SEAL")
        item_gate = next(
            condition
            for condition in seal_choice["requires"]
            if condition.get("type") == "item_min"
        )
        item_gate["quantity"] = 0
        with self.assertRaisesRegex(RuleError, "positive integer"):
            content_pack_from_mapping(gate_data)

        effect_data = content_data()
        relay_choice = find_choice(effect_data, "TAKE_DEAD_RELAY")
        inventory_effect = next(
            effect
            for effect in relay_choice["outcomes"]["default"]["effects"]
            if effect.get("type") == "inventory"
        )
        inventory_effect["quantity"] = 0
        with self.assertRaisesRegex(RuleError, "non-zero integer"):
            content_pack_from_mapping(effect_data)

    def test_equipment_item_definition_is_validated_during_content_load(self) -> None:
        data = content_data()
        data["registries"]["items"]["ITEM_DEPOT_JACKET"]["slot"] = "helmet"
        with self.assertRaisesRegex(RuleError, "Unsupported equipment slot"):
            content_pack_from_mapping(data)

    def test_persistence_rejects_corrupt_inventory_and_equipment_entries(self) -> None:
        bad_inventory = json.dumps(
            {
                "schema_version": 1,
                "seed": "s",
                "scene_id": "A",
                "inventory": {"ITEM_X": -1},
            }
        )
        with self.assertRaisesRegex(RuleError, "positive integers"):
            loads_state(bad_inventory)

        bad_equipment = json.dumps(
            {
                "schema_version": 1,
                "seed": "s",
                "scene_id": "A",
                "equipment": {
                    "body": {
                        "item_id": "ITEM_X",
                        "slot": "hands",
                    }
                },
            }
        )
        with self.assertRaisesRegex(RuleError, "must match"):
            loads_state(bad_equipment)

    def test_phase1_item_equipment_story_loop_survives_two_save_boundaries(self) -> None:
        with TemporaryDirectory() as directory:
            save_path = Path(directory) / "phase1-items.json"
            session = open_android_session(CONTENT, save_path=save_path)

            starting = {
                item["id"]: item["quantity"]
                for item in session.scene_view()["inventory"]["items"]
            }
            self.assertEqual(
                {
                    "ITEM_COURIER_NECKTAG": 1,
                    "ITEM_DEPOT_JACKET": 1,
                    "ITEM_MAINTENANCE_SEAL": 1,
                    "ITEM_SIGNAL_RING": 1,
                    "ITEM_WORK_GLOVES": 1,
                },
                starting,
            )

            equipped = session.equip("ITEM_DEPOT_JACKET")
            body = next(
                slot
                for slot in equipped["inventory"]["equipment"]
                if slot["slot"] == "body"
            )
            self.assertTrue(body["equipped"])
            self.assertEqual("ITEM_DEPOT_JACKET", body["item_id"])
            self.assertNotIn(
                "ITEM_DEPOT_JACKET",
                {item["id"] for item in equipped["inventory"]["items"]},
            )
            endurance = session.inspect_status("attributes.endurance")
            self.assertEqual(37.0, endurance["total"])
            self.assertEqual(2.0, endurance["breakdown"]["equipment:body"])

            session.save()
            restored = open_android_session(CONTENT, save_path=save_path)
            restored.load()
            restored_body = next(
                slot
                for slot in restored.scene_view()["inventory"]["equipment"]
                if slot["slot"] == "body"
            )
            self.assertTrue(restored_body["equipped"])
            self.assertEqual("ITEM_DEPOT_JACKET", restored_body["item_id"])
            self.assertEqual(
                37.0,
                restored.inspect_status("attributes.endurance")["total"],
            )

            after_relay = restored.choose("TAKE_DEAD_RELAY")
            relay = next(
                item
                for item in after_relay["inventory"]["items"]
                if item["id"] == "ITEM_DEAD_RELAY"
            )
            self.assertEqual(1, relay["quantity"])
            self.assertEqual("intact", after_relay["visuals"]["relay_state"])

            after_seal = restored.choose("USE_MAINTENANCE_SEAL")
            ids = {item["id"] for item in after_seal["inventory"]["items"]}
            self.assertNotIn("ITEM_MAINTENANCE_SEAL", ids)
            self.assertIn("ITEM_DEAD_RELAY", ids)
            self.assertEqual("opened", after_seal["visuals"]["relay_state"])

            restored.save()
            final_session = open_android_session(CONTENT, save_path=save_path)
            final_view = final_session.load()
            final_ids = {item["id"] for item in final_view["inventory"]["items"]}
            self.assertNotIn("ITEM_MAINTENANCE_SEAL", final_ids)
            self.assertIn("ITEM_DEAD_RELAY", final_ids)
            final_body = next(
                slot
                for slot in final_view["inventory"]["equipment"]
                if slot["slot"] == "body"
            )
            self.assertTrue(final_body["equipped"])
            self.assertEqual("ITEM_DEPOT_JACKET", final_body["item_id"])
            self.assertEqual("opened", final_view["visuals"]["relay_state"])

    def test_failed_equip_restores_full_authoritative_state(self) -> None:
        session = open_android_session(CONTENT)
        before = deepcopy(session.state.snapshot())
        session.content.registries["items"]["ITEM_DEPOT_JACKET"]["requirements"] = {
            "attributes": {"might": 999}
        }

        with self.assertRaises(AndroidBridgeError):
            session.equip("ITEM_DEPOT_JACKET")

        self.assertEqual(before, session.state.snapshot())


if __name__ == "__main__":
    unittest.main()
