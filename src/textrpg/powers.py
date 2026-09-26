from __future__ import annotations

from typing import Any, Dict, Mapping, MutableMapping

from .core import GameState, RuleError
from .progression import technique_available
from .simulation import apply_condition


TECHNIQUE_STAGES = (
    (0, "discovered"),
    (10, "unstable"),
    (40, "learned"),
    (120, "practiced"),
    (300, "mastered"),
)

_STAGE_ORDER = {
    "unknown": -1,
    "discovered": 0,
    "unstable": 1,
    "learned": 2,
    "practiced": 3,
    "mastered": 4,
}


def technique_stage(xp: float) -> str:
    if xp < 0:
        raise RuleError("Technique mastery XP cannot be negative")
    stage = "unknown"
    for threshold, name in TECHNIQUE_STAGES:
        if xp >= threshold:
            stage = name
        else:
            break
    return stage


def _player_path(state: GameState, path: str) -> Any:
    current: Any = state.player
    for part in path.split("."):
        if not isinstance(current, Mapping) or part not in current:
            return None
        current = current[part]
    return current


def _set_player_path(state: GameState, path: str, value: Any) -> None:
    parts = path.split(".")
    current: MutableMapping[str, Any] = state.player
    for part in parts[:-1]:
        node = current.get(part)
        if not isinstance(node, MutableMapping):
            node = {}
            current[part] = node
        current = node
    current[parts[-1]] = value


def _numeric_player_path(state: GameState, path: str) -> float:
    value = _player_path(state, path)
    if not isinstance(value, (int, float)):
        raise RuleError(f"Power resource path is missing or non-numeric: {path}")
    return float(value)


def discover_technique(state: GameState, ability_id: str, technique_id: str) -> Dict[str, Any]:
    ability = state.abilities.get(ability_id)
    if not ability:
        raise RuleError(f"Unknown ability: {ability_id}")
    techniques = ability.setdefault("techniques", {})
    if technique_id in techniques:
        return techniques[technique_id]
    record = {
        "mastery_xp": 0.0,
        "stage": "discovered",
        "uses": 0,
        "ready_at_minutes": state.time_minutes,
        "discovered_at_minutes": state.time_minutes,
    }
    techniques[technique_id] = record
    return record


def gain_technique_mastery(
    state: GameState,
    ability_id: str,
    technique_id: str,
    xp: float,
) -> Dict[str, Any]:
    if xp < 0:
        raise RuleError("Technique mastery gain cannot be negative")
    ability = state.abilities.get(ability_id)
    if not ability:
        raise RuleError(f"Unknown ability: {ability_id}")
    technique = ability.get("techniques", {}).get(technique_id)
    if not technique:
        raise RuleError(f"Technique has not been discovered: {technique_id}")

    before = dict(technique)
    technique["mastery_xp"] = float(technique.get("mastery_xp", 0.0)) + float(xp)
    technique["stage"] = technique_stage(technique["mastery_xp"])
    return {"before": before, "after": dict(technique)}


def _stage_at_least(actual: str, minimum: str) -> bool:
    if actual not in _STAGE_ORDER:
        raise RuleError(f"Unknown technique stage: {actual}")
    if minimum not in _STAGE_ORDER:
        raise RuleError(f"Unknown required technique stage: {minimum}")
    return _STAGE_ORDER[actual] >= _STAGE_ORDER[minimum]


def _extra_requirements_met(
    state: GameState,
    requirements: Mapping[str, Any],
) -> list[str]:
    reasons: list[str] = []

    attributes = state.player.get("attributes", {})
    for key, minimum in requirements.get("attributes", {}).items():
        if float(attributes.get(key, 0)) < float(minimum):
            reasons.append(f"attribute:{key}")

    skills = state.player.get("skills", {})
    for key, minimum in requirements.get("skills", {}).items():
        if float(skills.get(key, 0)) < float(minimum):
            reasons.append(f"skill:{key}")

    for key, expected in requirements.get("flags", {}).items():
        if state.flags.get(key) != expected:
            reasons.append(f"flag:{key}")

    for item_id, quantity in requirements.get("items", {}).items():
        if state.inventory.get(item_id, 0) < int(quantity):
            reasons.append(f"item:{item_id}")

    return reasons


def technique_use_status(
    state: GameState,
    ability_id: str,
    technique_id: str,
    definition: Mapping[str, Any],
) -> Dict[str, Any]:
    reasons: list[str] = []
    ability = state.abilities.get(ability_id)
    if not ability:
        return {"available": False, "reasons": ["ability_missing"]}

    technique = ability.get("techniques", {}).get(technique_id)
    if not technique:
        return {"available": False, "reasons": ["technique_undiscovered"]}

    requirements = definition.get("requirements", {})
    if not technique_available(state, ability_id, dict(requirements)):
        reasons.append("ability_requirements")

    reasons.extend(_extra_requirements_met(state, requirements))

    minimum_stage = definition.get("stage_min", "discovered")
    if not _stage_at_least(technique.get("stage", "unknown"), minimum_stage):
        reasons.append(f"stage:{minimum_stage}")

    ready_at = int(technique.get("ready_at_minutes", 0))
    if state.time_minutes < ready_at:
        reasons.append(f"cooldown:{ready_at - state.time_minutes}")

    for path, amount_raw in definition.get("costs", {}).items():
        amount = float(amount_raw)
        if amount < 0:
            raise RuleError(f"Technique cost cannot be negative: {path}")
        current = _numeric_player_path(state, path)
        if current < amount:
            reasons.append(f"resource:{path}")

    cooldown = int(definition.get("cooldown_minutes", 0))
    if cooldown < 0:
        raise RuleError("Technique cooldown cannot be negative")

    mastery_gain = float(definition.get("mastery_gain", 0))
    if mastery_gain < 0:
        raise RuleError("Technique mastery gain cannot be negative")

    for drawback in definition.get("drawbacks", []):
        if drawback.get("type") != "condition":
            raise RuleError(f"Unsupported power drawback type: {drawback.get('type')}")
        severity = int(drawback.get("severity", 1))
        if severity < 1 or severity > 5:
            raise RuleError("Condition severity must be in range 1..5")
        duration = drawback.get("duration_minutes")
        if duration is not None and int(duration) < 0:
            raise RuleError("Condition duration cannot be negative")

    return {
        "available": not reasons,
        "reasons": reasons,
        "ready_at_minutes": ready_at,
    }


def use_technique(
    state: GameState,
    ability_id: str,
    technique_id: str,
    definition: Mapping[str, Any],
) -> Dict[str, Any]:
    status = technique_use_status(state, ability_id, technique_id, definition)
    if not status["available"]:
        raise RuleError(
            f"Technique cannot be used: {technique_id} ({', '.join(status['reasons'])})"
        )

    ability = state.abilities[ability_id]
    technique = ability["techniques"][technique_id]

    spent: Dict[str, float] = {}
    for path, amount_raw in definition.get("costs", {}).items():
        amount = float(amount_raw)
        before = _numeric_player_path(state, path)
        _set_player_path(state, path, before - amount)
        spent[path] = amount

    cooldown = int(definition.get("cooldown_minutes", 0))
    technique["ready_at_minutes"] = state.time_minutes + cooldown
    technique["uses"] = int(technique.get("uses", 0)) + 1

    applied_drawbacks: list[str] = []
    for drawback in definition.get("drawbacks", []):
        condition_id = drawback["condition_id"]
        apply_condition(
            state,
            condition_id,
            severity=int(drawback.get("severity", 1)),
            duration_minutes=drawback.get("duration_minutes"),
            source=f"technique:{ability_id}:{technique_id}",
            tags=drawback.get("tags", ()),
            modifiers=drawback.get("modifiers"),
        )
        applied_drawbacks.append(condition_id)

    mastery_gain = float(definition.get("mastery_gain", 0))
    mastery_result = None
    if mastery_gain:
        mastery_result = gain_technique_mastery(
            state, ability_id, technique_id, mastery_gain
        )

    event = {
        "type": "technique_use",
        "ability_id": ability_id,
        "technique_id": technique_id,
        "time_minutes": state.time_minutes,
        "spent": spent,
        "ready_at_minutes": technique["ready_at_minutes"],
        "drawbacks": applied_drawbacks,
        "mastery": mastery_result,
    }
    state.history.append(event)
    return event


def ability_evolution_status(
    state: GameState,
    ability_id: str,
    evolution_id: str,
    definition: Mapping[str, Any],
) -> Dict[str, Any]:
    ability = state.abilities.get(ability_id)
    if not ability:
        return {"available": False, "reasons": ["ability_missing"]}

    if evolution_id in {
        record.get("evolution_id") for record in ability.get("evolutions", [])
    }:
        return {"available": False, "reasons": ["already_evolved"]}

    requirements = definition.get("requirements", {})
    reasons: list[str] = []

    if ability.get("rank", 0) < int(requirements.get("rank_min", 0)):
        reasons.append("rank")
    if float(ability.get("mastery_xp", 0)) < float(
        requirements.get("mastery_xp_min", 0)
    ):
        reasons.append("mastery_xp")

    for knowledge_id in requirements.get("knowledge", []):
        if knowledge_id not in state.knowledge:
            reasons.append(f"knowledge:{knowledge_id}")

    for perk_id in requirements.get("perks", []):
        if perk_id not in state.perks:
            reasons.append(f"perk:{perk_id}")

    reasons.extend(_extra_requirements_met(state, requirements))

    techniques = ability.get("techniques", {})
    for required_id, stage_min in requirements.get("techniques", {}).items():
        record = techniques.get(required_id)
        if not record or not _stage_at_least(record.get("stage", "unknown"), stage_min):
            reasons.append(f"technique:{required_id}:{stage_min}")

    return {"available": not reasons, "reasons": reasons}


def evolve_ability(
    state: GameState,
    ability_id: str,
    evolution_id: str,
    definition: Mapping[str, Any],
) -> Dict[str, Any]:
    status = ability_evolution_status(state, ability_id, evolution_id, definition)
    if not status["available"]:
        raise RuleError(
            f"Ability cannot evolve: {evolution_id} ({', '.join(status['reasons'])})"
        )

    ability = state.abilities[ability_id]
    result = definition.get("result", {})
    previous_form = ability.get("form")
    if "form" in result:
        ability["form"] = result["form"]
    if "rank_floor" in result:
        ability["rank"] = max(int(ability.get("rank", 0)), int(result["rank_floor"]))

    if "tags" in result:
        tags = list(dict.fromkeys([*ability.get("tags", []), *result["tags"]]))
        ability["tags"] = tags

    granted_perks: list[str] = []
    for perk_id, perk in result.get("grant_perks", {}).items():
        state.perks[perk_id] = {
            "source": f"evolution:{ability_id}:{evolution_id}",
            "modifiers": dict(perk.get("modifiers", {})),
            "tags": list(perk.get("tags", [])),
        }
        granted_perks.append(perk_id)

    record = {
        "evolution_id": evolution_id,
        "time_minutes": state.time_minutes,
        "previous_form": previous_form,
        "form": ability.get("form"),
    }
    ability.setdefault("evolutions", []).append(record)

    event = {
        "type": "ability_evolution",
        "ability_id": ability_id,
        "evolution_id": evolution_id,
        "time_minutes": state.time_minutes,
        "previous_form": previous_form,
        "form": ability.get("form"),
        "granted_perks": granted_perks,
    }
    state.history.append(event)
    return event
