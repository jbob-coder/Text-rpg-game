package com.thegame.rpg.engine

/**
 * Strict Android boundary for snapshots which contain the versioned player-safe room projection.
 *
 * BridgeSnapshotMapper remains responsible for field/type mapping. This boundary adds the
 * cross-field invariants which require the completed snapshot location and actor set.
 */
internal object PlayerSafeSnapshotMapper {
    fun fromMap(payload: Map<String, Any?>): GameSnapshot {
        val snapshot = BridgeSnapshotMapper.fromMap(payload)
        if (payload["room"] == null) return snapshot
        return snapshot.copy(
            room = RoomProjectionContract.validate(snapshot.location, snapshot.room),
        )
    }
}
