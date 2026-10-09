# Gate Twelve / Batch 001 — Asset Status & Production Matrix

Status: **ACTIVE AUDIT / STEP 7 SOURCE OF TRUTH FOR ASSET DECOMPOSITION**  
Parent region plan: `GATE_TWELVE_REGION_MASTER_PLAN.md`  
Parent visual contract: `PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`  
Audited branch: `docs/master-game-development-program`

---

# 1. Purpose

This matrix answers three different questions that must not be conflated:

1. **Was an asset planned?**
2. **Does an exact stable ID currently exist in audited visual catalogs/manifests?**
3. **Is the visual actually final/canon-reviewed?**

An `INTEGRATED` manifest state means the visual has a runtime binding on the exact recorded implementation line. It does **not** mean native-scale art review, Android-scale art review, palette approval, physical handset QA, or final canon approval have all occurred.

Open draft PR refinements are evidence of later work, not automatically promoted authority.

---

# 2. Audit inputs

Audited:
- Batch 001 catalog, units 001–100;
- Wave A/B/C manifests;
- current visual catalogs on this branch;
- current Gate Twelve geometry and composition standards;
- open refinement lines PR #22, #27, #28, #30 and the actor work inherited from the stacked branch line;
- approved Jack reference record reconciled from PR #22.

Exact-ID presence is deliberately conservative. If an exact planned ID is absent, that does not prove an equivalent visual does not exist under another ID. It means **audit before producing a duplicate**.

---

# 3. Region-level assets outside the 001–100 unit list

## `MAP_GATE_TWELVE_DISTRICT_BASE`

Stage:
- code-present in `PixelMapArtCatalog.kt`;
- 256x144 native presentation master;
- geometry locked as the current production scaffold in Region Master Plan Step 5;
- authored node/edge state remains external to the art.

Action:
- refine through material/landmark modules rather than redesigning the whole district;
- preserve node/hit-test projection.

## Room actor runtime

Current verified D-064 system:
- Python player-safe room projection owns actor presence;
- Android maps typed room-actor records;
- `PixelStoryActorCatalog` remains the presentation placement/art resolver;
- Tamsin and the injured courier retain opening-equivalence placements through semantic placement keys;
- scene/location IDs no longer decide story-actor presence.

Action:
- preserve the D-064 privacy/presence boundary;
- expand authored actor/pose/outfit/held-prop coverage only from projected player-safe state;
- contextual focus panels remain later presentation work and must not recreate hidden-state or scene/location presence inference.

## Ambient animation runtime

Open PR #31 contains Service Tunnel ambient-infrastructure animation work.

Stage:
- open draft implementation line;
- not silently promoted into this branch;
- must be evaluated against `GATE_TWELVE_MAP_ANIMATION_BLUEPRINT.md` and exact-head QA before canonicalization.

---

# 4. Full Batch 001 stage matrix

| # | Stable asset | Family | Native | Audited current stage | QA / next evidence |\n| ---: | --- | --- | --- | --- | --- |\n| 001 | `PLAYER_BODYFRAME_A_TURNAROUND` | Character | 1024+ reference -> 32x48 masters | BRIEF_LOCKED / technical | six_view_consistency=false, proportion_contract_reviewed=false, native_scale_reviewed=false; approved Jack Character-tab reference exists; six-view technical turnaround still needs construction/review. |\n| 002 | `PLAYER_GAMEPLAY_FRONT_BASE` | Character | 32x48 | INTEGRATED / technical | native_scale_reviewed=false, android_scale_reviewed=false, anchor_alignment_reviewed=false, palette_reviewed=false, state_binding_reviewed=true; PR #22 carries a later player-raster/silhouette refinement and Jack-reference alignment; that later runtime head is not silently promoted here. |\n| 003 | `PLAYER_GAMEPLAY_LEFT_PROFILE_BASE` | Character | 32x48 | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 004 | `PLAYER_GAMEPLAY_RIGHT_PROFILE_BASE` | Character | 32x48 | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 005 | `PLAYER_GAMEPLAY_BACK_BASE` | Character | 32x48 | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 006 | `PLAYER_IDLE_SHEET` | Animation | 32x48 x 4 frames | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 007 | `PLAYER_WALK_SHEET` | Animation | 32x48 x 6 frames/direction | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 008 | `PLAYER_RUN_SHEET` | Animation | 32x48 x 8 frames/direction | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 009 | `PLAYER_CROUCH_SHEET` | Animation | 32x48, 6 transition/loop frames | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 010 | `PLAYER_INTERACT_TOOL_SHEET` | Animation | 32x48, 4-6 frames | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 011 | `PLAYER_HURT_RECOVER_SHEET` | Animation | 32x48, 3-4 frames | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 012 | `PLAYER_TRACE_ACTIVATION_SHEET` | Animation | 32x48, 6-8 frames | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 013 | `PLAYER_PORTRAIT_NEUTRAL` | Portrait | 64x64 | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 014 | `PLAYER_PORTRAIT_EMOTION_TEMPLATES` | Portrait | 64x64 set | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 015 | `PLAYER_HAIR_LAYER_KIT_A` | Character layer | 32x48 + 64x64 portrait companion | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 016 | `PLAYER_FACE_SKIN_PALETTE_KIT_A` | Character layer | 32x48 + 64x64 | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 017 | `PLAYER_VISIBLE_STATUS_OVERLAYS` | Character overlay | 32x48 | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 018 | `NPC_TAMSIN_TURNAROUND` | Character | 1024+ reference -> 32x48 masters | BRIEF_LOCKED / provisional | six_view_consistency=false, identity_reviewed=false, asymmetry_reviewed=false; A front Tamsin room actor exists in current code under this stable ID, while Wave A still describes the full six-view turnaround as BRIEF_LOCKED. Reconcile manifest scope before calling the turnaround complete. |\n| 019 | `NPC_TAMSIN_PORTRAIT_EMOTIONS` | Portrait | 64x64 x 5 | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 020 | `NPC_TAMSIN_DIAGNOSTIC_POSE` | Character pose | 32x48 + 64x64 reference | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 021 | `ITEM_DEPOT_JACKET_ICON` | Item icon | 32x32 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 022 | `ITEM_DEPOT_JACKET_PAPERDOLL` | Equipment layer | 32x48 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, anchor_alignment_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 023 | `ITEM_WORK_GLOVES_ICON` | Item icon | 32x32 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 024 | `ITEM_WORK_GLOVES_PAPERDOLL` | Equipment layer | 32x48 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 025 | `ITEM_SIGNAL_RING_ICON` | Item icon | 32x32 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 026 | `ITEM_SIGNAL_RING_PAPERDOLL` | Equipment micro-layer | 32x48 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 027 | `ITEM_COURIER_NECKTAG_ICON` | Item icon | 32x32 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 028 | `ITEM_COURIER_NECKTAG_PAPERDOLL` | Equipment layer | 32x48 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 029 | `ITEM_MAINTENANCE_SEAL_ICON` | Item icon | 32x32 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 030 | `ITEM_DEAD_RELAY_INTACT` | Item/prop | 32x32 icon + 64x64 close-up | INTEGRATION NAMING DRIFT — Wave B manifest/runtime uses `ITEM_DEAD_RELAY_ICON`; catalog plans `ITEM_DEAD_RELAY_INTACT`. Reconcile ID/alias before new production. | not recorded in audited manifests |\n| 031 | `ITEM_DEAD_RELAY_OPENED` | Prop state | 64x64 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 032 | `ITEM_DEAD_RELAY_DAMAGED` | Prop state | 64x64 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 033 | `ITEM_DEAD_RELAY_SIGNAL_LOST` | Prop state | 64x64 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 034 | `PROP_DIAGNOSTIC_READER` | Held prop | 32x32 + 32x48 held layer | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 035 | `SUPPORT_COURIER_01` | Supporting character | 32x48 + pose reference | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests; Current room-actor code contains the injured courier pose; add manifest/provenance before VERIFIED. |\n| 036 | `NPC_TAMSIN_UTILITY_JACKET` | NPC clothing layer | 32x48 | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 037 | `NPC_TAMSIN_SATCHEL` | NPC accessory layer | 32x48 | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 038 | `NPC_TAMSIN_SYSTEMS_BADGE` | NPC identity micro-layer | 16x16 reference + 32x48 placement | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 039 | `UI_ITEM_QUALITY_FRAMES` | UI frame set | 32x32 | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 040 | `UI_EQUIPMENT_SLOT_ICON_SET` | UI icon set | 24x24 x slots | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests |\n| 041 | `PLATFORM_NINE_BLACKOUT_SCENE` | Location scene | 128x64 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 042 | `PLATFORM_NINE_EVACUATED_SCENE` | Location state | 128x64 | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests; high-priority missing exact scene/state asset for Gate Twelve content family. |\n| 043 | `RELAY_WORKBENCH_DEFAULT_SCENE` | Location scene | 128x64 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 044 | `RELAY_WORKBENCH_RELAY_OPEN_SCENE` | Location state | 128x64 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 045 | `GATE_TWELVE_SEALED_SCENE` | Location scene | 128x64 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 046 | `GATE_TWELVE_ECHO_ACTIVE_SCENE` | Location state | 128x64 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 047 | `SERVICE_TUNNEL_DEFAULT_SCENE` | Location scene | 128x64 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true; Open PR #27 refines the Service Tunnel base scene; keep current integrated master until the refinement is reviewed/verified/promoted. |\n| 048 | `SERVICE_TUNNEL_AFTERSHOCK_SCENE` | Location state | 128x64 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 049 | `EVAC_STAIR_DEFAULT_SCENE` | Location scene | 128x64 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true; Open PR #30 refines Quiet Stair; current integrated master remains the documented base until promotion. |\n| 050 | `TRACE_CHAMBER_IDLE_SCENE` | Location scene | 128x64 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 051 | `TRACE_CHAMBER_TRAINING_SCENE` | Location state | 128x64 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 052 | `DISTRICT_PLAZA_OPEN_SCENE` | Location scene | 128x64 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 053 | `DISTRICT_PLAZA_BLACKOUT_SCENE` | Location state | 128x64 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 054 | `DISTRICT_ARCHIVE_DEFAULT_SCENE` | Location scene | 128x64 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 055 | `DISTRICT_ARCHIVE_TERMINAL_CLOSEUP` | Location close-up | 128x64 | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests; high-priority missing exact scene/state asset for Gate Twelve content family. |\n| 056 | `WORKSHOP_ROW_DEFAULT_SCENE` | Location scene | 128x64 | INTEGRATED / provisional | native_scale_reviewed=false, android_scale_reviewed=false, palette_reviewed=false, state_binding_reviewed=true |\n| 057 | `WORKSHOP_ROW_RUMOR_SCENE` | Location state | 128x64 | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests; high-priority missing exact scene/state asset for Gate Twelve content family. |\n| 058 | `DEPOT_FACADE_EXTERIOR` | Environment module | 128x64 / reusable chunks | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 059 | `MAINTENANCE_CORRIDOR_CONNECTOR` | Environment module | 128x64 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests; Current reusable corridor is present; PR #28 has additional Service Tunnel composition/detail work not in this documentation branch. |\n| 060 | `MUNICIPAL_ARCHIVE_EXTERIOR` | Environment module | 128x64 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 061 | `MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS` | Environment atlas | 16x16/32x32 tiles | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests; Current infrastructure atlas is present; PR #28 contains additional atlas-composition detail not yet promoted into this documentation line. |\n| 062 | `EMERGENCY_LIGHT_OVERLAY` | Environment overlay | 128x64 alpha | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests; exact reusable overlay ID absent; audit equivalent blackout/emergency implementations before creating duplicate. |\n| 063 | `BLACKOUT_SHADOW_OVERLAY` | Environment overlay | 128x64 alpha | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests; exact reusable overlay ID absent; audit equivalent blackout/emergency implementations before creating duplicate. |\n| 064 | `EVACUATION_SIGNAGE_SET` | Environment decal set | 16x16/24x24 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 065 | `DISTRICT_AMBIENT_DECAL_SET` | Environment decal set | 16x16/32x32 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 066 | `PROP_DEPOT_DOOR` | Prop | 32x48 / scene-scale | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 067 | `PROP_RELAY_WORKBENCH` | Prop | 64x32 scene module | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 068 | `PROP_GATE_TWELVE_DOOR` | Prop | 64x48 scene module | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 069 | `PROP_TUNNEL_PIPE_SET` | Prop set | 16x16/32x32 modules | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 070 | `PROP_TUNNEL_CABLE_SET` | Prop set | 16x16/32x32 modules | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 071 | `PROP_TRACE_CHAMBER_APPARATUS` | Prop | 48x48 / scene module | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 072 | `PROP_ARCHIVE_SHELF` | Prop module | 32x48 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 073 | `PROP_ARCHIVE_TERMINAL` | Prop | 32x32 + close-up | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 074 | `PROP_WORKSHOP_BENCH` | Prop | 48x32 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 075 | `PROP_DISTRICT_NOTICE_BOARD` | Prop | 32x48 + close-up | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 076 | `UI_NAV_STORY_ICON` | UI icon | 24x24 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 077 | `UI_NAV_CHARACTER_ICON` | UI icon | 24x24 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 078 | `UI_NAV_STATS_ICON` | UI icon | 24x24 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 079 | `UI_NAV_INVENTORY_ICON` | UI icon | 24x24 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 080 | `UI_NAV_QUESTS_ICON` | UI icon | 24x24 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 081 | `UI_NAV_MAP_ICON` | UI icon | 24x24 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 082 | `UI_NAV_MORE_SETTINGS_ICON` | UI icon | 24x24 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 083 | `UI_RESOURCE_HEALTH_ICON` | HUD icon | 16x16 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 084 | `UI_RESOURCE_STAMINA_ICON` | HUD icon | 16x16 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 085 | `UI_RESOURCE_FOCUS_ICON` | HUD icon | 16x16 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 086 | `UI_RESOURCE_RESOLVE_ICON` | HUD icon | 16x16 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 087 | `UI_QUEST_MAIN_ICON` | Quest icon | 16x16 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 088 | `UI_QUEST_SIDE_ICON` | Quest icon | 16x16 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 089 | `UI_QUEST_OPTIONAL_ICON` | Quest icon | 16x16 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 090 | `UI_QUEST_LORE_ICON` | Quest icon | 16x16 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 091 | `MAP_PLAYER_MARKER` | Map icon | 16x16 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 092 | `MAP_NODE_DISCOVERED` | Map icon | 16x16 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 093 | `MAP_NODE_CURRENT` | Map icon | 16x16 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 094 | `MAP_NODE_REACHABLE` | Map icon | 16x16 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 095 | `MAP_NODE_UNAVAILABLE` | Map icon | 16x16 | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 096 | `FX_TRACE_ECHO_AMBIENT` | FX | 64x64 loop | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 097 | `FX_SIGNAL_PULSE` | FX | 64x64, 6-8 frames | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 098 | `FX_DIRECTIONAL_TRACE` | FX | 64x64, 6-8 frames | CODE_PRESENT / MANIFEST GAP | not recorded in audited manifests |\n| 099 | `FX_TRACE_STRAIN` | Status FX | 32x48 overlay + 64x64 portrait overlay | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests; exact planned FX/transition ID absent. |\n| 100 | `UI_MAP_TRAVEL_TRANSITION` | UI/transition | 128x64 or fullscreen tiled sequence | PLANNED / EXACT ID NOT FOUND IN AUDITED CURRENT CATALOGS | not recorded in audited manifests; exact planned FX/transition ID absent. |\n

---

# 5. Gate Twelve area decomposition

## 5.1 Depot Plaza

Existing/current families:
- `DISTRICT_PLAZA_OPEN_SCENE`;
- `DISTRICT_PLAZA_BLACKOUT_SCENE`;
- `DEPOT_FACADE_EXTERIOR`;
- `PROP_DISTRICT_NOTICE_BOARD`;
- evacuation/decal families;
- district map base.

Still required/review:
- final native-scale plaza art review;
- final paving/curb/road tile treatment;
- final lamp/tree modules;
- public actor slots/panel-safe composition;
- explicit future surface-world entrance anchor after parent city exists;
- emergency-light/shadow reusable overlay reconciliation (#062/#063).

## 5.2 Workshop Row

Existing/current families:
- `WORKSHOP_ROW_DEFAULT_SCENE`;
- `PROP_WORKSHOP_BENCH`;
- district ambient decals.

Missing exact planned state:
- `WORKSHOP_ROW_RUMOR_SCENE`.

Still required:
- reusable workshop bay/shutter/awning family;
- tool cart/scrap-bin/tool silhouettes;
- worker actor family only after NPC population data exists;
- practical signage family;
- native-scale material review.

## 5.3 Municipal Archive

Existing/current:
- `DISTRICT_ARCHIVE_DEFAULT_SCENE`;
- `MUNICIPAL_ARCHIVE_EXTERIOR`;
- shelf and terminal props.

Missing exact planned close-up:
- `DISTRICT_ARCHIVE_TERMINAL_CLOSEUP`.

Still required:
- final institutional facade/courtyard module review;
- clerk/visitor actor slots only when NPCs are authored;
- records/research indicators driven by projected state, not baked art.

## 5.4 Platform Nine

Existing/current:
- `PLATFORM_NINE_BLACKOUT_SCENE`;
- depot door;
- signage/decal families;
- map depot/track geometry;
- Tamsin/courier actor implementation line.

Missing exact planned state:
- `PLATFORM_NINE_EVACUATED_SCENE`.

Still required:
- post-evacuation visual state;
- final track/platform/depot material modules;
- reusable emergency/shadow overlays reconciled;
- crowd actor strategy;
- actor safe zones;
- future Plaza entrance scene transition.

## 5.5 Relay Workbench

Existing/current:
- `RELAY_WORKBENCH_DEFAULT_SCENE`;
- `RELAY_WORKBENCH_RELAY_OPEN_SCENE`;
- relay object states;
- workbench prop;
- Tamsin recovery actor placement.

Still required:
- diagnostic reader asset (#034);
- final diagnostic pose (#020);
- exact relay ID reconciliation at Batch unit #030;
- final room actor/prop occlusion anchors;
- native-scale QA.

## 5.6 Gate Twelve

Existing/current:
- `GATE_TWELVE_SEALED_SCENE`;
- `GATE_TWELVE_ECHO_ACTIVE_SCENE`;
- gate door prop;
- Trace FX families.

Still required:
- final gate material/silhouette review;
- future physical open/powered-off variants only if engine state supports them;
- actor safe zones;
- state overlay QA at phone scale.

## 5.7 Quiet Stair

Existing/current:
- `EVAC_STAIR_DEFAULT_SCENE`;
- signage;
- infrastructure atlas.

Refinement:
- PR #30 contains later scene refinement.

Still required:
- review/promote-or-reject refinement;
- future egress boundary art after destination exists;
- restrained guidance-light behavior;
- actor/event slots only if content requires them.

## 5.8 Service Tunnel

Existing/current:
- `SERVICE_TUNNEL_DEFAULT_SCENE`;
- `SERVICE_TUNNEL_AFTERSHOCK_SCENE`;
- maintenance corridor connector;
- infrastructure atlas;
- pipe/cable prop families;
- Tamsin opening actor placement.

Refinements:
- PR #27 scene refinement;
- PR #28 atlas/composition detail;
- PR #31 ambient animation.

Still required:
- reconcile these parallel/sibling lines;
- exact native-scale final scene review;
- define deeper-expansion visual stub;
- actor/panel safe zones;
- reduced-motion behavior for ambient animation.

## 5.9 Trace Chamber

Existing/current:
- `TRACE_CHAMBER_IDLE_SCENE`;
- `TRACE_CHAMBER_TRAINING_SCENE`;
- apparatus prop;
- Signal/Directional Trace FX.

Still required:
- Trace Strain exact planned asset (#099);
- actor training poses;
- measurement/diagnostic prop refinement;
- final controlled-room material review;
- verify active FX never exposes hidden route information.

---

# 6. Character/panel assets required by the room system

## Player / Jack Wilson

Authority:
- `UI_REFERENCE_CHARACTER_APPROVED_V1` is the approved visual identity target;
- 32x48 rig remains the technical runtime contract.

Still required before final player art:
- six-view Jack turnaround derived from approved identity without inventing unseen asymmetry;
- left/right/back gameplay masters;
- neutral portrait;
- emotion portraits/templates consistent with Jack;
- idle/walk/run/crouch/interact/hurt/Trace sheets as actually needed by shipped gameplay;
- face/skin/hair source layers;
- visible status overlays;
- equipment layer review against Jack silhouette.

## Tamsin

Current:
- source-backed canonical identity;
- front room actor code exists.

Still required:
- full six-view turnaround;
- portrait emotion set;
- diagnostic pose;
- explicit jacket/satchel/badge source layers or a documented decision that they remain inseparable in the character master;
- room-panel portrait mapping.

## Supporting courier

Current:
- room actor code exists.

Still required:
- manifest/provenance entry;
- no promotion to recurring named NPC unless content explicitly does so;
- optional close portrait only if dialogue/panel presentation requires one.

---

# 7. Asset reuse / overlay decision table

Reuse the same master when:
- identity is unchanged;
- perspective matches;
- scale matches;
- material/lighting can be locally harmonized;
- state semantics match.

Create an overlay when:
- architecture is unchanged;
- blackout/emergency/Trace/event state changes;
- a prop changes state;
- a temporary actor/FX enters.

Create a new view/master when:
- perspective changes materially;
- the physical architecture changes;
- the actor direction/pose cannot be derived without distortion;
- state changes the object silhouette substantially.

Reject/rebuild when:
- source looks pasted from another visual language;
- pixel density is incompatible;
- silhouette depends on anti-aliased detail;
- reference contradicts canonical identity;
- asset encodes hidden gameplay state.

---

# 8. Production priority after this audit

P0:
- resolve Jack/reference/turnaround authority;
- resolve exact asset-ID/manifest drift;
- finish missing exact current-region state assets #042, #055, #057;
- reconcile #062/#063 overlay equivalents;
- native-scale/phone-scale review of already integrated Gate Twelve scenes;
- reconcile Service Tunnel/Quiet Stair open refinements.

P1:
- actor-projection contract + room-panel assets;
- Tamsin turnaround/portraits/diagnostic pose;
- Jack remaining directional/portrait/status masters;
- diagnostic reader;
- world-facing Gate Twelve transition assets after parent geography exists.

P2:
- character movement animation sheets only when the application actually consumes them;
- travel transition #100 after final map travel UX is locked;
- broad world asset families only after world schemas exist.

---

# 9. Step-7 acceptance

Step 7 is complete when this matrix is treated as the production inventory and future work does not:
- recreate exact IDs blindly;
- confuse code presence with final art approval;
- confuse open PR refinement with canonical integration;
- lose Jack's approved reference because of branch ancestry;
- flatten temporary room states into new base scenes;
- build actor panels from hidden state.
