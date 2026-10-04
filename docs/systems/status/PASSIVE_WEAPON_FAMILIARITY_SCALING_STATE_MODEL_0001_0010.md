# THE GAME — Weapon Familiarity Passive Scaling & State Model 0001–0010

Status: **PHASE-C CALIBRATION / NOT CANON / NOT IMPLEMENTED**

Purpose: define bounded scaling and authoritative state categories for `PASSIVE_WPN_0001`–`PASSIVE_WPN_0010`.

## Shared state

Future implementation should distinguish:
- `qualification_state`;
- `ownership_state`;
- `equipment_identity`;
- `equipment_class`;
- `familiarity_state`;
- `practice_history`;
- `handling_context`;
- `maintenance_state`;
- `projection_state`.

## Per-record model

| ID | Effect input | Scaling direction | Hard cap |
|---|---|---|---|
| WPN_0001 | familiar balanced-blade handling penalty | validated practice with matching class | no benefit to unrelated geometry/classes |
| WPN_0002 | familiar recoil disruption | consistent practice with matching recoil profile | recoil physics still applies |
| WPN_0003 | reach/spacing estimation error | practiced long-reach equipment use | physical reach does not increase |
| WPN_0004 | improvised-equipment handling penalty | varied suitable-object practice | unsuitable objects remain unsuitable |
| WPN_0005 | ready/draw transition overhead | rehearsed familiar-equipment motion | no zero-time draw |
| WPN_0006 | sequence/cognitive reload overhead | validated repeated sequence | physical service steps remain required |
| WPN_0007 | grip-transition overhead | practiced approved grips | unsupported grips receive no benefit |
| WPN_0008 | contested retention handling | validated retention practice | no absolute immunity to loss of control |
| WPN_0009 | orientation/alignment awareness | repeated familiar blade handling | no automatic accuracy bonus outside scope |
| WPN_0010 | avoidable ammunition/resource waste | reviewed disciplined use history | does not create ammunition/resources |

## Qualification rules

The compact Wave-001 records currently use:
- practice sessions;
- meaningful equipment uses;
- safety/field review.

Future qualification must:
1. bind practice to valid equipment classes/profiles;
2. count meaningful use once;
3. reject trivial loops;
4. preserve hidden progress;
5. require review where the compact rule specifies it.

## Cross-family overlap watchlist

- Blade Balance ↔ Blades skill;
- Recoil Familiarity ↔ Ranged skill;
- Polearm Reach ↔ Distance Habit;
- Draw Economy ↔ Combat Rhythm / action-speed systems;
- Reload Memory ↔ Procedural Chunking;
- Weapon Retention ↔ physical grip passives;
- Ammunition Discipline ↔ profession/logistics passives.

Same-resolver effects use one capped composition path.

## Required tests

- unfamiliar equipment does not inherit full familiarity;
- duplicate practice events do not double-count;
- equipment replacement with a materially different profile is not treated as identical without a relationship rule;
- familiarity does not alter physical reach or recoil force;
- save/load preserves qualification and ownership exactly once;
- player-safe projection does not reveal hidden thresholds.

No runtime module is claimed here.
