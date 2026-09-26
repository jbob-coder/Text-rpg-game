from __future__ import annotations

from typing import Any, Dict


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

# Derived values that represent physical/resource capacities have a hard floor.
# Contest-style values may legitimately go below zero under severe penalties.
DERIVED_STAT_SPECS: Dict[str, Dict[str, Any]] = {
    "max_health": {"min": 0.0, "role": "maximum health capacity"},
    "max_stamina": {"min": 0.0, "role": "maximum stamina capacity"},
    "max_focus": {"min": 0.0, "role": "maximum focus capacity"},
    "max_resolve": {"min": 0.0, "role": "maximum resolve capacity"},
    "initiative": {"min": None, "role": "turn/order readiness score"},
    "accuracy": {"min": None, "role": "attack/precision score"},
    "evasion": {"min": None, "role": "avoidance score"},
    "guard": {"min": None, "role": "defensive score"},
    "carry_capacity": {"min": 0.0, "role": "maximum carrying capacity"},
}
