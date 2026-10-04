# THE GAME — Adversary Encounter Memory & Bounded Adaptation Standard

Status: **APPROVED FIRST-PASS V09 CONTRACT / NO ARBITRARY POWER SCALING**
Parent:
- docs/systems/PERSISTENT_ADVERSARY_WORLD_MEMORY_MASTER_PLAN.md
Related:
- docs/systems/NPC_MEMORY_EVENT_STANDARD.md
- docs/systems/NPC_KNOWLEDGE_BELIEF_PRIVACY_STANDARD.md
- docs/systems/INJURY_CONDITION_AFTERMATH_STANDARD.md

## 1. Purpose

Define what a persistent adversary remembers from an encounter and how that memory may cause bounded, explainable future changes.

## 2. Significant encounter record

Target summary:
- encounter_id;
- adversary_id;
- time/location;
- outcome;
- participants perceived;
- injuries;
- observed player actions/techniques;
- escape/capture/spare state;
- relevant ally/faction losses;
- knowledge gained;
- source memory IDs;
- aftermath reference.

Do not persist the entire tactical event log as adversary memory.

## 3. Perception boundary

An adversary can remember:
- what they perceived;
- what an ally/faction later told them;
- what they inferred through explicit rules.

They cannot adapt to:
- an unseen ability;
- hidden inventory;
- private player stats;
- reload attempts;
- UI-only selections.

## 4. Adaptation record

Target fields:
- adaptation_id;
- source memory/knowledge;
- category;
- precondition;
- selected change;
- bounded options;
- cost/resource/time;
- applied_at;
- expiration or permanence;
- player visibility;
- rationale.

## 5. Allowed adaptation classes

Examples:
- tactic preference;
- engagement range;
- retreat threshold;
- cover preference;
- equipment selection from available stock;
- ally request;
- route avoidance;
- surveillance/observation;
- resistance/preparation only if an authored ability/item/resource permits it.

## 6. Forbidden shortcut

Never use:
“lost to player -> +N stats”.

Stat/skill growth must come from the same progression/training/world systems available to that actor type.

## 7. Equipment adaptation

An adversary can equip a counter item only if:
- item exists;
- faction/actor can access it;
- enough world time/resources exist if modeled;
- actor knows a reason to prepare it;
- equipment legality permits it.

## 8. Deterministic selection

When multiple adaptation options are valid:
1. filter by knowledge/capability;
2. score by goal/doctrine/personality;
3. stable tie-break.

If variation is needed, use seeded deterministic selection and persist the chosen adaptation.

## 9. Memory consequences

Encounter memory may change:
- goals;
- fear/respect/hostility-like V09 state when adopted;
- faction report;
- route preferences;
- preparation.

It does not automatically alter ordinary player-to-NPC relationship axes unless the actor uses those axes and an explicit consequence exists.

## 10. Forgetting/decay

Critical adversary encounter history should not vanish arbitrarily.

Salience may decay, but durable major events remain historical.

## 11. Player-facing evidence

A later player may infer adaptation from:
- changed visible equipment;
- dialogue;
- tactical behavior;
- rumor;
- observed preparation.

The UI does not reveal the internal adaptation record automatically.

## 12. Tests

Required:
- unseen tactic cannot trigger counter;
- visible technique can create memory;
- bounded option filtering;
- no arbitrary stat inflation;
- deterministic choice;
- equipment access requirement;
- save/load;
- private adaptation redaction.
