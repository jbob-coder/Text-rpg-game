# THE GAME — NPC Memory Event Standard

Status: **APPROVED FIRST-PASS V05 CONTRACT / CURRENT PRIMITIVE PARTIAL**
Parent:
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
Current source:
- src/textrpg/social.py

## 1. Purpose

Define persistent NPC memory so later behavior can be traced to actual events instead of arbitrary state mutation.

Memory means this NPC remembers an event or experience. It is distinct from knowledge, which describes what the NPC believes is true.

## 2. Current reality

Current add_memory stores:
- memory_id;
- importance 1..5;
- turn;
- time_minutes;
- tags;
- data.

This is a usable primitive but lacks normalized event provenance, participants, location, confidence, visibility, emotional impact, and lifecycle policy.

The target contract extends it without invalidating current saves.

## 3. Memory identity

Recommended:
- memory_id identifies the remembered event for this NPC;
- event_id references authoritative world/history event when available;
- owner NPC is implied by its container.

Two NPCs may remember the same event differently while sharing event_id.

## 4. Target memory record

Fields:
- memory_id;
- event_id;
- occurred_turn/time;
- recorded_turn/time;
- location_id;
- participants;
- source/perception mode;
- importance 1..5;
- confidence 0..1;
- truth relation when known;
- emotional tags;
- relationship impact/reference;
- knowledge references;
- public/private classification;
- persistence class;
- decay/reinforcement state;
- data payload;
- provenance.

## 5. Source/perception modes

Suggested:
- witnessed;
- heard_from;
- inferred;
- read_record;
- told_by_player;
- combat_encounter;
- institutional_report;
- rumor.

Source does not guarantee truth.

## 6. Importance

Keep current 1..5:
1 minor;
2 meaningful;
3 important;
4 major;
5 defining/critical.

Importance may affect retrieval but does not automatically mutate relationships.

## 7. Persistence classes

Target:
- TRANSIENT;
- NORMAL;
- DURABLE;
- PERMANENT_STORY.

Phase 1 may treat current story memories as durable unless explicitly temporary.

Never silently delete a memory required by quest/rival/social causality.

## 8. Memory and knowledge

Example:
- Event: Jack hides the relay destination.
- Memory: Tamsin remembers Jack leaving without explaining.
- Knowledge: Tamsin still may not know Gate Twelve.
- Relationship: suspicion may rise.

These are separate writes.

## 9. Memory and relationship

One social event may create memory, relationship delta, and story-state transition.

The memory does not continuously recalculate relationship unless another rule defines that.

## 10. Retrieval

Decision systems query memories by tags, participant, event/location, importance, recency, goal, or knowledge.

Retrieval is read-only.

Checking whether an NPC remembers something must not create state.

## 11. Decay

Phase 1 does not require memory decay.

Future decay must never delete PERMANENT_STORY causality or run nondeterministically.

Reduced behavioral weighting is safer than destructive deletion.

## 12. Reinforcement

Repeated related events may update recurrence/salience or create linked memories.

Do not overwrite major history with a generic latest record.

## 13. Combat integration

After tactical encounters, deliberate memories may record:
- fought together;
- player abandoned/assisted NPC;
- adversary escaped;
- observed technique;
- injury caused;
- surrender/spare decision.

Raw combat logs are not copied wholesale.

## 14. Player-facing memory

NPC memory is private by default.

The player may learn it through dialogue, behavior, abilities, journal, or later social UI if justified.

## 15. Atomicity

Memory creation accompanying relationship/knowledge/story-state changes should be one validated transaction when they describe the same authored event.

## 16. Tests

Required:
- importance validation;
- duplicate-event policy deterministic;
- read-only retrieval no mutation;
- private memory not projected;
- permanent memory not decayed;
- combat aftermath creates only deliberate memories;
- save/load;
- transaction rollback.

## 17. Phase 1

Tamsin's opening path should eventually gain at least one explicit memory so a later scene can react to a remembered event rather than only a relationship number.
