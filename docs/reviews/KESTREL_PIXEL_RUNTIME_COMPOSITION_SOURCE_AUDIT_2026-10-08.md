# Kestrel — pixel runtime composition source audit (2026-10-08 AST)

**Disposition:** NON-OWNING / DOCUMENTATION REVIEW / NOT A BULLETIN CLAIM.  
**Observed authority HEAD:** `399451f6ccfff566b9b00cf49aabb016738f452a`.  
**Reviewer/session:** PLAYER_KESTREL / `SESSION_KESTREL_20261008T1752-0400_S02`.  
**Evidence type:** live GitHub file reads and source/test inspection only. **Tests executed in this review: none.** No screenshots, emulator, handset or APK evidence produced.

## 1. Governing authority and non-overlap

- `docs/VISUAL_BIBLE.md` (source blob `0e57a4a0`) owns the pixel visual language, identity coherence and acceptance principles. It now explicitly defers asset-grid/provenance rules to `docs/assets/PIXEL_ASSET_MASTER_PLAN.md` and runtime ordering to `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`.
- `docs/assets/PIXEL_ASSET_MASTER_PLAN.md` (blob `f6e98721`) specifies 128x64 scene masters, 32x48 character art and native-pixel/nearest-neighbor requirements. The approved Jack visual reference is a *reference*, not proof of a production sprite.
- `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md` (blob `ad37b656`) describes a **target 15-stage composition stack**, actor identity/art bounds, R0–R5 reuse/occlusion and visual QA.
- `docs/assets/ROOM_COMPOSITION_IMPLEMENTATION_CONTRACT.md` (blob `883af809`) already recognizes D-064 room-actor projection as implemented, while contextual portrait/focus panels, wider actor coverage and occlusion data remain work to be proved.
- This packet is an observed implementation-to-contract crosswalk. It does **not** create a new visual authority, grant a task, alter the state schema, authorize hidden information, or claim D-072/D-073/D-074 ownership.

## 2. Current rendered composition (source-backed)

`android/app/src/main/java/com/thegame/rpg/ui/SceneIllustration.kt` (blob `011a1819`) presently draws the source-native 128x64 scene or preferred raster, then state overlays selected from scene/relay projection, then environment decals, environment props, projected room actors, centered Trace FX and finally a Relay Workbench-specific relay-state sprite. These are **draw-call order**, not declared per-object foreground/background occlusion bands. If `PixelSceneCatalog.scene(locationId)` has no match, this component falls back to 64x32 procedural room geometry; the fallback is non-character migration art, not a source-native replacement.

The nine named location raster bindings come from `PixelRasterCatalog.scene(locationId)` (blob `6bfc11c8`), and `rememberPixelRaster` preferentially decodes them. `drawPixelRaster` uses `FilterQuality.None` and rounded destination bounds. Thus a Kotlin scene-master edit does not establish that the shipped visible PNG changed; source/raster correspondence and actual render screenshots must be verified separately.

`PixelStoryActorCatalog.placements(roomActors)` (blob `ef559b12`) accepts the already projected `List<GameRoomActor>`, maps only visual families `NPC_TAMSIN` and `SUPPORT_WOUNDED_COURIER` to authored 32x48 `PixelSprite` objects, resolves known semantic placement keys and skips unknown family/key pairs. No presence inference from raw scene flags occurs in this mapping. `PixelStoryActorPlacementResolver.kt` (blob `00fd8e5a`) provides four static presentation slots: courier 34,13; Platform Nine Tamsin 62,14; Relay Workbench Tamsin 90,14; Service Tunnel Tamsin 76,14. They are **sprite origins**, not world coordinates or ground pivots.

`GameScreen.kt` (blob `1705536c`) wires `snapshot.room.actors` to **both** `SceneIllustration` call sites. In the larger header layout the player's avatar is shown in a **separate `PlayerAvatarPanel`**, rather than being inserted as a room-actor layer. This distinction is consistent with the current bounded opening UI but does not establish the target shared room-depth model, selectable actor panels or in-scene player occlusion.

## 3. Observed implementation versus target

| Contract concern | Source-observed state | What is *not* established |
| --- | --- | --- |
| Room actor presence | D-064 player-safe projection reaches both scene consumers; unknown family/key is skipped | General NPC positions, schedules, all population or arbitrary tactical contacts |
| Room stack | Ordered source/raster -> overlays -> decals -> props -> actors -> Trace FX -> relay sprite | Declarative per-instance z-bands, actor/prop interleaving, foreground occlusion masks, depth-tested overlap |
| Scene delivery | Nine raster bindings with source-native `PixelSprite` fallback; no smooth raster filtering | Current raster/source pixel equivalence on this review HEAD or new-art visible delivery |
| Identity and outfit | Two authored room actor visual families; standalone avatar equipment panel | Expanded actor poses/outfit layers in the room, visible wound variants or selectable portraits |
| Focus/interaction | Existing narrative choices and actor inspectability information are separate concerns | Approved actor-specific contextual focus-panel state/action model |
| Motion | Scene-specific Trace FX repeats with a `delay(180L)` effect | Reduced-motion gating or final Galaxy A03 frame/power behavior in the scene renderer |
| State ownership | Scene/relay projected display fields and projected room actors select art | Any permission for UI to infer hidden NPC identity, combat occupancy, quest prerequisites or interaction legality |

**Important:** The apparent absence of z-band, focus-panel and reduced-motion handling from this composable is a *bounded source observation*, not proof of a runtime regression. The governing documents already classify several of these as future expansion. Do not file a duplicate CPR without an executable failure or a new cross-system causal defect.

## 4. Existing automated checks examined

- `android/app/src/test/java/com/thegame/rpg/ui/PixelStoryActorCatalogTest.kt` verifies authored actor dimensions/palette, chosen silhouette cues, projected-only presence, four opening placements and unknown-family/placement failure closed.
- `android/app/src/test/java/com/thegame/rpg/ui/PixelStoryActorPlacementResolverTest.kt` verifies four semantic slot coordinates and unknown-key rejection.
- `android/app/src/test/java/com/thegame/rpg/ui/PixelRasterCatalogTest.kt` verifies raster **mapping existence** for nine scenes/current loadout; it is not source-versus-PNG pixel equality or on-device visual verification.
- `tests/test_d064_android_scene_projection_source.py` statically asserts that both `GameScreen` scene call sites forward projected actors and that `SceneIllustration` uses the actor projection. This does not verify final pixel overlap, order or hit targets.

These checks were **read**, not executed in this review. Historical D-064/asset CI evidence remains historical and must not be represented as a fresh exact-HEAD test run.

## 5. Bounded future acceptance work (not new tasks)

**R-01 — Define truthful layer cases before redesign.** For each named Gate Twelve opening location, record whether a projected actor may stand behind a fixed prop, in front of it, or be masked by architecture. Compare intended per-area band ordering to existing draw-call order; defer new z/occlusion APIs until a real accepted consumer/fixture requires them. No engine tactical coordinate should be substituted for `placement_key` (OR-010).

**R-02 — Protect renderer input invariants.** Assert actors not projected to a viewer never appear in sprite placement or focus UI, including stale last-known tactical contacts (a contact is not necessarily a room actor). Check unknown family/key remains a safe absence and no hidden name/diagnosis/faction state leaks via variant selection.

**R-03 — Visual-delivery parity.** Pair changed `PixelSceneCatalog` masters with preferred `drawable-nodpi` PNG hash/equality evidence and a named-location screenshot. A source-only green unit test is insufficient to claim visible pixels changed.

**R-04 — Measure accessibility/motion.** Test 320dp layouts, larger system text, a motion-reduction configuration, and rapid scene transitions. Trace-FX animation loop is present; whether a user-visible reduced-motion control exists here is unverified. Compare actual screenshot and frame behavior separately in emulator and Galaxy A03; do not fabricate handset results.

**R-05 — Keep missing art truthful.** Missing portrait, equipment variant, or character family should not trigger a false identity or synthesized geometry. Retain game/equipment state, report missing asset provenance, and use only approved missing-art handling.

**R-06 — Preserve dependency boundaries.** D-072 is Silex-owned; D-073 and D-074 were BLOCKED on the inspected Bulletin. These findings can inform a future authorized D-074 visual consumer or separately published asset task, but neither is authorized by this review.

## 6. Review exit state

- Current live Bulletin recheck at observed HEAD: zero unclaimed ranked READY tasks; D-072 IN_PROGRESS/Silex; D-073/D-074 BLOCKED; other downstream ranked tasks BLOCKED.
- Review status: **DOCUMENTED, UNCLAIMED, NO CODE/TEST/CANON CHANGE**.
- The next player must refetch HEAD, Bulletin, source blobs, and owner decisions before treating any line of this packet as a still-current implementation state.
