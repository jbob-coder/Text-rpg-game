import unittest

from textrpg.beast_voice import available_voice_lines, select_voice_line, validate_voice_profile


class BeastVoiceTests(unittest.TestCase):
    def beast(self, **changes):
        state = {
            "beast_id": "BEAST_WHITE_FANG",
            "species_id": "SPECIES_WOLF",
            "level": 5,
            "development_xp": 400,
            "intelligence_tier": 1,
            "role": "pack_member",
            "follower_count": 0,
            "memories": [],
            "adaptations": [],
        }
        state.update(changes)
        return state

    def memory(self, **changes):
        memory = {
            "memory_id": "MEMORY_PLAYER_1",
            "opponent_id": "PLAYER_1",
            "encounter_count": 1,
            "last_seen_time_minutes": 100,
            "observations": {},
        }
        memory.update(changes)
        return memory

    def profile(self):
        return {
            "lines": [
                {
                    "line_id": "VOICE_GROWL",
                    "text": "A low warning growl.",
                    "min_intelligence_tier": 0,
                    "min_level": 1,
                },
                {
                    "line_id": "VOICE_SIMPLE_THREAT",
                    "text": "Leave my ground.",
                    "min_intelligence_tier": 3,
                    "min_level": 10,
                },
                {
                    "line_id": "VOICE_REMEMBERS_SPEAR",
                    "text": "The spear again. I remember its reach.",
                    "min_intelligence_tier": 3,
                    "min_level": 10,
                    "required_observations": ["OBS_WEAPON_SPEAR"],
                },
                {
                    "line_id": "VOICE_COMMAND_FLANK",
                    "text": "Circle wide. Cut off the retreat.",
                    "min_intelligence_tier": 4,
                    "min_level": 20,
                    "roles": ["commander", "territory_ruler", "regional_apex"],
                },
            ]
        }

    def test_profile_contract_accepts_authored_lines(self):
        self.assertEqual(validate_voice_profile(self.profile()), [])

    def test_low_intelligence_beast_only_receives_simple_line(self):
        lines = available_voice_lines(self.beast(), self.memory(), self.profile())
        self.assertEqual(lines, [{"line_id": "VOICE_GROWL", "text": "A low warning growl."}])

    def test_level_and_intelligence_both_gate_speech_complexity(self):
        smart_but_young = self.beast(intelligence_tier=5, level=5)
        lines = available_voice_lines(smart_but_young, self.memory(), self.profile())
        self.assertEqual([line["line_id"] for line in lines], ["VOICE_GROWL"])

    def test_memory_specific_line_requires_actual_observation(self):
        beast = self.beast(intelligence_tier=3, level=12)
        before = available_voice_lines(beast, self.memory(), self.profile())
        self.assertNotIn("VOICE_REMEMBERS_SPEAR", [line["line_id"] for line in before])

        memory = self.memory(
            observations={"OBS_WEAPON_SPEAR": {"count": 2, "confidence": 0.8}}
        )
        after = available_voice_lines(beast, memory, self.profile())
        self.assertIn("VOICE_REMEMBERS_SPEAR", [line["line_id"] for line in after])

    def test_commander_line_requires_role_as_well_as_stats(self):
        ordinary = self.beast(intelligence_tier=5, level=30, role="veteran")
        ordinary_lines = available_voice_lines(ordinary, self.memory(), self.profile())
        self.assertNotIn("VOICE_COMMAND_FLANK", [line["line_id"] for line in ordinary_lines])

        commander = self.beast(intelligence_tier=5, level=30, role="commander")
        commander_lines = available_voice_lines(commander, self.memory(), self.profile())
        self.assertIn("VOICE_COMMAND_FLANK", [line["line_id"] for line in commander_lines])

    def test_selected_line_is_deterministic_and_player_safe(self):
        beast = self.beast(intelligence_tier=5, level=30, role="commander")
        memory = self.memory(
            observations={"OBS_WEAPON_SPEAR": {"count": 2, "confidence": 0.9}}
        )
        first = select_voice_line(beast, memory, self.profile(), context_key="PLAYER_RETURNS")
        second = select_voice_line(beast, memory, self.profile(), context_key="PLAYER_RETURNS")
        self.assertEqual(first, second)
        self.assertEqual(set(first), {"line_id", "text"})
        self.assertNotIn("required_observations", first)
        self.assertNotIn("min_intelligence_tier", first)


if __name__ == "__main__":
    unittest.main()
