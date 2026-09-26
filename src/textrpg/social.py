from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, Iterable, Mapping

from .core import GameState, RuleError


RELATIONSHIP_AXES = ("trust", "respect", "affection", "fear", "suspicion", "debt", "loyalty")
PERSONALITY_AXES = ("empathy", "aggression", "caution", "ambition", "honesty", "loyalty", "curiosity", "discipline")


def ensure_npc(state: GameState, npc_id: str) -> Dict[str, Any]:
    npc = state.npcs.setdefault(npc_id, {})
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
    if importance < 1 or importance > 5:
        raise RuleError("Memory importance must be in range 1..5")
    npc = ensure_npc(state, npc_id)
    record = {
        "memory_id": memory_id,
        "importance": importance,
        "turn": state.turn,
        "time_minutes": state.time_minutes,
        "tags": list(tags),
        "data": dict(data or {}),
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
    if confidence < 0 or confidence > 1:
        raise RuleError("Knowledge confidence must be in range 0..1")
    if secrecy < 0 or secrecy > 5:
        raise RuleError("Knowledge secrecy must be in range 0..5")
    npc = ensure_npc(state, npc_id)
    record = {
        "source": source,
        "confidence": confidence,
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
    speaker_state = ensure_npc(state, speaker)
    if knowledge_id not in speaker_state["knowledge"]:
        raise RuleError(f"{speaker} does not know {knowledge_id}")
    source = speaker_state["knowledge"][knowledge_id]
    copied = deepcopy(source)
    copied["source"] = speaker
    copied["turn_learned"] = state.turn
    ensure_npc(state, recipient)["knowledge"][knowledge_id] = copied
    add_memory(
        state,
        recipient,
        f"MEM_HEARD_{knowledge_id}_FROM_{speaker}",
        importance=max(1, int(source.get("secrecy", 0))),
        tags=("knowledge_transfer", "voluntary" if voluntary else "leak"),
        data={"knowledge_id": knowledge_id, "speaker": speaker},
    )
    return copied


def eligible_leak_targets(
    state: GameState,
    *,
    holder: str,
    knowledge_id: str,
    network: Mapping[str, Iterable[str]],
) -> list[str]:
    """Return deterministic candidates for an authored gossip/leak step.

    This function does not randomly leak information. It exposes which connected
    characters qualify so content can choose when a propagation event occurs.
    """
    npc = ensure_npc(state, holder)
    record = npc["knowledge"].get(knowledge_id)
    if not record:
        return []
    secrecy = int(record.get("secrecy", 0))
    personality = npc.get("personality", {})
    discipline = float(personality.get("discipline", 50))
    honesty = float(personality.get("honesty", 50))
    pressure = (100 - discipline) + max(0.0, honesty - 70.0) - secrecy * 12
    if pressure < 35:
        return []
    targets = []
    for target in network.get(holder, []):
        if target == holder:
            continue
        target_knows = ensure_npc(state, target)["knowledge"]
        if knowledge_id not in target_knows:
            targets.append(target)
    return sorted(set(targets))


def adjust_relationship(
    state: GameState,
    npc_id: str,
    changes: Mapping[str, float],
    *,
    source: str = "unknown",
) -> Dict[str, Any]:
    """Apply bounded changes to independent relationship axes.

    Relationship axes remain separate. This function deliberately does not collapse
    trust, fear, affection, suspicion, or the other dimensions into one friendship score.
    """
    ensure_npc(state, npc_id)
    relationship = state.relationships[npc_id]
    before: Dict[str, float] = {}
    after: Dict[str, float] = {}

    for axis, delta_raw in changes.items():
        if axis not in RELATIONSHIP_AXES:
            raise RuleError(f"Unknown relationship axis: {axis}")
        if not isinstance(delta_raw, (int, float)):
            raise RuleError(f"Relationship change must be numeric: {axis}")
        before[axis] = float(relationship.get(axis, 0))
        value = before[axis] + float(delta_raw)
        relationship[axis] = max(-100.0, min(100.0, value))
        after[axis] = relationship[axis]

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

    for axis, minimum in (minimums or {}).items():
        if axis not in RELATIONSHIP_AXES:
            raise RuleError(f"Unknown relationship axis: {axis}")
        if float(relationship.get(axis, 0)) < float(minimum):
            return False

    for axis, maximum in (maximums or {}).items():
        if axis not in RELATIONSHIP_AXES:
            raise RuleError(f"Unknown relationship axis: {axis}")
        if float(relationship.get(axis, 0)) > float(maximum):
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
    if priority < 0 or priority > 100:
        raise RuleError("Goal priority must be in range 0..100")
    if progress < 0 or progress > 100:
        raise RuleError("Goal progress must be in range 0..100")
    if status not in GOAL_STATUSES:
        raise RuleError(f"Unsupported goal status: {status}")

    npc = ensure_npc(state, npc_id)
    goals = npc["goals"]
    if goal_id in goals:
        raise RuleError(f"Goal already exists for {npc_id}: {goal_id}")

    record = {
        "goal_id": goal_id,
        "priority": int(priority),
        "progress": float(progress),
        "status": status,
        "source": source,
        "created_turn": state.turn,
        "created_at_minutes": state.time_minutes,
        "updated_at_minutes": state.time_minutes,
        "data": dict(data or {}),
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
    if completion_threshold <= 0 or completion_threshold > 100:
        raise RuleError("Goal completion threshold must be in range (0, 100]")
    npc = ensure_npc(state, npc_id)
    goal = npc["goals"].get(goal_id)
    if not goal:
        raise RuleError(f"Unknown goal for {npc_id}: {goal_id}")
    if goal.get("status") in {"completed", "failed"}:
        raise RuleError(f"Cannot progress closed goal: {goal_id}")
    if not isinstance(delta, (int, float)):
        raise RuleError("Goal progress delta must be numeric")

    before = float(goal.get("progress", 0))
    after = max(0.0, min(100.0, before + float(delta)))
    goal["progress"] = after
    if after >= completion_threshold:
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
    """Move one authored NPC story track through an explicit guarded transition."""
    if not isinstance(to_state, str) or not to_state:
        raise RuleError("Story state must be a non-empty string")

    npc = ensure_npc(state, npc_id)
    story_state = npc["story_state"]
    previous = story_state.get(track_id)

    if allowed_from is not None:
        allowed = tuple(allowed_from)
        if previous not in allowed:
            raise RuleError(
                f"Invalid story-state transition for {npc_id}/{track_id}: "
                f"{previous!r} -> {to_state!r}"
            )

    story_state[track_id] = to_state
    event = {
        "type": "npc_story_transition",
        "npc_id": npc_id,
        "track_id": track_id,
        "from_state": previous,
        "to_state": to_state,
        "reason": reason,
        "data": dict(data or {}),
        "turn": state.turn,
        "time_minutes": state.time_minutes,
    }
    state.history.append(event)
    return event
