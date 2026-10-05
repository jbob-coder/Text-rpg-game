#!/usr/bin/env python3
"""Audit Wave-001 passive record ownership coverage.

This tool verifies that the 230 passive proposals in the canonical Wave-001
calibration table have a one-to-one record in the Phase-C owner/write-target
matrices. It is intentionally a documentation-integrity check: it does not
claim that conceptual owners or write targets exist in runtime code.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Iterable


PASSIVE_ID_RE = re.compile(r"^PASSIVE_([A-Z]+)_(\d{4})$")

REGISTRY_PATH = Path(
    "docs/systems/status/calibration/PASSIVES_WAVE_001.md"
)
OWNER_MATRIX_PATHS = (
    Path("docs/systems/status/PASSIVE_RECORD_OWNER_WRITE_TARGET_MATRIX_WAVE_001_A.md"),
    Path("docs/systems/status/PASSIVE_RECORD_OWNER_WRITE_TARGET_MATRIX_WAVE_001_B.md"),
    Path("docs/systems/status/PASSIVE_RECORD_OWNER_WRITE_TARGET_MATRIX_WAVE_001_C.md"),
)


def _table_cells(line: str) -> list[str]:
    if not line.startswith("|"):
        return []
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def registry_records(text: str) -> list[dict[str, str]]:
    """Extract passive records from the Wave-001 calibration table."""
    records: list[dict[str, str]] = []
    for line in text.splitlines():
        cells = _table_cells(line)
        if len(cells) < 7 or not PASSIVE_ID_RE.fullmatch(cells[0]):
            continue
        records.append(
            {
                "id": cells[0],
                "name": cells[1],
                "family": cells[2],
                "effect": cells[3],
                "acquisition_class": cells[4],
                "visibility": cells[5],
                "status": cells[6],
            }
        )
    return records


def owner_records(text: str) -> list[dict[str, str]]:
    """Extract passive rows from one owner/write-target matrix."""
    records: list[dict[str, str]] = []
    for line in text.splitlines():
        cells = _table_cells(line)
        if len(cells) < 6 or not PASSIVE_ID_RE.fullmatch(cells[0]):
            continue
        records.append(
            {
                "id": cells[0],
                "name": cells[1],
                "primary_stage": cells[2],
                "write_target": cells[3],
                "qualification_evidence_class": cells[4],
                "bounded_effect": cells[5],
            }
        )
    return records


def compare_passive_owner_coverage(
    registry: Iterable[dict[str, str]],
    owner_matrix: Iterable[dict[str, str]],
) -> dict:
    registry = list(registry)
    owner_matrix = list(owner_matrix)

    registry_ids = [record["id"] for record in registry]
    owner_ids = [record["id"] for record in owner_matrix]
    registry_counts = Counter(registry_ids)
    owner_counts = Counter(owner_ids)

    registry_set = set(registry_ids)
    owner_set = set(owner_ids)

    family_counts: Counter[str] = Counter()
    malformed_ids: list[str] = []
    for passive_id in registry_ids:
        match = PASSIVE_ID_RE.fullmatch(passive_id)
        if match is None:
            malformed_ids.append(passive_id)
            continue
        family_counts[match.group(1)] += 1

    incomplete_owner_rows = sorted(
        record["id"]
        for record in owner_matrix
        if any(
            not record[field].strip()
            for field in (
                "name",
                "primary_stage",
                "write_target",
                "qualification_evidence_class",
                "bounded_effect",
            )
        )
    )

    errors: list[str] = []
    duplicate_registry_ids = sorted(
        passive_id for passive_id, count in registry_counts.items() if count != 1
    )
    duplicate_owner_ids = sorted(
        passive_id for passive_id, count in owner_counts.items() if count != 1
    )
    missing_owner_ids = sorted(registry_set - owner_set)
    extra_owner_ids = sorted(owner_set - registry_set)

    if duplicate_registry_ids:
        errors.append("duplicate registry IDs")
    if duplicate_owner_ids:
        errors.append("duplicate owner-matrix IDs")
    if missing_owner_ids:
        errors.append("registry IDs missing from owner matrices")
    if extra_owner_ids:
        errors.append("owner-matrix IDs absent from registry")
    if incomplete_owner_rows:
        errors.append("owner-matrix rows with blank required fields")
    if malformed_ids:
        errors.append("malformed passive IDs")
    if len(registry) != 230:
        errors.append(f"registry count is {len(registry)}, expected 230")
    if len(owner_matrix) != 230:
        errors.append(f"owner-matrix count is {len(owner_matrix)}, expected 230")
    if len(family_counts) != 23:
        errors.append(f"family count is {len(family_counts)}, expected 23")
    wrong_family_counts = {
        family: count for family, count in family_counts.items() if count != 10
    }
    if wrong_family_counts:
        errors.append("one or more families do not contain exactly 10 records")

    return {
        "registry_count": len(registry),
        "owner_matrix_count": len(owner_matrix),
        "registry_unique_count": len(registry_set),
        "owner_matrix_unique_count": len(owner_set),
        "family_count": len(family_counts),
        "family_counts": dict(sorted(family_counts.items())),
        "duplicate_registry_ids": duplicate_registry_ids,
        "duplicate_owner_ids": duplicate_owner_ids,
        "missing_owner_ids": missing_owner_ids,
        "extra_owner_ids": extra_owner_ids,
        "incomplete_owner_rows": incomplete_owner_rows,
        "malformed_ids": sorted(malformed_ids),
        "wrong_family_counts": dict(sorted(wrong_family_counts.items())),
        "errors": errors,
        "ok": not errors,
    }


def audit(root: Path) -> dict:
    root = root.resolve()
    registry_path = root / REGISTRY_PATH
    owner_paths = [root / path for path in OWNER_MATRIX_PATHS]

    registry = registry_records(registry_path.read_text(encoding="utf-8"))
    owner_matrix: list[dict[str, str]] = []
    for path in owner_paths:
        owner_matrix.extend(owner_records(path.read_text(encoding="utf-8")))

    report = compare_passive_owner_coverage(registry, owner_matrix)
    report["registry_path"] = REGISTRY_PATH.as_posix()
    report["owner_matrix_paths"] = [path.as_posix() for path in OWNER_MATRIX_PATHS]
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root or a path inside the repository checkout",
    )
    parser.add_argument("--output", help="Optional JSON report path")
    args = parser.parse_args()

    root = Path(args.root)
    report = audit(root)
    payload = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        Path(args.output).write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
