# THE GAME — Tamsin Phase 1 Social Proof Packet

Status: **CURRENT-FACT AUDIT + PHASE 1 TARGET PACKET / NO RUNTIME CHANGE**
Parent:
- docs/systems/RECURRING_CHARACTER_PACKET_STANDARD.md
Current source:
- content/vertical_slice_01.json
- src/textrpg/social.py

## 1. Purpose

Use NPC_TAMSIN as the first recurring-character proof for Phase 1 requirements:
- #3 meaningful recurring NPC relationship path;
- #4 knowledge-gated gameplay chain;
- optional companion behavior for #9 tactical encounter.

This packet distinguishes what exists now from what still needs implementation.

## 2. Stable identity

Current stable ID:
- NPC_TAMSIN.

Current character record includes:
- average height class;
- slim athletic adult proportions;
- medium warm-brown skin;
- short angular layered near-black hair with heavy left-side fringe;
- dark brown eyes;
- charcoal municipal utility jacket, pale work shirt, dark trousers;
- high utility-jacket collar;
- narrow cross-body tool satchel;
- rolled right sleeve;
- municipal systems badge;
- right-eyebrow notch;
- defined forbidden visual deviations and emotion/pose set.

These are current authored identity facts.

## 3. Starting personality

Current:
- empathy 55;
- aggression 20;
- caution 65;
- ambition 40;
- honesty 70;
- loyalty 60;
- curiosity 75;
- discipline 70.

Do not rebalance these merely for combat convenience.

## 4. Starting relationship with Jack

Current:
- trust 15;
- respect 5;
- affection 0;
- fear 0;
- suspicion 5;
- debt 0;
- loyalty 0.

## 5. Current relationship branch evidence

Current opening content can:
- require trust >= 10 and suspicion <= 40 before asking Tamsin to recover the relay;
- add trust +2 for recovery help;
- add trust +3 when Jack shares Gate Twelve and asks her to join;
- add suspicion +4 when Jack hides Gate Twelve;
- add trust +1 when Jack asks her to join after she already learned the route.

This already proves that relationships are multidimensional and affect choices.

## 6. Current knowledge branch evidence

Key knowledge:
- KNOW_RELAY_DESTINATION_SERVICE_GATE_12.

Current paths:
- Jack may learn it privately from the relay;
- Tamsin may not know it;
- Jack may tell her;
- Tamsin may independently recover the handshake and learn it;
- later OPENING_DECISION choices use npc_knows / npc_not_knows.

This is a real knowledge-gated branch, not a future-only design.

## 7. Current story track

Track:
- TRACK_RELAY_CASE.

Observed current states/transitions include:
- null -> OBSERVING_RELAY after player accepts relay;
- OBSERVING_RELAY -> KNOWS_GATE_TWELVE after Tamsin recovers handshake;
- OBSERVING_RELAY -> JOINS_GATE_TWELVE after direct disclosure/invite;
- OBSERVING_RELAY -> PLAYER_LEFT_WITH_RELAY_SECRET after withholding;
- KNOWS_GATE_TWELVE -> JOINS_GATE_TWELVE after later invitation;
- KNOWS_GATE_TWELVE -> STAYS_AT_DEPOT when Jack asks her to stay;
- JOINS_GATE_TWELVE -> ENTERED_GATE_TWELVE when party enters the tunnel.

These transitions must remain legal regression fixtures.

## 8. Current goal

Current goal:
- GOAL_UNDERSTAND_GATE_TWELVE.

Current authored creation:
- priority 75;
- progress 10 through relay recovery path;
- progress 20 through direct disclosure/join path.

Current progression:
- +15 when joining after known route;
- +30 when entering the service tunnel with Jack.

The goal remains private unless deliberately projected.

## 9. Current party behavior

Current content can add NPC_TAMSIN to state.party.

OPENING_TUNNEL requires party_has NPC_TAMSIN for ENTER_GATE_TWELVE_WITH_TAMSIN.

The solo route remains possible without her.

This is the correct foundation for optional companion participation in the proposed Service Fork encounter.

## 10. Current memory gap

Current opening effects use:
- relationship;
- npc_learn;
- npc_goal_create/progress;
- npc_story_transition;
- party changes.

They do not currently create an explicit Tamsin memory for the key opening trust/secret event.

Phase 1 target:
add at least one durable memory, for example a semantic memory representing either:
- Jack shared Gate Twelve willingly;
- Jack concealed the route and left;
- Tamsin and Jack entered the tunnel together.

Exact memory IDs require implementation/content review.

## 11. Phase 1 requirement #3 acceptance path

A meaningful recurring relationship proof is satisfied when all are verified:
1. Tamsin starts with current seven-axis relationship;
2. at least two axes can produce different later behavior. Trust and suspicion are the minimum;
3. one event writes an explicit memory;
4. later content checks relationship and/or memory;
5. save/load preserves the result;
6. player-safe UI never receives unrelated hidden social state.

Current content already satisfies parts 1, 2, and existing later relationship gates. Explicit memory and later memory reaction still need bounded implementation.

## 12. Phase 1 requirement #4 acceptance path

Knowledge-gated proof:
1. Jack learns Gate Twelve destination;
2. Tamsin's knowledge remains independent;
3. disclosure/recovery changes Tamsin's knowledge;
4. OPENING_DECISION availability differs using npc_knows / npc_not_knows;
5. save/load preserves the branch;
6. UI does not reveal Tamsin's private knowledge map.

Most of this already exists in current content/rules and needs regression verification in the final Phase 1 branch.

## 13. Schedule/presence target

Minimum Phase 1 presence states:
- present at Platform Nine opening;
- present at Relay Workbench when current scene/story path says so;
- PARTY when she joins;
- stays at depot when STAYS_AT_DEPOT;
- absent from Jack's later solo locations when she did not join;
- no duplicate sprite/presence.

A full daily schedule is not required.

## 14. Proposed tactical use

If Tamsin is in party during ENCOUNTER_GT_SERVICE_FORK_CONTACT_01:
- she is optional companion;
- orders: HOLD, ADVANCE, FOCUS_TARGET, ASSIST, WITHDRAW;
- caution 65 and discipline 70 should influence deterministic utility once the companion AI mapping exists;
- she does not gain combat actions merely from her visual role.

An authored Tamsin tactical action/loadout remains a content decision.

## 15. Player-safe panel target

When present, safe panel may show:
- Tamsin known name;
- portrait/sprite;
- visible condition;
- current interactability;
- clearly communicated relationship changes if final UX supports them.

Must not show:
- exact hidden goal priority/progress;
- full knowledge map;
- all memories;
- raw personality numbers;
- AI utility.

## 16. Save/migration

Preserve:
- NPC_TAMSIN ID;
- current relationship axes;
- current knowledge ID;
- TRACK_RELAY_CASE states;
- GOAL_UNDERSTAND_GATE_TWELVE;
- party state.

Adding memory metadata/schedule fields should be backward-compatible or explicitly migrated.

## 17. Test packet

Required Phase 1 tests:
- start relationship exactly matches authored state;
- recovery-help trust/suspicion gate;
- trust +2 recovery path;
- suspicion +4 secret path;
- npc_knows/npc_not_knows decision branching;
- goal creation/progress;
- legal story transitions;
- illegal story transition rejected;
- party join/stay divergence;
- save/load preserves knowledge/relationship/goal/story state;
- player-safe projection redacts private goals/knowledge;
- explicit memory persists once added.

## 18. Status

Current runtime/content already provide a strong partial social proof.

Documentation status:
- identity: READY;
- personality: READY;
- relationship path: CURRENT;
- knowledge path: CURRENT;
- goal/story track: CURRENT;
- party branch: CURRENT;
- explicit memory proof: PENDING IMPLEMENTATION;
- schedule/presence model: CONTRACT READY;
- tactical companion use: PROPOSED.

This packet is sufficient to guide the bounded Phase 1 social migration without inventing a new recurring NPC.
