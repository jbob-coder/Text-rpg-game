# THE GAME — Passive Record Read-Dependency / Overlap Matrix Wave 001 — B

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
| PASSIVE_DEF_0001 | `DEFENSIVE_REACTION_STATE.modifier.flinch_control` | `recognized_threat_state`, `defensive_action_state`, `equipment_state`, `balance_injury_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_DEF_0002 | `DEFENSIVE_REACTION_STATE.modifier.brace_reflex` | `recognized_threat_state`, `defensive_action_state`, `equipment_state`, `balance_injury_state` | PASSIVE_PHY_0009 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_DEF_0003 | `DEFENSIVE_REACTION_STATE.modifier.cover_instinct` | `recognized_threat_state`, `defensive_action_state`, `equipment_state`, `balance_injury_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_DEF_0004 | `DEFENSIVE_REACTION_STATE.modifier.impact_angle` | `recognized_threat_state`, `defensive_action_state`, `equipment_state`, `balance_injury_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_DEF_0005 | `DEFENSIVE_REACTION_STATE.modifier.guard_integrity` | `recognized_threat_state`, `defensive_action_state`, `equipment_state`, `balance_injury_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_DEF_0006 | `DEFENSIVE_REACTION_STATE.modifier.evasion_recovery` | `recognized_threat_state`, `defensive_action_state`, `equipment_state`, `balance_injury_state` | PASSIVE_MOV_0004 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_DEF_0007 | `DEFENSIVE_REACTION_STATE.modifier.stagger_resistance` | `recognized_threat_state`, `defensive_action_state`, `equipment_state`, `balance_injury_state` | PASSIVE_MOV_0004, PASSIVE_PHY_0005, PASSIVE_RES_0010 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_DEF_0008 | `DEFENSIVE_REACTION_STATE.modifier.shield_habit` | `recognized_threat_state`, `defensive_action_state`, `equipment_state`, `balance_injury_state`, `ability_status_state` | PASSIVE_WPN_0008 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_DEF_0009 | `DEFENSIVE_REACTION_STATE.modifier.blast_posture` | `recognized_threat_state`, `defensive_action_state`, `equipment_state`, `balance_injury_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_DEF_0010 | `DEFENSIVE_REACTION_STATE.modifier.protective_positioning` | `recognized_threat_state`, `defensive_action_state`, `equipment_state`, `balance_injury_state`, `team_role_state` | PASSIVE_LDR_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SUR_0001 | `ENVIRONMENT_EXPOSURE_STATE.modifier.heat_tolerance` | `environment_context`, `exposure_history`, `recovery_state`, `travel_resource_state`, `injury_pain_state`, `hazard_environment_state` | PASSIVE_REC_0004, PASSIVE_RES_0001 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SUR_0002 | `ENVIRONMENT_EXPOSURE_STATE.modifier.cold_tolerance` | `environment_context`, `exposure_history`, `recovery_state`, `travel_resource_state`, `hazard_environment_state` | PASSIVE_REC_0005, PASSIVE_RES_0002 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SUR_0003 | `ENVIRONMENT_EXPOSURE_STATE.modifier.altitude_acclimation` | `environment_context`, `exposure_history`, `recovery_state`, `travel_resource_state`, `hazard_environment_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_SUR_0004 | `ENVIRONMENT_EXPOSURE_STATE.modifier.water_discipline` | `environment_context`, `exposure_history`, `recovery_state`, `travel_resource_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_SUR_0005 | `ENVIRONMENT_EXPOSURE_STATE.modifier.hunger_management` | `environment_context`, `exposure_history`, `recovery_state`, `travel_resource_state`, `injury_pain_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_SUR_0006 | `ENVIRONMENT_EXPOSURE_STATE.modifier.sleep_scarcity_tolerance` | `environment_context`, `exposure_history`, `recovery_state`, `travel_resource_state`, `injury_pain_state` | PASSIVE_REC_0006 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SUR_0007 | `ENVIRONMENT_EXPOSURE_STATE.modifier.toxin_familiarity` | `environment_context`, `exposure_history`, `recovery_state`, `travel_resource_state`, `hazard_environment_state` | PASSIVE_RES_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SUR_0008 | `ENVIRONMENT_EXPOSURE_STATE.modifier.storm_sense` | `environment_context`, `exposure_history`, `recovery_state`, `travel_resource_state`, `hazard_environment_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_SUR_0009 | `ENVIRONMENT_EXPOSURE_STATE.modifier.rough_terrain_adaptation` | `environment_context`, `exposure_history`, `recovery_state`, `travel_resource_state`, `hazard_environment_state` | PASSIVE_MOV_0001, PASSIVE_MOV_0007, PASSIVE_MOV_0008 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SUR_0010 | `ENVIRONMENT_EXPOSURE_STATE.modifier.wilderness_routine` | `environment_context`, `exposure_history`, `recovery_state`, `travel_resource_state` | PASSIVE_COG_0006 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SOC_0001 | `SOCIAL_CONTEXT_STATE.modifier.calm_presence` | `social_context`, `observable_reaction_state`, `known_relationship_reputation_state`, `focus_resolve_state`, `hazard_environment_state`, `social_reputation_state` | PASSIVE_MED_0010, PASSIVE_WIL_0001 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SOC_0002 | `SOCIAL_CONTEXT_STATE.modifier.lie_pattern_memory` | `social_context`, `observable_reaction_state`, `known_relationship_reputation_state`, `focus_resolve_state`, `team_role_state` | PASSIVE_COG_0003 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SOC_0003 | `SOCIAL_CONTEXT_STATE.modifier.audience_reading` | `social_context`, `observable_reaction_state`, `known_relationship_reputation_state`, `focus_resolve_state`, `social_reputation_state` | PASSIVE_PRO_0003 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SOC_0004 | `SOCIAL_CONTEXT_STATE.modifier.negotiation_stamina` | `social_context`, `observable_reaction_state`, `known_relationship_reputation_state`, `focus_resolve_state`, `stamina_state`, `focus_state`, `resolve_state`, `social_reputation_state` | PASSIVE_PRO_0007, PASSIVE_WIL_0010 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SOC_0005 | `SOCIAL_CONTEXT_STATE.modifier.social_recovery` | `social_context`, `observable_reaction_state`, `known_relationship_reputation_state`, `focus_resolve_state`, `social_reputation_state` | PASSIVE_WIL_0009 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SOC_0006 | `SOCIAL_CONTEXT_STATE.modifier.controlled_intimidation` | `social_context`, `observable_reaction_state`, `known_relationship_reputation_state`, `focus_resolve_state`, `hazard_environment_state`, `social_reputation_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_SOC_0007 | `SOCIAL_CONTEXT_STATE.modifier.rapport_habit` | `social_context`, `observable_reaction_state`, `known_relationship_reputation_state`, `focus_resolve_state`, `social_reputation_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_SOC_0008 | `SOCIAL_CONTEXT_STATE.modifier.boundary_sense` | `social_context`, `observable_reaction_state`, `known_relationship_reputation_state`, `focus_resolve_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_SOC_0009 | `SOCIAL_CONTEXT_STATE.modifier.conflict_de_escalation` | `social_context`, `observable_reaction_state`, `known_relationship_reputation_state`, `focus_resolve_state`, `ability_status_state` | PASSIVE_LDR_0001 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SOC_0010 | `SOCIAL_CONTEXT_STATE.modifier.reputation_awareness` | `social_context`, `observable_reaction_state`, `known_relationship_reputation_state`, `focus_resolve_state`, `social_reputation_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_LDR_0001 | `TEAM_COORDINATION_STATE.modifier.command_voice` | `team_identity`, `trusted_role_state`, `known_teammate_capabilities`, `operation_context`, `team_role_state` | PASSIVE_SOC_0009 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_LDR_0002 | `TEAM_COORDINATION_STATE.modifier.formation_awareness` | `team_identity`, `trusted_role_state`, `known_teammate_capabilities`, `operation_context`, `team_role_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_LDR_0003 | `TEAM_COORDINATION_STATE.modifier.delegation_habit` | `team_identity`, `trusted_role_state`, `known_teammate_capabilities`, `operation_context`, `team_role_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_LDR_0004 | `TEAM_COORDINATION_STATE.modifier.morale_anchor` | `team_identity`, `trusted_role_state`, `known_teammate_capabilities`, `operation_context`, `resolve_state` | PASSIVE_WIL_0008 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_LDR_0005 | `TEAM_COORDINATION_STATE.modifier.rescue_coordination` | `team_identity`, `trusted_role_state`, `known_teammate_capabilities`, `operation_context` | PASSIVE_DEF_0010, PASSIVE_MED_0001 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_LDR_0006 | `TEAM_COORDINATION_STATE.modifier.shared_timing` | `team_identity`, `trusted_role_state`, `known_teammate_capabilities`, `operation_context`, `team_role_state` | PASSIVE_CBT_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_LDR_0007 | `TEAM_COORDINATION_STATE.modifier.tactical_briefing` | `team_identity`, `trusted_role_state`, `known_teammate_capabilities`, `operation_context`, `team_role_state` | PASSIVE_COG_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_LDR_0008 | `TEAM_COORDINATION_STATE.modifier.crisis_assignment` | `team_identity`, `trusted_role_state`, `known_teammate_capabilities`, `operation_context` | PASSIVE_CBT_0008, PASSIVE_MED_0001, PASSIVE_WIL_0007 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_LDR_0009 | `TEAM_COORDINATION_STATE.modifier.team_memory` | `team_identity`, `trusted_role_state`, `known_teammate_capabilities`, `operation_context`, `team_role_state` | PASSIVE_COG_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_LDR_0010 | `TEAM_COORDINATION_STATE.modifier.chain_of_command_fluency` | `team_identity`, `trusted_role_state`, `known_teammate_capabilities`, `operation_context`, `team_role_state` | PASSIVE_FAC_0006 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_TEC_0001 | `TECHNICAL_TASK_STATE.modifier.tool_memory` | `technical_task_state`, `tool_material_state`, `procedure_state`, `quality_evidence_state`, `tool_material_procedure_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_TEC_0002 | `TECHNICAL_TASK_STATE.modifier.fine_motor_calibration` | `technical_task_state`, `tool_material_state`, `procedure_state`, `quality_evidence_state`, `tool_material_procedure_state` | PASSIVE_MED_0006 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_TEC_0003 | `TECHNICAL_TASK_STATE.modifier.diagnostic_habit` | `technical_task_state`, `tool_material_state`, `procedure_state`, `quality_evidence_state`, `ability_status_state` | PASSIVE_COG_0007 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_TEC_0004 | `TECHNICAL_TASK_STATE.modifier.failure_pattern_library` | `technical_task_state`, `tool_material_state`, `procedure_state`, `quality_evidence_state` | PASSIVE_COG_0003 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_TEC_0005 | `TECHNICAL_TASK_STATE.modifier.material_sense` | `technical_task_state`, `tool_material_state`, `procedure_state`, `quality_evidence_state`, `tool_material_procedure_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_TEC_0006 | `TECHNICAL_TASK_STATE.modifier.repair_economy` | `technical_task_state`, `tool_material_state`, `procedure_state`, `quality_evidence_state`, `tool_material_procedure_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_TEC_0007 | `TECHNICAL_TASK_STATE.modifier.clean_assembly` | `technical_task_state`, `tool_material_state`, `procedure_state`, `quality_evidence_state`, `tool_material_procedure_state` | PASSIVE_MED_0003 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_TEC_0008 | `TECHNICAL_TASK_STATE.modifier.improvised_fix` | `technical_task_state`, `tool_material_state`, `procedure_state`, `quality_evidence_state`, `tool_material_procedure_state`, `ability_status_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_TEC_0009 | `TECHNICAL_TASK_STATE.modifier.calibration_patience` | `technical_task_state`, `tool_material_state`, `procedure_state`, `quality_evidence_state`, `focus_state`, `tool_material_procedure_state` | PASSIVE_WIL_0006 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_TEC_0010 | `TECHNICAL_TASK_STATE.modifier.workshop_discipline` | `technical_task_state`, `tool_material_state`, `procedure_state`, `quality_evidence_state`, `tool_material_procedure_state` | PASSIVE_PRO_0006, PASSIVE_PRO_0008 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_MED_0001 | `MEDICAL_CASE_STATE.modifier.triage_reflex` | `medical_case_state`, `protocol_state`, `patient_observation_state`, `supervision_authorization_state` | PASSIVE_LDR_0005, PASSIVE_LDR_0008, PASSIVE_WIL_0007 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_MED_0002 | `MEDICAL_CASE_STATE.modifier.bleeding_control_habit` | `medical_case_state`, `protocol_state`, `patient_observation_state`, `supervision_authorization_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_MED_0003 | `MEDICAL_CASE_STATE.modifier.sterile_routine` | `medical_case_state`, `protocol_state`, `patient_observation_state`, `supervision_authorization_state` | PASSIVE_TEC_0007 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_MED_0004 | `MEDICAL_CASE_STATE.modifier.recovery_monitoring` | `medical_case_state`, `protocol_state`, `patient_observation_state`, `supervision_authorization_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_MED_0005 | `MEDICAL_CASE_STATE.modifier.pain_assessment` | `medical_case_state`, `protocol_state`, `patient_observation_state`, `supervision_authorization_state`, `injury_pain_state`, `team_role_state` | PASSIVE_INJ_0004 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_MED_0006 | `MEDICAL_CASE_STATE.modifier.stabilization_hands` | `medical_case_state`, `protocol_state`, `patient_observation_state`, `supervision_authorization_state` | PASSIVE_TEC_0002 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_MED_0007 | `MEDICAL_CASE_STATE.modifier.medication_discipline` | `medical_case_state`, `protocol_state`, `patient_observation_state`, `supervision_authorization_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_MED_0008 | `MEDICAL_CASE_STATE.modifier.rehabilitation_insight` | `medical_case_state`, `protocol_state`, `patient_observation_state`, `supervision_authorization_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_MED_0009 | `MEDICAL_CASE_STATE.modifier.injury_pattern_memory` | `medical_case_state`, `protocol_state`, `patient_observation_state`, `supervision_authorization_state`, `injury_pain_state` | PASSIVE_COG_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_MED_0010 | `MEDICAL_CASE_STATE.modifier.patient_calm` | `medical_case_state`, `protocol_state`, `patient_observation_state`, `supervision_authorization_state`, `social_reputation_state`, `ability_status_state` | PASSIVE_SOC_0001 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SYN_0001 | `ABILITY_EXECUTION_STATE.modifier.resource_cycling` | `primary_ability_identity`, `technique_mastery_state`, `ability_resource_strain_state`, `ability_use_history`, `ability_status_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_SYN_0002 | `ABILITY_EXECUTION_STATE.modifier.technique_compression` | `primary_ability_identity`, `technique_mastery_state`, `ability_resource_strain_state`, `ability_use_history`, `ability_status_state` | PASSIVE_COG_0006 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SYN_0003 | `ABILITY_EXECUTION_STATE.modifier.cast_stability` | `primary_ability_identity`, `technique_mastery_state`, `ability_resource_strain_state`, `ability_use_history`, `ability_status_state` | PASSIVE_WIL_0004 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SYN_0004 | `ABILITY_EXECUTION_STATE.modifier.overuse_warning` | `primary_ability_identity`, `technique_mastery_state`, `ability_resource_strain_state`, `ability_use_history`, `ability_status_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_SYN_0005 | `ABILITY_EXECUTION_STATE.modifier.recovery_channel` | `primary_ability_identity`, `technique_mastery_state`, `ability_resource_strain_state`, `ability_use_history`, `team_role_state`, `ability_status_state` | PASSIVE_CBT_0009, PASSIVE_REC_0001 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SYN_0006 | `ABILITY_EXECUTION_STATE.modifier.precision_scaling` | `primary_ability_identity`, `technique_mastery_state`, `ability_resource_strain_state`, `ability_use_history` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_SYN_0007 | `ABILITY_EXECUTION_STATE.modifier.dual_task_control` | `primary_ability_identity`, `technique_mastery_state`, `ability_resource_strain_state`, `ability_use_history`, `ability_status_state` | PASSIVE_WIL_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SYN_0008 | `ABILITY_EXECUTION_STATE.modifier.counter_feedback` | `primary_ability_identity`, `technique_mastery_state`, `ability_resource_strain_state`, `ability_use_history`, `ability_status_state` | PASSIVE_COG_0003 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SYN_0009 | `ABILITY_EXECUTION_STATE.modifier.ability_familiarity` | `primary_ability_identity`, `technique_mastery_state`, `ability_resource_strain_state`, `ability_use_history`, `focus_state`, `ability_status_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_SYN_0010 | `ABILITY_EXECUTION_STATE.modifier.evolution_sensitivity` | `primary_ability_identity`, `technique_mastery_state`, `ability_resource_strain_state`, `ability_use_history`, `ability_status_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_RES_0001 | `HAZARD_RESISTANCE_STATE.modifier.heat_resistance` | `hazard_type_state`, `exposure_state`, `adaptation_state`, `injury_recovery_state`, `hazard_environment_state` | PASSIVE_REC_0004, PASSIVE_SUR_0001 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_RES_0002 | `HAZARD_RESISTANCE_STATE.modifier.cold_resistance` | `hazard_type_state`, `exposure_state`, `adaptation_state`, `injury_recovery_state`, `hazard_environment_state` | PASSIVE_REC_0005, PASSIVE_SUR_0002 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_RES_0003 | `HAZARD_RESISTANCE_STATE.modifier.electric_tolerance` | `hazard_type_state`, `exposure_state`, `adaptation_state`, `injury_recovery_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_RES_0004 | `HAZARD_RESISTANCE_STATE.modifier.pressure_tolerance` | `hazard_type_state`, `exposure_state`, `adaptation_state`, `injury_recovery_state`, `hazard_environment_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_RES_0005 | `HAZARD_RESISTANCE_STATE.modifier.toxin_resistance` | `hazard_type_state`, `exposure_state`, `adaptation_state`, `injury_recovery_state`, `hazard_environment_state` | PASSIVE_SUR_0007 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_RES_0006 | `HAZARD_RESISTANCE_STATE.modifier.sonic_tolerance` | `hazard_type_state`, `exposure_state`, `adaptation_state`, `injury_recovery_state`, `hazard_environment_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_RES_0007 | `HAZARD_RESISTANCE_STATE.modifier.flash_resistance` | `hazard_type_state`, `exposure_state`, `adaptation_state`, `injury_recovery_state`, `injury_pain_state`, `hazard_environment_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_RES_0008 | `HAZARD_RESISTANCE_STATE.modifier.fear_resistance` | `hazard_type_state`, `exposure_state`, `adaptation_state`, `injury_recovery_state` | PASSIVE_COS_0009, PASSIVE_WIL_0002 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_RES_0009 | `HAZARD_RESISTANCE_STATE.modifier.fatigue_resistance` | `hazard_type_state`, `exposure_state`, `adaptation_state`, `injury_recovery_state` | PASSIVE_PHY_0010, PASSIVE_PRO_0001 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_RES_0010 | `HAZARD_RESISTANCE_STATE.modifier.disorientation_resistance` | `hazard_type_state`, `exposure_state`, `adaptation_state`, `injury_recovery_state`, `injury_pain_state` | PASSIVE_DEF_0007, PASSIVE_MOV_0004 | CANDIDATE_OVERLAP_REVIEW |

## Resolution rule

For every candidate overlap:
1. verify whether both records truly modify the same authoritative term;
2. if yes, assign one shared resolver key and cap;
3. if they operate at different stages, document ordered composition instead;
4. if they are merely adjacent concepts, mark the pair `DISTINCT_STAGE_NO_SHARED_TERM`;
5. preserve the decision in later implementation mapping and tests.

No record is canon-promoted by this matrix.
