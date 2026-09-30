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

### LIVE_CHECKPOINT_RECOVERY_2026_09_29

- EVENT_ID: EVENT_LIVE_CHECKPOINT_RECOVERY_2026_09_29
- CANON_STATE: CONFIRMED_CANON
- WORLD_TIME: Day -15, 08:19:46
- LOCAL_TIME_CONTEXT: restarted early military-academy timeline
- ACTORS: Elias Voss; Visitor Services clerk; repository continuity system
- LOCATION: Visitor Services counter, public/civilian side of secured military-academy complex
- CAUSE: World Director bootstrap required exact recovery of the last authoritative gameplay checkpoint before narration could resume.
- ACTION: latest authoritative Google Drive checkpoint and Elias persistent brain were re-read and synchronized into repository live-world state.
- IMMEDIATE_EFFECT: the previous UNKNOWN local scene in LIVE_WORLD_STATE is replaced by the recovered exact checkpoint.
- OFFSCREEN_PROPAGATION: none; this is a continuity recovery operation, not a new in-world event.
- PLAYER_VISIBLE: meta only; no new story action occurred.
- JACK_KNOWS: unchanged.
- NPC_KNOWLEDGE_CHANGES: none.
- STATE_CHANGES: LIVE_WORLD_STATE now records Elias at Day -15 08:19:46, current Visitor Services conversation, EVOLVE observations, and unresolved Adrian Voss recognition.
- CLOCKS_ADVANCED: none.
- OPEN_CONSEQUENCES: clerk's connection to Adrian Voss remains unresolved; Elias may continue probing naturally. Jack state remains UNKNOWN and user-controlled.
- SOURCE_FILE_OR_SESSION: Google Drive 12_GAMEPLAY_BRANCH/GAMEPLAY_CHECKPOINT_CURRENT.md latest markdown copy plus ELIAS_PERSISTENT_BRAIN.md.
- SUPERSEDES: only the placeholder UNKNOWN live-scene fields created during World Director bootstrap; it does not supersede historical gameplay records.

### ADRIAN_VOSS_RECORD_CLARIFICATION_0001

- EVENT_ID: EVENT_ADRIAN_VOSS_RECORD_CLARIFICATION_0001
- CANON_STATE: SIMULATION_CREATED_CONSEQUENCE
- WORLD_TIME: Day -15, 08:19:46–08:21:20
- LOCAL_TIME_CONTEXT: Visitor Services conversation before Academy intake
- ACTORS: Elias Voss; unnamed Visitor Services clerk
- LOCATION: Visitor Services counter, public/civilian side of secured military-academy complex
- CAUSE: Elias had a legitimate unresolved question after the clerk recognized Adrian Voss's surname.
- ACTION: Elias calmly asked how she knew of his father. The clerk explained that she had not known Adrian personally; she remembered his name from supply-routing records and a closed discrepancy review in which Adrian was the person who flagged the discrepancy.
- IMMEDIATE_EFFECT: Elias gains bounded new knowledge about the source of the clerk's recognition and reduces immediate suspicion toward her.
- OFFSCREEN_PROPAGATION: none established.
- PLAYER_VISIBLE: Elias's side of the exchange is narratively visible when resumed.
- JACK_KNOWS: no; Jack has not been present and gains no knowledge from this event.
- NPC_KNOWLEDGE_CHANGES: clerk knows Elias is Adrian Voss's son; no other new NPC knowledge established.
- STATE_CHANGES: Elias now has a new unresolved thread concerning Adrian's discrepancy review.
- CLOCKS_ADVANCED: LIVE_GAMEPLAY_CLOCK +1 minute 34 seconds; ACADEMY_CLOCK synchronized.
- OPEN_CONSEQUENCES: nature of the discrepancy; identity of any reviewed party; reason for closure; surviving records; present-day relevance.
- SOURCE_FILE_OR_SESSION: active narrated campaign, user authorization to continue under World Director mode.

## Rule

Do not add fictional events retroactively merely to make the world appear busy. If an event was not previously established, either:
- introduce it prospectively through simulation; or
- mark it DRAFT_CANON and state that it is a newly authored historical/current fact.

Never falsify prior player knowledge or choices.
