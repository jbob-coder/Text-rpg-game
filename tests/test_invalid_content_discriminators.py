"""Regression tests for malformed authored content discriminator types."""

import unittest

from textrpg import (
    RuleError,
    assert_valid_scenes,
    validate_content_pack,
    validate_scenes,
)


class InvalidContentDiscriminatorTests(unittest.TestCase):
    @staticmethod
    def scene(*, condition=None, effect=None):
        choice = {
            "id": "CHOICE_TEST",
            "text": "Continue",
            "outcomes": {"default": {"effects": [] if effect is None else [effect]}},
        }
        if condition is not None:
            choice["requires"] = [condition]
        return {"SCENE_TEST": {"choices": [choice]}}

    def test_unhashable_condition_types_return_errors(self):
        for kind in ([], {}, ["flag"], {"type": "flag"}):
            with self.subTest(kind=kind):
                scenes = self.scene(condition={"type": kind})
                errors = validate_scenes(scenes)
                self.assertTrue(any("unsupported type" in error for error in errors))
                with self.assertRaises(RuleError):
                    assert_valid_scenes(scenes)

    def test_unhashable_effect_types_return_errors_in_full_pack_validation(self):
        for kind in ([], {}, ["inventory"], {"type": "inventory"}):
            with self.subTest(kind=kind):
                scenes = self.scene(effect={"type": kind})
                self.assertTrue(
                    any("unsupported type" in error for error in validate_scenes(scenes))
                )
                # Follow-on registry/quest/power cross-reference passes must not
                # crash after the scene validator has reported the invalid type.
                errors = validate_content_pack(scenes, registries={"knowledge": {}})
                self.assertTrue(any("unsupported type" in error for error in errors))

    def test_unhashable_technique_stage_is_reported_as_invalid_value(self):
        for stage in ([], {}, ["learned"]):
            with self.subTest(stage=stage):
                scenes = self.scene(
                    condition={
                        "type": "technique_stage_min",
                        "ability_id": "ABILITY_TEST",
                        "technique_id": "TECH_TEST",
                        "stage": stage,
                    }
                )
                errors = validate_scenes(scenes)
                self.assertTrue(any(".stage has unsupported value" in e for e in errors))

    def test_valid_discriminators_still_work(self):
        scenes = self.scene(
            condition={"type": "item_min", "quantity": 1},
            effect={"type": "inventory", "item_id": "ITEM_TEST", "quantity": 1},
        )
        self.assertEqual([], validate_scenes(scenes))

    def test_unhashable_scene_destinations_are_validation_errors(self):
        for destination in ([], {}, ["SCENE_TEST"]):
            for location in ("choice", "outcome"):
                with self.subTest(destination=destination, location=location):
                    scenes = self.scene()
                    choice = scenes["SCENE_TEST"]["choices"][0]
                    if location == "choice":
                        choice["next_scene"] = destination
                    else:
                        choice["outcomes"]["default"]["next_scene"] = destination
                    errors = validate_scenes(scenes)
                    self.assertTrue(any("unknown scene" in e for e in errors))

    def test_unhashable_world_map_edge_endpoints_are_validation_errors(self):
        from textrpg.validation import validate_world_map

        nodes = {
            "NODE_A": {"x": 0, "y": 0},
            "NODE_B": {"x": 1, "y": 1},
        }
        for endpoint in ("from", "to"):
            for bad in ([], {}, ["NODE_A"]):
                with self.subTest(endpoint=endpoint, bad=bad):
                    edge = {"from": "NODE_A", "to": "NODE_B"}
                    edge[endpoint] = bad
                    errors = validate_world_map(
                        {"nodes": nodes, "edges": [edge]}, self.scene()
                    )
                    self.assertTrue(any("unknown node" in e for e in errors))

    def test_unhashable_quest_refs_are_validation_errors(self):
        quests = {
            "QUEST_TEST": {
                "start_stage": "STAGE_ONE",
                "stages": {"STAGE_ONE": {"objectives": {}}},
            }
        }
        for field, bad in (("quest_id", []), ("stage", {})):
            with self.subTest(field=field):
                effect = {
                    "type": "quest_stage",
                    "quest_id": "QUEST_TEST",
                    "stage": "STAGE_ONE",
                }
                effect[field] = bad
                errors = validate_content_pack(self.scene(effect=effect), quests)
                self.assertTrue(
                    any("unknown quest" in e or "unknown stage" in e for e in errors)
                )

    def test_unhashable_power_refs_are_validation_errors(self):
        effects = (
            {"type": "ability_discover", "ability_id": []},
            {
                "type": "technique_discover",
                "ability_id": "ABILITY_TEST",
                "technique_id": {},
            },
        )
        for effect in effects:
            with self.subTest(effect=effect):
                errors = validate_content_pack(self.scene(effect=effect), powers={})
                self.assertTrue(any("unknown power" in e for e in errors))
        condition = {
            "type": "technique_discoverable",
            "ability_id": [],
            "technique_id": "TECH_TEST",
        }
        errors = validate_content_pack(self.scene(condition=condition), powers={})
        self.assertTrue(any("unknown power" in e for e in errors))


    def test_extremely_large_json_integer_rejected_in_world_coordinates(self):
        from textrpg.validation import validate_world_map

        huge = 10 ** 400
        nodes = {"NODE_A": {"x": huge, "y": 12}}
        errors = validate_world_map({"nodes": nodes}, self.scene())
        self.assertTrue(any("NODE_A.x must be finite numeric" in e for e in errors))
        self.assertEqual([], validate_world_map(
            {"nodes": {"NODE_A": {"x": 12, "y": 100}}}, self.scene()
        ))

    def test_extremely_large_json_integer_rejected_in_effect_numbers(self):
        huge = 10 ** 400
        cases = (
            ("quality", {"type": "power_recover", "ability_id": "ABILITY_TEST",
                          "minutes": 1, "quality": huge}),
            ("progress", {"type": "npc_goal_create", "npc": "NPC_TEST",
                           "goal_id": "GOAL_TEST", "progress": huge}),
            ("delta", {"type": "npc_goal_progress", "npc": "NPC_TEST",
                        "goal_id": "GOAL_TEST", "delta": huge}),
            ("completion_threshold", {"type": "npc_goal_progress", "npc": "NPC_TEST",
                                      "goal_id": "GOAL_TEST", "delta": 1,
                                      "completion_threshold": huge}),
        )
        for field, effect in cases:
            with self.subTest(field=field):
                errors = validate_scenes(self.scene(effect=effect))
                self.assertTrue(any("." + field in e for e in errors), errors)



if __name__ == "__main__":
    unittest.main()
