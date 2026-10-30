"""Shared strict JSON decoding for saves and authored content."""

from __future__ import annotations

import json
from math import isfinite
from typing import Any


def _reject_constant(value: str) -> None:
    raise ValueError(f"Non-finite JSON number is not allowed: {value}")


def _finite_float(value: str) -> float:
    number = float(value)
    if not isfinite(number):
        raise ValueError(f"JSON number exceeds the finite float range: {value}")
    return number


def _unique_object_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    """Reject ambiguous keys at every object depth, including escaped aliases."""
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON object key is not allowed: {key!r}")
        result[key] = value
    return result


def loads_strict_json(raw: str) -> Any:
    """Reject non-finite numbers and duplicate keys at any nesting level."""
    return json.loads(
        raw,
        parse_constant=_reject_constant,
        parse_float=_finite_float,
        object_pairs_hook=_unique_object_keys,
    )
