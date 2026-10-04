# THE GAME — Vendor, Service & Ownership Standard

Status: **APPROVED FIRST-PASS V07 CONTRACT / VENDOR RUNTIME NOT IMPLEMENTED**
Parents:
- docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md
- docs/systems/ECONOMY_CURRENCY_PRICING_STANDARD.md
Related:
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
- docs/systems/NPC_SCHEDULE_PRESENCE_STANDARD.md

## 1. Purpose

Define vendors, services and item ownership as world/NPC/institution systems rather than generic menus.

## 2. Vendor identity

A vendor is:
- a persistent NPC;
- an institution/facility;
- or another explicitly authored world entity.

Vendor record:
- vendor_id;
- owner entity;
- location;
- schedule/access;
- inventory source;
- accepted currencies/trade;
- pricing policy;
- restock policy;
- legal/faction requirements;
- services;
- funds if modeled;
- canon status.

## 3. Inventory source

Vendor stock must come from:
- manufactured supply;
- resource chain;
- institution allocation;
- salvage/second-hand;
- authored special stock.

Do not generate arbitrary stock unrelated to world economy.

## 4. Restock

Restock can be:
- fixed authored;
- scheduled;
- supply-driven;
- one-time.

No restock timer is canon until time/calendar/economy support it.

## 5. Services

Services can include:
- treatment;
- diagnostics;
- repair if durability adopted;
- training;
- travel;
- information;
- lodging;
- other authored services.

Services use activity/economy/social requirements rather than item purchase rules when more appropriate.

## 6. Ownership record

Ownership may distinguish:
- legal owner;
- current possessor;
- location/container;
- stolen/disputed status;
- transfer source.

Phase 1 does not require item-instance ownership for ordinary player inventory.

## 7. Theft/crime

No theft system is required yet.

If adopted, taking an owned item must interact with:
- law;
- witnesses/knowledge;
- NPC memory;
- relationship/reputation;
- resale restrictions.

## 8. Access

Vendor/service availability may depend on:
- time/presence;
- faction/institution;
- reputation;
- relationship;
- legal status;
- quest/world state.

UI cannot show inaccessible private stock unless player knowledge permits.

## 9. Atomic transaction

Purchase/sale/service:
1. validate access;
2. validate stock/resources;
3. calculate authoritative price;
4. snapshot touched state;
5. transfer value/item or execute service;
6. append event;
7. commit/rollback atomically.

## 10. Gate Twelve

Current Gate Twelve Phase 1 does not need a vendor.

Workshop Row is a plausible future vendor/service location, but no shop catalog or prices are created by this standard.

## 11. Tests

When implemented:
- schedule/access;
- stock source;
- atomic purchase/sale;
- no duplication;
- restock determinism;
- hidden stock redaction;
- ownership transfer;
- save/load.
