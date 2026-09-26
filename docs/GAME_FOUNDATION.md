# Text RPG Game — Foundation v0.1

## Product goal

Build an authored, choice-driven RPG that feels like a living pen-and-paper campaign without requiring generative AI at runtime. The player reads scenes, talks to characters, acts alone or with a group, trains, fights, investigates, equips gear, develops powers, and changes the world through persistent decisions.

The core requirement is **stateful consequence**: choices should not merely move to the next paragraph. They must alter durable game state that later scenes can inspect.

## Design pillars

1. **Authored, not improvised.** Story, rules, outcomes, visuals, and character behavior are designed and versioned. Runtime AI is not required.
2. **Persistent consequence.** Dialogue, secrets, relationships, injuries, training, faction standing, items, knowledge, and previous choices can affect later scenes.
3. **Multiple valid solutions.** Social, technical, stealth, combat, knowledge, equipment, powers, and group composition can solve the same problem differently.
4. **Progress must be earned.** New capability comes from training, repeated use, study, mentors, equipment, discoveries, quests, and meaningful thresholds—not a single arbitrary button.
5. **Characters are stateful actors.** NPCs have memory, private knowledge, relationships, motivations, personality axes, and their own story state.
6. **Information is gameplay.** Knowing a fact can unlock choices. Revealing a fact can change who knows it, who trusts the player, and what later scenes occur.
7. **Deterministic rules.** The same save state plus the same seed and action must resolve identically. This makes saves, testing, replay analysis, and balancing reliable.
8. **Pixel-art presentation.** The rules layer is independent from the presentation layer so portraits, scene illustrations, UI animation, and later engine choices do not corrupt game state.

## Runtime state model

`GameState` is the authority for a playthrough. Recommended top-level state:

- `seed`: deterministic run seed.
- `scene_id`: current authored scene.
- `turn`: action counter used by deterministic checks.
- `time_minutes`: world time spent since run start.
- `player`: attributes, skills, resources, powers, perks, conditions, appearance, and progression.
- `flags`: durable decisions and world facts.
- `relationships`: per-NPC multidimensional relationship state.
- `knowledge`: facts the player has learned, including source/confidence/privacy.
- `inventory`: items and quantities.
- `quests`: active/completed/failed quest stages.
- `history`: append-only record of important choices and resolutions.

Do not encode important continuity only in prose. If future content needs to react to it, it needs a stable ID in state.

## Player statistics

Use layers instead of one giant power number.

### Core attributes

Suggested 0–100 scale:

- `might`: raw physical force.
- `agility`: movement speed, coordination, reaction.
- `endurance`: fatigue tolerance and physical resilience.
- `intellect`: reasoning, analysis, technical learning.
- `will`: mental resistance, discipline, pain tolerance.
- `perception`: noticing physical details, danger, tells, hidden objects.
- `presence`: social force, confidence, leadership, intimidation potential.

Attributes should move slowly. A normal conversation should not grant +5 Might.

### Skills

Skills are narrower and can advance faster than attributes. Example families:

- Combat: unarmed, blades, ranged, defense, tactics.
- Physical: athletics, stealth, traversal, survival.
- Technical: engineering, systems, medicine, crafting.
- Social: persuasion, deception, intimidation, empathy, leadership.
- Knowledge: history, factions, powers, creatures, investigation.

A check may combine one attribute and one skill. Example: `intellect + technical_systems * 0.6`.

### Resources

Resources are spent and recovered rather than permanently increased by each use:

- health
- stamina
- focus
- resolve
- power-specific energy pools

A power can use more than one resource. This supports tactical identity without forcing every power into the same mana system.

### Derived combat values

Derived values should be calculated from attributes, skills, equipment, conditions, and active effects:

- max health
- max stamina
- initiative
- accuracy
- evasion
- guard
- carry capacity
- movement/travel efficiency

Do not permanently store values that can be safely recalculated unless save compatibility requires it.

## Power and ability model

A power is not just a button. It is a structured progression object.

Recommended fields:

- stable `ability_id`
- family/category
- current rank
- mastery XP
- discovered techniques
- active techniques
- passive traits
- resource costs
- cooldown/recovery rules
- physical/mental prerequisites
- incompatibilities
- drawbacks
- evolution conditions
- hidden properties that become known through play

### Technique progression

A technique should normally pass through stages such as:

1. Unknown
2. Discovered
3. Unstable
4. Learned
5. Practiced
6. Mastered
7. Specialized or evolved

Advancement can require combinations of use count, quality of use, training time, instruction, stat thresholds, special events, and resources.

### Ability checks

Do not use only rank-versus-rank comparisons. A weaker power used intelligently may defeat a stronger one depending on distance, environment, information, equipment, fatigue, counters, and surprise.

## Perks and traits

Perks can originate from multiple systems:

- training
- background
- title/reputation
- injury/scar
- equipment
- power evolution
- relationships
- faction membership
- discoveries

Every perk should record its source. This prevents accidental duplication and makes removal/replacement rules reliable.

## Equipment

Equipment can modify both numbers and behavior.

An item may contain:

- slot
- quality/grade
- base modifiers
- requirements
- active ability
- passive perk
- set tags
- condition/durability if the final design uses durability
- attunement/mastery
- hidden property
- provenance/history

Crafted equipment can vary by material, crafter skill, recipe knowledge, process quality, and rare conditions. The same recipe does not have to create identical equipment.

## Choice resolution

Each choice has four separate questions:

1. Is it visible?
2. Is it enabled?
3. Does it require a check?
4. What persistent effects occur?

This distinction is essential. A player may see a locked option and understand what they are missing, while a secret option should not appear at all until the relevant information is known.

### Degree of success

Checks should support multiple result bands:

- critical success
- success
- failure
- critical failure

Different bands can alter relationships, consume different resources, reveal information, create injuries, or send the story to different scenes.

The current prototype uses deterministic seeded variance. Randomness is reproducible from save state.

## NPC model

Every important NPC should have a stable ID and four layers of state.

### Identity

Name, role, age range, faction, visual spec, voice/writing rules, biography, and immutable anchors.

### Personality

Use bounded numeric axes rather than one label. Example axes:

- empathy
- aggression
- caution
- ambition
- honesty
- loyalty
- curiosity
- discipline

These may drift slowly after major events. A character can become more suspicious or more compassionate without becoming a different person overnight.

### Relationship to player

Track independent axes:

- trust
- respect
- affection
- fear
- suspicion
- debt
- loyalty

A person can respect the player while distrusting them. One generic `friendship = 75` value cannot express that.

### Memory and private knowledge

NPC memory should record significant events, not every line of dialogue. Knowledge records should distinguish:

- what the player knows
- what an NPC knows
- what an NPC believes incorrectly
- what is secret
- who revealed it
- whether the information was verified

This enables hidden conversations, lies, leaks, blackmail, misunderstandings, and delayed consequences without runtime AI.

## Conversation system

Dialogue is authored as nodes with conditions and effects. A dialogue option can depend on:

- player stat/skill
- relationship axis
- prior line or decision
- known fact
- equipped item
- injury/status
- party member present
- faction reputation
- time/date
- quest stage

Group scenes can support interruptions and different speakers. The engine should know which characters are present. Private lines must never be exposed merely because the scene file contains them.

## Solo and group play modes

“Solo” and “group” describe story context, not separate games.

- Solo scenes emphasize direct player agency and private information.
- Group scenes include party composition, group resources, competing goals, interjections, and information exposure.
- The same quest may enter either scene family depending on previous choices.

Party members should not become puppets. They can refuse, leave, argue, volunteer, hide information, or act based on their own state.

## Knowledge graph and secret propagation

Information should be modeled as data because it can change the story as strongly as combat.

A knowledge record can include:

- `knowledge_id`
- topic/category
- source
- confidence
- truth state: unknown / true / false / mixed
- secrecy level
- who currently knows it
- who believes it
- evidence links
- leak consequences

Future system: propagation events can spread information through factions or relationships according to authored rules. This must be deterministic and inspectable, not AI-generated gossip.

## Progression pace

Progression uses three speeds:

- Fast: familiarity, short-term resource recovery, minor skill XP.
- Medium: skill ranks, technique mastery, relationship shifts, gear improvement.
- Slow: core attributes, major power ranks, personality changes, faction status, permanent transformations.

This prevents the player from becoming fundamentally different after one dialogue click while still making each session feel productive.

## Visual integration

The rules engine never decides what art should look like. It emits state and presentation tags, for example:

- `portrait_emotion = guarded`
- `scene_variant = archive_alarm`
- `animation = skill_unlock_minor`
- `equipment_visual_tag = plated_left_arm`

The UI/art layer resolves those tags to approved pixel assets.

## Save and compatibility rules

- All IDs are stable and never reused for a different meaning.
- Save files include a schema version.
- Migrations must be explicit.
- Story text may change without renaming stable IDs.
- Important state changes are append-logged for debugging.
- A save must never depend on chat memory.

## Prototype implemented in this branch

`src/textrpg/core.py` implements:

- authoritative serializable `GameState`
- scene lookup
- visible-vs-locked choice filtering
- conditional checks for stats, relationships, knowledge, and items
- deterministic seeded checks
- four degrees of success
- persistent effects for flags, player values, relationships, knowledge, inventory, and quest stages
- durable history entries

`content/sample_scene.json` is intentionally generic and non-canon. It demonstrates a private conversation, a skill check, and a knowledge-gated item solution without fixing the final story setting.

## Next engineering slice

1. Define canonical player stat ranges and derived-stat formulas.
2. Add NPC state records and NPC knowledge ownership.
3. Add ability mastery, training time, prerequisites, costs, and evolution rules.
4. Add equipment modifiers and perk-source tracking.
5. Add quest graph validation.
6. Add a save/load serializer with schema migrations.
7. Add a tiny presentation client after the target runtime is confirmed.
