# THE GAME — Story / Engine / Class / Ability Integration Audit — 2026-10-29

**Status:** WORKING-BRANCH EVIDENCE + PROPOSAL / NOT OWNER-APPROVED CANON / NOT MERGED  
**Repository:** jbob-coder/Text-rpg-game  
**Baseline authority branch:** docs/master-game-development-program  
**Verified initial baseline:** bc7d28b70bccaf57d2f38dfda0467b82e4bfe32d (2026-10-29)  
**Working branch:** work/story-engine-class-ability-20261029  
**Owner work intent:** story development, engine testing, class and ability refinement.  
**Coordination:** Independent owner-directed bounded contribution; does not impersonate Nodus, Veyra, Kestrel, Veyr, Quorix, Rivet or Strata, reactivate a Drive entity, seize Silex's D-072 claim, or claim D-084 DONE. D-084 remains governed by the live Bulletin, Drive activation and canon acceptance gates.

## 1. Verified authorities and boundaries

| Scope | Current evidence | Status / decision |
| --- | --- | --- |
| Historical world origin | [Drive primary H-01–H-36](https://docs.google.com/document/d/1FWyk7YzDmkb2DwOdkRAAHl0gNpVCRVPAiFNfEfSia1Q/edit) and [Drive canon hub](https://docs.google.com/document/d/1q8R9Yli-zexcOx0qzzgTNHkpssL2c8mbdFQmJH5SxIE/edit) | Owner narrative decisions; formal migration into game continuity still subject to WD-001 |
| Novella | [Volumen I v0.9.1](https://docs.google.com/document/d/1HEhArzECznhRgGGV7yeXTQdJRLHn15I-DsqdT59HQIg/edit); [Volume II candidate v0.3.8](https://docs.google.com/document/d/1pT_HlkZWa9bUaDangqsp99HxY37Lg1wgavUaqb9NF3Q/edit) | Separate editorial candidates, not validated game scenes |
| Detailed continuation | [New proposed chapter II](../story/PROPOSED_VOLUME_II_CHAPTER_02_2026-10-29.md) | Scene-composite hypothesis, NOT canon or content pack |
| Playable proof | content/vertical_slice_01.json; tests/test_vertical_slice.py | Gate Twelve / The Dead Relay is provisional_canon and has existing authored branch/save tests; not equivalent to the crystal-world historical novel |
| Rules ownership | src/textrpg/core.py, powers.py, progression.py, quests.py, persistence.py | Python owns authoritative gameplay state; Android consumes projections |
| Class design | docs/systems/COMBAT_CLASS_CATALOG.md; docs/systems/PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md | Seven **target** combat/adventure classes; not persisted/implemented as classes |
| Ability design | docs/systems/status/PRIMARY_ABILITY_CATALOG_INDEX.md | 47 first-wave **proposal** ability IDs across rarity categories, not installed abilities |
| Current engine correction | src/textrpg/powers.py and tests/test_powers.py on this branch | Discovery dependency cycles rejected at authored catalog validation; separate existing tests and CI required for completion |

## 2. Story progression and player-knowledge firewall

Confirmed historical constraints:
- The first portal openings, rips, intelligent invading civilization, beasts and the System occur in the same outbreak, not necessarily in one second or with universal witness knowledge (H-32–H-36).
- Beasts already possess crystals before crossing and are distinct from the advanced intelligent invaders (H-09/H-16/H-35).
- The first terrestrial war starts after the System appears; territorial truce is neither total peace nor confirmed victory (H-12/H-13).
- Humans have one randomized principal ability and any subskills arise from that one ability (H-05/H-06); perception of fate is a possible cultural belief, not a real assignment law.
- The celestial tablet is unknown to invaders and cannot be displayed to players/NPCs without a lawful in-world evidence path (H-03/H-04).

**Critical unresolved canon:** WD-001 fictional-world/Tierra identity, absolute dating and post-Crystal era abbreviation, chronological distance from truce to playable era, first forge relative to the war, story protagonist Jack/Steal vs Gate Twelve/Trace Echo, and the legal status of Smith in the world's social institutions. AC = Antes del Crystal. No synthetic post-Crystal abbreviation.

For a future quest, distinguish: (C) author-confirmed world truth, (O) observable event, (K) character knowledge with source, (R) rumor/false belief, and (I) actually encoded engine action. Example: a broken support may be (O), a rumored beast (R), a verified inspection record (K), but no player-safe narration may transform rumor into confirmed beast involvement (C) without observation/proof. Omniscient literary knowledge is never a substitute for state. Persistent NPCs also need the same provenance distinctions.

The chapter-II proposal offers an evidence-bearing decision, **not** an automatic global-world quest: protect people, investigate cause, or attempt bounded repair. For implementation it needs a separate, approved content-pack ID, world placement, available scene transitions, quest graph, stable actor IDs, visibility rules, NPC memory/relationship consequences and save/resume proof. The three routes are not currently added to the Gate Twelve proof.

## 3. Classes: acceptance-grade design connections, not runtime promises

Current catalog target families and proof opportunities:

| Target family | Defining evidence | Sample scene contribution | Runtime ownership |
| --- | --- | --- | --- |
| Vanguard | Protection/control under pressure | Keep people clear of an unstable passage | Legal tactical actions + actual protection event |
| Skirmisher | Movement/position/precision | Reach a difficult inspection point via verified route | Navigation/geometry/athletics/precision |
| Operator | Safe manipulation of complex equipment | Diagnose and repair within known material limits | Technical skills, equipment state, action result |
| Field Specialist | Survival/extraction/readiness | Stabilize an injured or exhausted traveler | World survival/medical/resources |
| Investigator | Evidence to warranted knowledge | Separate damage evidence from rumors | Investigation/knowledge provenance |
| Envoy | Trust, negotiation, bounded social leverage | Explain the closure, reduce harmful dispute | Relationship/social evidence; no guaranteed persuasion |
| Ability Specialist | Control of one earned primary ability | Assess whether using existing power is safe | Existing ability/technique mastery/resource systems |

**Class is earned discipline**, not a menu choice or new principal power. A later class award requires Foundation -> Practice -> Field Proof -> Specialization according to the class master documents. The evidence can be accumulated by choices and practice, but a quest completion must not blindly award class rank, global level or an unrelated skill.

**Smith distinction:** owner decisions H-20–H-27 treat Smith as a forging class/skill/profession concept. Forging output depends on existing core properties and Smith competence, not transmutation of hardness into unrelated properties. A core effect may address weapon or wielder according to its nature; avoid automatic duplication and runaway scaling. Smith is neither a second ability nor equivalent to the seven combat families. There is no accepted smith formula, rarity exception or save record at this checkpoint.

**Future schema proposal, not accepted:** evidence records should reference event_id, actor_id, subject_domain, subject_id, world_time, source_action, conditions, outcome, visibility, canonical_provenance, replay_id and source_revision. Do not add these to current GameState or save schema before migration gate. Existing history, quest and knowledge records must be assessed first; avoid creating duplicate ownership.

## 4. Abilities and technique-graph engine defect

**Observed original behavior:** validate_power_definitions checked direct self-reference and unknown prerequisite technique IDs but did not traverse mutual or longer discovery prerequisite graphs. Example: TECHNIQUE_A requires TECHNIQUE_B, while B requires A; both are valid IDs, but neither can be first discovered from normal progression. The quest graph already has Kahn-based cycle detection in src/textrpg/quests.py, providing a local engineering pattern.

**Bounded implementation on this branch:** validation builds a graph from each technique's discovery_requirements.techniques and rejects every directed cycle before gameplay. Per-technique use-time requirements remain independent; already-discovered techniques can legitimately have other usage requirements. Static validation does not mutate GameState, history, or resources.

**New test cases:**
1. Two-technique mutual discovery cycle rejected.
2. Three-technique discovery cycle rejected.
3. Acyclic chain accepted.
4. Usage-only mutually-referencing prerequisites are not mistaken for discovery cycles.

**Impact:** no schema migration; only authored catalog validation is stricter. An existing authored catalog with a true cycle will now fail early and must be repaired, not silently bypassed. Explicit owner/manual grants, if ever authorized, require separate decision; current validator assumes progression can start without pregranted techniques.

## 5. Execution/acceptance matrix

| Test gate | Command / evidence | Required outcome |
| --- | --- | --- |
| Python syntax and import | python -m compileall -q src tests | No syntax errors |
| Powers regression | PYTHONPATH=src python -m unittest tests.test_powers | All tests green, including four new cases |
| Progression and quests | PYTHONPATH=src python -m unittest tests.test_progression tests.test_quests | No regressions |
| Content validation/playthrough | PYTHONPATH=src python -m unittest tests.test_vertical_slice tests.test_content | Authored pack loads and branches still work |
| Whole Python suite | PYTHONPATH=src python -m unittest discover -s tests -v | Full exit code 0 |
| Android integration | Project Gradle unit tests and relevant Compose instrumentation | No projection/state regressions |
| GitHub exact-head gates | PR workflow tied to head SHA, no stale green | Required before merge |
| Device | Physical Galaxy A03 test | **UNVERIFIED** without device evidence |
| Canon | Owner explicit story/world and class-ID approvals | **OPEN**; never inferred from passing tests |

**Execution honesty:** test source was authored on the work branch; do not label anything passed until a local exact-source run or CI check reports the result. Similarly do not claim the chapter is approved, D-084 DONE, a real class runtime, or a production release.

## 6. Next bounded work, ordered

1. Execute Python exact-branch CI and fix any failing source/tests in this PR.
2. Verify power catalog cycles never crash on malformed technique metadata; add targeted negative tests if a crash is evidenced.
3. Compare the proposed story chapter with Volume II v0.3.8 for duplication, pacing, and knowledge firewall; retain both separately.
4. For D-084, reconcile WD-001 by owner-reviewed source mapping rather than silently converting the Terra/Tierra historical record into a named game planet.
5. Produce an accepted class-evidence read-only query contract on existing state owners **before** inventing class-save tables.
6. Treat H-05/H-06 single principal ability as a future schema/content validation requirement, with legacy-save migration and grandfathering analysis before enforcement.
7. Create a Smith material-property and bounded output-calibration test design with no fictional formula claim.
8. Choose a final story-to-game bridge only after narrative canon and Gate Twelve relationship are resolved.

**Continuity at handoff:** the code fix and chapter are isolated to a reversible working branch. The owner-controlled narrative docs remain unchanged. Any new ♾️ work should first check latest authority/PR HEAD and run the outstanding test gates rather than inventing extra class or canon state.

---

## 7. Autonomous continuation — 2026-10-29, later session

**Verified prior checkpoint:** GitHub Actions [40903508912](https://github.com/jbob-coder/Text-rpg-game/actions/runs/40903508912) on `70d4933ee85f68ad8071c42ed3efa935070689d6` completed successfully with `python-engine`, `android-unit-and-assemble`, and `android-emulator-smoke`. These results apply to **that commit only**, not automatically to later code.

**Additional code change:** `src/textrpg/powers.py` now checks stage-value type before membership lookup in three validators: technique discovery prerequisites, required stage for technique use, and evolution technique prerequisites. Previously, an unhashable JSON value such as `[]` or `{}` in these positions could cause `TypeError` rather than returning validation errors. A test in `tests/test_powers.py` covers all three validation paths and validates that authored catalogs report malformed stages.

**Narrative work:** new separate [proposed Chapter III, «El peso de una prueba»](../story/PROPOSED_VOLUME_II_CHAPTER_03_2026-10-29.md) expands one **hypothetical investigative** continuation of Chapter II. This is not declared canon, not installed as a quest, and not a determination of the final world/date. Compared against the 2026-10-27 Volume II v0.3.8 candidate, the new chapter does not replace its 25 narrative paragraphs or original two composed scenes; it remains an independent, reversible draft.

**Classes/Smith:** new [read-only readiness integration packet](../systems/CLASS_READINESS_AND_SINGLE_ABILITY_INTEGRATION_PACKET_2026-10-29.md) ties actual v1 state ownership and quest/evidence gaps to seven target class families, Smith professional constraints and H-05/H-06 single-principal-ability rule. It includes proposed query statuses and acceptance tests only; **no class runtime, rank, schema change, Smith formula or ability allocation change** was introduced.

**Test state after continuation:** the 2026-10-29 GitHub workflow for the latest PR HEAD must complete after these commits. Intermediate runs may be cancelled by superseding pushes and are not passing evidence. Check the exact HEAD SHA and all job conclusions before any approval/merge claim. Physical-device testing, canon approval, WD-001, D-084, and class migration gates remain open.
