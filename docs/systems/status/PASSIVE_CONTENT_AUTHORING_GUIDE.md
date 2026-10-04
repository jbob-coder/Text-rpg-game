# THE GAME — Passive Content Authoring Guide

Status: **ACTIVE TARGET-GAME AUTHORING GUIDE / IMPLEMENTATION DEFERRED**

Parents:
- `../STATUS_UI_ABILITIES_AND_PASSIVES_MASTER_PLAN.md`
- `PASSIVE_REGISTRY_SCHEMA.md`
- `PASSIVE_REQUIREMENT_LANGUAGE.md`
- `STATUS_KNOWLEDGE_VISIBILITY_STANDARD.md`

Purpose: define how to author scalable passive records that remain deterministic internally, hidden when appropriate, resistant to exploit farming, and reconstructable by a future developer.

## 1. Passive authoring state machine

1. `SEED`
2. `CALIBRATION_PROPOSAL`
3. `DEEP_AUTHORED`
4. `AUDITED`
5. `CANON_APPROVED`
6. `IMPLEMENTATION_MAPPED`
7. `IMPLEMENTED`
8. `VERIFIED`

A passive does not become canon or implemented merely by existing in the catalog.

## 2. Start with the effect

The effect must state:
- what changes;
- when it applies;
- what it does not change;
- whether it scales;
- whether it stacks;
- what caps it;
- whether it is always-on or conditional.

Avoid “better at X” without defining the affected state or resolution path.

## 3. Keep passives separate from primary abilities

A passive may:
- improve control;
- improve efficiency;
- reduce a cost;
- support an application;
- alter recovery;
- interact with technique use.

A passive must not silently grant a second primary ability.

## 4. Acquisition must be deterministic

Use `PASSIVE_REQUIREMENT_LANGUAGE.md`.

Requirements should be representable through:
- `all`;
- `any`;
- `not`;
- `sequence`;
- `within`;
- `count`.

Every accumulating requirement needs:
- increment event;
- unit;
- threshold;
- reset behavior;
- decay behavior;
- interruption behavior;
- stacking rule.

## 5. Hidden-until-qualified rule

Before qualification:
- no name;
- no icon;
- no locked slot;
- no exact requirement;
- no hidden progress percentage.

Internal counters may still exist.

After qualification:
- reveal policy follows the passive record;
- owner visibility may become active;
- public/institutional knowledge remains separate.

## 6. Exploit-control rule

Every repeatable unlock path must answer:
- what makes an event meaningful;
- what makes a target/activity trivial;
- whether duplicate event credit is possible;
- whether save/reload can duplicate progress;
- whether collusion can farm progress;
- whether self-harm could become the optimal strategy.

If self-destructive behavior dominates the unlock route, redesign the requirement.

## 7. Physical adaptation rule

For adaptation passives:
- progressive legitimate stress should matter;
- recovery should matter;
- injury should not be the intended currency;
- one extreme reckless event should not equal months of adaptation unless explicitly authored;
- the passive should not erase physiology.

## 8. Combat-history rule

For combat passives:
- only meaningful encounters count;
- helpless-target farming must not dominate;
- kill credit must respect future Level/XP contribution rules where relevant;
- training and live combat may use different evidence classes;
- defensive/passive learning may credit successful nonlethal resolutions if authored.

## 9. Injury/scar rule

Injury-derived passives require:
- documented injury state;
- stabilization;
- rehabilitation/adaptation;
- anti-reinjury farming;
- explicit distinction between compensation and magical healing.

## 10. Knowledge asymmetry

Every passive should eventually document:
- public knowledge;
- school knowledge;
- government knowledge;
- military/security knowledge;
- research knowledge;
- faction knowledge;
- classification;
- known method;
- false rumors;
- historical cases.

Knowledge of an unlock method does not itself satisfy the unlock unless the passive explicitly requires knowledge.

## 11. False-rumor authoring

A false rumor must have:
- source/provenance;
- what it claims;
- why people believe it;
- how dangerous or costly it is;
- who benefits from the misinformation if deliberate;
- how the truth can be discovered.

Do not use random lies solely to frustrate the player.

## 12. Significance model

Passive significance is multi-axis:
- prevalence;
- requirement rarity;
- power significance;
- secrecy;
- danger;
- historical uniqueness.

Do not force the primary-ability rarity ladder onto passives.

## 13. Interaction packet

Review:
- attributes;
- skills;
- primary ability;
- techniques;
- equipment;
- conditions/injury;
- profession/class;
- world activity;
- combat;
- social systems.

Explicitly identify duplicate/overlap risk with other passives.

## 14. Evolution and exclusivity

A passive may:
- stay static;
- scale;
- gain stages;
- evolve;
- merge;
- exclude another route.

Any such behavior needs stable IDs and migration rules.

Do not imply evolution merely because a stronger-sounding passive exists.

## 15. World-content requirement

A passive system requires activities that can actually satisfy its rules.

Authoring should identify content sources such as:
- training facilities;
- schools;
- professions;
- wilderness;
- beast zones;
- hospitals/rehabilitation;
- mentors;
- manuals;
- factions;
- classified programs;
- research;
- unique events.

A passive with an unlock condition that the world cannot produce is incomplete.

## 16. Implementation mapping

Before code:
- authoritative progress counters;
- qualifying-event source;
- hidden-state owner;
- save persistence;
- reveal transition;
- projection filtering;
- anti-farm rules;
- migration;
- tests.

Android must receive only player-safe projected data.

## 17. Test requirements

Every implemented passive should have tests for:
- unmet condition remains hidden;
- qualifying condition resolves deterministically;
- exact threshold boundary;
- duplicate-event rejection;
- invalid/trivial event rejection;
- reveal timing;
- save/load persistence;
- effect activation;
- stacking/cap;
- conflicts/exclusivity;
- hidden future evolution remains hidden.

## 18. Promotion checklist

A passive may be proposed for canon when:
- stable ID exists;
- effect is specific;
- scaling/stack/cap are defined or intentionally `TBD`;
- acquisition packet is deterministic;
- hidden-progress policy is safe;
- exploit controls are explicit;
- knowledge scopes are authored;
- significance is described;
- interactions/overlap reviewed;
- evolution behavior explicit;
- world content can support the unlock;
- implementation/test needs are known;
- no runtime claim is fabricated.
