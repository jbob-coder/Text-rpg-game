"""Read-only D-084 editorial review gate; this file is not a runtime lore loader.

Run: python tools/validate_d084_review_manifest.py
No imports from textrpg, no mutations and no access to private Google Drive.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/world/D084_EVENT_KNOWLEDGE_REVIEW_MANIFEST_2026-10-27.json"
SLICE = ROOT / "content/vertical_slice_01.json"
BURST = {
    "FIRST_PORTAL_OPENINGS", "SPATIAL_RUPTURES", "INTELLIGENT_INVADERS_ARRIVE",
    "CRYSTAL_BEARING_BEASTS_ARRIVE", "CELESTIAL_SYSTEM_APPEARS",
}
STATE_PATHS = {
    "state.knowledge", "state.npcs[*].knowledge", "state.npcs[*].memories",
    "state.npcs[*].goals", "state.npcs[*].story_state",
}

# These labels belong solely to the D-084 reviewer, not the shipped content pack.
# Fail closed if they appear even in a nested scene/dialogue/metadata string.
REVIEW_ONLY_CONTENT_IDS = {
    "REVIEW_INITIAL_BURST", "FIRST_WAR", "TERRITORIAL_TRUCE",
    "SYSTEM_TABLET_EXISTS",
} | BURST  # All five H-36 event labels are also reviewer-only until approved.


def _find_review_only_content_ids(value: Any, path: str = "content") -> list[str]:
    """Find accidental imports at any depth, including dictionary keys."""
    hits: list[str] = []
    if isinstance(value, dict):
        for key, item in value.items():
            if isinstance(key, str):
                normalized_key = key.casefold()
                for identifier in sorted(REVIEW_ONLY_CONTENT_IDS):
                    if identifier.casefold() in normalized_key:
                        hits.append(f"{path}.{key}: {identifier}")
            hits.extend(_find_review_only_content_ids(item, f"{path}.{key}"))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            hits.extend(_find_review_only_content_ids(item, f"{path}[{index}]"))
    elif isinstance(value, str):
        normalized_value = value.casefold()
        for identifier in sorted(REVIEW_ONLY_CONTENT_IDS):
            if identifier.casefold() in normalized_value:
                hits.append(f"{path}: {identifier}")
    return hits


# Closed, editorial-only contract: unknown fields can carry unreviewed lore or
# private NPC state. Reject extensions until a reviewed schema revision exists.
REVIEW_KEYS = {
    "manifest": {"schema_version", "kind", "review_status", "runtime_import",
                 "source_authorities", "initial_burst", "relative_events",
                 "unresolved", "calendar", "historical_sources", "editorial",
                 "knowledge_boundary", "gameplay_boundary"},
    "source_authorities": {"narrative", "manuscript", "technical"},
    "initial_burst": {"phase_id", "temporal_relation", "source_ids", "members",
                      "absolute_date", "location"},
    "relative_events.FIRST_WAR": {"id", "source_ids", "after", "absolute_date", "combatants"},
    "relative_events.TERRITORIAL_TRUCE": {"id", "source_ids", "after", "absolute_date", "signatories"},
    "unresolved": {"first_crystal_forging_relative_to_war", "current_game_year",
                   "world_identity_vs_earth", "post_crystal_era_label"},
    "calendar": {"ac_definition", "source", "allow_legacy_after_crystal_interpretation"},
    "historical_sources[]": {"id", "status", "observed_dates",
                             "adopted_into_current_canon"},
    "editorial": {"manuscript_version", "narrative_sections",
                  "historical_note_section", "chapter_xii_id",
                  "alternative_xii_id", "dr06_adaptation", "dr06_is_historical_event"},
    "knowledge_boundary": {"world_secret_proposition", "source_ids",
                           "author_truth_status", "initial_player_knowledge",
                           "initial_npc_knowledge", "invader_knowledge",
                           "android_raw_npc_state_allowed",
                           "requires_authored_discovery_for_runtime"},
    "gameplay_boundary": {"current_content_id", "current_content_canon_status",
                          "migration_status", "preserve_npc_id",
                          "preserve_existing_knowledge_id",
                          "preserve_existing_story_track", "protect_state_paths",
                          "never_auto_create_from_editorial"},
}


def _distinct_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        result = json.load(stream, object_pairs_hook=_distinct_pairs)
    if not isinstance(result, dict):
        raise ValueError("top-level JSON object required")
    return result


def validate(manifest: dict[str, Any], slice_content: dict[str, Any]) -> list[str]:
    """Validate non-runtime boundaries. Returns specific failures, never modifies inputs."""
    errors: list[str] = []

    def check_keys(label: str, value: dict[str, Any]) -> None:
        expected = REVIEW_KEYS[label]
        if set(value) != expected:
            missing = sorted(expected - set(value))
            unexpected = sorted(set(value) - expected)
            errors.append(f"{label} field mismatch: missing={missing}, unexpected={unexpected}")

    def string_ids(value: Any, label: str) -> list[str]:
        if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
            errors.append(f"{label} must be a list of strings")
            return []
        return value

    check_keys("manifest", manifest)

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    def obj(key: str) -> dict[str, Any]:
        value = manifest.get(key)
        if not isinstance(value, dict):
            errors.append(f"{key} must be an object")
            return {}
        check_keys(key, value)
        return value

    require(type(manifest.get("schema_version")) is int and manifest["schema_version"] == 1, "schema_version must equal integer 1")
    require(manifest.get("kind") == "D084_EDITORIAL_REVIEW_CONTRACT", "unexpected contract kind")
    require(manifest.get("review_status") == "PROPOSED_NOT_INTEGRATED", "review cannot auto-promote")
    require(manifest.get("runtime_import") is False, "review content must not be a runtime import")
    authorities = obj("source_authorities")
    require("H-01..H-36" in str(authorities.get("narrative", "")), "narrative source authority missing")
    require("v0.9.1" in str(authorities.get("manuscript", "")), "manuscript authority/version mismatch")

    burst = obj("initial_burst")
    members = burst.get("members")
    require(isinstance(members, list) and len(members) == 5 and set(map(str, members)) == BURST,
            "H-36 initial burst must contain exactly five distinct types")
    require(burst.get("phase_id") == "REVIEW_INITIAL_BURST", "phase ID must remain review-only")
    require(burst.get("temporal_relation") == "SAME_HISTORICAL_PHASE_NOT_SAME_SECOND", "burst cannot impose micro-order")
    require({"H-32", "H-33", "H-34", "H-35", "H-36"}.issubset(set(string_ids(burst.get("source_ids"), "initial_burst.source_ids"))), "H-36 provenance incomplete")
    require(burst.get("absolute_date") is None and burst.get("location") is None, "burst date/location remains unknown")

    events = manifest.get("relative_events")
    if not isinstance(events, list) or len(events) != 2 or not all(isinstance(x, dict) for x in events):
        errors.append("exactly two review-only relative event records required")
    else:
        war, truce = events
        check_keys("relative_events.FIRST_WAR", war)
        check_keys("relative_events.TERRITORIAL_TRUCE", truce)
        require(war.get("id") == "FIRST_WAR" and war.get("after") == "REVIEW_INITIAL_BURST"
                and "H-12" in string_ids(war.get("source_ids"), "FIRST_WAR.source_ids"), "First War must follow System in H-12")
        require(truce.get("id") == "TERRITORIAL_TRUCE" and truce.get("after") == "FIRST_WAR"
                and "H-13" in string_ids(truce.get("source_ids"), "TERRITORIAL_TRUCE.source_ids"), "territorial truce must follow First War in H-13")
        require(all(x.get("absolute_date") is None for x in events), "absolute historical years remain unadopted")
        require(war.get("combatants") is None and truce.get("signatories") is None, "war parties/signatories unverified")

    unresolved = obj("unresolved")
    require(unresolved.get("first_crystal_forging_relative_to_war") == "UNKNOWN", "first forge timing not determined")
    require(unresolved.get("current_game_year") is None, "game year not adopted")
    require(unresolved.get("world_identity_vs_earth") == "UNRECONCILED", "world identity conflict still open")
    require(unresolved.get("post_crystal_era_label") is None, "post-crystal era not named")

    calendar = obj("calendar")
    require(calendar.get("ac_definition") == "Antes del Crystal"
            and calendar.get("source") == "OWNER_CORRECTION_2026-10-08"
            and calendar.get("allow_legacy_after_crystal_interpretation") is False, "AC is Antes del Crystal, never After Crystal")

    legacy = manifest.get("historical_sources")
    require(isinstance(legacy, list) and len(legacy) == 1 and isinstance(legacy[0], dict)
            and legacy[0].get("id") == "WORLD_CAUSALITY_ATLAS_2670_V1"
            and legacy[0].get("status") == "HISTORICAL_UNLINKED"
            and legacy[0].get("adopted_into_current_canon") is False
            and legacy[0].get("observed_dates") == ["2645-2659", "2660", "2670"],
            "old 2670 campaign is not automatically H-36 canon")
    if isinstance(legacy, list):
        for historical_record in legacy:
            if isinstance(historical_record, dict):
                check_keys("historical_sources[]", historical_record)

    editorial = obj("editorial")
    require(editorial.get("manuscript_version") == "v0.9.1"
            and editorial.get("narrative_sections") == 12
            and editorial.get("historical_note_section") == "XIII", "manuscript revision or section count mismatch")
    require(editorial.get("chapter_xii_id") == "NOV-XII-MANUSCRITO-v0.9.1"
            and editorial.get("alternative_xii_id") == "NOV-XII-DR06-BORRADOR-v0.1", "unqualified NOV-XII is ambiguous")
    require(editorial.get("dr06_is_historical_event") is False
            and editorial.get("dr06_adaptation") == "COMPOSITE_SCENE_PROPOSED", "DR-06 remains proposed fiction")

    knowledge = obj("knowledge_boundary")
    require(knowledge.get("world_secret_proposition") == "SYSTEM_TABLET_EXISTS"
            and "H-04" in string_ids(knowledge.get("source_ids"), "knowledge_boundary.source_ids"), "System tablet must retain H-04 provenance")
    require(knowledge.get("author_truth_status") == "CONFIRMED_NARRATIVE_ONLY", "secret is not gameplay-enabled")
    require(knowledge.get("initial_player_knowledge") == "UNSPECIFIED_NO_AUTOGRANT"
            and knowledge.get("initial_npc_knowledge") == "UNSPECIFIED_NO_AUTOGRANT", "author truth must not be granted to NPC/player")
    require(knowledge.get("invader_knowledge") == "DOES_NOT_KNOW", "invaders do not know of the tablet")
    require(knowledge.get("android_raw_npc_state_allowed") is False
            and knowledge.get("requires_authored_discovery_for_runtime") is True, "privacy and discovery gates required")

    gameplay = obj("gameplay_boundary")
    require(gameplay.get("migration_status") == "NOT_AUTHORIZED", "narrative-to-game migration needs approval")
    require(gameplay.get("current_content_id") == "CONTENT_VERTICAL_SLICE_01"
            and gameplay.get("current_content_canon_status") == "provisional_canon", "provisional content must remain provisional")
    require(gameplay.get("preserve_npc_id") == "NPC_TAMSIN"
            and gameplay.get("preserve_existing_knowledge_id") == "KNOW_RELAY_DESTINATION_SERVICE_GATE_12"
            and gameplay.get("preserve_existing_story_track") == "TRACK_RELAY_CASE", "existing persistent social IDs must be preserved")
    require(set(string_ids(gameplay.get("protect_state_paths"), "gameplay_boundary.protect_state_paths")) == STATE_PATHS,
            "player/NPC/private state owners must be separate")
    require(set(string_ids(gameplay.get("never_auto_create_from_editorial"), "gameplay_boundary.never_auto_create_from_editorial")) ==
            {"npc", "location", "route", "quest", "item", "ability", "save_field"}, "proposed prose cannot create gameplay entities")

    require(slice_content.get("content_id") == gameplay.get("current_content_id")
            and slice_content.get("canon_status") == "provisional_canon", "current slice baseline changed: refresh before migration")
    initial = slice_content.get("initial_state")
    if not isinstance(initial, dict):
        errors.append("initial_state must be an object")
        initial = {}
    npcs = initial.get("npcs")
    if not isinstance(npcs, dict):
        errors.append("initial_state.npcs must be an object")
        npcs = {}
    npc = npcs.get("NPC_TAMSIN")
    if not isinstance(npc, dict):
        errors.append("Tamsin social containers changed")
        npc = {}
    require(all(x in npc for x in ("knowledge", "memories", "goals", "story_state")), "Tamsin social containers changed")
    for field, required_type in (("knowledge", dict), ("memories", list),
                                 ("goals", dict), ("story_state", dict)):
        require(isinstance(npc.get(field), required_type),
                f"Tamsin {field} must retain its original container type")
    player_knowledge = initial.get("knowledge", {})
    require(isinstance(player_knowledge, dict), "initial player knowledge must be an object")
    for npc_id, npc_state in npcs.items():
        if not isinstance(npc_state, dict):
            errors.append(f"initial NPC state must be an object: {npc_id}")
            continue
        if "knowledge" in npc_state:
            require(isinstance(npc_state["knowledge"], dict),
                    f"initial NPC knowledge must be an object: {npc_id}")
    for hit in _find_review_only_content_ids(slice_content):
        errors.append(f"review-only identifier imported into gameplay content: {hit}")
    relationships = initial.get("relationships")
    require(isinstance(relationships, dict) and gameplay.get("preserve_npc_id") in relationships,
            "Tamsin relationship anchor changed")
    return errors


def main() -> int:
    try:
        failures = validate(load_json(MANIFEST), load_json(SLICE))
    except (OSError, ValueError, TypeError) as exc:
        print(f"D-084 REVIEW GATE ERROR: {exc}", file=sys.stderr)
        return 2
    if failures:
        for error in failures:
            print(f"D-084 REVIEW FAIL: {error}", file=sys.stderr)
        return 1
    print("D-084 REVIEW PASS: editorial provenance, temporal constraints and non-runtime boundaries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
