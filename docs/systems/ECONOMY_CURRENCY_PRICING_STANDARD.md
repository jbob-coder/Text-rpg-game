# THE GAME — Economy, Currency & Pricing Standard

Status: **APPROVED FIRST-PASS V07 CONTRACT / CURRENCY AND NUMERIC PRICE SCALE NOT YET CANON**
Parents:
- docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md
- docs/systems/WORLD_BALANCE_INTEGRATION_PLAN.md
Related:
- docs/world/WORLD_POLITICAL_ENTITIES.md
- docs/systems/PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md

## 1. Purpose

Define the architecture for money, prices, wages, scarcity and trade without inventing economic numbers before world institutions/resources are ready.

## 2. Current reality

Current vertical-slice gameplay does not require a complete currency/pricing simulation.

No final currency name, denomination or global price scale is locked by this standard.

## 3. Economy ownership

Economy is authoritative game state/data.

UI may request/display transactions but cannot calculate final prices independently.

## 4. Currency model

Future currency record may include:
- currency_id;
- issuer/institution;
- region acceptance;
- denomination/precision;
- legal status;
- exchange relationship when multiple currencies exist.

Do not assume one universal currency until world political/economic canon supports it.

## 5. Price components

A final transaction price may depend on:
- base item/service value;
- local supply/scarcity;
- quality/condition;
- transport;
- tax/fees;
- vendor policy;
- faction/legal access;
- relationship/reputation only when authored;
- illegal-market risk.

Every modifier needs an explainable source.

## 6. Supply and sinks

Sources of value/currency may include:
- work;
- trade;
- quest/institution reward;
- sale of legitimate goods;
- salvage/resources.

Sinks may include:
- services;
- equipment;
- travel;
- treatment;
- taxes/fees;
- repairs if durability exists.

Do not add artificial sinks solely to slow progression.

## 7. Wages

Work compensation requires V10 profession/work contract plus employer/institution.

No generic fixed eight-hour wage loop is defined yet.

## 8. Regional differences

Regional price variation should reflect documented supply, transport, law and institutions.

Avoid arbitrary per-zone multipliers without provenance.

## 9. Inflation/simulation scope

A full agent-based economy is not required.

First implementation may use authored/derived price bands with bounded world-state modifiers.

## 10. Crime/black market

Illegal trade requires:
- law;
- ownership;
- faction/social consequences;
- vendor access.

Not Phase 1 required.

## 11. Player-safe preview

Before purchase/sale, show:
- price;
- quantity;
- known fees;
- affordability;
- legal restrictions known to the player.

Hidden negotiation thresholds or vendor private goals remain hidden.

## 12. Tests

Once implemented:
- deterministic price;
- no negative price/currency;
- regional modifier provenance;
- purchase/sale atomicity;
- affordability;
- save/load;
- hidden vendor state redaction.
