from __future__ import annotations

from dataclasses import dataclass, field
from hashlib import sha256
from typing import Any, Dict, List, Mapping, MutableMapping, Optional

from .modifiers import effective_player_value, validate_modifier_mapping


class RuleError(ValueError):
    """Raised when authored game data violates the engine contract."""


def _get_path(data: Mapping[str, Any], path: str, default: Any = None) -> Any:
    current: Any = data
    for part in path.split("."):
        if not isinstance(current, Mapping) or part not in current:
            return default
        current = current[part]
    return current


def _set_path(data: MutableMapping[str, Any], path: str, value: Any) -> None:
    parts = path.split(".")
    current: MutableMapping[str, Any] = data
    for part in parts[:-1]:
        node = current.get(part)
        if not isinstance(node, MutableMapping):
            node = {}
            current[part] = node
        current = node
    current[parts[-1]] = value


def _add_path(data: MutableMapping[str, Any], path: str, delta: float) -> None:
    current = _get_path(data, path, 0)
    if not isinstance(current, (int, float)) or isinstance(current, bool):
        raise RuleError(f"Cannot add numeric delta to non-numeric path: {path}")
    _set_path(data, path, current + delta)


@dataclass
class GameState:
    """Authoritative mutable state for one playthrough.

    The engine intentionally stores plain serializable values. A future UI can be
    Godot, Android, desktop, or web without changing the rules layer.
    """

    seed: str
    scene_id: str
    turn: int = 0
    time_minutes: int = 0
    player: Dict[str, Any] = field(default_factory=dict)
    flags: Dict[str, Any] = field(default_factory=dict)
    relationships: Dict[str, Dict[str, float]] = field(default_factory=dict)
    knowledge: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    inventory: Dict[str, int] = field(default_factory=dict)
    quests: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    npcs: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    party: List[str] = field(default_factory=list)
    abilities: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    equipment: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    perks: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    schema_version: int = 1
    history: List[Dict[str, Any]] = field(default_factory=list)

    def snapshot(self) -> Dict[str, Any]:
        return {
            "seed": self.seed,
            "scene_id": self.scene_id,
            "turn": self.turn,
            "time_minutes": self.time_minutes,
            "player": self.player,
            "flags": self.flags,
            "relationships": self.relationships,
            "knowledge": self.knowledge,
            "inventory": self.inventory,
            "quests": self.quests,
            "npcs": self.npcs,
            "party": self.party,
            "abilities": self.abilities,
            "equipment": self.equipment,
            "perks": self.perks,
            "schema_version": self.schema_version,
            "history": self.history,
        }


class RulesEngine:
    """Data-driven, deterministic rules engine for authored RPG content.

    No generative AI is required at runtime. Content is explicit and testable.
    """

    def __init__(
        self,
        scenes: Mapping[str, Dict[str, Any]],
        *,
        set_definitions: Mapping[str, Mapping[str, Any]] | None = None,
    ):
        self.scenes = dict(scenes)
        self.set_definitions = dict(set_definitions or {})
        try:
            for set_id, definition in self.set_definitions.items():
                thresholds = definition.get("thresholds", {})
                if not isinstance(thresholds, Mapping):
                    raise ValueError(f"Set thresholds must be an object: {set_id}")
                for pieces, bonus in thresholds.items():
                    if not isinstance(bonus, Mapping):
                        raise ValueError(f"Set bonus must be an object: {set_id}:{pieces}")
                    validate_modifier_mapping(
                        bonus.get("modifiers", {}),
                        source=f"set:{set_id}:{pieces}",
                    )
        except ValueError as exc:
            raise RuleError(f"Invalid set definitions: {exc}") from exc

    def get_scene(self, state: GameState) -> Dict[str, Any]:
        try:
            return self.scenes[state.scene_id]
        except KeyError as exc:
            raise RuleError(f"Unknown scene: {state.scene_id}") from exc

    def available_choices(self, state: GameState) -> List[Dict[str, Any]]:
        scene = self.get_scene(state)
        output: List[Dict[str, Any]] = []
        for choice in scene.get("choices", []):
            if self._conditions_met(state, choice.get("visible_if", [])):
                entry = dict(choice)
                entry["enabled"] = self._conditions_met(state, choice.get("requires", []))
                if not entry["enabled"]:
                    entry["disabled_reason"] = choice.get("disabled_reason", "Requirements not met")
                output.append(entry)
        return output

    def choose(self, state: GameState, choice_id: str) -> Dict[str, Any]:
        choices = {c["id"]: c for c in self.available_choices(state)}
        if choice_id not in choices:
            raise RuleError(f"Choice is not currently visible: {choice_id}")
        choice = choices[choice_id]
        if not choice["enabled"]:
            raise RuleError(f"Choice is currently locked: {choice_id}")

        result_key = "default"
        check_result: Optional[Dict[str, Any]] = None
        if "check" in choice:
            check_result = self._resolve_check(state, choice["check"], choice_id)
            result_key = check_result["degree"]

        outcome = choice.get("outcomes", {}).get(result_key)
        if outcome is None:
            outcome = choice.get("outcomes", {}).get("default", {})

        before_scene = state.scene_id
        self._apply_effects(state, outcome.get("effects", []))
        state.time_minutes += int(choice.get("time_cost_minutes", 0))
        state.turn += 1

        next_scene = outcome.get("next_scene", choice.get("next_scene"))
        if next_scene:
            if next_scene not in self.scenes:
                raise RuleError(f"Outcome points to unknown scene: {next_scene}")
            state.scene_id = next_scene

        event = {
            "turn": state.turn,
            "scene": before_scene,
            "choice": choice_id,
            "check": check_result,
            "outcome": result_key,
            "next_scene": state.scene_id,
            "time_minutes": state.time_minutes,
        }
        state.history.append(event)
        return event

    def _conditions_met(self, state: GameState, conditions: List[Dict[str, Any]]) -> bool:
        for condition in conditions:
            kind = condition.get("type")
            if kind == "flag":
                actual = state.flags.get(condition["key"])
                if actual != condition.get("equals", True):
                    return False
            elif kind == "stat_min":
                actual = self._effective_player_value(state, condition["path"])
                if actual < condition["value"]:
                    return False
            elif kind == "stat_max":
                actual = self._effective_player_value(state, condition["path"])
                if actual > condition["value"]:
                    return False
            elif kind == "relationship_min":
                actual = state.relationships.get(condition["npc"], {}).get(condition["axis"], 0)
                if actual < condition["value"]:
                    return False
            elif kind == "knows":
                if condition["knowledge_id"] not in state.knowledge:
                    return False
            elif kind == "npc_knows":
                npc = state.npcs.get(condition["npc"], {})
                if condition["knowledge_id"] not in npc.get("knowledge", {}):
                    return False
            elif kind == "party_has":
                if condition["npc"] not in state.party:
                    return False
            elif kind == "ability_rank_min":
                rank = state.abilities.get(condition["ability_id"], {}).get("rank", 0)
                if rank < condition["value"]:
                    return False
            elif kind == "has_perk":
                if condition["perk_id"] not in state.perks:
                    return False
            elif kind == "item_min":
                if state.inventory.get(condition["item_id"], 0) < condition.get("quantity", 1):
                    return False
            else:
                raise RuleError(f"Unknown condition type: {kind}")
        return True

    def _effective_player_value(self, state: GameState, path: str) -> float:
        if path.startswith("derived."):
            # Local import avoids a module-import cycle: stats depends on GameState.
            from .stats import derived_stats

            key = path.removeprefix("derived.")
            values = derived_stats(state, self.set_definitions)
            if key not in values:
                raise RuleError(f"Unknown derived stat: {path}")
            return float(values[key])
        try:
            return effective_player_value(state, path, self.set_definitions)
        except ValueError as exc:
            raise RuleError(f"Invalid effective player value for {path}: {exc}") from exc

    def _resolve_check(self, state: GameState, check: Dict[str, Any], choice_id: str) -> Dict[str, Any]:
        stat_path = check["stat"]
        stat = float(self._effective_player_value(state, stat_path))
        skill = float(self._effective_player_value(state, check.get("skill", "skills.none"))) if check.get("skill") else 0.0
        difficulty = float(check.get("difficulty", 50))
        variance = float(check.get("variance", 10))

        digest = sha256(f"{state.seed}|{state.turn}|{state.scene_id}|{choice_id}".encode("utf-8")).digest()
        normalized = int.from_bytes(digest[:8], "big") / float(2**64 - 1)
        roll = (normalized * 2.0 - 1.0) * variance
        score = stat + skill * float(check.get("skill_weight", 0.5)) + roll
        margin = score - difficulty

        thresholds = check.get(
            "degrees",
            {"critical_success": 20, "success": 0, "failure": -20, "critical_failure": -999999},
        )
        ordered = sorted(thresholds.items(), key=lambda kv: kv[1], reverse=True)
        degree = ordered[-1][0]
        for name, minimum_margin in ordered:
            if margin >= float(minimum_margin):
                degree = name
                break

        return {
            "stat": stat_path,
            "base": stat,
            "skill": skill,
            "roll": round(roll, 3),
            "difficulty": difficulty,
            "score": round(score, 3),
            "margin": round(margin, 3),
            "degree": degree,
        }

    def _apply_effects(self, state: GameState, effects: List[Dict[str, Any]]) -> None:
        for effect in effects:
            kind = effect["type"]
            if kind == "set_flag":
                state.flags[effect["key"]] = effect.get("value", True)
            elif kind == "add_player":
                _add_path(state.player, effect["path"], effect["value"])
            elif kind == "set_player":
                _set_path(state.player, effect["path"], effect["value"])
            elif kind == "relationship":
                npc = state.relationships.setdefault(effect["npc"], {})
                npc[effect["axis"]] = npc.get(effect["axis"], 0) + effect["value"]
            elif kind == "learn":
                state.knowledge[effect["knowledge_id"]] = {
                    "source": effect.get("source", "unknown"),
                    "confidence": effect.get("confidence", 1.0),
                    "private": effect.get("private", False),
                    "turn_learned": state.turn,
                }
            elif kind == "inventory":
                item_id = effect["item_id"]
                state.inventory[item_id] = state.inventory.get(item_id, 0) + effect["quantity"]
                if state.inventory[item_id] <= 0:
                    state.inventory.pop(item_id, None)
            elif kind == "quest_stage":
                quest = state.quests.setdefault(effect["quest_id"], {})
                quest["stage"] = effect["stage"]
                quest["status"] = effect.get("status", quest.get("status", "active"))
            elif kind == "npc_learn":
                npc = state.npcs.setdefault(effect["npc"], {})
                knowledge = npc.setdefault("knowledge", {})
                knowledge[effect["knowledge_id"]] = {
                    "source": effect.get("source", "unknown"),
                    "confidence": effect.get("confidence", 1.0),
                    "turn_learned": state.turn,
                }
            elif kind == "personality":
                npc = state.npcs.setdefault(effect["npc"], {})
                personality = npc.setdefault("personality", {})
                axis = effect["axis"]
                personality[axis] = max(-100, min(100, personality.get(axis, 0) + effect["value"]))
            elif kind == "party_add":
                npc_id = effect["npc"]
                if npc_id not in state.party:
                    state.party.append(npc_id)
            elif kind == "party_remove":
                npc_id = effect["npc"]
                if npc_id in state.party:
                    state.party.remove(npc_id)
            elif kind == "add_perk":
                try:
                    modifiers = validate_modifier_mapping(
                        effect.get("modifiers", {}),
                        source=f"perk:{effect['perk_id']}",
                    )
                except ValueError as exc:
                    raise RuleError(
                        f"Invalid perk modifiers for {effect['perk_id']}: {exc}"
                    ) from exc
                state.perks[effect["perk_id"]] = {
                    "source": effect.get("source", "unknown"),
                    "modifiers": modifiers,
                    "tags": effect.get("tags", []),
                }
            else:
                raise RuleError(f"Unknown effect type: {kind}")
