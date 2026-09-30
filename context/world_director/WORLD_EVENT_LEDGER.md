# World Event Ledger

Status: ACTIVE_APPEND_ONLY_LEDGER
Created: 2026-09-29

Purpose: record state-changing events in the living campaign so future sessions can reconstruct causality without relying on chat history.

## Event record schema

Each event should include:

- EVENT_ID
- CANON_STATE
- WORLD_TIME
- LOCAL_TIME_CONTEXT
- ACTORS
- LOCATION
- CAUSE
- ACTION
- IMMEDIATE_EFFECT
- OFFSCREEN_PROPAGATION
- PLAYER_VISIBLE
- JACK_KNOWS
- NPC_KNOWLEDGE_CHANGES
- STATE_CHANGES
- CLOCKS_ADVANCED
- OPEN_CONSEQUENCES
- SOURCE_FILE_OR_SESSION
- SUPERSEDES (optional)

## Ledger

### DIRECTOR_BOOTSTRAP_2026_09_29

- EVENT_ID: EVENT_DIRECTOR_BOOTSTRAP_2026_09_29
- CANON_STATE: CONFIRMED_CANON
- WORLD_TIME: documentation-only; live gameplay clock unchanged
- ACTORS: repository continuity system
- CAUSE: user authorized the assistant to operate from an omniscient world-director perspective and to preserve broader world state for continuation.
- ACTION: created the persistent World Director memory layer.
- IMMEDIATE_EFFECT: future sessions have a defined boot sequence, live-state file, Academy protection rule, and append-only event ledger.
- PLAYER_VISIBLE: meta only; not an in-world event.
- JACK_KNOWS: not applicable.
- STATE_CHANGES: narrative-governance files added.
- CLOCKS_ADVANCED: none.
- OPEN_CONSEQUENCES: recover exact last live Academy scene before advancing local time.
- SOURCE_FILE_OR_SESSION: user direction dated 2026-09-29.

## Rule

Do not add fictional events retroactively merely to make the world appear busy. If an event was not previously established, either:
- introduce it prospectively through simulation; or
- mark it DRAFT_CANON and state that it is a newly authored historical/current fact.

Never falsify prior player knowledge or choices.
