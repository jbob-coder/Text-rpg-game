"""Equipment activation must honor the authored item schema before mutations."""

import unittest
from copy import deepcopy

from textrpg import GameState, RuleError
from textrpg.equipment import equip_item, validate_item_definition


class EquipmentDefinitionRuntimeContractTests(unittest.TestCase):
    def test_equip_rejects_malformed_authored_metadata_atomically(self):
        malformed = [
            ("quality", [], "quality"),
            ("source", {}, "source"),
            ("active_ability", [], "active_ability"),
            ("label", 7, "label"),
        ]
        for field, value, description in malformed:
            with self.subTest(field=field):
                state = GameState(
                    seed="equip-validation",
                    scene_id="SCENE_A",
                    inventory={"ITEM_BAD": 1},
                )
                before = deepcopy(state.snapshot())
                item = {"item_id": "ITEM_BAD", "slot": "body", field: value}

                with self.assertRaisesRegex(RuleError, description):
                    validate_item_definition(item["item_id"], item)
                with self.assertRaisesRegex(RuleError, description):
                    equip_item(state, item, consume_inventory=True)

                self.assertEqual(state.snapshot(), before)

    def test_equip_accepts_valid_definition_and_consumes_one_item(self):
        state = GameState(
            seed="equip-validation",
            scene_id="SCENE_A",
            inventory={"ITEM_VALID": 2},
        )
        item = {
            "item_id": "ITEM_VALID",
            "slot": "body",
            "quality": "standard",
            "source": "quest",
            "label": "Protective vest",
            "active_ability": "ABILITY_TRACE",
        }
        validate_item_definition(item["item_id"], item)
        previous = equip_item(state, item, consume_inventory=True)

        self.assertIsNone(previous)
        self.assertEqual(state.inventory, {"ITEM_VALID": 1})
        self.assertEqual(state.equipment["body"]["quality"], "standard")
        self.assertEqual(state.equipment["body"]["source"], "quest")
        self.assertEqual(state.equipment["body"]["active_ability"], "ABILITY_TRACE")


if __name__ == "__main__":
    unittest.main()
