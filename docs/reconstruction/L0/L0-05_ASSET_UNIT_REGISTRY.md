# L0-05 — Asset Unit Registry

Layer: **L0 Foundation**  
Depends on: L0-02 (angle standard), L0-03 (native grid standard)  
Source: `docs/assets/ASSET_BATCH_001_001-100.md` … `ASSET_BATCH_005_401-500.md`

---

## 1. Purpose

This registry is the **complete, mechanically verified inventory** of every asset unit the v1
production plan defines, plus the assignment of each unit to an angle view set.

It exists so that:

- no unit is documented twice under two different IDs;
- no unit is skipped because it is 'obvious';
- every unit has exactly one view set, decided by rule rather than by taste;

- a rebuild can enumerate its full art workload before starting.

## 2. Verification record

Parsed directly from the five batch catalogs during corpus construction:

| Check | Result |
| --- | --- |
| Total units parsed | **500** |
| Number range | 001–500, continuous |
| Missing numbers | **NONE** |
| Duplicate stable asset IDs | **NONE** |
| Batch 001 | 100 units (6-column catalog, no canon-class column) |
| Batches 002–005 | 400 units (7-column catalog, with canon-class column) |

Canon-class distribution as authored:

| Canon class | Units |
| --- | ---: |
| technical/non-canon framework | 300 |
| — (not stated in source) | 100 |
| technical | 96 |
| current/provisional canon + technical | 4 |

**This distribution is the single most important governance fact in the asset plan:**
300 of 500 units are explicitly `technical/non-canon framework`. A rebuild that treats
them as story canon has misread the plan.


## 3. View-set assignment rule

One rule, applied by stable asset ID first and family second. The ID pattern
dominates because the ID is the stable identity (L0-06 §1).

| View set | Units | Meaning |
| --- | ---: | --- |
| `PRESENTATION_STATES` | 167 | state variants, no camera angles |
| `TILE_AXES` | 146 | seam/axis behaviour, no camera angles |
| `PROP_ANGLES` | 71 | presentation angle set + grip-in-context |
| `SIX_VIEW_DEFERRED` | 69 | all six specified, subset ships first |
| `SIX_VIEW` | 30 | full six-view turnaround, all views required |
| `SCENE_CAMERA` | 17 | single camera + state variants |

### 3.1 Rule, in evaluation order

1. `TURNAROUND` in the ID → `SIX_VIEW`.
2. `BODYFRAME` / `HEAD_SHAPE` / `GAMEPLAY_(FRONT|LEFT_PROFILE|RIGHT_PROFILE|BACK)` → `SIX_VIEW`.
3. family `npc archetype`, or an `_NPC_*_BASE`/`_BODY` ID → `SIX_VIEW`.
4. `PAPERDOLL` / `CLOTHING_KIT` / family clothing / equipment / animation → `SIX_VIEW_DEFERRED`.
5. family `location scene`, `location state`, `location close-up` → `SCENE_CAMERA`.
6. family prop / held / container / key item → `PROP_ANGLES`.
7. `ATLAS` / `TILE` / `_TILESET` / `MODULE` in the ID, or architecture/interior module family → `TILE_AXES`.
8. portrait family, or an `ICON`/`FRAME`/`MARKER`/`UI_`/`HUD`/`FX`/`TRANSITION`/`STATUS`/`BAR`/`BUTTON`/`PANEL`-shaped ID → `PRESENTATION_STATES`.
9. Otherwise → `TILE_AXES` (modular default).

### 3.2 Machine-readable companion

**`L0-05_ASSET_UNIT_REGISTRY.json`** carries the same 500 units under the same
rule, with its own integrity assertion (`500 units, 500 unique numbers, 500
unique asset IDs`). Both files are generated from one parse of the five batch
catalogs and are verified equal after generation. Where they disagree, the JSON
is authoritative for counts because its integrity is assertable.

### 3.3 Reading the assignment

`SCENE_CAMERA` is small because location scenes are authored as location masters
plus state variants, not as one scene per story beat. `TILE_AXES` is large
because most of batches 004–005 are modular architecture, materials and UI
shells whose reconstruction question is seam behaviour rather than camera angle.
That is the plan working as designed, not a gap.

## 4. The complete 500-unit registry

Columns: `#` · stable ID · family · native master · assigned view set · canon class.

Exact game use and production notes are in the batch catalogs and are **not**
duplicated here; this registry is the index, the batches are the detail.


### Batch 1 — 001–100

| # | Stable asset ID | Family | Native | View set | Canon class |
| ---: | --- | --- | --- | --- | --- |
| 001 | `PLAYER_BODYFRAME_A_TURNAROUND` | Character | 1024+ reference -> 32x48 masters | `SIX_VIEW` | — |
| 002 | `PLAYER_GAMEPLAY_FRONT_BASE` | Character | 32x48 | `SIX_VIEW` | — |
| 003 | `PLAYER_GAMEPLAY_LEFT_PROFILE_BASE` | Character | 32x48 | `SIX_VIEW` | — |
| 004 | `PLAYER_GAMEPLAY_RIGHT_PROFILE_BASE` | Character | 32x48 | `SIX_VIEW` | — |
| 005 | `PLAYER_GAMEPLAY_BACK_BASE` | Character | 32x48 | `SIX_VIEW` | — |
| 006 | `PLAYER_IDLE_SHEET` | Animation | 32x48 x 4 frames | `SIX_VIEW_DEFERRED` | — |
| 007 | `PLAYER_WALK_SHEET` | Animation | 32x48 x 6 frames/direction | `SIX_VIEW_DEFERRED` | — |
| 008 | `PLAYER_RUN_SHEET` | Animation | 32x48 x 8 frames/direction | `SIX_VIEW_DEFERRED` | — |
| 009 | `PLAYER_CROUCH_SHEET` | Animation | 32x48, 6 transition/loop frames | `SIX_VIEW_DEFERRED` | — |
| 010 | `PLAYER_INTERACT_TOOL_SHEET` | Animation | 32x48, 4-6 frames | `SIX_VIEW_DEFERRED` | — |
| 011 | `PLAYER_HURT_RECOVER_SHEET` | Animation | 32x48, 3-4 frames | `SIX_VIEW_DEFERRED` | — |
| 012 | `PLAYER_TRACE_ACTIVATION_SHEET` | Animation | 32x48, 6-8 frames | `SIX_VIEW_DEFERRED` | — |
| 013 | `PLAYER_PORTRAIT_NEUTRAL` | Portrait | 64x64 | `PRESENTATION_STATES` | — |
| 014 | `PLAYER_PORTRAIT_EMOTION_TEMPLATES` | Portrait | 64x64 set | `PRESENTATION_STATES` | — |
| 015 | `PLAYER_HAIR_LAYER_KIT_A` | Character layer | 32x48 + 64x64 portrait companion | `SIX_VIEW_DEFERRED` | — |
| 016 | `PLAYER_FACE_SKIN_PALETTE_KIT_A` | Character layer | 32x48 + 64x64 | `SIX_VIEW_DEFERRED` | — |
| 017 | `PLAYER_VISIBLE_STATUS_OVERLAYS` | Character overlay | 32x48 | `PRESENTATION_STATES` | — |
| 018 | `NPC_TAMSIN_TURNAROUND` | Character | 1024+ reference -> 32x48 masters | `SIX_VIEW` | — |
| 019 | `NPC_TAMSIN_PORTRAIT_EMOTIONS` | Portrait | 64x64 x 5 | `PRESENTATION_STATES` | — |
| 020 | `NPC_TAMSIN_DIAGNOSTIC_POSE` | Character pose | 32x48 + 64x64 reference | `TILE_AXES` | — |
| 021 | `ITEM_DEPOT_JACKET_ICON` | Item icon | 32x32 | `PRESENTATION_STATES` | — |
| 022 | `ITEM_DEPOT_JACKET_PAPERDOLL` | Equipment layer | 32x48 | `SIX_VIEW_DEFERRED` | — |
| 023 | `ITEM_WORK_GLOVES_ICON` | Item icon | 32x32 | `PRESENTATION_STATES` | — |
| 024 | `ITEM_WORK_GLOVES_PAPERDOLL` | Equipment layer | 32x48 | `SIX_VIEW_DEFERRED` | — |
| 025 | `ITEM_SIGNAL_RING_ICON` | Item icon | 32x32 | `PRESENTATION_STATES` | — |
| 026 | `ITEM_SIGNAL_RING_PAPERDOLL` | Equipment micro-layer | 32x48 | `SIX_VIEW_DEFERRED` | — |
| 027 | `ITEM_COURIER_NECKTAG_ICON` | Item icon | 32x32 | `PRESENTATION_STATES` | — |
| 028 | `ITEM_COURIER_NECKTAG_PAPERDOLL` | Equipment layer | 32x48 | `SIX_VIEW_DEFERRED` | — |
| 029 | `ITEM_MAINTENANCE_SEAL_ICON` | Item icon | 32x32 | `PRESENTATION_STATES` | — |
| 030 | `ITEM_DEAD_RELAY_INTACT` | Item/prop | 32x32 icon + 64x64 close-up | `PROP_ANGLES` | — |
| 031 | `ITEM_DEAD_RELAY_OPENED` | Prop state | 64x64 | `PROP_ANGLES` | — |
| 032 | `ITEM_DEAD_RELAY_DAMAGED` | Prop state | 64x64 | `PROP_ANGLES` | — |
| 033 | `ITEM_DEAD_RELAY_SIGNAL_LOST` | Prop state | 64x64 | `PROP_ANGLES` | — |
| 034 | `PROP_DIAGNOSTIC_READER` | Held prop | 32x32 + 32x48 held layer | `PROP_ANGLES` | — |
| 035 | `SUPPORT_COURIER_01` | Supporting character | 32x48 + pose reference | `TILE_AXES` | — |
| 036 | `NPC_TAMSIN_UTILITY_JACKET` | NPC clothing layer | 32x48 | `SIX_VIEW_DEFERRED` | — |
| 037 | `NPC_TAMSIN_SATCHEL` | NPC accessory layer | 32x48 | `TILE_AXES` | — |
| 038 | `NPC_TAMSIN_SYSTEMS_BADGE` | NPC identity micro-layer | 16x16 reference + 32x48 placement | `PRESENTATION_STATES` | — |
| 039 | `UI_ITEM_QUALITY_FRAMES` | UI frame set | 32x32 | `PRESENTATION_STATES` | — |
| 040 | `UI_EQUIPMENT_SLOT_ICON_SET` | UI icon set | 24x24 x slots | `PRESENTATION_STATES` | — |
| 041 | `PLATFORM_NINE_BLACKOUT_SCENE` | Location scene | 128x64 | `SCENE_CAMERA` | — |
| 042 | `PLATFORM_NINE_EVACUATED_SCENE` | Location state | 128x64 | `SCENE_CAMERA` | — |
| 043 | `RELAY_WORKBENCH_DEFAULT_SCENE` | Location scene | 128x64 | `SCENE_CAMERA` | — |
| 044 | `RELAY_WORKBENCH_RELAY_OPEN_SCENE` | Location state | 128x64 | `SCENE_CAMERA` | — |
| 045 | `GATE_TWELVE_SEALED_SCENE` | Location scene | 128x64 | `SCENE_CAMERA` | — |
| 046 | `GATE_TWELVE_ECHO_ACTIVE_SCENE` | Location state | 128x64 | `SCENE_CAMERA` | — |
| 047 | `SERVICE_TUNNEL_DEFAULT_SCENE` | Location scene | 128x64 | `SCENE_CAMERA` | — |
| 048 | `SERVICE_TUNNEL_AFTERSHOCK_SCENE` | Location state | 128x64 | `SCENE_CAMERA` | — |
| 049 | `EVAC_STAIR_DEFAULT_SCENE` | Location scene | 128x64 | `SCENE_CAMERA` | — |
| 050 | `TRACE_CHAMBER_IDLE_SCENE` | Location scene | 128x64 | `SCENE_CAMERA` | — |
| 051 | `TRACE_CHAMBER_TRAINING_SCENE` | Location state | 128x64 | `SCENE_CAMERA` | — |
| 052 | `DISTRICT_PLAZA_OPEN_SCENE` | Location scene | 128x64 | `SCENE_CAMERA` | — |
| 053 | `DISTRICT_PLAZA_BLACKOUT_SCENE` | Location state | 128x64 | `SCENE_CAMERA` | — |
| 054 | `DISTRICT_ARCHIVE_DEFAULT_SCENE` | Location scene | 128x64 | `SCENE_CAMERA` | — |
| 055 | `DISTRICT_ARCHIVE_TERMINAL_CLOSEUP` | Location close-up | 128x64 | `SCENE_CAMERA` | — |
| 056 | `WORKSHOP_ROW_DEFAULT_SCENE` | Location scene | 128x64 | `SCENE_CAMERA` | — |
| 057 | `WORKSHOP_ROW_RUMOR_SCENE` | Location state | 128x64 | `SCENE_CAMERA` | — |
| 058 | `DEPOT_FACADE_EXTERIOR` | Environment module | 128x64 / reusable chunks | `TILE_AXES` | — |
| 059 | `MAINTENANCE_CORRIDOR_CONNECTOR` | Environment module | 128x64 | `TILE_AXES` | — |
| 060 | `MUNICIPAL_ARCHIVE_EXTERIOR` | Environment module | 128x64 | `TILE_AXES` | — |
| 061 | `MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS` | Environment atlas | 16x16/32x32 tiles | `TILE_AXES` | — |
| 062 | `EMERGENCY_LIGHT_OVERLAY` | Environment overlay | 128x64 alpha | `TILE_AXES` | — |
| 063 | `BLACKOUT_SHADOW_OVERLAY` | Environment overlay | 128x64 alpha | `TILE_AXES` | — |
| 064 | `EVACUATION_SIGNAGE_SET` | Environment decal set | 16x16/24x24 | `TILE_AXES` | — |
| 065 | `DISTRICT_AMBIENT_DECAL_SET` | Environment decal set | 16x16/32x32 | `TILE_AXES` | — |
| 066 | `PROP_DEPOT_DOOR` | Prop | 32x48 / scene-scale | `PROP_ANGLES` | — |
| 067 | `PROP_RELAY_WORKBENCH` | Prop | 64x32 scene module | `PROP_ANGLES` | — |
| 068 | `PROP_GATE_TWELVE_DOOR` | Prop | 64x48 scene module | `PROP_ANGLES` | — |
| 069 | `PROP_TUNNEL_PIPE_SET` | Prop set | 16x16/32x32 modules | `PROP_ANGLES` | — |
| 070 | `PROP_TUNNEL_CABLE_SET` | Prop set | 16x16/32x32 modules | `PROP_ANGLES` | — |
| 071 | `PROP_TRACE_CHAMBER_APPARATUS` | Prop | 48x48 / scene module | `PROP_ANGLES` | — |
| 072 | `PROP_ARCHIVE_SHELF` | Prop module | 32x48 | `PROP_ANGLES` | — |
| 073 | `PROP_ARCHIVE_TERMINAL` | Prop | 32x32 + close-up | `PROP_ANGLES` | — |
| 074 | `PROP_WORKSHOP_BENCH` | Prop | 48x32 | `PROP_ANGLES` | — |
| 075 | `PROP_DISTRICT_NOTICE_BOARD` | Prop | 32x48 + close-up | `PROP_ANGLES` | — |
| 076 | `UI_NAV_STORY_ICON` | UI icon | 24x24 | `PRESENTATION_STATES` | — |
| 077 | `UI_NAV_CHARACTER_ICON` | UI icon | 24x24 | `PRESENTATION_STATES` | — |
| 078 | `UI_NAV_STATS_ICON` | UI icon | 24x24 | `PRESENTATION_STATES` | — |
| 079 | `UI_NAV_INVENTORY_ICON` | UI icon | 24x24 | `PRESENTATION_STATES` | — |
| 080 | `UI_NAV_QUESTS_ICON` | UI icon | 24x24 | `PRESENTATION_STATES` | — |
| 081 | `UI_NAV_MAP_ICON` | UI icon | 24x24 | `PRESENTATION_STATES` | — |
| 082 | `UI_NAV_MORE_SETTINGS_ICON` | UI icon | 24x24 | `PRESENTATION_STATES` | — |
| 083 | `UI_RESOURCE_HEALTH_ICON` | HUD icon | 16x16 | `PRESENTATION_STATES` | — |
| 084 | `UI_RESOURCE_STAMINA_ICON` | HUD icon | 16x16 | `PRESENTATION_STATES` | — |
| 085 | `UI_RESOURCE_FOCUS_ICON` | HUD icon | 16x16 | `PRESENTATION_STATES` | — |
| 086 | `UI_RESOURCE_RESOLVE_ICON` | HUD icon | 16x16 | `PRESENTATION_STATES` | — |
| 087 | `UI_QUEST_MAIN_ICON` | Quest icon | 16x16 | `PRESENTATION_STATES` | — |
| 088 | `UI_QUEST_SIDE_ICON` | Quest icon | 16x16 | `PRESENTATION_STATES` | — |
| 089 | `UI_QUEST_OPTIONAL_ICON` | Quest icon | 16x16 | `PRESENTATION_STATES` | — |
| 090 | `UI_QUEST_LORE_ICON` | Quest icon | 16x16 | `PRESENTATION_STATES` | — |
| 091 | `MAP_PLAYER_MARKER` | Map icon | 16x16 | `PRESENTATION_STATES` | — |
| 092 | `MAP_NODE_DISCOVERED` | Map icon | 16x16 | `TILE_AXES` | — |
| 093 | `MAP_NODE_CURRENT` | Map icon | 16x16 | `TILE_AXES` | — |
| 094 | `MAP_NODE_REACHABLE` | Map icon | 16x16 | `TILE_AXES` | — |
| 095 | `MAP_NODE_UNAVAILABLE` | Map icon | 16x16 | `TILE_AXES` | — |
| 096 | `FX_TRACE_ECHO_AMBIENT` | FX | 64x64 loop | `PRESENTATION_STATES` | — |
| 097 | `FX_SIGNAL_PULSE` | FX | 64x64, 6-8 frames | `PRESENTATION_STATES` | — |
| 098 | `FX_DIRECTIONAL_TRACE` | FX | 64x64, 6-8 frames | `PRESENTATION_STATES` | — |
| 099 | `FX_TRACE_STRAIN` | Status FX | 32x48 overlay + 64x64 portrait overlay | `PRESENTATION_STATES` | — |
| 100 | `UI_MAP_TRAVEL_TRANSITION` | UI/transition | 128x64 or fullscreen tiled sequence | `PRESENTATION_STATES` | — |

### Batch 2 — 101–200

| # | Stable asset ID | Family | Native | View set | Canon class |
| ---: | --- | --- | --- | --- | --- |
| 101 | `PLAYER_BODYFRAME_B` | Character base | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 102 | `PLAYER_BODYFRAME_C` | Character base | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 103 | `PLAYER_HEAD_SHAPE_KIT_A` | Character layer | 32x48 + 64x64 | `SIX_VIEW` | technical/non-canon framework |
| 104 | `PLAYER_HEAD_SHAPE_KIT_B` | Character layer | 32x48 + 64x64 | `SIX_VIEW` | technical/non-canon framework |
| 105 | `PLAYER_HAIR_LAYER_KIT_B` | Character layer | 32x48 + 64x64 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 106 | `PLAYER_HAIR_LAYER_KIT_C` | Character layer | 32x48 + 64x64 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 107 | `PLAYER_SKIN_RAMP_SET_B` | Palette layer | shared | `TILE_AXES` | technical/non-canon framework |
| 108 | `PLAYER_SKIN_RAMP_SET_C` | Palette layer | shared | `TILE_AXES` | technical/non-canon framework |
| 109 | `PLAYER_IDENTITY_MARK_KIT` | Character micro-layer | 32x48 + 64x64 | `TILE_AXES` | technical/non-canon framework |
| 110 | `PLAYER_FACIAL_HAIR_KIT_A` | Character layer | 32x48 + 64x64 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 111 | `PLAYER_WALK_FRONT_SHEET` | Animation | 32x48 x 6 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 112 | `PLAYER_WALK_BACK_SHEET` | Animation | 32x48 x 6 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 113 | `PLAYER_WALK_LEFT_SHEET` | Animation | 32x48 x 6 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 114 | `PLAYER_WALK_RIGHT_SHEET` | Animation | 32x48 x 6 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 115 | `PLAYER_RUN_FRONT_SHEET` | Animation | 32x48 x 8 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 116 | `PLAYER_RUN_BACK_SHEET` | Animation | 32x48 x 8 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 117 | `PLAYER_RUN_LEFT_SHEET` | Animation | 32x48 x 8 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 118 | `PLAYER_RUN_RIGHT_SHEET` | Animation | 32x48 x 8 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 119 | `PLAYER_TURN_IN_PLACE_SHEET` | Animation | 32x48 x 4-6 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 120 | `PLAYER_PICKUP_INTERACT_SHEET` | Animation | 32x48 x 4-6 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 121 | `PLAYER_TERMINAL_INTERACT_SHEET` | Animation | 32x48 x 4-6 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 122 | `PLAYER_DOOR_INTERACT_SHEET` | Animation | 32x48 x 4-6 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 123 | `PLAYER_SIT_IDLE_SHEET` | Animation | 32x48 x 4 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 124 | `PLAYER_KNEEL_INSPECT_SHEET` | Animation | 32x48 x 4-6 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 125 | `PLAYER_GUARD_READY_SHEET` | Animation | 32x48 x 4 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 126 | `PLAYER_PORTRAIT_FOCUSED` | Portrait | 64x64 | `PRESENTATION_STATES` | technical/non-canon framework |
| 127 | `PLAYER_PORTRAIT_CONCERNED` | Portrait | 64x64 | `PRESENTATION_STATES` | technical/non-canon framework |
| 128 | `PLAYER_PORTRAIT_HURT` | Portrait | 64x64 | `PRESENTATION_STATES` | technical/non-canon framework |
| 129 | `PLAYER_PORTRAIT_DETERMINED` | Portrait | 64x64 | `PRESENTATION_STATES` | technical/non-canon framework |
| 130 | `PLAYER_PORTRAIT_SURPRISED` | Portrait | 64x64 | `PRESENTATION_STATES` | technical/non-canon framework |
| 131 | `NPC_PORTRAIT_FRAME_STANDARD` | Portrait UI | 72x72 frame | `PRESENTATION_STATES` | technical/non-canon framework |
| 132 | `NPC_PORTRAIT_FRAME_URGENT` | Portrait UI | 72x72 frame | `PRESENTATION_STATES` | technical/non-canon framework |
| 133 | `NPC_PORTRAIT_SILHOUETTE_UNKNOWN` | Portrait | 64x64 | `PRESENTATION_STATES` | technical/non-canon framework |
| 134 | `NPC_PORTRAIT_OFFSCREEN_MARKER` | Portrait/UI | 24x24 | `PRESENTATION_STATES` | technical/non-canon framework |
| 135 | `NPC_EMOTION_NEUTRAL_TEMPLATE` | Portrait template | 64x64 | `PRESENTATION_STATES` | technical/non-canon framework |
| 136 | `NPC_EMOTION_FOCUSED_TEMPLATE` | Portrait template | 64x64 | `PRESENTATION_STATES` | technical/non-canon framework |
| 137 | `NPC_EMOTION_CONCERNED_TEMPLATE` | Portrait template | 64x64 | `PRESENTATION_STATES` | technical/non-canon framework |
| 138 | `NPC_EMOTION_ANGRY_TEMPLATE` | Portrait template | 64x64 | `PRESENTATION_STATES` | technical/non-canon framework |
| 139 | `NPC_EMOTION_RELIEVED_TEMPLATE` | Portrait template | 64x64 | `PRESENTATION_STATES` | technical/non-canon framework |
| 140 | `NPC_EMOTION_SUSPICIOUS_TEMPLATE` | Portrait template | 64x64 | `PRESENTATION_STATES` | technical/non-canon framework |
| 141 | `NPC_ARCHETYPE_MUNICIPAL_TECH_BASE` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 142 | `NPC_ARCHETYPE_COURIER_BASE` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 143 | `NPC_ARCHETYPE_ARCHIVIST_BASE` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 144 | `NPC_ARCHETYPE_WORKSHOP_MECHANIC_BASE` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 145 | `NPC_ARCHETYPE_SECURITY_BASE` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 146 | `NPC_ARCHETYPE_MEDIC_BASE` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 147 | `NPC_ARCHETYPE_EVACUEE_BASE_A` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 148 | `NPC_ARCHETYPE_EVACUEE_BASE_B` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 149 | `NPC_ARCHETYPE_VENDOR_BASE` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 150 | `NPC_ARCHETYPE_CONTRACTOR_BASE` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 151 | `NPC_ARCHETYPE_INVESTIGATOR_BASE` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 152 | `NPC_ARCHETYPE_SUPERVISOR_BASE` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 153 | `NPC_ARCHETYPE_TRAVELER_BASE` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 154 | `NPC_ARCHETYPE_SCAVENGER_BASE` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 155 | `NPC_ARCHETYPE_TECHNICIAN_TRAINEE_BASE` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 156 | `NPC_ARCHETYPE_FIELD_OPERATOR_BASE` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 157 | `NPC_ARCHETYPE_RESEARCHER_BASE` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 158 | `NPC_ARCHETYPE_CIVILIAN_FORMAL_BASE` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 159 | `NPC_ARCHETYPE_CIVILIAN_CASUAL_BASE` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 160 | `NPC_ARCHETYPE_INJURED_SUPPORT_BASE` | NPC archetype | 32x48 | `SIX_VIEW` | technical/non-canon framework |
| 161 | `NPC_ROLEKIT_MUNICIPAL_UTILITY` | NPC clothing kit | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 162 | `NPC_ROLEKIT_ARCHIVE_STAFF` | NPC clothing kit | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 163 | `NPC_ROLEKIT_WORKSHOP_STAFF` | NPC clothing kit | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 164 | `NPC_ROLEKIT_SECURITY_LIGHT` | NPC clothing kit | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 165 | `NPC_ROLEKIT_MEDICAL` | NPC clothing kit | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 166 | `NPC_ROLEKIT_COURIER` | NPC clothing kit | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 167 | `NPC_ROLEKIT_CONTRACTOR` | NPC clothing kit | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 168 | `NPC_ROLEKIT_CIVILIAN_WARM` | NPC clothing kit | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 169 | `NPC_ROLEKIT_CIVILIAN_COOL` | NPC clothing kit | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 170 | `NPC_ROLEKIT_FORMAL_OFFICE` | NPC clothing kit | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 171 | `NPC_ROLEKIT_FIELD_RAIN` | NPC clothing kit | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 172 | `NPC_ROLEKIT_FIELD_DUST` | NPC clothing kit | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 173 | `NPC_ROLEKIT_RESEARCH` | NPC clothing kit | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 174 | `NPC_ROLEKIT_SALVAGE` | NPC clothing kit | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 175 | `NPC_ROLEKIT_EMERGENCY_BLANKET` | NPC clothing overlay | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 176 | `NPC_ROLEKIT_INJURY_SLING` | NPC status clothing | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 177 | `NPC_ROLEKIT_TOOL_BELT` | NPC accessory kit | 32x48 | `TILE_AXES` | technical/non-canon framework |
| 178 | `NPC_ROLEKIT_SATCHEL_GENERIC` | NPC accessory kit | 32x48 | `TILE_AXES` | technical/non-canon framework |
| 179 | `NPC_ROLEKIT_BACKPACK_GENERIC` | NPC accessory kit | 32x48 | `TILE_AXES` | technical/non-canon framework |
| 180 | `NPC_ROLEKIT_ID_BADGE_GENERIC` | NPC accessory kit | 16x16 ref + 32x48 placement | `PRESENTATION_STATES` | technical/non-canon framework |
| 181 | `SOCIAL_EMOTE_TRUST_UP` | Social UI | 16x16 | `TILE_AXES` | technical/non-canon framework |
| 182 | `SOCIAL_EMOTE_TRUST_DOWN` | Social UI | 16x16 | `TILE_AXES` | technical/non-canon framework |
| 183 | `SOCIAL_EMOTE_SUSPICION` | Social UI | 16x16 | `TILE_AXES` | technical/non-canon framework |
| 184 | `SOCIAL_EMOTE_DEBT` | Social UI | 16x16 | `TILE_AXES` | technical/non-canon framework |
| 185 | `SOCIAL_EMOTE_LOYALTY` | Social UI | 16x16 | `TILE_AXES` | technical/non-canon framework |
| 186 | `NPC_STATUS_INJURY_MINOR` | NPC overlay | 32x48 | `PRESENTATION_STATES` | technical/non-canon framework |
| 187 | `NPC_STATUS_INJURY_MAJOR` | NPC overlay | 32x48 | `PRESENTATION_STATES` | technical/non-canon framework |
| 188 | `NPC_STATUS_EXHAUSTED` | NPC overlay | 32x48 | `PRESENTATION_STATES` | technical/non-canon framework |
| 189 | `NPC_STATUS_TRACE_AFFECTED` | NPC overlay | 32x48 | `PRESENTATION_STATES` | technical/non-canon framework |
| 190 | `NPC_STATUS_UNKNOWN_MASK` | NPC overlay | 32x48 | `PRESENTATION_STATES` | technical/non-canon framework |
| 191 | `CHARACTER_GROUND_SHADOW_SMALL` | Character staging | 32x16 | `TILE_AXES` | technical/non-canon framework |
| 192 | `CHARACTER_GROUND_SHADOW_MEDIUM` | Character staging | 32x16 | `TILE_AXES` | technical/non-canon framework |
| 193 | `CHARACTER_GROUND_SHADOW_LARGE` | Character staging | 40x16 | `TILE_AXES` | technical/non-canon framework |
| 194 | `CHARACTER_SPEAKER_FOCUS_RING` | Character staging | 40x56 | `TILE_AXES` | technical/non-canon framework |
| 195 | `CHARACTER_INTERACTION_MARKER` | Character staging | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 196 | `CHARACTER_PARTY_MARKER` | Character staging | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 197 | `CHARACTER_OFFSCREEN_DIRECTION_MARKER` | Character staging | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 198 | `CHARACTER_HIGH_CONTRAST_SILHOUETTE` | Accessibility | 32x48 mask | `TILE_AXES` | technical/non-canon framework |
| 199 | `CHARACTER_COLORBLIND_ROLE_MARKERS` | Accessibility | 16x16 set | `PRESENTATION_STATES` | technical/non-canon framework |
| 200 | `CHARACTER_DEBUG_ANCHOR_OVERLAY` | Developer asset | 32x48 grid | `TILE_AXES` | technical/non-canon framework |

### Batch 3 — 201–300

| # | Stable asset ID | Family | Native | View set | Canon class |
| ---: | --- | --- | --- | --- | --- |
| 201 | `EQUIP_TEMPLATE_HEAD_LIGHT` | Equipment template | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 202 | `EQUIP_TEMPLATE_HEAD_HEAVY` | Equipment template | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 203 | `EQUIP_TEMPLATE_CHEST_LIGHT` | Equipment template | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 204 | `EQUIP_TEMPLATE_CHEST_HEAVY` | Equipment template | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 205 | `EQUIP_TEMPLATE_HANDS_LIGHT` | Equipment template | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 206 | `EQUIP_TEMPLATE_HANDS_HEAVY` | Equipment template | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 207 | `EQUIP_TEMPLATE_LEGS_LIGHT` | Equipment template | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 208 | `EQUIP_TEMPLATE_LEGS_HEAVY` | Equipment template | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 209 | `EQUIP_TEMPLATE_FEET_LIGHT` | Equipment template | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 210 | `EQUIP_TEMPLATE_FEET_HEAVY` | Equipment template | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 211 | `EQUIP_TEMPLATE_NECK_SMALL` | Equipment template | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 212 | `EQUIP_TEMPLATE_NECK_LARGE` | Equipment template | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 213 | `EQUIP_TEMPLATE_RING_LEFT` | Equipment micro-layer | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 214 | `EQUIP_TEMPLATE_RING_RIGHT` | Equipment micro-layer | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 215 | `EQUIP_TEMPLATE_ACCESSORY_REAR` | Equipment template | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 216 | `EQUIP_TEMPLATE_ACCESSORY_FRONT` | Equipment template | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 217 | `EQUIP_TEMPLATE_MAIN_HAND_SMALL` | Equipment template | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 218 | `EQUIP_TEMPLATE_MAIN_HAND_LARGE` | Equipment template | 32x48 + overscan | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 219 | `EQUIP_TEMPLATE_OFF_HAND_SMALL` | Equipment template | 32x48 | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 220 | `EQUIP_TEMPLATE_OFF_HAND_LARGE` | Equipment template | 32x48 + overscan | `SIX_VIEW_DEFERRED` | technical/non-canon framework |
| 221 | `TOOL_ARCHETYPE_DIAGNOSTIC_SCANNER` | Held tool | 32x32 + 32x48 layer | `PROP_ANGLES` | technical/non-canon framework |
| 222 | `TOOL_ARCHETYPE_REPAIR_WRENCH` | Held tool | 32x32 + 32x48 layer | `PROP_ANGLES` | technical/non-canon framework |
| 223 | `TOOL_ARCHETYPE_CUTTER` | Held tool | 32x32 + 32x48 layer | `PROP_ANGLES` | technical/non-canon framework |
| 224 | `TOOL_ARCHETYPE_MULTITOOL` | Held tool | 32x32 + 32x48 layer | `PROP_ANGLES` | technical/non-canon framework |
| 225 | `TOOL_ARCHETYPE_FLASHLIGHT` | Held tool | 32x32 + 32x48 layer | `PROP_ANGLES` | technical/non-canon framework |
| 226 | `TOOL_ARCHETYPE_MEDKIT` | Held/pack item | 32x32 + 32x48 layer | `PROP_ANGLES` | technical/non-canon framework |
| 227 | `TOOL_ARCHETYPE_DATA_READER` | Held tool | 32x32 + 32x48 layer | `PROP_ANGLES` | technical/non-canon framework |
| 228 | `TOOL_ARCHETYPE_PRYBAR` | Held tool | 32x32 + 32x48 layer | `PROP_ANGLES` | technical/non-canon framework |
| 229 | `TOOL_ARCHETYPE_ROPE_KIT` | Held/pack item | 32x32 | `PROP_ANGLES` | technical/non-canon framework |
| 230 | `TOOL_ARCHETYPE_FIELD_METER` | Held tool | 32x32 + 32x48 layer | `PROP_ANGLES` | technical/non-canon framework |
| 231 | `WEAPON_ARCHETYPE_UNARMED_GUARD` | Combat presentation | 32x48 pose overlay | `TILE_AXES` | technical/non-canon framework |
| 232 | `WEAPON_ARCHETYPE_SHORT_BLADE` | Held weapon template | 32x32 + 32x48 layer | `PROP_ANGLES` | technical/non-canon framework |
| 233 | `WEAPON_ARCHETYPE_LONG_BLADE` | Held weapon template | 32x32 + overscan layer | `PROP_ANGLES` | technical/non-canon framework |
| 234 | `WEAPON_ARCHETYPE_BATON` | Held weapon template | 32x32 + 32x48 layer | `PROP_ANGLES` | technical/non-canon framework |
| 235 | `WEAPON_ARCHETYPE_COMPACT_RANGED` | Held weapon template | 32x32 + 32x48 layer | `PROP_ANGLES` | technical/non-canon framework |
| 236 | `WEAPON_ARCHETYPE_LONG_RANGED` | Held weapon template | 32x32 + overscan layer | `PROP_ANGLES` | technical/non-canon framework |
| 237 | `WEAPON_ARCHETYPE_THROWN` | Held weapon template | 32x32 + 32x48 layer | `PROP_ANGLES` | technical/non-canon framework |
| 238 | `DEFENSE_ARCHETYPE_LIGHT_SHIELD` | Off-hand template | 32x32 + 32x48 layer | `TILE_AXES` | technical/non-canon framework |
| 239 | `DEFENSE_ARCHETYPE_HEAVY_SHIELD` | Off-hand template | 32x32 + overscan layer | `TILE_AXES` | technical/non-canon framework |
| 240 | `WEAPON_FX_GENERIC_HIT_SPARK` | Combat FX | 32x32, 4 frames | `PRESENTATION_STATES` | technical/non-canon framework |
| 241 | `CONSUMABLE_TEMPLATE_HEALTH_SMALL` | Item icon | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 242 | `CONSUMABLE_TEMPLATE_STAMINA_SMALL` | Item icon | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 243 | `CONSUMABLE_TEMPLATE_FOCUS_SMALL` | Item icon | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 244 | `CONSUMABLE_TEMPLATE_RESOLVE_SMALL` | Item icon | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 245 | `CONSUMABLE_TEMPLATE_FIELD_RATION` | Item icon | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 246 | `CONSUMABLE_TEMPLATE_WATER` | Item icon | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 247 | `CONSUMABLE_TEMPLATE_STIMULANT` | Item icon | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 248 | `CONSUMABLE_TEMPLATE_ANTISEPTIC` | Item icon | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 249 | `MATERIAL_TEMPLATE_SCRAP_METAL` | Material icon | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 250 | `MATERIAL_TEMPLATE_WIRE` | Material icon | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 251 | `MATERIAL_TEMPLATE_CIRCUIT` | Material icon | 32x32 | `PRESENTATION_STATES` | technical/non-canon framework |
| 252 | `MATERIAL_TEMPLATE_GLASS` | Material icon | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 253 | `MATERIAL_TEMPLATE_CLOTH` | Material icon | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 254 | `MATERIAL_TEMPLATE_RUBBER` | Material icon | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 255 | `MATERIAL_TEMPLATE_CERAMIC` | Material icon | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 256 | `MATERIAL_TEMPLATE_BATTERY_CELL` | Material icon | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 257 | `MATERIAL_TEMPLATE_SIGNAL_COMPONENT` | Material icon | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 258 | `MATERIAL_TEMPLATE_ADHESIVE` | Material icon | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 259 | `MATERIAL_TEMPLATE_FASTENERS` | Material icon | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 260 | `MATERIAL_TEMPLATE_UNKNOWN_SAMPLE` | Material icon | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 261 | `KEYITEM_TEMPLATE_DOCUMENT` | Key item icon | 32x32 | `PROP_ANGLES` | technical/non-canon framework |
| 262 | `KEYITEM_TEMPLATE_ACCESS_PASS` | Key item icon | 32x32 | `PROP_ANGLES` | technical/non-canon framework |
| 263 | `KEYITEM_TEMPLATE_KEYCARD` | Key item icon | 32x32 | `PROP_ANGLES` | technical/non-canon framework |
| 264 | `KEYITEM_TEMPLATE_MECHANICAL_KEY` | Key item icon | 32x32 | `PROP_ANGLES` | technical/non-canon framework |
| 265 | `KEYITEM_TEMPLATE_MAP_FRAGMENT` | Key item icon | 32x32 | `PROP_ANGLES` | technical/non-canon framework |
| 266 | `KEYITEM_TEMPLATE_AUDIO_LOG` | Key item icon | 32x32 | `PROP_ANGLES` | technical/non-canon framework |
| 267 | `KEYITEM_TEMPLATE_PHOTO` | Key item icon | 32x32 | `PROP_ANGLES` | technical/non-canon framework |
| 268 | `KEYITEM_TEMPLATE_BADGE` | Key item icon | 32x32 | `PROP_ANGLES` | technical/non-canon framework |
| 269 | `KEYITEM_TEMPLATE_SEALED_PACKAGE` | Key item icon | 32x32 | `PROP_ANGLES` | technical/non-canon framework |
| 270 | `KEYITEM_TEMPLATE_DATA_CORE` | Key item icon | 32x32 | `PROP_ANGLES` | technical/non-canon framework |
| 271 | `CONTAINER_TEMPLATE_SMALL_CASE` | Container prop | 32x32 + open state | `PROP_ANGLES` | technical/non-canon framework |
| 272 | `CONTAINER_TEMPLATE_TOOLBOX` | Container prop | 32x32 + open state | `PROP_ANGLES` | technical/non-canon framework |
| 273 | `CONTAINER_TEMPLATE_LOCKER` | Container prop | 32x48 + open state | `PROP_ANGLES` | technical/non-canon framework |
| 274 | `CONTAINER_TEMPLATE_CRATE` | Container prop | 32x32 + open state | `PROP_ANGLES` | technical/non-canon framework |
| 275 | `CONTAINER_TEMPLATE_ARCHIVE_BOX` | Container prop | 32x32 + open state | `PROP_ANGLES` | technical/non-canon framework |
| 276 | `CONTAINER_TEMPLATE_MEDICAL_CASE` | Container prop | 32x32 + open state | `PROP_ANGLES` | technical/non-canon framework |
| 277 | `CONTAINER_TEMPLATE_SIGNAL_CASE` | Container prop | 32x32 + open state | `PROP_ANGLES` | technical/non-canon framework |
| 278 | `CONTAINER_TEMPLATE_PERSONAL_BAG` | Container prop | 32x32 + open state | `PROP_ANGLES` | technical/non-canon framework |
| 279 | `CONTAINER_TEMPLATE_SALVAGE_BIN` | Container prop | 32x32 + state | `PROP_ANGLES` | technical/non-canon framework |
| 280 | `CONTAINER_TEMPLATE_UNKNOWN_LOCKBOX` | Container prop | 32x32 + state | `PROP_ANGLES` | technical/non-canon framework |
| 281 | `UI_INVENTORY_CATEGORY_ALL` | Inventory UI icon | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 282 | `UI_INVENTORY_CATEGORY_EQUIPMENT` | Inventory UI icon | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 283 | `UI_INVENTORY_CATEGORY_CONSUMABLE` | Inventory UI icon | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 284 | `UI_INVENTORY_CATEGORY_MATERIAL` | Inventory UI icon | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 285 | `UI_INVENTORY_CATEGORY_KEYITEM` | Inventory UI icon | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 286 | `UI_ITEM_STATE_EQUIPPED` | Inventory UI | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 287 | `UI_ITEM_STATE_LOCKED` | Inventory UI | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 288 | `UI_ITEM_STATE_NEW` | Inventory UI | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 289 | `UI_ITEM_STATE_DAMAGED` | Inventory UI | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 290 | `UI_ITEM_STATE_QUEST_RELEVANT` | Inventory UI | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 291 | `UI_ITEM_COMPARE_UP` | Inventory UI | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 292 | `UI_ITEM_COMPARE_DOWN` | Inventory UI | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 293 | `UI_ITEM_COMPARE_MIXED` | Inventory UI | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 294 | `UI_ITEM_STACK_FRAME` | Inventory UI | 32x32 overlay | `PRESENTATION_STATES` | technical/non-canon framework |
| 295 | `UI_LOOT_PICKUP_FLASH` | Loot UI FX | 32x32, 4 frames | `PRESENTATION_STATES` | technical/non-canon framework |
| 296 | `UI_CRAFT_RECIPE_ICON` | Craft UI icon | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 297 | `UI_CRAFT_MISSING_PART` | Craft UI icon | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 298 | `UI_CRAFT_READY` | Craft UI icon | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 299 | `UI_ITEM_INSPECT_CURSOR` | Inventory UI | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 300 | `UI_ITEM_BLUEPRINT_DEBUG_GRID` | Developer asset | 32x32 grid | `PRESENTATION_STATES` | technical/non-canon framework |

### Batch 4 — 301–400

| # | Stable asset ID | Family | Native | View set | Canon class |
| ---: | --- | --- | --- | --- | --- |
| 301 | `ARCH_TILE_CONCRETE_WALL_A` | Architecture module | 16x16 tile | `TILE_AXES` | technical/non-canon framework |
| 302 | `ARCH_TILE_CONCRETE_WALL_B` | Architecture module | 16x16 tile | `TILE_AXES` | technical/non-canon framework |
| 303 | `ARCH_TILE_METAL_PANEL_A` | Architecture module | 16x16 tile | `TILE_AXES` | technical/non-canon framework |
| 304 | `ARCH_TILE_METAL_PANEL_B` | Architecture module | 16x16 tile | `TILE_AXES` | technical/non-canon framework |
| 305 | `ARCH_TILE_BRICK_MASONRY_A` | Architecture module | 16x16 tile | `TILE_AXES` | technical/non-canon framework |
| 306 | `ARCH_TILE_PLASTER_A` | Architecture module | 16x16 tile | `TILE_AXES` | technical/non-canon framework |
| 307 | `ARCH_TILE_TILE_FLOOR_A` | Architecture module | 16x16 tile | `TILE_AXES` | technical/non-canon framework |
| 308 | `ARCH_TILE_CONCRETE_FLOOR_A` | Architecture module | 16x16 tile | `TILE_AXES` | technical/non-canon framework |
| 309 | `ARCH_TILE_GRATE_FLOOR_A` | Architecture module | 16x16 tile | `TILE_AXES` | technical/non-canon framework |
| 310 | `ARCH_TILE_ROAD_ASPHALT_A` | Architecture module | 16x16 tile | `TILE_AXES` | technical/non-canon framework |
| 311 | `ARCH_EDGE_CURB_A` | Architecture module | 16x16/32x16 | `TILE_AXES` | technical/non-canon framework |
| 312 | `ARCH_EDGE_RAIL_A` | Architecture module | 16x32 | `TILE_AXES` | technical/non-canon framework |
| 313 | `ARCH_WINDOW_PUBLIC_A` | Architecture module | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 314 | `ARCH_WINDOW_INDUSTRIAL_A` | Architecture module | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 315 | `ARCH_DOOR_PUBLIC_A` | Architecture module | 32x48 | `TILE_AXES` | technical/non-canon framework |
| 316 | `ARCH_DOOR_SERVICE_A` | Architecture module | 32x48 | `TILE_AXES` | technical/non-canon framework |
| 317 | `ARCH_STAIRS_INDUSTRIAL_A` | Architecture module | 64x48 | `TILE_AXES` | technical/non-canon framework |
| 318 | `ARCH_STAIRS_PUBLIC_A` | Architecture module | 64x48 | `TILE_AXES` | technical/non-canon framework |
| 319 | `ARCH_ROOFLINE_URBAN_A` | Architecture module | 64x32 | `TILE_AXES` | technical/non-canon framework |
| 320 | `ARCH_STOREFRONT_MODULAR_A` | Architecture module | 64x48 | `TILE_AXES` | technical/non-canon framework |
| 321 | `INTERIOR_MODULE_SMALL_OFFICE` | Interior module | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 322 | `INTERIOR_MODULE_PUBLIC_LOBBY` | Interior module | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 323 | `INTERIOR_MODULE_WORKSHOP_BAY` | Interior module | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 324 | `INTERIOR_MODULE_MEDICAL_ROOM` | Interior module | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 325 | `INTERIOR_MODULE_STORAGE_ROOM` | Interior module | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 326 | `INTERIOR_MODULE_SECURITY_POST` | Interior module | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 327 | `INTERIOR_MODULE_CONTROL_ROOM` | Interior module | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 328 | `INTERIOR_MODULE_APARTMENT_SMALL` | Interior module | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 329 | `INTERIOR_MODULE_DORM_ROOM` | Interior module | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 330 | `INTERIOR_MODULE_CANTEEN` | Interior module | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 331 | `INTERIOR_MODULE_MARKET_STALL` | Interior/module | 64x64 | `TILE_AXES` | technical/non-canon framework |
| 332 | `INTERIOR_MODULE_ARCHIVE_STACKS` | Interior module | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 333 | `INTERIOR_MODULE_SERVER_ROOM` | Interior module | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 334 | `INTERIOR_MODULE_TRAINING_ROOM` | Interior module | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 335 | `INTERIOR_MODULE_LOCKER_ROOM` | Interior module | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 336 | `INTERIOR_MODULE_SERVICE_SHAFT` | Interior module | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 337 | `INTERIOR_MODULE_BASEMENT` | Interior module | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 338 | `INTERIOR_MODULE_PUBLIC_RECORD_DESK` | Interior module | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 339 | `INTERIOR_MODULE_SMALL_SHOP` | Interior module | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 340 | `INTERIOR_MODULE_TRANSIT_WAITING` | Interior module | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 341 | `PROP_BENCH_PUBLIC` | World prop | 32x16 | `PROP_ANGLES` | technical/non-canon framework |
| 342 | `PROP_CHAIR_OFFICE` | World prop | 16x24 | `PROP_ANGLES` | technical/non-canon framework |
| 343 | `PROP_TABLE_SMALL` | World prop | 32x16 | `PROP_ANGLES` | technical/non-canon framework |
| 344 | `PROP_DESK_TERMINAL` | World prop | 48x24 | `PROP_ANGLES` | technical/non-canon framework |
| 345 | `PROP_TRASH_BIN` | World prop | 16x24 | `PROP_ANGLES` | technical/non-canon framework |
| 346 | `PROP_TOOL_RACK` | World prop | 32x32 | `PROP_ANGLES` | technical/non-canon framework |
| 347 | `PROP_PIPE_VALVE` | World prop | 16x16 | `PROP_ANGLES` | technical/non-canon framework |
| 348 | `PROP_WALL_PANEL` | World prop | 16x24 | `PROP_ANGLES` | technical/non-canon framework |
| 349 | `PROP_FUSE_BOX` | World prop | 16x24 | `PROP_ANGLES` | technical/non-canon framework |
| 350 | `PROP_GENERATOR_SMALL` | World prop | 32x32 | `PROP_ANGLES` | technical/non-canon framework |
| 351 | `PROP_GENERATOR_LARGE` | World prop | 48x32 | `PROP_ANGLES` | technical/non-canon framework |
| 352 | `PROP_LAMP_FLOOR` | World prop | 16x32 | `PROP_ANGLES` | technical/non-canon framework |
| 353 | `PROP_LAMP_WALL` | World prop | 16x16 | `PROP_ANGLES` | technical/non-canon framework |
| 354 | `PROP_BARRICADE_LIGHT` | World prop | 32x16 | `PROP_ANGLES` | technical/non-canon framework |
| 355 | `PROP_CONE_WARNING` | World prop | 16x16 | `PROP_ANGLES` | technical/non-canon framework |
| 356 | `PROP_SIGN_POST` | World prop | 16x32 | `PROP_ANGLES` | technical/non-canon framework |
| 357 | `PROP_PALLET` | World prop | 32x16 | `PROP_ANGLES` | technical/non-canon framework |
| 358 | `PROP_CART_MAINTENANCE` | World prop | 32x24 | `PROP_ANGLES` | technical/non-canon framework |
| 359 | `PROP_CRATE_STACK` | World prop | 32x32 | `PROP_ANGLES` | technical/non-canon framework |
| 360 | `PROP_EMERGENCY_STRETCHER` | World prop | 48x16 | `PROP_ANGLES` | technical/non-canon framework |
| 361 | `ENV_OVERLAY_RAIN_LIGHT` | Environment overlay | 128x64 loop | `TILE_AXES` | technical/non-canon framework |
| 362 | `ENV_OVERLAY_RAIN_HEAVY` | Environment overlay | 128x64 loop | `TILE_AXES` | technical/non-canon framework |
| 363 | `ENV_OVERLAY_FOG_LIGHT` | Environment overlay | 128x64 alpha | `TILE_AXES` | technical/non-canon framework |
| 364 | `ENV_OVERLAY_DUST_LIGHT` | Environment overlay | 128x64 loop | `TILE_AXES` | technical/non-canon framework |
| 365 | `ENV_OVERLAY_WIND_DEBRIS` | Environment overlay | 128x64 loop | `TILE_AXES` | technical/non-canon framework |
| 366 | `ENV_OVERLAY_DAY_CLEAR` | Lighting overlay | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 367 | `ENV_OVERLAY_DUSK` | Lighting overlay | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 368 | `ENV_OVERLAY_NIGHT` | Lighting overlay | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 369 | `ENV_OVERLAY_EMERGENCY_RED` | Lighting overlay | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 370 | `ENV_OVERLAY_BACKUP_POWER` | Lighting overlay | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 371 | `ENV_OVERLAY_POWER_OFF` | Lighting overlay | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 372 | `ENV_OVERLAY_POWER_RESTORED` | Lighting overlay | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 373 | `ENV_OVERLAY_FIRELIGHT_SAFE` | Lighting overlay | 128x64 loop | `TILE_AXES` | technical/non-canon framework |
| 374 | `ENV_OVERLAY_HAZARD_WARNING` | Environment overlay | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 375 | `ENV_OVERLAY_TRACE_INTERFERENCE` | Environment/FX overlay | 128x64 loop | `TILE_AXES` | technical/non-canon framework |
| 376 | `ENV_OVERLAY_CROWD_LOW` | Scene overlay | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 377 | `ENV_OVERLAY_CROWD_HIGH` | Scene overlay | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 378 | `ENV_OVERLAY_DAMAGE_MINOR` | Scene overlay | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 379 | `ENV_OVERLAY_DAMAGE_MAJOR` | Scene overlay | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 380 | `ENV_OVERLAY_CLEANUP_RECOVERY` | Scene overlay | 128x64 | `TILE_AXES` | technical/non-canon framework |
| 381 | `MAP_TILE_DISTRICT_BASE_A` | Map module | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 382 | `MAP_TILE_DISTRICT_ROAD` | Map module | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 383 | `MAP_TILE_DISTRICT_BUILDING` | Map module | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 384 | `MAP_TILE_DISTRICT_PLAZA` | Map module | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 385 | `MAP_TILE_WATER_DRAIN` | Map module | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 386 | `MAP_TILE_GREENSPACE` | Map module | 32x32 | `TILE_AXES` | technical/non-canon framework |
| 387 | `MAP_ROUTE_NORMAL` | Map route | variable 16px segments | `TILE_AXES` | technical/non-canon framework |
| 388 | `MAP_ROUTE_SELECTED` | Map route | variable 16px segments | `TILE_AXES` | technical/non-canon framework |
| 389 | `MAP_ROUTE_BLOCKED` | Map route | variable 16px segments | `TILE_AXES` | technical/non-canon framework |
| 390 | `MAP_ROUTE_UNKNOWN` | Map route | variable 16px segments | `TILE_AXES` | technical/non-canon framework |
| 391 | `MAP_FOG_UNDISCOVERED` | Map overlay | 256x144 mask | `TILE_AXES` | technical/non-canon framework |
| 392 | `MAP_EVENT_MARKER` | Map icon | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 393 | `MAP_QUEST_MARKER` | Map icon | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 394 | `MAP_DANGER_MARKER` | Map icon | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 395 | `MAP_SERVICE_MARKER` | Map icon | 16x16 | `PRESENTATION_STATES` | technical/non-canon framework |
| 396 | `TRAVEL_TRANSITION_WALK` | Travel transition | 128x64, 6-10 frames | `PRESENTATION_STATES` | technical/non-canon framework |
| 397 | `TRAVEL_TRANSITION_INTERIOR` | Travel transition | 128x64, 4-8 frames | `PRESENTATION_STATES` | technical/non-canon framework |
| 398 | `TRAVEL_TRANSITION_STAIRS` | Travel transition | 128x64, 4-8 frames | `PRESENTATION_STATES` | technical/non-canon framework |
| 399 | `WORLD_INTERACT_HIGHLIGHT` | World/UI overlay | 16x16/outline | `TILE_AXES` | technical/non-canon framework |
| 400 | `WORLD_DEBUG_COLLISION_OVERLAY` | Developer asset | scene/grid overlay | `TILE_AXES` | technical/non-canon framework |

### Batch 5 — 401–500

| # | Stable asset ID | Family | Native | View set | Canon class |
| ---: | --- | --- | --- | --- | --- |
| 401 | `UI_PANEL_STORY_FRAME` | UI shell | 9-slice / pixel frame | `PRESENTATION_STATES` | technical |
| 402 | `UI_PANEL_CHARACTER_FRAME` | UI shell | 9-slice / pixel frame | `PRESENTATION_STATES` | technical |
| 403 | `UI_PANEL_STATS_FRAME` | UI shell | 9-slice / pixel frame | `PRESENTATION_STATES` | technical |
| 404 | `UI_PANEL_INVENTORY_FRAME` | UI shell | 9-slice / pixel frame | `PRESENTATION_STATES` | technical |
| 405 | `UI_PANEL_QUEST_FRAME` | UI shell | 9-slice / pixel frame | `PRESENTATION_STATES` | technical |
| 406 | `UI_PANEL_MAP_FRAME` | UI shell | 9-slice / pixel frame | `PRESENTATION_STATES` | technical |
| 407 | `UI_PANEL_SETTINGS_FRAME` | UI shell | 9-slice / pixel frame | `PRESENTATION_STATES` | technical |
| 408 | `UI_PANEL_DEVELOPER_FRAME` | UI shell | 9-slice / pixel frame | `PRESENTATION_STATES` | technical |
| 409 | `UI_CHOICE_CARD_ENABLED` | UI state | stretchable pixel card | `PRESENTATION_STATES` | technical |
| 410 | `UI_CHOICE_CARD_DISABLED` | UI state | stretchable pixel card | `PRESENTATION_STATES` | technical |
| 411 | `UI_CHOICE_CARD_SELECTED` | UI state | stretchable pixel card | `PRESENTATION_STATES` | technical |
| 412 | `UI_BUTTON_PRIMARY` | UI state | stretchable pixel button | `PRESENTATION_STATES` | technical |
| 413 | `UI_BUTTON_SECONDARY` | UI state | stretchable pixel button | `PRESENTATION_STATES` | technical |
| 414 | `UI_BUTTON_DANGER` | UI state | stretchable pixel button | `PRESENTATION_STATES` | technical |
| 415 | `UI_TAB_ACTIVE` | UI state | stretchable tab | `PRESENTATION_STATES` | technical |
| 416 | `UI_TAB_INACTIVE` | UI state | stretchable tab | `PRESENTATION_STATES` | technical |
| 417 | `UI_SCROLL_MARKER` | UI icon | 16x16 | `PRESENTATION_STATES` | technical |
| 418 | `UI_TOOLTIP_POINTER` | UI element | 16x16 / 9-slice | `PRESENTATION_STATES` | technical |
| 419 | `UI_MODAL_FRAME` | UI shell | 9-slice / pixel frame | `PRESENTATION_STATES` | technical |
| 420 | `UI_TOAST_FRAME` | UI shell | stretchable pixel frame | `PRESENTATION_STATES` | technical |
| 421 | `COMBAT_TARGET_MARKER` | Combat UI | 16x16 | `PRESENTATION_STATES` | technical |
| 422 | `COMBAT_ACTIVE_TURN_MARKER` | Combat UI | 16x16 | `PRESENTATION_STATES` | technical |
| 423 | `COMBAT_GUARD_MARKER` | Combat UI | 16x16 | `PRESENTATION_STATES` | technical |
| 424 | `COMBAT_EVADE_MARKER` | Combat UI | 16x16 | `PRESENTATION_STATES` | technical |
| 425 | `COMBAT_HIT_MARKER` | Combat UI | 16x16 | `PRESENTATION_STATES` | technical |
| 426 | `COMBAT_CRITICAL_MARKER` | Combat UI | 16x16 | `PRESENTATION_STATES` | technical |
| 427 | `COMBAT_BLOCK_MARKER` | Combat UI | 16x16 | `PRESENTATION_STATES` | technical |
| 428 | `COMBAT_STAGGER_MARKER` | Combat UI | 16x16 | `PRESENTATION_STATES` | technical |
| 429 | `COMBAT_DOWNED_MARKER` | Combat UI | 16x16 | `PRESENTATION_STATES` | technical |
| 430 | `COMBAT_RECOVER_MARKER` | Combat UI | 16x16 | `PRESENTATION_STATES` | technical |
| 431 | `COMBAT_RANGE_NEAR` | Combat UI | 16x16 | `TILE_AXES` | technical |
| 432 | `COMBAT_RANGE_MID` | Combat UI | 16x16 | `TILE_AXES` | technical |
| 433 | `COMBAT_RANGE_FAR` | Combat UI | 16x16 | `TILE_AXES` | technical |
| 434 | `COMBAT_COVER_LIGHT` | Combat UI | 16x16 | `TILE_AXES` | technical |
| 435 | `COMBAT_COVER_HEAVY` | Combat UI | 16x16 | `TILE_AXES` | technical |
| 436 | `INTERACT_SUCCESS_FLASH` | Interaction FX | 32x32, 4 frames | `TILE_AXES` | technical |
| 437 | `INTERACT_FAILURE_FLASH` | Interaction FX | 32x32, 4 frames | `TILE_AXES` | technical |
| 438 | `CHECK_SUCCESS_MARKER` | Rules feedback | 16x16 | `PRESENTATION_STATES` | technical |
| 439 | `CHECK_FAILURE_MARKER` | Rules feedback | 16x16 | `PRESENTATION_STATES` | technical |
| 440 | `CHECK_CRITICAL_MARKER` | Rules feedback | 16x16 | `PRESENTATION_STATES` | technical |
| 441 | `FX_ABILITY_DISCOVERY_REVEAL` | Ability FX | 64x64, 6-8 frames | `PRESENTATION_STATES` | technical |
| 442 | `FX_ABILITY_UNSTABLE_AURA` | Ability FX | 64x64 loop | `PRESENTATION_STATES` | technical |
| 443 | `FX_ABILITY_LEARNED_AURA` | Ability FX | 64x64 loop | `PRESENTATION_STATES` | technical |
| 444 | `FX_ABILITY_MASTERED_AURA` | Ability FX | 64x64 loop | `PRESENTATION_STATES` | technical |
| 445 | `FX_RESOURCE_DRAIN_HEALTH` | Resource FX | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 446 | `FX_RESOURCE_DRAIN_STAMINA` | Resource FX | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 447 | `FX_RESOURCE_DRAIN_FOCUS` | Resource FX | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 448 | `FX_RESOURCE_DRAIN_RESOLVE` | Resource FX | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 449 | `FX_RESOURCE_RECOVER_HEALTH` | Resource FX | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 450 | `FX_RESOURCE_RECOVER_STAMINA` | Resource FX | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 451 | `FX_RESOURCE_RECOVER_FOCUS` | Resource FX | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 452 | `FX_RESOURCE_RECOVER_RESOLVE` | Resource FX | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 453 | `FX_CONDITION_APPLIED` | Status FX | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 454 | `FX_CONDITION_CLEARED` | Status FX | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 455 | `FX_COOLDOWN_READY` | Ability UI FX | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 456 | `FX_COOLDOWN_LOCKED` | Ability UI FX | 32x32 loop | `PRESENTATION_STATES` | technical |
| 457 | `FX_TRACE_DISCOVERY` | Trace-specific FX | 64x64, 6-8 frames | `PRESENTATION_STATES` | current/provisional canon + technical |
| 458 | `FX_TRACE_TOLERANCE_GAIN` | Trace-specific FX | 64x64, 6 frames | `PRESENTATION_STATES` | current/provisional canon + technical |
| 459 | `FX_TRACE_DIRECTION_LOCK` | Trace-specific FX | 64x64, 6-8 frames | `PRESENTATION_STATES` | current/provisional canon + technical |
| 460 | `FX_TRACE_RECOVERY_SETTLE` | Trace-specific FX | 64x64, 6 frames | `PRESENTATION_STATES` | current/provisional canon + technical |
| 461 | `UI_QUEST_STARTED` | Quest feedback | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 462 | `UI_QUEST_OBJECTIVE_COMPLETE` | Quest feedback | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 463 | `UI_QUEST_OBJECTIVE_FAILED` | Quest feedback | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 464 | `UI_QUEST_COMPLETED` | Quest feedback | 32x32, 6 frames | `PRESENTATION_STATES` | technical |
| 465 | `UI_QUEST_FAILED` | Quest feedback | 32x32, 6 frames | `PRESENTATION_STATES` | technical |
| 466 | `UI_KNOWLEDGE_LEARNED` | Knowledge feedback | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 467 | `UI_KNOWLEDGE_UPDATED` | Knowledge feedback | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 468 | `UI_RELATIONSHIP_SHIFT` | Social feedback | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 469 | `UI_TIME_ADVANCE` | World feedback | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 470 | `UI_LOCATION_DISCOVERED` | World feedback | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 471 | `UI_LOCATION_ARRIVED` | World feedback | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 472 | `UI_WORLD_FLAG_VISIBLE_CHANGE` | World feedback | 32x32, 4 frames | `PRESENTATION_STATES` | technical |
| 473 | `TRANSITION_SCENE_CUT` | Scene transition | 128x64, 4 frames | `PRESENTATION_STATES` | technical |
| 474 | `TRANSITION_FADE_PIXEL` | Scene transition | 128x64, 6 frames | `PRESENTATION_STATES` | technical |
| 475 | `TRANSITION_FLASHBACK` | Scene transition | 128x64, 6-8 frames | `PRESENTATION_STATES` | technical |
| 476 | `TRANSITION_DISCOVERY` | Scene transition | 128x64, 6-8 frames | `PRESENTATION_STATES` | technical |
| 477 | `TRANSITION_QUEST_MILESTONE` | Scene transition | 128x64, 6-8 frames | `PRESENTATION_STATES` | technical |
| 478 | `TRANSITION_ABILITY_EVOLUTION` | Scene transition | 128x64, 8-12 frames | `PRESENTATION_STATES` | technical |
| 479 | `TRANSITION_SAVE_COMPLETE` | System transition | 64x32, 4 frames | `PRESENTATION_STATES` | technical |
| 480 | `TRANSITION_LOAD_COMPLETE` | System transition | 64x32, 4 frames | `PRESENTATION_STATES` | technical |
| 481 | `ACCESS_HIGH_CONTRAST_UI_FRAME` | Accessibility | 9-slice | `PRESENTATION_STATES` | technical |
| 482 | `ACCESS_HIGH_CONTRAST_ICON_MASKS` | Accessibility | 16x16/24x24 set | `PRESENTATION_STATES` | technical |
| 483 | `ACCESS_COLORBLIND_QUEST_SHAPES` | Accessibility | 16x16 set | `PRESENTATION_STATES` | technical |
| 484 | `ACCESS_COLORBLIND_RESOURCE_SHAPES` | Accessibility | 16x16 set | `TILE_AXES` | technical |
| 485 | `ACCESS_TEXT_BACKPLATE` | Accessibility UI | stretchable panel | `TILE_AXES` | technical |
| 486 | `ACCESS_FOCUS_OUTLINE` | Accessibility UI | stretchable outline | `TILE_AXES` | technical |
| 487 | `ACCESS_LARGE_ICON_VARIANTS` | Accessibility | 32x32 set | `PRESENTATION_STATES` | technical |
| 488 | `ACCESS_REDUCED_MOTION_STATIC_TRACE` | Accessibility FX | 64x64 static | `TILE_AXES` | technical |
| 489 | `ACCESS_REDUCED_MOTION_STATIC_TRANSITION` | Accessibility transition | 128x64 static/2-frame | `PRESENTATION_STATES` | technical |
| 490 | `ACCESS_AUDIO_NARRATION_ICON` | Accessibility/UI | 24x24 | `PRESENTATION_STATES` | technical |
| 491 | `DEV_GRID_8PX` | Developer asset | overlay | `TILE_AXES` | technical |
| 492 | `DEV_GRID_16PX` | Developer asset | overlay | `TILE_AXES` | technical |
| 493 | `DEV_SAFE_CROP_SCENE` | Developer asset | 128x64 overlay | `TILE_AXES` | technical |
| 494 | `DEV_PAPERDOLL_ZORDER_LEGEND` | Developer asset | 32x48 overlay | `SIX_VIEW_DEFERRED` | technical |
| 495 | `DEV_PALETTE_SWATCH_MASTER` | Developer asset | swatch sheet | `TILE_AXES` | technical |
| 496 | `DEV_ALPHA_HALO_TEST` | Developer asset | checkerboard test | `TILE_AXES` | technical |
| 497 | `DEV_ANIMATION_ONION_SKIN_GUIDE` | Developer asset | 32x48 overlay | `PRESENTATION_STATES` | technical |
| 498 | `DEV_MAP_NODE_HITBOX_OVERLAY` | Developer asset | 256x144 overlay | `TILE_AXES` | technical |
| 499 | `DEV_ASSET_MISSING_PLACEHOLDER` | Developer/runtime fallback | 32x32 | `TILE_AXES` | technical |
| 500 | `DEV_REFERENCE_NOT_FOR_SHIPPING_WATERMARK` | Reference utility | reference-size overlay | `TILE_AXES` | technical |
