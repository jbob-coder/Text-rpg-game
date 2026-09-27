import copy
import json
import unittest
from pathlib import Path

from textrpg import RuleError, content_pack_from_mapping, load_content_pack


ROOT = Path(__file__).resolve().parents[1]
SLICE = ROOT / "content" / "vertical_slice_01.json"


class ContentPackTests(unittest.TestCase):
    def data(self):
        return json.loads(SLICE.read_text(encoding="utf-8"))

    def test_load_vertical_slice_builds_state_and_engine(self):
        pack = load_content_pack(SLICE)
        self.assertEqual(pack.content_id, "CONTENT_VERTICAL_SLICE_01")
        self.assertEqual(pack.canon_status, "provisional_canon")
        self.assertEqual(pack.state.scene_id, "OPENING_DEPOT_BLACKOUT")
        choices = {choice["id"] for choice in pack.engine.available_choices(pack.state)}
        self.assertIn("TAKE_DEAD_RELAY", choices)
        self.assertIn("ABILITY_TRACE_ECHO", pack.engine.power_definitions)

    def test_unknown_initial_scene_is_rejected(self):
        data = self.data()
        data["initial_state"]["scene_id"] = "SCENE_MISSING"
        with self.assertRaises(RuleError):
            content_pack_from_mapping(data)

    def test_invalid_initial_attribute_is_rejected(self):
        data = self.data()
        data["initial_state"]["player"]["attributes"]["might"] = 150
        with self.assertRaises(RuleError):
            content_pack_from_mapping(data)

    def test_invalid_character_visual_record_is_rejected(self):
        data = self.data()
        del data["characters"]["NPC_TAMSIN"]["hair"]
        with self.assertRaises(RuleError):
            content_pack_from_mapping(data)

    def test_unknown_initial_state_field_is_rejected(self):
        data = self.data()
        data["initial_state"]["mystery_runtime_field"] = True
        with self.assertRaises(RuleError):
            content_pack_from_mapping(data)


if __name__ == "__main__":
    unittest.main()
