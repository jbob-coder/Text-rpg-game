from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

from .content import LoadedContentPack, load_content_pack
from .core import GameState, RuleError, RulesEngine
from .persistence import load_state, save_state


def render_scene(engine: RulesEngine, state: GameState) -> str:
    scene = engine.get_scene(state)
    lines = [
        "",
        f"== {scene.get('title', state.scene_id)} ==",
        scene.get("body", ""),
        "",
    ]
    choices = engine.available_choices(state)
    if not choices:
        lines.append("[No choices are currently available.]")
        return "\n".join(lines)

    for index, choice in enumerate(choices, start=1):
        suffix = ""
        if not choice.get("enabled", True):
            suffix = f" [LOCKED: {choice.get('disabled_reason', 'Requirements not met')}]"
        lines.append(f"{index}. {choice['text']}{suffix}")
    return "\n".join(lines)


def render_state_summary(state: GameState) -> str:
    resources = state.player.get("resources", {})
    quest_lines = []
    for quest_id, quest in sorted(state.quests.items()):
        quest_lines.append(
            f"{quest_id}: {quest.get('status', 'unknown')} / {quest.get('stage', 'unknown')}"
        )
    return "\n".join(
        [
            f"Scene: {state.scene_id}",
            f"Turn: {state.turn}",
            f"Time: {state.time_minutes} minutes",
            f"Party: {', '.join(state.party) if state.party else 'solo'}",
            "Resources: " + json.dumps(resources, sort_keys=True),
            "Quests: " + ("; ".join(quest_lines) if quest_lines else "none"),
        ]
    )


def _enabled_choice_ids(engine: RulesEngine, state: GameState) -> list[str]:
    return [
        choice["id"]
        for choice in engine.available_choices(state)
        if choice.get("enabled", True)
    ]


def apply_choice_number(
    engine: RulesEngine,
    state: GameState,
    choice_number: int,
) -> dict:
    choices = engine.available_choices(state)
    if choice_number < 1 or choice_number > len(choices):
        raise RuleError("Choice number is out of range")
    choice = choices[choice_number - 1]
    if not choice.get("enabled", True):
        raise RuleError(
            choice.get("disabled_reason", f"Choice is locked: {choice['id']}")
        )
    return engine.choose(state, choice["id"])


def play(
    pack: LoadedContentPack,
    *,
    save_path: str | Path | None = None,
    input_fn=input,
    output_fn=print,
) -> GameState:
    state = pack.state
    engine = pack.engine

    output_fn(f"{pack.title} [{pack.canon_status}]")
    output_fn("Commands: number = choose, state = summary, save = save, quit = exit")

    while True:
        output_fn(render_scene(engine, state))
        command = input_fn("> ").strip()

        if command.lower() in {"quit", "q", "exit"}:
            break
        if command.lower() in {"state", "stats"}:
            output_fn(render_state_summary(state))
            continue
        if command.lower() == "save":
            if save_path is None:
                output_fn("No save path configured.")
            else:
                save_state(save_path, state)
                output_fn(f"Saved: {save_path}")
            continue

        try:
            number = int(command)
            event = apply_choice_number(engine, state, number)
            output_fn(
                f"[{event['choice']}] -> {event['outcome']} | "
                f"time={event['time_minutes']}m"
            )
            if save_path is not None:
                save_state(save_path, state)
        except (ValueError, RuleError) as exc:
            output_fn(f"Invalid action: {exc}")

    return state


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Play an authored Text RPG content pack in a local terminal."
    )
    parser.add_argument("content", help="Path to a content-pack JSON file")
    parser.add_argument("--save", dest="save_path", help="Optional save JSON path")
    parser.add_argument(
        "--load-save",
        dest="load_save_path",
        help="Optional existing save JSON to resume against this content pack",
    )
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    try:
        pack = load_content_pack(args.content)
        if args.load_save_path:
            state = load_state(args.load_save_path)
            if state.scene_id not in pack.engine.scenes:
                raise RuleError(
                    f"Loaded save scene is not present in content pack: {state.scene_id}"
                )
            pack.state = state
        play(pack, save_path=args.save_path)
    except RuleError as exc:
        print(f"Cannot start game: {exc}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
