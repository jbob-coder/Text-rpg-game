import copy
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from threading import Barrier
from unittest import mock

from textrpg import GameState, RuleError, dumps_state, load_state, loads_state, save_state


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

    def test_two_simultaneous_saves_use_distinct_temporary_files(self):
        # Force both writes to reach replace() together. With the former fixed
        # save.json.tmp path one replacement consumes the other's source.
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "save.json"
            states = (
                GameState(seed="first", scene_id="SCENE_A"),
                GameState(seed="second", scene_id="SCENE_A"),
            )
            barrier = Barrier(2)
            real_replace = Path.replace

            def synchronized_replace(source, destination):
                barrier.wait(timeout=10)
                return real_replace(source, destination)

            with mock.patch.object(
                Path, "replace", autospec=True, side_effect=synchronized_replace
            ):
                with ThreadPoolExecutor(max_workers=2) as pool:
                    list(pool.map(lambda state: save_state(path, state), states))

            self.assertIn(load_state(path).seed, {"first", "second"})
            self.assertEqual([file.name for file in Path(directory).iterdir()], ["save.json"])

    def test_failed_replace_preserves_previous_save_and_cleans_temp(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "save.json"
            save_state(path, GameState(seed="original", scene_id="SCENE_A"))
            old_bytes = path.read_bytes()

            with mock.patch.object(
                Path, "replace", autospec=True, side_effect=OSError("replace refused")
            ):
                with self.assertRaisesRegex(OSError, "replace refused"):
                    save_state(path, GameState(seed="replacement", scene_id="SCENE_A"))

            self.assertEqual(path.read_bytes(), old_bytes)
            self.assertEqual(sorted(file.name for file in Path(directory).iterdir()), ["save.json"])

    def test_invalid_save_state_does_not_create_save_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory) / "new" / "nested"
            path = parent / "save.json"
            invalid = GameState(seed="invalid", scene_id="SCENE_A", schema_version=99)

            with self.assertRaisesRegex(RuleError, "schema"):
                save_state(path, invalid)
            self.assertFalse(parent.exists())

    def test_loading_missing_save_returns_rule_error(self):
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing.json"
            with self.assertRaisesRegex(RuleError, "Could not read save file"):
                load_state(missing)

    def test_loading_permission_denied_returns_rule_error(self):
        with mock.patch.object(
            Path, "read_text", autospec=True, side_effect=PermissionError("permission denied")
        ):
            with self.assertRaisesRegex(RuleError, "permission denied"):
                load_state("protected.json")

    def test_loading_non_utf8_save_returns_rule_error(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid-utf8.json"
            path.write_bytes(b"\\xff")
            with self.assertRaisesRegex(RuleError, "Could not read save file"):
                load_state(path)

if __name__ == "__main__":
    unittest.main()
