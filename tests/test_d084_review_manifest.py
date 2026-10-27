"""Negative regressions for D-084's *review-only*, never runtime, lore contract."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.validate_d084_review_manifest import MANIFEST, SLICE, load_json, validate


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

    def test_real_authority_slice_passes_current_nonruntime_guard(self):
        """CI must inspect the actual, entire content pack, not only a small fixture."""
        real_slice = load_json(SLICE)
        self.assertEqual([], validate(self.contract, real_slice))

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

    def test_rejects_new_unreviewed_editorial_field(self):
        self.contract["knowledge_boundary"]["initial_player_secret_payload"] = "SYSTEM_TABLET_EXISTS"
        self.assert_rejected("knowledge_boundary field mismatch")

    def test_rejects_new_runtime_autogrant_field(self):
        self.contract["gameplay_boundary"]["secret_autogrant"] = True
        self.assert_rejected("gameplay_boundary field mismatch")

    def test_rejects_missing_disclosure_gate(self):
        del self.contract["knowledge_boundary"]["requires_authored_discovery_for_runtime"]
        self.assert_rejected("knowledge_boundary field mismatch")

    def test_rejects_added_event_timing_detail(self):
        self.contract["relative_events"][0]["year"] = 2645
        self.assert_rejected("relative_events.FIRST_WAR field mismatch")

    def test_rejects_changed_historical_atlas_dates(self):
        self.contract["historical_sources"][0]["observed_dates"].append("2099")
        self.assert_rejected("old 2670 campaign")

    def test_rejects_mismatched_manuscript_authority(self):
        self.contract["source_authorities"]["manuscript"] = "Volumen I v0.8"
        self.assert_rejected("manuscript authority/version mismatch")

    def test_missing_provenance_list_is_rejected_not_crash(self):
        self.contract["initial_burst"]["source_ids"] = None
        self.assert_rejected("initial_burst.source_ids must be a list")

    def test_missing_war_provenance_list_is_rejected_not_crash(self):
        self.contract["relative_events"][0]["source_ids"] = None
        self.assert_rejected("FIRST_WAR.source_ids must be a list")

    def test_missing_social_state_is_rejected_not_crash(self):
        self.slice["initial_state"] = None
        self.assert_rejected("initial_state must be an object")

    def test_nonobject_npc_is_rejected_not_crash(self):
        self.slice["initial_state"]["npcs"]["NPC_TAMSIN"] = None
        self.assert_rejected("Tamsin social containers changed")

    def test_review_secret_cannot_be_seeded_in_player_knowledge(self):
        self.slice["initial_state"]["knowledge"] = {
            "SYSTEM_TABLET_EXISTS": {"learned": True},
        }
        self.assert_rejected("review-only identifier imported into gameplay content")

    def test_review_secret_cannot_be_seeded_in_npc_knowledge(self):
        self.slice["initial_state"]["npcs"]["NPC_TAMSIN"]["knowledge"][
            "SYSTEM_TABLET_EXISTS"
        ] = {"confidence": 1.0}
        self.assert_rejected("review-only identifier imported into gameplay content")

    def test_review_secret_cannot_leak_in_nested_scene_text(self):
        self.slice["scenes"] = {
            "OPENING": {"dialogue": [{"body": "SYSTEM_TABLET_EXISTS"}]},
        }
        self.assert_rejected("review-only identifier imported into gameplay content")

    def test_all_h36_burst_labels_are_rejected_in_scene_text(self):
        """Do not ship the review graph's H-36 event nodes as gameplay text."""
        for event_id in self.contract["initial_burst"]["members"]:
            with self.subTest(event_id=event_id):
                self.slice["scenes"] = {
                    "OPENING": {"dialogue": [{"body": event_id}]},
                }
                self.assert_rejected("review-only identifier imported into gameplay content")

    def test_all_h36_burst_labels_are_rejected_as_json_keys(self):
        """Recursive scan also catches unapproved event IDs in metadata keys."""
        for event_id in self.contract["initial_burst"]["members"]:
            with self.subTest(event_id=event_id):
                self.slice["scenes"] = {
                    "OPENING": {"flags": {event_id: True}},
                }
                self.assert_rejected("review-only identifier imported into gameplay content")

    def test_review_only_event_id_cannot_become_authored_key(self):
        self.slice["quests"] = [{"FIRST_WAR": {"known": True}}]
        self.assert_rejected("review-only identifier imported into gameplay content")

    def test_malformed_initial_player_knowledge_fails_closed(self):
        self.slice["initial_state"]["knowledge"] = []
        self.assert_rejected("initial player knowledge must be an object")

    def test_malformed_tamsin_knowledge_fails_closed(self):
        self.slice["initial_state"]["npcs"]["NPC_TAMSIN"]["knowledge"] = []
        self.assert_rejected("Tamsin knowledge must retain its original container type")

    def test_malformed_non_tamsin_npc_knowledge_fails_closed(self):
        self.slice["initial_state"]["npcs"]["NPC_OTHER"] = {"knowledge": "all secrets"}
        self.assert_rejected("initial NPC knowledge must be an object")

    def test_duplicate_json_keys_fail_closed(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "duplicates.json"
            path.write_text('{"schema_version":1,"schema_version":2}', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
                load_json(path)


if __name__ == "__main__":
    unittest.main()
