# THE GAME — Canon Review Dry Run: PASSIVE_FAC_0002 Credential Navigation

Status: **DRY REVIEW ONLY / NO CANON PROMOTION**

Review template:
- `STATUS_RECORD_CANON_PROMOTION_PACKET_TEMPLATE.md`

## 1. Record identity

- record ID: `PASSIVE_FAC_0002`
- display name: Credential Navigation
- type: passive
- family: Faction / Institutional
- current design status: calibration proposal
- implementation: not implemented

## 2. Dry-run decision

**PROPOSED REVIEW OUTCOME: RETURN_FOR_REFINEMENT**

No canon promotion occurs.

Reason:
the passive identity is bounded, but its meaning depends on an institutional credential/access model that is not yet authored at world level.

## 3. Governing effect

Current bounded effect:
improves navigation of known credential and access processes without bypassing authorization.

Hard boundaries:
- does not create credentials;
- does not create clearance;
- does not grant rank;
- does not reveal unknown restricted destinations;
- does not bypass a denied authorization check;
- does not make one institution's procedures universal.

## 4. State ownership

Conceptual owner:
`INSTITUTIONAL_SERVICE_STATE`.

Conceptual write target:
`INSTITUTIONAL_SERVICE_STATE.modifier.credential_navigation`.

Required conceptual reads:
- institution identity;
- authorized-role state;
- credential/clearance state;
- protocol version state.

Current direct-overlap matrix:
`NONE_IDENTIFIED`.

## 5. Qualification

Current compact calibration proposal:
- institutional service events >= 15;
- authorized role = true;
- protocol review = passed.

This is structurally coherent, but cannot be fully validated until the world has actual institution IDs, role/credential states, and protocol records.

Exact counts remain proposals.

## 6. Authorization boundary

Credential Navigation can only reduce avoidable workflow/navigation error inside a process the character is legitimately allowed to engage.

It must not:
- convert familiarity into access authority;
- infer a credential the character does not possess;
- expose a hidden clearance tier;
- bypass a locked gate/system;
- make a stale/revoked credential valid.

Authorization is resolved before the passive contributes.

## 7. Knowledge and visibility

Current compact posture:
- public rumored;
- school known;
- government known;
- faction known;
- public rumor contains an incomplete unlock recipe.

This is not ready for canon.

Reason:
the world has not yet established which institutions teach credential navigation, which credential systems exist, or why the public would know only a rumor while broad institutions know the method.

The row therefore remains a calibration posture.

## 8. Gate Twelve evidence

Confirmed local evidence:
- Service Gate Twelve and Service Tunnel have restricted/controlled-access framing;
- municipal/maintenance infrastructure exists locally.

Safe conclusion:
an access-workflow context is plausible.

Not established:
- credential tiers;
- badges/keys/identity technology;
- local authorization workflow;
- clearance hierarchy;
- named authority issuing credentials.

Therefore Gate Twelve supports the **need for a future access model**, but does not yet support the passive's final world integration.

## 9. World dependencies

Before promotion define:
- institution stable ID;
- role namespace;
- credential/access object or state;
- authorization check;
- protocol/version record;
- revocation/expiry behavior if applicable;
- who teaches/reviews the workflow;
- public versus internal knowledge;
- regional/institution variation.

## 10. Exploit review

Must prevent:
- farming unauthorized access attempts;
- counting invalid service as legitimate qualification;
- using the passive to reveal hidden access state;
- stale credential reuse;
- save/load duplicate qualification;
- cross-institution transfer without an explicit relationship.

## 11. Test obligations

Required future tests:
- no credential -> passive cannot grant access;
- denied authorization remains denied;
- stale/revoked credential remains invalid;
- wrong institution/protocol does not receive full familiarity;
- authorized service event counts once;
- unauthorized event does not count;
- save/load preserves qualification exactly once;
- UI does not reveal hidden clearance data.

## 12. Dry-run conclusion

Credential Navigation has a useful bounded identity, but the parent institutional credential model is too incomplete for canon promotion.

Return for refinement until world/institution authority and access semantics exist.

No canon promotion occurs.
