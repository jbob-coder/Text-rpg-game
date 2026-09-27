from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
from hashlib import sha256
from math import isfinite
from typing import Any, Dict, List, Mapping, MutableMapping, Optional

from .modifiers import (
    effective_player_value as _hardened_effective_player_value,
    modifier_breakdown,
    resolve_set_context,
    validate_modifier_mapping,
    validate_set_definitions,
)


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
    if (
        isinstance(current, bool)
        or not isinstance(current, (int, float))
        or not isfinite(float(current))
        or isinstance(delta, bool)
        or not isinstance(delta, (int, float))
        or not isfinite(float(delta))
    ):
        raise RuleError(f"Cannot add invalid numeric delta/value at path: {path}")
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


def _restore_snapshot(state: GameState, snapshot: Mapping[str, Any]) -> None:
    """Restore a deep-copied GameState snapshot after a failed transaction."""
    for key, value in snapshot.items():
        setattr(state, key, value)


def effective_player_value(
    state: GameState,
    path: str,
    *,
    equipment_sets: Optional[Mapping[str, Mapping[str, Any]]] = None,
    set_definitions: Optional[Mapping[str, Mapping[str, Any]]] = None,
) -> float:
    """Compatibility wrapper over the single hardened effective-value pipeline."""
    try:
        resolved = resolve_set_context(
            set_definitions,
            equipment_sets=equipment_sets,
        )
        return float(
            _hardened_effective_player_value(
                state,
                path,
                resolved,
            )
        )
    except ValueError as exc:
        raise RuleError(f"Invalid effective player value for {path}: {exc}") from exc


class RulesEngine:
    """Data-driven, deterministic rules engine for authored RPG content.

    No generative AI is required at runtime. Content is explicit and testable.
    """

    def __init__(
        self,
        scenes: Mapping[str, Dict[str, Any]],
        *,
        equipment_sets: Optional[Mapping[str, Mapping[str, Any]]] = None,
        quest_definitions: Optional[Mapping[str, Mapping[str, Any]]] = None,
        power_definitions: Optional[Mapping[str, Mapping[str, Any]]] = None,
        set_definitions: Optional[Mapping[str, Mapping[str, Any]]] = None,
    ):
        self.scenes = dict(scenes)
        try:
            resolved_sets = resolve_set_context(
                set_definitions,
                equipment_sets=equipment_sets,
            )
            self.equipment_sets = dict(resolved_sets or {})
            validate_set_definitions(self.equipment_sets)
        except ValueError as exc:
            raise RuleError(f"Invalid equipment-set definitions: {exc}") from exc
        self.set_definitions = self.equipment_sets
        self.quest_definitions = dict(quest_definitions or {})
        self.power_definitions = dict(power_definitions or {})

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
        if not isinstance(outcome, Mapping):
            raise RuleError(f"Choice outcome must be an object: {choice_id}:{result_key}")

        time_cost = choice.get("time_cost_minutes", 0)
        if isinstance(time_cost, bool) or not isinstance(time_cost, int) or time_cost < 0:
            raise RuleError(
                f"Choice time cost must be a non-negative integer: {choice_id}"
            )

        next_scene = outcome.get("next_scene", choice.get("next_scene"))
        if next_scene is not None:
            if not isinstance(next_scene, str) or not next_scene:
                raise RuleError(f"Choice next_scene must be a non-empty string: {choice_id}")
            if next_scene not in self.scenes:
                raise RuleError(f"Outcome points to unknown scene: {next_scene}")

        if isinstance(state.turn, bool) or not isinstance(state.turn, int) or state.turn < 0:
            raise RuleError("state.turn must be a non-negative integer")
        if not isinstance(state.history, list):
            raise RuleError("state.history must be a list")

        if time_cost:
            from .simulation import validate_time_advance

            validate_time_advance(state, time_cost)

        before_scene = state.scene_id
        snapshot = deepcopy(state.snapshot())

        try:
            self._apply_effects(state, outcome.get("effects", []))
            if time_cost:
                from .simulation import advance_time

                advance_time(state, time_cost)

            state.turn += 1
            if next_scene is not None:
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
        except Exception:
            _restore_snapshot(state, snapshot)
            raise

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
            elif kind == "relationship_max":
                actual = state.relationships.get(condition["npc"], {}).get(condition["axis"], 0)
                if actual > condition["value"]:
                    return False
            elif kind == "knows":
                if condition["knowledge_id"] not in state.knowledge:
                    return False
            elif kind == "not_knows":
                if condition["knowledge_id"] in state.knowledge:
                    return False
            elif kind == "npc_knows":
                npc = state.npcs.get(condition["npc"], {})
                if condition["knowledge_id"] not in npc.get("knowledge", {}):
                    return False
            elif kind == "npc_not_knows":
                npc = state.npcs.get(condition["npc"], {})
                if condition["knowledge_id"] in npc.get("knowledge", {}):
                    return False
            elif kind == "party_has":
                if condition["npc"] not in state.party:
                    return False
            elif kind == "ability_rank_min":
                rank = state.abilities.get(condition["ability_id"], {}).get("rank", 0)
                if rank < condition["value"]:
                    return False
            elif kind == "technique_discoverable":
                from .powers import technique_discovery_status

                ability_id = condition["ability_id"]
                technique_id = condition["technique_id"]
                power_definition = self.power_definitions.get(ability_id)
                if power_definition is None:
                    return False
                technique_definition = power_definition.get("techniques", {}).get(
                    technique_id
                )
                if technique_definition is None:
                    return False
                if not technique_discovery_status(
                    state,
                    ability_id,
                    technique_id,
                    technique_definition,
                    equipment_sets=self.equipment_sets,
                )["available"]:
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

    def explain_player_value(self, state: GameState, path: str) -> Dict[str, Any]:
        """Explain one effective/derived value without duplicating rule arithmetic."""
        if path.startswith("derived."):
            from .stats import derived_stat_breakdown

            key = path.removeprefix("derived.")
            breakdown = derived_stat_breakdown(
                state,
                key,
                equipment_sets=self.equipment_sets,
            )
            return {
                "kind": "derived",
                "path": path,
                "total": float(breakdown["total"]),
                "breakdown": breakdown,
            }

        try:
            breakdown = modifier_breakdown(
                state,
                path,
                equipment_sets=self.equipment_sets,
            )
        except ValueError as exc:
            raise RuleError(f"Invalid effective player value for {path}: {exc}") from exc
        return {
            "kind": "effective",
            "path": path,
            "total": float(breakdown["total"]),
            "breakdown": breakdown,
        }

    def _effective_player_value(self, state: GameState, path: str) -> float:
        return float(self.explain_player_value(state, path)["total"])

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
                axis = effect["axis"]
                value = float(npc.get(axis, 0)) + float(effect["value"])
                npc[axis] = max(-100.0, min(100.0, value))
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
                # Legacy direct-stage effect. New authored content should prefer the
                # graph-aware quest_start/quest_objective_* effects below.
                quest = state.quests.setdefault(effect["quest_id"], {})
                quest["stage"] = effect["stage"]
                quest["status"] = effect.get("status", quest.get("status", "active"))
            elif kind == "quest_start":
                from .quests import start_quest

                quest_id = effect["quest_id"]
                definition = self.quest_definitions.get(quest_id)
                if definition is None:
                    raise RuleError(f"Unknown quest definition: {quest_id}")
                start_quest(state, quest_id, definition)
            elif kind == "quest_objective_complete":
                from .quests import complete_objective

                quest_id = effect["quest_id"]
                definition = self.quest_definitions.get(quest_id)
                if definition is None:
                    raise RuleError(f"Unknown quest definition: {quest_id}")
                complete_objective(
                    state,
                    quest_id,
                    effect["objective_id"],
                    definition,
                )
            elif kind == "quest_objective_fail":
                from .quests import fail_objective

                quest_id = effect["quest_id"]
                definition = self.quest_definitions.get(quest_id)
                if definition is None:
                    raise RuleError(f"Unknown quest definition: {quest_id}")
                fail_objective(
                    state,
                    quest_id,
                    effect["objective_id"],
                    definition,
                )
            elif kind == "quest_fail":
                from .quests import fail_quest

                quest_id = effect["quest_id"]
                if quest_id not in self.quest_definitions:
                    raise RuleError(f"Unknown quest definition: {quest_id}")
                fail_quest(
                    state,
                    quest_id,
                    reason=effect.get("reason", "authored_scene"),
                )
            elif kind == "npc_learn":
                npc = state.npcs.setdefault(effect["npc"], {})
                knowledge = npc.setdefault("knowledge", {})
                knowledge[effect["knowledge_id"]] = {
                    "source": effect.get("source", "unknown"),
                    "confidence": effect.get("confidence", 1.0),
                    "turn_learned": state.turn,
                }
            elif kind == "npc_goal_create":
                from .social import set_goal

                set_goal(
                    state,
                    effect["npc"],
                    effect["goal_id"],
                    priority=int(effect.get("priority", 50)),
                    progress=float(effect.get("progress", 0)),
                    status=effect.get("status", "active"),
                    source=effect.get("source", "authored_scene"),
                    data=effect.get("data"),
                )
            elif kind == "npc_goal_progress":
                from .social import update_goal_progress

                update_goal_progress(
                    state,
                    effect["npc"],
                    effect["goal_id"],
                    float(effect["delta"]),
                    completion_threshold=float(
                        effect.get("completion_threshold", 100)
                    ),
                )
            elif kind == "npc_story_transition":
                from .social import transition_story_state

                transition_story_state(
                    state,
                    effect["npc"],
                    effect["track_id"],
                    effect["to_state"],
                    allowed_from=effect.get("allowed_from"),
                    reason=effect.get("reason", "authored_scene"),
                    data=effect.get("data"),
                )
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
            elif kind == "ability_discover":
                from .powers import discover_ability

                ability_id = effect["ability_id"]
                definition = self.power_definitions.get(ability_id)
                discover_ability(
                    state,
                    ability_id,
                    family=effect.get(
                        "family",
                        definition.get("family", "unknown") if definition else "unknown",
                    ),
                    form=effect.get(
                        "form",
                        definition.get("form") if definition else None,
                    ),
                    tags=effect.get(
                        "tags",
                        definition.get("tags", ()) if definition else (),
                    ),
                    data=effect.get("data"),
                    definition=definition,
                )
            elif kind == "technique_discover":
                from .powers import discover_technique

                ability_id = effect["ability_id"]
                technique_id = effect["technique_id"]
                power_definition = self.power_definitions.get(ability_id)
                technique_definition = None
                if power_definition is not None:
                    technique_definition = power_definition.get("techniques", {}).get(
                        technique_id
                    )
                    if technique_definition is None:
                        raise RuleError(
                            f"Unknown technique definition: {ability_id}/{technique_id}"
                        )
                discover_technique(
                    state,
                    ability_id,
                    technique_id,
                    technique_definition,
                    equipment_sets=self.equipment_sets,
                )
            elif kind == "technique_practice":
                from .powers import practice_technique

                practice_technique(
                    state,
                    effect["ability_id"],
                    effect["technique_id"],
                    minutes=int(effect["minutes"]),
                    intensity=float(effect.get("intensity", 1.0)),
                    mentor_bonus=float(effect.get("mentor_bonus", 0.0)),
                    stamina_per_hour=float(effect.get("stamina_per_hour", 4.0)),
                    focus_per_hour=float(effect.get("focus_per_hour", 6.0)),
                )
            elif kind == "technique_use":
                from .powers import use_technique

                ability_id = effect["ability_id"]
                technique_id = effect["technique_id"]
                definition = self.power_definitions.get(ability_id)
                if definition is None:
                    raise RuleError(f"Unknown power definition: {ability_id}")
                technique_definition = definition.get("techniques", {}).get(technique_id)
                if technique_definition is None:
                    raise RuleError(
                        f"Unknown technique definition: {ability_id}/{technique_id}"
                    )
                use_technique(
                    state,
                    ability_id,
                    technique_id,
                    technique_definition,
                    equipment_sets=self.equipment_sets,
                )
            elif kind == "power_recover":
                from .powers import recover_power_resource

                ability_id = effect["ability_id"]
                definition = self.power_definitions.get(ability_id)
                if definition is None:
                    raise RuleError(f"Unknown power definition: {ability_id}")
                recover_power_resource(
                    state,
                    ability_id,
                    definition,
                    minutes=int(effect["minutes"]),
                    quality=float(effect.get("quality", 1.0)),
                )
            else:
                raise RuleError(f"Unknown effect type: {kind}")
