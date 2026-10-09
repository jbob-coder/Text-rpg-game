# Room composition implementation contract

Parent: [Room actor/panel/overlay standard](ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md).
Evidence: program baseline `4d596bcd27b6e2f8ef9ce3a93b9dab22f5f4812e`.
Status: operational design contract. **Current authority update:** D-064 has implemented and verified the player-safe room-actor projection and typed Android actor consumer. Contextual focus-panel payloads, broader actor coverage, equipment/held-object expansion and several asset/occlusion details below remain target/proposed work. Evidence: `docs/evidence/D064_PLAYER_SAFE_ROOM_ACTOR_PROJECTION_FINAL_2026-10-05.md`.

## 1. Historical baseline and current gap

At the recorded program baseline, `SceneIllustration.kt` received projected location, scene ID and relay state; `PixelStoryActorCatalog.placements()` selected opening actors from scene/location IDs; and `GameSnapshot` had no general visible-actor list or contextual portrait-panel model.

D-064 superseded the **presence** portion of that baseline: Python now projects player-safe room actors, Android maps typed `GameRoomActor` records, and `SceneIllustration` consumes projected actor placements rather than inventing story-actor presence from scene/location IDs. The remaining gap is broader authored actor/population coverage plus the still-unimplemented contextual portrait/focus-panel model. Do not infer that every named person in prose stands in the room.

| Scene | Location | Existing actor placement x,y |
| --- | --- | --- |
| OPENING_DEPOT_BLACKOUT | PLATFORM_NINE | wounded courier 34,13; Tamsin 62,14 |
| OPENING_DECISION | PLATFORM_NINE | Tamsin 62,14 |
| OPENING_RECOVERY | RELAY_WORKBENCH | Tamsin 90,14 |
| OPENING_TUNNEL | SERVICE_TUNNEL | Tamsin 76,14 |

These are sprite origins on the 128x64 scene canvas, not feet or world coordinates. Unknown scene/location pairs return no actors. A target ground pivot must explicitly convert from these origins; do not reuse them as foot anchors.

## 2. Implemented actor boundary and proposed panel extension

D-064 implements the versioned player-safe room-actor boundary for visible actor/presentation identity and semantic placement. Future extensions may add or deepen authorized display name, presentation role, pose/outfit variant, inspectability, dialogue/interaction availability, visible condition tags and contextual panel data where their owners approve them. The asset registry resolves sprite/portrait IDs. The area packet resolves slots/pivots/occlusion; engine must not decide pixel art layout.

Do not emit private goals, undiscovered names, hidden relationships, raw memories, secret injuries, quest prerequisites, unrevealed equipment or enemy intentions. A visible appearance variant must be approved by the projection policy, even if it reveals no text.

UI selection is transient. Selecting an actor opens a focus panel only while that actor remains visible in the current room. Clear selection on departure, new game, incompatible load, invalid ID or changed projection. Do not persist UI selection as NPC/world state. Narrative dialogue chooses an active speaker separately from user inspection; more than one present actor never causes overlapping full panels.

## 3. Panel behavior

Room: show the area and present actors. Focus: one selected actor portrait/name plus authorized context/actions. Dialogue: the current authorized speaker; prose stays accessible UI text. Character: player identity/equipment, independent of whether an NPC panel is open.

Missing portrait: use a neutral authored missing-art treatment or text-only panel; never substitute another character. Missing outfit layer: retain logical equipment and report missing art in developer evidence; do not fabricate gear. Unknown actor identity stays unknown. NPC departure closes its panel. No people present means no actor panel.

Required cases: zero actors; one; several; anonymous actor; actor departs during interaction; save/load changes room; failed action; large text; portrait missing; hidden actor; occluded actor; disabled interaction; rapid room changes.

## 4. Reuse and overlay rules

| Family | Direct reuse allowed when | Adaptation required when | Never infer |
| --- | --- | --- | --- |
| Wall/pipe/door modules | density, perspective, material and anchors agree | lighting/size/wear differ | a decorative door is an accessible route |
| Character/equipment | shared 32x48 origin, pivot, slot and orientation | body/pose/direction changes | item ownership from a drawn shape |
| Portrait | same identity and authorized outfit/condition | crop/emotion/value contrast changes | relationship or hidden knowledge |
| Weather/damage/power | layer and state meaning match | perspective/occlusion differs | gameplay status from timer or color |
| Signs/text-art | sign frame fits area perspective | language/content/scale differs | old sign content belongs everywhere |
| UI chrome | semantic role and accessibility match | narrow screen/large text changes layout | controls or mechanics without engine support |

Text-defined pixel grids are source-native art, not UI prose. Render their palette cells without smooth filtering. World signs follow perspective; player text uses accessible typography. Integer scale/pixel-snapped anchors are preferred; use separate resolution families when a surface cannot fit instead of distorting a sprite. Palette swaps must preserve meaning and identity; recoloring alone cannot fix incompatible perspective.

Area packet fields: location ID; source/raster versions; geometry reference; palette/material/light signature; camera perspective; native grid; player/NPC ground slots; z layers; prop/sign/FX anchors; occlusion mask; arrival preview; visible-state variants; safe panel layout; reduced-motion policy; consumer; phone screenshots; provenance.

## 5. Raster precedence and replacement

`PixelRasterCatalog.scene()` binds nine PNGs by location. `SceneIllustration` prefers these PNGs when decoded. Therefore source Kotlin edits alone do not establish that visible art changed. Every scene refinement must update/re-export the preferred PNG or explicitly remove/change the binding with an approved fallback reason. Record source hash, raster hash and pixel equality/difference evidence. A stale raster is a blocking visual-delivery defect.

Source-native catalog remains an inspectable fallback. Authored map images remain preferred where approved; fallback geometry is not the final art. Do not replace approved art by re-creating a similar composition procedurally.

## 6. Creation queue and acceptance

First: reconcile preferred scene/raster pairs and later Tunnel/Stair branches. Second: area anchors/occlusion packets for the nine locations. Third: **preserve D-064 room-actor projection invariants while expanding authored actor coverage and semantic placements**. Fourth: Jack/Tamsin portrait/pose families from established references. Fifth: contextual panels and reusable chrome. Sixth: atmosphere/props/state variants bound to actual safe state. Later: expanded NPC population and tactical art once those rules exist.

Accept each asset independently as SOURCE_MASTER_PRESENT, RASTER_PRESENT, INTEGRATED, VERIFIED, CANON_APPROVED or DEFERRED_INTEGRATION; do not compress into one 'finished' flag. Existing batch IDs stay unchanged; new derivatives receive explicit variants/lineage rather than silently stealing old IDs.

Verification must prove engine projection/redaction, typed Kotlin mapping, unchanged opening actors, equipment rig alignment, source/raster synchronization, selection clearing, integer pixel rendering, panel behavior at phone/large-text scale, and save/load continuity. Galaxy A03 visual/performance acceptance remains separate from emulator evidence.
