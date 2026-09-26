import json
import unittest
from pathlib import Path

from textrpg import GameState, RuleError, RulesEngine


ROOT = Path(__file__).resolve().parents[1]


def load_engine():
    data = json.loads((ROOT / "content" / "sample_scene.json").read_text(encoding="utf-8"))
    return RulesEngine(data["scenes"])


def state(seed="test-seed"):
    return GameState(
        seed=seed,
        scene_id="SAMPLE_ARCHIVE_ENTRY",
        player={
            "attributes": {"intellect": 55},
            "skills": {"technical_systems": 12},
            "resources": {"focus": 50},
        },
        relationships={"NPC_MARA": {"trust": 25}},
        knowledge={"KNOW_CIPHER_SIGNATURE": {"source": "earlier_scene"}},
        inventory={"ITEM_CIPHER_KEY": 1},
    )


class RulesEngineTests(unittest.TestCase):
    def test_visibility_and_requirements(self):
        engine = load_engine()
        s = state()
        ids = {c["id"]: c for c in engine.available_choices(s)}
        self.assertTrue(ids["ASK_MARA_PRIVATELY"]["enabled"])
        self.assertTrue(ids["USE_CIPHER_KEY"]["enabled"])

    def test_hidden_choice_stays_hidden_without_knowledge(self):
        engine = load_engine()
        s = state()
        s.knowledge.clear()
        ids = {c["id"] for c in engine.available_choices(s)}
        self.assertNotIn("USE_CIPHER_KEY", ids)

    def test_choice_persists_knowledge_and_relationship(self):
        engine = load_engine()
        s = state()
        event = engine.choose(s, "ASK_MARA_PRIVATELY")
        self.assertIn("KNOW_ARCHIVE_ACCIDENT", s.knowledge)
        self.assertEqual(s.relationships["NPC_MARA"]["trust"], 27)
        self.assertEqual(s.time_minutes, 6)
        self.assertEqual(event["next_scene"], "SAMPLE_ARCHIVE_DECISION")

    def test_deterministic_check(self):
        engine = load_engine()
        a = state("same-seed")
        b = state("same-seed")
        ea = engine.choose(a, "FORCE_PANEL")
        eb = engine.choose(b, "FORCE_PANEL")
        self.assertEqual(ea["check"], eb["check"])

    def test_locked_choice_rejected(self):
        engine = load_engine()
        s = state()
        s.relationships["NPC_MARA"]["trust"] = 0
        with self.assertRaises(RuleError):
            engine.choose(s, "ASK_MARA_PRIVATELY")


class ExtendedStateTests(unittest.TestCase):
    def test_equipment_and_perks_modify_checks_without_mutating_base_stat(self):
        engine = load_engine()
        s = state("equipment-seed")
        s.equipment["hands"] = {
            "item_id": "ITEM_TOOL_GLOVES",
            "modifiers": {"attributes.intellect": 4},
        }
        s.perks["PERK_METHODICAL"] = {
            "source": "training",
            "modifiers": {"skills.technical_systems": 3},
        }
        event = engine.choose(s, "FORCE_PANEL")
        self.assertEqual(s.player["attributes"]["intellect"], 55)
        self.assertEqual(event["check"]["base"], 59.0)
        self.assertEqual(event["check"]["skill"], 15.0)

    def test_npc_knowledge_and_party_conditions(self):
        engine = RulesEngine({
            "A": {"choices": [{
                "id": "PRIVATE_GROUP_LINE",
                "text": "Use a fact only this group can act on.",
                "visible_if": [
                    {"type": "party_has", "npc": "NPC_MARA"},
                    {"type": "npc_knows", "npc": "NPC_MARA", "knowledge_id": "KNOW_ROUTE"}
                ],
                "outcomes": {"default": {"effects": []}}
            }]}
        })
        s = GameState(
            seed="x",
            scene_id="A",
            party=["NPC_MARA"],
            npcs={"NPC_MARA": {"knowledge": {"KNOW_ROUTE": {}}}},
        )
        self.assertEqual([c["id"] for c in engine.available_choices(s)], ["PRIVATE_GROUP_LINE"])

    def test_personality_effect_is_bounded(self):
        engine = RulesEngine({"A": {"choices": [{
            "id": "PRESSURE",
            "text": "Pressure NPC",
            "outcomes": {
                "default": {
                    "effects": [
                        {"type": "personality", "npc": "NPC_MARA", "axis": "caution", "value": 250}
                    ]
                }
            }
        }]}})
        s = GameState(seed="x", scene_id="A")
        engine.choose(s, "PRESSURE")
        self.assertEqual(s.npcs["NPC_MARA"]["personality"]["caution"], 100)


if __name__ == "__main__":
    unittest.main()
