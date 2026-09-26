# Status Screen Data Contract

Status: [DESIGNED] detailed player-facing contract. This document does **not** claim that a client UI is implemented.

Purpose: define exactly what the status/character screen is allowed to display, where every value comes from, what can remain hidden, and how future UI code must interact with the rules layer.

## 1. Core principle

The status screen is a **projection of authoritative game state**, not another rules engine.

The UI must never:

- recalculate combat formulas independently
- duplicate modifier stacking rules
- decide equipment-set thresholds itself
- infer hidden ability properties
- mutate permanent stats merely because an effective value is displayed
- assume player knowledge equals world truth
- turn undiscovered data into visible spoilers

The UI requests authoritative values/explanations from the rules layer and renders them.

## 2. Information layers

Every status-screen field belongs to one of these disclosure levels.

### VISIBLE

The player is entitled to the exact value now.

Examples:
- current Health
- known core attributes
- equipped items
- known skills
- currently known conditions

### EXPLAINABLE

The exact final value is visible and the player may inspect why it has that value.

Examples:
- Strength 12 base -> +2 equipment -> -1 injury -> 13 effective
- Evasion 17.4 -> formula inputs + set bonus

### DISCOVERED

A system exists, but details appear only after the character/player has discovered them.

Examples:
- ability rank
- known techniques
- identified condition
- known evolution requirement

### PARTIALLY_KNOWN

The player knows something exists but not its exact magnitude or mechanism.

Example:
- "Unknown interference affecting ability control"
- "Potential evolution condition: ???"

### HIDDEN

The UI must not reveal the field, identifier, threshold, or exact value.

Examples:
- undiscovered ability evolution branches
- NPC private knowledge
- hidden quest flags
- future event triggers
- exact secret propagation conditions

## 3. Primary status screen

The first screen should be readable in seconds.

Recommended order:

1. Identity
2. Current condition / urgent state
3. Core attributes
4. Current resources
5. Selected derived values
6. Active ability summary
7. Active conditions
8. Navigation to deeper sheets

Do not display every skill, formula term, inventory item, relationship axis, or hidden property simultaneously.

## 4. Identity block

Candidate fields:

- Name
- stable character identity internally
- current overall progression indicator if the final design retains one
- origin/background
- current path/archetype if used
- age/date/time where life-simulation context makes it important
- current broad condition

Authoritative sources:
- persistent character/player state
- world-time state
- progression subsystem

[QUESTION] Overall character Level/EXP remains an open design decision. The UI contract must not require it until that decision is resolved.

## 5. Core attribute block

Canonical source:
- permanent/base attribute state
- effective value explanation from the rules engine

The primary display should normally show the **effective current value**, while inspection reveals permanent base plus temporary/conditional contributions.

Example presentation concept:

```text
STRENGTH        13
Base            12
Field Harness   +2
Injured Arm     -1
```

Rules contract:
- UI asks the rules layer for the value/explanation.
- UI does not add equipment/perk/condition values itself.
- base value remains separately identifiable.
- temporary modifiers do not overwrite permanent progression.

Current implementation-review API:
- `RulesEngine.explain_player_value(state, "attributes.<id>")`

[CONFLICTING] Final canonical attribute IDs remain subject to DEC-STAT-001. The screen should bind to registry metadata rather than hard-code the current seven-stat list.

## 6. Resource block

Initial universal resources:

- Health
- Stamina
- Focus
- Resolve

Possible power-specific resources appear only when relevant/discovered.

Each resource display needs:

- current value
- current maximum
- optional regeneration/recovery indicator when player-facing
- critical warning state
- source of maximum on deeper inspection

Example:

```text
HEALTH    78 / 92
STAMINA   41 / 85
FOCUS     57 / 64
RESOLVE   70 / 70
```

The current resource is persistent mutable state.

The maximum is rules-derived state.

Changing equipment/conditions may change the maximum without permanently changing the underlying core attribute.

If a maximum drops below the current resource, the authoritative resource normalization rule determines the current value. UI must not invent its own clamping behavior.

## 7. Derived/combat block

Only expose derived values that meaningfully support player decisions.

Current candidate values:
- Max Health
- Max Stamina
- Max Focus
- Max Resolve
- Initiative
- Accuracy
- Evasion
- Guard
- Carry Capacity

Future derived stats must justify permanent UI space.

Current review/evolution rules support:
- centralized derived formulas
- direct `derived.*` modifiers
- source provenance
- domain floors
- full derived breakdown

Rules contract:
- `RulesEngine.explain_player_value(state, "derived.<id>")`
- UI may render formula explanation from returned structured data.
- UI must not reproduce formula coefficients as hard-coded client logic.

Example deep inspection:

```text
EVASION  8.5

Agility       10.0 x 0.65 = 6.50
Perception     0.0 x 0.20 = 0.00
Athletics      0.0 x 0.15 = 0.00
Scout Set                     +2.00
-----------------------------------
Final                          8.50
```

[PROVISIONAL] Exact coefficients remain balance data.

## 8. Skills and mastery

Core distinction:

- attribute = broad slow-moving capability
- skill = learned specialization
- mastery = quality/experience with a specific ability/weapon/discipline
- technique = discrete learned application

The status screen should not flatten these into one number.

Recommended navigation:

```text
SKILLS
  Combat
  Physical
  Technical
  Social
  Knowledge

MASTERY
  Abilities
  Weapons
  Disciplines
```

Each skill can show:
- current value
- effective modifiers
- category
- training progress where supported
- relevant mentor/training effects if known

Mastery can show:
- mastery XP/progress
- mastery stage
- techniques unlocked
- next visible threshold only if the player is allowed to know it

## 9. Ability panel

An ability is its own progression object.

Candidate visible fields:
- name
- stable internal ID hidden from ordinary player presentation
- rank/level
- mastery stage/progress
- current power resource
- cost
- control
- efficiency
- range if known
- cooldown/recovery if applicable
- known techniques
- known drawbacks
- known evolution progress

Possible underlying fields:
- rank
- mastery_xp
- mastery_stage
- techniques
- energy/resource pool
- control
- efficiency
- cooldown state
- prerequisites
- discovered properties
- hidden properties/evolution branches

Disclosure is critical.

A hidden evolution requirement should never appear because the data object contains it.

The ability UI requires a dedicated **player-visible projection** in the future rather than directly dumping the raw ability dictionary.

## 10. Conditions / injuries / status effects

Primary screen should show only active effects materially affecting current play.

Each player-visible condition may include:
- display name
- severity if known
- time remaining if knowable
- affected systems
- treatment/recovery clue if discovered

Rules data may also contain:
- stable condition ID
- source
- tags
- modifiers
- application time

Deep inspection may use modifier provenance to show exact numerical effects when the game design permits exact numbers.

A condition can exist mechanically without revealing every internal modifier.

## 11. Equipment interaction

The status UI should make these distinctions clear:

- base/permanent value
- equipment contribution
- set contribution
- perk contribution
- condition contribution
- final effective value

Equipment requirement eligibility is a separate rule.

Current design/implementation direction:
- equipment qualification uses permanent/base attributes and skills
- an equipped bonus does not qualify another item
- this avoids circular equipment dependencies and equip-order exploits

The UI should therefore label requirement comparison against **base** values when showing why an item can/cannot be equipped.

## 12. Perks

Perks may represent:
- training adaptations
- story-earned traits
- equipment-derived passives when modeled persistently
- background traits
- milestone rewards

Player-visible perk page can show:
- known perk name
- description
- known effects
- provenance/source when useful

Exact numeric modifiers may be expandable.

Hidden internal perks used for story state should not automatically enter this page merely because they exist in data.

## 13. Progression feedback

Progression should feel earned and slow.

The status UI should distinguish:

- permanent attribute gain
- temporary effective increase
- skill improvement
- mastery progress
- technique unlock
- ability rank change
- evolution/breakthrough event

These are not interchangeable.

Example:

```text
+0.18 Technical Systems
Training session completed.

NOT:
+1 Intellect
```

unless a genuine long-term attribute-training rule awarded that permanent change.

## 14. Time-sensitive state

Because this is a life-and-decisions RPG, the status layer may expose:

- current in-world time/date
- recovery time
- condition duration
- cooldowns
- training commitments
- deadlines

Only values known to the player should be shown precisely.

An uncertain deadline can be represented as narrative uncertainty rather than a hidden exact timestamp.

## 15. Relationships

Do not put every relationship axis on the primary status screen.

Possible deeper relationship sheet:
- known relationship summary
- player-observable tendencies
- important memories the player reasonably knows about
- faction/reputation context

Internal NPC relationship values may include:
- trust
- respect
- affection
- fear
- suspicion
- debt
- loyalty

These internal values are not automatically exact player-visible numbers.

[DESIGNED] The UI needs a player-visible relationship projection rather than direct access to all NPC relationship internals.

## 16. Knowledge and secrets

Player knowledge is a first-class state system.

Possible knowledge screen:
- discovered facts
- confidence/certainty when relevant
- source
- contradictions
- unresolved clues

Never expose:
- another NPC's private knowledge store
- objective truth flags the player has not established
- future leak candidates
- hidden authoring metadata

## 17. Debug/developer view

A developer mode may expose much more than the player UI.

Developer-only inspection can show:
- stable IDs
- raw base state
- modifier paths
- provenance keys
- formula coefficients
- hidden flags
- rule checks
- save schema version
- history/event entries

This view must be clearly separate from normal player presentation.

The new explainability pipeline is particularly useful here.

## 18. Update/event model

The UI should eventually subscribe/react to authoritative state-change events instead of polling and recalculating everything blindly.

Useful invalidation categories:

- PLAYER_BASE_STATS_CHANGED
- EFFECTIVE_MODIFIERS_CHANGED
- RESOURCES_CHANGED
- EQUIPMENT_CHANGED
- CONDITION_CHANGED
- PERK_CHANGED
- SKILL_CHANGED
- ABILITY_CHANGED
- TIME_ADVANCED
- KNOWLEDGE_CHANGED
- RELATIONSHIP_CHANGED

[DESIGNED] These are architecture categories, not implemented event names.

## 19. Caching rule

UI may cache a rendered projection for performance, but cache invalidation must be driven by state revision/event identity.

The rules layer remains authoritative.

Never persist a cached effective/derived number as if it were a new permanent stat.

## 20. Save compatibility

Status UI should not depend on the exact raw save shape.

Preferred future boundary:

```text
GameState
  -> Rules / Projection Service
     -> StatusScreenViewModel
        -> Client UI
```

This allows:
- save migrations
- stat-schema migrations
- formula balancing
- UI redesign
- alternate clients

without requiring every presentation layer to understand raw persistence internals.

## 21. Seven-to-eight stat migration compatibility

If DEC-STAT-001 resolves to the eight-stat model, the status UI should not require a redesign.

It should read the canonical attribute registry and render groups/order metadata.

Candidate grouping:

Physical:
- Strength
- Constitution
- Agility
- Dexterity

Mental/Awareness:
- Perception
- Intellect
- Willpower

Social:
- Presence

The view contract should therefore be registry-driven rather than seven hard-coded rows.

## 22. Acceptance checklist for future UI implementation

A status UI implementation is not complete unless:

1. every displayed number has an authoritative source
2. base and effective values cannot be confused
3. derived formulas are not duplicated in UI code
4. temporary modifiers never overwrite permanent stats
5. hidden content is filtered through player-visibility rules
6. resource maxima and current values stay consistent
7. equipment requirement UI uses the correct base-value contract
8. ability hidden/evolution data is not leaked
9. condition visibility respects discovery
10. player vs NPC knowledge is not conflated
11. the screen remains readable without showing every internal field
12. developer/debug detail is separable from player presentation
13. schema migration does not require rewriting formulas in the client

Related:
- `GAME_DIRECTION_AND_UI.md`
- `STAT_SCHEMA_EVALUATION.md`
- `DEC-UI-001`
- `DEC-MOD-001`
- `DEC-MOD-003`
