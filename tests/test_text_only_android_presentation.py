from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
UI = ROOT / "android/app/src/main/java/com/thegame/rpg/ui"
IMAGES = ROOT / "android/app/src/main/res/drawable-nodpi"

class TextOnlyAndroidPresentationTest(unittest.TestCase):
    def test_no_pixel_presentation_modules(self):
        self.assertEqual([], sorted(p.name for p in UI.glob("Pixel*.kt")))
        self.assertFalse((UI / "SceneIllustration.kt").exists())

    def test_no_shipped_pixel_drawables(self):
        self.assertEqual([], sorted(p.name for p in IMAGES.glob("pixel_*.png")))

    def test_scene_choices_and_map_are_kept(self):
        source = (UI / "GameScreen.kt").read_text(encoding="utf-8")
        self.assertIn("TextStory(", source)
        self.assertIn("onChoice(choice.id)", source)
        self.assertIn("MapSection(", source)
        self.assertIn('testTag("world-map-canvas")', source)
        self.assertIn('testTag("map-travel")', source)
        self.assertIn("onTravel(selected.id)", source)
        self.assertNotIn("PixelSprite", source)
        self.assertNotIn("SceneIllustration", source)

if __name__ == "__main__":
    unittest.main()
