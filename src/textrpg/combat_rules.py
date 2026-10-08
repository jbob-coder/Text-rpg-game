"""Transient knowledge, objective and retreat transactions above CombatSession."""
from __future__ import annotations

from contextlib import contextmanager
from copy import deepcopy
from dataclasses import dataclass
import hashlib
import math
from typing import Mapping

from .combat_grid import has_line_of_sight
from .combat_knowledge import CombatKnowledge, distance
from .combat_state import ACTIVATION_COMPLETE, CombatSession


_KINDS = {"ELIMINATE", "ESCAPE", "SURVIVE_ROUNDS", "REACH_CELL", "PROTECT_ACTOR",
          "INTERACT_RETRIEVE", "DISABLE_OBJECT", "CAPTURE_ACTOR"}
_INTERACTIONS = {"INTERACT_RETRIEVE", "DISABLE_OBJECT", "CAPTURE_ACTOR"}


def _number(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{label} must be finite numeric data")
    return float(value)


@dataclass(frozen=True)
class DetectionStats:
    """Resolved inputs from the actor's existing stat authority, not a stat model."""
    perception: float
    stealth: float
    sight_range: int = 6

    def __post_init__(self):
        _number(self.perception, "perception")
        _number(self.stealth, "stealth")
        if isinstance(self.sight_range, bool) or not isinstance(self.sight_range, int) or self.sight_range < 0:
            raise ValueError("sight range must be a non-negative integer")


@dataclass(frozen=True)
class Objective:
    objective_id: str
    kind: str
    actor_id: str
    anchor_id: str | None = None
    target_ids: tuple[str, ...] = ()
    rounds: int | None = None
    required: bool = True

    def __post_init__(self):
        if any(not isinstance(value, str) or not value for value in (self.objective_id, self.actor_id)):
            raise ValueError("objective and actor IDs must be non-empty text")
        if self.kind not in _KINDS:
            raise ValueError("unsupported objective kind")
        if not isinstance(self.required, bool):
            raise ValueError("objective.required must be boolean")
        if self.rounds is not None and (isinstance(self.rounds, bool)
                or not isinstance(self.rounds, int) or self.rounds < 1):
            raise ValueError("objective rounds must be a positive integer")
        object.__setattr__(self, "target_ids", tuple(self.target_ids))
        if len(set(self.target_ids)) != len(self.target_ids):
            raise ValueError("objective target IDs must be unique")


class EncounterRules:
    def __init__(self, session: CombatSession, *, controller_id: str, objectives=(),
                 action_loadouts: Mapping[str, tuple[str, ...]],
                 knowledge: CombatKnowledge | None = None,
                 detection_stats: Mapping[str, DetectionStats] | None = None,
                 detection_variance: float = 10):
        self.session = session
        if controller_id not in session.actors:
            raise ValueError("unknown encounter controller")
        self.controller_id = controller_id
        self.knowledge = knowledge or CombatKnowledge(session)
        if self.knowledge.session is not session:
            raise ValueError("knowledge belongs to another session")
        self.action_loadouts = {key: tuple(value) for key, value in action_loadouts.items()}
        if set(self.action_loadouts) != set(session.actors):
            raise ValueError("every actor requires an explicit action loadout")
        for loadout in self.action_loadouts.values():
            if len(loadout) > 16 or len(set(loadout)) != len(loadout):
                raise ValueError("action loadouts require at most 16 unique actions")
            for action_id in loadout:
                session._action_definition(action_id)
                session._action_cost(action_id)
        self.detection_stats = {key: DetectionStats(0, 0) for key in session.actors}
        for key, value in (detection_stats or {}).items():
            if key not in session.actors or not isinstance(value, DetectionStats):
                raise ValueError("invalid detection stat binding")
            self.detection_stats[key] = value
        self.detection_variance = _number(detection_variance, "detection variance")
        if self.detection_variance < 0:
            raise ValueError("detection variance cannot be negative")
        values = tuple(objectives)
        if any(not isinstance(objective, Objective) for objective in values):
            raise ValueError("objectives must contain Objective values")
        self.objectives = {objective.objective_id: objective for objective in values}
        if len(self.objectives) != len(values):
            raise ValueError("duplicate objective ID")
        self.anchors = {anchor.anchor_id: anchor.coord for anchor in session.tactical_map.objective_anchors}
        self.exits = {anchor.anchor_id: anchor.coord for anchor in session.tactical_map.exits}
        for objective in values:
            if objective.actor_id not in session.actors or any(
                    actor_id not in session.actors for actor_id in objective.target_ids):
                raise ValueError("objective references unknown actor")
            if objective.kind in {"REACH_CELL", "INTERACT_RETRIEVE", "DISABLE_OBJECT"}:
                if objective.anchor_id not in self.anchors:
                    raise ValueError("objective references unknown anchor")
            if objective.kind == "ESCAPE" and objective.anchor_id not in self.exits:
                raise ValueError("escape objective requires an authored exit")
            if objective.kind in {"SURVIVE_ROUNDS", "PROTECT_ACTOR"} and objective.rounds is None:
                raise ValueError("timed objective requires a round count")
            if objective.kind in {"ELIMINATE", "PROTECT_ACTOR", "CAPTURE_ACTOR"} and not objective.target_ids:
                raise ValueError("objective requires target actors")
            if objective.kind == "CAPTURE_ACTOR" and len(objective.target_ids) != 1:
                raise ValueError("capture requires exactly one target")
        self.objective_results = {key: "pending" for key in self.objectives}
        self.interactions: set[str] = set()
        self.departures: dict[str, str] = {}

    @contextmanager
    def _atomic(self):
        fields = ("round_index", "activation_index", "event_index", "active_actor_id",
                  "encounter_status", "committed_events", "initiative_order", "round_initiative")
        before = {key: deepcopy(getattr(self.session, key)) for key in fields}
        actors = {key: deepcopy(vars(actor)) for key, actor in self.session.actors.items()}
        contacts = dict(self.knowledge.contacts)
        results, interactions, departures = (dict(self.objective_results),
                                             set(self.interactions), dict(self.departures))
        try:
            yield
        except Exception:
            for key, value in before.items():
                setattr(self.session, key, value)
            for key, value in actors.items():
                vars(self.session.actors[key]).clear()
                vars(self.session.actors[key]).update(value)
            self.knowledge.contacts = contacts
            self.objective_results, self.interactions, self.departures = results, interactions, departures
            raise

    def action(self, actor_id, action_id, *, category=None):
        actor = self.session._active_actor(actor_id)
        if action_id not in self.action_loadouts.get(actor_id, ()):
            raise ValueError("action is not in actor loadout")
        definition = self.session._action_definition(action_id)
        if category is not None and definition.get("category") != category:
            raise ValueError("action category does not match requested operation")
        if actor.action_budget < self.session._action_cost(action_id):
            raise ValueError("insufficient action budget")
        return actor, definition

    def _commit_event(self, actor, action_id, target_key, change=lambda: None):
        budget, reserve, coord = actor.action_budget, actor.reaction_reserve, actor.coord
        actor.action_budget -= self.session._action_cost(action_id)
        change()
        return self.session._append_event(actor=actor, action_id=action_id,
            target_key=target_key, budget_before=budget, coord_before=coord,
            reserve_before=reserve, reserve_after=actor.reaction_reserve)

    def evaluate_objectives(self):
        if self.session.encounter_status != "active":
            return dict(self.objective_results)
        for key, objective in self.objectives.items():
            if self.objective_results[key] != "pending":
                continue
            actor = self.session.actors[objective.actor_id]
            targets = [self.session.actors[key] for key in objective.target_ids]
            complete = False
            failed = actor.incapacitated
            if objective.kind in _INTERACTIONS:
                complete = key in self.interactions
            elif objective.kind == "REACH_CELL":
                complete = not actor.withdrawn and actor.coord == self.anchors[objective.anchor_id]
            elif objective.kind == "ESCAPE":
                complete = self.departures.get(actor.actor_id) == objective.anchor_id
            elif objective.kind == "ELIMINATE":
                complete = all(target.incapacitated for target in targets)
            elif objective.kind in {"SURVIVE_ROUNDS", "PROTECT_ACTOR"}:
                complete = self.session.round_index > objective.rounds
                failed = failed or any(target.incapacitated for target in targets)
            if failed:
                self.objective_results[key] = "failed"
            elif complete:
                self.objective_results[key] = "completed"
        required = [self.objective_results[key] for key, objective in self.objectives.items()
                    if objective.required and objective.actor_id == self.controller_id]
        if self.session.actors[self.controller_id].incapacitated or "failed" in required:
            self.session.encounter_status = "failed"
        elif required and all(value == "completed" for value in required):
            self.session.encounter_status = "completed"
        return dict(self.objective_results)

    def commit_movement(self, actor_id, action_id, goal):
        self.action(actor_id, action_id)
        with self._atomic():
            try:
                event = self.session.commit_movement(actor_id=actor_id, action_id=action_id, goal=goal)
            except ValueError as exc:
                # Do not expose an unseen occupant or hidden alternative path.
                raise ValueError("movement unavailable") from exc
            for owner, target in tuple(self.knowledge.contacts):
                contact = self.knowledge.contact(owner, target)
                if contact.awareness == "SUSPECTED":
                    self.knowledge.contacts[owner, target] = contact
            self.refresh_awareness(event)
            self.evaluate_objectives()
            return event

    def preview_interaction(self, actor_id, action_id, objective_id):
        actor, definition = self.action(actor_id, action_id, category="interact")
        objective = self.objectives.get(objective_id)
        if (objective is None or objective.actor_id != actor_id
                or objective.kind not in _INTERACTIONS
                or self.objective_results[objective_id] != "pending"):
            raise ValueError("interaction unavailable")
        if objective.kind == "CAPTURE_ACTOR":
            target = self.session.actors[objective.target_ids[0]]
            if not target.incapacitated or target.actor_id not in self.knowledge.detected_actor_ids(actor_id):
                raise ValueError("capture unavailable")
            coord = target.coord
        else:
            coord = self.anchors[objective.anchor_id]
        if not definition.get("range_min", 0) <= distance(actor.coord, coord) <= definition.get("range_max", 0):
            raise ValueError("interaction out of range")
        if definition.get("requires_los") and not has_line_of_sight(self.session.tactical_map, actor.coord, coord):
            raise ValueError("interaction lacks line of sight")
        return coord

    def commit_interaction(self, actor_id, action_id, objective_id):
        self.preview_interaction(actor_id, action_id, objective_id)
        actor, _ = self.action(actor_id, action_id, category="interact")
        with self._atomic():
            event = self._commit_event(actor, action_id, objective_id,
                                       lambda: self.interactions.add(objective_id))
            self.evaluate_objectives()
            return event

    def preview_retreat(self, actor_id, action_id, exit_id):
        actor, _ = self.action(actor_id, action_id, category="retreat")
        if exit_id not in self.exits or actor.coord != self.exits[exit_id]:
            raise ValueError("retreat requires reaching an authored exit")
        return actor.coord

    def commit_retreat(self, actor_id, action_id, exit_id):
        self.preview_retreat(actor_id, action_id, exit_id)
        actor, _ = self.action(actor_id, action_id, category="retreat")

        def depart():
            actor.withdrawn = True
            actor.action_budget = actor.reaction_reserve = 0
            actor.reserved_reaction_id = None
            actor.activation_state = ACTIVATION_COMPLETE
            self.session.active_actor_id = None
            self.departures[actor_id] = exit_id

        with self._atomic():
            event = self._commit_event(actor, action_id, exit_id, depart)
            self.evaluate_objectives()
            if actor_id == self.controller_id and self.session.encounter_status == "active":
                self.session.encounter_status = "retreated"
            return event

    def commit_detection(self, actor_id, action_id):
        actor, definition = self.action(actor_id, action_id, category="detect")
        with self._atomic():
            event = self._commit_event(actor, action_id, "DETECTION_SCAN")
            self._detect_observer(actor_id, event, definition.get("range_max", 0))
            return event

    def _detect_observer(self, observer_id, event, max_range):
        observer = self.session.actors[observer_id]
        stats = self.detection_stats.get(observer_id, DetectionStats(0, 0))
        for target_id, target in sorted(self.session.actors.items()):
            if target_id == observer_id or target.withdrawn or target.reinforcement_round > self.session.round_index:
                continue
            separation = distance(observer.coord, target.coord)
            visible = (separation <= max_range and has_line_of_sight(
                self.session.tactical_map, observer.coord, target.coord))
            digest = hashlib.sha256(f"{event.digest}|{observer_id}|{target_id}".encode()).digest()
            roll = (int.from_bytes(digest[:8], "big") / (2**64 - 1) * 2 - 1) * self.detection_variance
            cell = self.session.tactical_map.cell_at(target.coord)
            margin = (stats.perception
                      - self.detection_stats.get(target_id, DetectionStats(0, 0)).stealth
                      - separation - cell.concealment + roll)
            self.knowledge.record_detection(observer_id, target_id, detected=visible and margin >= 0)

    def refresh_awareness(self, event):
        """Resolve movement-triggered detection inside the event's transaction."""
        if not self.session.committed_events or self.session.committed_events[-1] is not event:
            raise ValueError("awareness requires the latest committed combat event")
        for observer_id, observer in sorted(self.session.actors.items()):
            if (not observer.withdrawn and not observer.incapacitated
                    and observer.reinforcement_round <= self.session.round_index):
                stats = self.detection_stats.get(observer_id, DetectionStats(0, 0))
                self._detect_observer(observer_id, event, stats.sight_range)

    def advance_round(self):
        with self._atomic():
            order = self.session.advance_round()
            self.evaluate_objectives()
            return order

    def player_view(self, observer_id):
        view = self.knowledge.player_view(observer_id)
        view["objectives"] = [{"objective_id": key, "kind": objective.kind,
                               "status": self.objective_results[key]}
                              for key, objective in sorted(self.objectives.items())
                              if objective.actor_id == observer_id]
        view["encounter_status"] = self.session.encounter_status
        return view
