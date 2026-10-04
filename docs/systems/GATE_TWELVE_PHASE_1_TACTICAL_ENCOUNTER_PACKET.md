# THE GAME — Gate Twelve Phase 1 Tactical Encounter Packet

Status: **PROPOSED AUTHORED PHASE 1 ENCOUNTER / IMPLEMENTATION NOT APPLIED / CANON PENDING**
Repository: jbob-coder/Text-rpg-game
Location: SERVICE_TUNNEL
Phase 1 requirement owner:
- docs/PHASE_1_SOLO_PLAYABLE_PARALLEL_TRACK.md
Combat authorities:
- docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md
- docs/systems/TACTICAL_COORDINATE_OCCUPANCY_STANDARD.md
- docs/systems/TURN_INITIATIVE_ACTION_BUDGET_STANDARD.md
- docs/systems/MOVEMENT_PATHING_AND_POSITIONING_STANDARD.md
- docs/systems/LOS_DETECTION_AND_COMBAT_KNOWLEDGE_STANDARD.md
- docs/systems/DIRECTIONAL_COVER_TERRAIN_STANDARD.md
- docs/systems/COMBAT_ACTION_TARGETING_RESOLUTION_STANDARD.md
- docs/systems/INJURY_CONDITION_AFTERMATH_STANDARD.md
- docs/systems/COMBAT_AI_OBJECTIVES_RETREAT_STANDARD.md

## 1. Purpose

Define one bounded Gate Twelve tactical encounter deeply enough that a later implementation task can build it without inventing core combat behavior.

This packet is deliberately small:
- one authored tactical map;
- Jack as direct player character;
- Tamsin supported when she is in party state;
- two unidentified hostile human contacts;
- retreat and objective completion as legitimate outcomes;
- one persistent injury path;
- one knowledge/Trace Echo interaction;
- deterministic combat and aftermath.

It is not a final encounter-generation system and does not establish a named hostile faction.

## 2. Existing source evidence this packet preserves

Current content already establishes:
- Gate Twelve and Service Tunnel as stable locations;
- Service Tunnel as restricted lower infrastructure;
- fresh boot prints crossing the dust when Jack and Tamsin enter the tunnel;
- Trace Echo as a sensory/noncombat signal ability;
- Signal Pulse and later Directional Trace techniques;
- a directional trace pointing deeper below the mapped service level;
- Tamsin as a persistent NPC with relationship, knowledge, memory, goal and story-state support;
- Gate Twelve content as provisional canon.

Therefore this encounter uses the existing unresolved boot-print/trace tension without naming a faction that current canon has not defined.

## 3. Encounter identity

Proposed IDs:
- encounter_id: ENCOUNTER_GATE12_SERVICE_TUNNEL_CONTACT_01
- tactical_map_id: TACTMAP_GATE12_SERVICE_TUNNEL_01
- objective_set_id: OBJSET_GATE12_TUNNEL_CONTACT_01

Player-facing working title:
**Footsteps Below Gate Twelve**

Canon status:
- proposed;
- may be promoted only after owner/canon review and content migration.

## 4. Narrative trigger

Preferred trigger point:
- after Jack has entered Service Tunnel at least once;
- after the fresh boot-print evidence exists in narrative continuity;
- before the game resolves who made those prints;
- optionally after Trace Echo has been discovered, so Signal Pulse can have a tactical information use without becoming mandatory.

The encounter must not overwrite current opening scenes. It is inserted through a later content migration with its own trigger flag.

Proposed trigger prerequisites:
- vertical_slice_01.opening_complete == true;
- current location == SERVICE_TUNNEL;
- encounter flag gate12.tunnel_contact_resolved != true.

Optional Trace Echo branch:
- ABILITY_TRACE_ECHO exists;
- TECHNIQUE_SIGNAL_PULSE is available.

## 5. Narrative premise

Jack detects movement deeper in the restricted tunnel. Two unidentified people are moving through the infrastructure and appear to be avoiding public evacuation routes.

Their faction, employer, wider motive, and relationship to the dead relay remain UNKNOWN in this packet.

They are hostile only after contact escalates.

The first tactical objective is not “kill everyone.” The player can:
- reach the maintenance cutoff terminal and secure the local trace;
- withdraw back toward Gate Twelve;
- incapacitate both contacts;
- force/permit enemy withdrawal.

This preserves uncertainty and leaves later social/adversary content open.

## 6. Tactical map

### 6.1 Dimensions

Phase 1 map:
- width: 12 cells;
- height: 8 cells;
- z layers: 0 only;
- default terrain: service_floor;
- default movement cost: 1.

No diagonal movement.

### 6.2 Coordinate convention

Origin is north-west:
- x increases east;
- y increases south.

### 6.3 Layout sketch

Legend:
- # = LOS + movement blocker
- c = partial cover edge/object
- C = strong cover edge/object
- J = Jack deployment
- T = Tamsin deployment when present
- a/b = unidentified hostile deployments
- M = maintenance cutoff terminal
- R = player retreat exit
- E = hostile/deeper retreat exit
- . = normal floor

```text
y0  ############
y1  #....c...M.#
y2  #..##...a..#
y3  #..#..C....E
y4  #....c..b..#
y5  #..C........#
y6  RJ....##....#
y7  #T..........#
    012345678901
```

The ASCII diagram is semantic documentation, not final art.

### 6.4 Blockers and cover

Required full blockers:
- north boundary y=0;
- south/west/east boundary except explicit exits;
- cells (3,2), (4,2), (3,3), (6,6), (7,6).

Cover anchors:
- partial cover near (5,1);
- strong cover near (6,3);
- partial cover near (5,4);
- strong cover near (3,5).

Exact edge orientation must be authored in the later structured map record and visually matched by the scene art.

### 6.5 Anchors

- Jack spawn: (1,6,0)
- Tamsin spawn if party member: (1,7,0)
- hostile A spawn: (8,2,0)
- hostile B spawn: (9,4,0)
- maintenance terminal: (9,1,0)
- player retreat exit: west boundary at (0,6,0)
- hostile retreat/deeper exit: east boundary at (11,3,0)

No other boundary cell is a legal exit.

## 7. Encounter actors

### 7.1 Jack

actor_id:
- CHAR_JACK_WILSON / current player authority when the player identity migration is complete;
- until that migration, the tactical adapter uses the current authoritative player record rather than duplicating player stats.

Control:
- direct player control.

### 7.2 Tamsin

actor_id:
- NPC_TAMSIN

Deployment:
- only if party contains NPC_TAMSIN.

Control:
- constrained companion AI.

Initial order:
- ASSIST.

Knowledge:
- only current NPC knowledge plus encounter-observed facts.

### 7.3 Hostile contacts

Proposed encounter-local IDs:
- ACTOR_GATE12_UNKNOWN_CONTACT_A
- ACTOR_GATE12_UNKNOWN_CONTACT_B

Player-facing identity before identification:
- Unknown Contact

No permanent named-character identity is created by this packet.

Faction:
- UNKNOWN / deliberately not authored.

Persistence:
- by default these are encounter-local actors;
- if later promoted to recurring adversaries, V09 migration must assign stable world NPC IDs rather than reusing encounter-local IDs as if they had always been persistent.

## 8. Awareness at start

Jack:
- contact A = SUSPECTED;
- contact B = UNKNOWN.

If Tamsin is present:
- Tamsin begins with the same or less awareness than Jack; no omniscient sharing is implied.

Reason:
- current narrative establishes fresh boot prints and tunnel uncertainty, not exact enemy positions.

Contact A/B:
- know the tunnel geometry;
- know the player-side entry area only after movement/noise or direct detection;
- do not begin with automatic exact knowledge of Jack unless the trigger scene explicitly says contact has occurred.

## 9. Trace Echo tactical interaction

Trace Echo remains a sensory ability, not a damage power.

Optional action:
- action_id: ACTION_TRACE_SIGNAL_PULSE_TACTICAL
- derived from TECHNIQUE_SIGNAL_PULSE;
- budget cost: 2;
- uses the existing technique resource costs and drawback;
- target kind: CELL;
- target area: small authored radius centered on selected legal cell;
- effect: upgrades eligible signal/motion-related contact evidence by one awareness step when the target is within the technique's authored sensing conditions;
- cannot identify faction, motives, private goals, exact stats, or hidden inventory;
- cannot deal damage.

The normal technique cooldown/resource/COND_ECHO_STRAIN behavior remains authoritative.

If the player has not discovered Signal Pulse, the encounter remains fully completable.

## 10. Basic tactical actions

The first encounter needs a minimal action set.

### 10.1 Move
Uses the movement standard:
- cost 1 action-budget unit;
- 6 movement points.

### 10.2 Sprint
- cost 2;
- 10 movement points;
- normal Sprint reaction restriction.

### 10.3 Brace
- cost 1;
- grants a temporary authored defensive state until next activation;
- exact numeric bonus should be kept in the structured action record, not Compose.

Prototype default:
- +10 guard-equivalent tactical defense against direct physical attacks until next activation.

### 10.4 Basic close strike

action_id:
- ACTION_BASIC_CLOSE_STRIKE

Purpose:
- provide a minimal attack path without assuming a firearm or new inventory item.

Range:
- adjacent cardinal cell.

Cost:
- 2 action-budget units.

Prototype offense:
- attributes.agility + 0.5 * skills.unarmed.

Defense:
- target derived.evasion;
- cover does not apply to this adjacent strike unless a special terrain rule explicitly blocks contact.

Variance:
- deterministic +/-10.

Base power:
- 10.

Penetration:
- 0.

The action uses the standard margin degrees and damage transaction.

NPC tactical adapters need equivalent resolved attack/evasion/guard values.

## 11. Hostile AI

Working doctrine:
- CONTACT_AVOIDANCE_WITH_DEFENSIVE_FORCE.

Behavior priorities:
1. preserve deeper-route escape if badly injured;
2. prevent the player from freely reaching the terminal while hostile;
3. use cover;
4. attack only detected legal targets;
5. withdraw if the encounter's retreat threshold is met.

Initial personality/doctrine intent:
- cautious rather than suicidal;
- no omniscient knowledge;
- no automatic fight-to-death.

Suggested retreat threshold:
- health <= 35% OR severity >= 2 injury;
- unless the actor is currently blocking immediate objective failure and still has a legal escape plan.

This is a tuning default.

## 12. Companion behavior

If Tamsin is present:
- initial order = ASSIST;
- prioritize Jack's safety and terminal objective;
- do not chase retreating enemies through E unless the player later has a command/rule allowing it;
- WITHDRAW order causes Tamsin to prioritize R.

Relationship/loyalty may later modify order compliance, but Phase 1 should not invent arbitrary disobedience until its exact rule is documented.

## 13. Primary objective

Primary player objective:
**Reach and secure the maintenance cutoff terminal at M.**

Completion condition:
- Jack reaches an adjacent legal interaction cell;
- uses INTERACT on M;
- interaction completes without the encounter already being failed/resolved.

Interact cost:
- 1 action-budget unit.

Result:
- records KNOW_GATE12_TUNNEL_CONTACT_TRACE or another final approved knowledge ID;
- sets an encounter success flag;
- permits immediate tactical withdrawal or continued confrontation depending remaining actors.

The knowledge text/content must be authored later. This packet does not invent what the terminal proves about the contacts.

## 14. Alternate resolutions

Valid resolution classes:

### OBJECTIVE_SECURED
Terminal secured; player may leave or finish the encounter.

### PLAYER_WITHDREW
Jack reaches R and executes Retreat.

### HOSTILES_WITHDREW
Both contacts escape through E or become unable/unwilling to continue.

### HOSTILES_INCAPACITATED
Both contacts are incapacitated.

### PLAYER_INCAPACITATED
Jack reaches zero health and the encounter's authored fail/recovery flow executes.

Tamsin being incapacitated does not automatically end combat unless the encounter author explicitly adds that failure condition.

## 15. Retreat

Player Retreat:
- Jack must occupy (1,6,0) or another explicitly adjacent retreat interaction cell;
- Retreat action cost: 1;
- exit commits PLAYER_WITHDREW;
- no teleport from arbitrary cells.

Hostile withdrawal:
- hostile reaches (10,3,0) and uses Withdraw toward E;
- removed from tactical occupancy;
- aftermath records escaped contact.

## 16. Persistent injury for Phase 1

Proposed condition:
- COND_MINOR_LEG_STRAIN

Trigger:
- authored impact/critical injury result affecting legs;
- or generic injury generation chooses legs at severity 1.

Record:
- severity: 1;
- duration_minutes: 120;
- tags: injury, leg, combat;
- modifiers:
  - attributes.agility: -3
  - skills.athletics: -5

Recovery:
- existing time/condition expiry can remove it after 120 world minutes;
- recovery/rest actions may advance the required time;
- no special medicine item is required for this Phase 1 injury.

This is deliberately mild so the first encounter proves persistence without soft-locking the player.

A final implementation must validate that these modifier paths are accepted by the current modifier contract.

## 17. Aftermath writes

All aftermath writes are atomic.

Always record:
- encounter outcome;
- world time cost;
- relevant injuries/conditions;
- resource changes already committed through combat;
- encounter history event;
- gate12.tunnel_contact_resolved = true after terminal/withdraw/incapacitation resolution as appropriate.

Potential player knowledge:
- terminal/Trace-derived fact only if actually obtained.

Potential Tamsin memory if present:
- MEM_GATE12_TUNNEL_CONTACT_01
- importance based on final social standard;
- tags may include gate_twelve, danger, unknown_contacts.

Potential relationship consequence:
- do not award fixed trust merely for winning;
- relationship changes must be tied to specific authored behavior such as abandoning/helping Tamsin, sharing information, or protecting her.

Potential hostile persistence:
- none by default;
- any recurring-adversary promotion requires a separate V09 record.

## 18. World-time cost

Prototype aftermath time cost:
- 5 minutes base encounter overhead;
- plus later explicit treatment/recovery time outside combat.

Tactical rounds themselves do not map one-to-one to world minutes.

## 19. Save/interruption policy

Phase 1 does not require mid-combat serialization.

Required behavior:
- save allowed before trigger;
- encounter runtime begins from deterministic pre-combat state;
- app interruption may restart encounter from pre-combat checkpoint;
- durable save after atomic aftermath.

Do not partially serialize an unfinished encounter into schema version 1 without migration.

## 20. Android/player-safe tactical projection

Minimum projected data:
- encounter title/objective;
- visible cells;
- Jack;
- Tamsin if present/visible;
- detected/identified contacts only;
- current active actor;
- action budget;
- legal move cells;
- legal actions/targets;
- cover class;
- known hazards;
- known last positions;
- Retreat availability;
- objective state;
- player-visible combat log;
- visible conditions/injuries.

Must not project:
- hidden contact coordinates;
- hostile utility scores;
- future actions;
- hidden faction identity;
- private goals;
- hidden world consequences.

## 21. Performance budget for this encounter

Designed for Galaxy A02-class target:
- maximum simultaneous tactical actors: 4;
- tactical cells: 96;
- z layers: 1;
- no destructible terrain required;
- no continuous physics;
- AI computes only on activation/reaction decisions;
- bounded effects and animation.

This is a design budget, not measured performance evidence.

## 22. Required tests

Engine:
- map validation;
- deterministic pathing;
- spawn legality;
- awareness redaction;
- Signal Pulse does not expose forbidden data;
- initiative/action budget;
- attack determinism;
- retreat legality;
- terminal objective;
- AI no-cheat behavior;
- Tamsin optional deployment;
- injury persistence/expiry;
- atomic aftermath;
- pre-combat restart behavior.

Projection:
- unknown contact absent;
- suspected contact vague;
- detected contact exact;
- no hostile AI internals;
- legal action/move lists match engine.

Android:
- tap select;
- path preview;
- action selection;
- target selection;
- objective/retreat readability;
- phone-width tactical cells;
- reduced motion;
- restart after interruption.

## 23. Content migration required

To implement this packet later, create:
- structured tactical encounter record;
- structured tactical map record;
- tactical actor/archetype records;
- action definitions;
- one injury condition definition;
- trigger/quest/world-state integration;
- player-safe combat projection;
- Android tactical UI;
- tests.

Do not insert these directly into current story JSON until D-032 maps the schema/API boundary.

## 24. Acceptance gate

This encounter is Phase 1-ready only when:
- the packet is promoted/accepted;
- D-032 defines the runtime schema/API migration;
- the condition modifier paths are validated;
- exact structured records exist;
- Python tactical tests pass;
- save/aftermath tests pass;
- Android tactical flow passes;
- low-end profiling is captured.

## 25. Current result

This packet closes the missing **authored Gate Twelve encounter design** at documentation level only.

It does not claim:
- the encounter is in content;
- the combat engine exists;
- the Android tactical UI exists;
- the new hostile contacts are canon;
- the encounter has been tested.

Next combat engineering artifact:
- D-032 combat schema/API migration packet mapping this design into current GameState, RulesEngine, persistence, player-safe bridge, and Android consumer boundaries.
