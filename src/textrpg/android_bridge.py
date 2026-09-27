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
        scene = self.engine.get_scene(state)
        authored = scene.get("location_id")
        if isinstance(authored, str) and authored:
            return authored

        flagged = state.flags.get("location_id")
        if isinstance(flagged, str) and flagged:
            return flagged
        return state.scene_id

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
            return self.scene_view()
        except AndroidBridgeError:
            raise
        except RuleError as exc:
            raise AndroidBridgeError(
                "CHOICE_ERROR",
                "That choice is not available.",
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
