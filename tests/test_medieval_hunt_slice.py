import unittest

from textrpg.beast_harvest import apply_body_zone_damage, harvest_beast_crystal
from textrpg.beast_memory import adaptation_eligibility, record_encounter_observations
from textrpg.beast_progression import award_beast_development
from textrpg.beast_voice import available_voice_lines
from textrpg.crystal_forging import crystal_effect_output, integrate_crystal
from textrpg.medieval import reachable_target_zones


class MedievalHuntSliceTests(unittest.TestCase):
    def weapon(self):
        return {
            "family": "spear",
            "range_bands": ["close", "reach"],
            "target_tags": ["high", "limb", "core"],
            "damage_profile": {"pierce": 10},
        }

    def zones(self):
        return {
            "ZONE_HEAD": {
                "label": "Head",
                "facings": ["front", "left_flank", "right_flank"],
                "range_bands": ["close", "reach"],
                "tags": ["high"],
            },
            "ZONE_HEART_CORE": {
                "label": "Heart/Core",
                "facings": ["left_flank", "right_flank"],
                "range_bands": ["close", "reach"],
                "tags": ["core"],
                "requires_exposure_tags": ["CORE_EXPOSED"],
                "vital": True,
                "crystal_risk": True,
            },
        }

    def combat(self, **changes):
        state = {
            "facing": "front",
            "range_band": "reach",
            "attacker_posture": "standing",
            "defender_posture": "standing",
            "elevation": "level",
            "exposure_tags": [],
            "blocked_zones": [],
        }
        state.update(changes)
        return state

    def beast(self, **changes):
        state = {
            "beast_id": "BEAST_WHITE_FANG",
            "species_id": "SPECIES_WOLF",
            "level": 12,
            "development_xp": 500,
            "intelligence_tier": 3,
            "role": "veteran",
            "follower_count": 0,
            "memories": [],
            "adaptations": [],
        }
        state.update(changes)
        return state

    def memory(self):
        return {
            "memory_id": "MEMORY_PLAYER_1",
            "opponent_id": "PLAYER_1",
            "encounter_count": 0,
            "last_seen_time_minutes": 0,
            "observations": {},
        }

    def crystal_definition(self):
        return {
            "crystal_id": "CRYSTAL_WOLF_HEART",
            "core_zone_id": "ZONE_HEART_CORE",
            "base_grade": 2,
            "base_purity": 90,
            "base_stability": 90,
            "size": 1.0,
            "resonance_tags": ["frost"],
            "effects": {"EFFECT_FROST_EDGE": 20},
            "core_damage_sensitivity": 1.0,
            "decay_per_hour": 1.0,
        }

    def equipment(self):
        return {
            "instance_id": "ITEMINSTANCE_SPEAR_1",
            "definition_id": "WEAPON_SPEAR_IRON",
            "material_id": "MATERIAL_IRON",
            "forge_quality": 85,
            "condition": 100,
            "crystal_sockets": [
                {
                    "socket_id": "SOCKET_PRIMARY",
                    "max_grade": 3,
                    "allowed_source_types": ["beast"],
                    "allowed_resonance_tags": ["frost"],
                    "allowed_modes": ["socket", "fusion"],
                    "crystal": None,
                }
            ],
        }

    def progression_definition(self):
        return {
            "base_level_xp": 100,
            "growth_factor": 1.5,
            "repeat_decay": 0.5,
            "min_repeat_factor": 0.1,
            "max_xp_per_event": 500,
            "max_level": 50,
        }

    def voice_profile(self):
        return {
            "lines": [
                {
                    "line_id": "VOICE_GROWL",
                    "text": "A low warning growl.",
                    "min_intelligence_tier": 0,
                    "min_level": 1,
                },
                {
                    "line_id": "VOICE_REMEMBERS_SPEAR",
                    "text": "The spear again. I remember its reach.",
                    "min_intelligence_tier": 3,
                    "min_level": 10,
                    "required_observations": ["OBS_WEAPON_SPEAR"],
                },
            ]
        }

    def test_position_to_core_damage_to_harvest_to_forged_output(self):
        front_targets = reachable_target_zones(self.combat(), self.zones(), self.weapon())
        self.assertNotIn("ZONE_HEART_CORE", front_targets)

        exposed = self.combat(facing="left_flank", exposure_tags=["CORE_EXPOSED"])
        exposed_targets = reachable_target_zones(exposed, self.zones(), self.weapon())
        self.assertIn("ZONE_HEART_CORE", exposed_targets)

        core = {
            "zone_id": "ZONE_HEART_CORE",
            "max_integrity": 100,
            "damage_taken": 0,
            "hits": 0,
            "damage_by_type": {},
        }
        core = apply_body_zone_damage(core, 30, "pierce")
        crystal = harvest_beast_crystal(
            self.beast(life_state="dead"),
            core,
            self.crystal_definition(),
            instance_id="CRYSTALINSTANCE_HUNT_1",
            harvest_skill=90,
            tool_quality=90,
        )
        fitted = integrate_crystal(
            self.equipment(),
            crystal,
            "SOCKET_PRIMARY",
            integration_quality=90,
            smith_id="NPC_SMITH_1",
        )
        output = crystal_effect_output(
            fitted, "SOCKET_PRIMARY", "EFFECT_FROST_EDGE"
        )

        self.assertEqual(crystal["harvest"]["core_damage_percent"], 30.0)
        self.assertGreater(output["total"], 0.0)
        self.assertLess(output["total"], output["base_value"])

    def test_retreat_memory_development_adaptation_and_voice_are_connected(self):
        memory = record_encounter_observations(
            self.memory(),
            {"OBS_WEAPON_SPEAR": 0.8, "OBS_DODGE_LEFT": 0.7},
            occurred_at_minutes=100,
        )
        memory = record_encounter_observations(
            memory,
            {"OBS_WEAPON_SPEAR": 0.9, "OBS_DODGE_LEFT": 0.9},
            occurred_at_minutes=200,
        )

        beast = award_beast_development(
            self.beast(),
            {
                "event_id": "EVENT_SURVIVED_PLAYER_1",
                "repeat_key": "EVENTCLASS_SURVIVE_PLAYER",
                "type": "survival",
                "meaningful": True,
                "base_xp": 120,
                "significance": 1.0,
            },
            self.progression_definition(),
        )
        adaptation = adaptation_eligibility(
            beast,
            memory,
            {
                "min_intelligence_tier": 3,
                "min_elapsed_minutes": 180,
                "required_observations": {
                    "OBS_WEAPON_SPEAR": {"min_count": 2, "min_confidence": 0.8},
                    "OBS_DODGE_LEFT": {"min_count": 2, "min_confidence": 0.75},
                },
            },
            current_time_minutes=400,
        )
        lines = available_voice_lines(beast, memory, self.voice_profile())

        self.assertTrue(adaptation["eligible"])
        self.assertGreater(beast["development_xp"], 500)
        self.assertIn("VOICE_REMEMBERS_SPEAR", [line["line_id"] for line in lines])

    def test_repeated_survival_cannot_be_farmed_at_full_value(self):
        beast = self.beast(development_xp=0, level=1)
        event = {
            "event_id": "EVENT_SURVIVE_1",
            "repeat_key": "EVENTCLASS_SURVIVE_PLAYER",
            "type": "survival",
            "meaningful": True,
            "base_xp": 100,
            "significance": 1.0,
        }
        first = award_beast_development(beast, event, self.progression_definition())
        second = award_beast_development(
            first,
            {**event, "event_id": "EVENT_SURVIVE_2"},
            self.progression_definition(),
        )
        self.assertEqual(first["development_log"][-1]["awarded_xp"], 100.0)
        self.assertEqual(second["development_log"][-1]["awarded_xp"], 50.0)


if __name__ == "__main__":
    unittest.main()
