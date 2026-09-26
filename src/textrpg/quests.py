from __future__ import annotations

import re
from typing import Any, Dict, Mapping

from .core import GameState, RuleError


STABLE_ID = re.compile(r"^[A-Z][A-Z0-9_]*$")


QUEST_STATUSES = ("active", "completed", "failed")


def _validate_stable_id(value: Any, label: str, errors: list[str]) -> None:
    if not isinstance(value, str) or not STABLE_ID.fullmatch(value):
        errors.append(f"{label} must be a stable uppercase ID: {value!r}")


def validate_quest_definitions(
    definitions: Mapping[str, Mapping[str, Any]],
) -> list[str]:
    """Validate authored quest graphs before a playthrough uses them.

    Quest definitions are data. This validator checks stable IDs, stage/objective
    references, terminal outcomes, and branch targets without executing the quest.
    """
    errors: list[str] = []

    for quest_id, definition in definitions.items():
        _validate_stable_id(quest_id, "quest_id", errors)

        if not isinstance(definition, Mapping):
            errors.append(f"{quest_id} must be an object")
            continue

        stages = definition.get("stages")
        if not isinstance(stages, Mapping) or not stages:
            errors.append(f"{quest_id}.stages must be a non-empty object")
            continue

        start_stage = definition.get("start_stage")
        _validate_stable_id(start_stage, f"{quest_id}.start_stage", errors)
        if isinstance(start_stage, str) and start_stage not in stages:
            errors.append(f"{quest_id}.start_stage references unknown stage {start_stage!r}")

        for stage_id, stage in stages.items():
            _validate_stable_id(stage_id, f"{quest_id}.stage_id", errors)
            if not isinstance(stage, Mapping):
                errors.append(f"{quest_id}.{stage_id} must be an object")
                continue

            objectives = stage.get("objectives", {})
            if not isinstance(objectives, Mapping):
                errors.append(f"{quest_id}.{stage_id}.objectives must be an object")
                objectives = {}

            objective_ids = set(objectives.keys())
            for objective_id, objective in objectives.items():
                location = f"{quest_id}.{stage_id}.{objective_id}"
                _validate_stable_id(objective_id, f"{location}.objective_id", errors)
                if not isinstance(objective, Mapping):
                    errors.append(f"{location} must be an object")
                    continue

                for required_id in objective.get("requires_objectives", []):
                    if required_id not in objective_ids:
                        errors.append(
                            f"{location} requires unknown objective {required_id!r} "
                            f"in stage {stage_id}"
                        )

                for outcome_key in ("on_complete", "on_fail"):
                    outcome = objective.get(outcome_key)
                    if outcome is not None:
                        _validate_quest_outcome(
                            quest_id,
                            stage_id,
                            f"{location}.{outcome_key}",
                            outcome,
                            stages,
                            errors,
                        )

            for outcome_key in ("on_complete", "on_fail"):
                outcome = stage.get(outcome_key)
                if outcome is not None:
                    _validate_quest_outcome(
                        quest_id,
                        stage_id,
                        f"{quest_id}.{stage_id}.{outcome_key}",
                        outcome,
                        stages,
                        errors,
                    )

            if stage.get("terminal") is True:
                status = stage.get("terminal_status", "completed")
                if status not in ("completed", "failed"):
                    errors.append(
                        f"{quest_id}.{stage_id}.terminal_status must be completed or failed"
                    )

    return errors


def _validate_quest_outcome(
    quest_id: str,
    stage_id: str,
    location: str,
    outcome: Any,
    stages: Mapping[str, Any],
    errors: list[str],
) -> None:
    if not isinstance(outcome, Mapping):
        errors.append(f"{location} must be an object")
        return

    next_stage = outcome.get("next_stage")
    status = outcome.get("status")

    if next_stage is not None:
        _validate_stable_id(next_stage, f"{location}.next_stage", errors)
        if isinstance(next_stage, str) and next_stage not in stages:
            errors.append(
                f"{location} references unknown stage {next_stage!r} "
                f"from {quest_id}/{stage_id}"
            )

    if status is not None and status not in QUEST_STATUSES:
        errors.append(f"{location}.status has unsupported value {status!r}")

    if next_stage is None and status is None:
        errors.append(f"{location} must define next_stage or status")


def assert_valid_quest_definitions(
    definitions: Mapping[str, Mapping[str, Any]],
) -> None:
    errors = validate_quest_definitions(definitions)
    if errors:
        raise RuleError("Invalid quest definitions:\n- " + "\n- ".join(errors))


def start_quest(
    state: GameState,
    quest_id: str,
    definition: Mapping[str, Any],
) -> Dict[str, Any]:
    if quest_id in state.quests:
        raise RuleError(f"Quest already exists in state: {quest_id}")

    errors = validate_quest_definitions({quest_id: definition})
    if errors:
        raise RuleError("Invalid quest definition:\n- " + "\n- ".join(errors))

    stage = definition["start_stage"]
    record = {
        "status": "active",
        "stage": stage,
        "completed_objectives": [],
        "failed_objectives": [],
        "started_at_minutes": state.time_minutes,
        "updated_at_minutes": state.time_minutes,
        "history": [
            {
                "type": "quest_started",
                "stage": stage,
                "time_minutes": state.time_minutes,
            }
        ],
    }
    state.quests[quest_id] = record
    state.history.append(
        {
            "type": "quest_started",
            "quest_id": quest_id,
            "stage": stage,
            "turn": state.turn,
            "time_minutes": state.time_minutes,
        }
    )
    _resolve_terminal_stage(state, quest_id, definition)
    return record


def available_objectives(
    state: GameState,
    quest_id: str,
    definition: Mapping[str, Any],
) -> list[str]:
    quest = _active_quest(state, quest_id)
    stage = _stage_definition(quest_id, quest["stage"], definition)

    completed = set(quest.get("completed_objectives", []))
    failed = set(quest.get("failed_objectives", []))
    output: list[str] = []

    for objective_id, objective in stage.get("objectives", {}).items():
        if objective_id in completed or objective_id in failed:
            continue
        prerequisites = set(objective.get("requires_objectives", []))
        if prerequisites.issubset(completed):
            output.append(objective_id)

    return output


def complete_objective(
    state: GameState,
    quest_id: str,
    objective_id: str,
    definition: Mapping[str, Any],
) -> Dict[str, Any]:
    quest = _active_quest(state, quest_id)
    stage_id = quest["stage"]
    stage = _stage_definition(quest_id, stage_id, definition)
    objectives = stage.get("objectives", {})

    if objective_id not in objectives:
        raise RuleError(
            f"Objective does not belong to current quest stage: "
            f"{quest_id}/{stage_id}/{objective_id}"
        )
    if objective_id not in available_objectives(state, quest_id, definition):
        raise RuleError(f"Objective is not currently available: {objective_id}")

    quest["completed_objectives"].append(objective_id)
    quest["updated_at_minutes"] = state.time_minutes
    objective = objectives[objective_id]

    event = {
        "type": "quest_objective_completed",
        "quest_id": quest_id,
        "stage": stage_id,
        "objective_id": objective_id,
        "turn": state.turn,
        "time_minutes": state.time_minutes,
    }
    quest["history"].append(dict(event))
    state.history.append(dict(event))

    outcome = objective.get("on_complete")
    if outcome:
        _apply_quest_outcome(state, quest_id, definition, outcome, event)
    elif _all_required_objectives_complete(quest, stage):
        stage_outcome = stage.get("on_complete")
        if stage_outcome:
            _apply_quest_outcome(state, quest_id, definition, stage_outcome, event)

    _resolve_terminal_stage(state, quest_id, definition)
    return event


def fail_objective(
    state: GameState,
    quest_id: str,
    objective_id: str,
    definition: Mapping[str, Any],
) -> Dict[str, Any]:
    quest = _active_quest(state, quest_id)
    stage_id = quest["stage"]
    stage = _stage_definition(quest_id, stage_id, definition)
    objectives = stage.get("objectives", {})

    if objective_id not in objectives:
        raise RuleError(
            f"Objective does not belong to current quest stage: "
            f"{quest_id}/{stage_id}/{objective_id}"
        )
    if objective_id in quest.get("completed_objectives", []):
        raise RuleError(f"Completed objective cannot fail: {objective_id}")
    if objective_id in quest.get("failed_objectives", []):
        raise RuleError(f"Objective already failed: {objective_id}")

    quest["failed_objectives"].append(objective_id)
    quest["updated_at_minutes"] = state.time_minutes

    event = {
        "type": "quest_objective_failed",
        "quest_id": quest_id,
        "stage": stage_id,
        "objective_id": objective_id,
        "turn": state.turn,
        "time_minutes": state.time_minutes,
    }
    quest["history"].append(dict(event))
    state.history.append(dict(event))

    objective = objectives[objective_id]
    outcome = objective.get("on_fail") or stage.get("on_fail")
    if outcome:
        _apply_quest_outcome(state, quest_id, definition, outcome, event)

    _resolve_terminal_stage(state, quest_id, definition)
    return event


def fail_quest(
    state: GameState,
    quest_id: str,
    *,
    reason: str,
) -> Dict[str, Any]:
    quest = _active_quest(state, quest_id)
    quest["status"] = "failed"
    quest["updated_at_minutes"] = state.time_minutes
    event = {
        "type": "quest_failed",
        "quest_id": quest_id,
        "stage": quest["stage"],
        "reason": reason,
        "turn": state.turn,
        "time_minutes": state.time_minutes,
    }
    quest["history"].append(dict(event))
    state.history.append(dict(event))
    return event


def _active_quest(state: GameState, quest_id: str) -> Dict[str, Any]:
    quest = state.quests.get(quest_id)
    if not quest:
        raise RuleError(f"Quest is not active in state: {quest_id}")
    if quest.get("status") != "active":
        raise RuleError(f"Quest is not active: {quest_id}")
    return quest


def _stage_definition(
    quest_id: str,
    stage_id: str,
    definition: Mapping[str, Any],
) -> Mapping[str, Any]:
    stage = definition.get("stages", {}).get(stage_id)
    if not isinstance(stage, Mapping):
        raise RuleError(f"Unknown quest stage: {quest_id}/{stage_id}")
    return stage


def _all_required_objectives_complete(
    quest: Mapping[str, Any],
    stage: Mapping[str, Any],
) -> bool:
    completed = set(quest.get("completed_objectives", []))
    required = {
        objective_id
        for objective_id, objective in stage.get("objectives", {}).items()
        if objective.get("required", True)
    }
    return required.issubset(completed)


def _apply_quest_outcome(
    state: GameState,
    quest_id: str,
    definition: Mapping[str, Any],
    outcome: Mapping[str, Any],
    source_event: Mapping[str, Any],
) -> None:
    quest = state.quests[quest_id]
    previous_stage = quest["stage"]

    next_stage = outcome.get("next_stage")
    status = outcome.get("status")

    if next_stage is not None:
        if next_stage not in definition.get("stages", {}):
            raise RuleError(f"Quest outcome points to unknown stage: {next_stage}")
        quest["stage"] = next_stage
        quest["completed_objectives"] = []
        quest["failed_objectives"] = []

    if status is not None:
        if status not in QUEST_STATUSES:
            raise RuleError(f"Unsupported quest status: {status}")
        quest["status"] = status

    quest["updated_at_minutes"] = state.time_minutes

    transition = {
        "type": "quest_transition",
        "quest_id": quest_id,
        "from_stage": previous_stage,
        "to_stage": quest["stage"],
        "status": quest["status"],
        "source": source_event.get("type", "unknown"),
        "turn": state.turn,
        "time_minutes": state.time_minutes,
    }
    quest["history"].append(dict(transition))
    state.history.append(dict(transition))


def _resolve_terminal_stage(
    state: GameState,
    quest_id: str,
    definition: Mapping[str, Any],
) -> None:
    quest = state.quests[quest_id]
    if quest.get("status") != "active":
        return

    stage = _stage_definition(quest_id, quest["stage"], definition)
    if stage.get("terminal") is not True:
        return

    status = stage.get("terminal_status", "completed")
    if status not in ("completed", "failed"):
        raise RuleError(f"Invalid terminal quest status: {status}")

    quest["status"] = status
    quest["updated_at_minutes"] = state.time_minutes
    event = {
        "type": "quest_terminal",
        "quest_id": quest_id,
        "stage": quest["stage"],
        "status": status,
        "turn": state.turn,
        "time_minutes": state.time_minutes,
    }
    quest["history"].append(dict(event))
    state.history.append(dict(event))
