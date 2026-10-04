# THE GAME — Passive Record Read-Dependency / Overlap Matrix Wave 001 — A

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
| PASSIVE_PHY_0001 | `BODY_ADAPTATION_STATE.modifier.iron_tendons` | `training_history`, `body_condition_state`, `current_exertion_state`, `injury_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_PHY_0002 | `BODY_ADAPTATION_STATE.modifier.dense_bone` | `training_history`, `body_condition_state`, `current_exertion_state`, `injury_state`, `injury_pain_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_PHY_0003 | `BODY_ADAPTATION_STATE.modifier.efficient_recruitment` | `training_history`, `body_condition_state`, `current_exertion_state`, `injury_state` | PASSIVE_INJ_0010 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_PHY_0004 | `BODY_ADAPTATION_STATE.modifier.load_bearer` | `training_history`, `body_condition_state`, `current_exertion_state`, `injury_state`, `stamina_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_PHY_0005 | `BODY_ADAPTATION_STATE.modifier.shock_acclimation` | `training_history`, `body_condition_state`, `current_exertion_state`, `injury_state`, `injury_pain_state` | PASSIVE_DEF_0007 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_PHY_0006 | `BODY_ADAPTATION_STATE.modifier.grip_endurance` | `training_history`, `body_condition_state`, `current_exertion_state`, `injury_state`, `equipment_state` | PASSIVE_MOV_0006, PASSIVE_WPN_0008 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_PHY_0007 | `BODY_ADAPTATION_STATE.modifier.joint_stability` | `training_history`, `body_condition_state`, `current_exertion_state`, `injury_state`, `injury_pain_state`, `ability_status_state` | PASSIVE_INJ_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_PHY_0008 | `BODY_ADAPTATION_STATE.modifier.sprint_economy` | `training_history`, `body_condition_state`, `current_exertion_state`, `injury_state`, `stamina_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_PHY_0009 | `BODY_ADAPTATION_STATE.modifier.core_bracing` | `training_history`, `body_condition_state`, `current_exertion_state`, `injury_state` | PASSIVE_DEF_0002 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_PHY_0010 | `BODY_ADAPTATION_STATE.modifier.repetition_tolerance` | `training_history`, `body_condition_state`, `current_exertion_state`, `injury_state` | PASSIVE_PRO_0001, PASSIVE_RES_0009 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_REC_0001 | `CORE_RESOURCE_STATE.modifier.second_wind` | `core_resource_state`, `recovery_opportunity_state`, `exertion_history`, `active_condition_state`, `stamina_state` | PASSIVE_CBT_0009, PASSIVE_SYN_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_REC_0002 | `CORE_RESOURCE_STATE.modifier.rapid_lactate_clearance` | `core_resource_state`, `recovery_opportunity_state`, `exertion_history`, `active_condition_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_REC_0003 | `CORE_RESOURCE_STATE.modifier.deep_recovery` | `core_resource_state`, `recovery_opportunity_state`, `exertion_history`, `active_condition_state`, `stamina_state`, `focus_state` | PASSIVE_REC_0006 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_REC_0004 | `CORE_RESOURCE_STATE.modifier.heat_recovery` | `core_resource_state`, `recovery_opportunity_state`, `exertion_history`, `active_condition_state`, `hazard_environment_state` | PASSIVE_RES_0001, PASSIVE_SUR_0001 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_REC_0005 | `CORE_RESOURCE_STATE.modifier.cold_recovery` | `core_resource_state`, `recovery_opportunity_state`, `exertion_history`, `active_condition_state`, `hazard_environment_state` | PASSIVE_RES_0002, PASSIVE_SUR_0002 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_REC_0006 | `CORE_RESOURCE_STATE.modifier.sleep_efficiency` | `core_resource_state`, `recovery_opportunity_state`, `exertion_history`, `active_condition_state` | PASSIVE_REC_0003, PASSIVE_SUR_0006 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_REC_0007 | `CORE_RESOURCE_STATE.modifier.breath_reserve` | `core_resource_state`, `recovery_opportunity_state`, `exertion_history`, `active_condition_state` | PASSIVE_CBT_0003, PASSIVE_INJ_0008 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_REC_0008 | `CORE_RESOURCE_STATE.modifier.pain_recovery` | `core_resource_state`, `recovery_opportunity_state`, `exertion_history`, `active_condition_state`, `injury_pain_state`, `team_role_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_REC_0009 | `CORE_RESOURCE_STATE.modifier.microtear_repair` | `core_resource_state`, `recovery_opportunity_state`, `exertion_history`, `active_condition_state`, `tool_material_procedure_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_REC_0010 | `CORE_RESOURCE_STATE.modifier.recovery_discipline` | `core_resource_state`, `recovery_opportunity_state`, `exertion_history`, `active_condition_state`, `team_role_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_MOV_0001 | `MOVEMENT_ACTION_STATE.modifier.sure_foot` | `movement_action_state`, `terrain_state`, `body_condition_state`, `movement_familiarity_state`, `hazard_environment_state` | PASSIVE_SUR_0009 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_MOV_0002 | `MOVEMENT_ACTION_STATE.modifier.quiet_landing` | `movement_action_state`, `terrain_state`, `body_condition_state`, `movement_familiarity_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_MOV_0003 | `MOVEMENT_ACTION_STATE.modifier.lateral_burst` | `movement_action_state`, `terrain_state`, `body_condition_state`, `movement_familiarity_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_MOV_0004 | `MOVEMENT_ACTION_STATE.modifier.balance_recovery` | `movement_action_state`, `terrain_state`, `body_condition_state`, `movement_familiarity_state`, `injury_pain_state` | PASSIVE_DEF_0006, PASSIVE_DEF_0007, PASSIVE_RES_0010 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_MOV_0005 | `MOVEMENT_ACTION_STATE.modifier.vault_habit` | `movement_action_state`, `terrain_state`, `body_condition_state`, `movement_familiarity_state`, `stamina_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_MOV_0006 | `MOVEMENT_ACTION_STATE.modifier.climb_economy` | `movement_action_state`, `terrain_state`, `body_condition_state`, `movement_familiarity_state`, `stamina_state` | PASSIVE_PHY_0006 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_MOV_0007 | `MOVEMENT_ACTION_STATE.modifier.terrain_reader` | `movement_action_state`, `terrain_state`, `body_condition_state`, `movement_familiarity_state`, `hazard_environment_state` | PASSIVE_SUR_0009 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_MOV_0008 | `MOVEMENT_ACTION_STATE.modifier.long_stride` | `movement_action_state`, `terrain_state`, `body_condition_state`, `movement_familiarity_state` | PASSIVE_SUR_0009 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_MOV_0009 | `MOVEMENT_ACTION_STATE.modifier.fall_roll` | `movement_action_state`, `terrain_state`, `body_condition_state`, `movement_familiarity_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_MOV_0010 | `MOVEMENT_ACTION_STATE.modifier.direction_change` | `movement_action_state`, `terrain_state`, `body_condition_state`, `movement_familiarity_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_SEN_0001 | `PERCEPTION_EVIDENCE_STATE.modifier.low_light_acuity` | `sensory_input_state`, `observation_context`, `signal_quality_state`, `known_reference_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_SEN_0002 | `PERCEPTION_EVIDENCE_STATE.modifier.motion_focus` | `sensory_input_state`, `observation_context`, `signal_quality_state`, `known_reference_state`, `focus_state`, `species_ecology_state` | PASSIVE_CBT_0002 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SEN_0003 | `PERCEPTION_EVIDENCE_STATE.modifier.peripheral_discipline` | `sensory_input_state`, `observation_context`, `signal_quality_state`, `known_reference_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_SEN_0004 | `PERCEPTION_EVIDENCE_STATE.modifier.sound_separation` | `sensory_input_state`, `observation_context`, `signal_quality_state`, `known_reference_state` | PASSIVE_BST_0008, PASSIVE_INJ_0007 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SEN_0005 | `PERCEPTION_EVIDENCE_STATE.modifier.scent_memory` | `sensory_input_state`, `observation_context`, `signal_quality_state`, `known_reference_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_SEN_0006 | `PERCEPTION_EVIDENCE_STATE.modifier.thermal_discrimination` | `sensory_input_state`, `observation_context`, `signal_quality_state`, `known_reference_state`, `ability_status_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_SEN_0007 | `PERCEPTION_EVIDENCE_STATE.modifier.vibration_sense` | `sensory_input_state`, `observation_context`, `signal_quality_state`, `known_reference_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_SEN_0008 | `PERCEPTION_EVIDENCE_STATE.modifier.range_estimation` | `sensory_input_state`, `observation_context`, `signal_quality_state`, `known_reference_state` | PASSIVE_CBT_0007, PASSIVE_WPN_0003 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SEN_0009 | `PERCEPTION_EVIDENCE_STATE.modifier.threat_localization` | `sensory_input_state`, `observation_context`, `signal_quality_state`, `known_reference_state` | PASSIVE_CBT_0008 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_SEN_0010 | `PERCEPTION_EVIDENCE_STATE.modifier.detail_retention` | `sensory_input_state`, `observation_context`, `signal_quality_state`, `known_reference_state` | PASSIVE_COG_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_WIL_0001 | `MENTAL_PRESSURE_STATE.modifier.stress_lock` | `mental_pressure_state`, `focus_state`, `resolve_state`, `task_context` | PASSIVE_CBT_0003, PASSIVE_SOC_0001 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_WIL_0002 | `MENTAL_PRESSURE_STATE.modifier.fear_processing` | `mental_pressure_state`, `focus_state`, `resolve_state`, `task_context` | PASSIVE_RES_0008 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_WIL_0003 | `MENTAL_PRESSURE_STATE.modifier.pain_compartmentalization` | `mental_pressure_state`, `focus_state`, `resolve_state`, `task_context`, `injury_pain_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_WIL_0004 | `MENTAL_PRESSURE_STATE.modifier.focus_under_fire` | `mental_pressure_state`, `focus_state`, `resolve_state`, `task_context` | PASSIVE_SYN_0003 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_WIL_0005 | `MENTAL_PRESSURE_STATE.modifier.interruption_resistance` | `mental_pressure_state`, `focus_state`, `resolve_state`, `task_context` | PASSIVE_SYN_0007 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_WIL_0006 | `MENTAL_PRESSURE_STATE.modifier.patience_engine` | `mental_pressure_state`, `focus_state`, `resolve_state`, `task_context` | PASSIVE_CLS_0010, PASSIVE_TEC_0009 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_WIL_0007 | `MENTAL_PRESSURE_STATE.modifier.crisis_clarity` | `mental_pressure_state`, `focus_state`, `resolve_state`, `task_context` | PASSIVE_CBT_0008, PASSIVE_LDR_0008, PASSIVE_MED_0001 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_WIL_0008 | `MENTAL_PRESSURE_STATE.modifier.resolve_reserve` | `mental_pressure_state`, `focus_state`, `resolve_state`, `task_context`, `hazard_environment_state` | PASSIVE_LDR_0004 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_WIL_0009 | `MENTAL_PRESSURE_STATE.modifier.emotional_recovery` | `mental_pressure_state`, `focus_state`, `resolve_state`, `task_context` | PASSIVE_SOC_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_WIL_0010 | `MENTAL_PRESSURE_STATE.modifier.cognitive_endurance` | `mental_pressure_state`, `focus_state`, `resolve_state`, `task_context` | PASSIVE_COG_0008, PASSIVE_PRO_0010, PASSIVE_SOC_0004 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_COG_0001 | `KNOWLEDGE_LEARNING_STATE.modifier.pattern_compression` | `knowledge_provenance`, `study_practice_history`, `task_domain_state`, `error_confidence_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_COG_0002 | `KNOWLEDGE_LEARNING_STATE.modifier.accelerated_familiarity` | `knowledge_provenance`, `study_practice_history`, `task_domain_state`, `error_confidence_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_COG_0003 | `KNOWLEDGE_LEARNING_STATE.modifier.error_memory` | `knowledge_provenance`, `study_practice_history`, `task_domain_state`, `error_confidence_state`, `team_role_state` | PASSIVE_SOC_0002, PASSIVE_SYN_0008, PASSIVE_TEC_0004 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_COG_0004 | `KNOWLEDGE_LEARNING_STATE.modifier.cross_domain_transfer` | `knowledge_provenance`, `study_practice_history`, `task_domain_state`, `error_confidence_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_COG_0005 | `KNOWLEDGE_LEARNING_STATE.modifier.deep_recall` | `knowledge_provenance`, `study_practice_history`, `task_domain_state`, `error_confidence_state`, `team_role_state` | PASSIVE_BST_0006, PASSIVE_BST_0010, PASSIVE_CLS_0008, PASSIVE_FAC_0001, PASSIVE_FAC_0009, PASSIVE_LDR_0007, PASSIVE_LDR_0009, PASSIVE_MED_0009, PASSIVE_PRO_0004, PASSIVE_SEN_0010 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_COG_0006 | `KNOWLEDGE_LEARNING_STATE.modifier.procedural_chunking` | `knowledge_provenance`, `study_practice_history`, `task_domain_state`, `error_confidence_state` | PASSIVE_SUR_0010, PASSIVE_SYN_0002, PASSIVE_WPN_0006 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_COG_0007 | `KNOWLEDGE_LEARNING_STATE.modifier.analytical_habit` | `knowledge_provenance`, `study_practice_history`, `task_domain_state`, `error_confidence_state` | PASSIVE_TEC_0003 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_COG_0008 | `KNOWLEDGE_LEARNING_STATE.modifier.study_momentum` | `knowledge_provenance`, `study_practice_history`, `task_domain_state`, `error_confidence_state`, `focus_state` | PASSIVE_WIL_0010 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_COG_0009 | `KNOWLEDGE_LEARNING_STATE.modifier.mentor_assimilation` | `knowledge_provenance`, `study_practice_history`, `task_domain_state`, `error_confidence_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_COG_0010 | `KNOWLEDGE_LEARNING_STATE.modifier.field_synthesis` | `knowledge_provenance`, `study_practice_history`, `task_domain_state`, `error_confidence_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_CBT_0001 | `COMBAT_ACTION_STATE.modifier.guard_recovery` | `combat_action_state`, `recognized_threat_state`, `encounter_context`, `combat_history` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_CBT_0002 | `COMBAT_ACTION_STATE.modifier.target_transition` | `combat_action_state`, `recognized_threat_state`, `encounter_context`, `combat_history` | PASSIVE_SEN_0002 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_CBT_0003 | `COMBAT_ACTION_STATE.modifier.pressure_breathing` | `combat_action_state`, `recognized_threat_state`, `encounter_context`, `combat_history`, `stamina_state`, `hazard_environment_state` | PASSIVE_REC_0007, PASSIVE_WIL_0001 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_CBT_0004 | `COMBAT_ACTION_STATE.modifier.feint_recognition` | `combat_action_state`, `recognized_threat_state`, `encounter_context`, `combat_history` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_CBT_0005 | `COMBAT_ACTION_STATE.modifier.combat_rhythm` | `combat_action_state`, `recognized_threat_state`, `encounter_context`, `combat_history` | PASSIVE_LDR_0006, PASSIVE_WPN_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_CBT_0006 | `COMBAT_ACTION_STATE.modifier.finish_discipline` | `combat_action_state`, `recognized_threat_state`, `encounter_context`, `combat_history` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_CBT_0007 | `COMBAT_ACTION_STATE.modifier.distance_habit` | `combat_action_state`, `recognized_threat_state`, `encounter_context`, `combat_history`, `equipment_state` | PASSIVE_SEN_0008, PASSIVE_WPN_0003 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_CBT_0008 | `COMBAT_ACTION_STATE.modifier.threat_prioritization` | `combat_action_state`, `recognized_threat_state`, `encounter_context`, `combat_history` | PASSIVE_LDR_0008, PASSIVE_SEN_0009, PASSIVE_WIL_0007 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_CBT_0009 | `COMBAT_ACTION_STATE.modifier.recovery_window` | `combat_action_state`, `recognized_threat_state`, `encounter_context`, `combat_history`, `stamina_state`, `focus_state` | PASSIVE_REC_0001, PASSIVE_SYN_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_CBT_0010 | `COMBAT_ACTION_STATE.modifier.counter_timing` | `combat_action_state`, `recognized_threat_state`, `encounter_context`, `combat_history` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_WPN_0001 | `EQUIPMENT_HANDLING_STATE.modifier.blade_balance` | `equipment_identity`, `equipment_class`, `equipment_familiarity_state`, `action_context`, `equipment_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_WPN_0002 | `EQUIPMENT_HANDLING_STATE.modifier.recoil_familiarity` | `equipment_identity`, `equipment_class`, `equipment_familiarity_state`, `action_context`, `equipment_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_WPN_0003 | `EQUIPMENT_HANDLING_STATE.modifier.polearm_reach` | `equipment_identity`, `equipment_class`, `equipment_familiarity_state`, `action_context`, `equipment_state` | PASSIVE_CBT_0007, PASSIVE_SEN_0008 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_WPN_0004 | `EQUIPMENT_HANDLING_STATE.modifier.improvised_weapon` | `equipment_identity`, `equipment_class`, `equipment_familiarity_state`, `action_context`, `equipment_state`, `team_role_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_WPN_0005 | `EQUIPMENT_HANDLING_STATE.modifier.draw_economy` | `equipment_identity`, `equipment_class`, `equipment_familiarity_state`, `action_context`, `equipment_state` | PASSIVE_CBT_0005 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_WPN_0006 | `EQUIPMENT_HANDLING_STATE.modifier.reload_memory` | `equipment_identity`, `equipment_class`, `equipment_familiarity_state`, `action_context`, `equipment_state` | PASSIVE_COG_0006 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_WPN_0007 | `EQUIPMENT_HANDLING_STATE.modifier.grip_transition` | `equipment_identity`, `equipment_class`, `equipment_familiarity_state`, `action_context`, `equipment_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_WPN_0008 | `EQUIPMENT_HANDLING_STATE.modifier.weapon_retention` | `equipment_identity`, `equipment_class`, `equipment_familiarity_state`, `action_context`, `equipment_state` | PASSIVE_DEF_0008, PASSIVE_PHY_0006 | CANDIDATE_OVERLAP_REVIEW |
| PASSIVE_WPN_0009 | `EQUIPMENT_HANDLING_STATE.modifier.edge_awareness` | `equipment_identity`, `equipment_class`, `equipment_familiarity_state`, `action_context`, `equipment_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |
| PASSIVE_WPN_0010 | `EQUIPMENT_HANDLING_STATE.modifier.ammunition_discipline` | `equipment_identity`, `equipment_class`, `equipment_familiarity_state`, `action_context`, `equipment_state` | NONE_IDENTIFIED | NO_DIRECT_COLLISION_IDENTIFIED |

## Resolution rule

For every candidate overlap:
1. verify whether both records truly modify the same authoritative term;
2. if yes, assign one shared resolver key and cap;
3. if they operate at different stages, document ordered composition instead;
4. if they are merely adjacent concepts, mark the pair `DISTINCT_STAGE_NO_SHARED_TERM`;
5. preserve the decision in later implementation mapping and tests.

No record is canon-promoted by this matrix.
