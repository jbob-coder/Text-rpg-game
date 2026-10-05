from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
SCENE_ILLUSTRATION = REPO_ROOT / "android/app/src/main/java/com/thegame/rpg/ui/SceneIllustration.kt"
GAME_SCREEN = REPO_ROOT / "android/app/src/main/java/com/thegame/rpg/ui/GameScreen.kt"


class D064AndroidSceneProjectionSourceTests(unittest.TestCase):
    def test_scene_renderer_consumes_projected_room_actors_without_presence_heuristic(self):
        source = SCENE_ILLUSTRATION.read_text(encoding="utf-8")

        self.assertIn("roomActors: List<GameRoomActor>", source)
        self.assertIn("PixelStoryActorCatalog.placements(roomActors)", source)
        self.assertNotIn("PixelStoryActorCatalog.placements(\n                locationId = locationId", source)

    def test_scene_renderer_preserves_existing_fallback_scene_ids(self):
        source = SCENE_ILLUSTRATION.read_text(encoding="utf-8")
        for location_id in (
            "PLATFORM_NINE",
            "RELAY_WORKBENCH",
            "GATE_TWELVE",
            "SERVICE_TUNNEL",
            "EVAC_STAIR",
            "TRACE_CHAMBER",
            "DISTRICT_PLAZA",
            "DISTRICT_ARCHIVE",
            "WORKSHOP_ROW",
        ):
            self.assertIn(f'"{location_id}"', source)

    def test_game_screen_wires_authoritative_room_actors_into_every_scene_illustration(self):
        source = GAME_SCREEN.read_text(encoding="utf-8")
        call_count = source.count("SceneIllustration(")
        projected_actor_argument_count = source.count("roomActors = snapshot.room.actors")

        self.assertEqual(2, call_count)
        self.assertEqual(call_count, projected_actor_argument_count)


if __name__ == "__main__":
    unittest.main()
