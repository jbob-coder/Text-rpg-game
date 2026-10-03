from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
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

    def test_exporter_reconstructs_all_bindings_deterministically(self) -> None:
        with tempfile.TemporaryDirectory() as first_dir, tempfile.TemporaryDirectory() as second_dir:
            first = verifier.export_repository_rasters(ROOT, Path(first_dir))
            second = verifier.export_repository_rasters(ROOT, Path(second_dir))

            self.assertEqual(24, first["asset_count"])
            self.assertEqual(24, second["asset_count"])

            first_assets = {item["path"]: item for item in first["assets"]}
            second_assets = {item["path"]: item for item in second["assets"]}
            self.assertEqual(set(first_assets), set(second_assets))

            for relative_path in sorted(first_assets):
                first_bytes = (Path(first_dir) / relative_path).read_bytes()
                second_bytes = (Path(second_dir) / relative_path).read_bytes()
                self.assertEqual(first_bytes, second_bytes, relative_path)

                width, height, pixels = verifier.decode_png_rgba(first_bytes)
                self.assertEqual(first_assets[relative_path]["width"], width)
                self.assertEqual(first_assets[relative_path]["height"], height)
                self.assertEqual(width * height, len(pixels))

    def test_exporter_refuses_repository_root(self) -> None:
        with self.assertRaises(ValueError):
            verifier.export_repository_rasters(ROOT, ROOT)

    def test_binding_validator_rejects_path_escape(self) -> None:
        evidence = json.loads(
            (ROOT / verifier.BINDING_EVIDENCE).read_text(encoding="utf-8")
        )
        evidence["assets"][0]["path"] = "../escape.png"

        with self.assertRaises(ValueError):
            verifier._validate_binding_assets(evidence)

    def test_binding_validator_rejects_duplicate_path(self) -> None:
        evidence = json.loads(
            (ROOT / verifier.BINDING_EVIDENCE).read_text(encoding="utf-8")
        )
        evidence["assets"][-1]["path"] = evidence["assets"][0]["path"]

        with self.assertRaises(ValueError):
            verifier._validate_binding_assets(evidence)


if __name__ == "__main__":
    unittest.main()
