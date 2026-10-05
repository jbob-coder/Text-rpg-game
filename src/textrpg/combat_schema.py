from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Iterable


_STABLE_ID = re.compile(r"^[A-Z][A-Z0-9_]*$")
CARDINAL_DIRECTIONS = ("N", "E", "S", "W")
COVER_NONE = 0
COVER_PARTIAL = 1
COVER_STRONG = 2
COVER_RATINGS = {COVER_NONE, COVER_PARTIAL, COVER_STRONG}


def _require_plain_int(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{label} must be an integer")
    return value


def _require_positive_int(value: object, label: str) -> int:
    result = _require_plain_int(value, label)
    if result <= 0:
        raise ValueError(f"{label} must be a positive integer")
    return result


def _require_stable_id(value: object, label: str) -> str:
    if not isinstance(value, str) or _STABLE_ID.fullmatch(value) is None:
        raise ValueError(f"{label} must be a stable uppercase ID")
    return value


def _canonical_edges(values: Iterable[str], label: str) -> tuple[str, ...]:
    edges = tuple(values)
    if len(set(edges)) != len(edges):
        raise ValueError(f"{label} cannot contain duplicate edges")
    invalid = sorted(set(edges) - set(CARDINAL_DIRECTIONS))
    if invalid:
        raise ValueError(f"{label} has unsupported edges: {', '.join(invalid)}")
    return tuple(edge for edge in CARDINAL_DIRECTIONS if edge in edges)


def _canonical_cover(
    values: Iterable[tuple[str, int]],
) -> tuple[tuple[str, int], ...]:
    cover = tuple(values)
    edges = [edge for edge, _rating in cover]
    if len(set(edges)) != len(edges):
        raise ValueError("cover cannot contain duplicate edges")
    invalid = sorted(set(edges) - set(CARDINAL_DIRECTIONS))
    if invalid:
        raise ValueError(f"cover has unsupported edges: {', '.join(invalid)}")
    for edge, rating in cover:
        _require_plain_int(rating, f"cover.{edge}")
        if rating not in COVER_RATINGS:
            raise ValueError(f"cover.{edge} must be 0, 1, or 2")
    lookup = dict(cover)
    return tuple(
        (edge, lookup[edge])
        for edge in CARDINAL_DIRECTIONS
        if edge in lookup
    )


@dataclass(frozen=True, order=True)
class TacticalCoord:
    """One authoritative tactical-grid coordinate."""

    x: int
    y: int
    z: int = 0

    def __post_init__(self) -> None:
        _require_plain_int(self.x, "coord.x")
        _require_plain_int(self.y, "coord.y")
        _require_plain_int(self.z, "coord.z")

    @property
    def key(self) -> str:
        return f"{self.x},{self.y},{self.z}"

    @classmethod
    def from_key(cls, value: str) -> "TacticalCoord":
        if not isinstance(value, str):
            raise ValueError("tactical coordinate key must be text")
        parts = value.split(",")
        if len(parts) != 3:
            raise ValueError("tactical coordinate key must use x,y,z")
        try:
            coords = tuple(int(part) for part in parts)
        except ValueError as exc:
            raise ValueError("tactical coordinate key must contain integers") from exc
        return cls(*coords)


@dataclass(frozen=True)
class TacticalCell:
    """Canonical resolved cell used by pure tactical spatial queries."""

    coord: TacticalCoord
    terrain_id: str | None = None
    movement_cost: int = 1
    blocks_movement: bool = False
    blocks_los: bool = False
    los_blocked_edges: tuple[str, ...] = ()
    cover: tuple[tuple[str, int], ...] = ()
    concealment: int = 0
    hazard_ids: tuple[str, ...] = ()
    tags: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not isinstance(self.coord, TacticalCoord):
            raise ValueError("cell.coord must be TacticalCoord")
        if self.terrain_id is not None:
            _require_stable_id(self.terrain_id, "cell.terrain_id")
        _require_positive_int(self.movement_cost, "cell.movement_cost")
        if not isinstance(self.blocks_movement, bool):
            raise ValueError("cell.blocks_movement must be boolean")
        if not isinstance(self.blocks_los, bool):
            raise ValueError("cell.blocks_los must be boolean")
        _require_plain_int(self.concealment, "cell.concealment")
        if self.concealment < 0:
            raise ValueError("cell.concealment must be non-negative")
        object.__setattr__(
            self,
            "los_blocked_edges",
            _canonical_edges(self.los_blocked_edges, "cell.los_blocked_edges"),
        )
        object.__setattr__(self, "cover", _canonical_cover(self.cover))
        for index, hazard_id in enumerate(self.hazard_ids):
            _require_stable_id(hazard_id, f"cell.hazard_ids[{index}]")
        if len(set(self.hazard_ids)) != len(self.hazard_ids):
            raise ValueError("cell.hazard_ids cannot contain duplicates")
        if any(not isinstance(tag, str) or not tag for tag in self.tags):
            raise ValueError("cell.tags must contain non-empty text")

    def cover_rating(self, edge: str) -> int:
        if edge not in CARDINAL_DIRECTIONS:
            raise ValueError(f"unsupported cover edge: {edge!r}")
        return dict(self.cover).get(edge, COVER_NONE)

    def blocks_los_through(self, edge: str) -> bool:
        if edge not in CARDINAL_DIRECTIONS:
            raise ValueError(f"unsupported LOS edge: {edge!r}")
        return edge in self.los_blocked_edges


@dataclass(frozen=True)
class TacticalTransition:
    """Explicit authored edge between tactical cells, including z movement."""

    transition_id: str
    start: TacticalCoord
    end: TacticalCoord
    cost: int = 1
    bidirectional: bool = True

    def __post_init__(self) -> None:
        _require_stable_id(self.transition_id, "transition_id")
        if not isinstance(self.start, TacticalCoord) or not isinstance(
            self.end, TacticalCoord
        ):
            raise ValueError("transition endpoints must be TacticalCoord")
        if self.start == self.end:
            raise ValueError("transition endpoints must differ")
        _require_positive_int(self.cost, "transition.cost")
        if not isinstance(self.bidirectional, bool):
            raise ValueError("transition.bidirectional must be boolean")


@dataclass(frozen=True)
class TacticalZone:
    """Named deployment/spawn zone over canonical tactical cells."""

    zone_id: str
    cells: tuple[TacticalCoord, ...]

    def __post_init__(self) -> None:
        _require_stable_id(self.zone_id, "zone_id")
        if not self.cells:
            raise ValueError("zone.cells must not be empty")
        if len(set(self.cells)) != len(self.cells):
            raise ValueError("zone.cells cannot contain duplicates")


@dataclass(frozen=True)
class TacticalAnchor:
    """Named objective/exit anchor into a canonical tactical map."""

    anchor_id: str
    coord: TacticalCoord

    def __post_init__(self) -> None:
        _require_stable_id(self.anchor_id, "anchor_id")
        if not isinstance(self.coord, TacticalCoord):
            raise ValueError("anchor.coord must be TacticalCoord")


@dataclass(frozen=True)
class TacticalMap:
    """Immutable canonical map consumed by deterministic grid helpers."""

    map_id: str
    version: int
    width: int
    height: int
    z_layers: tuple[int, ...]
    cells: tuple[TacticalCell, ...]
    transitions: tuple[TacticalTransition, ...] = ()
    deployment_zones: tuple[TacticalZone, ...] = ()
    objective_anchors: tuple[TacticalAnchor, ...] = ()
    exits: tuple[TacticalAnchor, ...] = ()

    def __post_init__(self) -> None:
        _require_stable_id(self.map_id, "map_id")
        _require_positive_int(self.version, "map.version")
        _require_positive_int(self.width, "map.width")
        _require_positive_int(self.height, "map.height")
        if not self.z_layers:
            raise ValueError("map.z_layers must not be empty")
        if any(
            isinstance(layer, bool) or not isinstance(layer, int)
            for layer in self.z_layers
        ):
            raise ValueError("map.z_layers must contain integers")
        if len(set(self.z_layers)) != len(self.z_layers):
            raise ValueError("map.z_layers cannot contain duplicates")

        cell_lookup: dict[TacticalCoord, TacticalCell] = {}
        for cell in self.cells:
            if not isinstance(cell, TacticalCell):
                raise ValueError("map.cells must contain TacticalCell values")
            if cell.coord in cell_lookup:
                raise ValueError(f"duplicate tactical cell: {cell.coord.key}")
            if not self.in_bounds(cell.coord):
                raise ValueError(f"tactical cell out of bounds: {cell.coord.key}")
            cell_lookup[cell.coord] = cell

        transition_ids: set[str] = set()
        for transition in self.transitions:
            if transition.transition_id in transition_ids:
                raise ValueError(
                    f"duplicate tactical transition: {transition.transition_id}"
                )
            transition_ids.add(transition.transition_id)
            for endpoint in (transition.start, transition.end):
                cell = cell_lookup.get(endpoint)
                if cell is None:
                    raise ValueError(
                        f"transition {transition.transition_id} references "
                        f"unknown cell {endpoint.key}"
                    )
                if cell.blocks_movement:
                    raise ValueError(
                        f"transition {transition.transition_id} references "
                        f"blocked cell {endpoint.key}"
                    )

        self._validate_zones(self.deployment_zones, cell_lookup)
        self._validate_anchors("objective", self.objective_anchors, cell_lookup)
        self._validate_anchors("exit", self.exits, cell_lookup)

    def _validate_zones(
        self,
        zones: tuple[TacticalZone, ...],
        cell_lookup: dict[TacticalCoord, TacticalCell],
    ) -> None:
        seen: set[str] = set()
        for zone in zones:
            if zone.zone_id in seen:
                raise ValueError(f"duplicate deployment zone: {zone.zone_id}")
            seen.add(zone.zone_id)
            for coord in zone.cells:
                cell = cell_lookup.get(coord)
                if cell is None:
                    raise ValueError(
                        f"deployment zone {zone.zone_id} references unknown cell "
                        f"{coord.key}"
                    )
                if cell.blocks_movement:
                    raise ValueError(
                        f"deployment zone {zone.zone_id} references blocked cell "
                        f"{coord.key}"
                    )

    def _validate_anchors(
        self,
        kind: str,
        anchors: tuple[TacticalAnchor, ...],
        cell_lookup: dict[TacticalCoord, TacticalCell],
    ) -> None:
        seen: set[str] = set()
        for anchor in anchors:
            if anchor.anchor_id in seen:
                raise ValueError(f"duplicate {kind} anchor: {anchor.anchor_id}")
            seen.add(anchor.anchor_id)
            cell = cell_lookup.get(anchor.coord)
            if cell is None:
                raise ValueError(
                    f"{kind} anchor {anchor.anchor_id} references unknown cell "
                    f"{anchor.coord.key}"
                )
            if cell.blocks_movement:
                raise ValueError(
                    f"{kind} anchor {anchor.anchor_id} references blocked cell "
                    f"{anchor.coord.key}"
                )

    def in_bounds(self, coord: TacticalCoord) -> bool:
        return (
            0 <= coord.x < self.width
            and 0 <= coord.y < self.height
            and coord.z in self.z_layers
        )

    def cell_at(self, coord: TacticalCoord) -> TacticalCell | None:
        for cell in self.cells:
            if cell.coord == coord:
                return cell
        return None

    def transition_targets(
        self,
        coord: TacticalCoord,
    ) -> tuple[tuple[TacticalCoord, int], ...]:
        targets: list[tuple[TacticalCoord, int]] = []
        for transition in self.transitions:
            if transition.start == coord:
                targets.append((transition.end, transition.cost))
            elif transition.bidirectional and transition.end == coord:
                targets.append((transition.start, transition.cost))
        return tuple(
            sorted(
                targets,
                key=lambda item: (
                    item[0].y,
                    item[0].x,
                    item[0].z,
                    item[0].key,
                    item[1],
                ),
            )
        )
