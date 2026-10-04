# THE GAME — Time, Causal State & Snapshot Standard

Status: **PROVISIONAL CROSS-TIER DESIGN STANDARD / NOT CANON / NOT IMPLEMENTED**

Parent:
- `WORLD_SIMULATION_TIME_AND_DURATION_STANDARD.md`

Purpose: define shared terminology for Temporal Drag, Causal Mark, Time Partition, and Event Reversal.

## Core model
- The game retains one authoritative monotonic `world_time`; durable target semantics and the current `time_minutes` compatibility field are governed by `WORLD_SIMULATION_TIME_AND_DURATION_STANDARD.md`.
- Temporal Drag is a bounded local process-rate effect; it does not move the global clock backward.
- Time Partition is subjective processing; external world time and ordinary body mechanics remain authoritative.
- Causal Mark records one approved property and may restore that property at the current world time.
- Event Reversal records eligible bounded physical state and may restore that state at the current world time.

## Snapshot identity
Authoritative snapshots require a stable ID, capture time, expiry time, owner, target entity/zone, schema version, exclusions/anchors, and validity state.

## Identity rule
Snapshots reference stable entity IDs. Restoration updates eligible existing state and must not create duplicate stable identities.

## Causal Mark
The property whitelist is explicit. Restoring one property does not automatically restore linked properties. Dependency validation occurs before commit.

## Event Reversal
The zone snapshot is physical-state data, not a copy of every game system. Status progression, learned skills, faction/reputation records, and unrelated history remain outside the default restore scope.

## Save/load
Active snapshots, expiry, anchors, strain, and used/available state must persist deterministically. Loading cannot duplicate a restore transaction.

## Remaining blockers
- Temporal Drag process classes and boundary physics;
- final Causal Mark property whitelist;
- property dependency rules;
- Event Reversal membership and anchor semantics;
- snapshot use/consumption rules;
- numeric costs and system strain;
- legal/evidence consequences.

No ability is canon-promoted by this standard.