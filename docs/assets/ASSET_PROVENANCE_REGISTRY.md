# THE GAME — Asset Provenance Registry

Status: **ACTIVE / RECONCILIATION REGISTRY / INITIAL SEED**  
Repository: `jbob-coder/Text-rpg-game`  
Parent authorities:
- `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`
- `docs/assets/PIXEL_ART_PRODUCTION_AND_REUSE_LEDGER.md`
- `docs/assets/ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md`

## 1. Purpose

Track where each visual asset came from, what transformation produced the runtime artifact, which branch/consumer uses it, what stage it is in, and whether it may be reused.

This prevents:
- silently replacing approved references;
- confusing a PNG export with a source master;
- treating provisional art as canon;
- copying unrelated repository assets;
- losing provenance when branches are stacked;
- reusing assets with mismatched scale/perspective/material/state.

## 2. Registry identity

Every tracked asset requires a stable `asset_id`.

Runtime resource filename is not sufficient identity.

One asset ID may have:
- source master;
- external reference;
- generated working image;
- cleaned pixel master;
- raster export;
- code fallback;
- animation frames;
- state variants.

## 3. Required provenance fields

Each registry entry eventually records:

- asset ID;
- display label;
- asset class;
- owner/location/character/item;
- source authority;
- source path/reference;
- source hash when available;
- source dimensions;
- authoring method;
- transformation history;
- runtime raster path;
- runtime raster hash;
- code fallback path/symbol;
- native size;
- perspective;
- pixel density;
- palette/material family;
- light direction;
- anchor/pivot;
- z-order;
- state meaning;
- animation contract;
- branch;
- commit/HEAD;
- consumer;
- production stage;
- QA evidence;
- canonical approval;
- supersedes/superseded-by;
- reuse compatibility;
- notes.

## 4. Source-authority classes

Use:
- `OWNER_APPROVED_REFERENCE`;
- `REPOSITORY_SOURCE_MASTER`;
- `REPOSITORY_GENERATED_WORKING_ART`;
- `REPOSITORY_CODE_MASTER`;
- `RUNTIME_EXPORT`;
- `EXTERNAL_INSPIRATION_ONLY`;
- `HISTORICAL/UNVERIFIED`.

External inspiration never becomes a runtime source merely because it influenced design.

## 5. Production stages

Use the shared stage vocabulary:

- PLANNED
- BRIEF_LOCKED
- REFERENCE_SELECTED
- SOURCE_MASTER_PRESENT
- RASTER_PRESENT
- CODE_PRESENT
- INTEGRATED
- OPEN_PR_REFINEMENT
- QA_PENDING
- VERIFIED
- CANON_APPROVED
- DEFERRED_INTEGRATION
- SUPERSEDED
- REJECTED

Stage must be branch/HEAD-aware.

## 6. Reuse compatibility signature

Before reuse, compare:
- native pixel density;
- perspective;
- scale;
- anchor/pivot;
- palette/value range;
- light direction;
- material family;
- edge/outline treatment;
- wear/weathering;
- semantic role;
- state meaning;
- z-order;
- actor contrast;
- animation cadence.

A mismatch requires adaptation or a variant.

## 7. Runtime layers

Registry entries should identify intended layer:
1. environment/base;
2. structural module;
3. permanent prop;
4. ambient decal;
5. room actor;
6. actor equipment/held object;
7. state overlay;
8. transient FX;
9. UI portrait/panel art;
10. icon/chrome.

This helps prevent a state overlay being flattened into a base scene.

## 8. Branch awareness

Current project development contains stacked visual PRs.

Every promoted asset must record:
- branch where authored;
- branch where integrated;
- exact consumer branch/HEAD;
- whether later refinement exists;
- whether earlier variant is superseded.

Do not infer that the newest PR number is automatically canonical.

## 9. Initial program-branch raster seed

The audited program tree contained 24 PNG runtime rasters.

The following entries are seeded as **RASTER_PRESENT** on the documentation program branch unless a stronger stage is separately proven.

### Location scenes

- `pixel_platform_nine_blackout_scene.png`
- `pixel_relay_workbench_default_scene.png`
- `pixel_gate_twelve_sealed_scene.png`
- `pixel_service_tunnel_default_scene.png`
- `pixel_evac_stair_default_scene.png`
- `pixel_trace_chamber_idle_scene.png`
- `pixel_district_plaza_open_scene.png`
- `pixel_district_archive_default_scene.png`
- `pixel_workshop_row_default_scene.png`

These require reconciliation against later scene-art PRs and source-master provenance.

### Player

- `pixel_player_gameplay_front_base.png`
- `pixel_player_hair_tech_placeholder.png`

Status note:
- front base is runtime evidence, not final Jack identity;
- hair asset is explicitly placeholder-quality by name and must not become canonical merely through reuse.

### Starting equipment / item visuals

- `pixel_item_depot_jacket_icon.png`
- `pixel_item_depot_jacket_paperdoll.png`
- `pixel_item_work_gloves_icon.png`
- `pixel_item_work_gloves_paperdoll.png`
- `pixel_item_signal_ring_icon.png`
- `pixel_item_signal_ring_paperdoll.png`
- `pixel_item_courier_necktag_icon.png`
- `pixel_item_courier_necktag_paperdoll.png`
- `pixel_item_maintenance_seal_icon.png`

### Dead relay state family

- `pixel_item_dead_relay_icon.png`
- `pixel_item_dead_relay_damaged.png`
- `pixel_item_dead_relay_opened.png`
- `pixel_item_dead_relay_signal_lost.png`

This family demonstrates state variants and should remain separable from base scene art.

## 10. Source/code catalogs to reconcile

Current program branch also contains visual code catalogs including:
- scene;
- raster;
- map;
- markers;
- environment modules;
- props;
- decals;
- overlays;
- story actors;
- equipment slots;
- item quality frames;
- UI chrome/icons/utilities;
- Trace FX/strain.

Each catalog entry must eventually map to an asset registry ID or explicit procedural/fallback classification.

## 11. Jack reference authority

The approved Jack visual reference is documentation/reference input.

It is **not** a runtime sprite.

Production derivatives must record:
- reference authority;
- crop/turnaround interpretation;
- pixel conversion/redraw process;
- body proportions;
- hair/face identity;
- equipment alignment;
- portrait derivation;
- branch/QA.

## 12. Tamsin authority

Tamsin uses authored identity from content/visual documentation.

Any runtime actor/portrait must preserve:
- hair shape;
- skin tone;
- eyebrow notch;
- utility jacket;
- cross-body satchel;
- role markers.

Provenance must distinguish canonical identity specification from a particular sprite export.

## 13. External reference rules

External game/reference material can provide:
- composition ideas;
- hierarchy;
- pacing;
- readability;
- production workflow.

Do not register external copyrighted art as a runtime source.

If a generated/new original asset was inspired by a reference:
- classify reference as `EXTERNAL_INSPIRATION_ONLY`;
- record original production asset separately;
- ensure no protected character/map/UI expression is copied.

## 14. Hashing

When practical, store:
- SHA-256 of source master;
- SHA-256 of runtime export;
- Git blob SHA;
- dimensions.

Hashes identify bytes, not artistic approval.

## 15. Supersession

When an asset is replaced:
- old asset becomes `SUPERSEDED`;
- point to replacement asset ID;
- preserve historical branch/commit;
- remove runtime consumer only after migration;
- do not delete evidence merely to simplify the folder.

## 16. Generated assets

Generated art must still have:
- prompt/brief reference when available;
- date;
- intended asset ID;
- cleanup/pixelization pass;
- source dimensions;
- final native dimensions;
- human/owner approval status if required;
- runtime integration evidence.

A generated image is not automatically production-ready.

## 17. Area packet linkage

Every area packet should list:
- environment base asset IDs;
- structural modules;
- props;
- decals;
- actor sprites;
- portrait/panel assets;
- overlays;
- FX;
- animation assets;
- map preview;
- runtime consumer.

This registry becomes the provenance half of that packet.

## 18. Machine-readable future registry

Target future path:
`content/visual/asset_provenance.json`

Do not create it until:
- ID naming is locked;
- current branch assets are reconciled;
- validation schema is defined.

## 19. Immediate reconciliation queue

1. exact Gate Twelve scene source masters;
2. later Service Tunnel/Quiet Stair refinement branches;
3. map-surface texture branch;
4. Jack front/base/reference relationship;
5. Tamsin room actor source;
6. infrastructure atlas/source modules;
7. Bag/Skills approved references;
8. UI chrome/icon provenance;
9. animated Service Tunnel overlays;
10. asset families not present on program branch but present in open PRs.

## 20. Canon approval rule

An asset becomes `CANON_APPROVED` only when:
- identity/material brief is satisfied;
- provenance is known;
- native scale/perspective matches;
- runtime consumer is known;
- state semantics are correct;
- exact-head visual QA exists;
- replacement/supersession state is recorded.

Presence in the APK is not enough.


## Exact-baseline raster continuation

[Raster delivery evidence](RASTER_DELIVERY_EVIDENCE_2026-10-02.md) and `docs/evidence/raster_bindings_2026-10-02.json` now provide dimensions, SHA-256, Git blob and catalog binding for all 24 program-baseline rasters. Source-authoring lineage, later-branch variant reconciliation, source/raster equality and canon approval remain open.
