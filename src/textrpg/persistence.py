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
    payload: Dict[str, Any] = json.loads(raw)
    version = payload.get("schema_version")
    if version != CURRENT_SCHEMA_VERSION:
        raise RuleError(
            f"Unsupported save schema {version!r}; expected {CURRENT_SCHEMA_VERSION}. "
            "Add an explicit migration before loading this save."
        )
    required = ("seed", "scene_id")
    missing = [key for key in required if key not in payload]
    if missing:
        raise RuleError(f"Save is missing required keys: {', '.join(missing)}")

    fields = GameState.__dataclass_fields__
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
