# THE GAME — Passive Record Read-Dependency / Overlap Matrix Wave 001 — C

Status: **PHASE-C RECORD-LEVEL DEPENDENCY / OVERLAP NORMALIZATION / NOT CANON / NOT IMPLEMENTED**

Parents:
- `PASSIVE_RECORD_OWNER_WRITE_TARGET_MATRIX_WAVE_001_INDEX.md`
- `PASSIVE_CROSS_FAMILY_COMPOSITION_STANDARD.md`

Purpose: identify conceptual read dependencies and direct same-term/adjacent-resolver candidates for each passive before implementation mapping.

Important:
- dependencies are conceptual state requirements, not claims about existing runtime fields;
- overlap IDs are **candidate resolver collisions**, not assertions that both effects must use one formula;
- `NONE_IDENTIFIED` means no direct candidate was identified at current design depth, not proof that none can ever exist.

| Passive | Conceptual write target | Required conceptual reads | Direct overlap candidates | Normalization state |
|---|---|---|---|---|
| PASSIVE_BST_0001 | `CREATURE_FIELD_KNOWLEDGE_STATE.modifier.beast_tell_reader` | `species_identity`, `species_familiarity`, `field_observation_evidence`, `environment_context`, `species_ecology_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_BST_0002 | `CREATURE_FIELD_KNOWLEDGE_STATE.modifier.scent_mask_habit` | `species_identity`, `species_familiarity`, `field_observation_evidence`, `environment_context` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_BST_0003 | `CREATURE_FIELD_KNOWLEDGE_STATE.modifier.territory_sense` | `species_identity`, `species_familiarity`, `field_observation_evidence`, `environment_context`, `species_ecology_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_BST_0004 | `CREATURE_FIELD_KNOWLEDGE_STATE.modifier.carcass_handling` | `species_identity`, `species_familiarity`, `field_observation_evidence`, `environment_context`, `species_ecology_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_BST_0005 | `CREATURE_FIELD_KNOWLEDGE_STATE.modifier.crystal_harvest_calm` | `species_identity`, `species_familiarity`, `field_observation_evidence`, `environment_context`, `species_ecology_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_BST_0006 | `CREATURE_FIELD_KNOWLEDGE_STATE.modifier.predation_pattern_memory` | `species_identity`, `species_familiarity`, `field_observation_evidence`, `environment_context`, `species_ecology_state` | PASSIVE_COG_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_BST_0007 | `CREATURE_FIELD_KNOWLEDGE_STATE.modifier.pack_behavior_read` | `species_identity`, `species_familiarity`, `field_observation_evidence`, `environment_context`, `species_ecology_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_BST_0008 | `CREATURE_FIELD_KNOWLEDGE_STATE.modifier.beast_noise_filter` | `species_identity`, `species_familiarity`, `field_observation_evidence`, `environment_context`, `species_ecology_state` | PASSIVE_SEN_0004 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_BST_0009 | `CREATURE_FIELD_KNOWLEDGE_STATE.modifier.track_interpretation` | `species_identity`, `species_familiarity`, `field_observation_evidence`, `environment_context`, `species_ecology_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_BST_0010 | `CREATURE_FIELD_KNOWLEDGE_STATE.modifier.threat_species_recall` | `species_identity`, `species_familiarity`, `field_observation_evidence`, `environment_context`, `species_ecology_state` | PASSIVE_COG_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_INJ_0001 | `INJURY_REHABILITATION_STATE.modifier.scar_flexibility` | `documented_injury_state`, `medical_stability_state`, `rehabilitation_plan_state`, `functional_limit_state`, `injury_pain_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_INJ_0002 | `INJURY_REHABILITATION_STATE.modifier.compensated_gait` | `documented_injury_state`, `medical_stability_state`, `rehabilitation_plan_state`, `functional_limit_state`, `team_role_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_INJ_0003 | `INJURY_REHABILITATION_STATE.modifier.one_hand_adaptation` | `documented_injury_state`, `medical_stability_state`, `rehabilitation_plan_state`, `functional_limit_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_INJ_0004 | `INJURY_REHABILITATION_STATE.modifier.pain_map` | `documented_injury_state`, `medical_stability_state`, `rehabilitation_plan_state`, `functional_limit_state`, `injury_pain_state` | PASSIVE_MED_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_INJ_0005 | `INJURY_REHABILITATION_STATE.modifier.joint_protection` | `documented_injury_state`, `medical_stability_state`, `rehabilitation_plan_state`, `functional_limit_state`, `injury_pain_state` | PASSIVE_PHY_0007 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_INJ_0006 | `INJURY_REHABILITATION_STATE.modifier.vision_compensation` | `documented_injury_state`, `medical_stability_state`, `rehabilitation_plan_state`, `functional_limit_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_INJ_0007 | `INJURY_REHABILITATION_STATE.modifier.hearing_compensation` | `documented_injury_state`, `medical_stability_state`, `rehabilitation_plan_state`, `functional_limit_state` | PASSIVE_SEN_0004 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_INJ_0008 | `INJURY_REHABILITATION_STATE.modifier.breath_compensation` | `documented_injury_state`, `medical_stability_state`, `rehabilitation_plan_state`, `functional_limit_state`, `team_role_state` | PASSIVE_REC_0007 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_INJ_0009 | `INJURY_REHABILITATION_STATE.modifier.old_wound_warning` | `documented_injury_state`, `medical_stability_state`, `rehabilitation_plan_state`, `functional_limit_state`, `injury_pain_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_INJ_0010 | `INJURY_REHABILITATION_STATE.modifier.rehabilitation_strength` | `documented_injury_state`, `medical_stability_state`, `rehabilitation_plan_state`, `functional_limit_state` | PASSIVE_PHY_0003 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_PRO_0001 | `PROFESSION_WORK_STATE.modifier.shift_endurance` | `profession_identity`, `work_task_state`, `competency_review_state`, `workplace_context` | PASSIVE_PHY_0010, PASSIVE_RES_0009 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_PRO_0002 | `PROFESSION_WORK_STATE.modifier.work_pace` | `profession_identity`, `work_task_state`, `competency_review_state`, `workplace_context` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_PRO_0003 | `PROFESSION_WORK_STATE.modifier.customer_read` | `profession_identity`, `work_task_state`, `competency_review_state`, `workplace_context` | PASSIVE_SOC_0003 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_PRO_0004 | `PROFESSION_WORK_STATE.modifier.route_memory` | `profession_identity`, `work_task_state`, `competency_review_state`, `workplace_context` | PASSIVE_COG_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_PRO_0005 | `PROFESSION_WORK_STATE.modifier.inventory_habit` | `profession_identity`, `work_task_state`, `competency_review_state`, `workplace_context`, `tool_material_procedure_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_PRO_0006 | `PROFESSION_WORK_STATE.modifier.safety_routine` | `profession_identity`, `work_task_state`, `competency_review_state`, `workplace_context` | PASSIVE_FAC_0010, PASSIVE_TEC_0010 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_PRO_0007 | `PROFESSION_WORK_STATE.modifier.negotiation_routine` | `profession_identity`, `work_task_state`, `competency_review_state`, `workplace_context`, `social_reputation_state` | PASSIVE_SOC_0004 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_PRO_0008 | `PROFESSION_WORK_STATE.modifier.documentation_discipline` | `profession_identity`, `work_task_state`, `competency_review_state`, `workplace_context`, `tool_material_procedure_state` | PASSIVE_TEC_0010 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_PRO_0009 | `PROFESSION_WORK_STATE.modifier.tool_accountability` | `profession_identity`, `work_task_state`, `competency_review_state`, `workplace_context`, `tool_material_procedure_state`, `ability_status_state`, `species_ecology_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_PRO_0010 | `PROFESSION_WORK_STATE.modifier.professional_focus` | `profession_identity`, `work_task_state`, `competency_review_state`, `workplace_context`, `focus_state` | PASSIVE_WIL_0010 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_FAC_0001 | `INSTITUTIONAL_SERVICE_STATE.modifier.protocol_memory` | `institution_identity`, `authorized_role_state`, `credential_clearance_state`, `protocol_version_state` | PASSIVE_CLS_0001, PASSIVE_COG_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_FAC_0002 | `INSTITUTIONAL_SERVICE_STATE.modifier.credential_navigation` | `institution_identity`, `authorized_role_state`, `credential_clearance_state`, `protocol_version_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_FAC_0003 | `INSTITUTIONAL_SERVICE_STATE.modifier.bureaucratic_timing` | `institution_identity`, `authorized_role_state`, `credential_clearance_state`, `protocol_version_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_FAC_0004 | `INSTITUTIONAL_SERVICE_STATE.modifier.unit_cohesion` | `institution_identity`, `authorized_role_state`, `credential_clearance_state`, `protocol_version_state`, `team_role_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_FAC_0005 | `INSTITUTIONAL_SERVICE_STATE.modifier.clearance_awareness` | `institution_identity`, `authorized_role_state`, `credential_clearance_state`, `protocol_version_state` | PASSIVE_CLS_0003 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_FAC_0006 | `INSTITUTIONAL_SERVICE_STATE.modifier.chain_familiarity` | `institution_identity`, `authorized_role_state`, `credential_clearance_state`, `protocol_version_state`, `team_role_state` | PASSIVE_LDR_0010 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_FAC_0007 | `INSTITUTIONAL_SERVICE_STATE.modifier.institutional_language` | `institution_identity`, `authorized_role_state`, `credential_clearance_state`, `protocol_version_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_FAC_0008 | `INSTITUTIONAL_SERVICE_STATE.modifier.resource_request_skill` | `institution_identity`, `authorized_role_state`, `credential_clearance_state`, `protocol_version_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_FAC_0009 | `INSTITUTIONAL_SERVICE_STATE.modifier.internal_network_memory` | `institution_identity`, `authorized_role_state`, `credential_clearance_state`, `protocol_version_state` | PASSIVE_COG_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_FAC_0010 | `INSTITUTIONAL_SERVICE_STATE.modifier.security_habit` | `institution_identity`, `authorized_role_state`, `credential_clearance_state`, `protocol_version_state`, `team_role_state` | PASSIVE_CLS_0007, PASSIVE_PRO_0006 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_UEV_0001 | `WORLD_EVENT_LEDGER.modifier.survivor_s_echo` | `unique_event_id`, `participation_role`, `event_outcome_state`, `event_signature_state`, `team_role_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_UEV_0002 | `WORLD_EVENT_LEDGER.modifier.first_contact_scar` | `unique_event_id`, `participation_role`, `event_outcome_state`, `event_signature_state`, `injury_pain_state`, `team_role_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_UEV_0003 | `WORLD_EVENT_LEDGER.modifier.warzone_initiate` | `unique_event_id`, `participation_role`, `event_outcome_state`, `event_signature_state`, `team_role_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_UEV_0004 | `WORLD_EVENT_LEDGER.modifier.gateway_exposure` | `unique_event_id`, `participation_role`, `event_outcome_state`, `event_signature_state`, `team_role_state`, `ability_status_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_UEV_0005 | `WORLD_EVENT_LEDGER.modifier.crystal_storm_survivor` | `unique_event_id`, `participation_role`, `event_outcome_state`, `event_signature_state`, `hazard_environment_state`, `species_ecology_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_UEV_0006 | `WORLD_EVENT_LEDGER.modifier.collapse_escapee` | `unique_event_id`, `participation_role`, `event_outcome_state`, `event_signature_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_UEV_0007 | `WORLD_EVENT_LEDGER.modifier.duel_witness` | `unique_event_id`, `participation_role`, `event_outcome_state`, `event_signature_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_UEV_0008 | `WORLD_EVENT_LEDGER.modifier.mass_awakening_witness` | `unique_event_id`, `participation_role`, `event_outcome_state`, `event_signature_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_UEV_0009 | `WORLD_EVENT_LEDGER.modifier.lost_expedition_returnee` | `unique_event_id`, `participation_role`, `event_outcome_state`, `event_signature_state`, `team_role_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_UEV_0010 | `WORLD_EVENT_LEDGER.modifier.cosmic_glimpse` | `unique_event_id`, `participation_role`, `event_outcome_state`, `event_signature_state`, `ability_status_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_COS_0001 | `STATUS_SYSTEM_EVENT_LEDGER.modifier.status_intuition` | `system_event_id`, `status_confirmation_state`, `system_signature_state`, `system_anomaly_state`, `team_role_state`, `ability_status_state` | PASSIVE_CLS_0003 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_COS_0002 | `STATUS_SYSTEM_EVENT_LEDGER.modifier.hidden_prompt_sensitivity` | `system_event_id`, `status_confirmation_state`, `system_signature_state`, `system_anomaly_state`, `ability_status_state` | PASSIVE_COS_0008 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_COS_0003 | `STATUS_SYSTEM_EVENT_LEDGER.modifier.system_shock_tolerance` | `system_event_id`, `status_confirmation_state`, `system_signature_state`, `system_anomaly_state`, `ability_status_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_COS_0004 | `STATUS_SYSTEM_EVENT_LEDGER.modifier.level_surge_stability` | `system_event_id`, `status_confirmation_state`, `system_signature_state`, `system_anomaly_state`, `team_role_state`, `ability_status_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_COS_0005 | `STATUS_SYSTEM_EVENT_LEDGER.modifier.rarity_veil_awareness` | `system_event_id`, `status_confirmation_state`, `system_signature_state`, `system_anomaly_state`, `social_reputation_state`, `ability_status_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_COS_0006 | `STATUS_SYSTEM_EVENT_LEDGER.modifier.passive_revelation_sense` | `system_event_id`, `status_confirmation_state`, `system_signature_state`, `system_anomaly_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_COS_0007 | `STATUS_SYSTEM_EVENT_LEDGER.modifier.threshold_resonance` | `system_event_id`, `status_confirmation_state`, `system_signature_state`, `system_anomaly_state`, `team_role_state`, `ability_status_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_COS_0008 | `STATUS_SYSTEM_EVENT_LEDGER.modifier.system_error_recognition` | `system_event_id`, `status_confirmation_state`, `system_signature_state`, `system_anomaly_state`, `tool_material_procedure_state`, `ability_status_state` | PASSIVE_COS_0002 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_COS_0009 | `STATUS_SYSTEM_EVENT_LEDGER.modifier.cosmic_pressure_resistance` | `system_event_id`, `status_confirmation_state`, `system_signature_state`, `system_anomaly_state`, `resolve_state`, `hazard_environment_state`, `ability_status_state` | PASSIVE_RES_0008 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_COS_0010 | `STATUS_SYSTEM_EVENT_LEDGER.modifier.witness_resonance` | `system_event_id`, `status_confirmation_state`, `system_signature_state`, `system_anomaly_state`, `team_role_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_CLS_0001 | `CLASSIFIED_AUTHORIZATION_STATE.modifier.black_ledger` | `requirement_packet_id`, `authorization_state`, `compartment_state`, `redaction_policy_state`, `team_role_state`, `tool_material_procedure_state` | PASSIVE_FAC_0001 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_CLS_0002 | `CLASSIFIED_AUTHORIZATION_STATE.modifier.silent_threshold` | `requirement_packet_id`, `authorization_state`, `compartment_state`, `redaction_policy_state`, `tool_material_procedure_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_CLS_0003 | `CLASSIFIED_AUTHORIZATION_STATE.modifier.red_index` | `requirement_packet_id`, `authorization_state`, `compartment_state`, `redaction_policy_state`, `team_role_state`, `tool_material_procedure_state`, `ability_status_state` | PASSIVE_COS_0001, PASSIVE_FAC_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_CLS_0004 | `CLASSIFIED_AUTHORIZATION_STATE.modifier.glass_seal` | `requirement_packet_id`, `authorization_state`, `compartment_state`, `redaction_policy_state`, `hazard_environment_state`, `tool_material_procedure_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_CLS_0005 | `CLASSIFIED_AUTHORIZATION_STATE.modifier.null_stamp` | `requirement_packet_id`, `authorization_state`, `compartment_state`, `redaction_policy_state`, `social_reputation_state`, `tool_material_procedure_state`, `ability_status_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_CLS_0006 | `CLASSIFIED_AUTHORIZATION_STATE.modifier.grey_circuit` | `requirement_packet_id`, `authorization_state`, `compartment_state`, `redaction_policy_state`, `tool_material_procedure_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_CLS_0007 | `CLASSIFIED_AUTHORIZATION_STATE.modifier.closed_hand` | `requirement_packet_id`, `authorization_state`, `compartment_state`, `redaction_policy_state`, `tool_material_procedure_state` | PASSIVE_FAC_0010 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_CLS_0008 | `CLASSIFIED_AUTHORIZATION_STATE.modifier.night_archive` | `requirement_packet_id`, `authorization_state`, `compartment_state`, `redaction_policy_state`, `tool_material_procedure_state` | PASSIVE_COG_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_CLS_0009 | `CLASSIFIED_AUTHORIZATION_STATE.modifier.zero_witness` | `requirement_packet_id`, `authorization_state`, `compartment_state`, `redaction_policy_state`, `tool_material_procedure_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_CLS_0010 | `CLASSIFIED_AUTHORIZATION_STATE.modifier.white_room` | `requirement_packet_id`, `authorization_state`, `compartment_state`, `redaction_policy_state`, `focus_state`, `tool_material_procedure_state` | PASSIVE_WIL_0006 | CANDIDATE_OVERLAP_REVIEW |

## Resolution rule

For every candidate overlap:
1. verify whether both records truly modify the same authoritative term;
2. if yes, assign one shared resolver key and cap;
3. if they operate at different stages, document ordered composition instead;
4. if they are merely adjacent concepts, mark the pair `DISTINCT_STAGE_NO_SHARED_TERM`;
5. preserve the decision in later implementation mapping and tests.

No record is canon-promoted by this matrix.
