# THE GAME — Persistent Adversary Player-Safe Intel Standard

Status: **APPROVED FIRST-PASS V09 CONTRACT / PRIVACY-CRITICAL**
Parent:
- docs/systems/PERSISTENT_ADVERSARY_WORLD_MEMORY_MASTER_PLAN.md
Related:
- docs/systems/NPC_KNOWLEDGE_BELIEF_PRIVACY_STANDARD.md
- docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md

## 1. Purpose

Define the only information about persistent adversaries that may cross from authoritative hidden state into player-facing UI.

## 2. Core rule

The adversary system must project what Jack/player side knows, not what the engine knows.

A raw persistent-adversary record must never be sent to Compose.

## 3. Intel categories

Potential player-safe fields:
- contact/identity level;
- known name/alias;
- known faction/role;
- visible portrait/silhouette when appropriate;
- last known location;
- last encounter summary;
- visible injury/scar;
- observed equipment;
- observed techniques;
- known behavior/tactics;
- rumor entries;
- known status such as captured/dead only when learned;
- confidence/source labels when UX uses them.

## 4. Hidden fields

Never expose by default:
- private goals;
- exact utility scores;
- future route;
- hidden current location;
- adaptation candidate list;
- secret equipment preparation;
- unknown ability list;
- faction private orders;
- recurrence cooldown internals;
- succession candidates;
- objective truth behind rumors.

## 5. Knowledge sources

Intel can originate from:
- direct observation;
- prior encounter;
- NPC testimony;
- faction/public records;
- investigation;
- rumors;
- ability/sensor when canon.

Each field should be traceable to a knowledge source when needed.

## 6. Identity progression

Suggested display states:
- unknown contact;
- recognized individual/description;
- known alias/role;
- identified name;
- richer known profile.

The stable internal ID does not need to be displayed.

## 7. Last known location

A last-known location is not current truth.

UI must distinguish:
- current confirmed;
- recently observed;
- rumor;
- stale last known.

Do not update it just because the engine moves the adversary off-screen.

## 8. Injury/intel

A visible injury can become known through observation.

Internal severity/recovery timer remains hidden unless another system reveals it.

## 9. Adaptation feedback

The player may discover adaptation through:
- observed changed gear;
- changed tactics;
- dialogue;
- rumor.

Do not display “counter unlocked because you used X” unless a deliberate diagnostic/knowledge mechanic supports it.

## 10. UI surfaces

Future safe consumers may include:
- Story/current location;
- quest/intel journal;
- map rumor/last-known marker;
- tactical contact panel;
- People/relationship screen if appropriate.

A dedicated “rival screen” is not mandatory and must not drive the domain architecture.

## 11. Accessibility

If intel relies on color/icons, include text/shape equivalents.

Hidden information must remain hidden in accessibility descriptions too.

## 12. Tests

Required:
- unknown identity redaction;
- hidden current location redaction;
- stale last-known labeling;
- observed equipment only;
- rumor vs verified distinction;
- no AI/adaptation internals;
- accessibility strings preserve privacy;
- save/load knowledge/intel source.
