from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, Mapping

from .content import LoadedContentPack, load_content_pack
from .core import GameState, RuleError
from .equipment import DEFAULT_SLOTS, equip_item
from .persistence import load_state, save_state
from .room_projection import build_room_projection
from .status import build_status_view, inspect_status_value


class AndroidBridgeError(RuntimeError):
    """Stable error boundary between the Python engine and Android presentation."""

    def __init__(self, code: str, public_message: str, *, technical_detail: str | None = None) -> None:
        if not isinstance(code, str) or not code:
            raise ValueError("AndroidBridgeError code must be non-empty text")
        if not isinstance(public_message, str) or not public_message:
            raise ValueError("AndroidBridgeError public_message must be non-empty text")
        super().__init__(f"{code}: {public_message}")
        self.code = code
        self.public_message = public_message
        self.technical_detail = technical_detail or ""


def _pretty_id(stable_id: str, prefix: str) -> str:
    value = stable_id.removeprefix(prefix)
    return value.replace("_", " ").title()


class AndroidGameSession:
    """Narrow, player-safe facade over one authoritative RPG playthrough."""

    def __init__(self, content: LoadedContentPack, *, save_path: str | Path | None = None) -> None:
        if not isinstance(content, LoadedContentPack):
            raise TypeError("AndroidGameSession requires a LoadedContentPack")
        self.content = content
        self.engine = content.engine
        self.state = content.state
        self._save_path = Path(save_path) if save_path is not None else None

    def _location_for(self, state: GameState) -> str:
        override = state.flags.get("android.map_location_override")
        if isinstance(override, str) and override:
            return override
        scene = self.engine.get_scene(state)
        authored = scene.get("location_id")
        if isinstance(authored, str) and authored:
            return authored
        flagged = state.flags.get("location_id")
        if isinstance(flagged, str) and flagged:
            return flagged
        return state.scene_id

    def _room_view_for(self, state: GameState) -> Dict[str, Any]:
        """Project authored visible presence without exposing durable NPC internals."""
        scene = self.engine.get_scene(state)
        return build_room_projection(scene, self._location_for(state))

    def _status_view_for(self, state: GameState) -> Dict[str, Any]:
        registries = self.content.registries
        conditions = registries.get("conditions", {})
        status = build_status_view(state, self.engine, ability_definitions=self.content.raw.get("powers", {}), condition_definitions=conditions)
        equipment_names = {record["slot"]: record["name"] for record in self._inventory_view_for(state)["equipment"] if record["equipped"]}
        condition_names = {record["id"]: record["name"] for record in status["conditions"]}
        values = [("attributes", stat) for stat in status["attributes"]]
        values.extend(("skills", stat) for group in status["skills"].values() for stat in group)
        for namespace, stat in values:
            explanation = inspect_status_value(state, self.engine, f"{namespace}.{stat['id']}", condition_definitions=conditions)
            contributions = []
            for source, value in explanation["breakdown"].items():
                if source in ("base", "total") or value == 0:
                    continue
                kind, _, key = source.partition(":")
                slot = None
                if kind == "equipment":
                    slot = key; label = equipment_names.get(key, "Equipped item")
                elif kind == "condition": label = condition_names.get(key, "Condition")
                elif kind == "perk":
                    definition = self.engine.perk_definitions.get(key, {}); label = definition.get("label")
                    if not isinstance(label, str) or not label: label = _pretty_id(key, "PERK_")
                elif kind == "set": label = "Equipment set bonus"
                elif source == "unidentified_modifier": kind = "unidentified"; label = "Unidentified modifier"
                else: raise RuleError("Unsupported player-visible stat contribution")
                contributions.append({"kind": kind, "label": label, "slot": slot, "value": value})
            stat["contributions"] = contributions
        return status

    def _inventory_view_for(self, state: GameState) -> Dict[str, Any]:
        item_definitions = self.content.registries.get("items", {})
        if not isinstance(item_definitions, Mapping): item_definitions = {}
        items = []
        for item_id in sorted(state.inventory):
            quantity = state.inventory[item_id]
            if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0: continue
            definition = item_definitions.get(item_id, {})
            if not isinstance(definition, Mapping): definition = {}
            label, slot, quality = definition.get("label"), definition.get("slot"), definition.get("quality")
            equippable = isinstance(slot, str) and slot in DEFAULT_SLOTS
            items.append({"id": item_id, "name": label if isinstance(label, str) and label else _pretty_id(item_id, "ITEM_"), "quantity": quantity, "equippable": equippable, "slot": slot if equippable else None, "quality": quality if isinstance(quality, str) and quality else None})
        equipment = []
        for slot in DEFAULT_SLOTS:
            record = state.equipment.get(slot)
            if not isinstance(record, Mapping): equipment.append({"slot": slot, "equipped": False}); continue
            item_id = record.get("item_id")
            if not isinstance(item_id, str) or not item_id: equipment.append({"slot": slot, "equipped": False}); continue
            definition = item_definitions.get(item_id, {})
            if not isinstance(definition, Mapping): definition = {}
            label = definition.get("label")
            equipment.append({"slot": slot, "equipped": True, "item_id": item_id, "name": label if isinstance(label, str) and label else _pretty_id(item_id, "ITEM_"), "quality": record.get("quality", "standard") if isinstance(record.get("quality", "standard"), str) else "standard"})
        return {"items": items, "equipment": equipment}

    def _visuals_view_for(self, state: GameState) -> Dict[str, Any]:
        quantity = state.inventory.get("ITEM_DEAD_RELAY", 0)
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0: relay_state = None
        elif state.flags.get("relay.signal_lost") is True: relay_state = "signal_lost"
        elif state.flags.get("relay.casing_damaged") is True: relay_state = "damaged"
        elif "KNOW_RELAY_DESTINATION_SERVICE_GATE_12" in state.knowledge: relay_state = "opened"
        else: relay_state = "intact"
        return {"relay_state": relay_state}

    def _quest_view_for(self, state: GameState) -> list[Dict[str, Any]]:
        definitions = self.content.raw.get("quests", {})
        if not isinstance(definitions, Mapping): return []
        output = []
        for quest_id in sorted(state.quests):
            record = state.quests[quest_id]
            if not isinstance(record, Mapping): continue
            definition = definitions.get(quest_id, {}); definition = definition if isinstance(definition, Mapping) else {}
            stage_id = record.get("stage"); stages = definition.get("stages", {}); stage = stages.get(stage_id, {}) if isinstance(stages, Mapping) else {}; objectives = stage.get("objectives", {}) if isinstance(stage, Mapping) else {}; objectives = objectives if isinstance(objectives, Mapping) else {}
            completed, failed, visible_objectives = set(record.get("completed_objectives", [])), set(record.get("failed_objectives", [])), []
            for objective_id, objective in objectives.items():
                if not isinstance(objective_id, str) or not isinstance(objective, Mapping): continue
                if objective_id in completed: status = "completed"
                elif objective_id in failed: status = "failed"
                else:
                    prerequisites = objective.get("requires_objectives", []); prerequisites = prerequisites if isinstance(prerequisites, list) else []
                    status = "active" if set(prerequisites).issubset(completed) else "locked"
                visible_objectives.append({"id": objective_id, "title": objective.get("title") if isinstance(objective.get("title"), str) else _pretty_id(objective_id, "OBJ_"), "required": bool(objective.get("required", True)), "status": status})
            category = definition.get("category", "optional"); category = category if category in ("main", "side", "optional", "lore") else "optional"
            output.append({"id": quest_id, "title": definition.get("title") if isinstance(definition.get("title"), str) else _pretty_id(quest_id, "QUEST_"), "description": definition.get("description", "") if isinstance(definition.get("description", ""), str) else "", "category": category, "status": record.get("status", "active"), "stage": stage_id if isinstance(stage_id, str) else "", "objectives": visible_objectives})
        return output

    def _map_view_for(self, state: GameState) -> Dict[str, Any]:
        authored = self.content.raw.get("world_map", {})
        if not isinstance(authored, Mapping): return {"title": "World", "current_location": self._location_for(state), "nodes": [], "edges": []}
        raw_nodes, raw_edges = authored.get("nodes", {}), authored.get("edges", [])
        if not isinstance(raw_nodes, Mapping) or not isinstance(raw_edges, list): raise RuleError("world_map must contain object nodes and list edges")
        scene_defs = self.content.raw.get("scenes", {}); scene_defs = scene_defs if isinstance(scene_defs, Mapping) else {}
        discovered = {self._location_for(state)}
        if state.flags.get("android_debug.discover_all_map") is True: discovered.update(location_id for location_id in raw_nodes if isinstance(location_id, str))
        for event in state.history:
            if not isinstance(event, Mapping): continue
            for key in ("scene", "next_scene"):
                scene_id = event.get(key)
                if isinstance(scene_id, str):
                    scene = scene_defs.get(scene_id, {})
                    if isinstance(scene, Mapping) and isinstance(scene.get("location_id"), str) and scene.get("location_id"): discovered.add(scene["location_id"])
        for location_id, node in raw_nodes.items():
            if isinstance(location_id, str) and isinstance(node, Mapping):
                discover_flag = node.get("discover_flag")
                if isinstance(discover_flag, str) and discover_flag and state.flags.get(discover_flag) is True: discovered.add(location_id)
        current_location = self._location_for(state)
        def is_reachable(location_id: str) -> bool:
            if location_id == current_location: return True
            return any(isinstance(edge, Mapping) and {edge.get("from"), edge.get("to")} == {current_location, location_id} and edge.get("from") in discovered and edge.get("to") in discovered for edge in raw_edges)
        nodes = []
        for location_id, node in raw_nodes.items():
            if location_id not in discovered or not isinstance(location_id, str) or not isinstance(node, Mapping): continue
            x, y = node.get("x", 0), node.get("y", 0); x = 0 if isinstance(x, bool) or not isinstance(x, (int, float)) else x; y = 0 if isinstance(y, bool) or not isinstance(y, (int, float)) else y
            nodes.append({"id": location_id, "title": node.get("title") if isinstance(node.get("title"), str) else _pretty_id(location_id, ""), "description": node.get("description", "") if isinstance(node.get("description", ""), str) else "", "x": float(x), "y": float(y), "current": location_id == current_location, "reachable": is_reachable(location_id)})
        edges = [{"from": edge.get("from"), "to": edge.get("to")} for edge in raw_edges if isinstance(edge, Mapping) and isinstance(edge.get("from"), str) and isinstance(edge.get("to"), str) and edge.get("from") in discovered and edge.get("to") in discovered]
        return {"title": authored.get("title", "World") if isinstance(authored.get("title", "World"), str) else "World", "current_location": current_location, "nodes": nodes, "edges": edges}

    def _view_for(self, state: GameState) -> Dict[str, Any]:
        return {"scene": self.engine.build_scene_view(state), "status": self._status_view_for(state), "inventory": self._inventory_view_for(state), "quests": self._quest_view_for(state), "map": self._map_view_for(state), "room": self._room_view_for(state), "visuals": self._visuals_view_for(state), "meta": {"content_id": self.content.content_id, "canon_status": self.content.canon_status, "turn": state.turn, "time_minutes": state.time_minutes, "schema_version": state.schema_version, "location": self._location_for(state)}}

    def scene_view(self) -> Dict[str, Any]:
        try: return deepcopy(self._view_for(self.state))
        except RuleError as exc: raise AndroidBridgeError("VIEW_ERROR", "The current game state could not be displayed.", technical_detail=str(exc)) from exc

    def inspect_status(self, path: str) -> Dict[str, Any]:
        if not isinstance(path, str) or not path: raise AndroidBridgeError("STAT_INSPECTION_ERROR", "Choose a valid stat to inspect.", technical_detail="path must be non-empty text")
        try: return deepcopy(inspect_status_value(self.state, self.engine, path, condition_definitions=self.content.registries.get("conditions", {})))
        except RuleError as exc: raise AndroidBridgeError("STAT_INSPECTION_ERROR", "That stat cannot be inspected.", technical_detail=str(exc)) from exc

    def choose(self, choice_id: str) -> Dict[str, Any]:
        if not isinstance(choice_id, str) or not choice_id: raise AndroidBridgeError("CHOICE_ERROR", "That choice is not available.", technical_detail="choice_id must be non-empty text")
        try:
            self.engine.choose(self.state, choice_id); self.state.flags.pop("android.map_location_override", None); return self.scene_view()
        except AndroidBridgeError: raise
        except RuleError as exc: raise AndroidBridgeError("CHOICE_ERROR", "That choice is not available.", technical_detail=str(exc)) from exc

    def travel(self, location_id: str) -> Dict[str, Any]:
        if not isinstance(location_id, str) or not location_id: raise AndroidBridgeError("TRAVEL_ERROR", "Choose a valid destination.")
        authored = self.content.raw.get("world_map", {})
        if not isinstance(authored, Mapping): raise AndroidBridgeError("TRAVEL_ERROR", "Travel is not available in this area.")
        raw_nodes, raw_edges = authored.get("nodes", {}), authored.get("edges", [])
        if not isinstance(raw_nodes, Mapping) or not isinstance(raw_edges, list): raise AndroidBridgeError("TRAVEL_ERROR", "Travel data is unavailable.")
        if location_id not in raw_nodes: raise AndroidBridgeError("TRAVEL_ERROR", "That destination does not exist.")
        current = self._location_for(self.state)
        if current == location_id: return self.scene_view()
        target_node = raw_nodes.get(location_id, {})
        if not isinstance(target_node, Mapping): raise AndroidBridgeError("TRAVEL_ERROR", "Travel data for that destination is invalid.")
        visible_map = self._map_view_for(self.state); discovered = {node["id"] for node in visible_map["nodes"] if isinstance(node, Mapping) and isinstance(node.get("id"), str)}
        if location_id not in discovered: raise AndroidBridgeError("TRAVEL_ERROR", "That destination has not been discovered.")
        connected, travel_minutes = False, 5
        for edge in raw_edges:
            if isinstance(edge, Mapping) and {edge.get("from"), edge.get("to")} == {current, location_id}:
                connected = True; authored_minutes = edge.get("travel_minutes", 5)
                if isinstance(authored_minutes, bool) or not isinstance(authored_minutes, int) or authored_minutes < 0: raise AndroidBridgeError("TRAVEL_ERROR", "Travel time data is invalid.")
                travel_minutes = authored_minutes; break
        if not connected: raise AndroidBridgeError("TRAVEL_ERROR", "No discovered route connects those locations.")
        before = deepcopy(self.state.snapshot())
        try:
            from .simulation import advance_time
            advance_time(self.state, travel_minutes); target_scene = target_node.get("scene_id")
            if target_scene is not None:
                if not isinstance(target_scene, str) or not target_scene or target_scene not in self.engine.scenes: raise RuleError(f"Map destination references invalid scene: {location_id}")
                self.state.scene_id = target_scene; self.state.flags.pop("android.map_location_override", None)
            else: self.state.flags["android.map_location_override"] = location_id
            self.state.history.append({"type": "map_travel", "from": current, "to": location_id, "travel_minutes": travel_minutes, "turn": self.state.turn, "time_minutes": self.state.time_minutes}); return self.scene_view()
        except AndroidBridgeError: self.state = GameState(**before); raise
        except (RuleError, TypeError, ValueError) as exc: self.state = GameState(**before); raise AndroidBridgeError("TRAVEL_ERROR", "Travel could not be completed.", technical_detail=str(exc)) from exc

    def equip(self, item_id: str) -> Dict[str, Any]:
        if not isinstance(item_id, str) or not item_id: raise AndroidBridgeError("EQUIP_ERROR", "Choose a valid item to equip.")
        definitions = self.content.registries.get("items", {}); definition = definitions.get(item_id) if isinstance(definitions, Mapping) else None
        if not isinstance(definition, Mapping): raise AndroidBridgeError("EQUIP_ERROR", "That item cannot be equipped.", technical_detail=f"Missing authored equipment definition: {item_id}")
        before = deepcopy(self.state.snapshot())
        try:
            authored_item = dict(definition); authored_item["item_id"] = item_id; previous = equip_item(self.state, authored_item, consume_inventory=True)
            if isinstance(previous, Mapping):
                replaced_id = previous.get("item_id")
                if isinstance(replaced_id, str) and replaced_id: self.state.inventory[replaced_id] = self.state.inventory.get(replaced_id, 0) + 1
            self.state.history.append({"type": "equipment_changed", "action": "equip", "item_id": item_id, "slot": authored_item.get("slot"), "turn": self.state.turn, "time_minutes": self.state.time_minutes}); return self.scene_view()
        except AndroidBridgeError: self.state = GameState(**before); raise
        except (RuleError, TypeError, ValueError) as exc: self.state = GameState(**before); raise AndroidBridgeError("EQUIP_ERROR", "That item could not be equipped.", technical_detail=str(exc)) from exc

    def unequip(self, slot: str) -> Dict[str, Any]:
        if not isinstance(slot, str) or slot not in DEFAULT_SLOTS: raise AndroidBridgeError("EQUIP_ERROR", "Choose a valid equipment slot.")
        before = deepcopy(self.state.snapshot())
        try:
            record = self.state.equipment.get(slot)
            if not isinstance(record, Mapping): raise AndroidBridgeError("EQUIP_ERROR", "That equipment slot is already empty.")
            item_id = record.get("item_id")
            if not isinstance(item_id, str) or not item_id: raise RuleError(f"Equipped slot has no valid item_id: {slot}")
            del self.state.equipment[slot]; self.state.inventory[item_id] = self.state.inventory.get(item_id, 0) + 1
            self.state.history.append({"type": "equipment_changed", "action": "unequip", "item_id": item_id, "slot": slot, "turn": self.state.turn, "time_minutes": self.state.time_minutes}); return self.scene_view()
        except AndroidBridgeError: self.state = GameState(**before); raise
        except (RuleError, TypeError, ValueError) as exc: self.state = GameState(**before); raise AndroidBridgeError("EQUIP_ERROR", "That item could not be unequipped.", technical_detail=str(exc)) from exc

    def apply_cheat(self, code: str) -> Dict[str, Any]:
        """Apply an explicit developer cheat without exposing generic state mutation."""
        if not isinstance(code, str) or not code.strip():
            raise AndroidBridgeError("CHEAT_ERROR", "Enter a valid cheat code.")

        normalized = code.strip().upper()
        before = deepcopy(self.state.snapshot())
        try:
            if normalized == "FULLRESTORE":
                resources = self.state.player.setdefault("resources", {})
                if not isinstance(resources, dict):
                    raise RuleError("player.resources must be mutable")
                for resource in self._status_view_for(self.state)["resources"]:
                    resources[resource["id"]] = resource["max"]
            elif normalized == "CLEARCONDITIONS":
                self.state.player["conditions"] = {}
            elif normalized == "GIVE_RELAY":
                current = self.state.inventory.get("ITEM_DEAD_RELAY", 0)
                if isinstance(current, bool) or not isinstance(current, int) or current < 0:
                    raise RuleError("ITEM_DEAD_RELAY inventory quantity must be a non-negative integer")
                self.state.inventory["ITEM_DEAD_RELAY"] = current + 1
            elif normalized == "MAXATTR":
                attributes = self.state.player.setdefault("attributes", {})
                if not isinstance(attributes, dict):
                    raise RuleError("player.attributes must be mutable")
                for attribute in self._status_view_for(self.state)["attributes"]:
                    attributes[attribute["id"]] = 100
            elif normalized == "DEBUGMAP":
                self.state.flags["android_debug.discover_all_map"] = True
            elif normalized == "DISTRICT":
                if "DISTRICT_HUB" not in self.engine.scenes:
                    raise RuleError("DISTRICT cheat requires DISTRICT_HUB content")
                self.state.flags["world.free_roam_unlocked"] = True
                self.state.flags["vertical_slice_01.opening_complete"] = True
                self.state.flags.pop("android.map_location_override", None)
                self.state.scene_id = "DISTRICT_HUB"
            else:
                raise AndroidBridgeError(
                    "CHEAT_ERROR",
                    "Unknown cheat code.",
                    technical_detail=f"Unsupported cheat code: {normalized}",
                )

            self.state.history.append(
                {
                    "type": "cheat_applied",
                    "code": normalized,
                    "turn": self.state.turn,
                    "time_minutes": self.state.time_minutes,
                }
            )
            return self.scene_view()
        except AndroidBridgeError:
            self.state = GameState(**before)
            raise
        except (RuleError, TypeError, ValueError) as exc:
            self.state = GameState(**before)
            raise AndroidBridgeError(
                "CHEAT_ERROR",
                "The cheat code could not be applied.",
                technical_detail=str(exc),
            ) from exc

    def _resolve_save_path(self, path: str | Path | None) -> Path:
        resolved = Path(path) if path is not None else self._save_path
        if resolved is None:
            raise AndroidBridgeError(
                "SAVE_PATH_REQUIRED",
                "No save location is configured.",
            )
        return resolved

    def save(self, path: str | Path | None = None) -> None:
        """Persist authoritative state through the versioned save contract."""
        target = self._resolve_save_path(path)
        try:
            save_state(target, self.state)
        except (OSError, RuleError, TypeError, ValueError) as exc:
            raise AndroidBridgeError(
                "SAVE_ERROR",
                "The game could not be saved.",
                technical_detail=str(exc),
            ) from exc

    def load(self, path: str | Path | None = None) -> Dict[str, Any]:
        """Load transactionally; a bad save never replaces the live state."""
        target = self._resolve_save_path(path)
        try:
            candidate = load_state(target)
            self.engine.get_scene(candidate)
            candidate_view = self._view_for(candidate)
        except (OSError, RuleError, TypeError, ValueError) as exc:
            raise AndroidBridgeError(
                "LOAD_ERROR",
                "The saved game could not be loaded.",
                technical_detail=str(exc),
            ) from exc

        self.state = candidate
        return deepcopy(candidate_view)


def create_session(
    content_path: str | Path,
    save_path: str | Path | None = None,
) -> AndroidGameSession:
    """Load one authored content pack and create the stable Android-facing facade."""
    try:
        content = load_content_pack(content_path)
    except (OSError, RuleError, TypeError, ValueError) as exc:
        raise AndroidBridgeError(
            "CONTENT_ERROR",
            "Game content could not be loaded.",
            technical_detail=str(exc),
        ) from exc
    return AndroidGameSession(content, save_path=save_path)


def open_android_session(
    content_path: str | Path,
    *,
    save_path: str | Path | None = None,
) -> AndroidGameSession:
    """Compatibility name retained for the room-projection integration."""
    return create_session(content_path, save_path=save_path)
