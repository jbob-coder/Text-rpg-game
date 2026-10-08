"""Observer-local combat knowledge and explicit safe queries.

Records are encounter-local observations, not a second NPC/lore database. The
integration caller supplies KnownIdentity values from existing durable knowledge.
Geometric visibility never grants a new contact or identity by itself.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from .combat_grid import TacticalOccupant, cover_rating, find_path, has_line_of_sight
from .combat_schema import TacticalCoord
from .combat_state import CombatSession, MovementPlan, path_traversal_cost


@dataclass(frozen=True)
class KnownIdentity:
    name: str
    faction: str | None = None

    def __post_init__(self):
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("known identity requires a name")
        if self.faction is not None and not isinstance(self.faction, str):
            raise ValueError("known faction must be text")


@dataclass(frozen=True)
class Contact:
    contact_id: str
    awareness: str
    coord: TacticalCoord
    last_seen_round: int


@dataclass(frozen=True)
class TargetPreview:
    coord: TacticalCoord
    budget_cost: int
    cover_defense: int | None


def distance(a: TacticalCoord, b: TacticalCoord) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z)


class CombatKnowledge:
    def __init__(self, session: CombatSession, *,
                 identities: Mapping[tuple[str, str], KnownIdentity] | None = None):
        self.session = session
        self.identities = dict(identities or {})
        if any(not isinstance(value, KnownIdentity) for value in self.identities.values()):
            raise ValueError("identity input must contain allowlisted KnownIdentity values")
        self.contacts: dict[tuple[str, str], Contact] = {}

    def _observer(self, actor_id: str):
        actor = self.session.actors.get(actor_id)
        if actor is None or actor.reinforcement_round > self.session.round_index:
            raise ValueError("target unavailable")
        return actor

    def _present(self, actor_id: str):
        actor = self._observer(actor_id)
        if actor.withdrawn:
            raise ValueError("target unavailable")
        return actor

    def record_detection(self, observer_id: str, target_id: str, *, detected: bool):
        """Apply an authoritative observation; the calling transaction logs it."""
        if not isinstance(detected, bool):
            raise ValueError("detected must be boolean")
        observer, target = self._present(observer_id), self._present(target_id)
        if observer_id == target_id:
            raise ValueError("self is not a contact")
        key = (observer_id, target_id)
        previous = self.contacts.get(key)
        if detected:
            if not has_line_of_sight(self.session.tactical_map, observer.coord, target.coord):
                raise ValueError("detection requires line of sight")
            # Allocate tokens only on observation; hidden roster size cannot affect them.
            token = previous.contact_id if previous else "CONTACT_" + str(
                1 + sum(owner == observer_id for owner, _ in self.contacts))
            state = "IDENTIFIED" if key in self.identities else "DETECTED"
            self.contacts[key] = Contact(token, state, target.coord, self.session.round_index)
        elif previous:
            self.contacts[key] = Contact(previous.contact_id, "SUSPECTED",
                                         previous.coord, previous.last_seen_round)

    def contact(self, observer_id: str, target_id: str) -> Contact | None:
        known = self.contacts.get((observer_id, target_id))
        if known is None:
            return None
        observer = self._observer(observer_id)
        target = self.session.actors.get(target_id)
        current = (not observer.withdrawn and target is not None and not target.withdrawn
                   and target.reinforcement_round <= self.session.round_index
                   and target.coord == known.coord
                   and has_line_of_sight(self.session.tactical_map, observer.coord, known.coord))
        if known.awareness in {"DETECTED", "IDENTIFIED"} and not current:
            return Contact(known.contact_id, "SUSPECTED", known.coord, known.last_seen_round)
        return known

    def detected_actor_ids(self, observer_id: str) -> tuple[str, ...]:
        return tuple(target for owner, target in sorted(self.contacts)
                     if owner == observer_id and self.contact(owner, target).awareness
                     in {"DETECTED", "IDENTIFIED"})

    def visible_cells(self, observer_id: str) -> tuple[TacticalCoord, ...]:
        observer = self._observer(observer_id)
        if observer.withdrawn:
            return ()
        return tuple(cell.coord for cell in sorted(self.session.tactical_map.cells,
                                                  key=lambda cell: cell.coord)
                     if has_line_of_sight(self.session.tactical_map, observer.coord, cell.coord))

    def player_view(self, observer_id: str) -> dict:
        observer = self._observer(observer_id)
        result = []
        tokens = {} if observer.withdrawn else {observer_id: "SELF"}
        for owner, target_id in sorted(self.contacts):
            if owner != observer_id:
                continue
            contact = self.contact(owner, target_id)
            item = {"contact_id": contact.contact_id, "awareness": contact.awareness}
            if contact.awareness in {"DETECTED", "IDENTIFIED"}:
                item["coord"] = contact.coord.key
                tokens[target_id] = contact.contact_id
            else:
                item.update(last_known_coord=contact.coord.key,
                            last_seen_round=contact.last_seen_round)
            identity = self.identities.get((owner, target_id))
            if identity:
                item["identity"] = {"name": identity.name}
                if identity.faction is not None:
                    item["identity"]["faction"] = identity.faction
            result.append(item)
        return {
            "round": self.session.round_index,
            "action_budget": observer.action_budget,
            "contacts": sorted(result, key=lambda item: item["contact_id"]),
            "visible_cells": [coord.key for coord in self.visible_cells(observer_id)],
            "initiative": [tokens[actor_id] for actor_id in self.session.initiative_order
                           if actor_id in tokens],
            "active_contact": tokens.get(self.session.active_actor_id),
        }

    def preview_target(self, observer_id: str, action_id: str, *,
                       target_actor_id: str | None = None,
                       target_coord: TacticalCoord | None = None) -> TargetPreview:
        actor = self.session._active_actor(observer_id)
        definition = self.session._action_definition(action_id)
        cost = self.session._action_cost(action_id)
        if actor.action_budget < cost:
            raise ValueError("insufficient action budget")
        if (target_actor_id is None) == (target_coord is None):
            raise ValueError("choose exactly one target")
        if target_actor_id is not None:
            contact = self.contact(observer_id, target_actor_id)
            if contact is None or contact.awareness not in {"DETECTED", "IDENTIFIED"}:
                raise ValueError("target unavailable")
            if definition.get("requires_identification", False) and contact.awareness != "IDENTIFIED":
                raise ValueError("target unavailable")
            coord = contact.coord
        else:
            coord = target_coord
            if not isinstance(coord, TacticalCoord) or self.session.tactical_map.cell_at(coord) is None:
                raise ValueError("target unavailable")
            contacts = [self.contact(owner, target) for owner, target in self.contacts
                        if owner == observer_id]
            current = [contact for contact in contacts if contact.coord == coord
                       and contact.awareness in {"DETECTED", "IDENTIFIED"}]
            last_known = any(contact.coord == coord for contact in contacts)
            if definition.get("requires_identification") and not any(
                    contact.awareness == "IDENTIFIED" for contact in current):
                raise ValueError("target unavailable")
            if definition.get("requires_detection") and not current:
                raise ValueError("target unavailable")
            if not (current or definition.get("allows_blind_area_targeting")
                    or (definition.get("allows_last_known_position") and last_known)):
                raise ValueError("target unavailable")
        if not definition.get("range_min", 0) <= distance(actor.coord, coord) <= definition.get("range_max", 0):
            raise ValueError("target out of range")
        if definition.get("requires_los") and not has_line_of_sight(
                self.session.tactical_map, actor.coord, coord):
            raise ValueError("target lacks line of sight")
        # Same-cell and cross-layer rays have no universal cover/elevation bonus.
        rating = (cover_rating(self.session.tactical_map, actor.coord, coord)
                  if actor.coord != coord and actor.coord.z == coord.z else 0)
        defense = (rating * 10 if has_line_of_sight(self.session.tactical_map, actor.coord, coord)
                   else None)
        return TargetPreview(coord, cost, defense)

    def preview_movement(self, actor_id: str, action_id: str,
                         goal: TacticalCoord) -> MovementPlan:
        """Plan against observed occupancy; commit rechecks the real world."""
        actor = self.session._active_actor(actor_id)
        cost, allowance = self.session._movement_action(action_id)
        if actor.action_budget < cost:
            raise ValueError("insufficient action budget")
        known_ids = self.detected_actor_ids(actor_id)
        occupants = [TacticalOccupant(actor_id, actor.faction_id, actor.coord)]
        for target_id in known_ids:
            contact = self.contact(actor_id, target_id)
            target = self.session.actors[target_id]
            occupants.append(TacticalOccupant(target_id, "UNKNOWN", contact.coord,
                                               solid=not target.incapacitated))
        path = find_path(self.session.tactical_map, actor.coord, goal,
                         occupants=occupants, moving_actor_id=actor_id,
                         moving_faction_id=actor.faction_id)
        if path is None:
            raise ValueError("movement unavailable")
        traversal = path_traversal_cost(self.session.tactical_map, path)
        if traversal > allowance:
            raise ValueError("movement exceeds allowance")
        return MovementPlan(action_id, path, traversal, allowance, cost)
