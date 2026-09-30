# CANON_RECONCILIATION_REPORT

Status: PHASE_00_COMPLETE
Authority: USER_DIRECTION_2026-09-29
Repository: jbob-coder/Text-rpg-game
Branch: context/shared-game-context
Audit scope: all 24 Markdown files under `docs/world_history/` at commit `4036a51b61368d6e6e578f72d8dd6acdd92e0599`, plus current narrative authority and Academy continuity anchor
Live-game clock effect: NONE

## 1. Purpose

PHASE 00 exists to identify contradictions, naming ambiguity, missing historical bridges, protagonist-sensitive material, and unsafe assumptions before the world-history project expands.

This report does not advance Jack or Elias and does not write the First Interworld War.

## 2. Authority used

Priority for this audit:

1. current explicit user direction;
2. `context/CURRENT_NARRATIVE_AUTHORITY.md`;
3. `docs/world_history/WORLD_HISTORY_AND_REFERENCE_MASTER_BUILD_PLAN.md`;
4. active campaign files under `docs/world_history/`;
5. older draft connective material only where compatible.

Latest user-directed historical requirements used as correction authority:

- the First Interworld War happens, but Homunculi do not cause it;
- Homunculi are primarily a hidden anti-human society/network;
- their broad strategic direction is hostile to human survival;
- collaboration with that hostile network may be treated as a severe crime against humanity and can carry capital punishment in jurisdictions/eras where such a penalty exists;
- Homunculi are an important hidden threat, not the central explanation for every major event;
- world history must be extensive, lived-in, and reusable for scenario construction;
- protagonists' personal/family mysteries must remain unresolved.

## 3. Audit summary

Result: HIGH-IMPACT RECONCILIATION REQUIRED, but the historical foundation is usable.

The pre-Crystal, Veinfall, Early Crystal, Crystal Industrialization, portal-science, ecology, and crystal-classification foundations are broadly compatible with the latest direction.

The main contradiction cluster is Homunculus ontology/history.

The main missing-content cluster is:
- creature/threat encyclopedia;
- power registry;
- Kharvori civilization;
- 2606–2644 interworld expansion;
- First Interworld War causal chain;
- Academy historical evolution;
- present-2670 reference state.

No confirmed case was found in this audit where one promoted stable ID is clearly reused for two unrelated concepts. However, several naming/alias patterns must be normalized before the encyclopedia grows.

## 4. Critical findings

### C-001 — Homunculus ontology conflict
Severity: CRITICAL
State: MUST_RECONCILE

Current files define `SPECIES_HOMUNCULUS_001` as a sapient engineered species/population with varied individual loyalties.

Latest user direction defines "Homunculus" primarily as a hidden anti-human society/network composed of beast-associated beings and collaborators.

These are not the same ontology.

Decision for subsequent work:
- reserve **Homunculus** as the name of the hidden hostile society/network unless later user instruction explicitly reverses this;
- do not treat every beast-derived or engineered sapient organism as automatically Homunculus;
- do not reuse `SPECIES_HOMUNCULUS_001` for the new faction meaning;
- preserve the old file as provenance until PHASE 07 formally supersedes/renames the biological concept;
- create a new `FACTION_HOMUNCULUS_*` family during PHASE 07.

Rationale:
Stable IDs must not change meaning after promotion.

### C-002 — Old Homunculus rebellion/slavery model conflicts with new direction
Severity: CRITICAL
State: MUST_RECONCILE

Affected IDs/files:
- `EVENT_HOMUNCULUS_REBELLION_2587_2601`
- `LAW_HOMUNCULUS_CUSTODIAL_ORDER_2602`
- `STATUS_HOMUNCULUS_ENSLAVED_01`
- `SPECIES_HOMUNCULUS_001.md`
- `HOMUNCULUS_HISTORICAL_DEVELOPMENT_2556_2602.md`
- `ERA_050_PORTAL_EXPANSION_2559_2605.md`
- `PORTAL_EXPANSION_MILESTONES_2559_2605.md`

The older model makes Homunculus identity primarily a created species, labor population, rebellion, defeat, and later slavery regime.

The new model requires a clandestine anti-human society whose membership/activity is itself a grave security concern.

Resolution rule:
- old claims are **PENDING_SUPERSESSION**, not silently deleted;
- useful historical material such as engineered beast-compatible biology, frontier labor abuses, clandestine cells, sabotage, and portal security consequences may be preserved only after being reassigned to compatible entities/events;
- the old rebellion must not be used as the cause of the First Interworld War;
- current narration must not rely on the old Homunculus slavery/citizenship framework until PHASE 07 resolves terminology.

### C-003 — First Interworld War cause is correctly separate, but still undefined
Severity: HIGH
State: INTENTIONAL_GAP

The master chronology already identifies `WAR_FIRST_INTERWORLD_2645_2659` as Human/Kharvori.

This aligns with the latest user direction.

What is still missing:
- first-contact chronology;
- competing territorial/resource doctrines;
- failed diplomacy;
- escalation incidents;
- war trigger;
- factional war aims;
- theaters;
- why the conflict lasts fourteen years;
- why neither side achieves simple total victory;
- why `EVENT_HALCYON_GATE_CONCORD_2660` becomes acceptable.

Rule:
Do not fill this gap until Kharvori history and 2606–2644 expansion are built.

### C-004 — Anti-human collaboration law is missing
Severity: HIGH
State: REQUIRED_NEW_REFERENCE

Current law files cover crystal, ability, augmentation, harvesting, and portal sovereignty.

They do not yet define collaboration with a hostile Homunculus network.

Later law construction must distinguish:
- contact;
- coerced contact;
- intelligence reporting;
- trade;
- material support;
- concealment;
- recruitment;
- sabotage;
- operational collaboration.

Capital punishment must be jurisdiction- and era-specific, not universal.

Future ID family:
`LAW_ANTI_HUMAN_COLLABORATION_*` or another finalized equivalent.

### C-005 — Homunculus precursor technology references need neutralization
Severity: HIGH
State: HOLD_FOR_PHASE_07

`ERA_040_CRYSTAL_INDUSTRIALIZATION_2506_2558.md`,
`CRYSTAL_INDUSTRIAL_MILESTONES_2506_2558.md`, and
`TECH_CRYSTAL_INFRASTRUCTURE_REGISTRY_2506_2558.md`
currently connect biostabilization technology directly to later Homunculus development.

The technology itself remains useful canon.

Until ontology is rebuilt:
- keep the medical/tissue-engineering technology;
- treat "therefore Homunculus" as pending reconciliation;
- do not erase the technical lineage.

## 5. Naming and ID findings

### C-006 — Macro-era alias ambiguity
Severity: MEDIUM
State: NORMALIZE_IN_PHASE_01

Both abstract and concrete era identifiers exist, for example:
- `ERA_EARLY_CRYSTAL_2473` versus `ERA_030_EARLY_CRYSTAL_2473_2505`;
- `ERA_CRYSTAL_INDUSTRIALIZATION` versus `ERA_040_CRYSTAL_INDUSTRIALIZATION_2506_2558`;
- `ERA_PORTAL_EXPANSION` versus `ERA_050_PORTAL_EXPANSION_2559_2605`;
- `ERA_INTERWORLD_EXPANSION` versus planned `ERA_INTERWORLD_EXPANSION_2606_2644`.

These appear to represent aliases, not clearly different eras.

PHASE 01 must choose one rule:
- canonical concrete ID + human-readable alias; or
- macro parent ID + dated child-era IDs.

Do not let both forms become independent records accidentally.

### C-007 — Authority text resembles a stable ID
Severity: LOW
State: CLEANUP

`SPECIES_HOMUNCULUS_001_PLUS_USER_AUTHORIZED_CONNECTIVE_DESIGN`
appears in an authority field and matches the mechanical stable-ID pattern even though it is not intended as a species record.

PHASE 01 should require authority values to use labels that cannot be mistaken for entity IDs.

Recommended:
`Authority: SPECIES_HOMUNCULUS_001 + USER_AUTHORIZED_CONNECTIVE_DESIGN`

## 6. Protagonist mystery audit

### C-008 — Jack/Elias mystery boundary
Severity: PROTECTED
State: PASS_WITH_GUARDRAIL

World-history files mention Jack/Elias mainly to state that historical documentation must not automatically reveal their knowledge or explain their abilities.

No audited world-history file establishes a final answer for:
- Jack's family history;
- Jack's ability origin;
- Elias's family mystery;
- the true origin of Perfect Clone;
- the full meaning of Adrian Voss-related gaps.

Rule:
Use `PROTAGONIST_MYSTERY` for any future world-history record that approaches these subjects.

Do not use omniscient authoring permission to fill protagonist backstory gaps.

## 7. Academy audit

### C-009 — Academy historical identity is intentionally incomplete
Severity: REQUIRED_GAP
State: SAFE

The Academy is protected as a core narrative pillar, but its exact:
- canonical name;
- founding date;
- institutional ancestry;
- city/region;
- war role;
- postwar reform history;

remain undefined.

This is desirable at PHASE 00.

The Academy must later be derived from:
early ability training + beast response + portal security + wartime doctrine + reconstruction needs.

It must not be imported from unrelated Jack projects.

## 8. Creature / monster audit

### C-010 — No operational Creature Codex exists yet
Severity: HIGH
State: REQUIRED_BUILD

Existing ecology documents explain how creatures should fit into ecosystems, but the repository does not yet contain a reusable bestiary with:
- stable species records;
- operational threat levels;
- era availability;
- biome constraints;
- abilities;
- weaknesses;
- response doctrine;
- encounter suitability.

Therefore current history can discuss ecology in principle, but future scenarios cannot yet reliably query "what creature belongs here?"

PHASE 08 and PHASE 09 remain mandatory.

### C-011 — Creature threat levels are undefined
Severity: HIGH
State: REQUIRED_BUILD

There is no promoted standard mapping monster danger to:
- individual lethality;
- group threat;
- intelligence;
- reproduction;
- environmental spread;
- infrastructure damage;
- strategic danger.

Do not assign definitive monster levels until `CREATURE_CLASSIFICATION_STANDARD_V1.md` exists.

## 9. Ability-system audit

### C-012 — Ability families exist; encyclopedia does not
Severity: HIGH
State: REQUIRED_BUILD

Existing historical canon defines broad human ability families:
PHYSICAL, SENSORY, BIOLOGICAL, ENERGY, MENTAL, SPATIAL, TRANSFORMATION, MATERIAL, FIELD, ANOMALOUS.

Missing:
- reusable ability entries;
- cost/limitation standards;
- counter tags;
- medical risk tags;
- legal/military classifications;
- historical appearance;
- creature-specific ability taxonomy.

Do not infer Jack's Steal mechanics from generic world-history ability taxonomy.

## 10. Kharvori and interworld audit

### C-013 — Kharvori reference files are absent
Severity: CRITICAL_FOR_WAR
State: REQUIRED_BEFORE_PHASE_12

The master index requires Kharvori history from their own causal perspective, but no dedicated Kharvori species/civilization files exist in the audited world-history tree.

Required before war construction:
- biology;
- home ecology;
- social structure;
- governments/factions;
- economy;
- technology;
- military doctrine;
- portal/world access;
- pre-human history;
- internal disagreements;
- first-contact expectations.

### C-014 — 2606–2644 is the major chronological bridge
Severity: CRITICAL_FOR_WAR
State: REQUIRED

Current detailed era coverage ends in 2605.
The First Interworld War begins in 2645.

This 39-year bridge must not be summarized in a few paragraphs.

It must establish the world that makes the war possible.

## 11. Stable-ID collision scan

Scope:
All 24 Markdown files under `docs/world_history/` were enumerated from the branch tree and mechanically scanned for the established ID prefixes.

Result:
- repeated IDs were found as expected cross-references;
- no confirmed case was identified where the same promoted stable ID clearly names two unrelated concepts;
- alias ambiguity exists for macro-era IDs as described in C-006;
- one authority string falsely resembles a stable ID as described in C-007.

PHASE 01 should create a formal ID registry/template before the number of records grows substantially.

## 12. Material considered safe to preserve

Unless future evidence conflicts, the following foundations can proceed:

- broadly recognizable pre-Crystal Earth;
- rare anomalous humans before Veinfall;
- natural versus crystal-induced distinction;
- Veinfall in 2473;
- crystal effects across whole ecosystems;
- 11-day primary Veinfall cascade;
- approximately 18-month extended instability;
- gradual crystal industrialization;
- portal science progression;
- artificial portal development;
- early offworld settlement;
- multidimensional crystal classification;
- creature ecology as real ecology rather than encounter inventory;
- PUBLIC / CLASSIFIED / TRUE knowledge separation;
- First Interworld War date range 2645–2659;
- Human/Kharvori core conflict identity;
- Halcyon Gate Concord in 2660;
- present-era anchor 2670;
- Academy as a historically derived pillar;
- protagonist mystery protection.

## 13. Material frozen pending reconciliation

Do not expand these as if settled:

- `SPECIES_HOMUNCULUS_001` as the definitive meaning of "Homunculus";
- universal Homunculus enslavement/custodial present-state model;
- `STATUS_HOMUNCULUS_ENSLAVED_01`;
- `LAW_HOMUNCULUS_CUSTODIAL_ORDER_2602` as uncontested active canon;
- `EVENT_HOMUNCULUS_REBELLION_2587_2601` in its current emancipation-war formulation;
- any direct claim that biostabilization technology necessarily produced the modern hidden Homunculus society.

These records remain preserved for provenance until PHASE 07 rewrites/supersedes them traceably.

## 14. Historical gaps intentionally left open

Do not invent yet:
- ultimate source of crystals;
- ultimate source of natural human abilities;
- exact cause of Veinfall synchronization;
- Kharvori first-contact outcome details;
- First Interworld War trigger;
- protagonist family mysteries;
- origins of Jack's Steal;
- origins of Elias's Perfect Clone;
- exact Academy identity/founding chain.

## 15. Phase-00 completion record

CURRENT_OBJECTIVE:
Audit canon before further historical expansion.

VERIFIED_STATE:
24 world-history Markdown files scanned from branch tree at commit `4036a51b61368d6e6e578f72d8dd6acdd92e0599`, with current narrative authority and Academy anchor checked separately.

COMPLETED:
- Homunculus contradiction mapped;
- war-causation boundary protected;
- protagonist mystery boundary checked;
- Academy gap checked;
- creature-system gaps identified;
- ability-system gaps identified;
- Kharvori/2606–2644 gaps identified;
- stable-ID scan completed;
- era alias ambiguity identified.

IN_PROGRESS:
None for PHASE 00.

NEXT_ACTION:
PHASE 01 — create master document architecture, indexes, templates, stable-ID rules, cross-link rules, and formal separation between readable history-book text and technical encyclopedia records.

BLOCKERS:
None.

ASSUMPTIONS:
"Homunculus" will be treated as the name of a hidden anti-human society/network for future construction unless the user explicitly changes that direction.

UNKNOWNS:
Biological membership composition of the Homunculus network; historical predecessor entities; exact legal framework; exact origin.

DECISIONS:
Do not silently rewrite old Homunculus files during audit. Supersede them traceably in PHASE 07.

RISKS:
Continuing war or scenario design before PHASE 07/08 would propagate incorrect Homunculus and creature assumptions.

FILES_CHANGED_BY_PHASE_00:
- `docs/world_history/CANON_RECONCILIATION_REPORT.md`

VERIFICATION_PERFORMED:
Repository branch tree enumeration + content scan of all current `docs/world_history/*.md` descendants + authority/Academy check.

## 16. Completion gate

PHASE 00: PASS.

No identified high-impact contradiction needs to be silently carried forward.

Conflicted records are explicitly frozen, and the next safe step is PHASE 01.
