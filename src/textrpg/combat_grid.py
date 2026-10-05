from __future__ import annotations

from dataclasses import dataclass
import heapq
from math import inf
from typing import Iterable, Mapping

from .combat_schema import (
    CARDINAL_DIRECTIONS,
    TacticalCoord,
    TacticalMap,
)


_EDGE_PRIORITY = {edge: index for index, edge in enumerate(CARDINAL_DIRECTIONS)}
_OPPOSITE_EDGE = {"N": "S", "E": "W", "S": "N", "W": "E"}


@dataclass(frozen=True)
class TacticalOccupant:
    """Minimal spatial identity used by pure occupancy/path queries."""

    actor_id: str
    faction_id: str
    coord: TacticalCoord
    solid: bool = True

    def __post_init__(self) -> None:
        if not isinstance(self.actor_id, str) or not self.actor_id:
            raise ValueError("occupant.actor_id must be non-empty text")
        if not isinstance(self.faction_id, str) or not self.faction_id:
            raise ValueError("occupant.faction_id must be non-empty text")
        if not isinstance(self.coord, TacticalCoord):
            raise ValueError("occupant.coord must be TacticalCoord")
        if not isinstance(self.solid, bool):
            raise ValueError("occupant.solid must be boolean")


def cardinal_neighbors(coord: TacticalCoord) -> tuple[TacticalCoord, ...]:
    """Return N -> E -> S -> W same-z neighbors."""

    return (
        TacticalCoord(coord.x, coord.y - 1, coord.z),
        TacticalCoord(coord.x + 1, coord.y, coord.z),
        TacticalCoord(coord.x, coord.y + 1, coord.z),
        TacticalCoord(coord.x - 1, coord.y, coord.z),
    )


def occupancy_by_coord(
    occupants: Iterable[TacticalOccupant],
) -> dict[TacticalCoord, TacticalOccupant]:
    """Index solid occupants and reject impossible double occupancy."""

    indexed: dict[TacticalCoord, TacticalOccupant] = {}
    actor_ids: set[str] = set()
    for occupant in occupants:
        if not isinstance(occupant, TacticalOccupant):
            raise ValueError("occupants must contain TacticalOccupant values")
        if occupant.actor_id in actor_ids:
            raise ValueError(f"duplicate tactical actor id: {occupant.actor_id}")
        actor_ids.add(occupant.actor_id)
        if not occupant.solid:
            continue
        prior = indexed.get(occupant.coord)
        if prior is not None:
            raise ValueError(
                f"solid occupancy conflict at {occupant.coord.key}: "
                f"{prior.actor_id}, {occupant.actor_id}"
            )
        indexed[occupant.coord] = occupant
    return indexed


def is_traversable(tactical_map: TacticalMap, coord: TacticalCoord) -> bool:
    cell = tactical_map.cell_at(coord)
    return cell is not None and not cell.blocks_movement


def _occupied_for_step(
    coord: TacticalCoord,
    *,
    goal: TacticalCoord,
    occupancy: Mapping[TacticalCoord, TacticalOccupant],
    moving_actor_id: str | None,
    moving_faction_id: str | None,
    allow_allies_through: bool,
) -> bool:
    occupant = occupancy.get(coord)
    if occupant is None or occupant.actor_id == moving_actor_id:
        return False
    if coord == goal:
        return True
    if moving_faction_id is None:
        return True
    if occupant.faction_id != moving_faction_id:
        return True
    return not allow_allies_through


def _neighbor_steps(
    tactical_map: TacticalMap,
    coord: TacticalCoord,
) -> tuple[tuple[TacticalCoord, int], ...]:
    steps: list[tuple[TacticalCoord, int]] = []
    seen: set[TacticalCoord] = set()

    for neighbor in cardinal_neighbors(coord):
        if neighbor in seen or not tactical_map.in_bounds(neighbor):
            continue
        cell = tactical_map.cell_at(neighbor)
        if cell is None or cell.blocks_movement:
            continue
        steps.append((neighbor, cell.movement_cost))
        seen.add(neighbor)

    for neighbor, transition_cost in tactical_map.transition_targets(coord):
        if neighbor in seen:
            continue
        cell = tactical_map.cell_at(neighbor)
        if cell is None or cell.blocks_movement:
            continue
        steps.append((neighbor, transition_cost))
        seen.add(neighbor)

    return tuple(steps)


def find_path(
    tactical_map: TacticalMap,
    start: TacticalCoord,
    goal: TacticalCoord,
    *,
    occupants: Iterable[TacticalOccupant] = (),
    moving_actor_id: str | None = None,
    moving_faction_id: str | None = None,
    allow_allies_through: bool = False,
) -> tuple[TacticalCoord, ...] | None:
    """Deterministic A* for cardinal-only maps; Dijkstra when transitions exist."""

    if tactical_map.cell_at(start) is None or not is_traversable(tactical_map, start):
        return None
    if tactical_map.cell_at(goal) is None or not is_traversable(tactical_map, goal):
        return None

    occupancy = occupancy_by_coord(occupants)
    if _occupied_for_step(
        goal,
        goal=goal,
        occupancy=occupancy,
        moving_actor_id=moving_actor_id,
        moving_faction_id=moving_faction_id,
        allow_allies_through=allow_allies_through,
    ):
        return None
    if start == goal:
        return (start,)

    def heuristic(coord: TacticalCoord) -> int:
        # Explicit cross-z transitions may have authored costs unrelated to
        # x/y displacement, so same-z Manhattan is not guaranteed admissible
        # when any transition is present. Use deterministic Dijkstra in that
        # case and retain Manhattan A* only for cardinal-only maps.
        if tactical_map.transitions:
            return 0
        if coord.z != goal.z:
            return 0
        return abs(coord.x - goal.x) + abs(coord.y - goal.y)

    g_score: dict[TacticalCoord, int] = {start: 0}
    came_from: dict[TacticalCoord, TacticalCoord] = {}
    start_h = heuristic(start)
    queue: list[tuple[int, int, int, int, int, str, int, TacticalCoord]] = [
        (start_h, start_h, start.y, start.x, start.z, start.key, 0, start)
    ]

    while queue:
        _f, _h, _y, _x, _z, _key, queued_g, current = heapq.heappop(queue)
        if queued_g != g_score.get(current):
            continue
        if current == goal:
            path = [goal]
            while path[-1] != start:
                path.append(came_from[path[-1]])
            path.reverse()
            return tuple(path)

        for neighbor, step_cost in _neighbor_steps(tactical_map, current):
            if _occupied_for_step(
                neighbor,
                goal=goal,
                occupancy=occupancy,
                moving_actor_id=moving_actor_id,
                moving_faction_id=moving_faction_id,
                allow_allies_through=allow_allies_through,
            ):
                continue

            tentative = queued_g + step_cost
            if tentative >= g_score.get(neighbor, inf):
                continue
            g_score[neighbor] = tentative
            came_from[neighbor] = current
            h_cost = heuristic(neighbor)
            heapq.heappush(
                queue,
                (
                    tentative + h_cost,
                    h_cost,
                    neighbor.y,
                    neighbor.x,
                    neighbor.z,
                    neighbor.key,
                    tentative,
                    neighbor,
                ),
            )

    return None


def supercover_line(
    start: TacticalCoord,
    end: TacticalCoord,
) -> tuple[TacticalCoord, ...]:
    """Enumerate every same-z cell touched by a center-to-center grid ray."""

    if start.z != end.z:
        raise ValueError("supercover LOS across z layers requires explicit geometry")
    if start == end:
        return (start,)

    dx = end.x - start.x
    dy = end.y - start.y
    nx = abs(dx)
    ny = abs(dy)
    sign_x = 0 if dx == 0 else (1 if dx > 0 else -1)
    sign_y = 0 if dy == 0 else (1 if dy > 0 else -1)

    x = start.x
    y = start.y
    ix = 0
    iy = 0
    result: list[TacticalCoord] = [start]

    def append_unique(coord: TacticalCoord) -> None:
        if coord not in result:
            result.append(coord)

    while ix < nx or iy < ny:
        decision = (1 + 2 * ix) * ny - (1 + 2 * iy) * nx
        if decision == 0 and ix < nx and iy < ny:
            horizontal = TacticalCoord(x + sign_x, y, start.z)
            vertical = TacticalCoord(x, y + sign_y, start.z)
            candidates = [
                (_direction_between(TacticalCoord(x, y, start.z), horizontal), horizontal),
                (_direction_between(TacticalCoord(x, y, start.z), vertical), vertical),
            ]
            for _direction, coord in sorted(
                candidates, key=lambda item: _EDGE_PRIORITY[item[0]]
            ):
                append_unique(coord)
            x += sign_x
            y += sign_y
            ix += 1
            iy += 1
            append_unique(TacticalCoord(x, y, start.z))
        elif decision < 0 and ix < nx:
            x += sign_x
            ix += 1
            append_unique(TacticalCoord(x, y, start.z))
        else:
            y += sign_y
            iy += 1
            append_unique(TacticalCoord(x, y, start.z))

    return tuple(result)


def _direction_between(start: TacticalCoord, end: TacticalCoord) -> str:
    dx = end.x - start.x
    dy = end.y - start.y
    if start.z != end.z or abs(dx) + abs(dy) != 1:
        raise ValueError("edge direction requires cardinal same-z adjacent cells")
    if dx == 1:
        return "E"
    if dx == -1:
        return "W"
    if dy == 1:
        return "S"
    return "N"


def _edge_blocked(
    tactical_map: TacticalMap,
    start: TacticalCoord,
    end: TacticalCoord,
) -> bool:
    direction = _direction_between(start, end)
    source = tactical_map.cell_at(start)
    destination = tactical_map.cell_at(end)
    if source is None or destination is None:
        return True
    return source.blocks_los_through(direction) or destination.blocks_los_through(
        _OPPOSITE_EDGE[direction]
    )


def _ray_edge_pairs(
    start: TacticalCoord,
    end: TacticalCoord,
) -> tuple[tuple[TacticalCoord, TacticalCoord], ...]:
    """Return cardinal edge crossings, conservatively expanding exact corners."""

    if start.z != end.z:
        raise ValueError("ray edge crossings require matching z layers")
    if start == end:
        return ()

    dx = end.x - start.x
    dy = end.y - start.y
    nx = abs(dx)
    ny = abs(dy)
    sign_x = 0 if dx == 0 else (1 if dx > 0 else -1)
    sign_y = 0 if dy == 0 else (1 if dy > 0 else -1)

    x = start.x
    y = start.y
    ix = 0
    iy = 0
    pairs: list[tuple[TacticalCoord, TacticalCoord]] = []

    while ix < nx or iy < ny:
        current = TacticalCoord(x, y, start.z)
        decision = (1 + 2 * ix) * ny - (1 + 2 * iy) * nx
        if decision == 0 and ix < nx and iy < ny:
            horizontal = TacticalCoord(x + sign_x, y, start.z)
            vertical = TacticalCoord(x, y + sign_y, start.z)
            diagonal = TacticalCoord(x + sign_x, y + sign_y, start.z)
            corner_pairs = [
                (current, horizontal),
                (current, vertical),
                (horizontal, diagonal),
                (vertical, diagonal),
            ]
            pairs.extend(
                sorted(
                    corner_pairs,
                    key=lambda pair: (
                        _EDGE_PRIORITY[_direction_between(*pair)],
                        pair[0].y,
                        pair[0].x,
                        pair[1].y,
                        pair[1].x,
                    ),
                )
            )
            x += sign_x
            y += sign_y
            ix += 1
            iy += 1
        elif decision < 0 and ix < nx:
            nxt = TacticalCoord(x + sign_x, y, start.z)
            pairs.append((current, nxt))
            x += sign_x
            ix += 1
        else:
            nxt = TacticalCoord(x, y + sign_y, start.z)
            pairs.append((current, nxt))
            y += sign_y
            iy += 1

    return tuple(pairs)


def has_line_of_sight(
    tactical_map: TacticalMap,
    start: TacticalCoord,
    end: TacticalCoord,
) -> bool:
    """Resolve geometric same-z LOS without awareness/knowledge semantics."""

    if tactical_map.cell_at(start) is None or tactical_map.cell_at(end) is None:
        return False
    if start == end:
        return True
    try:
        touched = supercover_line(start, end)
        edge_pairs = _ray_edge_pairs(start, end)
    except ValueError:
        return False

    for coord in touched:
        cell = tactical_map.cell_at(coord)
        if cell is None or cell.blocks_los:
            return False
    return not any(_edge_blocked(tactical_map, a, b) for a, b in edge_pairs)


def incoming_cover_edge(start: TacticalCoord, target: TacticalCoord) -> str:
    """Return the deterministic target edge first crossed by the attack ray."""

    if start.z != target.z:
        raise ValueError("cover edge query requires matching z layers")
    dx = target.x - start.x
    dy = target.y - start.y
    if dx == 0 and dy == 0:
        raise ValueError("cover edge query requires distinct cells")

    horizontal = None
    vertical = None
    if dx > 0:
        horizontal = "W"
    elif dx < 0:
        horizontal = "E"
    if dy > 0:
        vertical = "N"
    elif dy < 0:
        vertical = "S"

    if horizontal is None:
        assert vertical is not None
        return vertical
    if vertical is None:
        return horizontal
    if abs(dx) > abs(dy):
        return horizontal
    if abs(dy) > abs(dx):
        return vertical
    return min((horizontal, vertical), key=_EDGE_PRIORITY.__getitem__)


def cover_rating(
    tactical_map: TacticalMap,
    attacker: TacticalCoord,
    target: TacticalCoord,
) -> int:
    cell = tactical_map.cell_at(target)
    if cell is None:
        raise ValueError(f"target is not a tactical cell: {target.key}")
    return cell.cover_rating(incoming_cover_edge(attacker, target))
