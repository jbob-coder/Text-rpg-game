# Game Direction and Status-Screen Reference

Purpose: preserve the user's intended game experience and the status-screen concept discussed in chat so future workstreams do not reduce the project to isolated mechanics.

## Product identity

[DIRECTION] This project is a **life-and-decisions text RPG**. The central experience is not rapid stat acquisition or a sequence of disconnected encounters. The player should feel that they are living through a persistent world where decisions, relationships, knowledge, injuries, training, equipment, powers, quests, and earlier conversations continue to matter later.

[DIRECTION] The game should feel alive because state persists and other systems react to that state.

[DIRECTION] Slow progression and real consequences are global design direction, not optional features.

[DIRECTION] Avoid trivial or instantaneous permanent gains. Important growth should normally require time, repeated use, training, study, mentors, risk, discoveries, meaningful thresholds, or consequences.

[DIRECTION] The player should be able to solve situations in multiple valid ways: physical, social, technical, stealth, knowledge, equipment, power use, or group composition.

[DIRECTION] Important continuity must be represented by durable state/stable IDs whenever future content needs to react to it. It must not exist only in prose or chat memory.

## Player-state architecture

[DIRECTION] The character sheet should be layered rather than represented by one overall power number.

Target conceptual hierarchy:

`core attributes -> resources -> derived statistics -> skills -> abilities -> mastery -> techniques -> evolution`

[DESIGNED] Character level, ability level, skill/mastery progression, techniques, and evolution should remain separable concepts so two characters at the same overall progression point can still be mechanically different.

[DESIGNED] Permanent core attributes should generally progress more slowly than narrower skills/masteries.

[DESIGNED] Resources are spend/recover values and should not be treated as ordinary point-buy attributes.

## Core-stat schema status

[CONFLICTING] Two candidate schemas currently exist.

### Existing repository schema

[IMPLEMENTED] The current repository uses seven slow-moving core attributes:

- `might` — raw physical force
- `agility` — movement, coordination, reaction
- `endurance` — fatigue tolerance and physical resilience
- `intellect` — reasoning and technical learning
- `will` — mental resistance and discipline
- `perception` — awareness, danger recognition, tells
- `presence` — social force and leadership pressure

### Expanded chat proposal

[DESIGNED] This chat proposed an eight-attribute split:

- `STR` / Strength — raw physical force, lifting, pushing, striking, grappling
- `CON` / Constitution — bodily robustness, health, injury resistance, poison/bleeding tolerance
- `AGI` / Agility — movement speed, balance, evasive movement, body control
- `DEX` / Dexterity — precision, fine coordination, weapon handling, parry/manipulation
- `PER` / Perception — detection, initiative support, hidden threats, weak points
- `INT` / Intellect — analysis, learning, technical understanding
- `WIL` / Willpower — mental resistance, concentration, ability control
- `PRE` / Presence — persuasion, intimidation, leadership, social pressure

[QUESTION] The unresolved architectural decision is whether `agility` should remain broad enough to include precision/coordination, or whether `dexterity` deserves its own core attribute.

Do not silently change executable stats until that design is resolved.

## Resources

[DESIGNED] Universal resources discussed for the player sheet:

- Health / HP
- Stamina
- Focus
- Resolve
- power-specific energy pools when appropriate
- XP/progression tracking where the final progression architecture requires it

[DIRECTION] Powers do not all need to share one universal mana pool. A power may have its own capacity, regeneration, cost structure, or other restrictions.

## Derived statistics

[DESIGNED] Derived values should come from core attributes, skills, equipment, conditions, perks, techniques, and situational effects rather than being separately leveled whenever recalculation is safe.

Candidate derived values discussed:

- physical power/damage support
- physical defense/resistance
- accuracy
- evasion
- movement/travel efficiency
- initiative
- parry/guard
- mental resistance
- ability power
- ability control
- critical performance where appropriate
- carry capacity
- maximum Health, Stamina, Focus, and Resolve

[PROVISIONAL] Exact formulas are balancing values and must not be treated as final canon until the playable loop gives evidence.

## Skills and mastery

[DIRECTION] Skills are narrower than core attributes and may improve faster through actual use, training, instruction, practice, and relevant events.

[DESIGNED] Mastery should represent quality/experience with a specific ability, weapon family, technique, or discipline rather than merely duplicating character level.

Possible progression lanes include:

- core attributes
- skills
- ability level/rank
- mastery XP
- technique unlock/practice/mastery
- evolution progress

The goal is to prevent one level-up event from making the character better at everything simultaneously.

## Ability model

[DESIGNED] A power/ability is a structured progression object, not merely a damage button.

Candidate fields include:

- stable ability ID
- name/family/category
- rank/level
- mastery XP
- resource pool/cost
- control
- efficiency
- range
- power/effect strength
- cooldown/recovery
- requirements
- drawbacks/failure conditions
- discovered techniques
- passive traits
- evolution conditions
- hidden properties that can be discovered through play

[DIRECTION] Higher mastery should be able to improve control, efficiency, reliability, options, or technique access rather than only inflating damage.

## Choice and consequence model

[DIRECTION] Choices should not merely advance to the next paragraph. Meaningful choices should be able to alter durable state that later scenes inspect.

Relevant persistent consequences include:

- relationships
- private/public knowledge
- NPC memory
- injuries/conditions
- inventory/equipment
- faction standing
- quests and story state
- personality drift after important events
- power progression
- secrets and information propagation
- time spent and opportunities missed

[DIRECTION] A consequence does not have to be immediately visible. Some effects can emerge much later as long as they are represented in state and can be traced.

## Living-world expectation

[DIRECTION] Important NPCs should behave as stateful actors rather than static dialogue menus.

They may have:

- stable identity
- personality axes
- multidimensional relationship values
- memories
- private knowledge
- goals
- story state
- faction/party connections

[DIRECTION] Player knowledge and NPC knowledge are not automatically identical. Information itself is gameplay.

[DIRECTION] Secret propagation should remain deterministic/inspectable and authored rather than random generative gossip.

## Time, training, injury, and recovery

[DIRECTION] Time is a meaningful game resource.

Training should consume time and usually resources. Recovery should consume time. Injuries/conditions can persist, worsen, improve, expire, or require treatment. This supports slow progression and makes choices about preparation, rest, risk, and urgency meaningful.

[DIRECTION] A permanent attribute should not jump because of one trivial conversation or one short action.

## Status-screen / character-sheet target

[DIRECTION] The player should have a readable status screen that exposes the important state without turning every moment into a spreadsheet. Deep information should be expandable; the immediate screen should prioritize information relevant to current decisions.

[DESIGNED] The status-screen concept shown in this chat should preserve these sections:

1. **Identity / progression**
   - Name
   - overall level/progression indicator if retained
   - EXP/progress if retained
   - origin/species/background where relevant
   - path/archetype if the final design uses one
   - current overall condition

2. **Core attributes**
   - whichever canonical attribute schema is ultimately selected
   - available attribute points only if that progression currency remains part of the final design

3. **Resources**
   - HP / Health
   - Stamina
   - Focus
   - Resolve
   - power-specific resource when relevant

4. **Derived/combat values**
   - only values meaningful enough to justify UI exposure
   - examples: physical power, accuracy, evasion, initiative, resistance/guard

5. **Ability panel**
   - ability name
   - rank/level
   - mastery
   - resource/cost state
   - control/efficiency where useful
   - known techniques
   - undiscovered/locked information represented without leaking hidden content

6. **Masteries / skills**
   - weapon, movement, observation, social, technical, or other relevant disciplines

7. **Status effects / injuries / conditions**
   - active effects that materially matter to the player

[DESIGNED] Hidden properties may be represented as `???`, locked entries, or undiscovered sections when revealing the exact information would undermine discovery gameplay.

### Reference layout discussed

```text
STATUS

NAME        <character>
LEVEL       <if retained>
EXP         <if retained>
ORIGIN      <background/species/origin>
PATH        <if retained>
CONDITION   <current condition>

ATTRIBUTES
<canonical core attributes>

RESOURCES
HP
STAMINA
FOCUS
RESOLVE
<power-specific pool when relevant>

DERIVED / COMBAT
Physical Power
Accuracy
Evasion
Initiative
Resistance / Guard

ABILITY
<ability name>
Rank / Level
Mastery
Energy / Cost State
Control
Efficiency
Techniques
Locked/Unknown discoveries

MASTERY / SKILLS
<relevant disciplines>

STATUS EFFECTS
<conditions/injuries/buffs/debuffs>
```

[PROVISIONAL] This is a structural UI reference, not a commitment to final typography, exact field names, formulas, or screen density.

## Presentation rule

[DIRECTION] The game should present enough numbers to support informed decisions while keeping narrative readability. Systems may be deep internally without forcing the player to inspect every variable at all times.

## Reference-material rule

[DIRECTION] Reference novels/material may be used to study progression logic, status screens, resource separation, abilities, and pacing. The game itself must remain original and must not copy protected story text, character names, plot, UI wording, or other expressive content.

## What this file does NOT claim

- It does not claim the eight-stat model is implemented.
- It does not resolve seven attributes versus eight attributes.
- It does not claim the example status screen already exists in a client UI.
- It does not make provisional formulas final canon.
- It does not replace source/tests when discussing implementation state.
