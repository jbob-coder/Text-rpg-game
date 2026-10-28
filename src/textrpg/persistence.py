from __future__ import annotations

import json
import os
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any, Dict

from .core import GameState, RuleError, validate_game_state_structure
from .json_contract import loads_strict_json


CURRENT_SCHEMA_VERSION = 1


def dumps_state(state: GameState) -> str:
    validate_game_state_structure(state)
    if state.schema_version != CURRENT_SCHEMA_VERSION:
        raise RuleError(
            f"Unsupported save schema {state.schema_version!r}; expected {CURRENT_SCHEMA_VERSION}. "
            "Add an explicit migration before saving this state."
        )
    payload = state.snapshot()
    try:
        return json.dumps(
            payload,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        raise RuleError("Game state cannot be serialized as strict JSON") from exc


def loads_state(raw: str) -> GameState:
    if not isinstance(raw, str):
        raise RuleError("Save payload must be JSON text")
    try:
        parsed = loads_strict_json(raw)
    except (json.JSONDecodeError, ValueError) as exc:
        raise RuleError("Save payload is not valid strict JSON") from exc
    if not isinstance(parsed, dict):
        raise RuleError("Save payload must be a JSON object")

    payload: Dict[str, Any] = parsed
    version = payload.get("schema_version")
    if (
        isinstance(version, bool)
        or not isinstance(version, int)
        or version != CURRENT_SCHEMA_VERSION
    ):
        raise RuleError(
            f"Unsupported save schema {version!r}; expected {CURRENT_SCHEMA_VERSION}. "
            "Add an explicit migration before loading this save."
        )

    required = ("seed", "scene_id")
    missing = [key for key in required if key not in payload]
    if missing:
        raise RuleError(f"Save is missing required keys: {', '.join(missing)}")
    for key in required:
        if not isinstance(payload[key], str) or not payload[key]:
            raise RuleError(f"Save field {key} must be a non-empty string")

    fields = GameState.__dataclass_fields__
    unknown = sorted(set(payload) - set(fields))
    if unknown:
        raise RuleError(
            "Save contains unsupported fields for the current schema: "
            + ", ".join(unknown)
        )

    kwargs = {key: value for key, value in payload.items() if key in fields}
    state = GameState(**kwargs)
    validate_game_state_structure(state)
    return state


def save_state(path: str | Path, state: GameState) -> None:
    # Validate before creating any files, and never reuse a shared .tmp path:
    # concurrent saves must not overwrite one another's in-progress contents.
    serialized = dumps_state(state)
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary_path: Path | None = None
    try:
        with NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=target.parent,
            prefix=f".{target.name}.",
            suffix=".tmp",
            delete=False,
        ) as temporary:
            temporary_path = Path(temporary.name)
            temporary.write(serialized)
        os.replace(temporary_path, target)
    finally:
        # os.replace removes the source on success. On any write/replace
        # failure, remove only the unique temporary file, not the prior save.
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def load_state(path: str | Path) -> GameState:
    return loads_state(Path(path).read_text(encoding="utf-8"))
