from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any, Dict

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

    def _view_for(self, state: GameState) -> Dict[str, Any]:
        location = state.flags.get("location_id")
        if not isinstance(location, str) or not location:
            location = state.scene_id
        return {
            "scene": self.engine.build_scene_view(state),
            "status": self._status_view_for(state),
            "meta": {
                "content_id": self.content.content_id,
                "canon_status": self.content.canon_status,
                "turn": state.turn,
                "time_minutes": state.time_minutes,
                "schema_version": state.schema_version,
                "location": location,
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
