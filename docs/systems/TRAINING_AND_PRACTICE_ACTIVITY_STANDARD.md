# THE GAME — Training & Practice Activity Standard

Status: **APPROVED FIRST-PASS V10 CONTRACT / CURRENT RUNTIME FOUNDATION EXISTS**
Parents:
- docs/systems/PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md
- docs/systems/PROGRESSION_MASTER_PLAN.md
Current source:
- src/textrpg/simulation.py
- src/textrpg/powers.py

## 1. Purpose

Define training of skills/attributes and practice of abilities/techniques as time/resource-bound progression, not instant menu upgrades.

## 2. Current runtime evidence

Current simulation supports:
- train(skill, minutes, intensity, mentor_bonus);
- train_attribute(...);
- stamina/focus costs;
- skill bounds;
- world-time advancement.

Current powers supports:
- technique mastery;
- practice_technique;
- resource costs;
- technique stages/discovery/use.

Current content uses these systems in Trace Chamber.

## 3. Training classes

First-pass:
- SKILL_TRAINING;
- ATTRIBUTE_TRAINING;
- TECHNIQUE_PRACTICE;
- ABILITY_MASTERY_USE;
- CONDITIONING_PROTOCOL.

Class/profession training can later compose these primitives.

## 4. Required definition fields

- activity_id;
- progression target;
- location;
- duration;
- intensity range;
- resource costs;
- mentor requirement/bonus if any;
- equipment/tool requirement if any;
- prerequisite knowledge;
- condition restrictions;
- output formula owner;
- repeat/diminishing policy;
- interruption rule.

## 5. Skill training

Preserve current skill catalog authority.

Training:
- cannot target unknown skill ID;
- consumes time;
- consumes relevant resources;
- cannot bypass cap;
- records progress;
- may be modified by mentor/location quality when later approved.

## 6. Attribute training

Attributes are more sensitive than skills.

Any attribute training needs:
- explicit allowed activity;
- stronger time/cost;
- caps/slow progression;
- balance review.

Do not expose a generic “train any attribute” UI merely because a primitive exists.

## 7. Technique practice

Practice requires:
- discovered/available technique;
- definition validation;
- enough ability resource and/or stamina/focus;
- time;
- legal location/context if authored.

Practice improves mastery according to the progression/power system.

It does not bypass discovery prerequisites.

## 8. Ability use vs practice

Real use and controlled practice are distinct event sources.

Both may add mastery if the ability contract allows it.

Practice is not automatically safer or equally efficient; definition owns risk/cost.

## 9. Mentors

Mentor bonus requires:
- NPC present/available;
- mentor knows/can teach the subject;
- relationship/payment/access if required;
- schedule compatibility.

Do not use a numeric mentor bonus without proving a mentor source.

## 10. Facilities

Facility quality may affect:
- allowed activity;
- risk;
- resource efficiency;
- max useful intensity;
- training output.

Trace Chamber is the current specialized proof facility for Trace Echo.

## 11. Injury/condition constraints

Conditions may:
- block training;
- cap intensity;
- increase cost;
- reduce gains;
- require recovery first.

Rules layer computes legality.

## 12. Diminishing returns

Phase 1 may preserve current formulas without a new daily fatigue system.

Long-range anti-grind may use:
- session caps;
- fatigue;
- diminishing repeated gains;
- mentor/facility access;
- resource recovery;
- skill ceilings.

Do not add all at once.

## 13. Player-safe preview

Show:
- subject;
- duration;
- known resource cost;
- legal/illegal;
- broad progress result where appropriate.

Do not expose hidden mastery thresholds unless the progression UI contract decides they are known.

## 14. Current Trace Chamber proof

Current authored actions include:
- PRACTICE_SIGNAL_PULSE_ONE_HOUR;
- PRACTICE_SIGNAL_PULSE_TWO_HOURS;
- TRAIN_POWER_FUNDAMENTALS_TWO_HOURS;
- COMPLETE_TRACE_TOLERANCE_PROTOCOL.

These should remain exact-content regression fixtures.

## 15. Tests

Required:
- unknown skill rejected;
- resource insufficiency rollback;
- time advancement;
- cap behavior;
- technique prerequisite;
- mastery progression;
- condition restriction;
- mentor/facility requirement;
- save/load;
- current Trace Chamber regression.

## 16. Phase 1

TRAIN_POWER_FUNDAMENTALS_TWO_HOURS is the cleanest existing proof of a timed activity that:
- consumes time/resources;
- changes progression;
- occurs at an authored location;
- persists through GameState.

Final Phase 1 validation must execute and save/load this path on the selected implementation head.
