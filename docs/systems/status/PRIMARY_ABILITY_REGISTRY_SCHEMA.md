# THE GAME — Primary Ability Registry Schema

Status: **ACTIVE TARGET-GAME AUTHORING STANDARD**

Parent:
- `../STATUS_UI_ABILITIES_AND_PASSIVES_MASTER_PLAN.md`
- `ABILITY_RARITY_STANDARD.md`

Purpose: define the stable record structure for every human primary ability.

---

# 1. Identity

Required fields:

- `ability_id`
- `display_name`
- `aliases[]`
- `rarity`
- `ability_family`
- `stable_version`
- `canon_status`
- `design_status`
- `implementation_status`

An ID is permanent and cannot later be reused for another ability.

---

# 2. Core law

Every ability must have a concise **core law** explaining what it actually does.

The core law defines:
- what phenomenon it controls/creates/changes;
- what it can affect;
- what it cannot affect;
- what must be present for it to work;
- whether the effect is generated, transformed, transferred, sensed, reinforced, suppressed, stored, or redirected.

This prevents uncontrolled ability drift.

---

# 3. Capability boundaries

Record:

- allowed capability domains;
- explicitly forbidden domains;
- range model;
- target model;
- line-of-sight needs;
- contact requirements;
- area behavior;
- duration;
- persistence after user stops;
- self-target rules;
- ally/enemy targeting rules;
- environmental constraints;
- maximum simultaneous effects;
- whether effects can be stacked.

Unknown values remain `TBD`; never silently invent them during implementation.

---

# 4. Awakening state

Record:
- age-18 initial manifestation;
- starting technique(s), if any;
- starting control level;
- starting resource burden;
- common awakening hazards;
- public visual/signature;
- known misclassification risk.

The awakening manifestation should express the ability's core law without granting the full endgame toolkit immediately.

---

# 5. Rarity justification

Required:
- canonical rarity;
- rarity rationale;
- known occurrence frequency;
- comparison against adjacent tier;
- institutional classification confidence;
- true rarity if public rarity is incorrect/hidden.

---

# 6. Level interaction

Document:
- whether Level increases raw output;
- whether Level increases scale/range;
- whether Level unlocks technique capacity;
- whether Level only supports stats rather than the ability directly;
- any Level gates;
- Level-100 interaction.

Do not assume every ability scales identically with Level.

---

# 7. Attribute interactions

List relationships to:
- Might;
- Agility;
- Endurance;
- Intellect;
- Will;
- Perception;
- Presence.

For each relevant attribute, describe what changes and why.

Do not make an attribute relevant solely to inflate build complexity.

---

# 8. Skill interactions

List relevant learned skills.

Examples:
- Technical Systems for a technology-interfacing ability;
- Medicine for biological/healing control;
- Tactics for battlefield application;
- Powers knowledge for analysis/control;
- Athletics for movement-heavy manifestations.

Skill interaction does not change the one-primary-ability rule.

---

# 9. Resource model

Record all costs:
- stamina;
- focus;
- resolve;
- health;
- ability-specific energy;
- environmental resource;
- stored charge;
- cooldown;
- recovery debt;
- long-term strain.

Every major effect must identify its cost model or explicitly state why no direct cost exists.

---

# 10. Mastery structure

Each ability should define:
- discovery/control stage;
- mastery XP/progression;
- stage thresholds;
- control improvements;
- efficiency improvements;
- stability changes;
- advanced application requirements.

Current runtime mastery concepts may be retained where compatible, but this schema owns the evolved target record.

---

# 11. Techniques

Each technique record must link back to the parent ability and include:

- `technique_id`;
- name;
- technique type;
- prerequisites;
- effect;
- cost;
- range/target;
- failure modes;
- counterplay;
- mastery;
- visibility;
- evolution links;
- visual/FX requirements.

Techniques are applications of the ability's core law, not unrelated powers.

---

# 12. Evolution

Record possible evolution routes:

- mastery-driven;
- Level-gated;
- stat-gated;
- knowledge-gated;
- event-gated;
- passive-synergy;
- environmental adaptation;
- cosmic/system intervention;
- Level-100 replacement interaction.

Evolution must preserve or explicitly transform the core law.

---

# 13. Passive synergies

Document:
- passives that enhance the ability;
- passives that modify cost/control;
- passives that create new legal applications;
- passives that conflict;
- mutually exclusive adaptations.

Do not bake every passive into the ability record itself; cross-reference stable passive IDs.

---

# 14. Counters and weaknesses

Required:
- natural counters;
- tactical counters;
- environmental counters;
- resource denial;
- range weaknesses;
- concentration weaknesses;
- matchup weaknesses;
- known institutional countermeasures.

If an ability has no obvious counter, document why and what other constraints keep it from being arbitrary.

---

# 15. Failure and danger

Record:
- overuse;
- misfire;
- recoil;
- self-injury;
- cognitive/mental strain;
- environmental damage;
- collateral risk;
- loss-of-control scenarios;
- catastrophic threshold.

High rarity may increase danger as well as potential.

---

# 16. World knowledge

Record:
- public knowledge;
- school curriculum;
- government records;
- military/security doctrine;
- research status;
- faction knowledge;
- classified information;
- false theories;
- known historical users.

The player's Status view must not inherit all world-internal knowledge automatically.

---

# 17. Social/legal implications

Record:
- registration rules;
- restrictions;
- dangerous-use laws;
- profession opportunities;
- mandatory monitoring if any;
- recruitment pressure;
- stigma/prestige;
- insurance/medical implications if world design supports them.

---

# 18. Known users

Each ability should support:
- current known users;
- historical users;
- famous incidents;
- Level ranges;
- technique differences;
- unique personal passives.

One ability identity may produce distinct builds across users unless it is Unique.

---

# 19. Visual production

Required visual documentation may include:
- awakening FX;
- Status icon;
- rarity frame;
- technique icons;
- active FX;
- environmental effect layers;
- injury/strain feedback;
- portrait/actor state tags.

Character rendering remains pixel-art assets; ability FX must not replace character identity with procedural geometry.

---

# 20. Content requirements

Every ability should eventually have:
- at least one awakening scene/example;
- training opportunities;
- technique discovery content;
- failure/overuse content;
- social consequence;
- tactical use;
- noncombat use where plausible;
- NPC/world reactions;
- counter content;
- progression hooks.

---

# 21. Example non-canon skeleton

```yaml
ability_id: ABILITY_EXAMPLE
display_name: Example
rarity: rare
ability_family: example_family
canon_status: non_canon_example
core_law:
  summary: Structural example only.
boundaries:
  allowed: []
  forbidden: []
awakening:
  initial_manifestation: TBD
resources:
  focus: TBD
techniques: []
evolution: []
passive_synergies: []
knowledge:
  public: unknown
```

This skeleton is not a game ability.

---

# 22. Validation

Future tooling should detect:
- duplicate ability IDs;
- invalid rarity;
- missing core law;
- technique links to wrong parent;
- dangling passive IDs;
- contradictory public/true rarity;
- impossible evolution links;
- missing visibility classification;
- missing implementation/canon state.

---

# 23. Reconstruction acceptance

One ability record must be sufficient for another developer/AI to determine:
- what the ability is;
- what it cannot do;
- why it has its rarity;
- how it scales;
- what it costs;
- how it is trained;
- what techniques belong to it;
- what counters it;
- what the world knows;
- what art/content/tests it needs;
- whether it is implemented.
