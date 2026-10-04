# THE GAME — Law, Status Architecture & Unique Ontology Standard

Status: **PROVISIONAL / NOT CANON / NOT IMPLEMENTED**

Purpose: separate three concepts required by Law Silence and Origin Key.

## Interaction rules
Law Silence targets only explicitly modeled eligible interaction rules. A future rule record needs a stable rule ID, domain, participants, trigger, result, scope, required knowledge, targetability class, protection class, dependencies, and version.

Provisional targetability classes: `SUPPRESSIBLE`, `CONDITIONALLY_SUPPRESSIBLE`, `PROTECTED`, and `OUTSIDE_DOMAIN`.

Law Silence does not discover hidden rules automatically and does not suppress multiple linked rules merely because one is selected.

## Status endpoints
Origin Key interacts with explicit Status endpoints. A future endpoint needs an ID, layer class, accepted authentication classes, permission set, child prerequisites, safeguards, activation state, and version.

Authentication and permission are separate. Suggested permission vocabulary: `DISCOVER`, `METADATA_READ`, `STATE_READ`, `INVOKE`, `CONFIGURE`, and `ADMIN`.

Origin Key does not receive `CONFIGURE` or `ADMIN` by default. Unmet child prerequisites remain unmet after successful authentication.

## Status layer classes
Provisional classes: `PERSONAL_INTERFACE`, `AUTHORIZED_SERVICE`, `DORMANT_FUNCTION`, `GOVERNANCE_LAYER`, and `ROOT_COSMIC_LAYER`.

Origin Key currently concerns approved dormant functions, not unrestricted governance or root access.

## Protected baseline
Proposed protected concerns include primary identity integrity, one-primary-ability identity, Unique exclusivity, authoritative Status ownership, stable-ID integrity, and Level-100 exception authority. Owner review is required before this becomes canon.

## Unique registry
The Unique rarity rule requires authoritative global exclusivity state. A future registry should store the Unique ability ID, current slot state, holder stable ID when applicable, acquisition event/time, persistence/succession rule, Level-100 interaction state, and version.

No transaction may create two active holders of one Unique ability identity.

The exact post-holder persistence/succession rule remains unresolved and must not be chosen implicitly in runtime code.

## Level-100 boundary
The Level-100 exception must consult Unique registry state. Replacement cannot create a second active holder of Origin Key. Replacement-away and slot-reopening behavior remain explicit design decisions.

## Separation
Law Silence is bounded rule suppression. Origin Key is Status authentication/access. Neither grants the other by default.

## Save/load
Unique registry state, endpoint activation state, one-time function state, access state, and system-strain state must persist deterministically. Save/load cannot duplicate Unique ownership or one-time endpoint use.

## Remaining blockers
- final suppressible-rule catalog;
- final protected-rule policy;
- Law Silence knowledge threshold;
- authored dormant Status endpoints;
- permission/safeguard content;
- Origin Key holder history;
- persistence/succession decision;
- Level-100 replacement decision;
- system-strain calibration;
- institutional/world integration.

No ability is canon-promoted by this standard.