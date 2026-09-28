# Reference Audit — REF_BATCH001_CONCEPT_BOARD_A

Status: `REFERENCE_GENERATED`  
Selection status: **NOT selected as a canonical character/item/location reference**  
Use: style-direction probe only

## Persisted reference

- Google Drive file: `REF_BATCH001_CONCEPT_BOARD_A.png`
- Drive file ID: `1JDvlmF_Mfy93rs_Llq5rB444EOUF5Gzr`
- Local/generated resolution: 1536 x 1024 RGB PNG
- SHA-256: `2d52f5364cecd1338e3c4cd0eafdbba7d5575e980f4c3d7856db3c6119e83ec8`
- Production rule: this file must not be packaged in the APK or copied into a production pixel-asset path.

## What is accepted from this board

The following are useful **style directions**, not canonical geometry:

1. crisp, deliberately clustered pixels rather than filtered smooth painting;
2. dark industrial base values suitable for the existing Ink/Deep/Panel Android theme;
3. restrained bright signal accents rather than full-scene neon saturation;
4. modular presentation of body, clothing, bags, held items and accessories;
5. separate portrait and gameplay-sprite thinking;
6. location art with strong landmark silhouettes and controlled focal lighting;
7. compact icon silhouettes designed to read at small scale;
8. ability FX separated from the character body;
9. map/UI icons separated from world art;
10. coherent family presentation rather than unrelated one-off illustrations.

## What is rejected as canon

The generated board contains visual/content decisions not supported by authoritative repository data. They may **not** be copied forward merely because they appear in the image.

### Unsupported/invented item concepts

Examples visible on the board include concepts such as:

- trace compass;
- relay key;
- data module;
- flashlight;
- field notes;
- utility boots;
- messenger bag;
- multi-tool;
- several relay operating states beyond the current authored relay state contract.

These are not current stable item IDs in `CONTENT_VERTICAL_SLICE_01`. If future content authors equivalents, they require their own stable IDs and briefs.

### Unsupported NPC identities

The board depicts:

- a specific wounded courier face/body;
- multiple generic named-looking people/archetypes.

The current opening courier is only a supporting scene character, not a canon identity sheet. The visual appearance on this board is therefore not canonical.

### Unapproved player identity

The board depicts a fixed player face/hair/outfit identity. Current repository content does not define a fixed canonical player face. The player section may be used to study scale/silhouette only.

### Tamsin deviations

The board is not authoritative for Tamsin. Tamsin must instead follow `CHARACTER_PIXEL_BLUEPRINTS.md` and the current character record in `content/vertical_slice_01.json`.

Critical locked Tamsin features remain:

- short angular layered crop;
- heavy **left-side** fringe;
- medium warm-brown skin;
- dark brown eyes;
- high charcoal utility-jacket collar;
- narrow cross-body tool satchel;
- rolled **right** sleeve;
- left-chest municipal systems badge;
- small notch through right eyebrow;
- no long hair;
- no neon clothing;
- no backpack substitution.

Any board detail conflicting with those rules is rejected.

### Unapproved location architecture

The board's exterior panorama and building facades are mood/composition references only. They do not define canonical district architecture, building count, skyline, era details, or map geography.

Named location geometry remains controlled by:

- current content/map definitions;
- Batch 001 location briefs;
- future approved location blueprints.

## Reference decision

This board is classified:

`REFERENCE_GENERATED -> STYLE_DIRECTION_ACCEPTED -> CANON_GEOMETRY_REJECTED`

It is **not** advanced to `REFERENCE_SELECTED` for any specific character, item or named location.

## Reuse boundary

A production artist/agent may use this board to answer:

- how dense should detail feel?
- how should dark industrial values and cyan/gold accents coexist?
- how can a sheet present modular pixel assets?
- how should small icons prioritize silhouette?

A production artist/agent may **not** use it to answer:

- what does the player canonically look like?
- what does Tamsin canonically look like when it conflicts with her identity record?
- which items exist?
- which NPCs exist?
- what exact buildings exist in the district?
- what gameplay states the relay has?

Those questions must come from repository data and approved blueprints.
