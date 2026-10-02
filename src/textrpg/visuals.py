from __future__ import annotations

import re
from typing import Any, Dict, Mapping

from .core import RuleError


STABLE_ID = re.compile(r"^[A-Z][A-Z0-9_]*$")

REQUIRED_FIELDS = (
    "height_class",
    "body_proportions",
    "skin_tone",
    "hair",
    "default_outfit",
    "silhouette_anchors",
    "role_markers",
    "equipment_attachment_points",
    "permanent_marks",
    "forbidden_deviations",
    "emotion_set",
    "poses",
)


def validate_character_visuals(
    records: Any,
) -> list[str]:
    """Validate canonical visual identity sheets for recurring characters."""
    errors: list[str] = []
    if not isinstance(records, Mapping):
        return ["character visual records must be an object"]

    for character_id, record in records.items():
        if not isinstance(character_id, str) or not STABLE_ID.fullmatch(character_id):
            errors.append(
                f"character_id must be a stable uppercase ID: {character_id!r}"
            )
            continue
        if not isinstance(record, Mapping):
            errors.append(f"{character_id} visual record must be an object")
            continue

        for field in REQUIRED_FIELDS:
            if field not in record:
                errors.append(f"{character_id} missing required visual field: {field}")

        for field in (
            "height_class",
            "body_proportions",
            "skin_tone",
            "default_outfit",
        ):
            value = record.get(field)
            if value is not None and (not isinstance(value, str) or not value.strip()):
                errors.append(f"{character_id}.{field} must be a non-empty string")

        hair = record.get("hair")
        if hair is not None:
            if not isinstance(hair, Mapping):
                errors.append(f"{character_id}.hair must be an object")
            else:
                for field in ("shape", "length", "palette"):
                    value = hair.get(field)
                    if not isinstance(value, str) or not value.strip():
                        errors.append(
                            f"{character_id}.hair.{field} must be a non-empty string"
                        )

        eye_color = record.get("eye_color")
        if eye_color is not None and (
            not isinstance(eye_color, str) or not eye_color.strip()
        ):
            errors.append(f"{character_id}.eye_color must be null or non-empty text")

        for field in (
            "silhouette_anchors",
            "role_markers",
            "equipment_attachment_points",
            "permanent_marks",
            "forbidden_deviations",
            "emotion_set",
            "poses",
        ):
            value = record.get(field)
            if value is None:
                continue
            if not isinstance(value, list):
                errors.append(f"{character_id}.{field} must be a list")
                continue
            if field in ("silhouette_anchors", "emotion_set", "poses") and not value:
                errors.append(f"{character_id}.{field} must not be empty")
            if any(not isinstance(item, str) or not item.strip() for item in value):
                errors.append(
                    f"{character_id}.{field} entries must be non-empty strings"
                )
            if len(value) != len(set(value)):
                errors.append(f"{character_id}.{field} contains duplicate entries")

        palette = record.get("palette")
        if palette is not None:
            if not isinstance(palette, Mapping):
                errors.append(f"{character_id}.palette must be an object")
            else:
                for name, value in palette.items():
                    if not isinstance(name, str) or not name:
                        errors.append(f"{character_id}.palette has invalid key")
                    if not isinstance(value, str) or not value:
                        errors.append(
                            f"{character_id}.palette.{name} must be non-empty text"
                        )

        references = record.get("approved_reference_assets", [])
        if not isinstance(references, list):
            errors.append(
                f"{character_id}.approved_reference_assets must be a list"
            )
        elif any(not isinstance(item, str) or not item for item in references):
            errors.append(
                f"{character_id}.approved_reference_assets entries must be strings"
            )

    return errors


def assert_valid_character_visuals(
    records: Mapping[str, Mapping[str, Any]],
) -> None:
    errors = validate_character_visuals(records)
    if errors:
        raise RuleError(
            "Invalid character visual identities:\n- " + "\n- ".join(errors)
        )


def character_generation_contract(
    character_id: str,
    record: Mapping[str, Any],
) -> Dict[str, Any]:
    """Return a normalized identity contract for art-generation/pixel-art tooling.

    This does not generate art. It produces the exact immutable identity facts that
    future art tools must carry forward before an image can be considered for canon.
    """
    errors = validate_character_visuals({character_id: record})
    if errors:
        raise RuleError(
            "Invalid character visual identity:\n- " + "\n- ".join(errors)
        )

    return {
        "character_id": character_id,
        "identity": {
            "height_class": record["height_class"],
            "body_proportions": record["body_proportions"],
            "skin_tone": record["skin_tone"],
            "hair": dict(record["hair"]),
            "eye_color": record.get("eye_color"),
            "default_outfit": record["default_outfit"],
            "silhouette_anchors": list(record["silhouette_anchors"]),
            "role_markers": list(record["role_markers"]),
            "equipment_attachment_points": list(
                record["equipment_attachment_points"]
            ),
            "permanent_marks": list(record["permanent_marks"]),
            "forbidden_deviations": list(record["forbidden_deviations"]),
        },
        "approved_expression_set": list(record["emotion_set"]),
        "approved_poses": list(record["poses"]),
        "palette": dict(record.get("palette", {})),
        "approved_reference_assets": list(
            record.get("approved_reference_assets", [])
        ),
        "canon_rule": (
            "Generated art is candidate-only until it matches this identity "
            "contract and is explicitly approved."
        ),
    }
