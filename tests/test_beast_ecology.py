import unittest

from textrpg.beast_ecology import (
    ecology_combat_score,
    resolve_beast_conflict,
    validate_ecology_profile,
    validate_territory_state,
)
from textrpg.core import RuleError


class BeastEcologyTests(unittest.TestCase):
    def beast(self, beast_id, **changes):
        state = {
            "beast_id": beast_id,
            "species_id": "SPECIES_WOLF",
            "level": 10,
            "development_xp": 1000,
            "intelligence_tier": 2,
            "role": "veteran",
            "follower_count": 0,
            "memories": [],
            "adaptations": [],
        }
        state.update(changes)
        return state

    def profile(self, **changes):
        profile = {
            "offense": 50,
            "defense": 50,
            "mobility": 50,
            "tactics": 50,
            "morale": 50,
            "injury_penalty": 0,
        }
        profile.update(changes)
        return profile

    def territory(self, **changes):
        territory = {
            "territory_id": "REGION_ASH_PASS",
            "controller_beast_id": "BEAST_DEFENDER",
            "defense_bonus": 20,
            "resource_value": 60,
        }
        territory.update(changes)
        return territory

    def test_profile_and_territory_contracts_are_strict(self):
        self.assertEqual(validate_ecology_profile(self.profile()), [])
        self.assertEqual(validate_territory_state(self.territory()), [])
        self.assertTrue(validate_ecology_profile(self.profile(tactics=float("nan"))))

    def test_intelligence_increases_value_of_tactics_without_becoming_raw_physical_power(self):
        low = ecology_combat_score(
            self.beast("BEAST_LOW", intelligence_tier=0),
            self.profile(tactics=100),
        )
        high = ecology_combat_score(
            self.beast("BEAST_HIGH", intelligence_tier=5),
            self.profile(tactics=100),
        )
        self.assertEqual(low["physical"], high["physical"])
        self.assertGreater(high["tactics"], low["tactics"])

    def test_commander_can_convert_followers_and_intelligence_into_command_value(self):
        veteran = ecology_combat_score(
            self.beast("BEAST_A", role="veteran", follower_count=12, intelligence_tier=5),
            self.profile(),
        )
        commander = ecology_combat_score(
            self.beast("BEAST_B", role="commander", follower_count=12, intelligence_tier=5),
            self.profile(),
        )
        self.assertEqual(veteran["command"], 0.0)
        self.assertGreater(commander["command"], 0.0)

    def test_injuries_reduce_coarse_world_combat_score(self):
        healthy = ecology_combat_score(self.beast("BEAST_A"), self.profile())
        injured = ecology_combat_score(
            self.beast("BEAST_B"), self.profile(injury_penalty=75)
        )
        self.assertLess(injured["total"], healthy["total"])

    def test_conflict_is_deterministic_for_same_seed_and_state(self):
        args = (
            self.beast("BEAST_ATTACKER"),
            self.beast("BEAST_DEFENDER"),
            self.profile(offense=70),
            self.profile(defense=60),
            self.territory(),
        )
        first = resolve_beast_conflict(
            *args, event_id="EVENT_BEAST_CONFLICT_1", seed="WORLD_SEED"
        )
        second = resolve_beast_conflict(
            *args, event_id="EVENT_BEAST_CONFLICT_1", seed="WORLD_SEED"
        )
        self.assertEqual(first, second)

    def test_decisive_attacker_win_can_transfer_territory_without_mutating_input(self):
        territory = self.territory(controller_beast_id="BEAST_DEFENDER", defense_bonus=0)
        result = resolve_beast_conflict(
            self.beast("BEAST_ATTACKER", level=30, intelligence_tier=4, role="commander", follower_count=10),
            self.beast("BEAST_DEFENDER", level=5),
            self.profile(offense=95, tactics=90, morale=90),
            self.profile(offense=15, defense=20, mobility=20, tactics=10, morale=20),
            territory,
            event_id="EVENT_TERRITORY_TAKEOVER",
            seed="WORLD_SEED",
            variance=0,
            claim_margin=10,
        )
        self.assertEqual(territory["controller_beast_id"], "BEAST_DEFENDER")
        self.assertTrue(result["territory_changed"])
        self.assertEqual(result["territory"]["controller_beast_id"], "BEAST_ATTACKER")

    def test_defender_receives_territory_bonus_only_when_it_controls_region(self):
        defender = self.beast("BEAST_DEFENDER")
        controlled = resolve_beast_conflict(
            self.beast("BEAST_ATTACKER"), defender,
            self.profile(), self.profile(), self.territory(),
            event_id="EVENT_CONTROLLED", seed="SEED", variance=0,
        )
        neutral = resolve_beast_conflict(
            self.beast("BEAST_ATTACKER"), defender,
            self.profile(), self.profile(),
            self.territory(controller_beast_id=None),
            event_id="EVENT_NEUTRAL", seed="SEED", variance=0,
        )
        self.assertGreater(
            controlled["defender_score"]["territory"],
            neutral["defender_score"]["territory"],
        )

    def test_self_conflict_is_rejected(self):
        beast = self.beast("BEAST_SAME")
        with self.assertRaises(RuleError):
            resolve_beast_conflict(
                beast, beast, self.profile(), self.profile(), self.territory(),
                event_id="EVENT_INVALID", seed="SEED",
            )


if __name__ == "__main__":
    unittest.main()
