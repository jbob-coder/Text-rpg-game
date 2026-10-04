# THE GAME — Canon Review Dry Run: PASSIVE_FAC_0005 Clearance Awareness

Status: **DRY REVIEW ONLY / NO CANON PROMOTION**

Review template:
- `STATUS_RECORD_CANON_PROMOTION_PACKET_TEMPLATE.md`

## 1. Record identity

- record ID: `PASSIVE_FAC_0005`
- display name: Clearance Awareness
- type: passive
- family: Faction / Institutional
- current design status: calibration proposal
- implementation: not implemented

## 2. Dry-run decision

**PROPOSED REVIEW OUTCOME: RETURN_FOR_REFINEMENT**

No canon promotion occurs.

Reason:
the passive has a defensible bounded identity, but it directly depends on a clearance/authorization model that THE GAME has not yet established at world/entity level.

## 3. Governing effect

Current bounded effect:
improves awareness of the user's own clearance boundaries and handling rules.

Hard boundaries:
- only the user's legitimately known/authorized boundary is eligible;
- no hidden-clearance discovery;
- no access bypass;
- no new credential/rank;
- no revelation of another person's clearance;
- no automatic knowledge of unfamiliar organizations;
- no system-administrator authority.

## 4. State ownership

Conceptual owner:
`INSTITUTIONAL_SERVICE_STATE`.

Conceptual write target:
`INSTITUTIONAL_SERVICE_STATE.modifier.clearance_awareness`.

Required conceptual reads:
- institution identity;
- authorized-role state;
- credential/clearance state;
- protocol version state.

Known adjacency:
`PASSIVE_CLS_0003 Red Index`.

Existing overlap adjudication:
`DISTINCT_STAGE_NO_SHARED_TERM`.

Interpretation:
Clearance Awareness concerns the user's legitimate institutional boundary; Red Index concerns one authorized protected classification signal. Neither should substitute for the other.

## 5. Qualification

Current compact calibration proposal:
- institutional service events >= 24;
- authorized role = true;
- protocol review = passed.

This shape is coherent only after:
- an institution exists;
- an authorized role exists;
- clearance/handling rules exist;
- protocol review is meaningful.

Exact counts remain proposals.

## 6. Knowledge review

Current compact posture:
- public false belief;
- school partial;
- government known;
- faction mixed.

A concrete false-belief candidate already exists in the reconciliation program:
memorizing visible clearance labels/access procedures is wrongly believed to reveal actual authorization boundaries.

That rumor is plausible as a candidate, but final provenance is not established.

The current `GOV_KNOWN` / `FACTION_MIXED` fields are also too generic:
which government or faction is not yet defined.

No compact knowledge row should be promoted unchanged.

## 7. Gate Twelve evidence

Confirmed:
- Service Gate Twelve is a controlled/restricted maintenance threshold;
- Service Tunnel is restricted infrastructure.

Safe inference:
a future access/authorization model is relevant.

Not established:
- clearance tiers;
- credential objects;
- badge/key systems;
- issuing authority;
- revocation policy;
- classified program;
- government/faction ownership.

Therefore Gate Twelve supports the **problem domain**, not the final passive world record.

## 8. Parent-system requirements

Before promotion define:
- institution stable ID;
- role namespace;
- credential/access representation;
- clearance scope;
- authorization decision;
- handling rules;
- protocol versioning;
- revocation/expiry behavior if used;
- knowledge/disclosure policy.

This parent system must resolve access independently from the passive.

## 9. Numeric readiness

Likely parent term:
procedural/interpretation error concerning one's own known clearance boundary.

Unit class:
`ERROR_BURDEN`.

No coefficient is justified until at least one real clearance workflow fixture exists.

## 10. Exploit review

Must prevent:
- unauthorized probing as an unlock farm;
- using denial responses to enumerate hidden clearance levels;
- learning another person's authority through the passive;
- stale/revoked credential reuse;
- cross-institution knowledge transfer without relationship rules;
- save/load duplicate service-event qualification.

## 11. Test obligations

Future minimum tests:
- no institution/role -> no valid effect context;
- denied access remains denied;
- unknown clearance remains hidden;
- revoked credential remains invalid;
- protocol version change can invalidate familiarity;
- Red Index remains a distinct resolver/stage;
- unauthorized events do not count toward qualification;
- duplicate event IDs do not count twice;
- player-safe projection does not reveal hidden access state.

## 12. Dry-run conclusion

Clearance Awareness is conceptually bounded but cannot advance until THE GAME has an actual institutional authorization/clearance model.

Dry outcome remains **RETURN_FOR_REFINEMENT**.

No canon promotion occurs.
