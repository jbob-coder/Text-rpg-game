from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, Mapping

from .content import LoadedContentPack, load_content_pack
from .core import GameState, RuleError
from .persistence import load_state, save_state
from .status import build_status_view


class AndroidBridgeError(RuntimeError):
    """Stable error boundary between the Python engine and Android presentation."""

    def __init__(
        self,
        code: str,
        public_message: str,
        *,
        technical_detail: str | None = None,
    ) -> None:
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

    def __init__(
        self,
        content: LoadedContentPack,
        *,
        save_path: str | Path | None = None,
    ) -> None:
        if not isinstance(content, LoadedContentPack):
            raise TypeError("AndroidGameSession requires a LoadedContentPack")
        self.content = content
        self.engine = content.engine
        self.state = content.state
        self._save_path = Path(save_path) if save_path is not None else None

    def _status_view_for(self, state: GameState) -> Dict[str, Any]:
        registries = self.content.registries
        return build_status_view(
            state,
            self.engine,
            ability_definitions=self.content.raw.get("powers", {}),
            condition_definitions=registries.get("conditions", {}),
        )

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


    def _inventory_view_for(self, state: GameState) -> Dict[str, Any]:
        item_definitions = self.content.registries.get("items", {})
        if not isinstance(item_definitions, Mapping):
            item_definitions = {}

        items: list[Dict[str, Any]] = []
        for item_id in sorted(state.inventory):
            quantity = state.inventory[item_id]
            if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0:
                continue
            definition = item_definitions.get(item_id, {})
            if not isinstance(definition, Mapping):
                definition = {}
            label = definition.get("label")
            items.append(
                {
                    "id": item_id,
                    "name": label if isinstance(label, str) and label else _pretty_id(item_id, "ITEM_"),
                    "quantity": quantity,
                }
            )

        equipment: list[Dict[str, Any]] = []
        for slot in (
            "head",
            "body",
            "hands",
            "legs",
            "feet",
            "main_hand",
            "off_hand",
            "accessory_1",
            "accessory_2",
        ):
            record = state.equipment.get(slot)
            if not isinstance(record, Mapping):
                equipment.append({"slot": slot, "equipped": False})
                continue
            item_id = record.get("item_id")
            if not isinstance(item_id, str) or not item_id:
                equipment.append({"slot": slot, "equipped": False})
                continue
            definition = item_definitions.get(item_id, {})
            if not isinstance(definition, Mapping):
                definition = {}
            label = definition.get("label")
            equipment.append(
                {
                    "slot": slot,
                    "equipped": True,
                    "item_id": item_id,
                    "name": label if isinstance(label, str) and label else _pretty_id(item_id, "ITEM_"),
                    "quality": record.get("quality", "standard")
                    if isinstance(record.get("quality", "standard"), str)
                    else "standard",
                }
            )
        return {"items": items, "equipment": equipment}

    def _quest_view_for(self, state: GameState) -> list[Dict[str, Any]]:
        definitions = self.content.raw.get("quests", {})
        if not isinstance(definitions, Mapping):
            return []

        output: list[Dict[str, Any]] = []
        for quest_id in sorted(state.quests):
            record = state.quests[quest_id]
            if not isinstance(record, Mapping):
                continue
            definition = definitions.get(quest_id, {})
            if not isinstance(definition, Mapping):
                definition = {}

            stage_id = record.get("stage")
            stages = definition.get("stages", {})
            stage = stages.get(stage_id, {}) if isinstance(stages, Mapping) else {}
            objectives = stage.get("objectives", {}) if isinstance(stage, Mapping) else {}
            if not isinstance(objectives, Mapping):
                objectives = {}

            completed = set(record.get("completed_objectives", []))
            failed = set(record.get("failed_objectives", []))
            visible_objectives: list[Dict[str, Any]] = []
            for objective_id, objective in objectives.items():
                if not isinstance(objective_id, str) or not isinstance(objective, Mapping):
                    continue
                if objective_id in completed:
                    status = "completed"
                elif objective_id in failed:
                    status = "failed"
                else:
                    prerequisites = objective.get("requires_objectives", [])
                    if not isinstance(prerequisites, list):
                        prerequisites = []
                    status = "active" if set(prerequisites).issubset(completed) else "locked"

                visible_objectives.append(
                    {
                        "id": objective_id,
                        "title": objective.get("title")
                        if isinstance(objective.get("title"), str)
                        else _pretty_id(objective_id, "OBJ_"),
                        "required": bool(objective.get("required", True)),
                        "status": status,
                    }
                )

            category = definition.get("category", "optional")
            if category not in ("main", "side", "optional", "lore"):
                category = "optional"

            output.append(
                {
                    "id": quest_id,
                    "title": definition.get("title")
                    if isinstance(definition.get("title"), str)
                    else _pretty_id(quest_id, "QUEST_"),
                    "description": definition.get("description", "")
                    if isinstance(definition.get("description", ""), str)
                    else "",
                    "category": category,
                    "status": record.get("status", "active"),
                    "stage": stage_id if isinstance(stage_id, str) else "",
                    "objectives": visible_objectives,
                }
            )
        return output

    def _map_view_for(self, state: GameState) -> Dict[str, Any]:
        authored = self.content.raw.get("world_map", {})
        if not isinstance(authored, Mapping):
            return {"title": "World", "current_location": self._location_for(state), "nodes": [], "edges": []}

        raw_nodes = authored.get("nodes", {})
        raw_edges = authored.get("edges", [])
        if not isinstance(raw_nodes, Mapping) or not isinstance(raw_edges, list):
            raise RuleError("world_map must contain object nodes and list edges")

        scene_defs = self.content.raw.get("scenes", {})
        if not isinstance(scene_defs, Mapping):
            scene_defs = {}

        discovered: set[str] = {self._location_for(state)}
        if state.flags.get("android_debug.discover_all_map") is True:
            discovered.update(
                location_id for location_id in raw_nodes
                if isinstance(location_id, str)
            )
        for event in state.history:
            if not isinstance(event, Mapping):
                continue
            for key in ("scene", "next_scene"):
                scene_id = event.get(key)
                if not isinstance(scene_id, str):
                    continue
                scene = scene_defs.get(scene_id, {})
                if isinstance(scene, Mapping):
                    location_id = scene.get("location_id")
                    if isinstance(location_id, str) and location_id:
                        discovered.add(location_id)

        nodes: list[Dict[str, Any]] = []
        for location_id, node in raw_nodes.items():
            if location_id not in discovered or not isinstance(location_id, str) or not isinstance(node, Mapping):
                continue
            x = node.get("x", 0)
            y = node.get("y", 0)
            if isinstance(x, bool) or not isinstance(x, (int, float)):
                x = 0
            if isinstance(y, bool) or not isinstance(y, (int, float)):
                y = 0
            nodes.append(
                {
                    "id": location_id,
                    "title": node.get("title")
                    if isinstance(node.get("title"), str)
                    else _pretty_id(location_id, ""),
                    "description": node.get("description", "")
                    if isinstance(node.get("description", ""), str)
                    else "",
                    "x": float(x),
                    "y": float(y),
                    "current": location_id == self._location_for(state),
                }
            )

        edges: list[Dict[str, str]] = []
        for edge in raw_edges:
            if not isinstance(edge, Mapping):
                continue
            start = edge.get("from")
            end = edge.get("to")
            if isinstance(start, str) and isinstance(end, str) and start in discovered and end in discovered:
                edges.append({"from": start, "to": end})

        return {
            "title": authored.get("title", "World")
            if isinstance(authored.get("title", "World"), str)
            else "World",
            "current_location": self._location_for(state),
            "nodes": nodes,
            "edges": edges,
        }

    def _view_for(self, state: GameState) -> Dict[str, Any]:
        return {
            "scene": self.engine.build_scene_view(state),
            "status": self._status_view_for(state),
            "inventory": self._inventory_view_for(state),
            "quests": self._quest_view_for(state),
            "map": self._map_view_for(state),
            "meta": {
                "content_id": self.content.content_id,
                "canon_status": self.content.canon_status,
                "turn": state.turn,
                "time_minutes": state.time_minutes,
                "schema_version": state.schema_version,
                "location": self._location_for(state),
            },
        }

    def scene_view(self) -> Dict[str, Any]:
        """Return a detached player-facing projection for the current game state."""
        try:
            return deepcopy(self._view_for(self.state))
        except RuleError as exc:
            raise AndroidBridgeError(
                "VIEW_ERROR",
                "The current game state could not be displayed.",
                technical_detail=str(exc),
            ) from exc

    def choose(self, choice_id: str) -> Dict[str, Any]:
        """Apply one visible choice and return the updated player-safe projection."""
        if not isinstance(choice_id, str) or not choice_id:
            raise AndroidBridgeError(
                "CHOICE_ERROR",
                "That choice is not available.",
                technical_detail="choice_id must be non-empty text",
            )
        try:
            self.engine.choose(self.state, choice_id)
            self.state.flags.pop("android.map_location_override", None)
            return self.scene_view()
        except AndroidBridgeError:
            raise
        except RuleError as exc:
            raise AndroidBridgeError(
                "CHOICE_ERROR",
                "That choice is not available.",
                technical_detail=str(exc),
            ) from exc



    def travel(self, location_id: str) -> Dict[str, Any]:
        """Move between discovered adjacent map nodes without bypassing story rules."""
        if not isinstance(location_id, str) or not location_id:
            raise AndroidBridgeError(
                "TRAVEL_ERROR",
                "Choose a valid destination.",
            )

        authored = self.content.raw.get("world_map", {})
        if not isinstance(authored, Mapping):
            raise AndroidBridgeError(
                "TRAVEL_ERROR",
                "Travel is not available in this area.",
            )
        raw_nodes = authored.get("nodes", {})
        raw_edges = authored.get("edges", [])
        if not isinstance(raw_nodes, Mapping) or not isinstance(raw_edges, list):
            raise AndroidBridgeError(
                "TRAVEL_ERROR",
                "Travel data is unavailable.",
            )
        if location_id not in raw_nodes:
            raise AndroidBridgeError(
                "TRAVEL_ERROR",
                "That destination does not exist.",
            )

        current = self._location_for(self.state)
        if current == location_id:
            return self.scene_view()

        visible_map = self._map_view_for(self.state)
        discovered = {
            node["id"] for node in visible_map["nodes"]
            if isinstance(node, Mapping) and isinstance(node.get("id"), str)
        }
        if location_id not in discovered:
            raise AndroidBridgeError(
                "TRAVEL_ERROR",
                "That destination has not been discovered.",
            )

        connected = False
        travel_minutes = 5
        for edge in raw_edges:
            if not isinstance(edge, Mapping):
                continue
            start = edge.get("from")
            end = edge.get("to")
            if {start, end} == {current, location_id}:
                connected = True
                authored_minutes = edge.get("travel_minutes", 5)
                if (
                    isinstance(authored_minutes, bool)
                    or not isinstance(authored_minutes, int)
                    or authored_minutes < 0
                ):
                    raise AndroidBridgeError(
                        "TRAVEL_ERROR",
                        "Travel time data is invalid.",
                    )
                travel_minutes = authored_minutes
                break

        if not connected:
            raise AndroidBridgeError(
                "TRAVEL_ERROR",
                "No discovered route connects those locations.",
            )

        before = deepcopy(self.state.snapshot())
        try:
            from .simulation import advance_time

            advance_time(self.state, travel_minutes)
            self.state.flags["android.map_location_override"] = location_id
            self.state.history.append(
                {
                    "type": "map_travel",
                    "from": current,
                    "to": location_id,
                    "travel_minutes": travel_minutes,
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
                "TRAVEL_ERROR",
                "Travel could not be completed.",
                technical_detail=str(exc),
            ) from exc

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
                self.state.inventory["ITEM_DEAD_RELAY"] = (
                    self.state.inventory.get("ITEM_DEAD_RELAY", 0) + 1
                )
            elif normalized == "MAXATTR":
                attributes = self.state.player.setdefault("attributes", {})
                if not isinstance(attributes, dict):
                    raise RuleError("player.attributes must be mutable")
                for attribute in self._status_view_for(self.state)["attributes"]:
                    attributes[attribute["id"]] = 100
            elif normalized == "DEBUGMAP":
                self.state.flags["android_debug.discover_all_map"] = True
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
        """Persist the authoritative state using the versioned engine save contract."""
        target = self._resolve_save_path(path)
        try:
            save_state(target, self.state)
        except (OSError, RuleError, ValueError, TypeError) as exc:
            raise AndroidBridgeError(
                "SAVE_ERROR",
                "The game could not be saved.",
                technical_detail=str(exc),
            ) from exc

    def load(self, path: str | Path | None = None) -> Dict[str, Any]:
        """Load a save transactionally: invalid saves never replace the live state."""
        target = self._resolve_save_path(path)
        try:
            candidate = load_state(target)
            self.engine.get_scene(candidate)
            candidate_view = self._view_for(candidate)
        except (OSError, RuleError, ValueError, TypeError) as exc:
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
    """Load one authored content pack and create an Android-facing game session."""
    try:
        content = load_content_pack(content_path)
    except (OSError, RuleError, ValueError, TypeError) as exc:
        raise AndroidBridgeError(
            "CONTENT_ERROR",
            "Game content could not be loaded.",
            technical_detail=str(exc),
        ) from exc
    return AndroidGameSession(content, save_path=save_path)
