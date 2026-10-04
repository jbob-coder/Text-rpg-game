# THE GAME — Gate Twelve Phase 1 Tactical Encounter Packet

Status: **PROPOSED PHASE 1 CONTENT PACKET / MECHANICAL CONTRACT READY / NOT CANON OR IMPLEMENTED**
Parents:
- docs/PHASE_1_SOLO_PLAYABLE_PARALLEL_TRACK.md
- docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md
- docs/systems/TACTICAL_COORDINATE_OCCUPANCY_STANDARD.md
- docs/systems/TURN_INITIATIVE_ACTION_BUDGET_STANDARD.md
- docs/systems/MOVEMENT_PATHING_AND_POSITIONING_STANDARD.md
- docs/systems/LOS_DETECTION_AND_COMBAT_KNOWLEDGE_STANDARD.md
- docs/systems/DIRECTIONAL_COVER_TERRAIN_STANDARD.md
- docs/systems/COMBAT_ACTION_TARGETING_RESOLUTION_STANDARD.md
- docs/systems/INJURY_CONDITION_AFTERMATH_STANDARD.md
- docs/systems/COMBAT_AI_OBJECTIVES_RETREAT_STANDARD.md
World/location authority:
- docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md
- content/vertical_slice_01.json

## 1. Purpose

Define one bounded tactical encounter that can prove the Phase 1 combat loop without requiring the full future combat catalog.

This packet deliberately separates:
- **CONFIRMED CURRENT FACTS** from current authored content;
- **PROPOSED PHASE 1 CONTENT** needed to create the encounter;
- **IMPLEMENTATION REQUIREMENTS** that must be satisfied before runtime integration.

Nothing in the proposed section becomes canon merely because it is detailed here.

## 2. Confirmed current facts used

Current content confirms:
- location ID SERVICE_TUNNEL;
- Service Tunnel is restricted infrastructure below the evacuation route;
- opening scene OPENING_TUNNEL states that fresh boot prints cross the dust;
- Gate Twelve connects to Service Tunnel;
- Service Tunnel connects to Trace Chamber;
- Directional Trace first use produces player knowledge KNOW_DIRECTIONAL_TRACE_POINTS_DEEPER;
- vertical_slice_01.directional_trace_first_use_complete is set when that prototype sequence ends;
- world.free_roam_unlocked is then true;
- Tamsin may or may not be in the party depending on the opening route;
- player/NPC knowledge and relationship state are authoritative Python state.

The encounter therefore uses Service Tunnel and the already-established deeper-route mystery without inventing a new parent-world location.

## 3. Proposed encounter identity

Proposed stable ID:
- ENCOUNTER_GT_SERVICE_FORK_CONTACT_01

Proposed tactical map ID:
- TACTICAL_MAP_GT_SERVICE_FORK_01

Working player-facing title:
- Contact at the Service Fork

Canon status:
- PROPOSED;
- requires owner/content review before migration into content JSON.

## 4. Trigger proposal

The encounter becomes eligible only after:
- vertical_slice_01.directional_trace_first_use_complete == true;
- player knows KNOW_DIRECTIONAL_TRACE_POINTS_DEEPER;
- player intentionally returns to SERVICE_TUNNEL and chooses to investigate deeper.

It must not interrupt the existing first Directional Trace scene chain.

This preserves the current prototype story and makes the battle a deliberate follow-up expedition.

## 5. Encounter premise

Jack returns to the Service Tunnel to inspect the deeper direction identified by Directional Trace.

Near the mapped service fork, movement and recent traces confirm that another living party is present.

The first tactical objective is not “kill everything.” It is to get enough information to decide whether to press forward or withdraw safely.

The hostile/contact identity is intentionally unresolved here.

## 6. Proposed participants

### Player side

Required:
- PLAYER_JACK / existing player authority.

Optional:
- NPC_TAMSIN only when current party state contains NPC_TAMSIN.

Tamsin uses companion constrained-autonomy/order rules rather than direct arbitrary control.

### Opposing side

Use two provisional encounter-local actor IDs:
- CONTACT_SERVICE_FORK_A;
- CONTACT_SERVICE_FORK_B.

These are **mechanical placeholders, not canonical named NPCs**.

Before canon promotion, content design must decide whether they become:
- human intruders;
- faction operatives;
- criminals;
- another authored humanoid group;
- or are replaced by a different encounter premise.

Do not create permanent identity art or lore for these placeholders.

## 7. Low-end encounter budget

Phase 1 cap for this packet:
- Jack: 1;
- optional Tamsin: 1;
- opposing contacts: 2;
- maximum simultaneously active actors: 4;
- no reinforcements in the first implementation;
- no destructible terrain;
- no particle-heavy continuous effects.

This is intentionally conservative for Galaxy A02-class targeting.

## 8. Tactical map proposal

Map size:
- 12 columns x 8 rows;
- z = 0 only for the first implementation.

Important anchors:
- PLAYER_ENTRY at (1,6,0);
- OPTIONAL_TAMSIN_ENTRY at (1,7,0);
- GATE_RETREAT_EXIT at (0,6,0);
- TRACE_FORK_OBJECTIVE at (10,2,0);
- CONTACT_A_START at (8,3,0);
- CONTACT_B_START at (10,4,0).

The map represents a bounded subsection of SERVICE_TUNNEL. It is not a new world-map node.

## 9. Terrain plan

Required terrain classes:
- normal service floor;
- difficult rubble;
- solid wall;
- low utility barrier;
- strong machinery housing;
- narrow maintenance conduit edge.

Prototype movement costs:
- normal 1;
- rubble 2;
- severe obstruction 3 only if specifically authored.

No diagonal movement.

## 10. Cover plan

Use edge-based cover.

Minimum authored cover:
- two partial-cover low barriers;
- two strong-cover machinery housings;
- at least one exposed route;
- at least two tactically distinct paths from entry toward objective.

The map should permit Jack to change attack angle rather than forcing a single corridor exchange.

## 11. LOS/detection setup

At encounter start:
- CONTACT_SERVICE_FORK_A is SUSPECTED, not automatically identified;
- CONTACT_SERVICE_FORK_B is UNKNOWN unless Jack/Tamsin detection succeeds;
- the trace fork objective is known because Jack deliberately came to investigate it;
- exact opponent identity remains unknown until legitimate identification.

The player-safe initiative list must not leak CONTACT_SERVICE_FORK_B before detection.

## 12. Primary objective

Primary objective type:
- REACH_CELL + INTERACT_RETRIEVE-style observation.

Success condition:
1. Jack reaches TRACE_FORK_OBJECTIVE or an adjacent legal interaction cell;
2. spends Interact action;
3. encounter records the deeper-route observation;
4. Jack then reaches either the Gate exit or a designated safe resolution position, depending the final authored story beat.

The interaction is an investigation/read, not item fabrication.

## 13. Alternate resolution — retreat

Retreat is always legal once Jack can path to GATE_RETREAT_EXIT.

Retreat result:
- encounter ends without requiring opponent elimination;
- no deeper-route confirmation is granted;
- any incurred injuries/resources remain;
- current contacts may remain unresolved for later state.

This directly proves persistent non-victory aftermath.

## 14. Elimination

Defeating both opposing contacts may make the objective safer but is not the primary success condition.

Do not require lethal outcomes.

Zero health means incapacitated under the combat standard. Canon treatment of incapacitated opposing contacts is decided by aftermath/content review.

## 15. Proposed actions

Jack minimum action set:
- Move;
- Sprint;
- Basic Attack or current legal combat-capable action once weapon/action source is authored;
- Brace;
- Interact;
- Prepare Reaction;
- Retreat through exit;
- applicable ability/technique only if action mapping is explicitly authored.

Tamsin minimum:
- Move;
- Brace;
- Assist;
- one authored basic defensive/technical action if canonically justified;
- Withdraw.

Opposing contacts:
- Move;
- Basic Attack;
- Brace;
- Prepare Reaction;
- Withdraw if retreat condition is reached.

No action should be invented from visual appearance.

## 16. AI profiles

CONTACT_SERVICE_FORK_A:
- cautious blocker;
- prioritizes denying direct access to TRACE_FORK_OBJECTIVE;
- prefers partial/strong cover;
- retreats when severely injured and exit is reachable.

CONTACT_SERVICE_FORK_B:
- mobile pressure;
- repositions toward exposed angles;
- cannot target Jack/Tamsin while unaware;
- retreats if isolated after Contact A leaves/incapacitates.

These are mechanical roles only until content identity is accepted.

## 17. Optional Tamsin order proof

When Tamsin is present, this encounter can prove:
- HOLD;
- ADVANCE;
- FOCUS_TARGET;
- ASSIST;
- WITHDRAW.

Tamsin remains constrained by:
- her current knowledge;
- caution;
- discipline;
- injury;
- legal path/action state.

The encounter must also work when Tamsin is absent.

## 18. Proposed persistent injury for Phase 1

Proposed ID:
- COND_TUNNEL_LEG_INJURY

Status:
- PROPOSED, not current runtime content.

Trigger for the test fixture:
- Jack receives a qualifying severity-1 or severity-2 leg injury under the injury standard.

Initial modifier proposal:
- attributes.agility: -3;
- skills.athletics: -5.

Recovery proposal:
- FIELD_TREATMENT activity or equivalent authored recovery action;
- requires 120 world minutes;
- may require a basic medical resource only if the item/economy domain later approves one;
- for the first implementation, do not invent a consumable solely to satisfy this encounter;
- after treatment, remove the condition atomically.

If no medical item is approved, time + valid recovery location/activity is sufficient for the Phase 1 proof.

## 19. Proposed aftermath results

### Investigate + withdraw/safe exit
May grant proposed knowledge:
- KNOW_SERVICE_FORK_RECENT_CONTACT;
- KNOW_DEEP_TRACE_ROUTE_CONTESTED.

These IDs require content/canon review before implementation.

### Retreat before investigation
- no deeper-route confirmation;
- preserve resources/injuries;
- record encounter retreat history;
- contacts remain unresolved.

### Opposing contact escapes
- preserve escape outcome as encounter history;
- later V09 adversary work may consume it, but Phase 1 must not fabricate a persistent rival automatically.

### Tamsin present
Potential durable effects may include:
- memory of the encounter;
- trust/respect/fear adjustment only if authored by content review;
- goal progress for GOAL_UNDERSTAND_GATE_TWELVE only if the objective genuinely advances that goal.

No automatic relationship reward simply for winning.

## 20. Save/interruption policy

Phase 1:
- save/checkpoint before encounter start;
- no required mid-combat save;
- aftermath commits before post-encounter save;
- app interruption may restart from pre-combat encounter checkpoint.

The pre-combat checkpoint must not be overwritten with partial tactical state.

## 21. Player-safe Android projection requirements

Required combat projection:
- encounter ID/title;
- round;
- active actor;
- visible initiative order;
- action budget;
- visible/known cells;
- legal move cells;
- safe path preview;
- visible actors;
- awareness/identity level;
- cover;
- objective;
- exit;
- legal actions;
- visible conditions;
- combat log entries safe for player knowledge.

Do not expose:
- hidden Contact B location;
- AI utility;
- private retreat thresholds;
- raw NPC goals;
- unknown action definitions.

## 22. Pixel-art requirements

Before production:
- tactical map footprint must be accepted;
- character combat sprite reuse compatibility must be checked;
- opposing contact identity must be canonically resolved;
- cover objects need source-native tactical readability;
- markers/LOS/selection overlays follow pixel composition standards.

No permanent art should be produced for CONTACT_SERVICE_FORK_A/B while they remain mechanical placeholders.

## 23. Required tests

Mechanical:
- map validates;
- entry/exit/objective reachable;
- four-way movement;
- cover angles work;
- hidden Contact B redaction;
- objective interaction;
- retreat without elimination;
- deterministic attack/AI outcome;
- optional Tamsin path;
- no Tamsin dependency when absent;
- injury trigger fixture;
- aftermath atomicity;
- save-before/restart-after interruption;
- save/load after aftermath.

Performance:
- four active actor maximum;
- path/AI queries bounded;
- no continuous real-time simulation;
- instrumentation records response time on representative Android target.

## 24. Canon/content decisions still required

Before integration:
1. approve or replace opponent premise;
2. decide whether the contacts are persistent NPCs, disposable encounter actors, beasts, or faction members;
3. approve knowledge IDs;
4. approve the Gate Twelve leg injury identity/recovery wording;
5. determine Jack's actual first combat action/weapon/ability source;
6. decide Tamsin's combat-capable action, if any;
7. approve narrative consequences.

## 25. Phase 1 impact

This packet moves Phase 1 requirement 9 from “mechanical contract only” to **AUTHORED ENCOUNTER PACKET PROPOSED**.

It moves requirement 10 to **SPECIFIC INJURY/RECOVERY PROPOSAL EXISTS**.

Neither requirement is implemented or verified yet.

Next technical consumer:
- combat schema/API migration packet mapping this encounter to current Python GameState, deterministic rules, player-safe bridge, tests, and Android tactical UI.
