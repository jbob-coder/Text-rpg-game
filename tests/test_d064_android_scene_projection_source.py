from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GAME_SCREEN = ROOT / "android/app/src/main/java/com/thegame/rpg/ui/GameScreen.kt"
SCENE_ILLUSTRATION = ROOT / "android/app/src/main/java/com/thegame/rpg/ui/SceneIllustration.kt"
ACTOR_CATALOG = ROOT / "android/app/src/main/java/com/thegame/rpg/ui/PixelStoryActorCatalog.kt"


def test_scene_illustration_consumes_projected_room_actors():
    source = SCENE_ILLUSTRATION.read_text(encoding="utf-8")
    assert "roomActors: List<GameRoomActor> = emptyList()" in source
    assert "PixelStoryActorCatalog.placements(roomActors)" in source
    assert "PixelStoryActorCatalog.placements(\n        locationId = locationId" not in source


def test_game_screen_wires_room_projection_at_both_scene_callsites():
    source = GAME_SCREEN.read_text(encoding="utf-8")
    assert source.count("roomActors = snapshot.room.actors") == 2


def test_catalog_maps_safe_visual_and_semantic_placement_fields():
    source = ACTOR_CATALOG.read_text(encoding="utf-8")
    assert "fun placements(actors: List<GameRoomActor>)" in source
    assert "actor.visualFamily" in source
    assert "PixelStoryActorPlacementResolver.resolve(actor.placementKey)" in source


def test_fallback_scene_contract_remains_present():
    source = GAME_SCREEN.read_text(encoding="utf-8")
    assert '"PLATFORM_NINE"' in source
    assert '"RELAY_WORKBENCH"' in source
    assert '"SERVICE_TUNNEL"' in source
