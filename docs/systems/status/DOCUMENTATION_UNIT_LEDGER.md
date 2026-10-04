# THE GAME — Status Corpus Documentation Unit Ledger

Status: **ACTIVE / REPRODUCIBLE COUNTING STANDARD**

Purpose: make the owner's “1k documentation” target measurable without equating quality with 1,000 empty Markdown files.

## 1. Documentation unit definition

One documentation unit is one stable-ID structured record that satisfies the minimum schema for its record type.

A heading, title, placeholder, TODO, or duplicate does **not** count.

## 2. Countable record types for Wave 001

| Type | Minimum required content | Planned |
|---|---|---:|
| Primary ability | ID, name, rarity, family, core law, boundary, resource, status | 47 |
| Passive | ID, name, family, effect, acquisition class, visibility, status | 230 |
| Technique | ID, parent ability, stage, effect, cost, failure/counter, status | 188 |
| Passive unlock path | ID, passive link, condition grammar, risk, hidden-progress rule, status | 230 |
| Passive knowledge profile | ID, passive link, public/school/government/faction visibility, rumor/classification, status | 230 |
| Awakening profile | ID, ability link, manifestation, hazard, public signal, status | 47 |
| Counter profile | ID, ability link, natural/tactical/environmental counter, failure condition, status | 47 |
| **TOTAL** |  | **1,019** |

## 3. Canon rule

Wave 001 records default to:
- `design_status: CALIBRATION_PROPOSAL`
- `canon_status: NOT_CANON_UNTIL_PROMOTED`
- `implementation_status: NOT_IMPLEMENTED`

Owner-established facts in parent standards remain canon.

## 4. Audit rule

Counts must be reproducible from stable record IDs.

Recommended future validator prefixes:
- `ABILITY_`
- `PASSIVE_`
- `TECH_`
- `UNLOCK_`
- `KNOW_`
- `AWAKE_`
- `COUNTER_`

A record counts once under exactly one primary unit type.

## 5. Quality gate

A unit is invalid if:
- its ID duplicates another;
- mandatory fields are missing;
- it contradicts parent canon;
- it is a cosmetic rename of an existing unit without a distinct rule;
- it leaks hidden requirements into player-safe fields;
- it claims runtime implementation without evidence.

## 6. Current ledger state

Target Wave 001: **1,019 units**.

The exact realized count must be updated only after all referenced calibration files are written and checked.
