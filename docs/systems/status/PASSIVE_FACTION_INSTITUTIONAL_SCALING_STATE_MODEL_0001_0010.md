# THE GAME — Faction / Institutional Passive Scaling & State Model 0001–0010

Status: **PHASE-C CALIBRATION / NOT CANON / NOT IMPLEMENTED**

Purpose: define bounded scaling and authoritative state categories for `PASSIVE_FAC_0001`–`PASSIVE_FAC_0010`.

## Shared state

Future implementation should distinguish:
- `qualification_state`;
- `ownership_state`;
- `institution_id`;
- `authorized_role_state`;
- `credential_state`;
- `clearance_state`;
- `protocol_version_state`;
- `known_contact_state`;
- `service_event_state`;
- `projection_state`.

## Per-record model

| ID | Effect input | Scaling direction | Hard cap |
|---|---|---|---|
| FAC_0001 | procedure-recall burden | repeated legitimate service history | outdated protocols remain possible |
| FAC_0002 | navigation error through known credential workflow | authorized process experience | no authorization bypass |
| FAC_0003 | administrative dependency/timing error | reviewed institutional history | no guaranteed approval speed |
| FAC_0004 | coordination overhead with familiar unit | stable team/service history | no forced cohesion or loyalty |
| FAC_0005 | mistakes about own clearance/handling boundaries | reviewed authorized service | no hidden-clearance revelation |
| FAC_0006 | responsibility-chain execution error | familiar chain history | unfamiliar organizations receive limited/no benefit |
| FAC_0007 | organization-specific terminology/form error | validated institutional use | no universal language mastery |
| FAC_0008 | incomplete legitimate resource request | reviewed request history | no guaranteed resource approval |
| FAC_0009 | recall burden for known internal contacts/roles | legitimate network history | unknown contacts remain unknown |
| FAC_0010 | routine security-procedure omission | reviewed authorized service | no immunity to social/technical compromise |

## Qualification rules

The compact records currently require:
- institutional service events;
- an authorized role;
- protocol review.

Future qualification must:
1. bind evidence to stable institution/service-event IDs;
2. validate role authorization at event time;
3. count each service event once;
4. preserve protocol version used for review;
5. reject access gained through invalid/unauthorized state as qualification evidence;
6. keep exact hidden progress out of ordinary Status projection.

## Cross-family overlap watchlist

- Protocol Memory ↔ Profession / Cognitive Deep Recall;
- Credential Navigation ↔ Social/Technical workflows;
- Unit Cohesion ↔ Leadership/Coordination;
- Clearance Awareness ↔ Unknown/Classified;
- Chain Familiarity ↔ Chain-of-Command Fluency;
- Institutional Language ↔ Profession/Cognitive;
- Security Habit ↔ Classified secrecy routines.

Same-resolver effects use one capped composition path.

## Required tests

- passive never bypasses credentials/clearance;
- outdated protocol versions are not treated as current;
- unknown contacts remain unknown;
- duplicate service-event IDs do not double-count;
- unauthorized service does not satisfy an authorized-role gate;
- save/load preserves qualification exactly once;
- player-safe projection excludes classified details not legitimately known.

No runtime module is claimed here.
