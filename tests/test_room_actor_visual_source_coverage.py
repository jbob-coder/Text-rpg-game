"""Cross-language source contract guard for authored, visible room people.

This is static source coverage, not a render, emulator or APK test.
It fails when a room-presence sidecar introduces a visual family or placement
key that the current Android actor catalog cannot render.
"""
from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "vertical_slice_01.json"
PRESENCE = ROOT / "content" / "vertical_slice_01_room_presence.json"
CATALOG = ROOT / "android" / "app" / "src" / "main" / "java" / "com" / "thegame" / "rpg" / "ui" / "PixelStoryActorCatalog.kt"
RESOLVER = ROOT / "android" / "app" / "src" / "main" / "java" / "com" / "thegame" / "rpg" / "ui" / "PixelStoryActorPlacementResolver.kt"


def _supported_families() -> set[str]:
    source = CATALOG.read_text(encoding="utf-8")
    section = source.split("private fun spriteFor(", 1)[1].split("\n    fun placements(", 1)[0]
    return set(re.findall(r'"([A-Z][A-Z0-9_]+)"\s*->\s*\w+', section))


def _supported_placements() -> set[str]:
    source = RESOLVER.read_text(encoding="utf-8")
    constants = dict(re.findall(r'const val (\w+) = "([^"]+)"', source))
    section = source.split("private val points = mapOf(", 1)[1].split("\n    fun resolve(", 1)[0]
    used = set(re.findall(r'(\w+)\s+to\s+PixelStoryActorStagePoint', section))
    return {constants[name] for name in used}


class RoomActorVisualSourceCoverageTests(unittest.TestCase):
    def test_every_authored_visible_person_has_existing_android_art_and_slot(self) -> None:
        content = json.loads(CONTENT.read_text(encoding="utf-8"))
        presence = json.loads(PRESENCE.read_text(encoding="utf-8"))
        scenes = content["scenes"]
        families = _supported_families()
        placements = _supported_placements()

        self.assertTrue(families, "Android story-actor sprite mapping was not found")
        self.assertTrue(placements, "Android story-actor placement mapping was not found")
        self.assertTrue(presence, "No authored room presence was found")

        for scene_id, actors in presence.items():
            with self.subTest(scene=scene_id):
                self.assertIn(scene_id, scenes)
                self.assertIsInstance(actors, list)
                seen: set[str] = set()
                for actor in actors:
                    presentation_id = actor["presentation_id"]
                    self.assertNotIn(presentation_id, seen)
                    seen.add(presentation_id)
                    self.assertIn(
                        actor["visual_family"], families,
                        f"{scene_id}/{presentation_id}: Android sprite family is missing",
                    )
                    self.assertIn(
                        actor["placement_key"], placements,
                        f"{scene_id}/{presentation_id}: Android placement is missing",
                    )


if __name__ == "__main__":
    unittest.main()
