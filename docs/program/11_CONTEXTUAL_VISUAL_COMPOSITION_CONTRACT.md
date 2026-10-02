# Contextual Visual Composition and Character Panel Contract

Status: **DOCUMENTED / TARGET CONTRACT — IMPLEMENTATION PENDING**
Repository: `jbob-coder/Text-rpg-game`
Program owner: Pixel Art / Asset / UI + Characters / NPC / Social

## 1. Purpose

Define how the Story screen, room/scene illustration, character panel, portraits, paper-doll layers, props, overlays, and contextual UI change according to authoritative scene state.

The core rule is:

> Presentation may react to who is present. Presentation may not decide who is present.

## 2. Current verified state

The current Android visual path already separates several concerns:

- `SceneIllustration.kt` renders a location scene master.
- scene overlays are selected separately.
- environment decals and props are placed separately.
- `PixelStoryActorCatalog.kt` places story actors on top of scene art.
- Trace/effect visuals are separate from the base environment.
- relay state is projected by the Python Android bridge as player-safe visual state.

Current actor placement is still keyed by `sceneId + locationId` inside the Android visual catalog.

Confirmed examples:
- `OPENING_DEPOT_BLACKOUT` / `PLATFORM_NINE`: wounded courier + Tamsin.
- `OPENING_DECISION` / `PLATFORM_NINE`: Tamsin.
- `OPENING_RECOVERY` / `RELAY_WORKBENCH`: Tamsin.
- `OPENING_TUNNEL` / `SERVICE_TUNNEL`: Tamsin.

This works for the current slice but it is not the final ownership model, because the UI catalog is effectively inferring presence from scene IDs.

## 3. Target ownership

### Engine/content owns
- which characters are physically present;
- who is in the party;
- who is absent, incapacitated, dead, hidden, or unavailable;
- who is the current/focused speaker when authored;
- public-safe expression/emotion/presentation tags;
- interaction availability;
- relationship/condition facts that are safe to expose;
- whether an NPC may be shown at all.

### Android/UI owns
- panel layout;
- which visible slot is largest;
- portrait versus full-body presentation;
- transition/animation between focus changes;
- responsive collapse at phone widths;
- how multiple present characters are arranged;
- visual emphasis;
- which approved asset variant maps to a presentation tag.

### Asset catalogs own
- stable art IDs;
- approved portrait/sprite variants;
- anchor points;
- z-order;
- palettes;
- scene placements that are purely spatial templates;
- reusable chrome/frames.

## 4. Target player-safe scene-presence projection

The target projection is documented as:

```text
scene_presence:
  present_characters:
    - character_id
      role
      focus
      party_member
      presentation_tags[]
  focused_character_id
  conversation_mode
```

This is a conceptual contract. Exact serialized field names may be adjusted during implementation, but the ownership and information boundaries are locked.

Allowed player-safe presentation tags may include:
- neutral
- focused
- concerned
- angry
- relieved
- diagnostic
- injured
- exhausted
- guarded

A tag exists only when authored/projected. UI must not infer hidden emotion from relationship scores.

## 5. Panel modes

### P0 — Environment only
Use when no visible character needs emphasis.

Shows:
- scene/location art;
- environmental overlays;
- relevant stateful props;
- no invented NPC portrait.

### P1 — Player + one focused character
Primary conversation layout.

Shows:
- player identity/presence;
- focused NPC portrait or sprite;
- name/role when player-safe;
- optional public-safe status/emotion tag;
- narrative/choices.

### P2 — Player + multiple present characters
Group scene.

Shows:
- focused speaker at highest emphasis;
- other present characters at lower emphasis;
- party members distinguishable from incidental NPCs;
- no hidden relationship values unless deliberately exposed by another UI surface.

### P3 — Party/travel
Used when the scene is more about group composition than a single speaker.

Shows:
- player;
- current party members;
- compact status;
- location/travel context.

### P4 — Character inspection
Separate from Story conversation.

Shows:
- paper-doll/equipment;
- stats/status allowed by the player projection;
- stable identity;
- no scene-only NPC presence inference.

## 6. Room/scene layering

Recommended render stack:

1. base location master;
2. permanent architecture;
3. permanent props;
4. stateful props;
5. environmental decals;
6. environmental state overlay;
7. visible NPC/story actors;
8. player actor where the composition requires it;
9. injury/status overlay;
10. ability/Trace FX;
11. interaction markers;
12. contextual UI chrome.

The order may be locally adjusted for occlusion, but gameplay meaning must remain intact.

## 7. Reuse compatibility matrix

An asset may be reused across locations only when the following remain compatible:

- native grid;
- perspective/camera;
- pivot/anchor;
- scale;
- light direction;
- material family;
- palette/value relationship;
- z-order/occlusion;
- semantic meaning;
- state ownership.

Examples:

### Safe reuse
- municipal lamp module in two civic locations with same perspective and lighting family;
- pipe support module across lower maintenance scenes;
- generic UI panel frame;
- map-marker family;
- approved injury overlay on a compatible character rig.

### Unsafe reuse
- portrait sprite pasted into a top-down map;
- bright daytime prop placed in a dark maintenance scene without relighting/versioning;
- Tamsin-specific satchel used as a generic NPC accessory;
- active Trace effect painted permanently into an idle scene;
- a locked-door visual reused to imply a lock when gameplay state says open.

## 8. External-reference extraction

The supplied visual sheets support these abstract principles:
- stable character turnarounds;
- layered equipment;
- separate icon families;
- separate FX families;
- location preview families;
- coherent panel/icon language;
- modular settlement/environment kits.

Not adopted automatically:
- any illustrated character identity;
- exact hairstyle/outfit;
- exact animation counts;
- exact palette;
- exact asset numbering;
- exact item names not already in the repository;
- exact environment layouts.

## 9. Migration from current actor placement

Current:
`sceneId + locationId -> PixelStoryActorCatalog.placements()`

Target:
`player-safe scene_presence projection -> visual resolver -> approved actor placements/panel composition`

Migration requirements:
1. add scene-presence projection to the engine/bridge;
2. preserve hidden-state redaction;
3. map known current scenes to equivalent projected presence;
4. update Android actor placement to consume projected characters;
5. preserve scene-specific spatial anchors separately from presence;
6. add regression tests proving absent characters do not render;
7. add group-scene tests;
8. add save/resume tests if presence depends on persistent state;
9. verify screenshots on representative mobile layout.

## 10. Failure and recovery

Potential failure: UI renders an NPC who should be absent.
Detection: projection/catalog mismatch test or screenshot.
Recovery: fall back to environment-only presentation rather than invent presence.

Potential failure: unknown character has no art.
Detection: projection contains stable character ID with no approved visual.
Recovery: use documented safe placeholder policy or omit visual emphasis while preserving text; never substitute another character.

Potential failure: overlay conflicts with character/equipment z-order.
Detection: visual QA/native-scale inspection.
Recovery: fix anchor/z-order metadata; do not alter gameplay state.

## 11. Acceptance tests for implementation phase

- a scene with no present NPC renders none;
- a scene with one focused NPC highlights only that NPC;
- a group scene preserves every projected visible member;
- changing party state changes panels without modifying UI-authored rules;
- save/load preserves the authoritative state used to derive presence;
- hidden NPC state never leaks through presentation tags;
- temporary overlays can be added/removed without rebuilding base scene art;
- 320dp-class layout remains readable and touch-safe;
- current opening scenes retain equivalent visible actors after migration.

## 12. Locked decisions

1. Scene presence belongs to engine/content state, not the asset catalog.
2. Android consumes a player-safe presence projection.
3. Character panels have environment, focused, group, party and inspection modes.
4. Assets remain layered and reusable only when their technical/semantic contracts match.
5. Unknown/missing art never authorizes substituting the wrong character.
6. Current hard-coded scene actor placement is migration debt, not the final architecture.
