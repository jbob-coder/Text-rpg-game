"""Regression tests for overflow-safe additive modifier calculations."""

import unittest

from textrpg import GameState, effective_player_value, modifier_breakdown
from textrpg.modifiers import (
    condition_modifiers,
    equipment_modifiers,
    modifier_totals,
    perk_modifiers,
    validate_modifier_mapping,
)


PATH = "attributes.might"


def state_with(*, equipment=None, perks=None, conditions=None):
    return GameState(
        seed="modifier-bounds",
        scene_id="SCENE_TEST",
        player={"attributes": {"might": 10}, "conditions": conditions or {}},
        equipment=equipment or {},
        perks=perks or {},
    )


class ModifierNumericBoundsTests(unittest.TestCase):
    def test_oversized_integer_modifier_reports_contract_error(self):
        with self.assertRaisesRegex(ValueError, "Non-finite numeric modifier"):
            validate_modifier_mapping({PATH: 10 ** 400}, source="test")
        with self.assertRaisesRegex(ValueError, "Non-finite numeric modifier"):
            validate_modifier_mapping({PATH: -(10 ** 400)}, source="test")

    def test_finite_individual_equipment_values_must_not_overflow_when_stacked(self):
        equipment = {
            "body": {"modifiers": {PATH: 1e308}},
            "hands": {"modifiers": {PATH: 1e308}},
        }
        state = state_with(equipment=equipment)
        with self.assertRaisesRegex(ValueError, "Non-finite numeric modifier"):
            equipment_modifiers(state)
        with self.assertRaisesRegex(ValueError, "Non-finite numeric modifier"):
            modifier_breakdown(state, PATH)
        with self.assertRaisesRegex(ValueError, "Non-finite numeric modifier"):
            effective_player_value(state, PATH)

    def test_perk_and_condition_stacking_must_stay_finite(self):
        state = state_with(perks={
            "PERK_A": {"modifiers": {PATH: 1e308}},
            "PERK_B": {"modifiers": {PATH: 1e308}},
        })
        with self.assertRaisesRegex(ValueError, "Non-finite numeric modifier"):
            perk_modifiers(state)

        state = state_with(conditions={
            "COND_A": {"modifiers": {PATH: -1e308}},
            "COND_B": {"modifiers": {PATH: -1e308}},
        })
        with self.assertRaisesRegex(ValueError, "Non-finite numeric modifier"):
            condition_modifiers(state)

    def test_cross_source_overflow_is_rejected(self):
        state = state_with(
            equipment={"body": {"modifiers": {PATH: 1e308}}},
            perks={"PERK_A": {"modifiers": {PATH: 1e308}}},
        )
        with self.assertRaisesRegex(ValueError, "Non-finite numeric modifier"):
            modifier_totals(state)

    def test_normal_additive_modifiers_remain_unchanged(self):
        state = state_with(
            equipment={"body": {"modifiers": {PATH: 2}}},
            perks={"PERK_A": {"modifiers": {PATH: 3}}},
            conditions={"COND_A": {"modifiers": {PATH: -1}}},
        )
        self.assertEqual(modifier_totals(state)[PATH], 4.0)
        self.assertEqual(modifier_breakdown(state, PATH)["total"], 14.0)
        self.assertEqual(effective_player_value(state, PATH), 14.0)


if __name__ == "__main__":
    unittest.main()
