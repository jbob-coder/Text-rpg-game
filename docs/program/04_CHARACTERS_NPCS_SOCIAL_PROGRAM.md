# Characters, NPCs and Social Program

Status: ACTIVE / ARCHITECTURE

## Scope

Owns:
- player identity/presentation contract;
- NPC identity records;
- scene presence;
- party membership;
- relationships;
- memory;
- knowledge;
- goals;
- faction membership;
- citizen classes/hierarchy;
- discrimination/prejudice systems where the setting requires them;
- social consequences;
- character panel binding.

## Existing strengths

The engine already has documented concepts for:
- NPC memory;
- private knowledge;
- relationship axes;
- goals;
- story-state transitions;
- knowledge sharing/leaks;
- party changes;
- player-safe redaction.

These systems should be extended rather than duplicated in UI.

## Scene-presence contract

Requirement P-NPC-001:
Every scene requiring character-specific presentation should expose an authoritative list of present/active/focused characters.

Target projection may eventually include:
- present_character_ids;
- focused_speaker_id;
- party_member_ids;
- expression/emotion presentation tags;
- public status tags;
- interaction availability.

Exact schema remains to be designed and migrated.

## Character visual identity

Recurring characters require stable visual identity records. Future art cannot regenerate them from memory alone after approval.

## Citizen hierarchy

The owner explicitly requested class/hierarchy and racism/discrimination-related world systems.

These are worldbuilding and simulation systems, not assumptions about real-world groups.

Before implementation the setting must define:
- legal/social classes;
- economic classes;
- faction/citizenship categories;
- species/origin categories if fictional;
- privileges/restrictions;
- institutional enforcement;
- reputation consequences;
- mobility between classes;
- regional variation;
- how prejudice affects dialogue, prices, access, policing, quests and relationships;
- safeguards against reducing every NPC to one prejudice score.

This area remains largely UNDECIDED.

## NPC autonomy target

NPCs should behave as persistent actors rather than static menu entries.

Target capabilities may include:
- personal schedules;
- goals;
- relationship-dependent decisions;
- knowledge propagation;
- joining/leaving/refusing;
- reacting to world events;
- rivalries and alliances;
- injuries/death/absence where authored;
- independent resource/equipment state when needed.

Do not claim these are implemented until confirmed by code/tests.

## Required future documents

- NPC_SCHEMA_V2
- SCENE_PRESENCE_PROJECTION
- SOCIAL_CLASS_HIERARCHY
- FICTIONAL_PREJUDICE_AND_ACCESS_RULES
- FACTION_SOCIAL_GRAPH
- NPC_SCHEDULE_AND_AUTONOMY
- PARTY_BEHAVIOR
- RELATIONSHIP_BALANCE
- KNOWLEDGE_PROPAGATION_V2
- CHARACTER_PANEL_BINDINGS
