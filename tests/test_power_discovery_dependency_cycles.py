"""Reject impossible authored technique discovery graphs before gameplay.

These tests deliberately distinguish discovery prerequisites (must be acyclic)
from technique-use requirements, which may depend on already-learned skills.
"""

import unittest

from textrpg import RuleError
from textrpg.powers import assert_valid_power_definitions, validate_power_definitions


class TechniqueDiscoveryDependencyCycleTests(unittest.TestCase):
    @staticmethod
    def pack(graph):
        return {
            "ABILITY_TRACE": {
                "techniques": {
                    name: {
                        "discovery_requirements": {
                            "techniques": {
                                dependency: "discovered" for dependency in dependencies
                            }
                        }
                    }
                    for name, dependencies in graph.items()
                }
            }
        }

    def test_mutual_discovery_prerequisites_are_rejected(self):
        definitions = self.pack({
            "TECHNIQUE_ALPHA": ["TECHNIQUE_BETA"],
            "TECHNIQUE_BETA": ["TECHNIQUE_ALPHA"],
        })
        errors = validate_power_definitions(definitions)
        self.assertTrue(any("circular discovery prerequisites" in e for e in errors), errors)
        with self.assertRaisesRegex(RuleError, "circular discovery prerequisites"):
            assert_valid_power_definitions(definitions)

    def test_three_technique_cycle_is_rejected_even_with_available_root(self):
        definitions = self.pack({
            "TECHNIQUE_ROOT": [],
            "TECHNIQUE_ALPHA": ["TECHNIQUE_BETA"],
            "TECHNIQUE_BETA": ["TECHNIQUE_GAMMA"],
            "TECHNIQUE_GAMMA": ["TECHNIQUE_ALPHA"],
        })
        errors = validate_power_definitions(definitions)
        self.assertTrue(any("circular discovery prerequisites" in e for e in errors), errors)

    def test_valid_discovery_chain_is_accepted(self):
        definitions = self.pack({
            "TECHNIQUE_ROOT": [],
            "TECHNIQUE_ALPHA": ["TECHNIQUE_ROOT"],
            "TECHNIQUE_BETA": ["TECHNIQUE_ALPHA"],
        })
        self.assertEqual(validate_power_definitions(definitions), [])

    def test_already_discovered_use_requirements_are_not_a_discovery_cycle(self):
        definitions = {
            "ABILITY_TRACE": {
                "techniques": {
                    "TECHNIQUE_ALPHA": {
                        "requirements": {"techniques": {"TECHNIQUE_BETA": "discovered"}},
                    },
                    "TECHNIQUE_BETA": {
                        "requirements": {"techniques": {"TECHNIQUE_ALPHA": "discovered"}},
                    },
                }
            }
        }
        self.assertEqual(validate_power_definitions(definitions), [])


if __name__ == "__main__":
    unittest.main()
