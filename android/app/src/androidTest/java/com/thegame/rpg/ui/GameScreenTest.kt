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
import com.thegame.rpg.engine.GameSnapshot
import com.thegame.rpg.engine.GameSkill
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
        composeRule.onNodeWithTag("stat-row-endurance")
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
        composeRule.onNodeWithTag("stat-contribution-equipment-body")
            .performScrollTo()
            .assertIsDisplayed()
        composeRule.onNodeWithText("EQUIPMENT // CHEST").assertIsDisplayed()
        composeRule.onNodeWithText("+2").assertIsDisplayed()
    }

    @Test
    fun moreMenuOpensDedicatedSkillsAndRequestsInspection() {
        var requestedPath: String? = null
        val skillsSnapshot = snapshot.copy(
            skills = listOf(
                GameSkill(
                    id = "athletics",
                    name = "Athletics",
                    category = "physical",
                    base = 20.0,
                    effective = 20.0,
                    delta = 0.0,
                    modified = false,
                ),
                GameSkill(
                    id = "technical_systems",
                    name = "Technical Systems",
                    category = "technical",
                    base = 25.0,
                    effective = 26.0,
                    delta = 1.0,
                    modified = true,
                ),
            )
        )

        composeRule.setContent {
            PixelTheme {
                TheGameRoot(
                    uiState = GameUiState(
                        bootState = BootState.Ready,
                        snapshot = skillsSnapshot,
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

        composeRule.onNodeWithTag("nav-more")
            .performScrollTo()
            .performClick()
        composeRule.onNodeWithText("SKILLS")
            .assertHasClickAction()
            .performClick()
        composeRule.onNodeWithText("2 ACTIVE SKILLS").assertIsDisplayed()
        composeRule.onNodeWithTag("skills-screen-row-technical_systems")
            .performScrollTo()
            .assertHasClickAction()
            .performClick()

        composeRule.runOnIdle {
            check(requestedPath == "skills.technical_systems") {
                "Expected Technical Systems inspection request, got $requestedPath"
            }
        }
    }

    @Test
    fun skillsScreenRendersAuthoritativeEquipmentContribution() {
        val skillsSnapshot = snapshot.copy(
            skills = listOf(
                GameSkill(
                    id = "technical_systems",
                    name = "Technical Systems",
                    category = "technical",
                    base = 25.0,
                    effective = 26.0,
                    delta = 1.0,
                    modified = true,
                ),
            )
        )
        val inspection = GameStatInspection(
            path = "skills.technical_systems",
            kind = "skill",
            total = 26.0,
            contributions = listOf(
                GameStatContribution("base", 25.0),
                GameStatContribution("equipment:hands", 1.0),
            ),
        )

        composeRule.setContent {
            PixelTheme {
                TheGameRoot(
                    uiState = GameUiState(
                        bootState = BootState.Ready,
                        snapshot = skillsSnapshot,
                        statInspectionPath = "skills.technical_systems",
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

        composeRule.onNodeWithTag("nav-more")
            .performScrollTo()
            .performClick()
        composeRule.onNodeWithText("SKILLS")
            .performClick()
        composeRule.onNodeWithTag("stat-contribution-equipment-hands")
            .performScrollTo()
            .assertIsDisplayed()
        composeRule.onNodeWithText("EQUIPMENT // HANDS").assertIsDisplayed()
        composeRule.onNodeWithText("+1").assertIsDisplayed()
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
            "DISTRICT_PLAZA" to "DISTRICT_HUB",
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
    fun unmappedEquippedItemDoesNotInventVisibleAvatarLayer() {
        val equippedSnapshot = snapshot.copy(
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
                GameScreen(
                    snapshot = equippedSnapshot,
                    busy = false,
                    onChoice = {},
                    onNavigate = {},
                )
            }
        }

        composeRule.onNodeWithTag("player-avatar").assertIsDisplayed()
        composeRule.onAllNodesWithTag("avatar-visible-gear").assertCountEquals(0)
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
        composeRule.onNodeWithTag("character-loadout-board")
            .assertIsDisplayed()
        composeRule.onNodeWithTag("character-slot-body")
            .assertHasClickAction()
            .performClick()
        composeRule.onNodeWithTag("character-equipment-detail")
            .performScrollTo()
            .assertIsDisplayed()
        composeRule.onNodeWithText("Depot utility jacket").assertIsDisplayed()
        composeRule.onNodeWithText("AVATAR LAYER // AUTHORED 32x48 // Z 20")
            .assertIsDisplayed()
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
            .performScrollTo()
            .assertIsDisplayed()
        composeRule.onNodeWithText("Future helmet").assertIsDisplayed()
        composeRule.onNodeWithText("AVATAR LAYER // NOT AUTHORED — LOGICAL EQUIPMENT ONLY")
            .assertIsDisplayed()
        composeRule.onAllNodesWithTag("avatar-visible-gear").assertCountEquals(0)
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


    @Test
    fun uncommonInventoryQualityRendersAsSeparateItemFrameOverlay() {
        composeRule.setContent {
            PixelTheme {
                PixelItemIcon(
                    itemId = "ITEM_SIGNAL_RING",
                    quality = "uncommon",
                    modifier = Modifier.size(48.dp),
                )
            }
        }

        composeRule.onNodeWithTag("item-icon-ITEM_SIGNAL_RING")
            .assertIsDisplayed()
        composeRule.onNodeWithTag("item-quality-frame-uncommon")
            .assertIsDisplayed()
    }

}
