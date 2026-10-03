from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL_PATH = ROOT / "tools" / "verify_pixel_raster_equivalence.py"

_spec = importlib.util.spec_from_file_location(
    "verify_pixel_raster_equivalence",
    TOOL_PATH,
)
if _spec is None or _spec.loader is None:
    raise RuntimeError(f"Unable to load {TOOL_PATH}")

verifier = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = verifier
_spec.loader.exec_module(verifier)


class PixelRasterEquivalenceToolTest(unittest.TestCase):
    def test_all_current_raster_bindings_match_source_masters(self) -> None:
        report = verifier.verify_repository(ROOT)

        self.assertEqual(24, report["asset_count"])
        self.assertEqual(
            "PASS",
            report["status"],
            json.dumps(report, indent=2, sort_keys=True),
        )
        self.assertEqual(24, report["matched_assets"])
        self.assertEqual(0, report["total_pixel_mismatches"])
        self.assertTrue(all(report["checks"].values()))


if __name__ == "__main__":
    unittest.main()
