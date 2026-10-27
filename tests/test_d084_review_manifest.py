"""Negative regressions for D-084's *review-only*, never runtime, lore contract."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.validate_d084_review_manifest import MANIFEST, load_json, validate


MINIMAL_CURRENT_SLICE = {
    "content_id": "CONTENT_VERTICAL_SLICE_01",
    "canon_status": "provisional_canon",
    "initial_state": {
        "npcs": {"NPC_TAMSIN": {
            "knowledge": {}, "memories": [], "goals": {}, "story_state": {}
        }},
        "relationships": {"NPC_TAMSIN": {"trust": 15}},
    },
}


class D084ReviewManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.contract = load_json(MANIFEST)
        self.slice = deepcopy(MINIMAL_CURRENT_SLICE)

    def assert_rejected(self, expected: str) -> None:
        failures = validate(self.contract, self.slice)
        self.assertTrue(any(expected in error for error in failures), failures)

    def test_fresh_manifest_passes_nonruntime_review(self):
        self.assertEqual([], validate(self.contract, self.slice))

    def test_review_gate_never_mutates_input(self):
        manifest = deepcopy(self.contract)
        slice_content = deepcopy(self.slice)
        validate(self.contract, self.slice)
        self.assertEqual(manifest, self.contract)
        self.assertEqual(slice_content, self.slice)

    def test_h36_phase_does_not_drop_invaders(self):
        self.contract["initial_burst"]["members"].remove("INTELLIGENT_INVADERS_ARRIVE")
        self.assert_rejected("exactly five distinct")

    def test_h36_cannot_duplicate_one_member_for_two_events(self):
        burst = self.contract["initial_burst"]["members"]
        burst[-1] = burst[0]
        self.assert_rejected("exactly five distinct")

    def test_no_fake_same_second_claim(self):
        self.contract["initial_burst"]["temporal_relation"] = "SAME_SECOND"
        self.assert_rejected("micro-order")

    def test_first_forging_is_not_prewar_by_assumption(self):
        self.contract["unresolved"]["first_crystal_forging_relative_to_war"] = "BEFORE_WAR"
        self.assert_rejected("first forge timing")

    def test_previously_misread_ac_cannot_return(self):
        self.contract["calendar"]["ac_definition"] = "After Crystal"
        self.assert_rejected("Antes del Crystal")

    def test_2670_atlas_must_not_be_automatically_imported(self):
        self.contract["historical_sources"][0]["adopted_into_current_canon"] = True
        self.assert_rejected("old 2670 campaign")

    def test_absolute_date_is_unverified(self):
        self.contract["relative_events"][0]["absolute_date"] = 2645
        self.assert_rejected("absolute historical years")

    def test_nov_xii_must_be_qualified(self):
        self.contract["editorial"]["chapter_xii_id"] = "NOV-XII"
        self.assert_rejected("unqualified NOV-XII")

    def test_dr06_proposal_cannot_become_historical_event(self):
        self.contract["editorial"]["dr06_is_historical_event"] = True
        self.assert_rejected("DR-06 remains")

    def test_npc_cannot_inherit_omniscient_author_truth(self):
        self.contract["knowledge_boundary"]["initial_npc_knowledge"] = "AUTO_GRANTED"
        self.assert_rejected("granted to NPC/player")

    def test_android_must_not_receive_raw_npc_state(self):
        self.contract["knowledge_boundary"]["android_raw_npc_state_allowed"] = True
        self.assert_rejected("privacy and discovery")

    def test_game_content_stays_provisional(self):
        self.slice["canon_status"] = "canon"
        self.assert_rejected("current slice baseline changed")

    def test_private_social_state_paths_are_preserved(self):
        self.contract["gameplay_boundary"]["protect_state_paths"].remove("state.npcs[*].knowledge")
        self.assert_rejected("state owners must be separate")

    def test_duplicate_json_keys_fail_closed(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "duplicates.json"
            path.write_text('{"schema_version":1,"schema_version":2}', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
                load_json(path)


if __name__ == "__main__":
    unittest.main()
