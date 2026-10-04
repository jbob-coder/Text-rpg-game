# L0-10 — Layer Stack Authority and Scene Composition

Layer: **L0 Foundation**
Depends on: L0-02 (angle standard), L0-03 (native grid and anchor standard)
Sources: `PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`, `PIXEL_ART_PRODUCTION_AND_REUSE_LEDGER.md`, `ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md`, `GLOBAL_ASSET_REUSE_OCCLUSION_MATRIX.md`

> **Why this is a separate document.** The project publishes **four different
> layer stacks**, each with its own authority and its own scope. They are not
> interchangeable and not contradictory — each answers a different question. A
> rebuild that picks one and applies it everywhere will be wrong somewhere.

---

## 1. The four stacks, and which question each answers

| Stack | Authority | Scope | Question answered |
| --- | --- | --- | --- |
| **A** — 13 layers | `PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md` §2 | any composited scene | What is the general scene stack? |
| **B** — 10 layers | `PIXEL_ART_PRODUCTION_AND_REUSE_LEDGER.md` §3 | production/reuse planning | What is the production grouping? |
| **C** — 10 layers | `ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md` §11 | rooms with actors | What is the room default? |
| **D** — 12 layers | `GLOBAL_ASSET_REUSE_OCCLUSION_MATRIX.md` §3 | occlusion correctness | What occludes what? |
| **E** — 10 entries | `ASSET_PROVENANCE_REGISTRY.md` §7 | provenance taxonomy | Which runtime layer owns this asset? |

**Selection rule.** Stack A for scene design; stack B for production tracking;
stack C when a room contains actors; stack D when occlusion is the question;
stack E for provenance classification. A rebuild states which stack it is using
and why.

## 2. Stack A — the 13-layer scene stack

From `PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md` §2. "Recommended order … may
vary by scene, but **every exception must be explicit**."

| # | Layer |
| ---: | --- |
| 1 | base backdrop / room shell |
| 2 | floor / permanent architecture |
| 3 | permanent environment modules |
| 4 | permanent props |
| 5 | state-dependent environment overlays |
| 6 | interaction props |
| 7 | rear character accessories |
| 8 | room actors / NPC sprites |
| 9 | player sprite when the presentation calls for it |
| 10 | held items/equipment |
| 11 | foreground props/occluders |
| 12 | ability/status FX |
| 13 | selection/focus treatment |

A further `14 dialogue/actor panel` and `15 narrative/action UI` extend the
presentation beyond the composited scene.

**Asset ownership by layer (Stack A §3):**

| Owner | Owns |
| --- | --- |
| **Base environment** | permanent walls; floor; fixed doors whose physical state never changes; structural supports; permanent furniture; broad lighting basis |
| **State overlay** | blackout shadow; emergency lighting; signal response; temporary damage; quest-safe visible changes; powered/unpowered visual state when projected |
| **Prop** | relay; diagnostic reader; container; bench; sign; terminal; door component if separately stateful; movable environmental object |
| **Character actor** | body; hair; identity; pose; visible clothing/equipment; player-safe temporary emotion/condition |
| **UI** | labels; dialogue text; action buttons; interaction affordance; status bars; actor focus panel; map selection state |

**UI does not own whether an NPC exists in the room.** That boundary is the
single most repeated rule in the composition standard and it is non-negotiable.

## 3. Stack B — the 10-layer production/reuse stack

Back to front:

| # | Layer |
| ---: | --- |
| 1 | environment/base scene |
| 2 | structural modules |
| 3 | permanent props |
| 4 | ambient decals |
| 5 | room actors |
| 6 | actor equipment/held-object layers |
| 7 | player-safe state overlays |
| 8 | transient FX |
| 9 | UI focus/panel layer |
| 10 | text/interaction layer |

**Its four rules:**

1. Base art never owns reachability.
2. Overlays never invent hidden state.
3. Actor panels never decide actor presence.
4. State-specific effects remain separable when architecture is unchanged.

Plus: **UI text is not baked into world art unless it is intentionally large
environmental signage.**

### 3.1 Mandatory production groupings

`PIXEL_ART_PRODUCTION_AND_REUSE_LEDGER.md` (2026-10-02 §12) defines twelve
required groupings:

`IDENTITY` · `AREA BASE` · `STRUCTURE` · `PROP` · `STATE OVERLAY` · `ACTOR` ·
`EQUIPMENT/HELD` · `FX/ANIMATION` · `PANEL/PORTRAIT` · `TEXT/SIGNAGE` · `MAP` ·
`UI CHROME`

**Every row must record:** stable asset ID, region/actor owner, stage,
branch/HEAD, source master, raster/export, consumer, reuse class, overlay
compatibility, QA evidence, and replacement/supersession link.

## 4. Stack C — the 10-layer room default

From `ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md` §11:

| # | Layer |
| ---: | --- |
| 1 | environment |
| 2 | structural modules |
| 3 | static props |
| 4 | state overlays **behind** actors |
| 5 | player |
| 6 | NPC room actors |
| 7 | held/equipment overlays |
| 8 | foreground occluders |
| 9 | FX |
| 10 | UI focus/panel layer |

**Override only when documented.**

The distinguishing feature is layer 4: state overlays sit **behind** actors, so
an actor is never washed out by an environmental state effect.

## 5. Stack D — the 12-layer occlusion order

From `GLOBAL_ASSET_REUSE_OCCLUSION_MATRIX.md` §3:

| # | Layer |
| ---: | --- |
| 1 | distant/background environment |
| 2 | terrain/floor |
| 3 | permanent architecture |
| 4 | rear permanent props |
| 5 | rear state overlays |
| 6 | rear actors/entities |
| 7 | main actors/entities |
| 8 | foreground props/architecture |
| 9 | status/injury overlays |
| 10 | ability/environment FX |
| 11 | interaction markers |
| 12 | contextual UI |

**The governing sentence:**

> Scene perspective may override the numerical order, **but never in a way that
> falsifies state**.

This is the occlusion correctness rule. Perspective can change draw order;
state ownership is fixed.

### 5.1 Beast-mixed variant

`ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md` §15.5 adds an 11-item variant
inserting beasts:

`… 6 NPC/story actors · 7 beasts · 8 player … 11 interaction markers · 12
contextual UI`

> Local occlusion may change draw order. **It must not change state
> ownership.**

**Note for rebuilds.** Beast insertion implies creatures exist in the evolved
design. No creature canon is authored today (see L0-01 §1), so this variant is
recorded as a specified-but-unpopulated ordering.

## 6. Stack E — the provenance taxonomy

From `ASSET_PROVENANCE_REGISTRY.md` §7. This classifies the **asset**, not the
draw order:

| # | Runtime layer |
| ---: | --- |
| 1 | environment/base |
| 2 | structural module |
| 3 | permanent prop |
| 4 | ambient decal |
| 5 | room actor |
| 6 | actor equipment/held object |
| 7 | state overlay |
| 8 | transient FX |
| 9 | UI portrait/panel art |
| 10 | icon/chrome |

**Stated purpose:** "prevents a state overlay being flattened into a base
scene." The taxonomy exists to stop the most common structural error.

## 7. Reconciling the stacks

The four stacks agree on substance and differ only in resolution. Mapped to a
single concept:

| Concept | A (13) | B (10) | C (10) | D (12) | E (10) |
| --- | ---: | ---: | ---: | ---: | ---: |
| Environment / base | 1–2 | 1 | 1 | 1–3 | 1 |
| Structural modules | 3 | 2 | 2 | 3 | 2 |
| Permanent props | 4 | 3 | 3 | 4 | 3 |
| Ambient decals | — | 4 | — | — | 4 |
| State overlays | 5 | 7 | 4 (behind actors) | 5 | 7 |
| Actors (NPC/room) | 8 | 5 | 6 | 6–7 | 5 |
| Player | 9 | — | 5 | 7 | — |
| Actor equipment / held | 10 | 6 | 7 | — | 6 |
| FX (ability/status) | 12 | 8 | 9 | 9–10 | 8 |
| UI focus/panel | 13 | 9 | 10 | 12 | 9–10 |
| Text / interaction | — | 10 | — | 11 | — |

**The one substantive disagreement** is where the player sits: stack A places
the player at 9 (after room actors), stack C at 5 (**before** NPC room actors).
A rebuild picks per scene and documents the choice — this is precisely the kind
of exception stack A permits if it is explicit.

## 8. Rules that hold across every stack

1. **Base art never owns reachability.** The engine decides; the map art shows.
2. **Overlays never invent hidden state.** Only engine-visible conditions drive
   overlays.
3. **Actor panels never decide actor presence.** UI does not own NPC existence.
4. **UI text is not baked into world art** unless intentionally large
   environmental signage.
5. **State-specific effects remain separable** when architecture is unchanged.
6. **State ownership is fixed** even when draw order changes.
7. **Ambient loops do not decide hazards.**
8. **Do not flatten a state overlay into a base scene.**
9. **Do not create a unique flattened room image** for one changed lamp, one
   opened item, one entering NPC, or one temporary effect.
10. **Use a full alternate base only when the physical environment materially
    changes.**

## 9. Overlay strategy

Use overlays when architecture is unchanged. Authored examples:

- Gate Twelve Echo-active signal;
- Service Tunnel aftershock;
- Relay Workbench relay-state inspection context;
- Platform Nine blackout;
- Depot Plaza blackout;
- status/ability FX.

The negative list from the same authority — do **not** make a whole new
flattened room image for:

- one changed lamp;
- one open item;
- one NPC entering;
- one temporary effect.

## 10. Animation classes

| Class | Use |
| --- | --- |
| `STATIC` | no motion |
| `AMBIENT_LOOP` | continuous environmental motion |
| `STATE_DRIVEN` | motion triggered by an authoritative state change |
| `CHARACTER_ACTION` | actor-driven motion |
| `TRANSITION` | screen/scene transitions |

Rules:

- integer-safe motion;
- restrained loops;
- reduced-motion behaviour must exist;
- **no hidden-state implication**;
- actor animation does not change actor identity;
- equipment follows rig anchors;
- **ambient loops do not decide hazards**.

## 11. What this means for angle documentation

The layer stacks change how a `SCENE_CAMERA` or `PROP_ANGLES` specification
must read. Per L0-02 §5, a scene's angle documentation must state:

1. which stack it uses;
2. the crop-safe zone for UI;
3. which layer owns each visible element;
4. which states are overlays rather than base changes;
5. any draw-order exception, explicitly declared.

A scene specification that lists pixels without assigning **ownership** is
incomplete, because ownership is what makes an overlay substitutable later.

## 12. Consequences for the rebuild

1. Declare the stack per scene or asset specification.
2. Never merge a state overlay into a base master.
3. Keep `base` and `state` as separate production assets from the first commit.
4. Use stack D when the question is "what covers what"; use stack E when the
   question is "who owns this asset".
5. Record the player-vs-NPC draw-order choice explicitly where it matters.
6. Do not treat the beast-mixed ordering as licence to invent creatures.
7. Record text/signage as its own grouping; never bake it into scene art except
   where deliberately environmental.