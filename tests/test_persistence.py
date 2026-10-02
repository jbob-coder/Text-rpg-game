import copy
import tempfile
import unittest
from pathlib import Path

from textrpg import GameState, RuleError, dumps_state, loads_state, save_state


class PersistenceTests(unittest.TestCase):
    def test_saving_incompatible_schema_preserves_state_and_existing_save(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "save.json"
            original = GameState(seed="s", scene_id="SCENE_A")
            save_state(path, original)
            original_bytes = path.read_bytes()
            for version in (0, 2):
                with self.subTest(version=version):
                    state = GameState(seed="s", scene_id="SCENE_A", schema_version=version)
                    before = copy.deepcopy(state.snapshot())
                    with self.assertRaisesRegex(RuleError, "schema"):
                        dumps_state(state)
                    with self.assertRaisesRegex(RuleError, "schema"):
                        save_state(path, state)
                    self.assertEqual(state.snapshot(), before)
                    self.assertEqual(path.read_bytes(), original_bytes)

    def test_load_rejects_non_finite_numbers_in_arbitrary_metadata(self):
        for token in ("NaN", "Infinity", "-Infinity", "1e400", "-1e400"):
            with self.subTest(token=token):
                raw = '{"schema_version":1,"seed":"s","scene_id":"A","flags":{"probe":' + token + '}}'
                with self.assertRaisesRegex(RuleError, "strict JSON"):
                    loads_state(raw)

    def test_round_trip_preserves_extended_state(self):
        state = GameState(
            seed="save-seed",
            scene_id="SCENE_1",
            party=["NPC_A"],
            abilities={"ABILITY_X": {"rank": 1, "mastery_xp": 120}},
            perks={"PERK_X": {"source": "training"}},
        )
        loaded = loads_state(dumps_state(state))
        self.assertEqual(loaded.snapshot(), state.snapshot())

    def test_unknown_schema_is_rejected(self):
        raw = '{"schema_version":999,"seed":"x","scene_id":"A"}'
        with self.assertRaises(RuleError):
            loads_state(raw)


    def test_round_trip_preserves_ability_discovery_and_visibility_state(self):
        state = GameState(
            seed="ability-save",
            scene_id="SCENE_A",
            abilities={
                "ABILITY_FLUX": {
                    "rank": 2,
                    "mastery_xp": 350.0,
                    "mastery_stage": "mastered",
                    "control": 12.0,
                    "efficiency": 8.0,
                    "techniques": {
                        "TECHNIQUE_PULSE": {
                            "mastery_xp": 40.0,
                            "stage": "learned",
                            "uses": 4,
                            "ready_at_minutes": 120,
                            "discovered_at_minutes": 10,
                        }
                    },
                    "evolution_visibility": {
                        "EVOLUTION_STABLE": {
                            "state": "partial",
                            "hint": "A stable pattern is required.",
                            "known_requirements": ["mastery"],
                        }
                    },
                    "evolutions": [],
                }
            },
        )
        loaded = loads_state(dumps_state(state))
        self.assertEqual(loaded.abilities, state.abilities)


    def test_non_object_save_payload_is_rejected(self):
        with self.assertRaises(RuleError):
            loads_state("[]")

    def test_invalid_json_is_wrapped_as_rule_error(self):
        with self.assertRaises(RuleError):
            loads_state("{not-json")

    def test_boolean_schema_version_is_rejected(self):
        raw = '{"schema_version":true,"seed":"x","scene_id":"A"}'
        with self.assertRaises(RuleError):
            loads_state(raw)

    def test_unknown_current_schema_field_is_rejected_instead_of_dropped(self):
        raw = (
            '{"schema_version":1,"seed":"x","scene_id":"A",'
            '"future_field":{"value":1}}'
        )
        with self.assertRaises(RuleError):
            loads_state(raw)

    def test_required_identity_fields_must_be_non_empty_strings(self):
        with self.assertRaises(RuleError):
            loads_state('{"schema_version":1,"seed":"","scene_id":"A"}')
        with self.assertRaises(RuleError):
            loads_state('{"schema_version":1,"seed":"x","scene_id":3}')



    def test_corrupt_nested_state_container_is_rejected_on_load(self):
        raw = (
            '{"schema_version":1,"seed":"x","scene_id":"A",'
            '"player":[]}'
        )
        with self.assertRaises(RuleError):
            loads_state(raw)

    def test_corrupt_party_entries_are_rejected_on_load(self):
        raw = (
            '{"schema_version":1,"seed":"x","scene_id":"A",'
            '"party":["NPC_A",3]}'
        )
        with self.assertRaises(RuleError):
            loads_state(raw)

    def test_dumps_state_rejects_corrupt_runtime_structure(self):
        state = GameState(seed="x", scene_id="A")
        state.history = ["not-an-event"]
        with self.assertRaises(RuleError):
            dumps_state(state)

    def test_non_finite_json_numbers_are_rejected_at_persistence_boundary(self):
        raw = (
            '{"schema_version":1,"seed":"x","scene_id":"A",'
            '"player":{"attributes":{"might":NaN}}}'
        )
        with self.assertRaises(RuleError):
            loads_state(raw)

        state = GameState(seed="x", scene_id="A")
        state.player["attributes"] = {"might": float("inf")}
        with self.assertRaises(RuleError):
            dumps_state(state)

    def test_non_json_serializable_nested_state_is_wrapped_as_rule_error(self):
        state = GameState(seed="x", scene_id="A")
        state.player["debug_values"] = {"not", "json"}
        with self.assertRaises(RuleError):
            dumps_state(state)

if __name__ == "__main__":
    unittest.main()
