from __future__ import annotations

from copy import deepcopy
from math import isfinite
from typing import Any, Dict, Iterable, Mapping, MutableMapping

from .core import GameState, RuleError


RELATIONSHIP_AXES = ("trust", "respect", "affection", "fear", "suspicion", "debt", "loyalty")
PERSONALITY_AXES = ("empathy", "aggression", "caution", "ambition", "honesty", "loyalty", "curiosity", "discipline")


def _finite_number(value: Any, label: str) -> float:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not isfinite(float(value))
    ):
        raise RuleError(f"{label} must be a finite number")
    return float(value)


def ensure_npc(state: GameState, npc_id: str) -> Dict[str, Any]:
    """Return/create one NPC shell without accepting corrupt nested containers."""
    if not isinstance(npc_id, str) or not npc_id:
        raise RuleError("NPC ID must be a non-empty string")
    if not isinstance(state.npcs, MutableMapping):
        raise RuleError("state.npcs must be mutable")
    if not isinstance(state.relationships, MutableMapping):
        raise RuleError("state.relationships must be mutable")

    existing = state.npcs.get(npc_id)
    if existing is None:
        npc: Dict[str, Any] = {
            "personality": {},
            "knowledge": {},
            "memories": [],
            "goals": {},
            "story_state": {},
        }
        create_npc = True
    else:
        if not isinstance(existing, MutableMapping):
            raise RuleError(f"NPC state must be mutable: {npc_id}")
        npc = existing
        create_npc = False
        expected = {
            "personality": Mapping,
            "knowledge": MutableMapping,
            "memories": list,
            "goals": MutableMapping,
            "story_state": MutableMapping,
        }
        for field_name, expected_type in expected.items():
            if field_name in npc and not isinstance(npc[field_name], expected_type):
                raise RuleError(
                    f"NPC {field_name} has invalid type: {npc_id}"
                )

    existing_relationship = state.relationships.get(npc_id)
    if existing_relationship is not None and not isinstance(
        existing_relationship,
        MutableMapping,
    ):
        raise RuleError(f"Relationship state must be mutable: {npc_id}")

    # Commit only after all existing state has passed structural preflight.
    if create_npc:
        state.npcs[npc_id] = npc
    npc.setdefault("personality", {})
    npc.setdefault("knowledge", {})
    npc.setdefault("memories", [])
    npc.setdefault("goals", {})
    npc.setdefault("story_state", {})
    state.relationships.setdefault(npc_id, {})
    return npc


def add_memory(
    state: GameState,
    npc_id: str,
    memory_id: str,
    *,
    importance: int = 1,
    tags: Iterable[str] = (),
    data: Mapping[str, Any] | None = None,
) -> Dict[str, Any]:
    if not isinstance(memory_id, str) or not memory_id:
        raise RuleError("Memory ID must be a non-empty string")
    if isinstance(importance, bool) or not isinstance(importance, int):
        raise RuleError("Memory importance must be an integer")
    if importance < 1 or importance > 5:
        raise RuleError("Memory importance must be in range 1..5")
    if isinstance(tags, (str, bytes)) or not isinstance(tags, Iterable):
        raise RuleError("Memory tags must be an iterable of non-empty strings")
    tag_values = list(tags)
    if not all(isinstance(tag, str) and tag for tag in tag_values):
        raise RuleError("Memory tags must contain only non-empty strings")
    if data is not None and not isinstance(data, Mapping):
        raise RuleError("Memory data must be an object")
    payload = dict(data or {})

    npc = ensure_npc(state, npc_id)
    record = {
        "memory_id": memory_id,
        "importance": importance,
        "turn": state.turn,
        "time_minutes": state.time_minutes,
        "tags": tag_values,
        "data": payload,
    }
    npc["memories"].append(record)
    return record


def npc_learn(
    state: GameState,
    npc_id: str,
    knowledge_id: str,
    *,
    source: str,
    confidence: float = 1.0,
    truth: str = "unknown",
    secrecy: int = 0,
) -> Dict[str, Any]:
    if not isinstance(knowledge_id, str) or not knowledge_id:
        raise RuleError("Knowledge ID must be a non-empty string")
    if not isinstance(source, str) or not source:
        raise RuleError("Knowledge source must be a non-empty string")
    if not isinstance(truth, str) or not truth:
        raise RuleError("Knowledge truth must be a non-empty string")
    confidence_value = _finite_number(confidence, "Knowledge confidence")
    if confidence_value < 0 or confidence_value > 1:
        raise RuleError("Knowledge confidence must be in range 0..1")
    if isinstance(secrecy, bool) or not isinstance(secrecy, int):
        raise RuleError("Knowledge secrecy must be an integer")
    if secrecy < 0 or secrecy > 5:
        raise RuleError("Knowledge secrecy must be in range 0..5")

    npc = ensure_npc(state, npc_id)
    record = {
        "source": source,
        "confidence": confidence_value,
        "truth": truth,
        "secrecy": secrecy,
        "turn_learned": state.turn,
    }
    npc["knowledge"][knowledge_id] = record
    return record


def share_knowledge(
    state: GameState,
    *,
    speaker: str,
    recipient: str,
    knowledge_id: str,
    voluntary: bool = True,
) -> Dict[str, Any]:
    """Transfer knowledge only after both source and recipient state preflight."""
    speaker_state = state.npcs.get(speaker)
    if speaker_state is None:
        raise RuleError(f"{speaker} does not know {knowledge_id}")
    if not isinstance(speaker_state, Mapping):
        raise RuleError(f"NPC state must be an object: {speaker}")

    speaker_knowledge = speaker_state.get("knowledge", {})
    if not isinstance(speaker_knowledge, Mapping):
        raise RuleError(f"NPC knowledge must be an object: {speaker}")
    if knowledge_id not in speaker_knowledge:
        raise RuleError(f"{speaker} does not know {knowledge_id}")

    source = speaker_knowledge[knowledge_id]
    if not isinstance(source, Mapping):
        raise RuleError(
            f"NPC knowledge record must be an object: {speaker}/{knowledge_id}"
        )
    try:
        importance = max(1, int(source.get("secrecy", 0)))
    except (TypeError, ValueError) as exc:
        raise RuleError(
            f"Knowledge secrecy must be integer-like: {speaker}/{knowledge_id}"
        ) from exc
    if importance > 5:
        raise RuleError("Memory importance must be in range 1..5")

    existing_recipient = state.npcs.get(recipient)
    if existing_recipient is not None:
        if not isinstance(existing_recipient, MutableMapping):
            raise RuleError(f"NPC state must be mutable: {recipient}")
        recipient_knowledge = existing_recipient.get("knowledge", {})
        recipient_memories = existing_recipient.get("memories", [])
        if not isinstance(recipient_knowledge, MutableMapping):
            raise RuleError(f"NPC knowledge must be mutable: {recipient}")
        if not isinstance(recipient_memories, list):
            raise RuleError(f"NPC memories must be a list: {recipient}")

    copied = deepcopy(dict(source))
    copied["source"] = speaker
    copied["turn_learned"] = state.turn
    memory = {
        "memory_id": f"MEM_HEARD_{knowledge_id}_FROM_{speaker}",
        "importance": importance,
        "turn": state.turn,
        "time_minutes": state.time_minutes,
        "tags": ["knowledge_transfer", "voluntary" if voluntary else "leak"],
        "data": {"knowledge_id": knowledge_id, "speaker": speaker},
    }

    # All failure-prone validation is complete before recipient state mutation.
    recipient_state = ensure_npc(state, recipient)
    recipient_state["knowledge"][knowledge_id] = copied
    recipient_state["memories"].append(memory)
    return copied


def eligible_leak_targets(
    state: GameState,
    *,
    holder: str,
    knowledge_id: str,
    network: Mapping[str, Iterable[str]],
) -> list[str]:
    """Return deterministic candidates without mutating NPC state.

    Eligibility is a query. Merely asking who could receive a leak must not create
    NPC shells, relationship entries, knowledge containers, or other durable state.
    """
    npc = state.npcs.get(holder)
    if npc is None:
        return []
    if not isinstance(npc, Mapping):
        raise RuleError(f"NPC state must be an object: {holder}")

    knowledge = npc.get("knowledge", {})
    if not isinstance(knowledge, Mapping):
        raise RuleError(f"NPC knowledge must be an object: {holder}")
    record = knowledge.get(knowledge_id)
    if not record:
        return []
    if not isinstance(record, Mapping):
        raise RuleError(
            f"NPC knowledge record must be an object: {holder}/{knowledge_id}"
        )

    secrecy = int(record.get("secrecy", 0))
    personality = npc.get("personality", {})
    if not isinstance(personality, Mapping):
        raise RuleError(f"NPC personality must be an object: {holder}")
    discipline = float(personality.get("discipline", 50))
    honesty = float(personality.get("honesty", 50))
    pressure = (100 - discipline) + max(0.0, honesty - 70.0) - secrecy * 12
    if pressure < 35:
        return []

    targets = []
    for target in network.get(holder, []):
        if target == holder:
            continue
        target_state = state.npcs.get(target)
        if target_state is None:
            target_knowledge: Mapping[str, Any] = {}
        else:
            if not isinstance(target_state, Mapping):
                raise RuleError(f"NPC state must be an object: {target}")
            target_knowledge = target_state.get("knowledge", {})
            if not isinstance(target_knowledge, Mapping):
                raise RuleError(f"NPC knowledge must be an object: {target}")
        if knowledge_id not in target_knowledge:
            targets.append(target)
    return sorted(set(targets))


def execute_leak_event(
    state: GameState,
    *,
    holder: str,
    knowledge_id: str,
    network: Mapping[str, Iterable[str]],
    recipients: Iterable[str] | None = None,
    max_recipients: int = 1,
    event_id: str = "LEAK_EVENT",
) -> Dict[str, Any]:
    """Execute an authored deterministic information-propagation event.

    Candidate eligibility still comes from authored network/personality/secrecy rules.
    When recipients are not explicitly authored, the sorted eligible list is used so
    the same state always produces the same recipients.
    """
    if isinstance(max_recipients, bool) or not isinstance(max_recipients, int) or max_recipients < 1:
        raise RuleError("Leak event max_recipients must be an integer >= 1")
    if not isinstance(state.history, list):
        raise RuleError("state.history must be a list")

    candidates = eligible_leak_targets(
        state,
        holder=holder,
        knowledge_id=knowledge_id,
        network=network,
    )

    if recipients is None:
        selected = candidates[:max_recipients]
    else:
        selected = sorted(set(recipients))
        if len(selected) > max_recipients:
            raise RuleError(
                f"Leak event selected {len(selected)} recipients but max is {max_recipients}"
            )
        invalid = [recipient for recipient in selected if recipient not in candidates]
        if invalid:
            raise RuleError(
                "Leak event recipient is not currently eligible: " + ", ".join(invalid)
            )

    npcs_before = deepcopy(state.npcs)
    relationships_before = deepcopy(state.relationships)
    history_before = deepcopy(state.history)
    try:
        for recipient in selected:
            share_knowledge(
                state,
                speaker=holder,
                recipient=recipient,
                knowledge_id=knowledge_id,
                voluntary=False,
            )

        event = {
            "type": "knowledge_leak",
            "event_id": event_id,
            "holder": holder,
            "knowledge_id": knowledge_id,
            "candidates": list(candidates),
            "recipients": list(selected),
            "turn": state.turn,
            "time_minutes": state.time_minutes,
        }
        state.history.append(event)
        return event
    except Exception:
        state.npcs = npcs_before
        state.relationships = relationships_before
        state.history = history_before
        raise


def adjust_relationship(
    state: GameState,
    npc_id: str,
    changes: Mapping[str, float],
    *,
    source: str = "unknown",
) -> Dict[str, Any]:
    """Apply bounded independent-axis changes as one atomic relationship update."""
    if not isinstance(changes, Mapping):
        raise RuleError("Relationship changes must be an object")
    if not isinstance(state.history, list):
        raise RuleError("state.history must be a list")

    existing = state.relationships.get(npc_id, {})
    if not isinstance(existing, Mapping):
        raise RuleError(f"Relationship state must be an object: {npc_id}")

    before: Dict[str, float] = {}
    after: Dict[str, float] = {}
    for axis, delta_raw in changes.items():
        if axis not in RELATIONSHIP_AXES:
            raise RuleError(f"Unknown relationship axis: {axis}")
        delta = _finite_number(delta_raw, f"Relationship change {axis}")
        current = _finite_number(
            existing.get(axis, 0),
            f"Relationship state {npc_id}/{axis}",
        )
        before[axis] = current
        value = current + delta
        after[axis] = max(-100.0, min(100.0, value))

    # All axes validate before durable state is created or modified.
    ensure_npc(state, npc_id)
    relationship = state.relationships[npc_id]
    relationship.update(after)

    event = {
        "type": "relationship_change",
        "npc_id": npc_id,
        "source": source,
        "before": before,
        "after": after,
        "turn": state.turn,
        "time_minutes": state.time_minutes,
    }
    state.history.append(event)
    return event


def relationship_meets(
    state: GameState,
    npc_id: str,
    *,
    minimums: Mapping[str, float] | None = None,
    maximums: Mapping[str, float] | None = None,
) -> bool:
    """Evaluate authored multidimensional relationship gates without flattening axes."""
    relationship = state.relationships.get(npc_id, {})
    if not isinstance(relationship, Mapping):
        raise RuleError(f"Relationship state must be an object: {npc_id}")
    if minimums is not None and not isinstance(minimums, Mapping):
        raise RuleError("Relationship minimums must be an object")
    if maximums is not None and not isinstance(maximums, Mapping):
        raise RuleError("Relationship maximums must be an object")

    for axis, minimum in (minimums or {}).items():
        if axis not in RELATIONSHIP_AXES:
            raise RuleError(f"Unknown relationship axis: {axis}")
        actual = _finite_number(
            relationship.get(axis, 0),
            f"Relationship state {npc_id}/{axis}",
        )
        minimum_value = _finite_number(
            minimum,
            f"Relationship minimum {axis}",
        )
        if actual < minimum_value:
            return False

    for axis, maximum in (maximums or {}).items():
        if axis not in RELATIONSHIP_AXES:
            raise RuleError(f"Unknown relationship axis: {axis}")
        actual = _finite_number(
            relationship.get(axis, 0),
            f"Relationship state {npc_id}/{axis}",
        )
        maximum_value = _finite_number(
            maximum,
            f"Relationship maximum {axis}",
        )
        if actual > maximum_value:
            return False

    return True


GOAL_STATUSES = ("active", "paused", "completed", "failed")


def set_goal(
    state: GameState,
    npc_id: str,
    goal_id: str,
    *,
    priority: int = 50,
    progress: float = 0.0,
    status: str = "active",
    source: str = "unknown",
    data: Mapping[str, Any] | None = None,
) -> Dict[str, Any]:
    """Create an explicit NPC goal record.

    Existing goal IDs cannot be silently replaced; callers must update the existing
    record through a dedicated transition/progress operation instead.
    """
    if not isinstance(goal_id, str) or not goal_id:
        raise RuleError("Goal ID must be a non-empty string")
    if isinstance(priority, bool) or not isinstance(priority, int):
        raise RuleError("Goal priority must be an integer")
    if priority < 0 or priority > 100:
        raise RuleError("Goal priority must be in range 0..100")
    progress_value = _finite_number(progress, "Goal progress")
    if progress_value < 0 or progress_value > 100:
        raise RuleError("Goal progress must be in range 0..100")
    if status not in GOAL_STATUSES:
        raise RuleError(f"Unsupported goal status: {status}")
    if not isinstance(source, str) or not source:
        raise RuleError("Goal source must be a non-empty string")
    if data is not None and not isinstance(data, Mapping):
        raise RuleError("Goal data must be an object")
    payload = dict(data or {})

    if not isinstance(state.history, list):
        raise RuleError("state.history must be a list")
    existing_npc = state.npcs.get(npc_id)
    if existing_npc is not None:
        if not isinstance(existing_npc, Mapping):
            raise RuleError(f"NPC state must be an object: {npc_id}")
        existing_goals = existing_npc.get("goals", {})
        if not isinstance(existing_goals, Mapping):
            raise RuleError(f"NPC goals must be an object: {npc_id}")
        if goal_id in existing_goals:
            raise RuleError(f"Goal already exists for {npc_id}: {goal_id}")

    npc = ensure_npc(state, npc_id)
    goals = npc["goals"]

    record = {
        "goal_id": goal_id,
        "priority": int(priority),
        "progress": progress_value,
        "status": status,
        "source": source,
        "created_turn": state.turn,
        "created_at_minutes": state.time_minutes,
        "updated_at_minutes": state.time_minutes,
        "data": payload,
    }
    goals[goal_id] = record
    state.history.append(
        {
            "type": "npc_goal_created",
            "npc_id": npc_id,
            "goal_id": goal_id,
            "status": status,
            "priority": int(priority),
            "turn": state.turn,
            "time_minutes": state.time_minutes,
        }
    )
    return record


def update_goal_progress(
    state: GameState,
    npc_id: str,
    goal_id: str,
    delta: float,
    *,
    completion_threshold: float = 100.0,
) -> Dict[str, Any]:
    threshold = _finite_number(
        completion_threshold,
        "Goal completion threshold",
    )
    if threshold <= 0 or threshold > 100:
        raise RuleError("Goal completion threshold must be in range (0, 100]")
    delta_value = _finite_number(delta, "Goal progress delta")
    if not isinstance(state.history, list):
        raise RuleError("state.history must be a list")

    npc = state.npcs.get(npc_id)
    if not isinstance(npc, Mapping):
        raise RuleError(f"Unknown goal for {npc_id}: {goal_id}")
    goals = npc.get("goals", {})
    if not isinstance(goals, Mapping):
        raise RuleError(f"NPC goals must be an object: {npc_id}")
    goal = goals.get(goal_id)
    if not isinstance(goal, MutableMapping):
        raise RuleError(f"Unknown goal for {npc_id}: {goal_id}")
    if goal.get("status") in {"completed", "failed"}:
        raise RuleError(f"Cannot progress closed goal: {goal_id}")

    before = _finite_number(
        goal.get("progress", 0),
        f"Goal progress state {npc_id}/{goal_id}",
    )
    after = max(0.0, min(100.0, before + delta_value))
    goal["progress"] = after
    if after >= threshold:
        goal["status"] = "completed"
    goal["updated_at_minutes"] = state.time_minutes

    event = {
        "type": "npc_goal_progress",
        "npc_id": npc_id,
        "goal_id": goal_id,
        "before": before,
        "after": after,
        "status": goal["status"],
        "turn": state.turn,
        "time_minutes": state.time_minutes,
    }
    state.history.append(event)
    return event


def transition_story_state(
    state: GameState,
    npc_id: str,
    track_id: str,
    to_state: str,
    *,
    allowed_from: Iterable[str | None] | None = None,
    reason: str = "unknown",
    data: Mapping[str, Any] | None = None,
) -> Dict[str, Any]:
    """Move one authored NPC story track through a preflighted transition."""
    if not isinstance(track_id, str) or not track_id:
        raise RuleError("Story track ID must be a non-empty string")
    if not isinstance(to_state, str) or not to_state:
        raise RuleError("Story state must be a non-empty string")
    if not isinstance(reason, str) or not reason:
        raise RuleError("Story transition reason must be a non-empty string")
    if data is not None and not isinstance(data, Mapping):
        raise RuleError("Story transition data must be an object")
    payload = dict(data or {})
    if allowed_from is not None:
        if isinstance(allowed_from, (str, bytes)) or not isinstance(allowed_from, Iterable):
            raise RuleError("allowed_from must be an iterable of states")
        allowed = tuple(allowed_from)
        if not all(value is None or (isinstance(value, str) and value) for value in allowed):
            raise RuleError("allowed_from entries must be non-empty strings or null")
    else:
        allowed = None
    if not isinstance(state.history, list):
        raise RuleError("state.history must be a list")

    existing_npc = state.npcs.get(npc_id)
    if existing_npc is None:
        previous = None
    else:
        if not isinstance(existing_npc, Mapping):
            raise RuleError(f"NPC state must be an object: {npc_id}")
        existing_story = existing_npc.get("story_state", {})
        if not isinstance(existing_story, Mapping):
            raise RuleError(f"NPC story_state must be an object: {npc_id}")
        previous = existing_story.get(track_id)

    if allowed is not None:
        if previous not in allowed:
            raise RuleError(
                f"Invalid story-state transition for {npc_id}/{track_id}: "
                f"{previous!r} -> {to_state!r}"
            )

    # Successful transition may create the NPC shell, but failed preflight cannot.
    npc = ensure_npc(state, npc_id)
    story_state = npc["story_state"]
    story_state[track_id] = to_state
    event = {
        "type": "npc_story_transition",
        "npc_id": npc_id,
        "track_id": track_id,
        "from_state": previous,
        "to_state": to_state,
        "reason": reason,
        "data": payload,
        "turn": state.turn,
        "time_minutes": state.time_minutes,
    }
    state.history.append(event)
    return event
