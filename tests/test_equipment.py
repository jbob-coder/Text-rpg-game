import unittest

from textrpg import GameState, RuleError
from textrpg.equipment import active_set_bonuses, equip_item, equipment_modifiers, set_counts


class EquipmentTests(unittest.TestCase):
    def test_requirements_and_set_bonus(self):
        state = GameState(
            seed="s",
            scene_id="A",
            player={"attributes": {"might": 30}, "skills": {"blades": 20}},
        )
        armor = {
            "item_id": "ITEM_A",
            "slot": "body",
            "requirements": {"attributes": {"might": 20}},
            "modifiers": {"attributes.endurance": 3},
            "set_id": "SET_RANGER",
        }
        gloves = {
            "item_id": "ITEM_B",
            "slot": "hands",
            "modifiers": {"skills.ranged": 2},
            "set_id": "SET_RANGER",
        }
        equip_item(state, armor)
        equip_item(state, gloves)
        self.assertEqual(set_counts(state), {"SET_RANGER": 2})

        definitions = {
            "SET_RANGER": {
                "thresholds": {"2": {"modifiers": {"attributes.perception": 4}}}
            }
        }
        self.assertIn("SET_RANGER:2", active_set_bonuses(state, definitions))
        self.assertEqual(equipment_modifiers(state, definitions)["attributes.perception"], 4)

    def test_requirement_failure(self):
        state = GameState(seed="s", scene_id="A", player={"attributes": {"might": 1}})
        with self.assertRaises(RuleError):
            equip_item(
                state,
                {
                    "item_id": "ITEM_X",
                    "slot": "body",
                    "requirements": {"attributes": {"might": 10}},
                },
            )


if __name__ == "__main__":
    unittest.main()
