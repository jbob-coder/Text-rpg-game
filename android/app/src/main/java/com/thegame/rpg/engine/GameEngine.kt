package com.thegame.rpg.engine

import android.content.Context
import com.thegame.rpg.boot.BootState

data class GameChoice(
    val id: String,
    val text: String,
    val enabled: Boolean,
    val disabledReason: String? = null,
)

data class GameResource(val id: String, val current: Double, val max: Double)

data class GameAttribute(
    val id: String,
    val name: String,
    val base: Double,
    val effective: Double,
    val delta: Double,
    val modified: Boolean,
    val role: String? = null,
)

data class GameDerivedStat(
    val id: String,
    val name: String,
    val value: Double,
    val role: String? = null,
)

data class GameSkill(
    val id: String,
    val name: String,
    val category: String,
    val base: Double,
    val effective: Double,
    val delta: Double,
    val modified: Boolean,
)

data class GameCondition(
    val id: String,
    val name: String,
    val severity: Int,
    val durationMinutes: Int?,
    val tags: List<String>,
)

data class GameIdentity(
    val name: String? = null,
    val origin: String? = null,
    val background: String? = null,
    val path: String? = null,
    val level: Int? = null,
)

data class GameInventoryItem(
    val id: String,
    val name: String,
    val quantity: Int,
    val equippable: Boolean = false,
    val slot: String? = null,
)

data class GameEquipmentSlot(
    val slot: String,
    val equipped: Boolean,
    val itemId: String? = null,
    val name: String? = null,
    val quality: String? = null,
)

data class GameInventory(
    val items: List<GameInventoryItem> = emptyList(),
    val equipment: List<GameEquipmentSlot> = emptyList(),
)

data class GameQuestObjective(
    val id: String,
    val title: String,
    val required: Boolean,
    val status: String,
)

data class GameQuest(
    val id: String,
    val title: String,
    val description: String,
    val category: String,
    val status: String,
    val stage: String,
    val objectives: List<GameQuestObjective>,
)

data class GameMapNode(
    val id: String,
    val title: String,
    val description: String,
    val x: Double,
    val y: Double,
    val current: Boolean,
    val reachable: Boolean = false,
)

data class GameMapEdge(val from: String, val to: String)

data class GameWorldMap(
    val title: String = "World",
    val currentLocation: String = "",
    val nodes: List<GameMapNode> = emptyList(),
    val edges: List<GameMapEdge> = emptyList(),
)

data class GameSnapshot(
    val sceneId: String,
    val title: String,
    val body: String,
    val choices: List<GameChoice>,
    val resources: List<GameResource>,
    val attributes: List<GameAttribute> = emptyList(),
    val derived: List<GameDerivedStat> = emptyList(),
    val skills: List<GameSkill> = emptyList(),
    val conditions: List<GameCondition> = emptyList(),
    val identity: GameIdentity = GameIdentity(),
    val inventory: GameInventory = GameInventory(),
    val quests: List<GameQuest> = emptyList(),
    val worldMap: GameWorldMap = GameWorldMap(),
    val turn: Int,
    val timeMinutes: Int,
    val location: String,
    val contentId: String? = null,
    val canonStatus: String? = null,
)

class EngineStartException(
    val stageId: String,
    val publicMessage: String,
    val technicalDetail: String,
    cause: Throwable? = null,
) : RuntimeException(publicMessage, cause) {
    fun toBootStateError(): BootState.Error = BootState.Error(
        stageId = stageId,
        publicMessage = publicMessage,
        technicalDetail = technicalDetail,
    )
}

internal class GatewayFailure(
    val stageId: String,
    val publicMessage: String,
    val technicalDetail: String,
    cause: Throwable? = null,
) : RuntimeException(publicMessage, cause)

interface GameEngine {
    suspend fun start(
        context: Context,
        onStage: (BootState) -> Unit = {},
    ): Result<GameSnapshot>

    suspend fun choose(choiceId: String): Result<GameSnapshot>
    suspend fun save(): Result<Unit>
    suspend fun load(): Result<GameSnapshot>
    suspend fun applyCheat(code: String): Result<GameSnapshot>
    suspend fun equip(itemId: String): Result<GameSnapshot> =
        Result.failure(UnsupportedOperationException("equip is not implemented"))
    suspend fun unequip(slot: String): Result<GameSnapshot> =
        Result.failure(UnsupportedOperationException("unequip is not implemented"))
    suspend fun travel(locationId: String): Result<GameSnapshot> =
        Result.failure(UnsupportedOperationException("travel is not implemented"))
}

internal object BridgeSnapshotMapper {
    fun fromMap(payload: Map<String, Any?>): GameSnapshot {
        val scene = objectMap(payload["scene"], "scene")
        val status = objectMap(payload["status"], "status")
        val meta = objectMap(payload["meta"], "meta")

        val sceneId = text(scene["id"], "scene.id")
        val choices = list(scene["choices"], "scene.choices").mapIndexed { index, item ->
            val choice = objectMap(item, "scene.choices[$index]")
            GameChoice(
                id = text(choice["id"], "scene.choices[$index].id"),
                text = text(choice["text"], "scene.choices[$index].text"),
                enabled = boolean(choice["enabled"], "scene.choices[$index].enabled"),
                disabledReason = optionalText(choice["disabled_reason"]),
            )
        }

        val resources = list(status["resources"], "status.resources").mapIndexed { index, item ->
            val resource = objectMap(item, "status.resources[$index]")
            GameResource(
                id = text(resource["id"], "status.resources[$index].id"),
                current = number(resource["current"], "status.resources[$index].current"),
                max = number(resource["max"], "status.resources[$index].max"),
            )
        }

        val attributes = optionalList(status["attributes"], "status.attributes").mapIndexed { index, item ->
            val attribute = objectMap(item, "status.attributes[$index]")
            GameAttribute(
                id = text(attribute["id"], "status.attributes[$index].id"),
                name = text(attribute["name"], "status.attributes[$index].name"),
                base = number(attribute["base"], "status.attributes[$index].base"),
                effective = number(attribute["effective"], "status.attributes[$index].effective"),
                delta = number(attribute["delta"], "status.attributes[$index].delta"),
                modified = boolean(attribute["modified"], "status.attributes[$index].modified"),
                role = optionalText(attribute["role"]),
            )
        }

        val derived = optionalList(status["derived"], "status.derived").mapIndexed { index, item ->
            val stat = objectMap(item, "status.derived[$index]")
            GameDerivedStat(
                id = text(stat["id"], "status.derived[$index].id"),
                name = text(stat["name"], "status.derived[$index].name"),
                value = number(stat["value"], "status.derived[$index].value"),
                role = optionalText(stat["role"]),
            )
        }

        val skillGroups = optionalObjectMap(status["skills"], "status.skills")
        val skills = buildList {
            skillGroups.forEach { (category, rawSkills) ->
                optionalList(rawSkills, "status.skills.$category").forEachIndexed { index, item ->
                    val skill = objectMap(item, "status.skills.$category[$index]")
                    add(
                        GameSkill(
                            id = text(skill["id"], "status.skills.$category[$index].id"),
                            name = text(skill["name"], "status.skills.$category[$index].name"),
                            category = category,
                            base = number(skill["base"], "status.skills.$category[$index].base"),
                            effective = number(skill["effective"], "status.skills.$category[$index].effective"),
                            delta = number(skill["delta"], "status.skills.$category[$index].delta"),
                            modified = boolean(skill["modified"], "status.skills.$category[$index].modified"),
                        )
                    )
                }
            }
        }

        val conditions = optionalList(status["conditions"], "status.conditions").mapIndexed { index, item ->
            val condition = objectMap(item, "status.conditions[$index]")
            GameCondition(
                id = text(condition["id"], "status.conditions[$index].id"),
                name = text(condition["name"], "status.conditions[$index].name"),
                severity = integer(condition["severity"], "status.conditions[$index].severity"),
                durationMinutes = optionalInteger(condition["duration_minutes"], "status.conditions[$index].duration_minutes"),
                tags = optionalList(condition["tags"], "status.conditions[$index].tags").mapIndexed { tagIndex, tag ->
                    text(tag, "status.conditions[$index].tags[$tagIndex]")
                },
            )
        }

        val identityMap = optionalObjectMap(status["identity"], "status.identity")
        val identity = GameIdentity(
            name = optionalText(identityMap["name"]),
            origin = optionalText(identityMap["origin"]),
            background = optionalText(identityMap["background"]),
            path = optionalText(identityMap["path"]),
            level = optionalInteger(identityMap["level"], "status.identity.level"),
        )

        val inventoryPayload = optionalObjectMap(payload["inventory"], "inventory")
        val inventoryItems = optionalList(inventoryPayload["items"], "inventory.items").mapIndexed { index, item ->
            val value = objectMap(item, "inventory.items[$index]")
            GameInventoryItem(
                id = text(value["id"], "inventory.items[$index].id"),
                name = text(value["name"], "inventory.items[$index].name"),
                quantity = integer(value["quantity"], "inventory.items[$index].quantity"),
                equippable = optionalBoolean(value["equippable"]) ?: false,
                slot = optionalText(value["slot"]),
            )
        }
        val equipmentSlots = optionalList(
            inventoryPayload["equipment"],
            "inventory.equipment",
        ).mapIndexed { index, item ->
            val value = objectMap(item, "inventory.equipment[$index]")
            GameEquipmentSlot(
                slot = text(value["slot"], "inventory.equipment[$index].slot"),
                equipped = boolean(value["equipped"], "inventory.equipment[$index].equipped"),
                itemId = optionalText(value["item_id"]),
                name = optionalText(value["name"]),
                quality = optionalText(value["quality"]),
            )
        }
        val inventory = GameInventory(
            items = inventoryItems,
            equipment = equipmentSlots,
        )

        val quests = optionalList(payload["quests"], "quests").mapIndexed { questIndex, item ->
            val quest = objectMap(item, "quests[$questIndex]")
            val objectives = optionalList(
                quest["objectives"],
                "quests[$questIndex].objectives",
            ).mapIndexed { objectiveIndex, objectiveItem ->
                val objective = objectMap(
                    objectiveItem,
                    "quests[$questIndex].objectives[$objectiveIndex]",
                )
                GameQuestObjective(
                    id = text(objective["id"], "quests[$questIndex].objectives[$objectiveIndex].id"),
                    title = text(objective["title"], "quests[$questIndex].objectives[$objectiveIndex].title"),
                    required = boolean(
                        objective["required"],
                        "quests[$questIndex].objectives[$objectiveIndex].required",
                    ),
                    status = text(objective["status"], "quests[$questIndex].objectives[$objectiveIndex].status"),
                )
            }
            GameQuest(
                id = text(quest["id"], "quests[$questIndex].id"),
                title = text(quest["title"], "quests[$questIndex].title"),
                description = optionalText(quest["description"]) ?: "",
                category = text(quest["category"], "quests[$questIndex].category"),
                status = text(quest["status"], "quests[$questIndex].status"),
                stage = optionalText(quest["stage"]) ?: "",
                objectives = objectives,
            )
        }

        val mapPayload = optionalObjectMap(payload["map"], "map")
        val mapNodes = optionalList(mapPayload["nodes"], "map.nodes").mapIndexed { nodeIndex, item ->
            val node = objectMap(item, "map.nodes[$nodeIndex]")
            GameMapNode(
                id = text(node["id"], "map.nodes[$nodeIndex].id"),
                title = text(node["title"], "map.nodes[$nodeIndex].title"),
                description = optionalText(node["description"]) ?: "",
                x = number(node["x"], "map.nodes[$nodeIndex].x"),
                y = number(node["y"], "map.nodes[$nodeIndex].y"),
                current = boolean(node["current"], "map.nodes[$nodeIndex].current"),
                reachable = optionalBoolean(node["reachable"]) ?: false,
            )
        }
        val mapEdges = optionalList(mapPayload["edges"], "map.edges").mapIndexed { edgeIndex, item ->
            val edge = objectMap(item, "map.edges[$edgeIndex]")
            GameMapEdge(
                from = text(edge["from"], "map.edges[$edgeIndex].from"),
                to = text(edge["to"], "map.edges[$edgeIndex].to"),
            )
        }
        val worldMap = GameWorldMap(
            title = optionalText(mapPayload["title"]) ?: "World",
            currentLocation = optionalText(mapPayload["current_location"]) ?: "",
            nodes = mapNodes,
            edges = mapEdges,
        )

        return GameSnapshot(
            sceneId = sceneId,
            title = text(scene["title"], "scene.title"),
            body = text(scene["body"], "scene.body"),
            choices = choices,
            resources = resources,
            attributes = attributes,
            derived = derived,
            skills = skills,
            conditions = conditions,
            identity = identity,
            inventory = inventory,
            quests = quests,
            worldMap = worldMap,
            turn = integer(meta["turn"], "meta.turn"),
            timeMinutes = integer(meta["time_minutes"], "meta.time_minutes"),
            location = optionalText(meta["location"]) ?: sceneId,
            contentId = optionalText(meta["content_id"]),
            canonStatus = optionalText(meta["canon_status"]),
        )
    }

    private fun objectMap(value: Any?, label: String): Map<String, Any?> {
        if (value !is Map<*, *>) throw IllegalArgumentException("$label must be an object")
        val output = LinkedHashMap<String, Any?>()
        value.forEach { (key, item) ->
            if (key !is String) throw IllegalArgumentException("$label keys must be text")
            output[key] = item
        }
        return output
    }

    private fun optionalObjectMap(value: Any?, label: String): Map<String, Any?> =
        if (value == null) emptyMap() else objectMap(value, label)

    private fun list(value: Any?, label: String): List<*> {
        if (value !is List<*>) throw IllegalArgumentException("$label must be a list")
        return value
    }

    private fun optionalList(value: Any?, label: String): List<*> =
        if (value == null) emptyList<Any?>() else list(value, label)

    private fun text(value: Any?, label: String): String {
        if (value !is String || value.isBlank()) {
            throw IllegalArgumentException("$label must be non-empty text")
        }
        return value
    }

    private fun optionalText(value: Any?): String? = when (value) {
        null -> null
        is String -> value.takeIf { it.isNotBlank() }
        else -> throw IllegalArgumentException("optional text field has invalid type")
    }

    private fun boolean(value: Any?, label: String): Boolean {
        if (value !is Boolean) throw IllegalArgumentException("$label must be boolean")
        return value
    }

    private fun number(value: Any?, label: String): Double {
        if (value !is Number) throw IllegalArgumentException("$label must be numeric")
        val output = value.toDouble()
        if (!output.isFinite()) throw IllegalArgumentException("$label must be finite")
        return output
    }

    private fun integer(value: Any?, label: String): Int {
        if (value !is Number) throw IllegalArgumentException("$label must be numeric")
        val asLong = value.toLong()
        if (asLong < 0 || asLong > Int.MAX_VALUE || value.toDouble() != asLong.toDouble()) {
            throw IllegalArgumentException("$label must be a non-negative integer")
        }
        return asLong.toInt()
    }

    private fun optionalInteger(value: Any?, label: String): Int? =
        if (value == null) null else integer(value, label)

    private fun optionalBoolean(value: Any?): Boolean? = when (value) {
        null -> null
        is Boolean -> value
        else -> throw IllegalArgumentException("optional boolean field has invalid type")
    }
}
