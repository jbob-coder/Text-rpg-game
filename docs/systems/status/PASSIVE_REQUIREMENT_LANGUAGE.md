# THE GAME — Passive Requirement Language

Status: **ACTIVE TARGET-GAME AUTHORING STANDARD**

Parent:
- `PASSIVE_REGISTRY_SCHEMA.md`

Purpose: standardize how hidden passive unlock conditions are expressed, combined, validated, and kept secret from the player until qualification.

---

# 1. Principle

Passive unlocks are rule-driven, not arbitrary author fiat at runtime.

A passive requirement packet must be representable as deterministic structured conditions.

Narrative events may satisfy conditions, but the rule still needs a stable internal definition.

---

# 2. Boolean structure

Requirement packets support:

- `all` — every child requirement must pass;
- `any` — one or more child requirements may pass;
- `not` — forbidden state;
- `sequence` — ordered milestones;
- `within` — bounded time window;
- `count` — repeated event threshold.

Nested conditions are allowed but should remain auditable.

---

# 3. Requirement types

Initial target vocabulary:

### Progression
- level_min
- level_max
- attribute_min
- attribute_max
- skill_min
- ability_id
- ability_rarity
- ability_mastery_min
- technique_known
- passive_owned

### Activity
- activity_minutes
- activity_sessions
- intensity_min
- workload_min
- distance
- repetitions
- successful_attempts
- failed_attempts_with_learning

### Combat
- beast_kills
- beast_family_kills
- pk_kills
- encounters_survived
- damage_taken
- damage_avoided
- ally_protections
- nonlethal_resolutions
- weapon_usage
- combat_condition

### Survival / physiology
- near_exhaustion_survivals
- injury_history
- recovery_completed
- environmental_exposure
- sleep_deprivation_event
- starvation_event
- temperature_exposure
- poison/toxin_exposure
- disease_recovery

Dangerous requirement types must be authored carefully and must not make intentional self-destruction the dominant strategy.

### World / narrative
- location_visited
- region_condition
- world_flag
- quest_state
- unique_event
- time_of_day
- date
- historical_event_experienced

### Social / institutional
- relationship_min
- faction_rank
- institutional_rank
- profession_grade
- mentor_relationship
- social_status
- reputation_min

### Knowledge / training
- knowledge_owned
- manual_studied
- mentor_training
- facility_used
- exam_passed
- research_completed

### Equipment / item
- item_owned
- item_used
- equipment_tag
- equipment_mastery
- material_exposure

---

# 4. Accumulation

Accumulating requirements must define:
- what event increments progress;
- unit;
- qualifying threshold;
- reset behavior;
- decay behavior;
- whether interrupted sessions count;
- whether multiple simultaneous sources stack.

Never use vague prose such as “train a lot.”

---

# 5. Intensity

For extreme-experience passives, intensity is separate from duration.

A requirement may need:
- moderate duration;
- high intensity;
- repeated recovery;
- sustained progression over days/weeks;
- survival without catastrophic injury.

One reckless event should not automatically equal months of disciplined adaptation unless explicitly authored.

---

# 6. Hidden progress

Internal progress may be tracked while remaining invisible.

Player-safe Status must not expose:
- percentage toward an unknown passive;
- hidden counters;
- hidden names;
- requirement hints not learned in-world.

A discovered training method may optionally reveal partial guidance without revealing exact thresholds.

---

# 7. Knowledge-gated hints

The world may contain knowledge records that reveal:
- that a passive exists;
- a broad method;
- one prerequisite;
- false rumors;
- incomplete historical cases.

Knowledge does not change the underlying requirement unless the passive explicitly requires that knowledge.

---

# 8. Secret methods

Some institutions/factions may know exact unlock methods and suppress them.

A passive record can therefore distinguish:
- exact internal requirement;
- public theory;
- institutional method;
- player-known method.

This supports espionage, research, mentorship, black markets, classified training, and misinformation.

---

# 9. Risk metadata

Every dangerous requirement should record:
- expected injury probability band;
- lethal-risk possibility;
- recovery burden;
- equipment/facility mitigation;
- mentor mitigation;
- exploit concern.

This metadata supports balance and content authoring; it is not automatically player-visible.

---

# 10. Mutual exclusion

Some passives may be mutually exclusive due to:
- incompatible physiology;
- conflicting adaptations;
- opposing training;
- ability-law conflict;
- one-time event choice.

Mutual exclusion must be explicit via stable IDs.

---

# 11. Sequence example

A passive may require:

1. reach Endurance threshold;
2. complete repeated high-intensity conditioning;
3. survive a qualifying exhaustion event;
4. complete recovery;
5. repeat under higher load.

This is structurally valid, but no thresholds become canon until an actual passive record defines them.

---

# 12. Anti-exploit rules

The requirement system should be designed so that:
- killing trivial targets repeatedly does not unlock every combat adaptation;
- intentionally taking meaningless damage is not optimal;
- repeated zero-risk exercise eventually stops qualifying for high-tier adaptation;
- party members cannot farm each other without consequence unless a specific rule allows it;
- save/reload does not duplicate counted events;
- deterministic IDs prevent the same event from counting twice when not intended.

---

# 13. Validation

Future tooling should reject:
- unknown requirement types;
- negative impossible thresholds;
- impossible `all` combinations;
- direct circular dependencies;
- dangling passive/ability/technique IDs;
- invalid time windows;
- mutually exclusive required states;
- visibility metadata that leaks hidden requirements.

---

# 14. Reconstruction acceptance

A future implementation must be able to evaluate a passive unlock from authoritative state/history without reading narrative prose or guessing designer intent.
