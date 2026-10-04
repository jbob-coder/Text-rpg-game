# THE GAME — Unknown / Classified Passive State Model 0001–0010

Status: **PHASE-C CALIBRATION / INTENTIONALLY COMPARTMENTED / NOT CANON / NOT IMPLEMENTED**

Shared state:
`qualification_state`, `ownership_state`, `classified_requirement_packet_id`, `authorization_state`, `compartment_id`, `redaction_policy`, `player_safe_projection`, `audit_state`.

Rules:
1. every qualification points to an authored `CLS_XX` requirement packet;
2. authorization/context must be validated authoritatively;
3. ordinary player projection contains no redacted requirement details;
4. developer/debug access stays separate;
5. save/load preserves authorization/ownership without exposing redacted content;
6. classification is not permission to contradict parent system laws;
7. placeholders are not canon programs/institutions.

Required tests:
redacted-field absence, unauthorized access rejection, compartment separation, save/load exactness, stable packet IDs, no client-side reconstruction of hidden requirements, and no governance bypass.
