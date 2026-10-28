"""Regression guard: THE GAME keeps a navigable map but no sprite-art runtime.

Owner direction supersedes the retired pixel visual/asset production documents.
Visual historical records remain in docs/Git history, not in Android runtime.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
UI = ROOT / "android/app/src/main/java/com/thegame/rpg/ui"
DRAWABLE = ROOT / "android/app/src/main/res/drawable-nodpi"

FORBIDDEN_RENDER_FILES = (
    "SceneIllustration.kt",
    "PixelEnvironmentPreview.kt",
    "PixelStoryActorPlacementResolver.kt",
)
FORBIDDEN_CALLS = (
    "SceneIllustration(",
    "PlayerAvatarPanel(",
    "PixelItemIcon(",
    "PixelUiIcon(",
    "drawPixelSprite(",
)


class TextFirstPresentationPolicyTests(unittest.TestCase):
    def test_no_pixel_runtime_catalogs_or_character_scene_renderers(self):
        self.assertEqual([], sorted(p.name for p in UI.glob("Pixel*Catalog.kt")))
        self.assertEqual(
            [],
            sorted(name for name in FORBIDDEN_RENDER_FILES if (UI / name).exists()),
        )

    def test_no_pixel_sprite_pngs_in_packaged_android_resources(self):
        self.assertEqual(
            [], sorted(p.name for p in DRAWABLE.glob("pixel_*.png"))
        )

    def test_active_android_ui_does_not_call_sprites_or_art_layers(self):
        active = (
            "GameScreen.kt",
            "CharacterSection.kt",
            "PixelComponents.kt",
            "StatusComponents.kt",
            "StatsSection.kt",
            "PixelMapTravelTransition.kt",
        )
        for filename in active:
            source = (UI / filename).read_text(encoding="utf-8")
            for call in FORBIDDEN_CALLS:
                with self.subTest(file=filename, call=call):
                    self.assertNotIn(call, source)

    def test_text_choice_and_map_travel_are_preserved(self):
        source = (UI / "GameScreen.kt").read_text(encoding="utf-8")
        self.assertIn("snapshot.choices.forEach", source)
        self.assertIn("world-map-canvas", source)
        self.assertIn("map.edges.forEach", source)
        self.assertIn("map.nodes.forEach", source)
        self.assertIn("onTravel(selected.id)", source)
        self.assertTrue((ROOT / "src/textrpg/core.py").is_file())


if __name__ == "__main__":
    unittest.main()
