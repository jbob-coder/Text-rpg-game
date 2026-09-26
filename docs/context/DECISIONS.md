# Design and Architecture Decisions

This file records accepted, open, conflicting, superseded, and rejected project decisions. It is not an implementation log.

---

## DEC-STAT-001 — Core attribute count and Dexterity split

Status: [CONFLICTING] / OPEN

Existing repository position:
- seven core attributes: `might`, `agility`, `endurance`, `intellect`, `will`, `perception`, `presence`
- current `agility` covers movement, coordination, and reaction

Expanded chat proposal:
- eight core attributes: `STR / CON / AGI / DEX / PER / INT / WIL / PRE`
- separate `DEX` from `AGI`
- use `CON` as dedicated bodily robustness/health-resilience attribute

Reason this is open:
- seven stats reduce UI/balance complexity
- eight stats reduce responsibility overload and can create clearer physical build identity
- changing implemented attributes later may require migration work

Resolution rule:
- evaluate both schemas against combat, stealth, traversal, technical tasks, social play, investigation, injury/recovery, training, powers, and life-simulation decisions before selecting canonical names/responsibilities
- no silent implementation migration before resolution

Related: `CP-2026-09-27-STATS-SCHEMA-01`

---

## DEC-DIR-001 — Slow progression and persistent consequence

Status: [DIRECTION] ACCEPTED

The game is a life-and-decisions text RPG. Slow earned progression, meaningful persistent consequences, and a living stateful world are project-wide direction, not isolated features.

Consequences may affect relationships, knowledge, NPC memory, injuries, inventory/equipment, quests, factions, powers, time, and later scene availability.

Permanent growth should not normally come from trivial or instantaneous actions.

---

## DEC-STATE-001 — Important continuity is structured state

Status: [DIRECTION] ACCEPTED

If later content must react to something, it should normally have structured state and a stable identifier rather than exist only in prose or conversational memory.

Source/tests outrank chat recollection for implementation claims.

---

## DEC-UI-001 — Layered status screen

Status: [DESIGNED] ACTIVE DESIGN

The character/status screen should expose a layered model rather than one power number. Expected sections include identity/progression, core attributes, resources, derived values, abilities, mastery/skills, and active status effects.

Hidden properties may remain undiscovered/locked (`???`) until gameplay reveals them.

The screen must remain readable: deep systems can be expandable rather than placing every internal variable on the primary view.

Exact field names, formulas, layout density, and the seven-vs-eight core-stat schema remain provisional/open where noted in `GAME_DIRECTION_AND_UI.md`.
