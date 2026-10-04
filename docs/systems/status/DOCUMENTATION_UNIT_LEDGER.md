# THE GAME — Status Corpus Documentation Unit Ledger

Status: **ACTIVE / WAVE 001 STRUCTURALLY VERIFIED**

Purpose: make the owner's “1k documentation” target measurable without equating quality with 1,000 empty Markdown files.

## 1. Documentation unit definition

One documentation unit is one stable-ID structured record that satisfies the minimum counting schema for its record type.

A heading, title, placeholder, TODO, or duplicate does **not** count.

This counting contract is intentionally smaller than the final reconstruction-grade registry schemas. A record can count as a Wave 001 documentation unit while still requiring deeper authoring before canon promotion.

## 2. Wave 001 realized counts

| Type | Minimum counting content | Planned | Realized | Structural result |
|---|---|---:|---:|---|
| Primary ability | ID, name, rarity, family, core law, boundary, resource, status | 47 | 47 | PASS |
| Passive | ID, name, family, effect, acquisition class, visibility, status | 230 | 230 | PASS |
| Technique | ID, parent ability, stage, effect, cost, failure/counter, status | 188 | 188 | PASS |
| Passive unlock path | ID, passive link, condition grammar, risk, hidden-progress rule, status | 230 | 230 | PASS |
| Passive knowledge profile | ID, passive link, public/school/government/faction visibility, rumor/classification, status | 230 | 230 | PASS |
| Awakening profile | ID, ability link, manifestation, hazard, public signal, status | 47 | 47 | PASS |
| Counter profile | ID, ability link, natural/tactical/environmental counter, failure condition, status | 47 | 47 | PASS |
| **TOTAL** |  | **1,019** | **1,019** | **PASS** |

## 3. Verified integrity

Wave 001 structural audit found:
- **1,019** realized records;
- **1,019** globally unique record IDs;
- **0** duplicate IDs;
- **0** dangling ability-parent references;
- **0** dangling passive-parent references.

Audit:
- `STATUS_CORPUS_WAVE_001_AUDIT.md`

## 4. Canon rule

Wave 001 records default to:
- `design_status: CALIBRATION_PROPOSAL`
- `canon_status: NOT_CANON_UNTIL_PROMOTED`
- `implementation_status: NOT_IMPLEMENTED`

Owner-established facts in parent standards remain canon.

## 5. Counting prefixes

Counted stable-ID prefixes:
- `ABILITY_`
- `PASSIVE_`
- `TECH_`
- `UNLOCK_`
- `KNOW_`
- `AWAKE_`
- `COUNTER_`

A record counts once under exactly one primary unit type.

## 6. Quality gate

A unit is invalid if:
- its ID duplicates another;
- mandatory counting fields are missing;
- it contradicts parent canon;
- it is only a cosmetic rename without a distinct rule;
- it leaks hidden requirements into player-safe fields;
- it claims runtime implementation without evidence.

## 7. Count completion is not design completion

Wave 001 has passed the **1,000-unit structural target**.

It has **not** passed final reconstruction-grade schema completion.

The next work is to deepen the existing records rather than immediately multiplying more shallow entries.

Required refinement includes:
- complete primary-ability registry fields;
- complete passive registry fields;
- individualized techniques;
- individualized counters;
- detailed world/institution knowledge;
- legal/social consequences;
- visual/content/test dependencies;
- contradiction and overlap audit;
- explicit canon promotion decisions.

## 8. Current ledger state

**Wave 001 structural target: COMPLETE — 1,019 / 1,019 units verified.**

**Wave 001 reconstruction-grade design target: IN PROGRESS.**
