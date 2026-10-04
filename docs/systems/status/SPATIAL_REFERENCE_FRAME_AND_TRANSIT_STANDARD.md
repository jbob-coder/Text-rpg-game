# THE GAME — Spatial Reference Frame & Transit Standard

Status: **PROVISIONAL CROSS-TIER DESIGN STANDARD / NOT CANON UNTIL OWNER REVIEW / NOT IMPLEMENTED**

Parents:
- `PRIMARY_ABILITY_WAVE_001_REFINEMENT_COMPLETENESS_AUDIT.md`
- spatial ability detail packets from Uncommon through Legendary.

Purpose: establish one shared reference-frame vocabulary for Blink Step, Spatial Anchor, Fold Step, Spatial Dominion, and World Gate.

## 1. Reference-frame requirement

Every spatial effect must resolve against an explicit frame. No ability may use an undefined absolute-position model.

A future authoritative frame record needs:
- frame ID and type;
- origin/owner;
- position and orientation basis;
- linear/angular motion where relevant;
- gravity/environment context;
- validity state;
- parent frame when nested.

Provisional frame classes:
- `LOCAL_ENVIRONMENT`;
- `PLATFORM`;
- `ANCHOR`;
- `FIELD`.

## 2. General movement rule

Spatial movement must not provide free velocity cancellation or free acceleration merely because position changes.

For atomic relocation, the proposed default is:
**preserve the subject's pre-effect linear velocity in the resolved parent frame unless the ability explicitly defines a velocity transform.**

Therefore:
- Blink Step does not automatically cancel falling velocity;
- Blink Step does not automatically match a differently moving destination platform;
- relocation within one moving platform naturally retains the platform's shared motion.

Exact energy accounting remains a separate blocker.

## 3. Orientation

Atomic self-relocation preserves orientation by default.

A technique may add controlled reorientation only if separately authored and costed.

## 4. Destination validity

A valid atomic destination must:
- be inside permitted range;
- satisfy the parent's endpoint/LOS rules;
- belong to a valid frame;
- have enough free volume for the complete transit envelope;
- pass barrier rules;
- remain valid at commit.

The transit envelope includes the subject and approved carried/equipped items.

If destination validity fails, atomic relocation does not commit.

## 5. Moving platforms

A destination on a moving platform uses that PLATFORM frame for local position validation.

Atomic relocation does not automatically grant the platform's velocity.

A future velocity-matching technique would be a separate capability.

## 6. Vertical relocation

Vertical movement is legal when range, endpoint, and destination rules allow it.

Current velocity and destination gravity still apply after relocation.

## 7. Transit classes

Two classes are required.

### ATOMIC_RELOCATION
Used by Blink Step.
The complete transit envelope commits as one state transition or remains at source.

### APERTURE_TRANSIT
Used by Fold Step and World Gate.
Objects/characters move through an open spatial connection over time.

Aperture transit therefore needs separate rules for:
- throughput;
- exit occupancy;
- closure timing;
- environmental transfer;
- objects extending across the connection.

## 8. Fold Step transform

Fold Step connects two stable local endpoints.

Proposed mapping:
- source-local position maps to destination-local position;
- orientation maps according to endpoint orientation;
- velocity relative to the source endpoint frame maps into the destination endpoint frame.

Any energy difference created by differing endpoint frames must be accounted for by the future energy/reserve standard.

## 9. World Gate transform

World Gate uses calibrated ANCHOR frames.

Each anchor eventually needs:
- endpoint position/orientation;
- parent frame;
- motion;
- calibration version;
- environment metadata;
- ownership/authentication metadata where approved.

Traveler/cargo motion is interpreted locally relative to the source anchor and mapped locally relative to the destination anchor.

World Gate therefore does not depend on one global absolute frame.

## 10. Spatial Anchor

Spatial Anchor binds a target to a selected frame.

Proposed selection hierarchy:
1. explicit calibrated frame;
2. intentional support PLATFORM frame;
3. LOCAL_ENVIRONMENT frame.

An anchor on a moving vehicle therefore remains fixed relative to that vehicle, subject to finite anchor strength.

Anchor does not grant general invulnerability.

## 11. Spatial Anchor contests

A relocation/displacement attempt against an anchor must evaluate:
- anchor strength/state;
- incoming spatial effect strength/state;
- frame validity;
- range/duration;
- resource/control state.

Possible outcomes:
- anchor holds;
- anchor breaks and incoming effect resolves;
- incoming effect fails;
- separately authored unstable outcome.

Rarity alone never decides the contest.

Exact formula remains `TBD`.

## 12. Spatial Dominion

Spatial Dominion owns a bounded FIELD attached to an explicit parent frame.

The field must identify:
- boundary;
- parent frame;
- allowed transform types;
- affected path classes;
- inclusion rules;
- collapse behavior.

A child standard must later decide whether path changes apply to:
- projectiles;
- light;
- sound;
- fluids;
- ability lines;
- navigation/pathfinding.

Until then, “all paths” is not assumed.

## 13. Barrier and LOS rules

A spatial barrier must be an explicit authored state with defined blocked spatial classes.

Direct LOS and remote imagery are different:
- direct LOS may satisfy a visual endpoint requirement;
- mirrors/cameras/screens do not automatically create a valid endpoint;
- sensor knowledge alone is not automatically LOS;
- World Gate uses calibrated anchors rather than LOS.

## 14. Ability interaction matrix

| Ability | Class | Frame rule | Motion rule | Main remaining blocker |
|---|---|---|---|---|
| Blink Step | atomic relocation | local/platform endpoint | preserve pre-effect velocity | carry envelope + numeric limits |
| Spatial Anchor | positional constraint | explicit selected frame | position fixed relative to frame | contest formula |
| Fold Step | local aperture | paired endpoint frames | map source-local to destination-local motion | energy + closure rules |
| Spatial Dominion | bounded path field | FIELD on parent frame | path-specific | path taxonomy |
| World Gate | long-range aperture | calibrated ANCHOR frames | map anchor-local motion | energy/throughput/environment/security |

## 15. Save/state requirements

Future authoritative state may need:
- active anchor IDs and frames;
- active spatial fields;
- gate-anchor calibration/version;
- aperture state;
- cooldown/resource state;
- unresolved contest state.

No UI layer may invent missing frame state.

## 16. Required future tests

- Blink Step preserves pre-effect velocity.
- Blink Step rejects invalid occupied destinations.
- Blink Step behaves consistently within a moving platform.
- Spatial Anchor follows its selected frame.
- Anchor contests do not use rarity alone.
- Fold Step transforms local motion between oriented endpoints.
- Spatial Dominion affects only approved path classes.
- World Gate rejects invalid/outdated anchor calibration.
- World Gate uses destination-anchor local framing.
- Save/load does not duplicate spatial state.

## 17. Remaining design gates

Still open:
- exact velocity/energy accounting;
- angular-motion treatment;
- aperture closure semantics;
- spatial contest formula;
- Spatial Dominion path taxonomy;
- mass/volume limits;
- barrier taxonomy;
- exact save policy during active aperture transit.

This standard resolves the shared frame vocabulary and proposed baseline behavior, but it does not canon-promote any ability.
