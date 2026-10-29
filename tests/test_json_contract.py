"""Regression coverage for the shared authored-content/save JSON decoder."""

import unittest

from textrpg.json_contract import loads_strict_json


class StrictJsonObjectKeysTests(unittest.TestCase):
    def test_duplicate_root_key_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate JSON object key"):
            loads_strict_json('{"seed":"first","seed":"second"}')

    def test_nested_duplicate_key_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate JSON object key"):
            loads_strict_json('{"player":{"flags":{"VISIBLE":false,"VISIBLE":true}}}')

    def test_escaped_alias_is_detected_as_duplicate(self):
        # JSON unescaping happens before object_pairs_hook receives keys.
        with self.assertRaisesRegex(ValueError, "Duplicate JSON object key"):
            loads_strict_json('{"scene_id":"A","scene\\u005fid":"B"}')

    def test_duplicate_names_in_different_objects_are_allowed(self):
        result = loads_strict_json('{"left":{"id":"A"},"right":{"id":"B"}}')
        self.assertEqual(result, {"left": {"id": "A"}, "right": {"id": "B"}})

    def test_regular_numbers_and_objects_still_decode(self):
        result = loads_strict_json('{"schema_version":1,"flags":{"F":true},"value":2.5}')
        self.assertEqual(result, {"schema_version": 1, "flags": {"F": True}, "value": 2.5})


if __name__ == "__main__":
    unittest.main()
