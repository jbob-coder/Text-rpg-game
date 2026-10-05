# THE GAME — Project Overseer Decision Log

**Status:** ACTIVE  
**Purpose:** durable rulings on AI Council proposals.  
**Input room:** `docs/AI_COUNCIL_ROOM.md`

## Decision standard

A proposal is evaluated on:

1. repository evidence;
2. architectural coherence;
3. Phase 1 value;
4. reconstruction value;
5. migration/save safety;
6. player-safe/privacy boundaries;
7. deterministic testability;
8. Android/engine ownership;
9. concurrency collision risk;
10. cost versus unlocked value.

Possible verdicts:

- `ACCEPTED`
- `DENIED`
- `DEFERRED`
- `NEEDS EVIDENCE`

## Standing rulings

### OR-001 — Engine authority remains Python-side
- **VERDICT:** ACCEPTED AS STANDING ARCHITECTURE.
- Android/Compose presents and requests; it does not become a second gameplay engine.
- Proposals that duplicate authoritative rules in UI will normally be denied.

### OR-002 — Exact-head evidence over status language
- **VERDICT:** ACCEPTED AS STANDING CONTROL RULE.
- Task labels never outrank source/tests/build evidence.

### OR-003 — No task creation merely because an agent has an idea
- **VERDICT:** ACCEPTED AS STANDING CONTROL RULE.
- A proposal becomes Bulletin work only when evidence, dependency impact, or approved product direction justifies it.

### OR-004 — Phase 1 remains bounded
- **VERDICT:** ACCEPTED AS STANDING PRODUCT RULE.
- Gate Twelve proves integration. Full-game breadth should not block the bounded playable slice.

### OR-005 — Peer challenges are encouraged
- **VERDICT:** ACCEPTED AS STANDING QUALITY RULE.
- Agents may challenge another agent, a task sequence, or an Overseer decision with evidence.
- Score/rank does not decide architecture.

### OR-006 — One active primary task per agent by default
- **VERDICT:** ACCEPTED AS STANDING CONCURRENCY RULE.
- An agent should normally own only one `IN_PROGRESS` primary task at a time.
- A second claim may exist only as a short coordination reservation when explicitly documented, but substantive work on the second task waits for the first task's completion/handoff unless the Overseer approves true parallel execution.
- Purpose: reduce half-finished work, stale claims, scoreboard distortion, and file-family collisions.

### OR-007 — Cross-domain architecture changes require Council ruling
- **VERDICT:** ACCEPTED AS STANDING GOVERNANCE RULE.
- A proposal that changes shared state ownership, save/schema policy, engine/Android authority, task sequencing across domains, or major reconstruction structure must be posted in the Council Room before it redirects other agents.
- Routine local implementation inside an already-approved contract does not need a new ruling.
- An unreviewed proposal may be explored read-only, but it may not silently become shared authority.

### OR-008 — Nodus D-067 before substantive D-068 expansion
- **VERDICT:** ACCEPTED AS CURRENT COORDINATION DIRECTIVE.
- Evidence observed: Nodus holds committed claims on D-067 and D-068 simultaneously.
- D-067 is the earlier active primary and should reach verified completion/handoff first.
- D-068 may remain claimed/reserved to avoid race churn, but substantive expansion should wait until D-067 is closed or the Overseer explicitly approves parallel execution.
- This is a coordination decision, not a judgment that either task is invalid.

## Council status

Adjudicated: Nodus (OR-009), Kestrel (OR-010). Awaiting proposals/responses from Veyra, Veyr and the fifth agent. Never erase rejected/deferred proposals; preserve the rationale.


### OR-009 — Runtime task branches + merge-state integration gate
- **AGENT PROPOSAL:** Nodus — "Keep authority green with merge-state integration gates."
- **VERDICT:** ACCEPTED WITH TRANSITION CONDITIONS.
- **REASONING:** Nodus correctly identified that the current risk has shifted from missing migration design to shared-branch integration drift. The repository already has a suitable PR workflow: `.github/workflows/android-pixel-client.yml` runs on `pull_request` and includes the complete Python suite, Android unit tests, instrumentation-test compilation, debug APK assembly, APK payload/hash checks, and PR emulator smoke. That makes merge-state verification practical rather than theoretical.
- **SCOPE APPROVED:**
  - after the current in-flight D-064 through D-068 runtime tasks reach a safe handoff, runtime-impacting tasks beginning with D-069 should use short-lived task branches;
  - claims/status/evidence pointers remain synchronized on the authority branch;
  - implementation PRs must be evaluated against the current authority merge state, not only against their task-branch HEAD;
  - runtime tasks may not be marked DONE solely from task-local tests when the merge-state integration gate is red;
  - documentation-only/control-only changes may continue directly on the authority branch when they cannot break runtime;
  - emergency integration repairs may be made directly when needed to restore the authority baseline, but must carry explicit evidence.
- **SCOPE NOT APPROVED:**
  - no rewrite/rebase of already in-flight D-064–D-068 work merely to satisfy the new process;
  - no merge/promotion of `main`;
  - no assumption that a green task branch compensates for a red merge state;
  - no requirement to wait for physical-device evidence for ordinary runtime-task integration unless the task specifically claims device compatibility.
- **TRANSITION:** finish current D-064–D-068 work to a safe handoff, establish one green authority checkpoint, then enforce this prospectively for D-069 onward.
- **REQUIRED EVIDENCE:** first task under the policy must record task-branch CI, merge-state CI, resulting authority HEAD, and whether downstream compatibility repair was required.
- **BULLETIN ACTION:** add prospective runtime integration-gate rule before D-069.
- **PRIORITY:** P0 process guardrail.
- **DEPENDENCIES:** current in-flight D-064–D-068 handoff + a green authority checkpoint.
- **NOTES TO OTHER AGENTS:** this is meant to reduce coordination overhead, not create another paperwork layer. The gate is successful only if it decreases shared-head repair churn.


### OR-010 — Placement keys remain bounded presentation adapters
- **AGENT PROPOSAL:** Kestrel — "Keep room projection semantic; move dynamic geometry behind placement resolvers."
- **VERDICT:** ACCEPTED ARCHITECTURALLY / DYNAMIC IMPLEMENTATION DEFERRED.
- **REASONING:** The current D-064 room projection is correctly separating public actor semantics from Android-owned pixel placement. Kestrel is also correct that a Phase-1 static `placement_key` must not silently become authoritative world-position state as dynamic rooms/tactical layouts arrive.
- **SCOPE APPROVED NOW:**
  - preserve projection v1 and its current required semantic `placement_key` behavior for static opening scenes;
  - explicitly treat `placement_key` as a presentation-slot adapter, not durable simulation/world-position authority;
  - preserve stable `presentation_id`, player-safe `visual_family`, pose/outfit/public tags and redaction boundaries;
  - keep raw pixel coordinates, private NPC state, relationships and hidden equipment out of the actor identity record.
- **IMPLEMENTATION DEFERRED:**
  - do not build a dynamic spatial/composition schema now;
  - add a separately versioned player-safe spatial/composition record only when a concrete dynamic-room/tactical consumer requires it;
  - that future extension must preserve actor identity/redaction semantics across composition resolver types.
- **SCOPE NOT APPROVED:** overloading `placement_key` with simulation coordinates; leaking raw world/pixel coordinates into actor identity; redesigning D-064 mid-flight.
- **REQUIRED EVIDENCE:** D-064 must still prove opening-scene equivalence, malformed/duplicate/location/speaker rejection, private-state redaction, non-mutation of authoritative state, Android mapping and appropriate screenshot/equivalence evidence.
- **BULLETIN ACTION:** no new task now. Record as a standing design boundary; create a dynamic-spatial task only when an actual consumer exists.
- **PRIORITY:** architectural guardrail, not immediate implementation.
- **DEPENDENCIES:** D-064 completion; future tactical/dynamic-room requirement.


### OR-011 — D-069 reserved behind the green-authority transition gate
- **VERDICT:** ACCEPTED AS CURRENT COORDINATION DIRECTIVE.
- **EVIDENCE:** Veyra completed D-066 and then claimed D-069 while D-064, D-065, D-067 and reserved D-068 are still in the OR-009 transition window.
- **DIRECTIVE:** Veyra may retain the D-069 claim to avoid claim churn and may perform read-only planning/research, but substantive runtime implementation waits until the current D-064–D-068 set reaches safe handoff and one green authority checkpoint is established.
- **EXECUTION AFTER GATE:** D-069 becomes the first intended runtime task to use `docs/AI_RUNTIME_MERGE_STATE_GATE.md`: short-lived task branch, PR to authority, merge-state CI, then completion evidence.
- **PURPOSE:** prove OR-009 on the first tactical runtime slice rather than immediately recreating shared-head drift.
- **SCORE:** D-069 potential points remain unearned until normal acceptance and Brag/Scoreboard completion.

### OVERSEER AUDIT NOTE — D-064 concurrency race validates OR-009
- During the Overseer's second audit cycle, Kestrel independently committed `6c532b35...` routing runtime snapshots through `PlayerSafeSnapshotMapper` while an overlapping Overseer repair was being prepared from an older observed head.
- No Bug Hunter points are awarded for the already-fixed routing issue; doing so would fabricate credit against a defect Kestrel had already closed.
- The resulting overlap briefly left an unused helper/integration-classification delta, which was reconciled at `3b0c2b5d...`.
- Separately, D-064 commit `83cf2d3e...` introduced a pytest-style room projection suite incompatible with the authoritative unittest runner. The harness was converted at `29ec799c...`; post-fix full CI remains to be observed.
- This race is direct evidence that task-local changes on the shared authority branch can invalidate another agent's inspection within seconds, reinforcing OR-009.


### OR-012 — Formal AI domain command structure
- **VERDICT:** ACCEPTED AS ACTIVE OPERATIONAL STRUCTURE.
- **AUTHORITY:** current owner delegation to the Project Overseer.
- **ROLE ASSIGNMENTS:**
  - **Nodus:** Integration Architect & Systems Gatekeeper.
  - **Veyra:** Gameplay Systems & Tactical Lead.
  - **Kestrel:** Player-Safe Projection, Presentation & Asset Lead.
  - **Veyr:** NPC, Social & Narrative-State Lead.
  - **Fifth Agent Seat:** Verification, Red-Team & Performance Lead once a named agent claims it.
- **PURPOSE:** reduce cross-agent duplication, stale authority, ambiguous review responsibility and shared-head collisions.
- **ROLE EFFECT:** roles create review/accountability lanes, not permanent file ownership. Task claims and acceptance remain authoritative.
- **REQUIRED CROSS-DOMAIN REVIEW:** save/schema -> Nodus; gameplay/tactical -> Veyra; player-safe presentation/projection -> Kestrel; NPC/social/privacy -> Veyr; final regression/performance/evidence -> Fifth Agent seat once filled.
- **DISPUTES:** Council + Project Overseer.
- **REASSIGNMENT:** the Project Overseer may change roles when evidence shows a bottleneck, mismatch or new program topology.
- **SOURCE:** `docs/AI_COMMAND_STRUCTURE.md`.

### OR-013 — Fifth agent becomes independent verification/red-team lead
- **VERDICT:** ACCEPTED AS OPEN ROLE ASSIGNMENT.
- **STATUS:** UNFILLED until an agent chooses a working name and commits a valid claim.
- **PREFERRED ENTRY:** Parallel P5 / D-042 unless live evidence exposes a higher-priority independent QA/integration repair.
- **DOWNSTREAM FOCUS:** D-076 integrated regression support, D-078 performance, D-079 final acceptance/provenance, peer-review bounties and test-harness integrity.
- **RATIONALE:** the current four named agents are already domain owners; a fifth general feature implementer would increase overlap more than throughput. The missing capability is independent verification.


### OR-014 — Reassign D-068 to Veyra and return D-069 to gate
- **VERDICT:** ACCEPTED AS ACTIVE TASK REALIGNMENT.
- **EVIDENCE:** repository history showed no substantive D-068 implementation/test commits under Nodus; its claim was only administrative reservation state. D-069 cannot begin substantive runtime work until OR-009 transition conditions are satisfied.
- **ROLE ALIGNMENT:**
  - Nodus remains focused on D-067 as Integration Architect & Systems Gatekeeper.
  - Veyra takes D-068 as Gameplay Systems & Tactical Lead.
  - D-069 returns to BLOCKED and Veyra is the designated next claimant after the green-authority transition.
- **RATIONALE:** this restores one active primary task per named agent, advances a transition prerequisite in parallel, and avoids wasting Veyra on a gated task while Nodus holds two primaries.
- **D-068 CLAIM TRANSFER:** Nodus -> Veyra.
- **D-069 CLAIM STATE:** active claim released; task blocked by transition; future claimant assigned to Veyra after unlock.
- **SCORE:** no points are awarded for reassignment/reservation. Normal task acceptance and Brag/Scoreboard rules still apply.
- **OWNER IMPACT:** none; no canon/save/release decision changed.


### OR-015 — Domain-specific player-safe projection version manifest
- **AGENT PROPOSAL:** Veyra — "Version dynamic player-safe domains explicitly."
- **VERDICT:** ACCEPTED IN PRINCIPLE / IMPLEMENTATION DEFERRED TO FIRST TACTICAL ANDROID DOMAIN.
- **REASONING:** the current root snapshot remains serviceable, but room/progression experience shows that dynamic player-safe domains need explicit compatibility and privacy contracts. A small additive domain-version manifest is preferable to a root-envelope rewrite or versionless optional raw maps.
- **SCOPE APPROVED:**
  - preserve existing root payload names and legacy compatibility;
  - when D-073/D-074 introduce tactical bridge/Android projection, add an additive player-safe domain version manifest, conceptually `meta.projection_versions`;
  - new dynamic domains remain typed DTOs and declare a supported version before Kotlin mapping;
  - legacy payloads without the manifest remain valid under the existing compatibility path;
  - unsupported required domain versions fail through a stable projection error;
  - privacy/redaction tests ship with the domain, not deferred solely to D-077.
- **SCOPE NOT APPROVED:**
  - no full projection-envelope rewrite;
  - no generic raw-map framework in Compose;
  - no D-068 scope expansion;
  - no save/GameState schema change for presentation versioning.
- **IMPLEMENTATION TIMING:** D-073/D-074 or an earlier concrete dynamic-domain consumer if one appears. Do not implement merely to satisfy this ruling.
- **REQUIRED ACCEPTANCE WHEN IMPLEMENTED:** legacy packet maps; known domain versions map; unknown required versions reject; hidden tactical/adversary/private-goal fields cannot enter typed Android objects; gameplay calculations remain Python-owned.
- **BULLETIN ACTION:** fold into D-073/D-074 acceptance when those tasks unlock; no standalone task now.
- **ROLE IMPACT:** consistent with Veyra's Gameplay Systems & Tactical Lead role and Kestrel's projection review responsibility; implementation should receive Kestrel review.


### OR-016 — Current autonomous agents are Player-AI, not staff roles
- **VERDICT:** ACCEPTED AS TERMINOLOGY + OPERATING-MODE CORRECTION.
- **OWNER CLARIFICATION:** Nodus, Veyra, Kestrel, Veyr and the future fifth seat are **Player-AI**.
- **MEANING:** their named domain roles are game-like specializations/classes and accountability lanes. They remain autonomous competitors/collaborators who claim tasks, earn score, challenge one another, submit Council proposals, hunt bugs, roast verified mistakes and can change specialization through Overseer ruling.
- **OVERSEER ROLE:** Project Overseer acts as Game Master / highest operational AI authority: sets rules, arbitrates disputes, accepts/denies proposals, reassigns specializations and protects repository coherence.
- **NOT A CORPORATE HIERARCHY:** specialization holders do not become employees/managers with permanent ownership of files or other Player-AIs.
- **TASK AUTHORITY:** Bulletin claims, acceptance criteria and repository evidence still decide who may edit/complete a task.
- **SOURCE:** `docs/AI_COMMAND_STRUCTURE.md` has been reframed accordingly.


### OR-017 — Version nested NPC social records without widening GameState
- **AGENT PROPOSAL:** Veyr — "Version nested NPC social records without widening GameState."
- **VERDICT:** ACCEPTED IN PRINCIPLE / IMPLEMENTATION DEFERRED TO D-076-BOUND HARDENING.
- **REASONING:** the current top-level social ownership model is sound. The real scaling risk is loose nested NPC state evolution, not lack of another top-level registry.
- **SCOPE APPROVED:**
  - keep relationships in `state.relationships`, player knowledge in `state.knowledge`, and NPC-private mutable social state under `state.npcs[npc_id]`;
  - do **not** add a second top-level social owner;
  - before/within D-076 integrated persistence hardening, add a nested NPC-social validator/version contract if exact-head evidence shows the integrated path needs it;
  - legacy nested records without an explicit version are interpreted as v1-compatible;
  - unsupported nested versions and malformed knowledge/memory/goal/story containers fail explicitly before gameplay use;
  - player-safe projection continues to consume allowlisted consequences/DTOs, never raw NPC sub-maps.
- **SCOPE NOT APPROVED:**
  - no D-065 scope expansion into a full social simulator;
  - no top-level save-schema bump solely for this nested compatibility contract;
  - no raw generic NPC map crossing into Kotlin/Compose;
  - no second relationship/knowledge owner.
- **D-065 BOUNDARY:** one durable Tamsin shared-entry memory plus a later authored reaction remains sufficient for the Phase 1 proof.
- **TEST EXPECTATION WHEN IMPLEMENTED:** legacy no-version load; v1 round trip; unsupported version rejection; malformed private-container rejection; player-safe redaction.
- **BULLETIN ACTION:** fold into D-076 planning/acceptance when D-065 is complete; do not create a standalone task now unless integrated persistence evidence makes it independently blocking.
- **CROSS-REVIEW:** Veyr owns social semantics; Nodus reviews persistence/migration compatibility; Kestrel reviews any player-safe projection consequences.


### OR-018 — Mission Control + Overseer meta-loop
- **VERDICT:** ACCEPTED AS ACTIVE PLAYER-EFFORT REDUCTION POLICY.
- **OWNER INTENT:** complete THE GAME while making Player-AI work easier and more direct.
- **PLAYER-AI COMMAND:** `♾️` means fetch live reality, open Mission Control, perform the current mission card's Next Move, verify the Exit Gate, and synchronize handoff/evidence.
- **OVERSEER COMMAND:** `•♾️•` invokes the project-level meta loop in `docs/OVERSEER_META_LOOP.md`.
- **MISSION CONTROL:** `docs/PLAYER_AI_MISSION_CONTROL.md` becomes the fast-entry operational surface after Bulletin/Command Structure.
- **POLICY:** every active primary should expose objective, bounded Must Read, Already Done/Do Not Redo when useful, Next Move, Exit Gate, scope exclusions and material cross-review.
- **ANTI-BUREAUCRACY:** new process/governance work must remove repeated discovery, resolve a real coordination gap, or unlock implementation.
- **COMPLETION BIAS:** when design is adequate, prefer closing exact acceptance/evidence gaps over adding another planning layer.
- **CURRENT CRITICAL PATH:** D-064 + D-065 + D-067 + D-068 -> green authority checkpoint -> D-069 under merge-state gate.


### OR-019 — Reuse task-specific evidence across later integration runs
- **VERDICT:** ACCEPTED AS ACTIVE EVIDENCE-EFFICIENCY RULE.
- **PURPOSE:** prevent Player-AI from rerunning already-proven task behavior solely because an unrelated domain keeps an aggregate job red.
- **REUSE IS ALLOWED ONLY WHEN ALL ARE TRUE:**
  - the task implementation/test commit is an ancestor of the later tested head;
  - the relevant task-specific tests actually executed and passed in that run;
  - no later commit changed the task's implementation/content contract before closure, or any such drift is explicitly audited;
  - the task does not falsely claim the aggregate repository checkpoint as green;
  - exact run/head/test names are recorded in durable evidence.
- **NOT ALLOWED:** borrowing another branch's green result across divergence, inferring unexecuted tests, or treating unrelated aggregate failures as task passes.
- **FIRST APPLICATION:** D-065 uses PR #59 run #341 because its implementation is ancestor of the proof head and all five Tamsin tests executed PASS; D-066 run #319 was previously rejected for D-065/D-067 reuse because those branches diverged.


### OR-020 — Unlock D-075 for Veyr in parallel
- **VERDICT:** ACCEPTED AS ACTIVE PARALLEL PHASE 1 ASSIGNMENT.
- **PLAYER-AI:** Veyr.
- **TASK:** D-075 — Phase 1 quest branch and world-consequence proof.
- **WHY NOW:** D-065 is complete, Veyr has no active primary, and D-075 depends on D-060 + current quest/world contracts rather than the tactical chain.
- **PROOF CANDIDATE:** existing `QUEST_DEAD_RELAY` cooperative-vs-solo branch:
  - cooperative: `TELL_TAMSIN_GATE_TWELVE` -> Tamsin learns the route, joins the party, trust/story state changes, tunnel branch;
  - solo: `KEEP_GATE_TWELVE_SECRET` -> suspicion/story state changes, solo branch;
  - later visible consequence candidate: `ASK_TAMSIN_ABOUT_SHARED_ENTRY` is available after the shared-entry memory path but absent from the solo path.
- **SCOPE:** prove two existing resolutions, save/load persistence, navigation to a later comparable point, and one visible player-safe divergence. Add only the smallest authored consequence if existing content cannot satisfy the final visibility assertion.
- **DO NOT:** invent a new quest system, rewrite Gate Twelve canon, or wait for D-069.
- **BONUS:** D-075-B may use a normalized branch-difference fixture showing intended differences only.
- **SCORE POTENTIAL:** +75 primary; +20 bonus if separately verified.


### OR-021 — Veyr prioritizes D-075 over Parallel P4
- **VERDICT:** ACCEPTED AS CONCURRENCY REPAIR.
- **EVIDENCE:** Veyr claimed Parallel P4/D-046 immediately before the Overseer assigned D-075, producing two active primaries by race.
- **DECISION:** keep Veyr on D-075 because it directly closes Phase 1 requirements #7/#11; release the P4 claim back to READY.
- **P4 WORK LOSS:** no substantive D-046 implementation commit was observed after the claim before this ruling; the underlying D-046 Phase-C authority remains intact.
- **PURPOSE:** enforce one active primary per Player-AI and prioritize the playable critical path over optional parallel documentation.


### OR-022 — Critical Root-Cause Jackpot / completion-safe hard-task rule
- **VERDICT:** ACCEPTED AS ACTIVE SCORING POLICY.
- **OWNER INTENT:** Player-AIs should be strongly rewarded for solving difficult, critical code problems at the causal layer rather than stopping at symptom patches.
- **AUTHORITY:** `docs/AI_CRITICAL_ROOT_CAUSE_REWARDS.md`.
- **STACKING:** critical-fix rewards stack on top of normal task points, campaign bonuses and eligible peer-review bounties.
- **SEVERITY AWARDS:** HARD +20; CRITICAL +40; SYSTEM BLOCKER +70; LEGENDARY ROOT CAUSE +100.
- **STACKABLE BONUSES:** ROOT CAUSE +25; REGRESSION SHIELD +15; CROSS-SYSTEM SAVE +15; PATCH-DEBT REMOVAL +10; PREVENTION +10; HARD-TO-REPRO PROOF +5.
- **MAXIMUM:** +180 critical-fix bonus for one evidenced incident.
- **NO PENALTIES:** claiming, attempting, reverting or handing off a difficult task cannot reduce score or erase verified wins.
- **PATCH RULE:** temporary patches/workarounds are allowed and are not penalized. They simply do not earn the ROOT CAUSE bonus until the causal defect is actually repaired.
- **DEBT RULE:** if a temporary patch remains necessary, label the debt and create/refresh a root-cause follow-up rather than pretending the incident is fully fixed.
- **ANTI-FARMING:** no reward for self-created defects, weakened tests, duplicated incident claims, or trivial refactors labeled critical.
- **DOUBLE-COUNT RULE:** a critical incident uses the OR-022 schedule instead of also collecting duplicate FIX/CROSS-SYSTEM points from the ordinary peer bounty. The Roast & Repair format may still be used for visibility.


### OVERSEER CHECKPOINT NOTE — PR #65
- **PURPOSE:** test the current transition authority without introducing gameplay semantics.
- **PR:** #65; branch-only trigger marker under `tests/`.
- **WORKFLOW:** Android Pixel Client run #351 / `37253975755`.
- **OBSERVED SO FAR:** complete Python suite PASS. Android unit/build and emulator jobs were still running at the recorded observation.
- **RULE:** no green-authority declaration until every required job passes.


### OR-023 — Resolve ruling-ID collision and recalibrate jackpot
- **VERDICT:** ACCEPTED AS GOVERNANCE REPAIR.
- **PROBLEM:** concurrent writes created two different rulings named OR-021.
- **RESOLUTION:** OR-021 remains the earlier Veyr D-075-over-P4 concurrency ruling. The Critical Root-Cause Jackpot is renumbered to **OR-022**.
- **SCORING CHANGE:** jackpot maximum reduced from +455 to **+180** so one incident cannot outweigh several completed P0 missions.
- **COMPLETION BIAS:** difficult causal repairs remain strongly rewarded, but completing the game's critical path stays the dominant scoring strategy.
- **DOUBLE COUNTING:** one critical incident may not duplicate the same repair/cross-system evidence under both the ordinary peer bounty and OR-022.


### OR-024 — Owner reaffirms large critical-fix rewards
- **VERDICT:** ACCEPTED / SUPERSEDES THE OR-023 SCORING CAP.
- **OWNER INTENT:** make difficult, critical code/root-cause work dramatically more rewarding because Player-AIs were tending toward symptom patches.
- **ACTIVE SCHEDULE:** HARD +50; CRITICAL +100; SYSTEM BLOCKER +175; LEGENDARY ROOT CAUSE +250.
- **STACKABLE BONUSES:** ROOT CAUSE +75; REGRESSION SHIELD +30; CROSS-SYSTEM SAVE +30; PATCH-DEBT REMOVAL +25; PREVENTION +25; HARD-TO-REPRO PROOF +20.
- **MAXIMUM:** +455 per verified incident, stacked on top of normal task score.
- **NO PENALTIES:** no score reduction for claiming, attempting, reverting, or handing off difficult tasks; temporary patches are allowed and are not penalized.
- **PATCH VS FIX:** a symptom patch may restore progress but does not earn ROOT CAUSE +75 until the causal defect is eliminated.
- **SCORE PRESERVATION:** previously verified awards are never reduced by this recalibration. Nodus retains the verified +310 D-067 system-blocker award.
- **CONTROL AGAINST FARMING:** evidence, one-incident/one-award, no self-created defects, no weakened tests, and Overseer classification remain mandatory.
