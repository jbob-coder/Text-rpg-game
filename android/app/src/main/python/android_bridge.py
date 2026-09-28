from __future__ import annotations

from copy import deepcopy
import json
from typing import Any

from textrpg.content import content_pack_from_mapping
from textrpg.core import RuleError
from textrpg.json_contract import loads_strict_json
from textrpg.persistence import dumps_state, loads_state
from textrpg.status import build_status_view


class AndroidGameSession:
    """Thin JSON bridge from Android UI intent to the authoritative rules engine."""

    def __init__(self, content_json: str, save_json: str = "") -> None:
        if not isinstance(content_json, str) or not content_json.strip():
            raise RuleError("Android content payload must be non-empty JSON text")
        if not isinstance(save_json, str):
            raise RuleError("Android save payload must be JSON text")

        try:
            content_data = loads_strict_json(content_json)
        except ValueError as exc:
            raise RuleError("Android content payload is not valid strict JSON") from exc

        self._pack = content_pack_from_mapping(content_data)
        self._state = self._pack.state

        if save_json.strip():
            resumed = loads_state(save_json)
            if resumed.scene_id not in self._pack.engine.scenes:
                raise RuleError(
                    "Loaded Android save scene is not present in the content pack: "
                    + resumed.scene_id
                )
            self._state = resumed
            self._pack.state = resumed

    def _view(self) -> dict[str, Any]:
        powers = self._pack.raw.get("powers", {})
        conditions = self._pack.registries.get("conditions", {})
        return {
            "game": {
                "content_id": self._pack.content_id,
                "title": self._pack.title,
                "canon_status": self._pack.canon_status,
            },
            "scene": self._pack.engine.build_scene_view(self._state),
            "status": build_status_view(
                self._state,
                self._pack.engine,
                ability_definitions=powers,
                condition_definitions=conditions,
            ),
            "turn": self._state.turn,
            "time_minutes": self._state.time_minutes,
            "party": list(self._state.party),
        }

    @staticmethod
    def _json(payload: Any) -> str:
        return json.dumps(
            payload,
            ensure_ascii=False,
            allow_nan=False,
            separators=(",", ":"),
        )

    def view_json(self) -> str:
        return self._json(self._view())

    def save_json(self) -> str:
        return dumps_state(self._state)

    def choose_json(self, choice_id: str) -> str:
        if not isinstance(choice_id, str) or not choice_id:
            raise RuleError("Android choice ID must be non-empty text")

        before = deepcopy(self._state)
        try:
            self._pack.engine.choose(self._state, choice_id)
            payload = {
                "view": self._view(),
                "save": dumps_state(self._state),
            }
            return self._json(payload)
        except Exception:
            self._state = before
            self._pack.state = before
            raise


def create_session(content_json: str, save_json: str = "") -> AndroidGameSession:
    return AndroidGameSession(content_json, save_json)
