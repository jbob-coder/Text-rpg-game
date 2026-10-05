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

data class GameStatusContribution(val kind: String, val label: String, val value: Double, val slot: String? = null)
data class GameAttribute(val id: String, val name: String, val base: Double, val effective: Double, val delta: Double, val modified: Boolean, val role: String? = null, val contributions: List<GameStatusContribution> = emptyList())
data class GameDerivedStat(val id: String, val name: String, val value: Double, val role: String? = null)
data class GameSkill(val id: String, val name: String, val category: String, val base: Double, val effective: Double, val delta: Double, val modified: Boolean, val contributions: List<GameStatusContribution> = emptyList())
data class GameStatContribution(val source: String, val value: Double)
data class GameStatInspection(val path: String, val kind: String, val total: Double, val contributions: List<GameStatContribution>)
data class GameCondition(val id: String, val name: String, val severity: Int, val durationMinutes: Int?, val tags: List<String>)
data class GameIdentity(val name: String? = null, val origin: String? = null, val background: String? = null, val path: String? = null, val level: Int? = null)
data class GameInventoryItem(val id: String, val name: String, val quantity: Int, val equippable: Boolean = false, val slot: String? = null, val quality: String? = null)
data class GameEquipmentSlot(val slot: String, val equipped: Boolean, val itemId: String? = null, val name: String? = null, val quality: String? = null)
data class GameInventory(val items: List<GameInventoryItem> = emptyList(), val equipment: List<GameEquipmentSlot> = emptyList())
data class GameVisuals(val relayState: String? = null)
data class GameQuestObjective(val id: String, val title: String, val required: Boolean, val status: String)
data class GameQuest(val id: String, val title: String, val description: String, val category: String, val status: String, val stage: String, val objectives: List<GameQuestObjective>)
data class GameMapNode(val id: String, val title: String, val description: String, val x: Double, val y: Double, val current: Boolean, val reachable: Boolean = false)
data class GameMapEdge(val from: String, val to: String)
data class GameWorldMap(val title: String = "World", val currentLocation: String = "", val nodes: List<GameMapNode> = emptyList(), val edges: List<GameMapEdge> = emptyList())

data class GameAbilityResource(
    val label: String,
    val current: Double,
    val max: Double? = null,
    val recoveryPerHour: Double? = null,
)

data class GameTechnique(
    val id: String,
    val name: String,
    val stage: String,
    val masteryXp: Double,
    val uses: Int,
    val ready: Boolean,
    val cooldownRemainingMinutes: Int,
)

data class GameAbility(
    val id: String,
    val name: String,
    val rank: Int,
    val masteryStage: String,
    val masteryXp: Double,
    val form: String? = null,
    val state: String,
    val resource: GameAbilityResource? = null,
    val techniques: List<GameTechnique> = emptyList(),
    val completedEvolutionIds: List<String> = emptyList(),
)

data class GameRoomActor(
    val presentationId: String,
    val knownActorId: String?,
    val displayName: String,
    val visualFamily: String,
    val placementKey: String,
    val poseKey: String?,
    val outfitKey: String?,
    val visibleTags: List<String>,
    val inspectable: Boolean,
    val dialogueAvailable: Boolean,
    val actions: List<String>,
)

data class GameRoomProjection(
    val projectionVersion: Int = 1,
    val locationId: String = "",
    val actors: List<GameRoomActor> = emptyList(),
    val activeSpeakerPresentationId: String? = null,
)

data class GameSnapshot(
    val sceneId: String, val title: String, val body: String, val choices: List<GameChoice>,
    val resources: List<GameResource>, val attributes: List<GameAttribute> = emptyList(),
    val derived: List<GameDerivedStat> = emptyList(), val skills: List<GameSkill> = emptyList(),
    val conditions: List<GameCondition> = emptyList(), val identity: GameIdentity = GameIdentity(),
    val inventory: GameInventory = GameInventory(), val quests: List<GameQuest> = emptyList(),
    val worldMap: GameWorldMap = GameWorldMap(), val room: GameRoomProjection = GameRoomProjection(),
    val visuals: GameVisuals = GameVisuals(), val turn: Int, val timeMinutes: Int, val location: String,
    val contentId: String? = null, val canonStatus: String? = null,
    val abilities: List<GameAbility> = emptyList(),
)

class EngineStartException(val stageId: String, val publicMessage: String, val technicalDetail: String, cause: Throwable? = null) : RuntimeException(publicMessage, cause) {
    fun toBootStateError(): BootState.Error = BootState.Error(stageId = stageId, publicMessage = publicMessage, technicalDetail = technicalDetail)
}
internal class GatewayFailure(val stageId: String, val publicMessage: String, val technicalDetail: String, cause: Throwable? = null) : RuntimeException(publicMessage, cause)

interface GameEngine {
    suspend fun start(context: Context, onStage: (BootState) -> Unit = {}): Result<GameSnapshot>
    suspend fun choose(choiceId: String): Result<GameSnapshot>
    suspend fun save(): Result<Unit>
    suspend fun load(): Result<GameSnapshot>
    suspend fun applyCheat(code: String): Result<GameSnapshot>
    suspend fun equip(itemId: String): Result<GameSnapshot> = Result.failure(UnsupportedOperationException("equip is not implemented"))
    suspend fun unequip(slot: String): Result<GameSnapshot> = Result.failure(UnsupportedOperationException("unequip is not implemented"))
    suspend fun travel(locationId: String): Result<GameSnapshot> = Result.failure(UnsupportedOperationException("travel is not implemented"))
    suspend fun inspectStatus(path: String): Result<GameStatInspection> = Result.failure(UnsupportedOperationException("stat inspection is not implemented"))
}

internal object BridgeSnapshotMapper {
    fun statInspectionFromMap(payload: Map<String, Any?>): GameStatInspection {
        val path = text(payload["path"], "inspection.path")
        val kind = text(payload["kind"], "inspection.kind")
        val total = number(payload["total"], "inspection.total")
        val breakdown = objectMap(payload["breakdown"], "inspection.breakdown")
        return GameStatInspection(path, kind, total, breakdown.map { (source, rawValue) -> GameStatContribution(source, number(rawValue, "inspection.breakdown.$source")) })
    }

    fun fromMap(payload: Map<String, Any?>): GameSnapshot {
        val scene = objectMap(payload["scene"], "scene")
        val status = objectMap(payload["status"], "status")
        val meta = objectMap(payload["meta"], "meta")
        val sceneId = text(scene["id"], "scene.id")
        val choices = list(scene["choices"], "scene.choices").mapIndexed { index, item ->
            val choice = objectMap(item, "scene.choices[$index]")
            GameChoice(text(choice["id"], "scene.choices[$index].id"), text(choice["text"], "scene.choices[$index].text"), boolean(choice["enabled"], "scene.choices[$index].enabled"), optionalText(choice["disabled_reason"]))
        }
        val resources = list(status["resources"], "status.resources").mapIndexed { index, item ->
            val r = objectMap(item, "status.resources[$index]"); GameResource(text(r["id"], "status.resources[$index].id"), number(r["current"], "status.resources[$index].current"), number(r["max"], "status.resources[$index].max"))
        }
        val attributes = optionalList(status["attributes"], "status.attributes").mapIndexed { index, item ->
            val a = objectMap(item, "status.attributes[$index]"); GameAttribute(text(a["id"], "status.attributes[$index].id"), text(a["name"], "status.attributes[$index].name"), number(a["base"], "status.attributes[$index].base"), number(a["effective"], "status.attributes[$index].effective"), number(a["delta"], "status.attributes[$index].delta"), boolean(a["modified"], "status.attributes[$index].modified"), optionalText(a["role"]), contributions(a["contributions"], "status.attributes[$index].contributions"))
        }
        val derived = optionalList(status["derived"], "status.derived").mapIndexed { index, item -> val s=objectMap(item,"status.derived[$index]"); GameDerivedStat(text(s["id"],"status.derived[$index].id"),text(s["name"],"status.derived[$index].name"),number(s["value"],"status.derived[$index].value"),optionalText(s["role"])) }
        val skills = buildList { optionalObjectMap(status["skills"], "status.skills").forEach { (category, raw) -> optionalList(raw,"status.skills.$category").forEachIndexed { index,item -> val s=objectMap(item,"status.skills.$category[$index]"); add(GameSkill(text(s["id"],"status.skills.$category[$index].id"),text(s["name"],"status.skills.$category[$index].name"),category,number(s["base"],"status.skills.$category[$index].base"),number(s["effective"],"status.skills.$category[$index].effective"),number(s["delta"],"status.skills.$category[$index].delta"),boolean(s["modified"],"status.skills.$category[$index].modified"),contributions(s["contributions"],"status.skills.$category[$index].contributions"))) } } }
        val abilities = optionalList(status["abilities"], "status.abilities").mapIndexed { abilityIndex, item ->
            val path = "status.abilities[$abilityIndex]"
            val ability = objectMap(item, path)
            require("requirements" !in ability && "discovery_requirements" !in ability && "effects" !in ability) {
                "$path contains forbidden authored progression internals"
            }
            val masteryXp = nonNegativeNumber(ability["mastery_xp"], "$path.mastery_xp")
            val resource = ability["resource"]?.let { rawResource ->
                val resourcePath = "$path.resource"
                val value = objectMap(rawResource, resourcePath)
                val current = nonNegativeNumber(value["current"], "$resourcePath.current")
                val max = optionalNumber(value["max"], "$resourcePath.max")?.also {
                    require(it > 0.0) { "$resourcePath.max must be positive" }
                    require(current <= it) { "$resourcePath.current cannot exceed max" }
                }
                val recovery = optionalNumber(value["recovery_per_hour"], "$resourcePath.recovery_per_hour")?.also {
                    require(it >= 0.0) { "$resourcePath.recovery_per_hour must be non-negative" }
                }
                GameAbilityResource(
                    label = text(value["label"], "$resourcePath.label"),
                    current = current,
                    max = max,
                    recoveryPerHour = recovery,
                )
            }
            val techniques = optionalList(ability["techniques"], "$path.techniques").mapIndexed { techniqueIndex, rawTechnique ->
                val techniquePath = "$path.techniques[$techniqueIndex]"
                val technique = objectMap(rawTechnique, techniquePath)
                require("requirements" !in technique && "discovery_requirements" !in technique && "effects" !in technique) {
                    "$techniquePath contains forbidden authored progression internals"
                }
                GameTechnique(
                    id = stableId(technique["technique_id"], "$techniquePath.technique_id"),
                    name = text(technique["name"], "$techniquePath.name"),
                    stage = text(technique["stage"], "$techniquePath.stage"),
                    masteryXp = nonNegativeNumber(technique["mastery_xp"], "$techniquePath.mastery_xp"),
                    uses = integer(technique["uses"], "$techniquePath.uses"),
                    ready = boolean(technique["ready"], "$techniquePath.ready"),
                    cooldownRemainingMinutes = integer(
                        technique["cooldown_remaining_minutes"],
                        "$techniquePath.cooldown_remaining_minutes",
                    ),
                )
            }
            GameAbility(
                id = stableId(ability["id"], "$path.id"),
                name = text(ability["name"], "$path.name"),
                rank = integer(ability["rank"], "$path.rank"),
                masteryStage = text(ability["mastery_stage"], "$path.mastery_stage"),
                masteryXp = masteryXp,
                form = optionalText(ability["form"]),
                state = text(ability["state"], "$path.state"),
                resource = resource,
                techniques = techniques,
                completedEvolutionIds = stableIdList(
                    ability["completed_evolutions"],
                    "$path.completed_evolutions",
                ),
            )
        }
        val conditions = optionalList(status["conditions"],"status.conditions").mapIndexed { index,item -> val c=objectMap(item,"status.conditions[$index]"); GameCondition(text(c["id"],"status.conditions[$index].id"),text(c["name"],"status.conditions[$index].name"),integer(c["severity"],"status.conditions[$index].severity"),optionalInteger(c["duration_minutes"],"status.conditions[$index].duration_minutes"),textList(c["tags"],"status.conditions[$index].tags")) }
        val im=optionalObjectMap(status["identity"],"status.identity"); val identity=GameIdentity(optionalText(im["name"]),optionalText(im["origin"]),optionalText(im["background"]),optionalText(im["path"]),optionalInteger(im["level"],"status.identity.level"))
        val ip=optionalObjectMap(payload["inventory"],"inventory")
        val inventoryItems = optionalList(ip["items"], "inventory.items").mapIndexed { i, item ->
            val v = objectMap(item, "inventory.items[$i]")
            val quantity = integer(v["quantity"], "inventory.items[$i].quantity")
            if (quantity <= 0) throw IllegalArgumentException("inventory.items[$i].quantity must be positive")
            val equippable = optionalBoolean(v["equippable"]) ?: false
            val slot = optionalText(v["slot"])
            if (equippable && slot == null) {
                throw IllegalArgumentException("inventory.items[$i].slot is required when equippable")
            }
            GameInventoryItem(
                text(v["id"], "inventory.items[$i].id"),
                text(v["name"], "inventory.items[$i].name"),
                quantity,
                equippable,
                slot,
                optionalText(v["quality"]),
            )
        }
        val equipmentSlots = optionalList(ip["equipment"], "inventory.equipment").mapIndexed { i, item ->
            val v = objectMap(item, "inventory.equipment[$i]")
            val equipped = boolean(v["equipped"], "inventory.equipment[$i].equipped")
            val itemId = optionalText(v["item_id"])
            val name = optionalText(v["name"])
            if (equipped && itemId == null) {
                throw IllegalArgumentException("inventory.equipment[$i].item_id is required when equipped")
            }
            if (!equipped && (itemId != null || name != null)) {
                throw IllegalArgumentException("inventory.equipment[$i] cannot expose item identity when unequipped")
            }
            GameEquipmentSlot(
                text(v["slot"], "inventory.equipment[$i].slot"),
                equipped,
                itemId,
                name,
                optionalText(v["quality"]),
            )
        }
        val inventory = GameInventory(inventoryItems, equipmentSlots)
        val quests=optionalList(payload["quests"],"quests").mapIndexed { qi,item -> val q=objectMap(item,"quests[$qi]"); val objectives=optionalList(q["objectives"],"quests[$qi].objectives").mapIndexed { oi,oitem -> val o=objectMap(oitem,"quests[$qi].objectives[$oi]"); GameQuestObjective(text(o["id"],"quests[$qi].objectives[$oi].id"),text(o["title"],"quests[$qi].objectives[$oi].title"),boolean(o["required"],"quests[$qi].objectives[$oi].required"),text(o["status"],"quests[$qi].objectives[$oi].status")) }; GameQuest(text(q["id"],"quests[$qi].id"),text(q["title"],"quests[$qi].title"),optionalText(q["description"])?:"",text(q["category"],"quests[$qi].category"),text(q["status"],"quests[$qi].status"),optionalText(q["stage"])?:"",objectives) }
        val mp=optionalObjectMap(payload["map"],"map"); val nodes=optionalList(mp["nodes"],"map.nodes").mapIndexed { i,item -> val n=objectMap(item,"map.nodes[$i]"); GameMapNode(text(n["id"],"map.nodes[$i].id"),text(n["title"],"map.nodes[$i].title"),optionalText(n["description"])?:"",number(n["x"],"map.nodes[$i].x"),number(n["y"],"map.nodes[$i].y"),boolean(n["current"],"map.nodes[$i].current"),optionalBoolean(n["reachable"])?:false) }; val edges=optionalList(mp["edges"],"map.edges").mapIndexed { i,item -> val e=objectMap(item,"map.edges[$i]"); GameMapEdge(text(e["from"],"map.edges[$i].from"),text(e["to"],"map.edges[$i].to")) }; val worldMap=GameWorldMap(optionalText(mp["title"])?:"World",optionalText(mp["current_location"])?:"",nodes,edges)

        val roomPayload = optionalObjectMap(payload["room"], "room")
        val room = if (roomPayload.isEmpty()) GameRoomProjection() else {
            val version = integer(roomPayload["projection_version"], "room.projection_version")
            require(version == 1) { "room.projection_version is unsupported" }
            val actors = list(roomPayload["actors"], "room.actors").mapIndexed { index, item ->
                val actor = objectMap(item, "room.actors[$index]")
                GameRoomActor(
                    presentationId = text(actor["presentation_id"], "room.actors[$index].presentation_id"),
                    knownActorId = optionalText(actor["known_actor_id"]),
                    displayName = text(actor["display_name"], "room.actors[$index].display_name"),
                    visualFamily = text(actor["visual_family"], "room.actors[$index].visual_family"),
                    placementKey = text(actor["placement_key"], "room.actors[$index].placement_key"),
                    poseKey = optionalText(actor["pose_key"]),
                    outfitKey = optionalText(actor["outfit_key"]),
                    visibleTags = textList(actor["visible_tags"], "room.actors[$index].visible_tags"),
                    inspectable = boolean(actor["inspectable"], "room.actors[$index].inspectable"),
                    dialogueAvailable = boolean(actor["dialogue_available"], "room.actors[$index].dialogue_available"),
                    actions = textList(actor["actions"], "room.actors[$index].actions"),
                )
            }
            GameRoomProjection(version, text(roomPayload["location_id"], "room.location_id"), actors, optionalText(roomPayload["active_speaker_presentation_id"]))
        }
        val vp=optionalObjectMap(payload["visuals"],"visuals"); val relay=optionalText(vp["relay_state"]); require(relay==null || relay in setOf("intact","opened","damaged","signal_lost")) { "visuals.relay_state is not a supported player-facing state" }; val visuals=GameVisuals(relay)
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
            room = room,
            visuals = visuals,
            turn = integer(meta["turn"], "meta.turn"),
            timeMinutes = integer(meta["time_minutes"], "meta.time_minutes"),
            location = optionalText(meta["location"]) ?: sceneId,
            contentId = optionalText(meta["content_id"]),
            canonStatus = optionalText(meta["canon_status"]),
            abilities = abilities,
        )
    }

    private fun objectMap(value: Any?, label: String): Map<String, Any?> { if(value !is Map<*,*>) throw IllegalArgumentException("$label must be an object"); val out=LinkedHashMap<String,Any?>(); value.forEach { (k,v)-> if(k !is String) throw IllegalArgumentException("$label keys must be text"); out[k]=v }; return out }
    private fun optionalObjectMap(value: Any?, label: String)=if(value==null) emptyMap() else objectMap(value,label)
    private fun list(value: Any?, label: String): List<*> { if(value !is List<*>) throw IllegalArgumentException("$label must be a list"); return value }
    private fun optionalList(value: Any?, label: String)=if(value==null) emptyList<Any?>() else list(value,label)
    private fun text(value: Any?, label: String): String { if(value !is String || value.isBlank()) throw IllegalArgumentException("$label must be non-empty text"); return value }
    private fun textList(value: Any?, label: String): List<String> = optionalList(value,label).mapIndexed { i,item -> text(item,"$label[$i]") }
    private val stableIdPattern = Regex("^[A-Z][A-Z0-9_]*$")
    private fun stableId(value: Any?, label: String): String = text(value, label).also {
        require(stableIdPattern.matches(it)) { "$label must be a stable uppercase ID" }
    }
    private fun stableIdList(value: Any?, label: String): List<String> = optionalList(value, label).mapIndexed { index, item ->
        stableId(item, "$label[$index]")
    }
    private fun contributions(value: Any?, path: String)=optionalList(value,path).mapIndexed { i,item -> val r=objectMap(item,"$path[$i]"); val kind=text(r["kind"],"$path[$i].kind"); require(kind in setOf("equipment","set","perk","condition","unidentified")); val slot=optionalText(r["slot"]); require((kind=="equipment"&&slot!=null)||(kind!="equipment"&&slot==null)); GameStatusContribution(kind,text(r["label"],"$path[$i].label"),number(r["value"],"$path[$i].value"),slot) }
    private fun optionalText(value: Any?): String?=when(value){null->null;is String->value.takeIf{it.isNotBlank()};else->throw IllegalArgumentException("optional text field has invalid type")}
    private fun boolean(value: Any?, label:String):Boolean { if(value !is Boolean) throw IllegalArgumentException("$label must be boolean"); return value }
    private fun number(value:Any?,label:String):Double { if(value !is Number) throw IllegalArgumentException("$label must be numeric"); val o=value.toDouble(); if(!o.isFinite()) throw IllegalArgumentException("$label must be finite"); return o }
    private fun nonNegativeNumber(value: Any?, label: String): Double = number(value, label).also {
        require(it >= 0.0) { "$label must be non-negative" }
    }
    private fun optionalNumber(value: Any?, label: String): Double? = if (value == null) null else number(value, label)
    private fun integer(value:Any?,label:String):Int { if(value !is Number) throw IllegalArgumentException("$label must be numeric"); val l=value.toLong(); if(l<0||l>Int.MAX_VALUE||value.toDouble()!=l.toDouble()) throw IllegalArgumentException("$label must be a non-negative integer"); return l.toInt() }
    private fun optionalInteger(value:Any?,label:String)=if(value==null)null else integer(value,label)
    private fun optionalBoolean(value:Any?):Boolean?=when(value){null->null;is Boolean->value;else->throw IllegalArgumentException("optional boolean field has invalid type")}
}
