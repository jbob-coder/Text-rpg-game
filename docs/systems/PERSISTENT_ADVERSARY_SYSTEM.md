# Persistent Adversary System

Status: **REVIEWABLE / ORIGINAL SYSTEM ARCHITECTURE**
Domain: NPC / Beast / Combat / World
Requirement: `P-RIVAL-001`

## 1. Goal

Create an original system where selected recurring adversaries can remember encounters, change through consequences, alter relationships/territory/behavior, and reappear later.

This is a general systemic-rivalry design. It must not copy proprietary branding, hierarchy presentation, names, dialogue structure, rank ladders or one-to-one mechanics from another title.

## 2. Who can become persistent

Potential categories:
- hostile NPC;
- faction operative;
- criminal/bandit-type NPC if the setting uses them;
- rival hunter/competitor;
- bestia;
- other authored recurring adversary.

Not every enemy becomes persistent.

## 3. Persistent adversary record

Target fields:
- stable adversary ID;
- base entity ID;
- category;
- first encounter;
- last known state;
- territory/location;
- faction/pack;
- relationship/rivalry axes;
- encounter memories;
- injuries/scars;
- learned counters/adaptations;
- victories/losses/escapes;
- resources/equipment if relevant;
- goals;
- current availability;
- narrative hooks;
- player-known versus hidden information.

## 4. Memory

Record significant encounter facts, not full transcripts.

Potential memory events:
- player defeated adversary;
- adversary defeated player;
- adversary escaped;
- player spared/captured/released;
- specific injury inflicted;
- territory lost;
- ally/pack member lost;
- tactic repeatedly observed.

## 5. Adaptation

Adaptation may change:
- tactics;
- equipment;
- resistance/behavior;
- route choice;
- allies;
- territory;
- willingness to retreat;
- dialogue/presentation.

Adaptation must have authored bounds.

It must not become arbitrary AI stat inflation.

## 6. Injuries/scars

Persistent visible injuries can:
- modify capability;
- create weakness;
- create adaptation;
- alter appearance;
- influence behavior.

Visual scars/injury state must derive from authoritative persistent state.

## 7. Promotion/demotion replacement

A future faction hierarchy may allow status changes, but no proprietary ladder is assumed.

Possible original outcomes:
- gains responsibility;
- loses status;
- changes faction role;
- gains territory;
- loses territory;
- becomes independent.

Exact hierarchy is faction-specific.

## 8. Beast adversaries

A persistent bestia may retain:
- injury;
- territory;
- pack status;
- fear/aggression toward player;
- learned response;
- migration change;
- hunting pressure response.

It does not need human social ranks.

## 9. Encounter selection

Reappearance should depend on:
- location/territory;
- world state;
- availability;
- player history;
- faction/pack state;
- authored cooldown/timing;
- quest/event conditions.

Do not force a rival into unrelated scenes merely to keep the system visible.

## 10. Information boundary

Player UI may show only learned/observed information.

Hidden:
- future appearance schedule;
- hidden traits;
- exact adaptation rules;
- secret faction state.

## 11. Death/permanent removal

Final policy remains unresolved.

Possible states:
- active;
- injured;
- recovering;
- displaced;
- captured;
- retired;
- dead;
- unknown.

Permanent death/removal must be authoritative and persistent.

## 12. System interactions

Persistent adversaries can connect to:
- combat;
- factions;
- quests;
- economy/resource control;
- settlements;
- beast zones;
- reputation;
- knowledge;
- visual injury assets;
- world map events.

## 13. Anti-repetition rules

To avoid a gimmick loop:
- only meaningful adversaries persist;
- encounters need context;
- changes should be traceable to prior events;
- repeated reappearance needs authored justification;
- adaptations are bounded;
- the system should not override main story logic.

## 14. Determinism

Selection/adaptation can use seeded deterministic variation, but state transitions must remain inspectable/testable.

## 15. Implementation readiness gaps

- selection eligibility;
- maximum active persistent adversaries;
- memory schema;
- adaptation catalog;
- recurrence timing;
- death/removal rules;
- territory integration;
- faction hierarchy integration;
- bestia-specific adaptation rules;
- UI/journal surface.

## 16. Acceptance expectation

Implementation-ready when one real adversary can:
1. be promoted into persistent state;
2. record one encounter;
3. change from the result;
4. reappear under valid world conditions;
5. expose only player-safe information;
6. preserve state through save/load;
7. retire/die without corrupting references.
