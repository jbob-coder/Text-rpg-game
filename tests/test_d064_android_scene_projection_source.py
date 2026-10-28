"""Source-level protection for the text-first Android interface.

The Python/Kotlin room projection boundary remains, but authored character art and
scene illustrations must not be a prerequisite of viewing a narrative scene.
"""
from pathlib import Path
import unittest

REPO_ROOT = Path(__file__).resolve().parents[1]
UI = REPO_ROOT / "android/app/src/main/java/com/thegame/rpg/ui/GameScreen.kt"
CHARACTER = REPO_ROOT / "android/app/src/main/java/com/thegame/rpg/ui/CharacterSection.kt"
BRIDGE = REPO_ROOT / "src/textrpg/android_bridge.py"
KOTLIN = REPO_ROOT / "android/app/src/main/java/com/thegame/rpg/engine/GameEngine.kt"


class TextFirstAndroidPresentationSourceTests(unittest.TestCase):
    def test_narrative_and_character_do_not_invoke_scene_or_avatar_art(self):
        screen = UI.read_text(encoding="utf-8")
        character = CHARACTER.read_text(encoding="utf-8")
        for forbidden in ("SceneIllustration(", "PlayerAvatarPanel(", "drawPixelSprite("):
            self.assertNotIn(forbidden, screen)
        for forbidden in ("PlayerAvatarPanel(", "PixelItemIcon(", "PixelUiIcon("):
            self.assertNotIn(forbidden, character)
        self.assertIn("NarrativePanel(", screen)
        self.assertIn("snapshot.choices.forEach", screen)

    def test_authored_room_projection_remains_on_the_engine_boundary(self):
        bridge = BRIDGE.read_text(encoding="utf-8")
        kotlin = KOTLIN.read_text(encoding="utf-8")
        self.assertIn('"room"', bridge)
        self.assertIn("data class GameRoomProjection(", kotlin)
        self.assertIn("RoomProjectionContract", kotlin)

    def test_map_remains_a_selectable_authoritative_route_graph(self):
        screen = UI.read_text(encoding="utf-8")
        self.assertIn("world-map-canvas", screen)
        self.assertIn("map.nodes.forEach", screen)
        self.assertIn("map.edges.forEach", screen)
        self.assertIn("onTravel(selected.id)", screen)
        self.assertNotIn("PixelMapArtCatalog", screen)
        self.assertNotIn("PixelMapMarkerCatalog", screen)


if __name__ == "__main__":
    unittest.main()
