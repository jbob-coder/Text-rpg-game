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

# Formula definitions are data so runtime calculations, explainability, tests,
# documentation, and future UI can refer to one source of truth.
DERIVED_FORMULAS: Dict[str, Dict[str, Any]] = {
    "max_health": {
        "base": 50.0,
        "terms": {"attributes.endurance": 2.0, "attributes.will": 0.5},
    },
    "max_stamina": {
        "base": 40.0,
        "terms": {"attributes.endurance": 1.5, "skills.athletics": 0.5},
    },
    "max_focus": {
        "base": 30.0,
        "terms": {"attributes.intellect": 0.8, "attributes.will": 0.7},
    },
    "max_resolve": {
        "base": 25.0,
        "terms": {
            "attributes.will": 1.1,
            "attributes.presence": 0.35,
            "skills.leadership": 0.15,
        },
    },
    "initiative": {
        "base": 0.0,
        "terms": {"attributes.agility": 0.7, "attributes.perception": 0.3},
    },
    "accuracy": {
        "base": 0.0,
        "terms": {
            "attributes.perception": 0.55,
            "attributes.agility": 0.20,
            "skills.ranged": 0.25,
        },
    },
    "evasion": {
        "base": 0.0,
        "terms": {
            "attributes.agility": 0.65,
            "attributes.perception": 0.20,
            "skills.athletics": 0.15,
        },
    },
    "guard": {
        "base": 0.0,
        "terms": {
            "attributes.endurance": 0.45,
            "attributes.might": 0.25,
            "skills.defense": 0.30,
        },
    },
    "carry_capacity": {
        "base": 10.0,
        "terms": {"attributes.might": 0.8, "attributes.endurance": 0.2},
    },
}

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
