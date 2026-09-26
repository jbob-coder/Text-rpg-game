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
