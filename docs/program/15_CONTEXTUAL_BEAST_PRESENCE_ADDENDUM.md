# Contextual Visual Composition — Beast Presence Addendum

Status: **NORMATIVE ADDENDUM**
Extends: `11_CONTEXTUAL_VISUAL_COMPOSITION_CONTRACT.md`
Authority: `13_BEAST_ENTITY_ECOSYSTEM_AND_SCENE_PRESENCE_STANDARD.md`

## Scope

This addendum extends the contextual composition contract from character-only presence to all visible authored actors relevant to the scene, including the game's **bestias**.

## Locked rule

Presentation may react to a character or bestia only when authoritative game/content state says that entity is present.

The Android/UI layer may not invent presence from an available sprite, portrait, scene ID, or asset catalog entry.

## Target scene presence

The future player-safe presence projection must support, at minimum:

```text
present_characters[]
present_beasts[]
focused_entity_id
focused_entity_type
conversation_mode
encounter_mode
```

Exact serialized field names remain an implementation detail.

## Mixed scenes

The scene system must support:
- player + NPC;
- player + multiple NPCs;
- player + bestia;
- player + multiple bestias;
- player + NPCs + bestias;
- party + bestias;
- environment-only scenes.

Character and beast presence must not be collapsed into one social model.

## Beast-focused presentation

When a bestia is the focused entity, presentation may show only player-safe/observed information such as:
- known identity;
- visible condition;
- visible injury;
- focus/encounter state;
- player-known information.

It must not expose hidden stats, unseen entities, or unlearned ecological information.

## Layering extension

Scene composition may contain:
1. base environment;
2. architecture;
3. permanent props;
4. stateful props;
5. environment overlays;
6. NPC/story actors;
7. bestias;
8. player where composition requires;
9. injury/status overlays;
10. abilities/FX;
11. interaction markers;
12. contextual UI.

Occlusion may change the draw order locally, but state ownership does not change.

## Acceptance expectation

Future implementation must prove:
- absent bestias do not render;
- present bestias render using the correct stable identity;
- mixed character/bestia scenes preserve every projected entity;
- UI does not create hidden beast state;
- missing beast art falls back safely without substituting another species;
- save/resume preserves the authoritative state from which presence is derived.

## Terminology

Use **bestia / beast** as the normative game term. “Monster” is not the project taxonomy unless explicitly introduced later.
