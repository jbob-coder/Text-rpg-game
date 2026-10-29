# Android text-first UI: visual retirement and dependency audit

**Date:** 2026-10-27 AST. **Repository:** jbob-coder/Text-rpg-game.  
**Authority source examined:** docs/master-game-development-program @ `24b1986e10e5f42b4c14967e9c05a04a3e4e1186`.  
**Status:** proposed code migration in a task branch; review/tests and integration required.

## Owner-required result

A text-choice RPG with an **interactive map** for location discovery/travel. No active pixel sprites, illustrated room scenes, equipment paper-doll, pixel icon catalogs or raster resources. Do not change Python game rules or save format.

## Findings in source

1. `MainActivity.kt` used `TheGamePixelTheme`, which was defined in `PixelTheme.kt`.
2. `GameScreen.kt` owned visible choices, tabs, status, settings, map, navigation, and game text, **but** embedded `SceneIllustration`, `PlayerAvatarPanel`, sprite-derived resources/graphics, `PixelMapArtCatalog`, marker icons and an animated travel overlay.
3. `CharacterSection.kt`, `StatsSection.kt`, `StatusComponents.kt`, `SceneIllustration.kt`, `Pixel*.kt` and `drawable-nodpi/pixel_*.png` made the pixel presentation a real compile/runtime dependency. Original Android tests asserted pixels and screenshot art.
4. `src/textrpg/core.py`, `content.py`, `android_bridge.py` and Android `GameSnapshot.worldMap`/room projection own gameplay and player-visible data. Their logic must remain.
5. Old `docs/VISUAL_BIBLE.md` and `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md` state pixel art is mandatory. They do not document the later owner correction until amended; this is a documentation authority contradiction, not proof the owner changed the game engine.

## Proposed code mapping

| Before | Replacement / disposition |
| --- | --- |
| PixelTheme in Android Activity | Material3 `MaterialTheme` without pixel theme |
| PixelGameShell / StoryScene / SceneIllustration / player avatar | TextGameShell + TextStory; scene text, choices, present actor names, resource values |
| Pixel paper-doll and item decoration | TextCharacter / TextInventory with existing equip/unequip callbacks |
| Illustrated Stats panel | TextStats / inspect-status callback, Python values |
| Pixel quest presentation | TextQuests showing Python quest projections |
| PixelMapArtCatalog + PixelMapMarkerCatalog | simple Compose Canvas lines and node markers, plus accessible text list of locations |
| MapTravelTransitionOverlay | immediate acknowledgement of a successful engine-owned travel transition; **no simulated animation** |
| Asset/test code only supporting removed pixels | delete, replace with text/map smoke and source-gate tests |
| Python GameState, RulesEngine, bridge, persistence | unchanged |

**Retained safeguards:** the same GameSnapshot identifiers, choice IDs, map node IDs, reachability flags, travel callbacks, inventory/equipment callbacks, status-inspection path, save/load controls and narration callbacks.

## Migration risks to verify

- Compiling after mass removal of former pixel source files may reveal additional imports/consumers; Gradle build and instrumentation tests are required.
- A text-only appearance is not proof that gameplay and persistence behave correctly.
- Asset references in historical Markdown and archived evidence are **not active runtime assets**. They remain to explain provenance, visibly superseded by owner correction.
- `GameVisuals` and the Python `visuals.py` validation contract remain in the non-visual data/compatibility layer; removing them requires separate content/schema and bridge migration proof.
- Android UI tests formerly asserting sprites must be rewritten, not silently counted as passing.
- No physical device, emulator, Gradle or Python execution has been performed by this static GitHub revision alone. Do not claim release readiness on that basis.

## Minimum exit checks

1. `PYTHONPATH=src python -m unittest discover -s tests -v` (including text-only source constraints).
2. `gradle -p android testDebugUnitTest --stacktrace`.
3. `gradle -p android :app:assembleDebug --stacktrace`.
4. `gradle -p android connectedDebugAndroidTest --stacktrace` in a supported emulator/device.
5. Manual check: enter game, select a story choice, inspect stats, equip/unequip, save/load, reveal map, select a reachable node and travel; confirm no animated sprite/illustration/pixel asset appears.
6. Confirm PR diff contains no changes to Python core rules, authored content, or save schema.

## Historical authority boundary

Superseded: `docs/VISUAL_BIBLE.md`, `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md` and their older asset production derivatives as active product requirements. The current owner decision log `docs/GAME_CONTEXT_LOGS/2026-10-27_TEXT_MAP_VISUAL_RETIREMENT.md` wins for visual design. Preserve their old content for audit/history only, not as instructions to recreate art.
