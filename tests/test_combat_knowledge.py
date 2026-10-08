from copy import deepcopy
import json
import unittest

from textrpg import combat_knowledge as knowledge
from textrpg.combat_schema import TacticalCell, TacticalCoord, TacticalMap
from test_combat_turns import actor, active_session, line_map


class CombatKnowledgeTests(unittest.TestCase):
    def make_knowledge(self, *, identities=None):
        enemy = actor("SECRET_ENEMY", TacticalCoord(3, 0, 0), faction_id="SECRET_FACTION", initiative=5)
        session, player = active_session(line_map(6), extra_actors=(enemy,))
        session.combat_actions.update({
            "SHOT": {"category": "attack", "cost": 1, "range_max": 5,
                     "requires_los": True, "requires_detection": True},
            "IDENTIFIED_SHOT": {"category": "attack", "cost": 1, "range_max": 5,
                                "requires_identification": True},
            "BLIND": {"category": "attack", "cost": 1, "range_max": 5,
                      "allows_blind_area_targeting": True},
            "LAST_KNOWN": {"category": "attack", "cost": 1, "range_max": 5,
                           "allows_last_known_position": True},
        })
        return session, player, enemy, knowledge.CombatKnowledge(session, identities=identities)

    def test_los_does_not_reveal_an_unknown_actor_or_private_state(self):
        session, player, enemy, known = self.make_knowledge()
        before = deepcopy(session.__dict__)
        view = known.player_view(player.actor_id)
        self.assertEqual([], view["contacts"])
        self.assertNotIn(enemy.actor_id, json.dumps(view))
        self.assertNotIn(enemy.faction_id, json.dumps(view))
        self.assertEqual(before, session.__dict__)

    def test_detection_is_observer_specific_and_does_not_identify(self):
        session, player, enemy, known = self.make_knowledge()
        known.record_detection(player.actor_id, enemy.actor_id, detected=True)
        contact, = known.player_view(player.actor_id)["contacts"]
        self.assertEqual("DETECTED", contact["awareness"])
        self.assertEqual("3,0,0", contact["coord"])
        self.assertNotIn("identity", contact)
        self.assertNotIn(enemy.actor_id, json.dumps(contact))
        self.assertEqual([], known.player_view(enemy.actor_id)["contacts"])

    def test_legitimate_identity_is_an_explicit_allowlist(self):
        identity = knowledge.KnownIdentity(name="Known guard", faction="Known faction")
        session, player, enemy, known = self.make_knowledge(
            identities={("ACTOR_A", "SECRET_ENEMY"): identity})
        known.record_detection(player.actor_id, enemy.actor_id, detected=True)
        contact, = known.player_view(player.actor_id)["contacts"]
        self.assertEqual("IDENTIFIED", contact["awareness"])
        self.assertEqual({"name": "Known guard", "faction": "Known faction"}, contact["identity"])
        known.preview_target(player.actor_id, "IDENTIFIED_SHOT", target_actor_id=enemy.actor_id)

    def test_stale_detection_keeps_last_position_without_following_hidden_actor(self):
        session, player, enemy, known = self.make_knowledge()
        known.record_detection(player.actor_id, enemy.actor_id, detected=True)
        enemy.coord = TacticalCoord(5, 0, 0)
        contact, = known.player_view(player.actor_id)["contacts"]
        self.assertEqual("SUSPECTED", contact["awareness"])
        self.assertEqual("3,0,0", contact["last_known_coord"])
        self.assertNotIn("coord", contact)
        with self.assertRaisesRegex(ValueError, "target unavailable"):
            known.preview_target(player.actor_id, "SHOT", target_actor_id=enemy.actor_id)
        plan = known.preview_target(player.actor_id, "LAST_KNOWN", target_coord=TacticalCoord(3, 0, 0))
        self.assertEqual(TacticalCoord(3, 0, 0), plan.coord)

    def test_hidden_and_nonexistent_actor_targets_have_the_same_safe_failure(self):
        session, player, enemy, known = self.make_knowledge()
        errors = []
        for target in (enemy.actor_id, "DOES_NOT_EXIST"):
            with self.assertRaises(ValueError) as error:
                known.preview_target(player.actor_id, "BLIND", target_actor_id=target)
            errors.append(str(error.exception))
        self.assertEqual(["target unavailable"] * 2, errors)
        self.assertEqual(TacticalCoord(3, 0, 0), known.preview_target(
            player.actor_id, "BLIND", target_coord=TacticalCoord(3, 0, 0)).coord)

    def test_identification_range_and_los_are_independent_requirements(self):
        session, player, enemy, known = self.make_knowledge()
        known.record_detection(player.actor_id, enemy.actor_id, detected=True)
        with self.assertRaises(ValueError):
            known.preview_target(player.actor_id, "IDENTIFIED_SHOT", target_actor_id=enemy.actor_id)
        session.combat_actions["SHOT"]["range_max"] = 2
        with self.assertRaisesRegex(ValueError, "range"):
            known.preview_target(player.actor_id, "SHOT", target_actor_id=enemy.actor_id)

    def test_lost_los_preserves_stale_contact_and_cannot_create_new_detection(self):
        session, player, enemy, known = self.make_knowledge()
        known.record_detection(player.actor_id, enemy.actor_id, detected=True)
        session.tactical_map = TacticalMap("MAP_WALL", 1, 6, 1, (0,), tuple(
            TacticalCell(TacticalCoord(x, 0, 0), blocks_los=x == 2) for x in range(6)))
        self.assertEqual("SUSPECTED", known.player_view(player.actor_id)["contacts"][0]["awareness"])
        with self.assertRaisesRegex(ValueError, "line of sight"):
            known.record_detection(player.actor_id, enemy.actor_id, detected=True)

    def test_cover_defense_uses_incoming_edge_without_flank_bonus(self):
        session, player, enemy, known = self.make_knowledge()
        session.tactical_map = TacticalMap("MAP_COVER", 1, 6, 1, (0,), tuple(
            TacticalCell(TacticalCoord(x, 0, 0), cover=(("W", 2), ("E", 1)) if x == 3 else ())
            for x in range(6)))
        known.record_detection(player.actor_id, enemy.actor_id, detected=True)
        self.assertEqual(20, known.preview_target(player.actor_id, "SHOT", target_actor_id=enemy.actor_id).cover_defense)
        player.coord = TacticalCoord(5, 0, 0)
        self.assertEqual(10, known.preview_target(player.actor_id, "SHOT", target_actor_id=enemy.actor_id).cover_defense)

    def test_hidden_occupancy_does_not_change_safe_movement_preview(self):
        session, player, enemy, known = self.make_knowledge()
        before = deepcopy(session.__dict__)
        path = known.preview_movement(player.actor_id, "ACTION_MOVE", TacticalCoord(4, 0, 0))
        self.assertEqual(TacticalCoord(4, 0, 0), path.path[-1])
        self.assertEqual(before, session.__dict__)
        enemy.coord = TacticalCoord(5, 0, 0)
        self.assertEqual(path, known.preview_movement(player.actor_id, "ACTION_MOVE", TacticalCoord(4, 0, 0)))
        known.record_detection(player.actor_id, enemy.actor_id, detected=True)
        with self.assertRaises(ValueError):
            known.preview_movement(player.actor_id, "ACTION_MOVE", TacticalCoord(5, 0, 0))

    def test_blind_area_preview_does_not_disclose_unseen_cover(self):
        session, player, enemy, known = self.make_knowledge()
        session.tactical_map = TacticalMap("MAP_UNSEEN", 1, 6, 1, (0,), tuple(
            TacticalCell(TacticalCoord(x, 0, 0), blocks_los=x == 2,
                         cover=(("W", 2),) if x == 3 else ()) for x in range(6)))
        preview = known.preview_target(player.actor_id, "BLIND", target_coord=TacticalCoord(3, 0, 0))
        self.assertIsNone(preview.cover_defense)


if __name__ == "__main__":
    unittest.main()
