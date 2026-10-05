"""Transient deterministic combat-session state for D-070.

This module deliberately owns encounter-local mutable state only. It consumes the
immutable tactical schema/grid authority from D-069 and does not mutate GameState
or save-schema data.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
import hashlib
import math
from typing import Iterable

from .combat_grid import TacticalOccupant, find_path, occupancy_by_coord
from .combat_schema import CARDINAL_DIRECTIONS, TacticalCoord, TacticalMap


PHASE1_ACTION_BUDGET = 4
PHASE1_MOVE_POINTS = 6
PHASE1_SPRINT_POINTS = 10

ACTIVATION_PENDING = "pending"
ACTIVATION_ACTIVE = "active"
ACTIVATION_RESOLVING_ACTION = "resolving_action"
ACTIVATION_WAITING_REACTION = "waiting_reaction"
ACTIVATION_COMPLETE = "complete"
ACTIVATION_SKIPPED = "skipped"

_ACTIVATION_STATES = {
    ACTIVATION_PENDING,
    ACTIVATION_ACTIVE,
    ACTIVATION_RESOLVING_ACTION,
    ACTIVATION_WAITING_REACTION,
    ACTIVATION_COMPLETE,
    ACTIVATION_SKIPPED,
}


def _require_non_empty_text(value: object, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{label} must be non-empty text")
    return value


def _require_initiative(value: object) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("actor.initiative must be numeric")
    result = float(value)
    if not math.isfinite(result):
        raise ValueError("actor.initiative must be finite")
    return result


@dataclass(frozen=True)
class MovementPlan:
    action_id: str
    path: tuple[TacticalCoord, ...]
    traversal_cost: int
    movement_allowance: int
    action_budget_cost: int


@dataclass(frozen=True)
class CombatEvent:
    event_index: int
    round_index: int
    activation_index: int
    actor_id: str
    action_id: str
    target_key: str
    budget_before: int
    budget_after: int
    coord_before: TacticalCoord
    coord_after: TacticalCoord
    digest: str


def path_traversal_cost(
    tactical_map: TacticalMap,
    path: tuple[TacticalCoord, ...],
) -> int:
    """Calculate traversal cost for a D-069-authoritative path."""

    if not path:
        raise ValueError("path must not be empty")
    total = 0
    for start, end in zip(path, path[1:]):
        transition_cost = next(
            (
                cost
                for target, cost in tactical_map.transition_targets(start)
                if target == end
            ),
            None,
        )
        if transition_cost is not None:
            total += transition_cost
            continue

        if start.z != end.z or abs(start.x - end.x) + abs(start.y - end.y) != 1:
            raise ValueError(
                f"path contains non-authoritative edge: {start.key} -> {end.key}"
            )
        destination = tactical_map.cell_at(end)
        if destination is None or destination.blocks_movement:
            raise ValueError(f"path enters non-traversable cell: {end.key}")
        total += destination.movement_cost
    return total


@dataclass
class TacticalActorState:
    """Encounter-local mutable actor state."""

    actor_id: str
    faction_id: str
    coord: TacticalCoord
    initiative: float
    facing: str = "N"
    action_budget: int = 0
    activation_state: str = ACTIVATION_PENDING
    incapacitated: bool = False

    def __post_init__(self) -> None:
        self.actor_id = _require_non_empty_text(self.actor_id, "actor.actor_id")
        self.faction_id = _require_non_empty_text(
            self.faction_id,
            "actor.faction_id",
        )
        if not isinstance(self.coord, TacticalCoord):
            raise ValueError("actor.coord must be TacticalCoord")
        self.initiative = _require_initiative(self.initiative)
        if self.facing not in CARDINAL_DIRECTIONS:
            raise ValueError("actor.facing must be one of N/E/S/W")
        if isinstance(self.action_budget, bool) or not isinstance(
            self.action_budget,
            int,
        ):
            raise ValueError("actor.action_budget must be an integer")
        if self.action_budget < 0:
            raise ValueError("actor.action_budget cannot be negative")
        if self.activation_state not in _ACTIVATION_STATES:
            raise ValueError("actor.activation_state is unsupported")
        if not isinstance(self.incapacitated, bool):
            raise ValueError("actor.incapacitated must be boolean")


class CombatSession:
    """Authoritative transient round/activation state."""

    def __init__(
        self,
        *,
        encounter_id: str,
        tactical_map: TacticalMap,
        seed: int,
        actors: Iterable[TacticalActorState],
        combat_actions: Mapping[str, Mapping[str, object]] | None = None,
    ) -> None:
        self.encounter_id = _require_non_empty_text(encounter_id, "encounter_id")
        if not isinstance(tactical_map, TacticalMap):
            raise ValueError("tactical_map must be TacticalMap")
        if isinstance(seed, bool) or not isinstance(seed, int):
            raise ValueError("seed must be an integer")

        actor_list = tuple(actors)
        if not actor_list:
            raise ValueError("combat session requires at least one actor")
        if any(not isinstance(actor, TacticalActorState) for actor in actor_list):
            raise ValueError("actors must contain TacticalActorState values")

        for actor in actor_list:
            cell = tactical_map.cell_at(actor.coord)
            if cell is None:
                raise ValueError(
                    f"actor {actor.actor_id} spawns on unknown cell "
                    f"{actor.coord.key}"
                )
            if cell.blocks_movement:
                raise ValueError(
                    f"actor {actor.actor_id} spawns on blocked cell "
                    f"{actor.coord.key}"
                )

        occupancy_by_coord(
            TacticalOccupant(
                actor.actor_id,
                actor.faction_id,
                actor.coord,
                solid=not actor.incapacitated,
            )
            for actor in actor_list
        )

        self.tactical_map = tactical_map
        self.seed = seed
        self.combat_actions = (
            {}
            if combat_actions is None
            else {action_id: dict(definition) for action_id, definition in combat_actions.items()}
        )
        self.actors = {actor.actor_id: actor for actor in actor_list}
        self.round_index = 1
        self.activation_index = 0
        self.event_index = 0
        self.active_actor_id: str | None = None
        self.committed_events: list[object] = []
        self.encounter_status = "active"
        self.initiative_order = self._snapshot_initiative_order()

    def _snapshot_initiative_order(self) -> tuple[str, ...]:
        eligible = [
            actor
            for actor in self.actors.values()
            if not actor.incapacitated
        ]
        eligible.sort(key=lambda actor: (-actor.initiative, actor.actor_id))
        return tuple(actor.actor_id for actor in eligible)

    def begin_next_activation(self) -> TacticalActorState | None:
        """Activate the next round-snapshot actor, skipping incapacity safely."""

        if self.active_actor_id is not None:
            active = self.actors[self.active_actor_id]
            if active.activation_state in {
                ACTIVATION_ACTIVE,
                ACTIVATION_RESOLVING_ACTION,
                ACTIVATION_WAITING_REACTION,
            }:
                raise ValueError("current activation must complete before advancing")
            self.active_actor_id = None

        while self.activation_index < len(self.initiative_order):
            actor_id = self.initiative_order[self.activation_index]
            self.activation_index += 1
            actor = self.actors[actor_id]
            if actor.incapacitated:
                actor.action_budget = 0
                actor.activation_state = ACTIVATION_SKIPPED
                continue

            actor.action_budget = PHASE1_ACTION_BUDGET
            actor.activation_state = ACTIVATION_ACTIVE
            self.active_actor_id = actor_id
            return actor

        return None


    def complete_active_activation(self) -> TacticalActorState:
        """Complete the current normal activation and expire unused budget."""

        if self.active_actor_id is None:
            raise ValueError("no active combat actor")
        actor = self.actors[self.active_actor_id]
        if actor.activation_state not in {
            ACTIVATION_ACTIVE,
            ACTIVATION_RESOLVING_ACTION,
            ACTIVATION_WAITING_REACTION,
        }:
            raise ValueError("active actor is not in a completable activation state")
        actor.action_budget = 0
        actor.activation_state = ACTIVATION_COMPLETE
        self.active_actor_id = None
        return actor

    def round_is_complete(self) -> bool:
        """Return whether the current round snapshot has no activation left."""

        return (
            self.active_actor_id is None
            and self.activation_index >= len(self.initiative_order)
        )

    def advance_round(self) -> tuple[str, ...]:
        """Advance after the current round completes and snapshot initiative again."""

        if not self.round_is_complete():
            raise ValueError("cannot advance round while activations remain")
        self.round_index += 1
        self.activation_index = 0
        for actor in self.actors.values():
            actor.action_budget = 0
            if actor.incapacitated:
                actor.activation_state = ACTIVATION_SKIPPED
            else:
                actor.activation_state = ACTIVATION_PENDING
        self.initiative_order = self._snapshot_initiative_order()
        return self.initiative_order


    def _active_actor(self, actor_id: str) -> TacticalActorState:
        if self.active_actor_id != actor_id:
            raise ValueError("only the active actor may initiate a normal action")
        actor = self.actors.get(actor_id)
        if actor is None:
            raise ValueError(f"unknown combat actor: {actor_id}")
        if actor.activation_state != ACTIVATION_ACTIVE:
            raise ValueError("active actor is not ready for a normal action")
        return actor

    def _movement_action(self, action_id: str) -> tuple[int, int]:
        definition = self.combat_actions.get(action_id)
        if definition is None:
            raise ValueError(f"unknown combat action: {action_id}")
        category = definition.get("category")
        if category == "move":
            allowance = PHASE1_MOVE_POINTS
        elif category == "sprint":
            allowance = PHASE1_SPRINT_POINTS
        else:
            raise ValueError(f"combat action {action_id} is not a movement action")
        cost = definition.get("cost")
        if isinstance(cost, bool) or not isinstance(cost, int) or cost < 0:
            raise ValueError(f"combat action {action_id} has invalid budget cost")
        return cost, allowance

    def _occupants(self) -> tuple[TacticalOccupant, ...]:
        return tuple(
            TacticalOccupant(
                actor.actor_id,
                actor.faction_id,
                actor.coord,
                solid=not actor.incapacitated,
            )
            for actor in self.actors.values()
        )

    def preview_movement(
        self,
        *,
        actor_id: str,
        action_id: str,
        goal: TacticalCoord,
        allow_allies_through: bool = True,
    ) -> MovementPlan:
        """Return a read-only movement plan using D-069 path authority."""

        actor = self._active_actor(actor_id)
        budget_cost, allowance = self._movement_action(action_id)
        if actor.action_budget < budget_cost:
            raise ValueError("insufficient action budget")
        path = find_path(
            self.tactical_map,
            actor.coord,
            goal,
            occupants=self._occupants(),
            moving_actor_id=actor.actor_id,
            moving_faction_id=actor.faction_id,
            allow_allies_through=allow_allies_through,
        )
        if path is None:
            raise ValueError("no legal tactical path")
        traversal_cost = path_traversal_cost(self.tactical_map, path)
        if traversal_cost > allowance:
            raise ValueError(
                f"movement path costs {traversal_cost}, allowance is {allowance}"
            )
        return MovementPlan(
            action_id=action_id,
            path=path,
            traversal_cost=traversal_cost,
            movement_allowance=allowance,
            action_budget_cost=budget_cost,
        )

    def _append_movement_event(
        self,
        *,
        actor: TacticalActorState,
        plan: MovementPlan,
        budget_before: int,
        coord_before: TacticalCoord,
    ) -> CombatEvent:
        next_index = self.event_index + 1
        target_key = plan.path[-1].key
        digest_source = (
            f"{self.seed}|{self.encounter_id}|{self.round_index}|"
            f"{self.activation_index}|{next_index}|{actor.actor_id}|"
            f"{plan.action_id}|{target_key}"
        )
        event = CombatEvent(
            event_index=next_index,
            round_index=self.round_index,
            activation_index=self.activation_index,
            actor_id=actor.actor_id,
            action_id=plan.action_id,
            target_key=target_key,
            budget_before=budget_before,
            budget_after=actor.action_budget,
            coord_before=coord_before,
            coord_after=actor.coord,
            digest=hashlib.sha256(digest_source.encode("utf-8")).hexdigest(),
        )
        self.committed_events.append(event)
        self.event_index = next_index
        return event

    def commit_movement(
        self,
        *,
        actor_id: str,
        action_id: str,
        goal: TacticalCoord,
        allow_allies_through: bool = True,
    ) -> CombatEvent:
        """Commit one atomic transient movement action or roll it back."""

        actor = self._active_actor(actor_id)
        plan = self.preview_movement(
            actor_id=actor_id,
            action_id=action_id,
            goal=goal,
            allow_allies_through=allow_allies_through,
        )
        coord_before = actor.coord
        budget_before = actor.action_budget
        state_before = actor.activation_state
        event_index_before = self.event_index
        event_count_before = len(self.committed_events)

        try:
            actor.activation_state = ACTIVATION_RESOLVING_ACTION
            actor.action_budget -= plan.action_budget_cost
            actor.coord = plan.path[-1]
            event = self._append_movement_event(
                actor=actor,
                plan=plan,
                budget_before=budget_before,
                coord_before=coord_before,
            )
            actor.activation_state = ACTIVATION_ACTIVE
            return event
        except Exception:
            actor.coord = coord_before
            actor.action_budget = budget_before
            actor.activation_state = state_before
            self.event_index = event_index_before
            del self.committed_events[event_count_before:]
            raise
