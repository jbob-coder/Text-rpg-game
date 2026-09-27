from __future__ import annotations

from math import isfinite
from typing import Any, Dict, Mapping, MutableMapping

from .core import RuleError


INTELLIGENCE_MIN = 0
INTELLIGENCE_MAX = 5
OBSERVATION_KINDS = (
    "weapon_family",
    "target_zone",
    "range_band",
    "opening_action",
    "defense_reaction",
    "technique",
    "trap",
    "party_role",
    "terrain",
    "retreat",
)
ADAPTATION_TYPES = ("behavioral", "tactical", "strategic", "biological")
BEAST_ROLES = (
    "solitary",
    "pack_member",
    "veteran",
    "guardian",
    "chieftain",
    "commander",
    "territory_ruler",
    "regional_apex",
)

_ADAPTATION_REQUIREMENTS: Dict[str, Dict[str, float]] = {
    "behavioral": {
        "min_intelligence": 1,
        "min_observations": 2,
        "min_confidence": 0.30,
    },
    "tactical": {
        "min_intelligence": 2,
        "min_observations": 3,
        "min_confidence": 0.50,
    },
    "strategic": {
        "min_intelligence": 4,
        "min_observations": 4,
        "min_confidence": 0.70,
    },
    "biological": {
        "min_intelligence": 0,
        "min_observations": 3,
        "min_confidence": 0.55,
        "min_elapsed_minutes": 10080,
        "min_resource_score": 0.50,
    },
}


def _string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise RuleError(f"{label} must be a non-empty string")
    return value


def _finite(
    value: Any,
    label: str,
    *,
    minimum: float | None = None,
    maximum: float | None = None,
) -> float:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not isfinite(float(value))
    ):
        raise RuleError(f"{label} must be a finite number")
    number = float(value)
    if minimum is not None and number < minimum:
        raise RuleError(f"{label} must be >= {minimum}")
    if maximum is not None and number > maximum:
        raise RuleError(f"{label} must be <= {maximum}")
    return number


def _non_negative_int(value: Any, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise RuleError(f"{label} must be a non-negative integer")
    return value


def _intelligence(value: Any, label: str = "beast.intelligence") -> int:
    if (
        isinstance(value, bool)
        or not isinstance(value, int)
        or value < INTELLIGENCE_MIN
        or value > INTELLIGENCE_MAX
    ):
        raise RuleError(
            f"{label} must be an integer in range "
            f"{INTELLIGENCE_MIN}..{INTELLIGENCE_MAX}"
        )
    return value


def validate_beast_state(beast: Mapping[str, Any]) -> None:
    if not isinstance(beast, Mapping):
        raise RuleError("beast state must be an object")

    beast_id = _string(beast.get("beast_id"), "beast.beast_id")
    _string(beast.get("species_id"), f"{beast_id}.species_id")

    level = beast.get("level", 1)
    if isinstance(level, bool) or not isinstance(level, int) or level < 1:
        raise RuleError(f"{beast_id}.level must be an integer >= 1")

    _finite(
        beast.get("development_xp", 0.0),
        f"{beast_id}.development_xp",
        minimum=0.0,
    )
    _intelligence(beast.get("intelligence", 0), f"{beast_id}.intelligence")

    role = beast.get("role", "solitary")
    if role not in BEAST_ROLES:
        raise RuleError(f"Unsupported beast role: {role}")

    alive = beast.get("alive", True)
    if not isinstance(alive, bool):
        raise RuleError(f"{beast_id}.alive must be boolean")

    memory = beast.get("encounter_memory", {})
    if not isinstance(memory, Mapping):
        raise RuleError(f"{beast_id}.encounter_memory must be an object")

    for memory_key, record in memory.items():
        _string(memory_key, f"{beast_id}.encounter_memory key")
        if not isinstance(record, Mapping):
            raise RuleError(f"Encounter memory must be an object: {memory_key}")
        if record.get("kind") not in OBSERVATION_KINDS:
            raise RuleError(f"Unsupported encounter observation kind: {record.get('kind')}")
        _string(record.get("value"), f"{memory_key}.value")
        _non_negative_int(record.get("observations", 0), f"{memory_key}.observations")
        _finite(
            record.get("confidence", 0.0),
            f"{memory_key}.confidence",
            minimum=0.0,
            maximum=1.0,
        )
        _non_negative_int(record.get("first_seen", 0), f"{memory_key}.first_seen")
        _non_negative_int(record.get("last_seen", 0), f"{memory_key}.last_seen")

    adaptations = beast.get("adaptations", [])
    if not isinstance(adaptations, list) or not all(
        isinstance(item, str) and item for item in adaptations
    ):
        raise RuleError(f"{beast_id}.adaptations must be a list of non-empty strings")

    followers = beast.get("followers", [])
    if not isinstance(followers, list) or not all(
        isinstance(item, str) and item for item in followers
    ):
        raise RuleError(f"{beast_id}.followers must be a list of non-empty strings")


def encounter_memory_capacity(beast: Mapping[str, Any]) -> int:
    validate_beast_state(beast)
    intelligence = _intelligence(beast.get("intelligence", 0))
    return 4 + intelligence * 4


def _memory_key(kind: str, value: str) -> str:
    return f"{kind}:{value}"


def record_encounter_observation(
    beast: MutableMapping[str, Any],
    *,
    kind: str,
    value: str,
    time_minutes: int,
    confidence_increment: float = 0.25,
) -> Dict[str, Any]:
    """Persist one observed player/world pattern in bounded beast memory.

    Confidence grows from actual observations. Intelligence changes learning
    efficiency and memory capacity but never creates observations by itself.
    """
    if not isinstance(beast, MutableMapping):
        raise RuleError("beast state must be mutable")
    validate_beast_state(beast)
    if kind not in OBSERVATION_KINDS:
        raise RuleError(f"Unsupported encounter observation kind: {kind}")
    value = _string(value, "observation value")
    time_minutes = _non_negative_int(time_minutes, "observation time_minutes")
    confidence_increment = _finite(
        confidence_increment,
        "observation confidence_increment",
        minimum=0.0,
        maximum=1.0,
    )

    existing_memory = beast.get("encounter_memory")
    if existing_memory is None:
        memory: MutableMapping[str, Any] = {}
        beast["encounter_memory"] = memory
    elif not isinstance(existing_memory, MutableMapping):
        raise RuleError("beast.encounter_memory must be mutable")
    else:
        memory = existing_memory

    intelligence = _intelligence(beast.get("intelligence", 0))
    learning_factor = 0.50 + 0.10 * intelligence
    key = _memory_key(kind, value)
    existing = memory.get(key)

    if existing is None:
        record = {
            "kind": kind,
            "value": value,
            "observations": 1,
            "confidence": round(confidence_increment * learning_factor, 4),
            "first_seen": time_minutes,
            "last_seen": time_minutes,
        }
        memory[key] = record
    else:
        if not isinstance(existing, MutableMapping):
            raise RuleError(f"Encounter memory must be mutable: {key}")
        observations = _non_negative_int(existing.get("observations", 0), f"{key}.observations")
        old_confidence = _finite(
            existing.get("confidence", 0.0),
            f"{key}.confidence",
            minimum=0.0,
            maximum=1.0,
        )
        new_confidence = old_confidence + (
            (1.0 - old_confidence) * confidence_increment * learning_factor
        )
        existing["observations"] = observations + 1
        existing["confidence"] = round(min(1.0, new_confidence), 4)
        existing["last_seen"] = time_minutes
        record = dict(existing)

    capacity = encounter_memory_capacity(beast)
    if len(memory) > capacity:
        candidates = [
            (memory_key, memory_record)
            for memory_key, memory_record in memory.items()
            if memory_key != key
        ]
        if candidates:
            evict_key, _ = min(
                candidates,
                key=lambda pair: (
                    float(pair[1].get("confidence", 0.0)),
                    int(pair[1].get("last_seen", 0)),
                    pair[0],
                ),
            )
            del memory[evict_key]

    return dict(memory[key])


def adaptation_readiness(
    beast: Mapping[str, Any],
    *,
    kind: str,
    value: str,
    adaptation_type: str,
    elapsed_minutes: int = 0,
    resource_score: float = 0.0,
) -> Dict[str, Any]:
    """Explain whether observed evidence is sufficient for an adaptation.

    This does not choose or apply a counter. It only evaluates whether the beast
    has enough evidence/capability for authored adaptation logic to consider one.
    """
    validate_beast_state(beast)
    if kind not in OBSERVATION_KINDS:
        raise RuleError(f"Unsupported encounter observation kind: {kind}")
    value = _string(value, "observation value")
    if adaptation_type not in ADAPTATION_TYPES:
        raise RuleError(f"Unsupported adaptation type: {adaptation_type}")
    elapsed_minutes = _non_negative_int(elapsed_minutes, "elapsed_minutes")
    resource_score = _finite(
        resource_score,
        "resource_score",
        minimum=0.0,
        maximum=1.0,
    )

    requirements = _ADAPTATION_REQUIREMENTS[adaptation_type]
    intelligence = _intelligence(beast.get("intelligence", 0))
    record = beast.get("encounter_memory", {}).get(_memory_key(kind, value))

    reasons: list[str] = []
    observations = 0
    confidence = 0.0
    if record is None:
        reasons.append("no_observation")
    else:
        observations = _non_negative_int(
            record.get("observations", 0),
            "memory observations",
        )
        confidence = _finite(
            record.get("confidence", 0.0),
            "memory confidence",
            minimum=0.0,
            maximum=1.0,
        )

    if intelligence < int(requirements["min_intelligence"]):
        reasons.append("insufficient_intelligence")
    if observations < int(requirements["min_observations"]):
        reasons.append("insufficient_observations")
    if confidence < float(requirements["min_confidence"]):
        reasons.append("insufficient_confidence")

    if adaptation_type == "biological":
        if elapsed_minutes < int(requirements["min_elapsed_minutes"]):
            reasons.append("insufficient_time")
        if resource_score < float(requirements["min_resource_score"]):
            reasons.append("insufficient_resources")

    return {
        "adaptation_type": adaptation_type,
        "kind": kind,
        "value": value,
        "ready": not reasons,
        "observations": observations,
        "confidence": confidence,
        "reasons": reasons,
    }


def communication_tier(
    beast: Mapping[str, Any],
    species_definition: Mapping[str, Any],
) -> int:
    """Return capability tier limited by both intelligence and species anatomy."""
    validate_beast_state(beast)
    if not isinstance(species_definition, Mapping):
        raise RuleError("species_definition must be an object")

    max_tier = species_definition.get("max_communication_tier", 0)
    if (
        isinstance(max_tier, bool)
        or not isinstance(max_tier, int)
        or max_tier < INTELLIGENCE_MIN
        or max_tier > INTELLIGENCE_MAX
    ):
        raise RuleError(
            "species max_communication_tier must be an integer in range 0..5"
        )

    return min(_intelligence(beast.get("intelligence", 0)), max_tier)


def command_eligibility(
    beast: Mapping[str, Any],
    species_definition: Mapping[str, Any],
) -> Dict[str, Any]:
    """Evaluate authored leadership requirements without equating level to command."""
    validate_beast_state(beast)
    if not isinstance(species_definition, Mapping):
        raise RuleError("species_definition must be an object")

    social_species = species_definition.get("social_species", False)
    if not isinstance(social_species, bool):
        raise RuleError("species social_species must be boolean")

    requirements = species_definition.get("command_requirements", {})
    if not isinstance(requirements, Mapping):
        raise RuleError("species command_requirements must be an object")

    min_intelligence = requirements.get("min_intelligence", 4)
    _intelligence(min_intelligence, "command min_intelligence")

    min_level = requirements.get("min_level", 1)
    if isinstance(min_level, bool) or not isinstance(min_level, int) or min_level < 1:
        raise RuleError("command min_level must be an integer >= 1")

    min_followers = requirements.get("min_followers", 1)
    if (
        isinstance(min_followers, bool)
        or not isinstance(min_followers, int)
        or min_followers < 0
    ):
        raise RuleError("command min_followers must be a non-negative integer")

    reasons: list[str] = []
    if not social_species:
        reasons.append("species_not_social")
    if beast.get("intelligence", 0) < min_intelligence:
        reasons.append("insufficient_intelligence")
    if beast.get("level", 1) < min_level:
        reasons.append("insufficient_level")
    if len(beast.get("followers", [])) < min_followers:
        reasons.append("insufficient_followers")
    if beast.get("alive", True) is False:
        reasons.append("not_alive")

    return {
        "eligible": not reasons,
        "reasons": reasons,
        "required": {
            "min_intelligence": min_intelligence,
            "min_level": min_level,
            "min_followers": min_followers,
            "social_species": True,
        },
    }
