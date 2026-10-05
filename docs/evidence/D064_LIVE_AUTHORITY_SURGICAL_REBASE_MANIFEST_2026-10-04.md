# D-064 — Live-Authority Surgical Rebase Manifest

**Status:** READY FOR KESTREL EXECUTION  
**Owner:** Kestrel  
**Overseer:** AXIOM  
**Observed authority HEAD:** `16b6b1830d4d2b6752d281890f65ae594c932963`  
**Historical green branch:** PR #63 head `c8268ea25a79eed0631d22a7a70e625f022c38d3`, run #354 / `37257967729` — fully green but stale/diverged.  
**RED evidence branch:** PR #68 head `5565a83415b9251ecf4fdf3e494e8c08ecd40299`, run #355 / `37258411701` — intentionally red against old production contract.

## Goal

Recreate only the D-064 projected-room-actor presentation migration on top of the live authority branch.

Do **not** transplant the large formatting/compaction churn from PR #63.

The final integration should be easy to review because every changed production line should be directly connected to projected actor authority.

## Live-authority source anchors

At this manifest's observed authority:

- `GameScreen.kt` SHA: `6b6af3ad19a5ca755b11b2748bacedd29f347866`
- `SceneIllustration.kt` SHA: `619c9cf5f6610f9ab9e118b8cab3ab3a875031f4`
- `PixelStoryActorCatalog.kt` SHA: `8714a2f1aa5aed497bd6a71f3d50acc0ac980783`
- `PixelStoryActorCatalogTest.kt` SHA: `314fb71166ff7f2088022dcf9e54c9be5b5e86fe`
- `GameEngine.kt` already contains `GameRoomActor`; no model change is required.

Re-fetch all of these before editing.

## Production change 1 — GameScreen.kt

There are two `SceneIllustration(...)` callsites.

At both callsites add only:

```kotlin
roomActors = snapshot.room.actors,
```

Do not alter the surrounding layout, spacing, dimensions, or unrelated presentation code.

## Production change 2 — SceneIllustration.kt

Add:

```kotlin
import com.thegame.rpg.engine.GameRoomActor
```

Extend the function signature only:

```kotlin
fun SceneIllustration(
    locationId: String,
    sceneId: String? = null,
    relayState: String? = null,
    roomActors: List<GameRoomActor> = emptyList(),
    modifier: Modifier = Modifier,
)
```

Replace only the old actor-presence lookup:

```kotlin
PixelStoryActorCatalog.placements(
    locationId = locationId,
    sceneId = sceneId,
)
```

with:

```kotlin
PixelStoryActorCatalog.placements(roomActors)
```

Do **not** compact or reformat the rest of `SceneIllustration.kt`. Preserve the existing raster, overlay, prop, FX, relay and fallback-scene code byte-for-byte where practical.

## Production change 3 — PixelStoryActorCatalog.kt

Add:

```kotlin
import com.thegame.rpg.engine.GameRoomActor
```

Preserve the current sprite definitions, comments, palettes and formatting.

Replace only the current scene/location-based `placements(locationId, sceneId)` function with:

```kotlin
private fun spriteFor(actor: GameRoomActor): PixelSprite? = when (actor.visualFamily) {
    "NPC_TAMSIN" -> tamsinFront
    "SUPPORT_WOUNDED_COURIER" -> woundedCourier
    else -> null
}

fun placements(actors: List<GameRoomActor>): List<PixelStoryActorPlacement> =
    actors.mapNotNull { actor ->
        val sprite = spriteFor(actor) ?: return@mapNotNull null
        val point = PixelStoryActorPlacementResolver.resolve(actor.placementKey)
            ?: return@mapNotNull null
        PixelStoryActorPlacement(
            sprite = sprite,
            x = point.x,
            y = point.y,
        )
    }
```

Contract:
- presence comes only from projected `room.actors`;
- visual selection comes only from player-safe `visualFamily`;
- coordinates come only from semantic `placementKey`;
- unknown visual families or placement keys render nothing;
- the catalog must not infer presence from scene/location IDs.

## Test change 1 — PixelStoryActorCatalogTest.kt

Import `GameRoomActor` and replace the old scene/location presence test with projected-actor fixtures.

Use a helper equivalent to:

```kotlin
private fun actor(
    presentationId: String,
    visualFamily: String,
    placementKey: String,
) = GameRoomActor(
    presentationId = presentationId,
    knownActorId = null,
    displayName = presentationId,
    visualFamily = visualFamily,
    placementKey = placementKey,
    poseKey = null,
    outfitKey = null,
    visibleTags = emptyList(),
    inspectable = false,
    dialogueAvailable = false,
    actions = emptyList(),
)
```

Required cases:

1. opening courier + Tamsin:
   - `SUPPORT_WOUNDED_COURIER` / `PLATFORM_NINE_COURIER_LEFT` -> `34,13`
   - `NPC_TAMSIN` / `PLATFORM_NINE_TAMSIN_RIGHT` -> `62,14`

2. relay:
   - `NPC_TAMSIN` / `RELAY_WORKBENCH_TAMSIN_RIGHT` -> `90,14`

3. tunnel:
   - `NPC_TAMSIN` / `SERVICE_TUNNEL_TAMSIN_RIGHT` -> `76,14`

4. empty projected actor list -> no story actors.

5. unknown `visualFamily` -> omitted.

6. unknown `placementKey` -> omitted.

PR #68 is useful RED evidence for these expectations, but do not merge the RED-only branch.

## Test change 2 — source-contract regression

Add/port:

`tests/test_d064_android_scene_projection_source.py`

It should prove:

- `SceneIllustration` accepts `roomActors: List<GameRoomActor>`;
- story actors are rendered through `PixelStoryActorCatalog.placements(roomActors)`;
- the old location/scene actor-presence call is absent;
- both `SceneIllustration` callsites in `GameScreen.kt` pass `snapshot.room.actors`;
- existing fallback scene IDs remain present.

Keep this as a source-contract regression only; do not use it to replace Kotlin/runtime tests.

## Do not carry forward

From PR #63, do **not** carry:

- one-line compaction of `SceneIllustration.kt`;
- one-line compaction of sprite palettes/rect calls;
- deletion of descriptive sprite comments;
- unrelated formatting changes;
- fallback scene rendering rewrites;
- any visual/art change not necessary for projected actor authority.

Those changes increase merge risk without contributing to D-064 acceptance.

## Final branch workflow

1. fetch live authority HEAD;
2. create a fresh short-lived D-064 integration branch from that HEAD;
3. apply only the five-file surgical delta above;
4. include/port the focused source-contract test;
5. run local focused tests when available;
6. open/update PR against `docs/master-game-development-program`;
7. require merge-state CI:
   - Python;
   - Android unit/build/package;
   - emulator smoke/screenshots;
8. if CI is green, write D-064 evidence and Next Player Learning Record;
9. append Coordination Room `FINISH`;
10. mark D-064 DONE;
11. AXIOM/Veyra may then unlock/claim D-069.

## Acceptance reminder

PR #63's green run proves the migration concept works.

It does **not** prove current merge-state compatibility because the branch diverged from authority.

The final proof must come from a fresh current-authority branch/PR with the minimal delta above.
