"""Transient deterministic combat-session state for D-070.

This module deliberately owns encounter-local mutable state only. It consumes the
immutable tactical schema/grid authority from D-069 and does not mutate GameState
or save-schema data.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable

from .combat_grid import TacticalOccupant, occupancy_by_coord
from .combat_schema import CARDINAL_DIRECTIONS, TacticalCoord, TacticalMap


PHASE1_ACTION_BUDGET = 4

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
