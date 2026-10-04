# THE GAME — Work, Study & Research Activity Standard

Status: **APPROVED FIRST-PASS V10 CONTRACT / WORK SYSTEM FUTURE, STUDY/RESEARCH PARTIAL**
Parent:
- docs/systems/PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md
Related:
- docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
- docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md

## 1. Purpose

Define non-combat productive activities without inventing economy, employment, education, or research systems before their dependencies exist.

## 2. Current reality

Current content already supports research-like actions:
- examining the relay;
- Municipal Archive records;
- analyzing stable Trace patterns;
- diagnostic/research work in Gate Twelve locations.

A formal profession/payroll system does not yet exist.

## 3. Study

Study converts authored information sources plus time/attention into:
- knowledge;
- skill progress when justified;
- quest progress;
- technique/class prerequisites when documented.

Study requires a source:
- book/record/data;
- instructor;
- facility;
- known research question.

No source means no generic “study” gain.

## 4. Research

Research differs from simple study by producing or validating an inference.

Research definition may require:
- research subject ID;
- input knowledge;
- evidence sources;
- facility/tool;
- skill/attribute;
- duration;
- deterministic resolution;
- output knowledge;
- confidence/provenance;
- repeat rule.

Municipal Archive and Trace Chamber have different research identities and should not become interchangeable menus.

## 5. Diagnostics

Diagnostic activities are a practical research subclass:
- inspect device/system;
- compare traces;
- identify malfunction;
- produce knowledge/state.

Relay Workbench is the current proof context.

Diagnostics must not silently become crafting/repair.

## 6. Work/profession

A work activity requires a formal employment/economy contract before it can award money.

Target work fields:
- employer/institution;
- role/profession;
- schedule;
- location;
- required skill/status;
- duration;
- compensation source;
- reputation;
- performance rule;
- absence/failure consequence;
- legal/faction requirements.

Do not implement “work 8 hours = currency” in isolation.

## 7. Compensation

Compensation must come from an economy source ledger.

It may include:
- currency;
- goods;
- reputation;
- access;
- training;
- housing/service benefit.

The work system cannot mint value without provenance.

## 8. Education/classes

Formal classes may combine:
- schedule;
- instructor;
- tuition/access;
- curriculum;
- skill progression;
- attendance;
- exams/evaluation.

Not required for Phase 1.

## 9. Research uncertainty

If research uses a check:
- use deterministic authored resolution;
- failure may consume time without fabricating false knowledge unless the research definition explicitly supports mistaken inference;
- player-safe preview should not reveal hidden thresholds.

## 10. Knowledge output

Every research/study result identifies:
- knowledge ID;
- source;
- confidence;
- private/public;
- downstream uses.

Avoid generic “research points” unless a dedicated research progression system is later approved.

## 11. NPC participation

NPC may act as:
- instructor;
- coworker;
- supervisor;
- expert;
- research collaborator.

Participation requires presence, capability, and schedule/access.

Any social consequence is authored separately.

## 12. Location identity

Suggested current roles:
- Municipal Archive: records/study/validation;
- Relay Workbench: diagnostics;
- Trace Chamber: controlled power research/training;
- Workshop Row: future practical work/service only after economy/profession contracts.

## 13. Interruption

Research/work interruption defines:
- time spent;
- partial result;
- evidence preserved;
- compensation;
- social/employer consequence.

Phase 1 should keep research activities atomic where current content already does.

## 14. Player-safe projection

Show:
- activity;
- duration;
- source/facility;
- known requirements;
- known cost;
- known broad output.

Hide:
- undiscovered findings;
- secret employer/faction data;
- private NPC evaluation;
- hidden thresholds.

## 15. Tests

Required:
- no study without source;
- research input requirement;
- knowledge provenance;
- deterministic check if used;
- no unowned currency generation;
- NPC participant availability;
- interruption policy;
- save/load.

## 16. Phase 1

Phase 1 can use existing Trace analysis or Archive investigation as research evidence, but requirement #8 only needs one integrated life/activity proof. Training already provides the cleaner first proof.
