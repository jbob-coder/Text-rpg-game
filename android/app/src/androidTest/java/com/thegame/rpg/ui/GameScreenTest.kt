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
import com.thegame.rpg.TravelTransitionUiState
import com.thegame.rpg.engine.GameChoice
import com.thegame.rpg.engine.GameCondition
import com.thegame.rpg.engine.GameEquipmentSlot
import com.thegame.rpg.engine.GameInventory
import com.thegame.rpg.engine.GameResource
import com.thegame.rpg.engine.GameSnapshot
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
    fun gameplayShellShowsScrollableNarrativeChoicesAvatarAndNavigation() {
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
        composeRule.onNodeWithTag("player-avatar").assertIsDisplayed()

        snapshot.choices.forEach { choice ->
            composeRule.onNodeWithTag("choice-${choice.id}")
                .assertIsDisplayed()
                .assertHasClickAction()
        }

        listOf("Stats", "Inventory", "Quests", "Map", "More").forEach { label ->
            composeRule.onNodeWithText(label).assertIsDisplayed().assertHasClickAction()
        }
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
    fun currentCatalogIconsRenderAsRealComposeAssets() {
        val itemIds = listOf(
            "ITEM_DEPOT_JACKET",
            "ITEM_WORK_GLOVES",
            "ITEM_SIGNAL_RING",
            "ITEM_COURIER_NECKTAG",
            "ITEM_MAINTENANCE_SEAL",
            "ITEM_DEAD_RELAY",
        )

        composeRule.setContent {
            PixelTheme {
                Column {
                    itemIds.forEach { itemId ->
                        PixelItemIcon(
                            itemId = itemId,
                            modifier = Modifier.size(48.dp),
                        )
                    }
                }
            }
        }

        itemIds.forEach { itemId ->
            composeRule.onNodeWithTag("item-icon-$itemId")
                .assertIsDisplayed()
        }
    }

    @Test
    fun productionUiIconCatalogRendersThroughCompose() {
        composeRule.setContent {
            PixelTheme {
                Column {
                    PixelUiIconCatalog.productionIcons.forEach { icon ->
                        PixelUiIcon(
                            sprite = icon,
                            modifier = Modifier.size(24.dp),
                            testTag = "production-ui-icon",
                        )
                    }
                }
            }
        }

        composeRule.onAllNodesWithTag("production-ui-icon")
            .assertCountEquals(PixelUiIconCatalog.productionIcons.size)
    }

    @Test
    fun equipmentSlotIconSetRendersThroughCompose() {
        composeRule.setContent {
            PixelTheme {
                Column {
                    PixelEquipmentSlotCatalog.productionSlots.forEach { icon ->
                        PixelUiIcon(
                            sprite = icon,
                            modifier = Modifier.size(24.dp),
                            testTag = "production-equipment-slot-icon",
                        )
                    }
                }
            }
        }

        composeRule.onAllNodesWithTag("production-equipment-slot-icon")
            .assertCountEquals(PixelEquipmentSlotCatalog.productionSlots.size)
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

        composeRule.onNodeWithTag("scene-illustration")
            .assertIsDisplayed()
    }

    @Test
    fun allCurrentNamedSceneMastersRenderThroughCompose() {
        val locations = listOf(
            "PLATFORM_NINE",
            "RELAY_WORKBENCH",
            "GATE_TWELVE",
            "SERVICE_TUNNEL",
            "EVAC_STAIR",
            "TRACE_CHAMBER",
            "DISTRICT_PLAZA",
            "DISTRICT_ARCHIVE",
            "WORKSHOP_ROW",
        )

        composeRule.setContent {
            PixelTheme {
                Column {
                    locations.forEach { locationId ->
                        SceneIllustration(
                            locationId = locationId,
                            relayState = if (locationId == "RELAY_WORKBENCH") "intact" else null,
                            modifier = Modifier.size(96.dp, 48.dp),
                        )
                    }
                }
            }
        }

        composeRule.onAllNodesWithTag("scene-illustration")
            .assertCountEquals(locations.size)
    }

    @Test
    fun playerFacingSceneIdsRenderStateOverlaysThroughCompose() {
        val cases = listOf(
            "GATE_TWELVE" to "POWER_GATE_TWELVE_SIGNAL",
            "SERVICE_TUNNEL" to "TRACE_DIRECTIONAL_AFTERSHOCK",
            "TRACE_CHAMBER" to "POWER_FIRST_PRACTICE",
        )

        composeRule.setContent {
            PixelTheme {
                Column {
                    cases.forEach { (locationId, sceneId) ->
                        SceneIllustration(
                            locationId = locationId,
                            sceneId = sceneId,
                            modifier = Modifier.size(256.dp, 128.dp),
                        )
                    }
                }
            }
        }

        composeRule.onAllNodesWithTag("scene-illustration")
            .assertCountEquals(cases.size)
    }

    @Test
    fun equippedGearIsReflectedByTheVisibleAvatar() {
        val equippedSnapshot = snapshot.copy(
            inventory = GameInventory(
                equipment = listOf(
                    GameEquipmentSlot(
                        slot = "body",
                        equipped = true,
                        itemId = "ITEM_DEPOT_JACKET",
                        name = "Depot utility jacket",
                    ),
                    GameEquipmentSlot(
                        slot = "ring_1",
                        equipped = true,
                        itemId = "ITEM_SIGNAL_RING",
                        name = "Signal ring",
                    ),
                )
            )
        )

        composeRule.setContent {
            PixelTheme {
                GameScreen(
                    snapshot = equippedSnapshot,
                    busy = false,
                    onChoice = {},
                    onNavigate = {},
                )
            }
        }

        composeRule.onNodeWithTag("avatar-visible-gear").assertIsDisplayed()
        composeRule.onNodeWithText("VISIBLE GEAR // CHEST • RING I").assertIsDisplayed()
    }

    @Test
    fun projectedEchoStrainConditionActivatesVisibleAvatarFx() {
        val strainedSnapshot = snapshot.copy(
            conditions = listOf(
                GameCondition(
                    id = PixelTraceStrainCatalog.ECHO_STRAIN_CONDITION_ID,
                    name = "Echo Strain",
                    severity = 2,
                    durationMinutes = 35,
                    tags = listOf("power", "sensory", "strain"),
                )
            )
        )

        composeRule.setContent {
            PixelTheme {
                GameScreen(
                    snapshot = strainedSnapshot,
                    busy = false,
                    onChoice = {},
                    onNavigate = {},
                )
            }
        }

        composeRule.onNodeWithTag("player-avatar-canvas-trace-strain")
            .assertIsDisplayed()
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
        composeRule.onNodeWithTag("map-travel-transition-canvas")
            .assertIsDisplayed()
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
