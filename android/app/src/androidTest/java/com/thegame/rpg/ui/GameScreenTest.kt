package com.thegame.rpg.ui

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.size
import androidx.compose.ui.Modifier
import androidx.compose.ui.test.assert
import androidx.compose.ui.test.assertCountEquals
import androidx.compose.ui.test.assertHasClickAction
import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.hasScrollAction
import androidx.compose.ui.test.junit4.createComposeRule
import androidx.compose.ui.test.onAllNodesWithTag
import androidx.compose.ui.test.onNodeWithTag
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.performClick
import androidx.compose.ui.test.performScrollTo
import androidx.compose.ui.unit.dp
import com.thegame.rpg.GameUiState
import com.thegame.rpg.TravelTransitionUiState
import com.thegame.rpg.boot.BootState
import com.thegame.rpg.engine.GameAttribute
import com.thegame.rpg.engine.GameChoice
import com.thegame.rpg.engine.GameCondition
import com.thegame.rpg.engine.GameEquipmentSlot
import com.thegame.rpg.engine.GameInventory
import com.thegame.rpg.engine.GameResource
import com.thegame.rpg.engine.GameRoomActor
import com.thegame.rpg.engine.GameRoomProjection
import com.thegame.rpg.engine.GameSnapshot
import com.thegame.rpg.engine.GameStatContribution
import com.thegame.rpg.engine.GameStatInspection
import com.thegame.rpg.engine.GameVisuals
import org.junit.Rule
import org.junit.Test

class GameScreenTest {
    @get:Rule
    val composeRule = createComposeRule()

    private val snapshot = GameSnapshot(
        sceneId = "SCENE_GATE",
        title = "City Gate",
        body = "Rain needles the old stone while the gate guards watch every traveler.",
        choices = listOf(
            GameChoice("ENTER", "Enter the city", true),
            GameChoice("WAIT", "Wait beneath the arch", true),
        ),
        resources = listOf(
            GameResource("health", 10.0, 12.0),
            GameResource("stamina", 8.0, 10.0),
        ),
        turn = 3,
        timeMinutes = 45,
        location = "CITY_GATE",
    )

    @Test
    fun gameplayShellShowsScrollableNarrativeAndTextNavigation() {
        composeRule.setContent {
            PixelTheme {
                GameScreen(
                    snapshot = snapshot,
                    busy = false,
                    onChoice = {},
                    onNavigate = {},
                )
            }
        }

        composeRule.onNodeWithTag("narrative-scroll")
            .assertIsDisplayed()
            .assert(hasScrollAction())
        composeRule.onNodeWithText(snapshot.body).assertIsDisplayed()
        composeRule.onNodeWithTag("story-resource-hud").assertIsDisplayed()
        composeRule.onNodeWithTag("story-resource-value-health").assertIsDisplayed()
        composeRule.onNodeWithText("Health 10 / 12").assertIsDisplayed()
        composeRule.onNodeWithTag("story-resource-value-stamina").assertIsDisplayed()
        composeRule.onAllNodesWithTag("player-avatar").assertCountEquals(0)
        composeRule.onAllNodesWithTag("scene-illustration").assertCountEquals(0)
        composeRule.onNodeWithText("READ ALOUD")
            .performScrollTo()
            .assertIsDisplayed()

        snapshot.choices.forEach { choice ->
            composeRule.onNodeWithTag("choice-${choice.id}")
                .performScrollTo()
                .assertIsDisplayed()
                .assertHasClickAction()
        }

        listOf("Stats", "Inventory", "Quests", "Map", "More").forEach { label ->
            composeRule.onNodeWithText(label).assertIsDisplayed().assertHasClickAction()
        }
    }

    @Test
    fun playerSafeRoomActorsRemainVisibleAsTextWithoutArtwork() {
        val withActor = snapshot.copy(
            room = GameRoomProjection(
                locationId = "CITY_GATE",
                actors = listOf(
                    GameRoomActor(
                        presentationId = "NPC_TAMSIN",
                        knownActorId = "NPC_TAMSIN",
                        displayName = "Tamsin",
                        visualFamily = "NPC_TAMSIN",
                        placementKey = "GATE_RIGHT",
                        poseKey = null,
                        outfitKey = null,
                        visibleTags = emptyList(),
                        inspectable = true,
                        dialogueAvailable = false,
                        actions = emptyList(),
                    )
                ),
            )
        )
        composeRule.setContent {
            PixelTheme {
                GameScreen(
                    snapshot = withActor,
                    busy = false,
                    onChoice = {},
                    onNavigate = {},
                )
            }
        }
        composeRule.onNodeWithTag("room-actors-text").assertIsDisplayed()
        composeRule.onNodeWithText("PRESENT: Tamsin").assertIsDisplayed()
        composeRule.onAllNodesWithTag("player-avatar").assertCountEquals(0)
        composeRule.onAllNodesWithTag("scene-illustration").assertCountEquals(0)
    }

    @Test
    fun overflowingNarrativeShowsAuthoredScrollMarker() {
        val longSnapshot = snapshot.copy(
            body = List(24) {
                "The maintenance corridor keeps narrowing while emergency relays pulse against the wall."
            }.joinToString(" "),
        )

        composeRule.setContent {
            PixelTheme {
                androidx.compose.foundation.layout.Box(
                    Modifier.size(width = 320.dp, height = 480.dp),
                ) {
                    GameScreen(
                        snapshot = longSnapshot,
                        busy = false,
                        onChoice = {},
                        onNavigate = {},
                    )
                }
            }
        }

        composeRule.onNodeWithTag("narrative-scroll-marker").assertIsDisplayed()
    }

    @Test
    fun stableGameScreenMapControlEmitsNavigationRequest() {
        var destination: String? = null

        composeRule.setContent {
            PixelTheme {
                GameScreen(
                    snapshot = snapshot,
                    busy = false,
                    onChoice = {},
                    onNavigate = { destination = it },
                )
            }
        }

        composeRule.onNodeWithTag("nav-map")
            .performScrollTo()
            .assertIsDisplayed()
            .assertHasClickAction()
            .performClick()

        composeRule.runOnIdle {
            check(destination == "Map") {
                "Expected stable GameScreen to emit Map navigation, got $destination"
            }
        }
    }

    @Test
    fun statsScreenRequestsPlayerSafeInspection() {
        var requestedPath: String? = null
        val statSnapshot = snapshot.copy(
            attributes = listOf(
                GameAttribute(
                    id = "endurance",
                    name = "Endurance",
                    base = 35.0,
                    effective = 37.0,
                    delta = 2.0,
                    modified = true,
                    role = "sustained physical resilience",
                )
            )
        )

        composeRule.setContent {
            PixelTheme {
                TheGameRoot(
                    uiState = GameUiState(
                        bootState = BootState.Ready,
                        snapshot = statSnapshot,
                    ),
                    onChoice = {},
                    onSave = {},
                    onLoad = {},
                    onNarrate = { false },
                    onReplayNarration = { false },
                    onStopNarration = {},
                    autoReadNarration = false,
                    onAutoReadChange = {},
                    narrationRate = 0.92f,
                    onNarrationRateChange = {},
                    textDelayMs = 0,
                    onTextDelayChange = {},
                    onCheat = {},
                    onEquip = {},
                    onUnequip = {},
                    onInspectStatus = { requestedPath = it },
                    onTravel = {},
                    onTravelTransitionFinished = {},
                )
            }
        }

        composeRule.onNodeWithTag("nav-stats")
            .performScrollTo()
            .performClick()
        composeRule.onNodeWithTag("stats-attribute-endurance")
            .performScrollTo()
            .assertHasClickAction()
            .performClick()

        composeRule.runOnIdle {
            check(requestedPath == "attributes.endurance") {
                "Expected Endurance inspection request, got $requestedPath"
            }
        }
    }

    @Test
    fun statsScreenRendersPlayerSafeEquipmentContribution() {
        val statSnapshot = snapshot.copy(
            attributes = listOf(
                GameAttribute(
                    id = "endurance",
                    name = "Endurance",
                    base = 35.0,
                    effective = 37.0,
                    delta = 2.0,
                    modified = true,
                    role = "sustained physical resilience",
                )
            )
        )
        val inspection = GameStatInspection(
            path = "attributes.endurance",
            kind = "attribute",
            total = 37.0,
            contributions = listOf(
                GameStatContribution("base", 35.0),
                GameStatContribution("equipment:body", 2.0),
            ),
        )

        composeRule.setContent {
            PixelTheme {
                TheGameRoot(
                    uiState = GameUiState(
                        bootState = BootState.Ready,
                        snapshot = statSnapshot,
                        statInspectionPath = "attributes.endurance",
                        statInspection = inspection,
                    ),
                    onChoice = {},
                    onSave = {},
                    onLoad = {},
                    onNarrate = { false },
                    onReplayNarration = { false },
                    onStopNarration = {},
                    autoReadNarration = false,
                    onAutoReadChange = {},
                    narrationRate = 0.92f,
                    onNarrationRateChange = {},
                    textDelayMs = 0,
                    onTextDelayChange = {},
                    onCheat = {},
                    onEquip = {},
                    onUnequip = {},
                    onInspectStatus = {},
                    onTravel = {},
                    onTravelTransitionFinished = {},
                )
            }
        }

        composeRule.onNodeWithTag("nav-stats")
            .performScrollTo()
            .performClick()
        composeRule.onNodeWithTag("stats-attribute-detail")
            .performScrollTo()
            .assertIsDisplayed()
        composeRule.onNodeWithText("Chest: +2").assertIsDisplayed()
    }

    @Test
    fun projectedRelayStateRendersThroughNarrativeScene() {
        val relaySnapshot = snapshot.copy(
            location = "RELAY_WORKBENCH",
            visuals = GameVisuals(relayState = "damaged"),
        )

        composeRule.setContent {
            PixelTheme {
                GameScreen(
                    snapshot = relaySnapshot,
                    busy = false,
                    onChoice = {},
                    onNavigate = {},
                )
            }
        }

        composeRule.onNodeWithText(relaySnapshot.body).assertIsDisplayed()
        composeRule.onAllNodesWithTag("scene-illustration").assertCountEquals(0)
    }

    @Test
    fun characterScreenSelectsAuthoredPaperDollSlotAndRoutesUnequip() {
        var unequippedSlot: String? = null
        val equippedSnapshot = snapshot.copy(
            inventory = GameInventory(
                equipment = listOf(
                    GameEquipmentSlot(
                        slot = "body",
                        equipped = true,
                        itemId = "ITEM_DEPOT_JACKET",
                        name = "Depot utility jacket",
                        quality = "standard",
                    ),
                    GameEquipmentSlot(
                        slot = "hands",
                        equipped = true,
                        itemId = "ITEM_WORK_GLOVES",
                        name = "Insulated work gloves",
                        quality = "standard",
                    ),
                )
            )
        )

        composeRule.setContent {
            PixelTheme {
                TheGameRoot(
                    uiState = GameUiState(
                        bootState = BootState.Ready,
                        snapshot = equippedSnapshot,
                    ),
                    onChoice = {},
                    onSave = {},
                    onLoad = {},
                    onNarrate = { false },
                    onReplayNarration = { false },
                    onStopNarration = {},
                    autoReadNarration = false,
                    onAutoReadChange = {},
                    narrationRate = 0.92f,
                    onNarrationRateChange = {},
                    textDelayMs = 0,
                    onTextDelayChange = {},
                    onCheat = {},
                    onEquip = {},
                    onUnequip = { unequippedSlot = it },
                    onInspectStatus = {},
                    onTravel = {},
                    onTravelTransitionFinished = {},
                )
            }
        }

        composeRule.onNodeWithTag("nav-character")
            .performScrollTo()
            .performClick()
        composeRule.onNodeWithTag("character-scroll")
            .assertIsDisplayed()
        composeRule.onNodeWithTag("character-slot-body")
            .assertHasClickAction()
            .performClick()
        composeRule.onNodeWithTag("character-equipment-detail")
            .assertIsDisplayed()
        composeRule.onNodeWithText("Depot utility jacket").assertIsDisplayed()
        composeRule.onNodeWithText("UNEQUIP")
            .assertHasClickAction()
            .performClick()

        composeRule.runOnIdle {
            check(unequippedSlot == "body") {
                "Expected Character screen to route body unequip, got $unequippedSlot"
            }
        }
    }

    @Test
    fun characterScreenKeepsUnmappedEquipmentLogicalOnly() {
        val unmappedSnapshot = snapshot.copy(
            inventory = GameInventory(
                equipment = listOf(
                    GameEquipmentSlot(
                        slot = "head",
                        equipped = true,
                        itemId = "ITEM_FUTURE_HELMET",
                        name = "Future helmet",
                    ),
                )
            )
        )

        composeRule.setContent {
            PixelTheme {
                TheGameRoot(
                    uiState = GameUiState(
                        bootState = BootState.Ready,
                        snapshot = unmappedSnapshot,
                    ),
                    onChoice = {},
                    onSave = {},
                    onLoad = {},
                    onNarrate = { false },
                    onReplayNarration = { false },
                    onStopNarration = {},
                    autoReadNarration = false,
                    onAutoReadChange = {},
                    narrationRate = 0.92f,
                    onNarrationRateChange = {},
                    textDelayMs = 0,
                    onTextDelayChange = {},
                    onCheat = {},
                    onEquip = {},
                    onUnequip = {},
                    onInspectStatus = {},
                    onTravel = {},
                    onTravelTransitionFinished = {},
                )
            }
        }

        composeRule.onNodeWithTag("nav-character")
            .performScrollTo()
            .performClick()
        composeRule.onNodeWithTag("character-slot-head")
            .assertHasClickAction()
            .performClick()
        composeRule.onNodeWithTag("character-equipment-detail")
            .assertIsDisplayed()
        composeRule.onNodeWithText("Future helmet").assertIsDisplayed()
    }

    @Test
    fun confirmedTravelTransitionRendersRouteAndFinishes() {
        composeRule.mainClock.autoAdvance = false
        var finishedToken: Long? = null

        composeRule.setContent {
            PixelTheme {
                MapTravelTransitionOverlay(
                    transition = TravelTransitionUiState(
                        token = 7L,
                        fromLocation = "DISTRICT_PLAZA",
                        toLocation = "DISTRICT_ARCHIVE",
                    ),
                    onFinished = { finishedToken = it },
                    modifier = Modifier.fillMaxSize(),
                )
            }
        }

        composeRule.onNodeWithTag("map-travel-transition")
            .assertIsDisplayed()
        composeRule.onAllNodesWithTag("map-travel-transition-canvas")
            .assertCountEquals(0)
        composeRule.onNodeWithText("DISTRICT PLAZA → DISTRICT ARCHIVE")
            .assertIsDisplayed()

        composeRule.mainClock.advanceTimeBy(900L)
        composeRule.waitForIdle()
        composeRule.runOnIdle {
            check(finishedToken == 7L) {
                "Expected travel transition token 7 to finish, got $finishedToken"
            }
        }
        composeRule.mainClock.autoAdvance = true
    }


}
