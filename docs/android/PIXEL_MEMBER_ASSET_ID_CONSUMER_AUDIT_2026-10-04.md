# THE GAME — Pixel Member / Asset-ID Consumer Audit — 2026-10-04

Status: **ACTIVE / D-026 MEMBER-LEVEL ZERO-CONSUMER PASS COMPLETE**  
Repository: `jbob-coder/Text-rpg-game`  
Branch: `docs/master-game-development-program`  
Audited source HEAD: `b79185fd673ff7838ef1b8f2814d1459230052fb`

Machine-readable companion:

`docs/evidence/pixel_member_consumer_audit_2026-10-04.json`

## 1. Purpose

This closes the next deletion-safety layer after the file-level pixel-catalog audit.

The question is no longer:

> “Is the catalog file used?”

The question is:

> “Which individual current visual IDs/members have a current production consumer path, and which do not?”

This pass audits the top-level ID constants in the current Android pixel presentation sources and separately checks the generated Trace-strain portrait-frame family.

A generic runtime lookup counts as a current consumer path even when a particular authored playthrough may not activate every variant. That distinction prevents valid contract-reserved assets from being mislabeled as dead code.

## 2. Audited ID surface

Current top-level ID-like constants inspected:

- **110 total**;
- **109 visual asset IDs**;
- **1 non-visual condition trigger ID**: `COND_ECHO_STRAIN`.

Family counts:

| Source family | Top-level IDs |
| --- | ---: |
| PixelAssetCatalog | 15 |
| PixelCharacterStagingCatalog | 1 |
| PixelEnvironmentDecalCatalog | 2 |
| PixelEnvironmentModuleCatalog | 4 |
| PixelEnvironmentOverlayCatalog | 2 |
| PixelEnvironmentPropCatalog | 10 |
| PixelEquipmentSlotCatalog | 12 |
| PixelItemQualityFrameCatalog | 2 |
| PixelMapArtCatalog | 1 |
| PixelMapMarkerCatalog | 5 |
| PixelMapTravelTransition | 1 |
| PixelSceneCatalog | 9 |
| PixelSceneOverlayCatalog | 5 |
| PixelStoryActorCatalog | 2 |
| PixelTraceFxCatalog | 3 |
| PixelTraceStrainCatalog visual family ID | 1 |
| PixelTraceStrainCatalog condition trigger | 1 |
| PixelUiChromeCatalog | 17 |
| PixelUiIconCatalog | 15 |
| PixelUiUtilityCatalog | 2 |

Generated frame IDs are subordinate to these families and are not double-counted as top-level constants.

## 3. Confirmed top-level visual IDs with no current production consumer

Exactly three current top-level visual IDs were not found on a current production lookup/render path.

| Asset ID | Source | Current classification | Disposition |
| --- | --- | --- | --- |
| `MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS` | PixelEnvironmentModuleCatalog | **PRODUCED_DEFERRED_INTEGRATION** | **KEEP** provenance/source; optional PR #28 composition remains deferred |
| `UI_CHOICE_CARD_SELECTED` | PixelUiChromeCatalog | **NO CURRENT PRODUCTION REFERENCE FOUND** | **KEEP RESERVED** pending final choice-selection UX |
| `UI_BUTTON_DANGER` | PixelUiChromeCatalog | **NO CURRENT PRODUCTION REFERENCE FOUND** | **KEEP RESERVED** pending final destructive/danger-action UX |

Important:

**No deletion is authorized by this result.**

A zero-current-consumer result is evidence for later teardown analysis, not automatic permission to remove the member.

## 4. Generated member family with no current production consumer

`PixelTraceStrainCatalog` currently creates:

- four avatar strain frames;
- four portrait strain frames.

Current production path:

`conditions -> PixelTraceStrainCatalog.avatarForConditions -> PixelComponents / player avatar`

No current production call to:

`PixelTraceStrainCatalog.portraitForConditions`

was found in the audited source.

Therefore:

`FX_TRACE_STRAIN_PORTRAIT_FRAME_1..4`

are classified:

**GENERATED / SOURCE PRESENT / NO CURRENT PRODUCTION CONSUMER / KEEP DEFERRED FOR FUTURE PORTRAIT SURFACE**

This is consistent with the still-missing final Jack/Tamsin/courier portrait work. Do not delete these merely to reduce current code size.

## 5. Contract-reachable families that are not zero-consumer

### Panel chrome

All eight `PixelPanelChrome` panel kinds are used across current production surfaces:

- STORY;
- CHARACTER;
- STATS;
- INVENTORY;
- QUEST;
- MAP;
- SETTINGS;
- DEVELOPER;
- MODAL is used by Character detail/modal presentation.

The panel frame members are therefore not zero-consumer even when the individual frame field is reached indirectly through `PixelUiChromeCatalog.panel(kind)`.

### Choice/button chrome

Current production direct paths exist for:

- `choiceEnabled`;
- `choiceDisabled`;
- `buttonPrimary`;
- `buttonSecondary`;
- `tabActive`;
- `tabInactive`.

No current production path was found for:
- `choiceSelected`;
- `buttonDanger`.

### Map markers

Current map rendering uses:

- `discoveredMarker` directly;
- `playerMarker` directly for the current node;
- `currentMarker`, `reachableMarker`, and `unavailableMarker` through `stateOverlay(current, reachable)`.

All five are current consumer-reachable.

### Equipment slots

All 12 equipment-slot assets are returned by the active `slot(slotId)` lookup:

- head;
- body;
- hands;
- legs;
- feet;
- main hand;
- off hand;
- ring 1;
- ring 2;
- neck;
- accessory 1;
- accessory 2.

The current Character/Inventory surfaces call this lookup from projected slot IDs. These members are contract-reachable and must not be removed because a particular current loadout happens to leave a slot empty.

### Item quality

The active lookup supports:

- standard;
- uncommon.

Current authored item content includes both qualities, so both current quality-frame assets are content-reachable.

### Scenes

All nine current scene masters:
- have an active scene lookup;
- have a current raster/source delivery path;
- correspond to current authored world locations.

Their 24-raster consumer audit is owned by:

`docs/assets/CURRENT_ASSET_CONSUMER_ZERO_CONSUMER_AUDIT_2026-10-04.md`

### Scene overlays

All five current scene-overlay members are returned by either:

- `forScene(sceneId)`; or
- `forVisualState(locationId, relayState)`.

They remain current contract-reachable presentation layers.

### Story actors

Both current story actor masters:
- `NPC_TAMSIN_TURNAROUND`;
- `SUPPORT_COURIER_01`;

are returned by current `sceneId + locationId` placement rules.

They remain consumed, but the presence-selection mechanism is transitional and must migrate toward D-030's player-safe actor projection.

### Trace FX

Current SceneIllustration consumes:
- general Trace Echo frames through `forScene`;
- signal-pulse frames through `signalPulseForScene`;
- directional Trace frames through `directionalTraceForScene`.

These are not zero-consumer.

### UI icons

Current UI calls the active mappings for:
- navigation icons;
- resources;
- quest categories.

The icon family is therefore contract-reachable.

This audit does not claim every quest category or resource variant appears in every playthrough.

### UI utilities

Both current utility assets are directly consumed:
- scroll marker;
- narration icon.

### 5.1 Post-D-064 story actor consumer correction — 2026-10-08

**History versus current:** The "Story actors" paragraph in section 5 is accurate for this audit's original October-04 source HEAD; the `sceneId + locationId` presence rule was subsequently replaced by completed D-064. Current authority inspection at `247b1305461194ba97a06e9ae652409c0b242ee9` confirms `PixelStoryActorCatalog.placements(actors: List<GameRoomActor>)` now consumes only player-safe projected room actors passed by `SceneIllustration`, not hardcoded scene/location combinations. `visualFamily` selects art, `placementKey` resolves presentation coordinates via `PixelStoryActorPlacementResolver`; unknown values produce no placement.

Both `NPC_TAMSIN_TURNAROUND` and `SUPPORT_COURIER_01` remain production-consumed; **their top-level non-zero-consumer classification is unchanged**. The original 109-ID/three zero-consumer/four generated portrait-frame counts remain historical audit results, not a new recount at this HEAD. [D-064 executed evidence](../evidence/D064_PLAYER_SAFE_ROOM_ACTOR_PROJECTION_FINAL_2026-10-05.md) confirms historical integration and tests. Source readback only in this addendum; no new build/test pass or asset removal. D-030 contextual actor panels/interaction remain open independently from implemented room-presence mapping.

## 6. Environment members

Current production location/scene placement rules consume the environment decal and prop members.

The three 128x64 arrival-preview modules remain integrated.

The infrastructure tile atlas is intentionally the exception:

`MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS = PRODUCED_DEFERRED_INTEGRATION`

PR #28 proves one optional composition use, but that behavior is not current runtime authority.

## 7. Deletion-safety conclusion

Current member-level findings:

- current visual top-level IDs audited: **109**;
- top-level visual IDs with no current production consumer: **3**;
- generated Trace-strain portrait frames with no current production consumer: **4**;
- deletion-authorized visual members: **0**.

The three top-level zero-current-consumer IDs and four portrait frames should be carried into final teardown analysis as explicit candidates/reserved assets, not silently deleted.

Before any future REMOVE decision, require:

1. final UX/system decision;
2. provenance record;
3. replacement/no-longer-needed rationale;
4. search for runtime and test consumers;
5. migration/rollback impact;
6. destination-head build/tests;
7. visual evidence when applicable.

## 8. D-026 / D-021 effect

This closes the current **member/asset-ID level zero-consumer matrix** requested by D-026/D-021.

Remaining Android reconstruction work is no longer basic current pixel-member discovery.

Still open:

- D-030 actor/room projection implementation migration map;
- future activity projection;
- tactical-combat projection;
- hierarchical world-map projection;
- persistent-adversary intel projection;
- final destination APK component migration map;
- exact-head runtime/build execution after implementation changes.

## 9. Verification boundary

No Kotlin, Python, raster, content, save or runtime file was changed.

No tests/builds were executed.

This is a static source-consumer audit at the recorded exact source HEAD.
