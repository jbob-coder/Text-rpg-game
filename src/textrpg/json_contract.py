"""Shared finite-number JSON decoding for saves and authored content."""

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


def loads_strict_json(raw: str) -> Any:
    """Reject non-standard constants and numeric literals that overflow to infinity."""
    return json.loads(raw, parse_constant=_reject_constant, parse_float=_finite_float)
