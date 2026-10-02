# Beast Entity, Ecosystem and Scene Presence Standard

Status: **STRUCTURED / GLOBAL FOUNDATION**
Domains: World / Ecosystem / Combat / Visual Composition

## 1. Terminology

Normative term for the game's non-human hostile, neutral, territorial, tameable, ecological, or otherwise creature-like entities is:

**BEAST / bestia**

Do not substitute the generic term “monster” in project specifications unless a future explicit taxonomy distinguishes a separate category.

A beast is not automatically hostile.

## 2. Beast ownership model

A beast may participate in several systems:

- ecosystem;
- beast zone;
- encounter/combat;
- resource/loot;
- tracking;
- migration;
- faction/settlement pressure;
- scene presence;
- visual composition;
- persistent injury/state;
- rivalry/adversary systems where appropriate.

No single UI or asset catalog owns beast truth.

## 3. Stable beast identity

Every authored beast species/type eventually needs:

- stable beast ID;
- display name;
- taxonomy/category;
- ecosystem memberships;
- physical scale class;
- behavior profile;
- threat band;
- senses;
- movement modes;
- combat capabilities;
- weaknesses/resistances if used;
- body/harvest/resource profile if used;
- visual identity;
- audio identity if used;
- known variants;
- progression/evolution/mutation rules if adopted;
- persistence model.

Individual persistent beasts may additionally receive individual IDs.

## 4. Beast-zone contract

A beast zone is a spatial/ecological record, not merely a level range.

Required fields when authored:

- stable zone ID;
- parent region;
- coordinate/boundary space;
- species present;
- density bands;
- migration entrances/exits;
- habitat/resource drivers;
- time/season behavior if used;
- threat bands;
- human/settlement interaction;
- faction control/access;
- hunting/harvesting pressure;
- repopulation rules;
- quests/events;
- visual/map representation;
- state variants.

## 5. Ecosystem relationship

Every beast belongs to one or more ecosystem contexts.

Document:
- food/resource dependencies;
- predators/prey/competitors where relevant;
- shelter/habitat;
- migration;
- reproduction/repopulation assumptions if simulated;
- response to resource depletion;
- response to human expansion/hunting;
- world-event changes.

Do not create a giant simulation merely because the documentation supports ecological relationships. Runtime depth is a separate implementation decision.

## 6. Scene presence

Beasts use the same authority principle as characters:

> Presentation may react to a beast that is authoritatively present. Presentation may not invent beast presence.

Target player-safe scene presence expands to:

```text
scene_presence:
  present_characters[]
  present_beasts[]
  focused_entity
  focused_entity_type
  conversation_mode
  encounter_mode
```

Exact serialized names remain implementation details.

## 7. Beast panel/composition modes

### B0 — Environmental/background beast
Visible in scene composition but not the focused encounter entity.

### B1 — Focused beast
A beast is the primary visual/interaction focus.

May show:
- stable beast identity if known;
- public/observed condition;
- distance/range band if the combat/exploration system exposes it;
- visible injury;
- player-known scan/knowledge information.

### B2 — Multiple beasts
Group/pack/herd encounter.

Must preserve:
- individual/pack identity where gameplay distinguishes them;
- focus selection;
- no hidden-stat leakage.

### B3 — Beast + NPC/party mixed scene
Characters and beasts can coexist.

The composition system must not assume one category excludes the other.

### B4 — Combat/tactical scene
Combat UI may replace ordinary Story emphasis while consuming the same authoritative entity identities/state.

## 8. Visual asset families

Beast production may require:

- species master;
- scale reference;
- front/side/back or other required turnarounds;
- idle/movement/action frames;
- attack/defense states;
- injury overlays;
- status overlays;
- body-part layers if body-part gameplay is adopted;
- map marker;
- bestiary/journal icon;
- portrait/focus panel image;
- resource/harvest item icons.

Exact grids/resolutions are decided by the visual system, not by this taxonomy document.

## 9. Reuse rules

Reusable beast FX, injury, shadow, status, or environmental interaction assets require compatible:

- rig;
- scale;
- perspective;
- anchor;
- material/body surface;
- lighting;
- semantic meaning.

Do not reuse one species' identity-bearing anatomy to represent another species merely to save asset work.

## 10. Combat relationship

The future tactical combat system must be able to receive beasts as combatants without creating a separate contradictory rules engine.

Potential shared combat entities:
- player;
- party NPC;
- human hostile;
- beast;
- other future combat-capable actor categories.

Species-specific rules extend the shared combat contract.

## 11. Persistent adversary relationship

Some beasts may become persistent adversaries if the future rivalry system supports that behavior.

A persistent beast adversary may remember/recur through authored state such as:
- prior encounter;
- injury/scar;
- territory;
- learned behavior/counter;
- relationship/threat state;
- pack status.

This remains a target concept, not an implementation claim.

## 12. Loot/resource relationship

Beast-derived resources must come from authoritative beast/encounter state.

Potential factors:
- species;
- body part;
- damage;
- preservation;
- harvesting method;
- player skill;
- tool;
- world/ecosystem state.

Exact loot rules remain unresolved under the economy/ecosystem program.

## 13. Unknowns

Still undecided globally:
- final beast taxonomy;
- number of species;
- tame/capture/bonding rules, if any;
- reproduction simulation depth;
- mutation/evolution system;
- body-part combat scope;
- persistent individual-beast frequency;
- bestiary knowledge progression;
- exact threat/rank relationship;
- beast AI architecture.

## 14. Acceptance expectation

Future beast documentation is implementation-ready only when:
- stable identity exists;
- ecosystem/zone context exists;
- encounter role is clear;
- visible/persistent state ownership is clear;
- asset requirements are clear;
- loot/resources do not contradict economy rules;
- combat integration is specified;
- unknowns required for implementation are resolved.
