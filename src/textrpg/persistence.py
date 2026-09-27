from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from .core import GameState, RuleError


CURRENT_SCHEMA_VERSION = 1


def dumps_state(state: GameState) -> str:
    payload = state.snapshot()
    payload["schema_version"] = CURRENT_SCHEMA_VERSION
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)


def loads_state(raw: str) -> GameState:
    if not isinstance(raw, str):
        raise RuleError("Save payload must be JSON text")
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuleError("Save payload is not valid JSON") from exc
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
    return GameState(**kwargs)


def save_state(path: str | Path, state: GameState) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    temp = target.with_suffix(target.suffix + ".tmp")
    temp.write_text(dumps_state(state), encoding="utf-8")
    temp.replace(target)


def load_state(path: str | Path) -> GameState:
    return loads_state(Path(path).read_text(encoding="utf-8"))
