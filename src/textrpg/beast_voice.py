from __future__ import annotations

from hashlib import sha256
from typing import Any, Dict, List, Mapping

from .beast_memory import validate_encounter_memory
from .core import RuleError
from .medieval import validate_beast_runtime_state


def _stable_id(value: Any) -> bool:
    return (
        isinstance(value, str)
        and bool(value)
        and value[0].isalpha()
        and all(char.isupper() or char.isdigit() or char == "_" for char in value)
    )


def validate_voice_profile(profile: Any) -> List[str]:
    if not isinstance(profile, Mapping):
        return ["beast voice profile must be an object"]
    lines = profile.get("lines")
    if not isinstance(lines, list):
        return ["voice_profile.lines must be a list"]

    errors: List[str] = []
    seen: set[str] = set()
    for index, line in enumerate(lines):
        label = f"voice_profile.lines[{index}]"
        if not isinstance(line, Mapping):
            errors.append(f"{label} must be an object")
            continue
        line_id = line.get("line_id")
        if not _stable_id(line_id):
            errors.append(f"{label}.line_id must be a stable uppercase ID")
        elif line_id in seen:
            errors.append(f"duplicate voice line ID: {line_id}")
        else:
            seen.add(line_id)
        if not isinstance(line.get("text"), str) or not line.get("text"):
            errors.append(f"{label}.text must be a non-empty string")
        minimum_intelligence = line.get("min_intelligence_tier", 0)
        if (
            isinstance(minimum_intelligence, bool)
            or not isinstance(minimum_intelligence, int)
            or not 0 <= minimum_intelligence <= 5
        ):
            errors.append(f"{label}.min_intelligence_tier must be an integer in range 0..5")
        minimum_level = line.get("min_level", 1)
        if isinstance(minimum_level, bool) or not isinstance(minimum_level, int) or minimum_level < 1:
            errors.append(f"{label}.min_level must be an integer >= 1")
        roles = line.get("roles", [])
        if not isinstance(roles, list) or not all(isinstance(role, str) and role for role in roles):
            errors.append(f"{label}.roles must be a list of non-empty strings")
        required_observations = line.get("required_observations", [])
        if not isinstance(required_observations, list) or not all(
            isinstance(observation_id, str) and observation_id.startswith("OBS_")
            for observation_id in required_observations
        ):
            errors.append(f"{label}.required_observations must contain OBS_ IDs")
    return errors


def available_voice_lines(
    beast_state: Mapping[str, Any],
    memory: Mapping[str, Any],
    profile: Mapping[str, Any],
) -> List[Dict[str, str]]:
    beast_errors = validate_beast_runtime_state(beast_state)
    memory_errors = validate_encounter_memory(memory)
    profile_errors = validate_voice_profile(profile)
    if beast_errors or memory_errors or profile_errors:
        raise RuleError(
            "Invalid beast voice contract:\n- "
            + "\n- ".join(beast_errors + memory_errors + profile_errors)
        )

    observations = memory.get("observations", {})
    output: List[Dict[str, str]] = []
    for line in profile["lines"]:
        if beast_state["intelligence_tier"] < line.get("min_intelligence_tier", 0):
            continue
        if beast_state["level"] < line.get("min_level", 1):
            continue
        roles = line.get("roles", [])
        if roles and beast_state["role"] not in roles:
            continue
        required = line.get("required_observations", [])
        if any(observation_id not in observations for observation_id in required):
            continue
        output.append({"line_id": line["line_id"], "text": line["text"]})
    return output


def select_voice_line(
    beast_state: Mapping[str, Any],
    memory: Mapping[str, Any],
    profile: Mapping[str, Any],
    *,
    context_key: str,
) -> Dict[str, str] | None:
    """Select one eligible authored line deterministically and expose no hidden gates."""
    if not isinstance(context_key, str) or not context_key:
        raise RuleError("voice context_key must be a non-empty string")
    available = available_voice_lines(beast_state, memory, profile)
    if not available:
        return None
    key = beast_state["beast_id"] + "|" + context_key + "|" + "|".join(
        line["line_id"] for line in available
    )
    digest = sha256(key.encode("utf-8")).digest()
    index = int.from_bytes(digest[:8], "big") % len(available)
    return dict(available[index])
