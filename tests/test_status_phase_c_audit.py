from __future__ import annotations

import unittest
from pathlib import Path

from tools.status_phase_c_audit import (
    audit,
    compare_passive_owner_coverage,
    owner_records,
    registry_records,
)


ROOT = Path(__file__).resolve().parents[1]


class StatusPhaseCAuditTests(unittest.TestCase):
    def test_wave001_passive_owner_matrix_covers_registry_exactly(self) -> None:
        report = audit(ROOT)

        self.assertTrue(report["ok"], report["errors"])
        self.assertEqual(230, report["registry_count"])
        self.assertEqual(230, report["owner_matrix_count"])
        self.assertEqual(230, report["registry_unique_count"])
        self.assertEqual(230, report["owner_matrix_unique_count"])
        self.assertEqual(23, report["family_count"])
        self.assertTrue(all(count == 10 for count in report["family_counts"].values()))
        self.assertEqual([], report["missing_owner_ids"])
        self.assertEqual([], report["extra_owner_ids"])
        self.assertEqual([], report["duplicate_registry_ids"])
        self.assertEqual([], report["duplicate_owner_ids"])
        self.assertEqual([], report["incomplete_owner_rows"])

    def test_audit_detects_missing_owner_record(self) -> None:
        registry = registry_records(
            """
| ID | Name | Family | Effect | Acquisition class | Visibility | Status |
|---|---|---|---|---|---|---|
| PASSIVE_TST_0001 | One | Test | Effect one | test | HIDDEN_UNTIL_QUALIFIED | CALIBRATION_PROPOSAL |
| PASSIVE_TST_0002 | Two | Test | Effect two | test | HIDDEN_UNTIL_QUALIFIED | CALIBRATION_PROPOSAL |
"""
        )
        owners = owner_records(
            """
| ID | Name | Primary stage | Proposed conceptual write target | Qualification evidence class | Bounded effect |
|---|---|---|---|---|---|
| PASSIVE_TST_0001 | One | EXECUTION | `TEST_STATE.modifier.one` | `test` | Effect one |
"""
        )

        report = compare_passive_owner_coverage(registry, owners)

        self.assertFalse(report["ok"])
        self.assertEqual(["PASSIVE_TST_0002"], report["missing_owner_ids"])

    def test_audit_detects_duplicate_owner_record(self) -> None:
        registry = registry_records(
            """
| ID | Name | Family | Effect | Acquisition class | Visibility | Status |
|---|---|---|---|---|---|---|
| PASSIVE_TST_0001 | One | Test | Effect one | test | HIDDEN_UNTIL_QUALIFIED | CALIBRATION_PROPOSAL |
"""
        )
        owners = owner_records(
            """
| ID | Name | Primary stage | Proposed conceptual write target | Qualification evidence class | Bounded effect |
|---|---|---|---|---|---|
| PASSIVE_TST_0001 | One | EXECUTION | `TEST_STATE.modifier.one` | `test` | Effect one |
| PASSIVE_TST_0001 | One | EXECUTION | `TEST_STATE.modifier.one` | `test` | Effect one |
"""
        )

        report = compare_passive_owner_coverage(registry, owners)

        self.assertFalse(report["ok"])
        self.assertEqual(["PASSIVE_TST_0001"], report["duplicate_owner_ids"])


if __name__ == "__main__":
    unittest.main()
