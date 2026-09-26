from __future__ import annotations

from typing import Any, Dict, Mapping

from .core import GameState, RuleError
from .modifiers import effective_player_value, modifier_totals


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
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise RuleError(f"Expected numeric value for {key}")
    return float(value)


def _effective(
    state: GameState,
    path: str,
    set_definitions: Mapping[str, Mapping[str, Any]] | None,
) -> float:
    try:
        return effective_player_value(state, path, set_definitions)
    except ValueError as exc:
        raise RuleError(f"Invalid effective player value for {path}: {exc}") from exc


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
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            errors.append(f"attribute {key} must be numeric")
            continue
        spec = ATTRIBUTE_SPECS[key]
        if value < spec["min"] or value > spec["max"]:
            errors.append(f"attribute {key} out of range {spec['min']}..{spec['max']}: {value}")
    for key, value in skills.items():
        if key not in SKILL_CATALOG:
            errors.append(f"unknown skill: {key}")
        if isinstance(value, bool) or not isinstance(value, (int, float)) or value < 0 or value > 100:
            errors.append(f"skill {key} must be numeric in range 0..100")
    return errors


def derived_stats(
    state: GameState,
    set_definitions: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, float]:
    might = _effective(state, "attributes.might", set_definitions)
    agility = _effective(state, "attributes.agility", set_definitions)
    endurance = _effective(state, "attributes.endurance", set_definitions)
    intellect = _effective(state, "attributes.intellect", set_definitions)
    will = _effective(state, "attributes.will", set_definitions)
    perception = _effective(state, "attributes.perception", set_definitions)
    presence = _effective(state, "attributes.presence", set_definitions)
    athletics = _effective(state, "skills.athletics", set_definitions)
    defense = _effective(state, "skills.defense", set_definitions)
    ranged = _effective(state, "skills.ranged", set_definitions)
    leadership = _effective(state, "skills.leadership", set_definitions)

    modifiers = modifier_totals(state, set_definitions)

    def direct(name: str) -> float:
        return float(modifiers.get(f"derived.{name}", 0.0))

    return {
        "max_health": round(50 + endurance * 2.0 + will * 0.5 + direct("max_health"), 2),
        "max_stamina": round(40 + endurance * 1.5 + athletics * 0.5 + direct("max_stamina"), 2),
        "max_focus": round(30 + intellect * 0.8 + will * 0.7 + direct("max_focus"), 2),
        "max_resolve": round(25 + will * 1.1 + presence * 0.35 + leadership * 0.15 + direct("max_resolve"), 2),
        "initiative": round(agility * 0.7 + perception * 0.3 + direct("initiative"), 2),
        "accuracy": round(perception * 0.55 + agility * 0.20 + ranged * 0.25 + direct("accuracy"), 2),
        "evasion": round(agility * 0.65 + perception * 0.20 + athletics * 0.15 + direct("evasion"), 2),
        "guard": round(endurance * 0.45 + might * 0.25 + defense * 0.30 + direct("guard"), 2),
        "carry_capacity": round(10 + might * 0.8 + endurance * 0.2 + direct("carry_capacity"), 2),
    }


def initialize_resources(
    state: GameState,
    *,
    refill: bool = False,
    set_definitions: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, float]:
    resources = state.player.setdefault("resources", {})
    derived = derived_stats(state, set_definitions)
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
