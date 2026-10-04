# THE GAME — Gate Twelve / Tamsin Phase 1 Social Packet

Status: **CURRENT-STATE GROUNDED + PROPOSED PHASE 1 EXTENSION / V05**
Character:
- NPC_TAMSIN
Sources:
- content/vertical_slice_01.json
- src/textrpg/social.py
Parents:
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
- docs/systems/RECURRING_CHARACTER_PACKET_STANDARD.md
- docs/PHASE_1_SOLO_PLAYABLE_PARALLEL_TRACK.md

## 1. Purpose

Turn the existing Tamsin foundation into the first Phase 1 recurring-NPC proof without rewriting established content.

This packet separates:
- CURRENT: already authored/runtime-supported;
- PROPOSED: additional Phase 1 consequences still needing content migration.

## 2. CURRENT identity

Stable ID:
- NPC_TAMSIN

Current visual profile establishes:
- slim athletic adult;
- medium warm brown skin;
- short angular layered dark hair with left-side fringe;
- dark brown eyes;
- charcoal municipal utility jacket;
- cross-body tool satchel;
- rolled right sleeve;
- municipal systems badge;
- small notch through right eyebrow.

Those details are visual identity evidence, not social-state authority.

## 3. CURRENT starting personality

Current values:
- empathy 55;
- aggression 20;
- caution 65;
- ambition 40;
- honesty 70;
- loyalty 60;
- curiosity 75;
- discipline 70.

Interpretation:
- relatively cautious, curious, disciplined and honest;
- lower aggression;
- moderate-to-positive empathy/loyalty.

These values do not authorize knowledge or story actions by themselves.

## 4. CURRENT starting relationship

At new game:
- trust 15;
- respect 5;
- affection 0;
- fear 0;
- suspicion 5;
- debt 0;
- loyalty 0.

Current content already uses trust and suspicion as explicit gates.

## 5. CURRENT relationship changes

Existing authored consequences include:
- ASK_TAMSIN_FOR_RECOVERY_HELP -> trust +2;
- TELL_TAMSIN_GATE_TWELVE -> trust +3;
- KEEP_GATE_TWELVE_SECRET -> suspicion +4;
- ASK_TAMSIN_TO_JOIN_KNOWN_ROUTE -> trust +1.

These are existing source facts.

## 6. CURRENT knowledge path

Tamsin may learn:
- KNOW_RELAY_DESTINATION_SERVICE_GATE_12

Sources currently include:
- ITEM_DEAD_RELAY during recovery;
- PLAYER when Jack tells her.

Knowledge confidence is explicitly authored.

## 7. CURRENT goal

GOAL_UNDERSTAND_GATE_TWELVE may be created with:
- priority 75;
- progress 10 when she recovers the relay handshake;
- progress 20 when directly invited after being told;
- later +15 for joining after recovery;
- later +30 after entering Service Tunnel.

The exact resulting progress depends on the authored route.

## 8. CURRENT story track

TRACK_RELAY_CASE currently uses states including:
- OBSERVING_RELAY;
- KNOWS_GATE_TWELVE;
- JOINS_GATE_TWELVE;
- PLAYER_LEFT_WITH_RELAY_SECRET;
- STAYS_AT_DEPOT;
- ENTERED_GATE_TWELVE.

Transitions are preflighted in social.py and content uses explicit allowed_from states.

## 9. CURRENT party/presence

Tamsin can be added to party by authored choices.

Current content does not yet provide a general autonomous schedule system.

Phase 1 should preserve event-driven presence until the schedule system is implemented.

## 10. PROPOSED Phase 1 social proof

Phase 1 requirement #3 needs:
- stable NPC identity;
- at least two changing relationship dimensions;
- remembered interaction/durable consequence;
- knowledge/private-state boundary;
- later reaction to prior state.

The existing foundation is close but needs one explicit later social reaction packet.

## 11. PROPOSED memory records

Add only through later content/schema migration:

MEM_TAMSIN_RELAY_DECISION_01
- importance: 3;
- tags: relay, gate_twelve, trust;
- created when Jack either shares or withholds the Gate Twelve information;
- data records route/reason, not hidden player thoughts.

MEM_TAMSIN_TUNNEL_CONTACT_01
- importance: 4;
- tags: gate_twelve, danger, unknown_contacts;
- created only if Tamsin is present for the Phase 1 tactical encounter.

These memories must not be created if she did not witness/learn the event.

## 12. PROPOSED second-axis consequences

To prove multidimensional relationships, the next Phase 1 content should change respect in addition to existing trust/suspicion.

Recommended event-bound changes:

If Tamsin is present in the tactical encounter and Jack secures the terminal while using ASSIST/HOLD/WITHDRAW orders coherently and does not abandon an incapacitated Tamsin:
- respect +2.

If Jack deliberately withdraws while Tamsin remains incapacitated and rescue was legally available:
- trust -3;
- respect -2.

These are proposed event rules, not current content.

No automatic relationship gain for merely winning.

## 13. PROPOSED later reaction

After the encounter or next meaningful Gate Twelve scene, Tamsin's response should depend on durable state.

Cooperative branch candidate:
- trust >= 18;
- respect >= 7;
- suspicion <= 10;
- Tamsin knows Gate Twelve destination/contact context.

Possible consequence:
- she voluntarily shares a diagnostic interpretation or assists a technical check.

Guarded branch candidate:
- suspicion >= 9 OR trust < 15;
- relevant knowledge exists.

Possible consequence:
- she asks for explanation, withholds optional assistance, or requires a social/technical resolution before sharing her interpretation.

Exact dialogue and knowledge reward remain content work; the state gate is the important contract.

## 14. Privacy

Player may observe:
- Tamsin's presence;
- dialogue/reaction;
- known relationship consequences if UX exposes them;
- facts she chooses to share.

Player must not receive:
- raw goal priority;
- private memory list;
- exact hidden suspicion/trust if UI chooses qualitative display;
- knowledge she has not shared;
- future decision utility.

## 15. Tactical integration

If Tamsin is present in ENCOUNTER_GATE12_SERVICE_TUNNEL_CONTACT_01:
- she uses constrained companion AI;
- initial order ASSIST;
- no omniscient enemy knowledge;
- combat memory is created only after authoritative aftermath.

Her personality may later influence order execution, but Phase 1 should keep behavior deterministic and testable.

## 16. Save/load

Required durable state for this proof:
- relationship axes;
- Tamsin knowledge;
- Tamsin memories;
- goal state;
- story track;
- party/presence;
- encounter/social consequence flags.

A save/reload must not reset her to initial values.

## 17. Tests

Required:
- starting state exactness;
- existing trust/suspicion effects remain unchanged;
- story transitions enforce allowed_from;
- goal creation/progression;
- memory only when perceived;
- two-axis proposed consequence;
- cooperative/guarded gate;
- private-state redaction;
- save/load;
- optional absence from tactical encounter.

## 18. Phase 1 status

CURRENT:
- identity, personality, relationship, knowledge, goal, story-track and party foundations exist.

PENDING:
- explicit durable memories for the proof;
- respect-changing event;
- later branch consuming two relationship axes;
- general schedule/presence system;
- player-safe recurring-character projection completion.

This packet is sufficient to guide the next bounded social implementation without inventing a different NPC model.
