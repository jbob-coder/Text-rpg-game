from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from textrpg.android_bridge import AndroidBridgeError, create_session


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "vertical_slice_01.json"


def item_quantity(view: dict, item_id: str) -> int:
    return next(
        (
            item["quantity"]
            for item in view["inventory"]["items"]
            if item["id"] == item_id
        ),
        0,
    )


def equipment_slot(view: dict, slot: str) -> dict:
    return next(
        entry
        for entry in view["inventory"]["equipment"]
        if entry["slot"] == slot
    )


class Phase1InventoryEquipmentProofTests(unittest.TestCase):
    def test_gate_twelve_inventory_equipment_story_and_save_loop(self) -> None:
        with TemporaryDirectory() as directory:
            save_path = Path(directory) / "phase1-items.json"
            session = create_session(CONTENT, save_path=save_path)

            initial = session.scene_view()
            self.assertEqual(1, item_quantity(initial, "ITEM_MAINTENANCE_SEAL"))
            self.assertEqual(1, item_quantity(initial, "ITEM_DEPOT_JACKET"))
            self.assertEqual(1, item_quantity(initial, "ITEM_WORK_GLOVES"))
            self.assertEqual(1, item_quantity(initial, "ITEM_SIGNAL_RING"))
            self.assertEqual(1, item_quantity(initial, "ITEM_COURIER_NECKTAG"))
            self.assertEqual(0, item_quantity(initial, "ITEM_DEAD_RELAY"))
            self.assertFalse(equipment_slot(initial, "body")["equipped"])

            equipped = session.equip("ITEM_DEPOT_JACKET")
            self.assertEqual(0, item_quantity(equipped, "ITEM_DEPOT_JACKET"))
            body = equipment_slot(equipped, "body")
            self.assertTrue(body["equipped"])
            self.assertEqual("ITEM_DEPOT_JACKET", body["item_id"])
            self.assertEqual("standard", body["quality"])

            endurance = session.inspect_status("attributes.endurance")
            self.assertEqual(37.0, endurance["total"])
            self.assertEqual(35.0, endurance["breakdown"]["base"])
            self.assertEqual(2.0, endurance["breakdown"]["equipment:body"])

            session.save()
            restored = create_session(CONTENT, save_path=save_path)
            loaded = restored.load()
            self.assertEqual(0, item_quantity(loaded, "ITEM_DEPOT_JACKET"))
            self.assertEqual("ITEM_DEPOT_JACKET", equipment_slot(loaded, "body")["item_id"])
            self.assertEqual(37.0, restored.inspect_status("attributes.endurance")["total"])

            unequipped = restored.unequip("body")
            self.assertEqual(1, item_quantity(unequipped, "ITEM_DEPOT_JACKET"))
            self.assertFalse(equipment_slot(unequipped, "body")["equipped"])
            self.assertEqual(35.0, restored.inspect_status("attributes.endurance")["total"])

            acquired = restored.choose("TAKE_DEAD_RELAY")
            self.assertEqual(1, item_quantity(acquired, "ITEM_DEAD_RELAY"))
            self.assertEqual(1, item_quantity(acquired, "ITEM_MAINTENANCE_SEAL"))
            self.assertEqual("intact", acquired["visuals"]["relay_state"])

            opened = restored.choose("USE_MAINTENANCE_SEAL")
            self.assertEqual(1, item_quantity(opened, "ITEM_DEAD_RELAY"))
            self.assertEqual(0, item_quantity(opened, "ITEM_MAINTENANCE_SEAL"))
            self.assertEqual("opened", opened["visuals"]["relay_state"])
            self.assertNotIn("ITEM_MAINTENANCE_SEAL", restored.state.inventory)

            restored.save()
            final_session = create_session(CONTENT, save_path=save_path)
            final_view = final_session.load()
            self.assertEqual(1, item_quantity(final_view, "ITEM_DEAD_RELAY"))
            self.assertEqual(0, item_quantity(final_view, "ITEM_MAINTENANCE_SEAL"))
            self.assertEqual(1, item_quantity(final_view, "ITEM_DEPOT_JACKET"))
            self.assertFalse(equipment_slot(final_view, "body")["equipped"])
            self.assertEqual("opened", final_view["visuals"]["relay_state"])

    def test_failed_equipment_actions_do_not_partially_mutate_state(self) -> None:
        session = create_session(CONTENT)
        session.equip("ITEM_DEPOT_JACKET")
        before = deepcopy(session.state.snapshot())

        with self.assertRaises(AndroidBridgeError) as missing_item:
            session.equip("ITEM_DOES_NOT_EXIST")
        self.assertEqual("EQUIP_ERROR", missing_item.exception.code)
        self.assertEqual(before, session.state.snapshot())

        with self.assertRaises(AndroidBridgeError) as empty_slot:
            session.unequip("ring_2")
        self.assertEqual("EQUIP_ERROR", empty_slot.exception.code)
        self.assertEqual(before, session.state.snapshot())


if __name__ == "__main__":
    unittest.main()
