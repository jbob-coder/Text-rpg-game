# THE GAME — Passive Registry Schema

Status: **ACTIVE TARGET-GAME AUTHORING STANDARD**

Purpose: define one stable record format capable of supporting a very large passive catalog without leaking hidden requirements or losing provenance.

## 1. Required identity fields

Every passive record requires:

- `passive_id` — stable machine ID;
- `display_name`;
- `primary_family`;
- `tags[]`;
- `design_status` — proposal / approved / deprecated / etc.;
- `canon_status`;
- `implementation_status`;
- `version`.

IDs are never reused for a different passive.

## 2. Effect definition

Record:
- concise effect;
- full mechanical effect;
- scaling rule;
- stack rule;
- cap rule if any;
- activation mode: always-on / conditional / toggled-by-condition;
- resources affected;
- attributes/skills affected;
- primary ability interactions;
- technique interactions;
- equipment interactions;
- condition/injury interactions;
- world/noncombat effects;
- tactical-combat effects.

## 3. Acquisition definition

Record internal requirements as structured conditions, not prose only.

Possible requirement classes:

- Level;
- attribute threshold;
- skill threshold;
- primary ability identity;
- ability rarity;
- mastery/rank;
- technique use/history;
- activity duration;
- intensity;
- repetition count;
- kill history;
- beast family history;
- PK history if canonically relevant;
- survival event;
- injury;
- recovery;
- environmental exposure;
- location;
- profession;
- class;
- faction/institution;
- mentor;
- equipment;
- item;
- knowledge;
- world flag;
- sequence;
- time window;
- unique event;
- mutual exclusion;
- forbidden state.

## 4. Hidden requirement policy

Internal requirements may exist before the character knows the passive exists.

Player-facing projection before qualification:
- no passive name;
- no icon;
- no locked slot;
- no exact requirement text;
- no progress bar revealing the hidden goal.

After qualification/reveal:
- the Status may reveal the passive;
- known effect is shown;
- acquisition history may be shown if designed;
- future evolutions remain hidden unless separately discovered.

## 5. Requirement progress

Some passives may track hidden progress internally.

Examples:
- accumulated high-intensity training minutes;
- number of near-exhaustion survivals;
- distance traversed under specified load;
- successful defenses under pressure;
- repeated exposure to one environment.

Hidden progress exists for deterministic resolution but is not automatically player-visible.

## 6. Difficulty and danger

A requirement packet must distinguish:
- intended challenge;
- expected risk;
- lethal-risk possibility;
- recovery burden;
- exploit risk.

The system should not encourage meaningless self-damage loops.

If extreme physical stress is required, the game should evaluate:
- legitimate training intensity;
- recovery state;
- adaptation history;
- injury risk;
- trainer/facility quality where relevant;
- repeated safe/unsafe exposure.

## 7. Knowledge fields

Every passive record should support:

- `public_knowledge`;
- `school_knowledge`;
- `government_knowledge`;
- `military_knowledge`;
- `research_knowledge`;
- `faction_knowledge[]`;
- `classified_level`;
- `known_unlock_method`;
- `false_rumors[]`;
- `historical_cases[]`.

This allows a passive to exist while its unlock method is monopolized or suppressed.

## 8. Rarity/significance fields

Do not automatically reuse primary ability rarity.

A passive should separately record:
- prevalence;
- requirement rarity;
- power significance;
- secrecy;
- danger;
- historical uniqueness.

This prevents “rare because powerful” from becoming the only classification model.

## 9. Evolution

A passive may:
- remain static;
- scale;
- gain stages;
- evolve into another passive;
- merge with another passive;
- become mutually exclusive with another path.

Every evolution requires explicit records.

## 10. Example authoring skeleton

```yaml
passive_id: PASSIVE_EXAMPLE
display_name: Example
primary_family: physical_adaptation
tags:
  - endurance
design_status: proposal
canon_status: non_canon_example
implementation_status: not_implemented
effect:
  summary: Example only.
requirements:
  all:
    - type: activity_duration
      activity_tag: high_intensity_conditioning
      minimum_minutes: TBD
visibility:
  before_qualification: hidden
  on_qualification: reveal
knowledge:
  public_knowledge: unknown
```

The example is structural only and is not a canon passive.

## 11. Catalog partitioning

When the catalog grows, split by family and stable ranges, for example:

- `passives/physical/PASSIVE_PHYSICAL_0001-0100.md`
- `passives/sensory/PASSIVE_SENSORY_0001-0100.md`

The exact record-storage format can later become structured JSON/YAML plus human-readable generated indexes if that improves validation.

## 12. Validation requirements

Future tooling should detect:
- duplicate IDs;
- missing families;
- invalid requirement types;
- impossible mutually exclusive requirements;
- dangling evolution links;
- missing knowledge state;
- leaked hidden requirements in player-safe exports;
- broken cross-references;
- deprecated IDs reused incorrectly.

## 13. Reconstruction requirement

Another developer/agent must be able to determine from one passive record:
- what it does;
- how it is earned internally;
- whether the player should know it exists;
- who in the world knows its method;
- what it interacts with;
- whether it is implemented;
- which tests/content/assets it needs.
