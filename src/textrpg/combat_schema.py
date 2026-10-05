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


_MAP_FIELDS = {
    "map_id",
    "version",
    "width",
    "height",
    "z_layers",
    "default_cell",
    "overrides",
    "transitions",
    "deployment_zones",
    "objective_anchors",
    "exits",
}
_CELL_FIELDS = {
    "terrain_id",
    "movement_cost",
    "blocks_movement",
    "blocks_los",
    "los_blocked_edges",
    "cover",
    "concealment",
    "hazard_ids",
    "tags",
}
_TRANSITION_FIELDS = {"from", "to", "cost", "bidirectional"}


def _mapping(value: object, label: str) -> dict:
    from collections.abc import Mapping

    if not isinstance(value, Mapping):
        raise ValueError(f"{label} must be an object")
    return dict(value)


def _reject_unknown_fields(
    record: dict,
    allowed: set[str],
    label: str,
) -> None:
    unknown = sorted(set(record) - allowed)
    if unknown:
        raise ValueError(
            f"{label} has unsupported fields: {', '.join(str(item) for item in unknown)}"
        )


def _text_tuple(value: object, label: str) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, list):
        raise ValueError(f"{label} must be a list")
    result = tuple(value)
    if any(not isinstance(item, str) or not item for item in result):
        raise ValueError(f"{label} must contain non-empty text")
    if len(set(result)) != len(result):
        raise ValueError(f"{label} cannot contain duplicates")
    return result


def _cell_from_mapping(
    coord: TacticalCoord,
    value: object,
    label: str,
) -> TacticalCell:
    record = _mapping(value, label)
    _reject_unknown_fields(record, _CELL_FIELDS, label)

    cover_raw = record.get("cover", {})
    cover_mapping = _mapping(cover_raw, f"{label}.cover")
    cover = tuple((str(edge), rating) for edge, rating in cover_mapping.items())

    return TacticalCell(
        coord=coord,
        terrain_id=record.get("terrain_id"),
        movement_cost=record.get("movement_cost", 1),
        blocks_movement=record.get("blocks_movement", False),
        blocks_los=record.get("blocks_los", False),
        los_blocked_edges=_text_tuple(
            record.get("los_blocked_edges", []),
            f"{label}.los_blocked_edges",
        ),
        cover=cover,
        concealment=record.get("concealment", 0),
        hazard_ids=_text_tuple(
            record.get("hazard_ids", []),
            f"{label}.hazard_ids",
        ),
        tags=_text_tuple(record.get("tags", []), f"{label}.tags"),
    )


def _coord_from_value(value: object, label: str) -> TacticalCoord:
    if not isinstance(value, str):
        raise ValueError(f"{label} must be an x,y,z coordinate key")
    try:
        return TacticalCoord.from_key(value)
    except ValueError as exc:
        raise ValueError(f"{label} is invalid: {exc}") from exc


def parse_tactical_map_definition(
    map_id: str,
    value: object,
) -> TacticalMap:
    """Parse one strict sparse authored map into canonical immutable cells."""

    _require_stable_id(map_id, "tactical map id")
    record = _mapping(value, f"tactical_maps.{map_id}")
    _reject_unknown_fields(record, _MAP_FIELDS, f"tactical_maps.{map_id}")

    required = {
        "map_id",
        "version",
        "width",
        "height",
        "z_layers",
        "default_cell",
        "overrides",
        "transitions",
        "deployment_zones",
        "objective_anchors",
        "exits",
    }
    missing = sorted(required - set(record))
    if missing:
        raise ValueError(
            f"tactical_maps.{map_id} missing required fields: {', '.join(missing)}"
        )
    if record["map_id"] != map_id:
        raise ValueError(
            f"tactical_maps.{map_id}.map_id must equal mapping key {map_id}"
        )

    version = _require_positive_int(record["version"], f"tactical_maps.{map_id}.version")
    width = _require_positive_int(record["width"], f"tactical_maps.{map_id}.width")
    height = _require_positive_int(record["height"], f"tactical_maps.{map_id}.height")

    z_raw = record["z_layers"]
    if not isinstance(z_raw, list) or not z_raw:
        raise ValueError(f"tactical_maps.{map_id}.z_layers must be a non-empty list")
    z_layers = tuple(
        _require_plain_int(layer, f"tactical_maps.{map_id}.z_layers[{index}]")
        for index, layer in enumerate(z_raw)
    )
    if len(set(z_layers)) != len(z_layers):
        raise ValueError(f"tactical_maps.{map_id}.z_layers cannot contain duplicates")

    default_cell = _mapping(
        record["default_cell"],
        f"tactical_maps.{map_id}.default_cell",
    )
    _reject_unknown_fields(
        default_cell,
        _CELL_FIELDS,
        f"tactical_maps.{map_id}.default_cell",
    )
    overrides = _mapping(
        record["overrides"],
        f"tactical_maps.{map_id}.overrides",
    )

    override_by_coord: dict[TacticalCoord, dict] = {}
    for raw_coord, override in overrides.items():
        coord = _coord_from_value(
            raw_coord,
            f"tactical_maps.{map_id}.overrides key",
        )
        if coord in override_by_coord:
            raise ValueError(
                f"tactical_maps.{map_id}.overrides duplicates coordinate {coord.key}"
            )
        override_record = _mapping(
            override,
            f"tactical_maps.{map_id}.overrides.{coord.key}",
        )
        _reject_unknown_fields(
            override_record,
            _CELL_FIELDS,
            f"tactical_maps.{map_id}.overrides.{coord.key}",
        )
        if not (
            0 <= coord.x < width
            and 0 <= coord.y < height
            and coord.z in z_layers
        ):
            raise ValueError(
                f"tactical_maps.{map_id}.overrides coordinate out of bounds: "
                f"{coord.key}"
            )
        override_by_coord[coord] = override_record

    cells: list[TacticalCell] = []
    for z in z_layers:
        for y in range(height):
            for x in range(width):
                coord = TacticalCoord(x, y, z)
                merged = dict(default_cell)
                merged.update(override_by_coord.get(coord, {}))
                cells.append(
                    _cell_from_mapping(
                        coord,
                        merged,
                        f"tactical_maps.{map_id}.cells.{coord.key}",
                    )
                )

    transitions_raw = _mapping(
        record["transitions"],
        f"tactical_maps.{map_id}.transitions",
    )
    transitions: list[TacticalTransition] = []
    for transition_id, transition_value in transitions_raw.items():
        _require_stable_id(transition_id, "tactical transition id")
        transition_record = _mapping(
            transition_value,
            f"tactical_maps.{map_id}.transitions.{transition_id}",
        )
        _reject_unknown_fields(
            transition_record,
            _TRANSITION_FIELDS,
            f"tactical_maps.{map_id}.transitions.{transition_id}",
        )
        missing_transition = {"from", "to"} - set(transition_record)
        if missing_transition:
            raise ValueError(
                f"tactical_maps.{map_id}.transitions.{transition_id} missing "
                f"required fields: {', '.join(sorted(missing_transition))}"
            )
        transitions.append(
            TacticalTransition(
                transition_id=transition_id,
                start=_coord_from_value(
                    transition_record["from"],
                    f"tactical_maps.{map_id}.transitions.{transition_id}.from",
                ),
                end=_coord_from_value(
                    transition_record["to"],
                    f"tactical_maps.{map_id}.transitions.{transition_id}.to",
                ),
                cost=transition_record.get("cost", 1),
                bidirectional=transition_record.get("bidirectional", True),
            )
        )

    zones_raw = _mapping(
        record["deployment_zones"],
        f"tactical_maps.{map_id}.deployment_zones",
    )
    deployment_zones: list[TacticalZone] = []
    for zone_id, zone_value in zones_raw.items():
        _require_stable_id(zone_id, "deployment zone id")
        if not isinstance(zone_value, list):
            raise ValueError(
                f"tactical_maps.{map_id}.deployment_zones.{zone_id} must be a list"
            )
        deployment_zones.append(
            TacticalZone(
                zone_id,
                tuple(
                    _coord_from_value(
                        item,
                        f"tactical_maps.{map_id}.deployment_zones."
                        f"{zone_id}[{index}]",
                    )
                    for index, item in enumerate(zone_value)
                ),
            )
        )

    def parse_anchors(field: str) -> tuple[TacticalAnchor, ...]:
        raw = _mapping(record[field], f"tactical_maps.{map_id}.{field}")
        anchors: list[TacticalAnchor] = []
        for anchor_id, coord_value in raw.items():
            _require_stable_id(anchor_id, f"{field} id")
            anchors.append(
                TacticalAnchor(
                    anchor_id,
                    _coord_from_value(
                        coord_value,
                        f"tactical_maps.{map_id}.{field}.{anchor_id}",
                    ),
                )
            )
        return tuple(anchors)

    return TacticalMap(
        map_id=map_id,
        version=version,
        width=width,
        height=height,
        z_layers=z_layers,
        cells=tuple(cells),
        transitions=tuple(transitions),
        deployment_zones=tuple(deployment_zones),
        objective_anchors=parse_anchors("objective_anchors"),
        exits=parse_anchors("exits"),
    )


def parse_tactical_maps(value: object) -> dict[str, TacticalMap]:
    """Parse the optional top-level tactical map mapping."""

    records = _mapping(value, "tactical_maps")
    parsed: dict[str, TacticalMap] = {}
    for map_id, definition in records.items():
        if not isinstance(map_id, str):
            raise ValueError("tactical map IDs must be text")
        parsed[map_id] = parse_tactical_map_definition(map_id, definition)
    return parsed
