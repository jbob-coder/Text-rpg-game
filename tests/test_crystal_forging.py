import unittest

from textrpg.core import RuleError
from textrpg.crystal_forging import (
    crystal_socket_compatibility,
    integrate_crystal,
    remove_socketed_crystal,
    validate_equipment_instance,
)


class CrystalForgingTests(unittest.TestCase):
    def item(self):
        return {
            "instance_id": "ITEMINSTANCE_SPEAR_1",
            "definition_id": "WEAPON_SPEAR_IRON",
            "material_id": "MATERIAL_IRON",
            "forge_quality": 72,
            "condition": 100,
            "crystal_sockets": [
                {
                    "socket_id": "SOCKET_PRIMARY",
                    "max_grade": 3,
                    "allowed_source_types": ["mine", "beast"],
                    "allowed_resonance_tags": ["frost", "force"],
                    "allowed_modes": ["socket", "fusion"],
                    "crystal": None,
                }
            ],
        }

    def crystal(self, **changes):
        crystal = {
            "instance_id": "CRYSTALINSTANCE_WOLF_1",
            "crystal_id": "CRYSTAL_WOLF_HEART",
            "source_type": "beast",
            "source_beast_id": "BEAST_WHITE_FANG",
            "grade": 2,
            "purity": 85,
            "stability": 74,
            "harvest_integrity": 96,
            "size": 1.0,
            "resonance_tags": ["frost"],
        }
        crystal.update(changes)
        return crystal

    def test_equipment_instance_contract_accepts_valid_socket(self):
        self.assertEqual(validate_equipment_instance(self.item()), [])

    def test_grade_and_resonance_are_independent_compatibility_gates(self):
        grade_result = crystal_socket_compatibility(
            self.item(), self.crystal(grade=5), "SOCKET_PRIMARY"
        )
        self.assertEqual(grade_result, {"compatible": False, "reasons": ["grade"]})

        resonance_result = crystal_socket_compatibility(
            self.item(),
            self.crystal(resonance_tags=["lightning"]),
            "SOCKET_PRIMARY",
        )
        self.assertEqual(
            resonance_result,
            {"compatible": False, "reasons": ["resonance"]},
        )

    def test_integration_is_copy_on_write_and_preserves_crystal_provenance(self):
        item = self.item()
        crystal = self.crystal()
        updated = integrate_crystal(
            item,
            crystal,
            "SOCKET_PRIMARY",
            mode="socket",
            integration_quality=88,
            smith_id="NPC_SMITH_1",
        )
        self.assertIsNone(item["crystal_sockets"][0]["crystal"])
        installed = updated["crystal_sockets"][0]["crystal"]
        self.assertEqual(installed["source_beast_id"], "BEAST_WHITE_FANG")
        self.assertEqual(installed["harvest_integrity"], 96)
        self.assertEqual(updated["crystal_sockets"][0]["integration"]["quality"], 88.0)

    def test_fusion_locks_the_crystal(self):
        fused = integrate_crystal(
            self.item(),
            self.crystal(),
            "SOCKET_PRIMARY",
            mode="fusion",
            integration_quality=91,
        )
        self.assertTrue(fused["crystal_sockets"][0]["locked"])
        with self.assertRaises(RuleError):
            remove_socketed_crystal(fused, "SOCKET_PRIMARY")

    def test_replaceable_socket_can_remove_crystal_without_mutating_source_item(self):
        fitted = integrate_crystal(
            self.item(),
            self.crystal(),
            "SOCKET_PRIMARY",
            mode="socket",
            integration_quality=80,
        )
        removed = remove_socketed_crystal(fitted, "SOCKET_PRIMARY")
        self.assertIsNotNone(fitted["crystal_sockets"][0]["crystal"])
        self.assertIsNone(removed["crystal_sockets"][0]["crystal"])

    def test_occupied_socket_rejects_second_crystal(self):
        fitted = integrate_crystal(
            self.item(),
            self.crystal(),
            "SOCKET_PRIMARY",
            mode="socket",
            integration_quality=80,
        )
        result = crystal_socket_compatibility(
            fitted,
            self.crystal(instance_id="CRYSTALINSTANCE_WOLF_2"),
            "SOCKET_PRIMARY",
        )
        self.assertEqual(result, {"compatible": False, "reasons": ["occupied"]})

    def test_nonfinite_integration_quality_is_rejected(self):
        with self.assertRaises(RuleError):
            integrate_crystal(
                self.item(),
                self.crystal(),
                "SOCKET_PRIMARY",
                integration_quality=float("nan"),
            )


if __name__ == "__main__":
    unittest.main()
