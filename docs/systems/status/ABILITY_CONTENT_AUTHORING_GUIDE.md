# THE GAME — Primary Ability Content Authoring Guide

Status: **ACTIVE TARGET-GAME AUTHORING GUIDE / IMPLEMENTATION DEFERRED**

Parents:
- `../STATUS_UI_ABILITIES_AND_PASSIVES_MASTER_PLAN.md`
- `PRIMARY_ABILITY_REGISTRY_SCHEMA.md`
- `ABILITY_RARITY_STANDARD.md`
- `STATUS_KNOWLEDGE_VISIBILITY_STANDARD.md`
- `AWAKENING_EVENT_STANDARD.md`
- `LEVEL_100_EXCEPTION_STANDARD.md`

Purpose: define the repeatable workflow for turning a primary-ability idea into a reconstruction-grade record without ability drift, rarity inflation, hidden-state leaks, or unsupported implementation claims.

## 1. Authoring state machine

Every ability moves through explicit states:

1. `SEED` — concept only;
2. `CALIBRATION_PROPOSAL` — stable ID + core law + first boundaries;
3. `DEEP_AUTHORED` — full registry fields materially filled or intentionally `TBD`;
4. `AUDITED` — overlap/rarity/counter/world review completed;
5. `CANON_APPROVED` — explicit design-authority promotion;
6. `IMPLEMENTATION_MAPPED` — engine/save/UI/test mapping written;
7. `IMPLEMENTED` — runtime evidence exists;
8. `VERIFIED` — tests/QA prove intended behavior.

Do not skip directly from seed to implemented.

## 2. Start with the core law

Write one concise sentence answering:
- what phenomenon is controlled/generated/transformed/sensed/stored/suppressed/redirected;
- what the user actually causes;
- what the ability does **not** do.

If the law cannot be stated clearly, the ability is not ready for catalog entry.

## 3. Define forbidden domains immediately

For every allowed behavior, ask what neighboring power would be an illegal expansion.

Examples:
- impulse control is not sustained telekinesis;
- thermal sight is not x-ray vision;
- water movement is not water creation;
- skin reinforcement is not healing;
- light emission is not hard-light construction.

These forbidden domains are permanent review anchors.

## 4. Rarity calibration

Rarity is not selected because the name sounds impressive.

Evaluate:
- scarcity;
- governing-law exceptionalism;
- initial manifestation;
- breadth;
- technique depth;
- evolution ceiling;
- resource burden;
- counter availability;
- strategic value;
- institutional attention.

Then compare against:
- one ability below;
- one ability above;
- at least one same-tier peer.

If the ability would fit equally well in several tiers, the rationale is incomplete.

## 5. Awakening packet

Author:
- first manifestation;
- age-18 event handling;
- immediate hazard;
- observable signature;
- medical/safety response;
- classification uncertainty;
- public versus protected fields.

Do not use awakening to give the user their endgame toolkit.

## 6. Boundary packet

Record:
- range;
- target type;
- line of sight;
- contact;
- area;
- duration;
- persistence;
- simultaneous effects;
- stacking;
- environmental requirements;
- invalid targets;
- self/ally/enemy rules.

Use `TBD` rather than inventing a numeric value that has not been calibrated.

## 7. Resource packet

Every meaningful technique must answer:
- what is spent;
- what accumulates;
- what recovers;
- what happens on depletion;
- whether there is recovery debt;
- whether use can injure the user;
- whether the environment supplies a required resource.

No ability may have unlimited high-value output merely because its cost field was omitted.

## 8. Level / attribute / skill interactions

Level interaction must respect `LEVEL_AND_XP_STANDARD.md`.

Until Level rewards are locked:
- do not assume every Level increases raw ability output;
- do not add automatic range or damage scaling;
- do not use Level to replace mastery/training.

Attribute and skill links must have a causal reason.

## 9. Technique authoring

A technique is an application of the parent law.

Each technique needs:
- stable technique ID;
- display name;
- role/type;
- prerequisites;
- effect;
- range/target;
- cost;
- failure;
- counterplay;
- mastery;
- visibility;
- evolution links;
- FX/content requirements.

Technique progression should broaden control, efficiency, reliability, or applications before it simply multiplies raw power.

## 10. Counterplay requirement

At least one meaningful counter route must exist unless the record explicitly explains why another constraint substitutes for normal counterplay.

Review:
- natural/physical limits;
- range;
- resource denial;
- concentration;
- environment;
- equipment;
- team tactics;
- knowledge;
- institutional countermeasures.

“Use a stronger ability” is not sufficient counter design.

## 11. Failure and danger

Author:
- minor failure;
- misuse;
- overuse;
- self-injury;
- collateral;
- loss of control;
- catastrophic threshold if any;
- recovery.

Higher rarity may increase danger rather than remove it.

## 12. World integration

For any ability considered for canon, document:
- public understanding;
- school training;
- government classification;
- military/security doctrine;
- research value;
- faction interest;
- profession opportunities;
- legal restrictions;
- insurance/medical effects if supported;
- black/illicit-market interest where relevant;
- historical users/incidents.

Do not invent named institutions inside an ability record before the world documents establish them.

## 13. Known-user rule

If no user has been authored, write `TBD` or `none authored`.

Never fabricate historical users simply to make an ability feel established.

## 14. Visual/content packet

Every promoted ability eventually needs:
- Status icon;
- rarity treatment;
- awakening FX;
- technique FX;
- strain/failure feedback;
- at least one training example;
- tactical use;
- noncombat use where plausible;
- social consequence;
- counter content;
- NPC/world reaction.

FX must preserve authored pixel-art character identity and mobile readability.

## 15. Implementation mapping

Before code:
- authoritative state owner;
- data schema;
- save fields;
- migration;
- projection/player-safe fields;
- Android model/view;
- content loader;
- validators;
- tests.

Do not let Android infer hidden ability truth that belongs to the engine.

## 16. Promotion checklist

An ability may be proposed for canon only when:
- stable ID exists;
- core law is clear;
- forbidden domains are explicit;
- rarity rationale passes adjacency review;
- awakening is authored;
- boundaries are actionable;
- resource model exists;
- techniques are individualized;
- counters/failures are specific;
- Level/stat/skill interactions are explicit or intentionally `TBD`;
- world knowledge is mapped;
- visual/content burden is understood;
- overlap review passes;
- no implementation is falsely claimed.

## 17. Rejection patterns

Reject or return for rewrite when:
- the ability has multiple unrelated laws;
- rarity is justified only by “very powerful”;
- costs are absent;
- every counter is bypassed by another undocumented sub-power;
- techniques are cosmetic renames;
- hidden knowledge is exposed to player UI;
- Level 100 is used as a normal respec shortcut;
- Unique is treated as synonymous with omnipotent;
- a proposal is written as if it is already runtime truth.
