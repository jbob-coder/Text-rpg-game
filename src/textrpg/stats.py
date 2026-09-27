from __future__ import annotations

from typing import Any, Dict, Mapping

from .core import GameState, RuleError, effective_player_value as core_effective_player_value


ATTRIBUTE_SPECS: Dict[str, Dict[str, Any]] = {
    "might": {"min": 0, "max": 100, "pace": "slow", "role": "raw physical force"},
    "agility": {"min": 0, "max": 100, "pace": "slow", "role": "movement, coordination, reaction"},
    "endurance": {"min": 0, "max": 100, "pace": "slow", "role": "fatigue tolerance and resilience"},
    "intellect": {"min": 0, "max": 100, "pace": "slow", "role": "reasoning and technical learning"},
    "will": {"min": 0, "max": 100, "pace": "slow", "role": "mental resistance and discipline"},
    "perception": {"min": 0, "max": 100, "pace": "slow", "role": "awareness, danger, and tells"},
    "presence": {"min": 0, "max": 100, "pace": "slow", "role": "social force and leadership"},
}

SKILL_CATALOG: Dict[str, str] = {
    "unarmed": "combat",
    "blades": "combat",
    "ranged": "combat",
    "defense": "combat",
    "tactics": "combat",
    "athletics": "physical",
    "stealth": "physical",
    "traversal": "physical",
    "survival": "physical",
    "engineering": "technical",
    "technical_systems": "technical",
    "medicine": "technical",
    "crafting": "technical",
    "persuasion": "social",
    "deception": "social",
    "intimidation": "social",
    "empathy": "social",
    "leadership": "social",
    "investigation": "knowledge",
    "history": "knowledge",
    "factions": "knowledge",
    "powers": "knowledge",
    "creatures": "knowledge",
}

RESOURCE_KEYS = ("health", "stamina", "focus", "resolve")


def _num(mapping: Mapping[str, Any], key: str) -> float:
    value = mapping.get(key, 0)
    if not isinstance(value, (int, float)):
        raise RuleError(f"Expected numeric value for {key}")
    return float(value)


def validate_player_stats(state: GameState) -> list[str]:
    errors: list[str] = []
    attrs = state.player.get("attributes", {})
    skills = state.player.get("skills", {})
    if not isinstance(attrs, dict):
        return ["player.attributes must be an object"]
    if not isinstance(skills, dict):
        errors.append("player.skills must be an object")
        skills = {}
    for key, value in attrs.items():
        if key not in ATTRIBUTE_SPECS:
            errors.append(f"unknown attribute: {key}")
            continue
        if not isinstance(value, (int, float)):
            errors.append(f"attribute {key} must be numeric")
            continue
        spec = ATTRIBUTE_SPECS[key]
        if value < spec["min"] or value > spec["max"]:
            errors.append(f"attribute {key} out of range {spec['min']}..{spec['max']}: {value}")
    for key, value in skills.items():
        if key not in SKILL_CATALOG:
            errors.append(f"unknown skill: {key}")
        if not isinstance(value, (int, float)) or value < 0 or value > 100:
            errors.append(f"skill {key} must be numeric in range 0..100")
    return errors


def effective_player_value(
    state: GameState,
    path: str,
    *,
    equipment_sets: Mapping[str, Mapping[str, Any]] | None = None,
) -> float:
    """Public stats-layer alias for the shared core aggregation contract."""
    return core_effective_player_value(
        state,
        path,
        equipment_sets=equipment_sets,
    )


def derived_stats(
    state: GameState,
    *,
    equipment_sets: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, float]:
    """Calculate derived values from the shared effective-value contract."""
    def effective(path: str) -> float:
        return core_effective_player_value(
            state,
            path,
            equipment_sets=equipment_sets,
        )

    might = effective("attributes.might")
    agility = effective("attributes.agility")
    endurance = effective("attributes.endurance")
    intellect = effective("attributes.intellect")
    will = effective("attributes.will")
    perception = effective("attributes.perception")
    presence = effective("attributes.presence")
    athletics = effective("skills.athletics")
    defense = effective("skills.defense")
    ranged = effective("skills.ranged")
    leadership = effective("skills.leadership")

    values = {
        "max_health": 50 + endurance * 2.0 + will * 0.5,
        "max_stamina": 40 + endurance * 1.5 + athletics * 0.5,
        "max_focus": 30 + intellect * 0.8 + will * 0.7,
        "max_resolve": 25 + will * 1.1 + presence * 0.35 + leadership * 0.15,
        "initiative": agility * 0.7 + perception * 0.3,
        "accuracy": perception * 0.55 + agility * 0.20 + ranged * 0.25,
        "evasion": agility * 0.65 + perception * 0.20 + athletics * 0.15,
        "guard": endurance * 0.45 + might * 0.25 + defense * 0.30,
        "carry_capacity": 10 + might * 0.8 + endurance * 0.2,
    }

    for key in list(values):
        values[key] += effective(f"derived.{key}")
        values[key] = round(values[key], 2)
    return values


def initialize_resources(
    state: GameState,
    *,
    refill: bool = False,
    equipment_sets: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, float]:
    resources = state.player.setdefault("resources", {})
    derived = derived_stats(state, equipment_sets=equipment_sets)
    maxima = {
        "health": derived["max_health"],
        "stamina": derived["max_stamina"],
        "focus": derived["max_focus"],
        "resolve": derived["max_resolve"],
    }
    for key, maximum in maxima.items():
        max_key = f"max_{key}"
        resources[max_key] = maximum
        if refill or key not in resources:
            resources[key] = maximum
        else:
            resources[key] = min(float(resources[key]), maximum)
    return maxima
