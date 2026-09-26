# Core Stat Schema Evaluation — Seven vs Eight Attributes

Status: [DESIGNED] evaluation / recommendation candidate. This document does **not** change executable stats.

Purpose: stress-test the current seven-stat foundation against the expanded eight-stat proposal before the project creates enough content that changing stat identity becomes expensive.

## 1. Design constraints

Any canonical stat schema must support all of the following without one attribute becoming an obvious universal answer:

- physical combat
- ranged combat
- stealth
- traversal
- precision/fine manipulation
- technical work and crafting
- medicine
- investigation
- social interaction
- mental resistance
- power/ability control
- injury/recovery
- training and long-term life simulation
- equipment requirements
- deterministic checks
- readable status UI
- future progression/evolution systems

[DIRECTION] Core attributes are slow-moving long-horizon properties. Skills/mastery progress faster. Resources are spend/recover values and are not core attributes.

## 2. Current seven-stat foundation

Current implemented IDs:

- `might`
- `agility`
- `endurance`
- `intellect`
- `will`
- `perception`
- `presence`

### Strengths

- compact UI
- easier initial balancing
- fewer migration concerns
- each stat already has code/tests/formulas
- adequate for a simpler narrative RPG

### Weaknesses

The main pressure points are physical-role overload.

`agility` currently owns movement, coordination, and reaction. That makes one attribute relevant to sprinting, dodging, balance, weapon precision, fine manipulation, and potentially crafting/tool use unless those responsibilities are pushed entirely into skills.

`endurance` currently combines fatigue tolerance and bodily resilience. That is workable, but terminology can blur the distinction between the permanent attribute and the spendable Stamina resource.

`might` is mechanically clear but uses a less conventional player-facing term than Strength.

## 3. Expanded eight-stat candidate

Recommended candidate IDs and responsibilities:

| ID | Player-facing name | Owns | Must not own |
| --- | --- | --- | --- |
| `strength` | Strength | raw force, lifting, pushing, grappling force, heavy impact | health, precision, movement speed |
| `constitution` | Constitution | bodily robustness, injury tolerance, poison/bleed resistance, long-duration physical resilience | spendable Stamina, raw damage |
| `agility` | Agility | body movement, balance, evasive motion, acceleration, gross motor reaction | weapon precision/fine manipulation |
| `dexterity` | Dexterity | precision, hand-eye coordination, fine manipulation, weapon/tool handling | sprint speed, bodily toughness |
| `perception` | Perception | detection, sensory awareness, tells, danger recognition, target acquisition | learned investigation knowledge |
| `intellect` | Intellect | reasoning, learning, analysis, technical understanding | mental endurance/control |
| `will` | Willpower | discipline, concentration, mental resistance, pain tolerance, ability control support | social authority |
| `presence` | Presence | social force, confidence, leadership pressure, intimidation/persuasion support | empathy knowledge or deception skill itself |

## 4. Why Dexterity is the key decision

The seven-stat model works only if `agility` is allowed to cover both whole-body movement and fine precision.

That creates four problems:

1. A fast/evasive character automatically trends toward being a precise weapon/tool user.
2. Ranged combat can become overly dependent on Agility + Perception, making one physical stat disproportionately valuable.
3. Technical/medical actions that require fine hands have no clean physical attribute.
4. Equipment requirements for precise weapons cannot distinguish coordination from movement speed.

A separate Dexterity stat resolves those ownership conflicts.

The cost is one additional player-facing number and a future migration from the current foundation.

## 5. Scenario stress test

The preferred rule pattern is generally:

`effective core attribute + relevant skill + situational modifiers`

A task chooses the attribute that represents the *kind of capability being tested*, while the skill represents learned competence.

| Scenario | Primary core attribute | Skill / secondary system | Why |
| --- | --- | --- | --- |
| force a jammed door | Strength | athletics / context | raw force |
| hold a collapsing object | Strength or Constitution by fiction | athletics | force vs sustained bodily stress |
| sprint across a street | Agility | athletics | movement execution |
| climb for ten minutes | Constitution or Agility by obstacle | traversal | endurance vs body control |
| dodge a visible strike | Agility | defense | evasive body movement |
| thread a shot through cover | Dexterity | ranged | weapon precision |
| notice an ambush | Perception | investigation/survival | awareness |
| pick a delicate mechanism | Dexterity | technical_systems | fine manipulation |
| repair unfamiliar machinery | Intellect | engineering | understanding/design reasoning |
| perform delicate surgery | Dexterity or Intellect by phase | medicine | execution vs diagnosis/planning |
| resist poison | Constitution | condition/resistance rules | bodily resilience |
| resist mental coercion | Willpower | relevant perk/ability defense | mental resistance |
| maintain a difficult power | Willpower | ability mastery | control/concentration |
| analyze an unknown power | Intellect | powers | comprehension |
| detect a lie | Perception | empathy/investigation | tells + learned reading |
| persuade a neutral NPC | Presence | persuasion | social force + technique |
| intimidate through reputation | Presence | intimidation + reputation | social pressure, not raw Strength by default |
| sneak across open ground | Agility | stealth | body movement/noise control |
| palm a small object unnoticed | Dexterity | stealth | fine manipulation |
| survive prolonged deprivation | Constitution | survival | physical resilience + learned practice |

Important rule: avoid automatically adding multiple core attributes to every check. That recreates stat inflation and makes the sheet harder to understand. Multi-attribute formulas should be reserved for derived values or deliberately complex systems.

## 6. Resource separation

Resources remain separate regardless of seven vs eight attributes:

- Health — current physical condition/damage capacity
- Stamina — spendable physical exertion
- Focus — spendable concentration/cognitive effort
- Resolve — spendable/pressure-facing mental-social endurance where the final design needs it
- power-specific pools — ability-family-specific capacity when appropriate

A core attribute can influence a resource maximum or recovery rate without becoming that resource.

Example architecture:

`Constitution -> contributes to Max Health / Max Stamina`

but

`Constitution != Stamina`

This distinction is important for injuries, exhaustion, recovery, temporary conditions, and equipment.

## 7. Skills remain the specialization layer

The eight-stat proposal does not replace skills.

Examples:

- high Dexterity with no ranged skill = naturally coordinated but untrained shooter
- high Intellect with low engineering = smart but not an engineer
- high Presence with low persuasion = forceful personality without refined persuasion technique
- high Agility with low stealth = fast/mobile but not automatically quiet
- high Constitution with low survival = physically hardy but not knowledgeable about wilderness survival

This preserves build identity and keeps core stats from determining every outcome directly.

## 8. Ability/power progression remains separate

[DIRECTION] Powers are not another core attribute.

Ability state can independently track:

- stable ability ID
- rank/level
- mastery XP/stage
- control
- efficiency
- power/effect strength
- range
- resource pool/cost
- cooldown/recovery
- techniques
- prerequisites
- drawbacks
- evolution/breakthrough conditions

Core stats can support an ability check, but ability progression should not collapse into Strength/Will/etc.

Example:

`Willpower + ability mastery -> control/reliability`

while the ability's actual resource capacity or evolution requirement may follow its own rules.

## 9. Derived-stat ownership under the eight-stat candidate

These are architectural examples, not final balance formulas.

- Max Health: primarily Constitution, possibly small Will contribution
- Max Stamina: Constitution + Athletics/training
- Max Focus: Intellect + Willpower
- Max Resolve: Willpower + Presence/Leadership where appropriate
- Initiative: Agility + Perception
- Accuracy: Dexterity + Perception + weapon skill
- Evasion: Agility + Perception + Athletics/Defense
- Guard: Constitution/Strength + Defense depending final combat model
- Carry Capacity: Strength + Constitution
- Fine Manipulation: normally use Dexterity directly with task skill rather than adding another permanent derived stat

[PROVISIONAL] Exact weights remain balancing data.

## 10. UI impact

Eight stats are still small enough for a readable status panel if grouped correctly:

Physical:
- Strength
- Constitution
- Agility
- Dexterity

Mental / Awareness:
- Perception
- Intellect
- Willpower

Social:
- Presence

The player should see base/effective distinctions through inspection/tooltips rather than duplicate every number on the primary screen.

The new effective-value explainability work supports this:

`base -> equipment/set/perk/condition contributions -> effective value -> derived formula -> final value`

The UI must consume the rules explanation contract rather than reimplement formulas.

## 11. Migration impact

If the project accepts the eight-stat model, this is the cheapest stage to migrate because the content base is still small.

Likely mapping:

- `might` -> `strength`
- `endurance` -> `constitution`
- `agility` -> remains `agility`
- new `dexterity` -> requires an explicit initialization/migration rule
- `intellect`, `will`, `perception`, `presence` -> semantic continuity, with player-facing naming allowed to change independently from stable IDs if desired

[QUESTION] Existing-save initialization for new Dexterity must not be guessed. Options include copying old Agility, deriving from a formula, assigning a baseline, or requiring a migration choice. This must be decided before any persistent save using the new schema is considered stable.

## 12. Recommendation candidate

[DESIGNED] **Eight core attributes are the stronger long-term architecture for the intended game**, mainly because Dexterity removes a real responsibility overload from Agility and Constitution creates a clearer distinction between permanent bodily resilience and the spendable Stamina resource.

This is not a recommendation to inflate the game with more stats. The rule is the opposite: eight should be treated as the ceiling for generic core attributes unless a future mechanic proves a new attribute has a distinct, repeated rules purpose.

The seven-stat model remains viable if the project deliberately decides that fine precision belongs entirely to skills and that Agility is allowed to be broad. That choice should be explicit rather than accidental.

## 13. Acceptance gate

Do not migrate executable code solely because this document recommends eight.

Before canonicalization:

1. review the scenario matrix
2. confirm whether Dexterity deserves a core slot
3. confirm `constitution` vs `endurance` terminology
4. choose stable internal IDs
5. define save migration before changing schema version
6. update derived formulas and validation registry as one atomic migration
7. update status-screen labels
8. update tests/content in the same change
9. run the full test suite
10. record the decision in `DECISIONS.md`

Related:
- `DEC-STAT-001`
- `CP-2026-09-27-STATS-SCHEMA-01`
- `CP-2026-09-27-EFFECTIVE-HARDENING-04`
