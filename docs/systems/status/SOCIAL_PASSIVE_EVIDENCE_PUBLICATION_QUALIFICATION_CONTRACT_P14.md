# THE GAME — Social Passive Evidence, Reputation Publication & Qualification Contract (P14 / D-046)

Status: **PHASE-C TARGET-DESIGN CONTRACT / NOT CANON / NOT IMPLEMENTED**
Claim: **Wave 3 P14 / D-046 — PLAYER_VEYR**, source basis `docs/master-game-development-program` @ `787eefe56ad12598b798352686a367bfdca2cc5e`.
In scope: `PASSIVE_SOC_0007` (Rapport Habit) and `PASSIVE_SOC_0010` (Reputation Awareness), **not** new passive records or world events.

## 1. Controlling fact and decision

P9 established that a **Tamsin-specific** cooperative/solo `QUEST_DEAD_RELAY` consequence may be player-known through a later allowed dialogue choice, but does not become a public reputation fact. P14 closes the *design-routing ambiguity*, not the missing gameplay feature: the future pipeline must distinguish (A) authored event occurrence, (B) who observed/learned which fact, (C) separately authorized public publication, (D) per-character passive qualification, and (E) player-safe projection. These are five different decisions. Neither the event itself nor a private NPC memory automatically authorizes the next stage.

Current code remains the authority for **CURRENT** behavior. Proposed field names and records below are *conceptual schema requirements*, not existing `GameState` keys, stable IDs, implemented services, or permission to alter save schema v1.

## 2. CURRENT / TARGET / BLOCKED authority map

| Layer | CURRENT evidenced source | TARGET authority for a later approved implementation | Explicit blocker |
|---|---|---|---|
| Authored occurrence | `RulesEngine.choose` appends `turn/scene/choice/outcome/time` history; `quests.py` records `quest_id/stage/objective` transitions. `GameState.history` is generic persisted evidence. | Quest/world action owner emits a stable, versioned **occurrence reference** after a successful authored transaction; its source owns truth/rollback. | Existing history rows do not themselves prove globally unique event occurrence or social qualification semantics. |
| NPC observation and knowledge | `social.py` owns NPC knowledge, memories, relationship adjustments and explicit knowledge transfer, including `source/confidence/truth/secrecy` on NPC knowledge. | NPC/social knowledge owner records whether a validated durable actor observed a specific occurrence or was later informed; separate origin and recipient provenance. | Private memory, actor relation and transferred belief are not a public broadcast or public truth. `ensure_npc` can create shells for unknown IDs; validate actors first. |
| Public reputation publication | No verified global publisher, audience or reputation-policy owner in current runtime or Gate Twelve evidence. | A separately approved world/social **publication authority** validates the publisher's mandate, published assertion, intended audience, source chain, truth/uncertainty status and publicity time. | WD-004/WD-008 world authority, real dissemination medium, witness/publication rules and named roles remain unauthored. **Do not synthesize public consensus from relationship scores, scene visibility, place labels or history counts.** |
| Social qualification | Target passive family records and conceptual `SOCIAL_CONTEXT_STATE` are documented; `GameState.perks` exists but is not the target Phase-C social owner. | A future Status qualification gate reads a typed, proven social-case event and record-specific authored predicates, applies anti-replay, and separately commits ownership/reveal state. | No approved repeat interval/case identity, qualifications, thresholds, effect coefficients, save migration or runtime resolver. |
| Player-safe disclosure | `RulesEngine.build_scene_view`, `AndroidGameSession._view_for` and Status inspection project authored known information; no explicit passive-list/reputation DTO. | Per-viewer allowlist derives known consequence or authorized published assertion; passive reveal remains separately gated. | No endpoint may expose private `npcs[*].knowledge/memories`, inferred public truth, hidden requirement IDs or qualification counters. |

## 3. Proposed provenance contract — fields as responsibilities, not runtime additions

A future producer must supply **occurrence identity** (stable event reference + authoring version), **source domain** (quest/social/world), **causal actor identity** (validated persistent character/NPC reference), **resolution** (approved branch/outcome), **authoritative moment** (world turn/time), and **rollback/transaction identity**. This provenance must be generated at commit, not reconstructed by counting generic `history` rows or by Android.

An **observer/knowledge record** must additionally distinguish direct witness from learned hearsay, source speaker/channel, holder identity, what exact assertion was learned, confidence/truth posture and secrecy/permission. An NPC learning a rumor does not assert that the rumor is true; a player can know of a false rumor without being granted hidden truth. `share_knowledge` is a targeted transfer, not public publication.

A **publication record** must be separate, and may only exist when an approved world/social institution, authored medium, actor or rule has *specific authority* for that kind of publication. It must identify original occurrence/assertion, publisher, audience, publication channel, dissemination scope, authorization proof, publicity event identity and retraction/correction ancestry. Lack of a publisher means **NO_PUBLICATION**, not an implicit town-wide reputation value. No actual publisher, social network, government or press service is created by this document.

A **qualification record**, if later authorized, must identify stable holder/passive, source occurrence, authored predicate/version, approved qualifying participation, credit outcome, distinct social-case key, ownership/reveal disposition, provenance and audit. These conceptual requirements are informed by `PASSIVE_EVENT_QUALIFICATION_GOVERNANCE_STANDARD.md`, but that standard expressly governs `PASSIVE_UEV_*`, `PASSIVE_COS_*` and eligible `PASSIVE_CLS_*` packet/event cases. It is **not** presently a `PASSIVE_SOC_*` implementation or automatic scope extension.

## 4. Determinism, anti-farm and transaction boundary

1. **Validate before write:** accepted authored occurrence; known durable actor(s); permitted source/observer roles; exact record-specific qualification predicate; legal target owner; required published assertion if an effect specifically uses public reputation. A world fact may exist without being known or published.
2. **Replay identity:** derive eligibility from one canonical authored occurrence/case identity. For a future qualification ledger, deduplicate on the equivalent of *(stable character, passive, qualifying case/occurrence, requirement version)*, not on UI action count, scene visit count or raw timestamp alone. Replaying a view, repeating an Android request, save/load or copying `history` cannot generate new credit.
3. **Repeated social practice:** for `SOC_0007`, a single cooperative Tamsin branch is at most one legitimate context. Future approved criteria must define a meaningful *distinct case*, repetition/cooldown and outcome-validation rule; no numeric repetitions or threshold are invented here. Never reward harassment, pressure spam or repeated conversation options simply because they are repeatable.
4. **Atomic commit:** occurrence evidence, observer knowledge, qualifying-credit state, ownership/reveal effects and any authorized publication must either commit under the governing domain transaction plan or leave no partial new NPC shell, history, achievement, public rumor or Status disclosure. Cross-domain commit coordination and rollback belong to the eventual runtime implementation owner.
5. **Effects are downstream and limited:** qualifying a passive does not itself edit public opinion, overwrite NPC agency, mint rumor sources, create relationships or grant hidden knowledge. Its future social-action effect must use an approved `SOCIAL_CONTEXT_STATE` decision/resolver API; reputation-policy and NPC/private knowledge owners retain their own data.
6. **Version/migration:** any future durable typed ledger and new save field require explicit schema-v1 compatibility and migration approval. Until then the model is a design packet only.

## 5. Two bounded P9 evidence traces

**A. `SOC_0007` / Tamsin cooperative route:** D-075 verifies an authored cooperative branch consequence and an authorized later interaction `ASK_TAMSIN_ABOUT_SHARED_ENTRY`. The engine/quest source may prove this actor-specific outcome. A future social resolver may consume it as *one validated context* if authoring and distinct-case criteria permit. It cannot infer a generic habit counter, public Tamsin endorsement or `PASSIVE_SOC_0007` ownership. Private Tamsin memories remain invisible.

**B. `SOC_0010` / known-versus-public precedent:** The player may know their own authorized Tamsin interaction; another NPC may or may not know it. A solo/secret route does not silently become public. Even a genuine independent NPC hearsay transfer proves only that the recipient learned an assertion; no public standing exists without separately authorized publicity evidence. `SOC_0010` may eventually improve **recall of already-known consequences**, never hidden opinions or future audience reactions. Its compact "false public belief / school rumor / restricted institution" posture remains an unverified calibration proposal pending a real source and world authorization.

## 6. Visibility matrix (future contract)

| Fact category | Player may view when | Never infer from |
|---|---|---|
| Own authored visible choice/outcome | Current scene/quest projection explicitly allows it | NPC memory or undisclosed branch |
| Learned social assertion | Legitimately learned and permitted for the viewer | Global `state.knowledge` key guess, NPC-private confidence |
| Public reputation assertion | An approved publication event is known/observable to the viewer | Relationship score, archive/plaza presence or multiple NPC rumors |
| Unknown/false rumor | Authored rumor itself has been learned; uncertainty/provenance disclosed appropriately | A fabricated consensus or automatic truth verdict |
| Qualified passive | Approved Status acquisition **and** separate reveal authorization | Qualifier progress, one completed quest, source event alone |
| Hidden future method/threshold | Only an expressly authored discovery/reveal rule permits the datum | Client computation, DTO fallback, debugging provenance |

## 7. Future executable acceptance cases (not run in this document)

- **Known branch is not public:** D-075 coop vs solo retains its distinct player-safe choices; neither route auto-creates a public reputation item.
- **Witness is not publisher:** one named NPC learning a social assertion does not produce a public reputation fact or reveal the NPC's secrecy to the player.
- **Unknown/unapproved identity:** a transient `persistent_ref`/recipient never creates `state.npcs`, relationships, qualification or publication through the proposed adapter.
- **Duplicate request:** same authored case replayed via choice presentation, retry, save/load or re-entry yields at most one validated credit; distinct authored cases remain distinguishable.
- **Version change:** legacy/no-event-ID evidence cannot be retroactively counted without an accepted migration; unsupported requirement versions reject safely.
- **Atomic failure:** late failure at observer qualification/publication leaves all durable owners unchanged, including history, rewards and player projection.
- **False assertion/privacy:** known rumor can remain uncertain/false; observer-private truth, relationship axes, hidden Status requirements and undiscovered passive names never leak.
- **After ownership:** qualifying `SOC_0007` does not mint rapport; `SOC_0010` does not supply facts the character never learned.
- **Cross-layer:** future bridge/Android tests reject unknown passive/reputation payload versions and forbid UI-owned acquisition or inferred hidden values.

Existing test leads: `tests/test_social.py`, `tests/test_phase1_quest_branch_world_consequence.py`, `tests/test_android_bridge.py`. **No Python/Android/CI/device tests executed by this documentation pass.**

## 8. P14 closure versus remaining master D-046 work

**Contract resolution:** Five-stage provenance gates, distinct current/target owners, anti-repeat and failed-transaction invariants, actor-versus-public disclosure conditions, and P9-specific decision traces are explicit. This closes the **P9-to-P14 design ambiguity**, not implementation readiness.

**Still requires owner/canon approval:** public reputation publisher and world policy (WD-004/WD-008 where applicable); actor-observation authoring; SOC social-case qualification/credit and effect APIs; source occurrence and migration rules; passive-list DTO, privacy tests, coefficients, thresholds and player discovery. Master D-046 remains IN_PROGRESS. D-072/Silex, P11 Android atomicity and other Wave-3 lanes are untouched.
