"""Bounded deterministic decision packages; no UI or omniscient target queries."""
from __future__ import annotations

from dataclasses import dataclass

from .combat_grid import cover_rating
from .combat_knowledge import distance
from .combat_rules import EncounterRules
from .combat_schema import TacticalCoord


@dataclass(frozen=True)
class AIProfile:
    doctrine: str = "cautious"
    hostile_actor_ids: tuple[str, ...] = ()
    must_withdraw: bool = False
    max_candidates: int = 64
    max_destinations: int = 24

    def __post_init__(self):
        if self.doctrine not in {"cautious", "aggressive", "companion", "beast"}:
            raise ValueError("unknown AI doctrine")
        if not isinstance(self.must_withdraw, bool):
            raise ValueError("must_withdraw must be boolean")
        for value, limit in ((self.max_candidates, 64), (self.max_destinations, 24)):
            if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= limit:
                raise ValueError("AI limits exceed the Phase 1 bounds")
        object.__setattr__(self, "hostile_actor_ids", tuple(self.hostile_actor_ids))


@dataclass(frozen=True)
class CompanionOrder:
    kind: str
    target_actor_id: str | None = None

    def __post_init__(self):
        if self.kind not in {"HOLD", "ADVANCE", "FOCUS_TARGET", "ASSIST", "WITHDRAW"}:
            raise ValueError("unknown companion order")
        if self.kind in {"FOCUS_TARGET", "ASSIST"} and not self.target_actor_id:
            raise ValueError("order requires a target")


@dataclass(frozen=True)
class ActionCandidate:
    action_id: str
    target_key: str = ""
    goal: TacticalCoord | None = None
    utility: int = 0
    path_key: str = ""


@dataclass(frozen=True)
class AIDecision:
    selected: ActionCandidate
    candidates: tuple[ActionCandidate, ...]

    @property
    def diagnostics(self):
        """Developer-only data; never passed through EncounterRules.player_view."""
        return {
            "selected": {"action_id": self.selected.action_id, "target": self.selected.target_key},
            "candidate_count": len(self.candidates),
            "candidates": [{"action_id": c.action_id, "target": c.target_key,
                            "utility": c.utility, "path": c.path_key} for c in self.candidates],
            "tie_break": "action_id, target_key, path_key",
        }


def choose_action(rules: EncounterRules, actor_id: str, *,
                  profile: AIProfile | None = None, order: CompanionOrder | None = None,
                  goal: TacticalCoord | None = None) -> AIDecision:
    """Select one knowledge-legal package; its eventual commit must revalidate.

    Bounded Phase 1 heuristics prioritize objective completion and withdrawal.
    Target pressure is a flat known-target heuristic, not a damage prediction.
    Attack/ability effect execution remains the authored action resolver's job.
    """
    profile = profile or AIProfile()
    session = rules.session
    actor = session._active_actor(actor_id)
    if not isinstance(profile, AIProfile) or (order is not None and not isinstance(order, CompanionOrder)):
        raise ValueError("invalid AI profile/order")
    loadout = tuple(sorted(rules.action_loadouts.get(actor_id, ())))
    legal = []
    for action_id in loadout:
        try:
            _, definition = rules.action(actor_id, action_id)
        except ValueError:
            continue
        legal.append((action_id, definition))
    ends = [action_id for action_id, definition in legal
            if definition.get("category") == "end_activation" and session._action_cost(action_id) == 0]
    if not ends:
        raise ValueError("AI requires a legal zero-cost End Activation")
    candidates = [ActionCandidate(ends[0])]

    def offer(candidate):
        if len(candidates) < profile.max_candidates:
            candidates.append(candidate)

    detected = rules.knowledge.detected_actor_ids(actor_id)
    threats = tuple(target for target in detected if target in profile.hostile_actor_ids)
    objectives = tuple(objective for key, objective in sorted(rules.objectives.items())
                       if objective.actor_id == actor_id and rules.objective_results[key] == "pending")
    withdrawing = profile.must_withdraw or (order is not None and order.kind == "WITHDRAW")
    if withdrawing and rules.exits:
        goal = min(rules.exits.values(), key=lambda coord: (distance(actor.coord, coord), coord.key))
    elif order and order.kind == "ASSIST" and order.target_actor_id in detected:
        goal = rules.knowledge.contact(actor_id, order.target_actor_id).coord
    elif goal is None:
        goal = next((rules.anchors[objective.anchor_id] for objective in objectives
                     if objective.anchor_id in rules.anchors), None)
    if goal is not None and (not isinstance(goal, TacticalCoord) or session.tactical_map.cell_at(goal) is None):
        raise ValueError("AI goal must be an authored map cell")

    # Essential objective/exit packages precede optional movement pruning.
    for action_id, definition in legal:
        if len(candidates) >= profile.max_candidates:
            break
        category = definition.get("category")
        cost = session._action_cost(action_id)
        if category == "interact":
            for objective in objectives:
                if len(candidates) >= profile.max_candidates:
                    break
                try:
                    rules.preview_interaction(actor_id, action_id, objective.objective_id)
                except ValueError:
                    continue
                offer(ActionCandidate(action_id, objective.objective_id, utility=1000 - cost))
        elif category == "retreat":
            for exit_id in sorted(rules.exits):
                if len(candidates) >= profile.max_candidates:
                    break
                try:
                    rules.preview_retreat(actor_id, action_id, exit_id)
                except ValueError:
                    continue
                completes_escape = any(o.kind == "ESCAPE" and o.anchor_id == exit_id for o in objectives)
                utility = (1000 if completes_escape else 800 if withdrawing else -100) - cost
                offer(ActionCandidate(action_id, exit_id, utility=utility))
        elif category in {"attack", "ability"}:
            for target_id in threats:
                if len(candidates) >= profile.max_candidates:
                    break
                try:
                    preview = rules.knowledge.preview_target(actor_id, action_id, target_actor_id=target_id)
                except ValueError:
                    continue
                pressure = {"cautious": 40, "aggressive": 80, "companion": 40, "beast": 50}[profile.doctrine]
                utility = pressure - (preview.cover_defense or 0) - cost
                if order and order.kind == "FOCUS_TARGET" and order.target_actor_id == target_id:
                    utility += 150
                offer(ActionCandidate(action_id, target_id, utility=utility))

    def movement_utility(coord, *, apply_order=True):
        progress = distance(actor.coord, goal) - distance(coord, goal) if goal else 0
        utility = progress * 5
        if withdrawing and progress > 0:
            utility += 800
        for objective in objectives:
            if objective.kind == "REACH_CELL" and coord == rules.anchors[objective.anchor_id]:
                utility += 1000
        cover_value = 0
        for target_id in threats:
            known = rules.knowledge.contact(actor_id, target_id)
            if coord != known.coord and coord.z == known.coord.z:
                cover_weight = 20 if profile.doctrine == "cautious" else 10
                cover_value += cover_rating(session.tactical_map, known.coord, coord) * cover_weight
        utility += min(100, cover_value)
        if apply_order and order:
            if order.kind == "HOLD":
                utility -= 150
            elif order.kind in {"ADVANCE", "ASSIST"} and progress > 0:
                utility += 50 if order.kind == "ADVANCE" else 150
        return utility

    destinations = sorted((coord for coord in rules.knowledge.visible_cells(actor_id) if coord != actor.coord),
                          key=lambda coord: (-movement_utility(coord, apply_order=False), coord.key))
    for coord in destinations[:profile.max_destinations]:
        if len(candidates) >= profile.max_candidates:
            break
        for action_id, definition in legal:
            if definition.get("category") not in {"move", "sprint"}:
                continue
            try:
                plan = rules.knowledge.preview_movement(actor_id, action_id, coord)
            except ValueError:
                continue
            offer(ActionCandidate(action_id, coord.key, coord,
                                  movement_utility(coord) - plan.action_budget_cost,
                                  ";".join(step.key for step in plan.path)))
    ordered = tuple(sorted(candidates, key=lambda c: (c.action_id, c.target_key, c.path_key)))
    selected = min(ordered, key=lambda c: (-c.utility, c.action_id, c.target_key, c.path_key))
    return AIDecision(selected, ordered)
