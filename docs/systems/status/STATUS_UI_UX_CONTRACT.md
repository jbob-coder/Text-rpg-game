# THE GAME — Status UI UX Contract

Status: **ACTIVE TARGET-GAME UX CONTRACT / IMPLEMENTATION DEFERRED**

Parents:
- `../STATUS_UI_ABILITIES_AND_PASSIVES_MASTER_PLAN.md`
- `STATUS_UI_CORE_CONTRACT.md`
- `STATUS_KNOWLEDGE_VISIBILITY_STANDARD.md`
- `../android/APPLICATION_UX_MASTER_PLAN.md`

Purpose: define how Status, Level, primary ability, techniques, and passives should be presented without exposing hidden engine truth or turning the game into a menu-first experience.

## 1. Product role

Status UI supports the world/story experience.

It must:
- explain the character's known state;
- support planning and training decisions;
- show consequences and progression;
- preserve mystery/knowledge asymmetry;
- remain secondary to current-location/story play.

It must not become an omniscient database.

## 2. Data authority

The engine owns authoritative truth.

Presentation receives a player-safe projection.

The Status screen must never infer hidden values from:
- missing slots;
- array lengths;
- catalog counts;
- internal IDs;
- debug fields;
- implementation-only enums;
- hidden progress counters.

## 3. Primary Status surface

Recommended sections:
- identity summary;
- Level / XP information that is legitimately known;
- core attributes/resources;
- conditions/injuries;
- primary ability;
- known techniques;
- revealed/active passives;
- skills/profession/class/ranks where defined elsewhere;
- equipment summary;
- knowledge/notes links where justified.

Final navigation placement remains governed by the Android UX master plan.

## 4. Primary ability card

Player-safe fields may include:
- public/self-known display name;
- rarity the character is allowed to know;
- family/classification if known;
- concise known description;
- mastery/control state;
- known resource burden;
- known techniques;
- discovered drawbacks;
- discovered counters;
- known evolution information only if discovered.

Do not show:
- hidden true rarity;
- undiscovered techniques;
- classified government interpretation;
- unrevealed evolution;
- hidden cosmic/system properties.

## 5. Technique presentation

Each known technique should support:
- name;
- concise effect;
- current mastery/proficiency if the game exposes it;
- cost/resource hint;
- target/range summary;
- known failure warning;
- training/discovery provenance where useful.

Unknown techniques should not appear as a row of question marks unless the character has legitimate knowledge that additional techniques exist.

## 6. Passive presentation

Before qualification:
- no passive name;
- no icon;
- no locked row;
- no percentage;
- no “2 of 10 hidden passives” count.

After qualification/reveal:
- show name;
- show known effect;
- show active/revealed state;
- optionally show acquisition provenance if designed;
- do not reveal undiscovered upgrade/evolution paths.

## 7. Passive reveal event

A passive reveal should be clear enough that the player understands a durable state change occurred.

The reveal should identify:
- passive name;
- known effect;
- immediate activation state;
- source/provenance only if player-safe;
- any known drawback.

It should not disclose the hidden numeric threshold that was just satisfied unless the design explicitly says the character learns it.

## 8. Level / XP presentation

Because the exact XP curve/reward model remains open:
- do not hard-lock a final bar design yet;
- UI must support exact XP if canon later exposes it;
- UI must also support partial/qualitative progress if visibility rules limit knowledge;
- Level 100 should have exceptional presentation if reached, but not tease ordinary users with a normal respec button.

## 9. Level-100 exception UX

No implementation until the Level-100 child design is complete.

Future UX must:
- make permanence/risk explicit;
- show what is lost/retained;
- prevent accidental confirmation;
- separate public historical record from private system choice;
- support safe interruption/recovery around irreversible state changes.

## 10. Knowledge-state labels

Useful player-facing states may include:
- known;
- partially known;
- rumored;
- classified/withheld where the character legitimately knows something is withheld;
- disputed;
- false belief only when the character currently believes it.

Do not label something “false” to the player before they have evidence that it is false.

## 11. Awakening event presentation

The age-18 awakening is a story/world sequence first.

Status presentation should support:
- initial private readout;
- public classification view;
- school/government record differences;
- temporary medical/safety state;
- reaction sequence;
- recruiter/authority follow-up.

Do not reduce awakening to a single loot-style rarity popup.

## 12. Error and uncertainty states

The UI must support:
- unreadable/unstable classification;
- incomplete knowledge;
- conflicting records;
- outdated public classification;
- projection failure;
- missing content asset;
- unsupported schema;
- save/load mismatch.

Errors must not fabricate game truth.

## 13. Responsive/mobile rules

Inherit application-wide requirements:
- phone-first touch targets;
- scalable text;
- low-end Galaxy A03-class performance target;
- portrait/landscape only where product support is explicitly enabled;
- avoid desktop-first dense tables;
- keep primary art/story visible when Status is contextual rather than full-screen.

## 14. Accessibility

Status UI needs:
- scalable text;
- high contrast;
- non-color-only rarity/condition markers;
- reduced motion;
- screen-reader/narration compatibility where supported;
- flash-safe passive/level/ability reveal effects;
- clear focus order;
- large touch targets.

## 15. Pixel-art presentation

Use:
- nearest-neighbor;
- correct source aspect;
- authored icons/frames;
- composited overlays;
- restrained FX.

Do not:
- smooth pixel art;
- replace character identity with procedural geometry;
- flatten temporary states into duplicate permanent assets when overlays suffice.

## 16. Developer/debug separation

Developer Status tools may expose:
- full hidden catalog;
- requirement counters;
- true rarity;
- debug IDs;
- validation state.

These must be visibly and architecturally separate from player UI.

A debug build must not accidentally ship hidden truth into ordinary projection models.

## 17. Save/load behavior

Presentation preferences may be application-owned.

Gameplay Status state belongs to authoritative gameplay/save systems.

UI should reconstruct from authoritative projected state after load; it should not maintain a second competing gameplay truth.

## 18. Reconstruction acceptance

A future developer must be able to determine:
- what the player can see;
- what remains hidden;
- why it is hidden;
- how ability/technique/passive information appears;
- how awakening differs from ordinary Status inspection;
- how uncertainty/classification is represented;
- how mobile/accessibility constraints affect layout;
- how debug tools avoid leaking hidden data.
