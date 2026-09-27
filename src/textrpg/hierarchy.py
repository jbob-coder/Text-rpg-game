from __future__ import annotations

from typing import Any, Dict, Mapping, MutableMapping

from .beasts import BEAST_ROLES, validate_beast_state
from .core import RuleError
from .territory import validate_region_state


def _string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise RuleError(f"{label} must be a non-empty string")
    return value


def _non_negative_int(value: Any, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise RuleError(f"{label} must be a non-negative integer")
    return value


def validate_role_definitions(definitions: Mapping[str, Mapping[str, Any]]) -> None:
    if not isinstance(definitions, Mapping):
        raise RuleError("role definitions must be an object")
    seen_ranks: set[int] = set()
    for role_id, definition in definitions.items():
        if role_id not in BEAST_ROLES:
            raise RuleError(f"Unsupported beast role definition: {role_id}")
        if not isinstance(definition, Mapping):
            raise RuleError(f"Role definition must be an object: {role_id}")
        rank = _non_negative_int(definition.get("rank"), f"{role_id}.rank")
        if rank in seen_ranks:
            raise RuleError(f"Role rank must be unique: {rank}")
        seen_ranks.add(rank)
        _non_negative_int(definition.get("min_intelligence", 0), f"{role_id}.min_intelligence")
        _non_negative_int(definition.get("min_level", 1), f"{role_id}.min_level")
        _non_negative_int(definition.get("min_followers", 0), f"{role_id}.min_followers")
        _non_negative_int(definition.get("min_victories", 0), f"{role_id}.min_victories")
        _non_negative_int(definition.get("min_territories", 0), f"{role_id}.min_territories")
        for field in ("requires_social_species", "can_control_territory"):
            value = definition.get(field, False)
            if not isinstance(value, bool):
                raise RuleError(f"{role_id}.{field} must be boolean")


def role_eligibility(
    beast: Mapping[str, Any],
    species_definition: Mapping[str, Any],
    role_id: str,
    definitions: Mapping[str, Mapping[str, Any]],
    *,
    victories: int = 0,
    territories_controlled: int = 0,
) -> Dict[str, Any]:
    validate_beast_state(beast)
    validate_role_definitions(definitions)
    if not isinstance(species_definition, Mapping):
        raise RuleError("species_definition must be an object")
    role_id = _string(role_id, "role_id")
    if role_id not in definitions:
        raise RuleError(f"Unknown role definition: {role_id}")
    victories = _non_negative_int(victories, "victories")
    territories_controlled = _non_negative_int(territories_controlled, "territories_controlled")

    definition = definitions[role_id]
    social_species = species_definition.get("social_species", False)
    if not isinstance(social_species, bool):
        raise RuleError("species social_species must be boolean")

    reasons: list[str] = []
    if definition.get("requires_social_species", False) and not social_species:
        reasons.append("species_not_social")
    if beast.get("intelligence", 0) < definition.get("min_intelligence", 0):
        reasons.append("insufficient_intelligence")
    if beast.get("level", 1) < definition.get("min_level", 1):
        reasons.append("insufficient_level")
    if len(beast.get("followers", [])) < definition.get("min_followers", 0):
        reasons.append("insufficient_followers")
    if victories < definition.get("min_victories", 0):
        reasons.append("insufficient_victories")
    if territories_controlled < definition.get("min_territories", 0):
        reasons.append("insufficient_territories")
    if beast.get("alive", True) is False:
        reasons.append("not_alive")

    return {
        "role_id": role_id,
        "eligible": not reasons,
        "rank": definition["rank"],
        "reasons": reasons,
        "can_control_territory": definition.get("can_control_territory", False),
    }


def highest_eligible_role(
    beast: Mapping[str, Any],
    species_definition: Mapping[str, Any],
    definitions: Mapping[str, Mapping[str, Any]],
    *,
    victories: int = 0,
    territories_controlled: int = 0,
) -> Dict[str, Any] | None:
    validate_role_definitions(definitions)
    eligible: list[Dict[str, Any]] = []
    for role_id in definitions:
        result = role_eligibility(
            beast,
            species_definition,
            role_id,
            definitions,
            victories=victories,
            territories_controlled=territories_controlled,
        )
        if result["eligible"]:
            eligible.append(result)
    if not eligible:
        return None
    eligible.sort(key=lambda entry: (-entry["rank"], entry["role_id"]))
    return eligible[0]


def apply_role_promotion(
    beast: MutableMapping[str, Any],
    species_definition: Mapping[str, Any],
    definitions: Mapping[str, Mapping[str, Any]],
    target_role: str,
    *,
    victories: int = 0,
    territories_controlled: int = 0,
) -> Dict[str, Any]:
    if not isinstance(beast, MutableMapping):
        raise RuleError("beast state must be mutable")
    validate_beast_state(beast)
    validate_role_definitions(definitions)
    target = role_eligibility(
        beast,
        species_definition,
        target_role,
        definitions,
        victories=victories,
        territories_controlled=territories_controlled,
    )
    if not target["eligible"]:
        raise RuleError(f"Beast is not eligible for role {target_role}: {target['reasons']}")

    current_role = beast.get("role", "solitary")
    if current_role not in definitions:
        raise RuleError(f"Current beast role has no authored definition: {current_role}")
    current_rank = definitions[current_role]["rank"]
    if target["rank"] <= current_rank:
        raise RuleError("Role promotion must increase authored role rank")

    beast["role"] = target_role
    return {
        "before_role": current_role,
        "after_role": target_role,
        "before_rank": current_rank,
        "after_rank": target["rank"],
    }


def assign_region_controller(
    region: MutableMapping[str, Any],
    beast: Mapping[str, Any],
    definitions: Mapping[str, Mapping[str, Any]],
) -> Dict[str, Any]:
    if not isinstance(region, MutableMapping):
        raise RuleError("region state must be mutable")
    validate_region_state(region)
    validate_beast_state(beast)
    validate_role_definitions(definitions)
    role = beast.get("role", "solitary")
    if role not in definitions:
        raise RuleError(f"Current beast role has no authored definition: {role}")
    if definitions[role].get("can_control_territory", False) is not True:
        raise RuleError(f"Beast role cannot control territory: {role}")
    if beast["beast_id"] not in region.get("beast_ids", []):
        raise RuleError("Territory controller must be present in region beast_ids")

    previous = region.get("territory_controller")
    region["territory_controller"] = beast["beast_id"]
    return {
        "region_id": region["region_id"],
        "previous_controller": previous,
        "new_controller": beast["beast_id"],
        "controller_role": role,
    }
