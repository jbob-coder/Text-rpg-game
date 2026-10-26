# D-084 — Historical canon source reconciliation (non-owning)
 
**Recorded:** 2026-10-26 AST (America/Puerto_Rico)  
**Repository:** `jbob-coder/Text-rpg-game`  
**Authority source baseline:** `docs/master-game-development-program@dac5d22cdbe211d0d35d3df98b542be2653f1b85` (observed 2026-10-26)  
**Classification:** SOURCE INVENTORY / EDITORIAL CONTINUITY EVIDENCE — **NOT A D-084 CLAIM, NOT A CANON CHANGE, NOT GAMEPLAY IMPLEMENTATION**.

## Why this exists

The repository's D-084 bulletin and task register remain at an October 8–9 checkpoint. Google Drive's separate THE GAME historical-story workspace contains later original-world decisions (H-01–H-36), a literary manuscript v0.8, a causal/event ledger, and conflict controls last modified by mid-October. Restarting D-084 as though no source material exists would duplicate writing and risk promoting proposals to canon. This one bounded file connects the source authorities for the next valid task claimant without taking their claim or editing existing task statuses.

The canonical Google Drive `ENTITY_REGISTRY.json` was read on 2026-10-26: all seven named Player-AIs (Nodus, Veyra, Kestrel, Veyr, Quorix, Rivet, Strata) have `status=INACTIVE` and `active_session_id=null`. **No agent was activated, no agent identity or claim was inherited, and no Bulletin CLAIM/START/DONE was made by this evidence work.** Silex's D-072 ownership remains outside this file.

## Source authority map

| Source | Observed status / responsibility | URL |
| --- | --- | --- |
| **History and Canon Center** | Read-first editorial policy and provenance index; **not** an alternative source of canon. Viewed 2026-10-26. | [Center](https://docs.google.com/document/d/1q8R9Yli-zexcOx0qzzgTNHkpssL2c8mbdFQmJH5SxIE/edit) |
| **Original Priority History** | Primary explicit narrative decisions H-01–H-36, including corrective H-32–H-36; use it over secondary paraphrases for the historical world. Viewed 2026-10-26. | [Canonical H-register](https://docs.google.com/document/d/1FWyk7YzDmkb2DwOdkRAAHl0gNpVCRVPAiFNfEfSia1Q/edit) |
| **Historical Relational Register** | EVT, ENT, REL and CAP graph / editorial synchronization, not an independent canon. New NOV-X/XI links verified on 2026-10-26. | [Relational register](https://docs.google.com/document/d/1vrkgISD2qwCzFTs9Pe1alut67Rh6UTa628rr560FXBw/edit) |
| **Novelized World History, Volume I, draft v0.8** | Eleven literary sections and XII historical note; includes draft scenes DR-01/DR-05 and NOV-X/XI source appendices. A literary proposal **not approved canon**. | [Manuscript](https://docs.google.com/document/d/1HEhArzECznhRgGGV7yeXTQdJRLHn15I-DsqdT59HQIg/edit) |
| **Knowledge and Disclosure Matrix** | M-01–M-08, P-COM, P-SEQ and proposed GF-01–GF-06 group framing. Interpretations and alternatives, **not** six canon factions. | [Knowledge matrix](https://docs.google.com/document/d/14PA6WqqbPZjLnUH0hACWOCXDABuRZfgZ8zFyEfqJr7E/edit) |
| **First War dossier** | Historical constraints, alternative candidate events and source incompatibilities, including open R-WAR-01 and older atlas dates. Not event approval. | [War dossier](https://docs.google.com/document/d/1WXLD2op8PjH8p-AQcPnL0L_zHlrggFZJW1hFREqenfc/edit) |
| **♾️ Continuity and resumption protocol** | Work continuity with no promise of background execution; Oct 15 Session 022 pending repair identified. | [Continuity handoff](https://docs.google.com/document/d/1qvxeu8LmeJri-rzF1n5HlYwiSP6XDOP1EjGi5Id9v-I/edit) |
| **Repository D-084 task and owner priority** | Operational authority for GitHub task scope/claims. Oct 8 directive: crystal-centered setting and **AC = Antes del Crystal**, not after. | [Bulletin](../AI_TASK_BULLETIN_BOARD.md), [Master Task Register](../THE_GAME_MASTER_TASK_REGISTER.md) |
| **Repository Gate Twelve playable slice** | Real existing code/content, but `provisional_canon`; cannot establish final world chronology, Jack/Steal identity, or entire geopolitical setting. | [Source](../../content/vertical_slice_01.json), [world canon queue](WORLD_CANON_DECISION_QUEUE.md) |

**Precedence by question, not by folder alone:** source files and executed tests own *implemented behavior*; explicit owner decisions and the H-register own *approved narrative history*; later owner-approved corrections supersede older ambiguous paraphrases; the manuscript owns *draft prose*, not world facts; the Bulletin owns *claims/status*, not the text of historical canon. When owner directives from different dates or universes appear inconsistent, preserve both with provenance until lineage or a later exact choice is proved.

## Stable constraint graph: facts vs proposals

Tags: `C` = confirmed in the H-register/owner priority; `P` = literary or worldbuilding proposal only; `U` = unresolved / not established; `X` = provenance or project-lineage conflict requiring adjudication. These tags do **not** change GameState, content metadata or registry IDs.

| ID | Status | Historical boundary and relation | Evidence / safe use |
| --- | --- | --- | --- |
| HST-01 | C | H-36: first portals, spatial ruptures, invading conquerors, first beasts and manifestation of the System are the **same initial historical outbreak**. No exact second/location or universal simultaneity of human observation is established. | H-32–H-36; EVT-003/004/005/006/012, REL-016/017 |
| HST-02 | C | H-01/02/35: invaders are intelligent conquerors with advanced pre-arrival technology; H-09/10/16/17: beasts are **distinct** organisms with crystal cores already present before crossing; some can evolve. Neither class can be silently substituted for the other. | ENT-002 ≠ ENT-004 (REL-018), hybrid beast ENT-005 |
| HST-03 | C | H-03–H-06: celestial help is indirect; the System arrives during the outbreak, and one human main ability is assigned randomly with derivative capabilities. No screen/UI, tablet mechanism or public knowledge schedule follows automatically. | H-32/H-36, M-05 |
| HST-04 | C | H-11: humans eventually discover applications for crystals, including some medieval-form weapons. H-12: the First War follows the System. **Their relative weapon-introduction date is not specified.** | EVT-007/009; REL-012 and R-WAR-01 open |
| HST-05 | C | H-13: the territorial non-conquest truce suspends conquest to allow reorganization. This is neither definitive peace nor proof of a victor. | EVT-010/011, NOV-XI; negotiators and borders U |
| HST-06 | C | Repo owner correction: `AC = Antes del Crystal` (before the event). Treat prior `AC = After Crystal` as superseded; do not call `2010 AC` a post-event society. | Oct 8 owner override in Bulletin/D-084 |
| HST-07 | P | NOV-X / DR-01 supply-store scene and NOV-XI / DR-05 settlement receiving truce news are literary composites, **not approved named sites, NPCs, quests, historical testimonies, institutions or events**. | Manuscript v0.8 appendices X/XI; register NOV-X/XI |
| HST-08 | P | GF-01–GF-06 are possible analytical group classes; P-SEQ/P-HIT and P-EVT are hypothetical causal paths, not official governments, factions, battles or military chronology. | Knowledge matrix; war dossier |
| HST-09 | U | Event date, calendar after Crystal, length and absolute endpoints of war/truce, first crystal arms relative to war, territorial control, political signatories, origin of first human discovery, established game-entry year all still require exact source/owner authority. | QH open; R-WAR-01 and RSK-001 |
| HST-10 | X | Oct 8 repository directive says fictional, crystal-centered **original world**; later H-register/manuscript describes an initial Earth/humanity crisis. Do not silently choose real-world Earth, alternate Earth, a distinct fictional planet or cross-project transplant until source lineage is resolved. | Bulletin D-084 vs original-history H-register / manuscript |
| HST-11 | X | Historic owner character Jack Wilson / `Steal` vs playable Gate Twelve / `Trace Echo` is a **lineage/canon conflict**, not evidence of equivalence, replacement or migration. | D-084 Master Task Register; provisional content file |
| HST-12 | X | An older atlas proposes 2645–2659 conflicts / 2660 agreement; it is **not verified for this same H-36 event chain**. Do not promote its Halcyon name, dates or geography. | First War dossier; RSK-001 |

### Temporal partial order (not a dated calendar)

`OUTBREAK {portals, ruptures, invaders, beasts, System}` (H-36 concurrency)
→ `First War` occurs **after the System** (H-12)
→ `territorial truce` (H-13)
→ `later society / playable context` (desired editorial destination; **date/implementation bridge unverified**).

The human adoption of crystals/arms is a **known eventual result**, not a proven edge from the outbreak to a specific point within, before, or after the First War. Do not turn a descriptive chapter order into a timeline.

## October 26 verified editorial repair

The Session 022 continuity protocol identified that the narrative register lacked **NOV-X** and **NOV-XI**, even though both already existed in manuscript v0.8. On 2026-10-26, the historical relational register was read and the two entries were found missing. A revision-guarded append added only the two index links, each with its H/EVT/CAP references, scenario-proposal classification and outstanding risks. A subsequent Google Docs native paragraph read verified **exactly one NOV-X and exactly one NOV-XI entry**. The primary H-register, chapter manuscript, GameState, quests and playable content were not edited.

No claim is made here that Google Docs supports an executable runtime, that the literary manuscript is accepted, or that a repo test was run.

## D-084 bounded next move for a valid future owner/claimant

1. Validate **live** repository HEAD/Bulletin and the canonical Drive entity activation status before task acquisition. This file is non-owning research, not permission to reuse an inactive Player-AI identity or steal Silex's D-072.
2. Reconcile H-01–H-36 with the Oct 8 `AC` correction and determine whether the Earth-language historical account represents the same original fictional-world setting. Keep classification `X` until an explicit lineage finding exists.
3. Locate the original same-campaign timeline document before setting calendar values. Compare any source for `2010 AC`, `2000 BC`, 2645–2659/2660, pre-/post-crystal labels and the game era. Unsupported periods remain `U`.
4. Build a durable world-bible volume from established history and tagged proposals; do **not** restart an already written 11-section novel, introduce invented canonical cities/factions, or promote literary composites. Preserve H-36's concurrency and H-35's category separation.
5. Advance the draft's next **civilian truce / everyday institutions / reconstruction** section only as literary proposal, with citations to H-13, M-08 and CAP-14/15. New candidate scenes need proposal IDs and knowledge-boundary checks; no retrospective invented treaties or map changes.
6. Connect proposed region/world facts to `WORLD_CANON_DECISION_QUEUE.md` only after their canon status is resolved. Keep existing map coordinates and current save IDs untouched.
7. Require independent verification for eventual Python/Android behavior or content changes. Never label D-084 `DONE` until source, narrative, chronology, cross-reference, claim, and review requirements are satisfied.

## Tests and change boundary

- **Executed:** connected GitHub HEAD and recursive-tree reads; source file reads; connected Drive search/fetch; Google Docs revision-guarded append plus native paragraph readback of the narrative register for NOV-X/XI.
- **Not executed:** Python test suite, Android unit/instrumentation tests, APK build, emulator/device playthrough, canon approval, D-084 ownership claim, or any main/default-branch merge.
- **Files changed in this repo proposal:** this source bridge only. It is not a canonical world-history volume and has no effect on gameplay.
- **Next verification on branch:** fetch this file back from the new branch, verify the authority-branch comparison contains this file only, then request review through a **draft** pull request (not an implementation merge candidate).
