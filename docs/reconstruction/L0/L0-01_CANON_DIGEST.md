# L0-01 — Canon Digest

Layer: **L0 Foundation**
Depends on: nothing
Sources: `content/vertical_slice_01.json`, `docs/GAME_FOUNDATION.md`, `docs/VISUAL_BIBLE.md`, `docs/assets/*`, `docs/world/*`, `docs/systems/*`

> **Authority note.** This digest is a *derived restatement* of canon that already
> exists elsewhere. It exists so that the rest of the corpus can reference canon
> from one place. It does not supersede any source document. Where this digest
> and a source disagree, the source wins.

---

## 1. What canon is authored today

The world is **partially authored**. This matters enormously for the rebuild and
must be stated first, because a rebuilder who assumes a fully-authored world will
invent content and present it as canon.

| Area | State | Source |
| --- | --- | --- |
| Opening story (Platform Nine → Gate Twelve) | **Authored, 19 scenes** | `content/vertical_slice_01.json` |
| Player character (Jack Wilson) | **Identity reference approved** | `docs/assets/references/UI_REFERENCE_CHARACTER_APPROVED_V1.md` |
| NPC_TAMSIN | **Authored identity record** | `content/vertical_slice_01.json` → `characters.NPC_TAMSIN` |
| Power `ABILITY_TRACE_ECHO` | **Authored, 2 techniques** | `content/vertical_slice_01.json` → `powers` |
| Quests (4) | **Authored with stages/objectives** | `content/vertical_slice_01.json` → `quests` |
| Items (6) | **Authored, 5 in opening loadout** | `content/vertical_slice_01.json` → `registries.items` |
| Knowledge facts (8) | **Authored** | `content/vertical_slice_01.json` → `registries.knowledge` |
| Gate Twelve district map | **Authored, 9 nodes, 8 edges** | `content/vertical_slice_01.json` → `world_map` |
| Locations outside the district | **NOT AUTHORED** | — |
| Political entities / factions | **NAMED PROPOSALS, NOT CANON** | `docs/world/GATE_TWELVE_PARENT_WORLD_PROPOSAL.md` |
| Parent region / settlement | **NAMED PROPOSALS, NOT CANON** | same |
| Wider world geography/scale | **SCHEMA + PROPOSAL, SCALE UNLOCKED** | `docs/world/WORLD_GEOGRAPHY_STANDARD.md` |
| Ability/passive corpora | **STRUCTURE AUTHORED, NOT PROMOTED** | `docs/systems/status/` |
| Beasts / creatures | **NOT SPECIFIED IN DOCS** | — |
| Player-visible identity of Jack beyond reference | **PARTIAL** | see §4 |

`WORLD_POLITICAL_ENTITIES.md` and `WORLD_SETTLEMENT_CATALOG.md` explicitly state:
"No kingdom or government is invented here solely to fill the catalog." That
discipline is binding. **Empty means empty, not "to be invented casually".**

**Correction (recorded 2026-10-03, after delegated extraction).** An earlier
draft of this table stated that political entities and parent settlements were
"empty catalogs". That was inaccurate. `GATE_TWELVE_PARENT_WORLD_PROPOSAL.md`
does supply named candidates, and `WORLD_DEVELOPMENT_MASTER_INDEX.md` §901
records them explicitly. They are **proposals awaiting owner decision**, not
absent. The distinction matters: a name exists, but no decision has been taken,
so a rebuild must not treat it as canon. See §1.1.

## 1.1 The Arden proposals — named, not decided

`docs/world/GATE_TWELVE_PARENT_WORLD_PROPOSAL.md` supplies a minimal candidate
parent chain for owner decision. It is a **proposal, not confirmed canon** —
`WORLD_DEVELOPMENT_MASTER_INDEX.md` §901 says so in terms.

| Level | Proposed ID | Working name | Status |
| --- | --- | --- | --- |
| WORLD | `WORLD_PRIMARY_01` | unnamed — name intentionally open | — |
| REGION | `REGION_ALDER_BASIN_01` | Alder Basin | **PROPOSED** |
| POLITICAL/ADMIN | `ADMIN_ARDEN_MUNICIPAL_01` | Arden Municipal Authority | **PROPOSED**, local authority only |
| SETTLEMENT | `SETTLEMENT_ARDEN_CROSSING_01` | Arden Crossing | **PROPOSED** |

**Alder Basin** is proposed as a temperate low-basin transport region.
**Arden Crossing** is proposed as a medium transit/repair city built around an
old regional transport junction rather than a megacity.

**Arden Municipal Authority** would own/operate or regulate civic transit/depot
infrastructure and the Municipal Archive; Workshop Row "may contain private
contractors operating under municipal…" contract.

**How a rebuild must treat this.** These are the *only* named world-level
entities in the project, and they are **undecided**. `WORLD_DEVELOPMENT_MASTER_INDEX.md`
§901 lists them among owner-decision inputs alongside climate logic, the
municipal-parent model and parent-facing route stubs.

Therefore:

- do not canonise `Alder Basin`, `Arden Crossing` or the `Arden Municipal
  Authority` as settled;
- do not delete them either — they are the current best candidate and a rebuild
  that discards them loses the owner's expressed direction;
- the world **name is deliberately open** and must stay open until decided;
- existing Gate Twelve local IDs, W3 coordinates and the eight authored route
  records are **unchanged** by the proposal, so content work proceeds normally.

## 1.2 The ability/passive corpora are structure, not canon

A second correction worth stating loudly, because it governs a large part of
the project.

`docs/systems/status/DOCUMENTATION_UNIT_LEDGER.md` lines 43–45 set the default
for **every catalog record**:

```
design_status: CALIBRATION_PROPOSAL
canon_status: NOT_CANON_UNTIL_PROMOTED
implementation_status: NOT_IMPLEMENTED
```

The ability and passive corpora are therefore **mature as structure** —
verified stable-ID units across ability, passive and technique records — while
being **almost entirely un-promoted and unimplemented**.

A rebuild must not treat an ability or passive record as canon merely because
it is fully specified. Promotion is a separate act.

## 2. The world as authored
Four condensed subsections follow: premise, technology, mystery, tone. The
mystery and the tone are the two most load-bearing, because a rebuild that
gets them wrong produces a game that reads as a different game even when every
mechanic is correct.

### 2.1 Premise

A **district blackout** reaches a **municipal tram depot** before the official
evacuation order does. Emergency floor strips burn red. A maintenance courier
lies unconscious-but-alive beside a **dead relay case** that is too heavy to
carry further. A systems apprentice, **Tamsin**, is holding the depot doors
powered so the remaining passengers can leave.

This is the opening: `OPENING_DEPOT_BLACKOUT`, titled **"The Last Light in
Platform Nine"**.

### 2.2 Technology level and texture

The world is **near-future municipal infrastructure**, not fantasy and not
science fiction. The material vocabulary is deliberately mundane and civic:

- municipal tram depot and evacuation platforms;
- maintenance benches, workbenches, tool storage;
- obsolete municipal relay hardware with status pulse indicators;
- diagnostic readers, salvaged readers, field tools;
- address plates, notice boards, record ledgers, backup lamps;
- service corridors, maintenance stairs, sealed service gates;
- emergency floor strips, emergency lighting, backup power.

The single supernatural element — **Trace Echo** — is described in
mechanical/spatial terms rather than magical ones. It is *not* a voice or a
message. The canon wording is explicit:

> "The sensation is not a voice or a message; it is a spatial afterimage, as if
> recent energy use has left a pressure pattern in the metal around you."
> — `POWER_GATE_TWELVE_SIGNAL`

**Setting character (locked).** `docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md`
§6.1 defines Gate Twelve as **"grounded municipal infrastructure under emergency
pressure"**, explicitly NOT: cyberpunk nightclub architecture, neon city
spectacle, fantasy medieval settlement, sterile sci-fi laboratory, or abstract UI
geometry. Owner direction requires the game "not default to cyberpunk/neon
shorthand". §6.17 adds that Trace/Echo is **"a specific phenomenon, not generic
'magic tech glow'"**.

This single sentence is the most important tonal constraint in the project. The
world does not explain itself through prophecy. It explains itself through
infrastructure.

### 2.3 The central mystery

A **dead municipal relay** — obsolete, casing cold, address plate **physically
scraped away** — nonetheless emits a **faint status pulse repeating from
inside**. Recovering its destination means admitting what someone was trying to
do. The destination resolves to **Service Gate Twelve**, a sealed maintenance
entrance below the depot, while the official evacuation route runs the opposite
direction.

The deeper mystery is that **municipal crews stopped routine work at Gate Twelve
earlier than public records suggest**, and that **some sealed service routes
remain powered when public corridors go dark** — by deliberate design.

The story's answer is deliberately *not* a supernatural revelation. The Archive
lore quest states plainly:

> "It contains no supernatural revelation, but it explains why some sealed
> service routes remain powered when public corridors go dark."
> — `DISTRICT_ARCHIVE`

The intended shape is: **the world is explained by administrative decisions, and
the uncanny is a real but unremarkable residue of infrastructure.**

### 2.4 Tone

Restraint. Fatigue over heroism. The player is competent but untrained, and the
canon is careful never to grant control too early:

- "The first impression is not control."
- "The first controlled use gives you a baseline, not an upgrade."
- "Direction, Not Mastery."
- "A New Route, Not a Free Upgrade."
- "One Hour, No Shortcut."
- "A Method Instead of a Shortcut."

Every power milestone is explicitly framed as *not* a power spike. A rebuild
that makes Trace Echo feel powerful on first acquisition has broken the tone.

## 3. Trace Echo — the power system as authored
The power system is the game's progression spine. It is deliberately
cost-gated: Trace Echo is the only ability in the authored slice, and it is
gated behind stat thresholds, a knowledge fact, a perk, and prerequisite
technique mastery before its second technique unlocks.

### 3.1 Identity

| Field | Value |
| --- | --- |
| Ability ID | `ABILITY_TRACE_ECHO` |
| Family | `sensory_resonance` |
| Form | `latent_trace` |
| Tags | `sensory`, `noncombat`, `signal` |
| Resource path | `power_resources.trace_resonance` |
| Maximum / starting | 10 / 10 |
| Recovery | 2 per hour |

It is a **personal perception**, not a received transmission. The knowledge
record is named `KNOW_TRACE_ECHO_IS_PERSONAL_PERCEPTION`.

### 3.2 Techniques

**`TECHNIQUE_SIGNAL_PULSE`**

| Property | Value |
| --- | --- |
| Stage minimum | `discovered` |
| Requirements | rank 0, mastery 0, knowledge `KNOW_TRACE_ECHO_IS_PERSONAL_PERCEPTION` |
| Cost | focus 3, trace_resonance 2 |
| Cooldown | 10 minutes |
| Mastery gain | 2 (technique), 1 (ability) |
| Drawback | `COND_ECHO_STRAIN` severity 1, 20 min |

**`TECHNIQUE_DIRECTIONAL_TRACE`**

| Property | Value |
| --- | --- |
| Stage minimum | `discovered` |
| Requirements | rank 0, mastery 20 XP, knowledge `KNOW_TRACE_ECHO_PATTERN_STABLE`, perk `PERK_TRACE_TOLERANCE`, perception ≥45, will ≥45, skills.powers ≥10, and `TECHNIQUE_SIGNAL_PULSE` learned |
| Cost | focus 5, trace_resonance 4 |
| Cooldown | 30 minutes |
| Mastery gain | 3 (technique), 2 (ability) |
| Drawback | `COND_ECHO_STRAIN` severity 2, 35 min |

The escalation is deliberate: **double cost, triple cooldown, heavier strain,
gated behind a stat/perk/knowledge wall** — for strictly directional
information that does not yet work reliably.

### 3.3 Strain

`COND_ECHO_STRAIN` ("Echo Strain") is a condition with severity tiers. It
modifies attributes while active and is the mechanic that makes Trace use
pacing-based rather than resource-pool-based. Sensory strain is the game's
primary limiter on ability spam.

### 3.4 Technique stage ladder

From `GAME_FOUNDATION.md`: Unknown → Discovered → Unstable → Learned → Practiced
→ Mastered → Specialized/evolved. Advancement may require combinations of use
count, quality of use, training time, instruction, stat thresholds, specific
events, and resources.

## 4. The player character — Jack Wilson

The player is **Jack Wilson**, established by owner-approved reference
`UI_REFERENCE_CHARACTER_APPROVED_V1`. This supersedes the earlier v1 blueprint
assumption of a generic/customizable body frame.

**Locked consequence.** The 32x48 rig, pivots, equipment anchors, paper-doll
separation and source-native pixel rules remain valid technical contracts. The
**visual identity target is no longer generic**: future player sprites,
portraits, Character panels, equipment-aligned silhouettes and animation masters
must preserve Jack Wilson's approved identity and the approved reference's
human-readable **non-chibi** proportions, hair/face silhouette and
layered-clothing/equipment presentation.

**What the reference does not decide:** gameplay statistics; inventory/equipment
legality; hidden state; collision/hitboxes; exact unseen turnaround views; exact
32x48 anchor positions; animation timing.

**Proportions:** adult human, head-to-height ratio near **1:4**, total visible
height ~44 px at gameplay scale. Not chibi. Not a smooth-painting miniature.

**Opening stats (authored):**

| Attribute | Value | | Skill | Value |
| --- | ---: | --- | --- | ---: |
| might | 30 | | athletics | 20 |
| agility | 35 | | technical_systems | 25 |
| endurance | 35 | | investigation | 20 |
| intellect | 45 | | persuasion | 15 |
| will | 40 | | | |
| perception | 40 | | **Resources** | |
| presence | 30 | | health / stamina / focus / resolve | 100 / 70 / 60 / 50 |

Jack is **intellect-leaning, physically unremarkable**. This is intentional and
must shape both his default art treatment and his progression identity.

## 5. NPC_TAMSIN — canonical identity record

Authored verbatim in `content/vertical_slice_01.json`. This is the single
highest-fidelity character spec in the project and must not drift.

### 5.1 Identity

| Field | Value |
| --- | --- |
| Height class | average |
| Build | slim athletic adult; long forearms; compact stance |
| Skin | medium warm brown |
| Hair | angular layered crop, short, heavy **left**-side fringe |
| Hair palette | near-black with muted cool highlights |
| Eyes | dark brown |

### 5.2 Silhouette anchors (the three that must read in black)

1. high utility-jacket collar
2. narrow cross-body tool satchel
3. rolled **right** sleeve

### 5.3 Role and attachment markers

- small municipal systems badge on **left chest**
- left hip tool loop
- cross-body satchel strap

### 5.4 Permanent mark

- small notch through **right eyebrow**

### 5.5 Forbidden deviations (verbatim)

- no long hair
- no saturated neon clothing
- do not remove the eyebrow notch
- do not replace the cross-body tool satchel with a backpack

### 5.6 Palette anchors

| Token | Hex |
| --- | --- |
| jacket | `#30343B` |
| shirt | `#C9C7BE` |
| trousers | `#24272C` |
| skin shadow | `#8B5F4B` |

### 5.7 Emotion and pose sets

- **Emotions (5):** neutral, focused, concerned, angry, relieved
- **Poses (4):** front, profile, three-quarter, holding diagnostic reader

### 5.8 Anatomical side rule (critical)

For **front-facing** characters:

> **subject LEFT = viewer RIGHT**
> **subject RIGHT = viewer LEFT**

For Tamsin in front view:

| Feature | Anatomical side | Front-view side |
| --- | --- | --- |
| Heavy fringe | Tamsin left | viewer right |
| Badge | Tamsin left chest | viewer right |
| Tool loop | Tamsin left hip | viewer right |
| Eyebrow notch | Tamsin right eyebrow | viewer left |
| Rolled sleeve | Tamsin right arm | viewer left |

**If a rendered image contradicts this table, it is rejected.** This is the
single most frequently violated rule in character pixel art and is restated here
because the whole corpus depends on it.

### 5.9 Tamsin's pronoun

Canon text in `OPENING_TUNNEL` reads: "Tamsin kills the emergency panel, pockets
**her** reader, and follows you beneath the platform." Tamsin is **she/her**.

## 6. Items and opening loadout

| Item ID | Label | Slot | Quality | Modifier | Visual asset |
| --- | --- | --- | --- | --- | --- |
| `ITEM_MAINTENANCE_SEAL` | Maintenance seal | — | — | — | `pixel_item_maintenance_seal_icon.png` |
| `ITEM_DEPOT_JACKET` | Depot utility jacket | body | standard | endurance +2 | icon + paperdoll |
| `ITEM_WORK_GLOVES` | Insulated work gloves | hands | standard | technical_systems +1 | icon + paperdoll |
| `ITEM_SIGNAL_RING` | Signal ring | ring_1 | **uncommon** | perception +1 | icon + paperdoll |
| `ITEM_COURIER_NECKTAG` | Courier neck tag | neck | standard | presence +1 | icon + paperdoll |
| `ITEM_DEAD_RELAY` | Dead municipal relay | — | — | — | icon + 3 state variants |

Five items are `source: opening_loadout`. The Signal Ring is the only
`uncommon`-quality item in the opening loadout, which makes it the first
teaching case for the quality-frame system.

## 7. Knowledge records (8)

| ID | Label |
| --- | --- |
| `KNOW_RELAY_WAS_DELIVERED_BY_COURIER` | Relay courier handoff |
| `KNOW_RELAY_DESTINATION_SERVICE_GATE_12` | Relay destination: Service Gate Twelve |
| `KNOW_TRACE_ECHO_IS_PERSONAL_PERCEPTION` | Trace Echo is personal perception |
| `KNOW_GATE_TWELVE_RECENT_TRACE` | Recent trace below Gate Twelve |
| `KNOW_TRACE_ECHO_PATTERN_STABLE` | Stable Trace Echo pattern theory |
| `KNOW_DIRECTIONAL_TRACE_POINTS_DEEPER` | Directional Trace points deeper below Gate Twelve |
| `KNOW_PLATFORM_NINE_EVAC_PROTOCOL` | Platform Nine evacuation protocol |
| `KNOW_GATE_TWELVE_CREW_WITHDRAWAL` | Gate Twelve crew withdrawal |

These are the **information-as-gameplay** substrate. Several are gated behind
*mundane* records — the two lore-adjacent facts (`..._EVAC_PROTOCOL`,
`..._CREW_WITHDRAWAL`) come from the Archive and Workshop Row respectively, not
from supernatural sources.

## 8. The Gate Twelve district

`world_map.title = "Gate Twelve District"`. Nine nodes with authored coordinates
on a 0–100 map space.

| Node | Title | x | y | Gated by |
| --- | --- | ---: | ---: | --- |
| `PLATFORM_NINE` | Platform Nine | 18 | 36 | — (start) |
| `RELAY_WORKBENCH` | Relay Workbench | 34 | 31 | — |
| `GATE_TWELVE` | Service Gate Twelve | 53 | 48 | — |
| `SERVICE_TUNNEL` | Service Tunnel | 70 | 61 | via Gate Twelve |
| `EVAC_STAIR` | Quiet Stair | 40 | 70 | — |
| `TRACE_CHAMBER` | Trace Chamber | 82 | 39 | via Gate/Tunnel |
| `DISTRICT_PLAZA` | Depot Plaza | 48 | 18 | `world.free_roam_unlocked` |
| `DISTRICT_ARCHIVE` | Municipal Archive | 66 | 16 | `world.free_roam_unlocked` |
| `WORKSHOP_ROW` | Workshop Row | 29 | 16 | `world.free_roam_unlocked` |

Edges (8), with the only two authored travel costs:

- `PLATFORM_NINE` → `RELAY_WORKBENCH`
- `PLATFORM_NINE` → `GATE_TWELVE`
- `PLATFORM_NINE` → `EVAC_STAIR`
- `GATE_TWELVE` → `SERVICE_TUNNEL`
- `GATE_TWELVE` → `TRACE_CHAMBER`
- `SERVICE_TUNNEL` → `TRACE_CHAMBER`
- `DISTRICT_PLAZA` → `DISTRICT_ARCHIVE` — **8 minutes**
- `DISTRICT_PLAZA` → `WORKSHOP_ROW` — **7 minutes**

Note the asymmetry: the story path (Platform Nine → Gate Twelve → Tunnel) has
**no authored travel_minutes**, while the free-roam district edges do. Travel
time is currently specified only for the free-roam layer.

### 8.1 Location character (authored descriptions)

- **Platform Nine** — evacuation platform inside the municipal tram depot. Red
  emergency floor strips. Crowd pressure. The last lit place.
- **Relay Workbench** — a maintenance bench where the dead relay can be examined.
  Tool storage, diagnostic lighting, focal area centered on relay work.
- **Service Gate Twelve** — a sealed maintenance entrance below the depot.
  Heavy municipal maintenance door, central seam, restrained gold/cyan cues.
- **Service Tunnel** — restricted infrastructure running under the evacuation
  route. Pipes, cable trays, maintenance supports, dark central depth.
- **Quiet Stair** — a maintenance stair which exits away from the main
  evacuation flow. Angular stairs, sparse guidance lights, controlled depth.
  Visually contrasts crowded Platform Nine.
- **Trace Chamber** — a controlled space used to reproduce and stabilize Trace
  Echo. Central apparatus/field area, calibration lines, restrained cyan.
- **Depot Plaza** — open space outside the tram depot, the district's temporary
  meeting point. Emergency lighting; foot traffic spreading again.
- **Municipal Archive** — public records annex on backup power. Tall shelving,
  backup lamps, public records terminal, municipal storage palette.
- **Workshop Row** — repair shops and municipal contractors west of the depot.
  Open repair stalls, salvage benches, practical materials.

## 9. Quests

| Quest ID | Title | Category | Stages |
| --- | --- | --- | --- |
| `QUEST_DEAD_RELAY` | (main, untitled in record) | main | RELAY → DECIDE → TUNNEL_ROUTE \| SOLO_ROUTE → COMPLETE; failure → RECOVER |
| `QUEST_GATE_TWELVE_ECHO` | Gate Twelve Echo | side | DISCOVER → PRACTICE → FIRST_USE → RECOVER → COMPLETE |
| `QUEST_TRACE_STABILIZATION` | Trace Stabilization | optional | FOUNDATION → DIRECTIONAL → COMPLETE |
| `QUEST_PLATFORM_NINE_RECORDS` | Platform Nine Records | lore | READ_RECORDS → COMPLETE |

`QUEST_DEAD_RELAY` is the only quest with a failure branch
(`OBJ_ASK_FOR_HELP` in `STAGE_RECOVER`), and the only one with a genuine
**solo/together fork** (`OBJ_CHOOSE_WITH_TAMSIN` vs `OBJ_CHOOSE_SOLO`). Both are
narratively load-bearing and must survive any rebuild.

## 10. Opening flags
All four are `false` at the start of `CONTENT_VERTICAL_SLICE_01`. Three of them
gate free-roam district content and one gates the Trace Echo quest, so they are
the first flags a rebuild should wire.

```
world.free_roam_unlocked        = false
world.district_notices_reviewed = false
world.workshop_rumor_heard      = false
world.trace_echo_quest_started  = false
```

## 11. Tamsin's starting relationship and personality

Starting player→Tamsin: trust 15, respect 5, affection 0, fear 0, suspicion 5,
debt 0, loyalty 0. **She starts suspicious and barely trusting.**

Tamsin personality axes: empathy 55, aggression 20, caution 65, ambition 40,
honesty 70, loyalty 60, curiosity 75, discipline 70. **High caution and high
curiosity with high honesty** — she investigates, she tells the truth, and she
is careful. Any art or dialogue treatment that makes her warm, careless or
deceptive at first meeting contradicts the numbers.

## 12. Design pillars (binding on all reconstruction)

1. **Authored, not improvised.**
2. **Persistent consequence** — choices alter durable state later scenes inspect.
3. **Multiple valid solutions.**
4. **Progress must be earned.**
5. **Characters are stateful actors.**
6. **Information is gameplay.**
7. **Deterministic rules** — same save + seed + action = same resolution.
8. **Pixel-art presentation** — rules layer independent of presentation.

## 13. Visual direction summary

Pixel art is a **product constraint, not a prototype treatment** (`VISUAL_BIBLE.md`).

**UI palette anchors (cross-system):**

| Token | Hex |
| --- | --- |
| Ink | `#10151A` |
| Deep | `#172128` |
| Panel | `#22303A` |
| PanelAlt | `#2D3D48` |
| Paper | `#E9E2CC` |
| Muted | `#9FB0B9` |
| Cyan | `#63D8D1` |
| Gold | `#E2B65F` |
| Danger | `#D66B66` |
| Disabled | `#59666D` |

These are *interface* anchors, not a mandate that every world object use them
literally. World assets may introduce local ramps while preserving readable
relationships with Cyan / Gold / Danger feedback.

**Light and mood:** one dominant light direction per location set. Cyan and gold
are the two "technical/active" accents; red/orange is emergency; Danger red is
reserved for failure and damage. The world reads as **cold infrastructure lit by
its own emergency systems**.

## 14. What a rebuilder must NOT assume

1. Do not assume a wider world exists. Only the Gate Twelve district is authored.
2. Do not invent factions, kingdoms or settlements to fill empty catalogs.
3. Do not assume beasts/creatures exist — no canon defines them.
4. Do not assume Jack's appearance is free. It is Jack Wilson, approved reference.
5. Do not assume Trace Echo is magic, prophecy, or communication. It is a
   spatial afterimage — a personal perception of residual energy in structure.
6. Do not assume abilities are fun to spam. Strain and cooldowns are the design.
7. Do not assume "no supernatural revelation" means "supernatural is false".
   The Archive is mundane; that is not the same as the Trace being mundane.
8. Do not assume `main` is canonical. It contains one README.