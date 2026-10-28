# THE GAME — Visible People / Room Actor Coverage Audit

Date: 2026-10-27 AST  
Status: SOURCE-VERIFIED CROSSWALK; **not** an executed Android/render/device acceptance  
Repository: `jbob-coder/Text-rpg-game`  
Authority source HEAD read before branch creation: `dac5d22cdbe211d0d35d3df98b542be2653f1b85`  
Working branch: `audit/visual-people-coverage-20261027`  
Related task: D-006 existing-state audit; supplements, does not replace, the existing deep audit or master task register.

## Goal and non-goals

Make every *authored and player-visible* person eligible for consistent display without assuming that all narrated or defined people are physically present in a scene. Reuse the current engine-to-Android visual projection; do not add actors from prose, raw NPC records, historical projects, new story content, generic placeholder sprites or hidden player state.

This is a coverage and regression guard, **not** a claim of final art, complete NPC simulation, expanded canon, animation or release approval.

## Verified current source chain

1. `content/vertical_slice_01_room_presence.json` explicitly authors visible people per scene. `src/textrpg/content.py::_apply_room_presence_sidecar` merges it into scene definitions when `load_content_pack` is used.
2. `src/textrpg/room_projection.py::build_room_projection` builds a detached, versioned, player-safe list; it forbids internal NPC data, unsupported fields, duplicate presentation IDs and presentation coordinates.
3. `src/textrpg/android_bridge.py::AndroidGameSession._room_view_for` projects `room`; map-only travel to a different location clears stale people instead of showing them elsewhere.
4. Android `GameSnapshot.room.actors` reaches both `SceneIllustration` call sites in `GameScreen.kt`.
5. `PixelStoryActorCatalog.kt` resolves the projected `visualFamily` into an authored 32×48 sprite; `PixelStoryActorPlacementResolver.kt` translates a semantic placement key into visual coordinates. Unknown families/keys are deliberately skipped; they must not be replaced with invented presence.

## Exact authored coverage at the audited source

`content/vertical_slice_01.json`: 19 scene records, 1 character-visual definition (`NPC_TAMSIN`) and 1 durable initial-state NPC (`NPC_TAMSIN`). **This does not mean other people are forbidden in future content.**

`content/vertical_slice_01_room_presence.json`: 4 scenes with 5 authored visible-person entries, representing **2 unique presentation IDs**.

| Scene | Location | Authored visible people | Supported pixel families and semantic placement |
| --- | --- | --- | --- |
| `OPENING_DEPOT_BLACKOUT` | `PLATFORM_NINE` | Tamsin; wounded courier | `NPC_TAMSIN` / `PLATFORM_NINE_TAMSIN_RIGHT`; `SUPPORT_WOUNDED_COURIER` / `PLATFORM_NINE_COURIER_LEFT` |
| `OPENING_DECISION` | `PLATFORM_NINE` | Tamsin | `NPC_TAMSIN` / `PLATFORM_NINE_TAMSIN_RIGHT` |
| `OPENING_RECOVERY` | `RELAY_WORKBENCH` | Tamsin | `NPC_TAMSIN` / `RELAY_WORKBENCH_TAMSIN_RIGHT` |
| `OPENING_TUNNEL` | `SERVICE_TUNNEL` | Tamsin | `NPC_TAMSIN` / `SERVICE_TUNNEL_TAMSIN_RIGHT` |

Both projected families and all four referenced placement keys have Android source mappings. No unsupported family or placement was found in those five entries.

Other scenes without explicit room presence must not receive invented people. `NPC_MARA` appears as a reference in the separate `content/sample_scene.json` example; that reference does **not** establish a playable Android sprite or presence in `vertical_slice_01`. The player is shown in `PlayerAvatarPanel` in the wider story layout and is not part of the room NPC sprite catalog.

## Change introduced by this bounded audit

Added `tests/test_room_actor_visual_source_coverage.py`. Its source contract test reads the current content sidecar and Kotlin mapping files to reject:
- authored room-presence scene IDs absent from the main content pack;
- duplicate presentation IDs within one authored scene;
- visible persons whose `visual_family` is not mapped to an Android sprite;
- visible persons whose `placement_key` is not mapped to an Android presentation point.

**Verification status:** an equivalent static source cross-check was performed on five entries and returned zero missing family/placement mappings; the new Python test itself and the full Python/Android test suites have **not** been executed for this branch. This guard is intentionally source-level and cannot prove APK packaging, actual rendering, z-order/occlusion or physical device results.

## Practical visual policy / next gates

1. **Use every explicitly present person**, not merely a hardcoded chosen subset. Projected presence is authoritative; an NPC record, narrative mention, sample/demo file or map location alone never makes a person visible.
2. **Preserve individual identity:** existing approved shape, palette, pose and equipment conventions apply per person. Do not clone Jack/Tamsin into generic people or invent visual designs for identities lacking approved assets.
3. **One visual implementation per family:** reuse `PixelStoryActorCatalog`, `PixelStoryActorPlacementResolver` and scene composition layers; do not create competing scene-based actor inference.
4. **Add future people in one bounded, traceable sequence:** establish player-safe authored scene presence; approve/produce matching identity art and placement mappings; run this guard plus Python/Android unit tests; inspect responsive screenshots and occlusion; verify on device before claiming release readiness.
5. **Keep separate completion labels:** authored != catalog-mapped != rendered in APK != visually accepted. The final two labels remain unverified here.
6. **No unrelated changes:** no new scenes, people, mechanics, movement animation, invented physics/light behavior or canon promotion were made in this patch.

To run the focused static coverage test from the repository root:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p 'test_room_actor_visual_source_coverage.py' -v
```

Follow with the full Python and Android test gates under their existing build instructions. Do not interpret an unexecuted command as a passing test.
