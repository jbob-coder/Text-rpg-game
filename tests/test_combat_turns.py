from __future__ import annotations

import unittest

from textrpg.combat_schema import TacticalCell, TacticalCoord, TacticalMap, TacticalTransition
from textrpg.combat_state import (
    ACTIVATION_ACTIVE,
    PHASE1_MOVE_POINTS,
    PHASE1_SPRINT_POINTS,
    CombatSession,
    TacticalActorState,
    path_traversal_cost,
)


def line_map(
    width: int,
    *,
    costs: dict[int, int] | None = None,
) -> TacticalMap:
    costs = costs or {}
    return TacticalMap(
        "MAP_MOVEMENT_TEST",
        1,
        width,
        1,
        (0,),
        tuple(
            TacticalCell(
                TacticalCoord(x, 0, 0),
                movement_cost=costs.get(x, 1),
            )
            for x in range(width)
        ),
    )


def transition_map() -> TacticalMap:
    cells = (
        TacticalCell(TacticalCoord(0, 0, 0)),
        TacticalCell(TacticalCoord(0, 0, 1)),
    )
    return TacticalMap(
        "MAP_TRANSITION_TEST",
        1,
        1,
        1,
        (0, 1),
        cells,
        (
            TacticalTransition(
                "TRANSITION_TEST",
                TacticalCoord(0, 0, 0),
                TacticalCoord(0, 0, 1),
                cost=4,
            ),
        ),
    )


def actions() -> dict[str, dict[str, object]]:
    return {
        "ACTION_MOVE": {
            "action_id": "ACTION_MOVE",
            "category": "move",
            "cost": 1,
        },
        "ACTION_SPRINT": {
            "action_id": "ACTION_SPRINT",
            "category": "sprint",
            "cost": 2,
        },
    }


def actor(
    actor_id: str,
    coord: TacticalCoord,
    *,
    faction_id: str = "FACTION_A",
    initiative: float = 10,
) -> TacticalActorState:
    return TacticalActorState(
        actor_id=actor_id,
        faction_id=faction_id,
        coord=coord,
        initiative=initiative,
    )


def active_session(
    tactical_map: TacticalMap,
    *,
    actor_state: TacticalActorState | None = None,
    extra_actors: tuple[TacticalActorState, ...] = (),
) -> tuple[CombatSession, TacticalActorState]:
    primary = actor_state or actor("ACTOR_A", TacticalCoord(0, 0, 0))
    session = CombatSession(
        encounter_id="ENCOUNTER_MOVEMENT_TEST",
        tactical_map=tactical_map,
        seed=23,
        actors=(primary,) + extra_actors,
        combat_actions=actions(),
    )
    session.begin_next_activation()
    return session, primary


class CombatMovementTests(unittest.TestCase):
    def test_preview_is_read_only_and_move_allows_six_points(self) -> None:
        session, primary = active_session(line_map(7))
        before = (
            primary.coord,
            primary.action_budget,
            primary.activation_state,
            session.event_index,
            tuple(session.committed_events),
        )

        plan = session.preview_movement(
            actor_id=primary.actor_id,
            action_id="ACTION_MOVE",
            goal=TacticalCoord(6, 0, 0),
        )

        self.assertEqual(PHASE1_MOVE_POINTS, plan.movement_allowance)
        self.assertEqual(6, plan.traversal_cost)
        self.assertEqual(1, plan.action_budget_cost)
        self.assertEqual(before[0], primary.coord)
        self.assertEqual(before[1], primary.action_budget)
        self.assertEqual(before[2], primary.activation_state)
        self.assertEqual(before[3], session.event_index)
        self.assertEqual(before[4], tuple(session.committed_events))

    def test_move_rejects_seven_points_without_spending_budget(self) -> None:
        session, primary = active_session(line_map(8))

        with self.assertRaisesRegex(ValueError, "allowance is 6"):
            session.commit_movement(
                actor_id=primary.actor_id,
                action_id="ACTION_MOVE",
                goal=TacticalCoord(7, 0, 0),
            )

        self.assertEqual(TacticalCoord(0, 0, 0), primary.coord)
        self.assertEqual(4, primary.action_budget)
        self.assertEqual(0, session.event_index)
        self.assertEqual([], session.committed_events)

    def test_sprint_allows_ten_points_and_spends_authored_budget_cost(self) -> None:
        session, primary = active_session(line_map(8))

        event = session.commit_movement(
            actor_id=primary.actor_id,
            action_id="ACTION_SPRINT",
            goal=TacticalCoord(7, 0, 0),
        )

        self.assertEqual(PHASE1_SPRINT_POINTS, 10)
        self.assertEqual(TacticalCoord(7, 0, 0), primary.coord)
        self.assertEqual(2, primary.action_budget)
        self.assertEqual(1, session.event_index)
        self.assertEqual(1, event.event_index)
        self.assertEqual(4, event.budget_before)
        self.assertEqual(2, event.budget_after)
        self.assertEqual("7,0,0", event.target_key)
        self.assertEqual(64, len(event.digest))
        self.assertEqual(ACTIVATION_ACTIVE, primary.activation_state)

    def test_terrain_cost_counts_against_movement_allowance(self) -> None:
        tactical_map = line_map(7, costs={3: 2})
        session, primary = active_session(tactical_map)

        with self.assertRaisesRegex(ValueError, "costs 7, allowance is 6"):
            session.preview_movement(
                actor_id=primary.actor_id,
                action_id="ACTION_MOVE",
                goal=TacticalCoord(6, 0, 0),
            )

        self.assertEqual(TacticalCoord(0, 0, 0), primary.coord)
        self.assertEqual(4, primary.action_budget)

    def test_transition_cost_comes_from_authoritative_map_edge(self) -> None:
        tactical_map = transition_map()
        path = (
            TacticalCoord(0, 0, 0),
            TacticalCoord(0, 0, 1),
        )
        self.assertEqual(4, path_traversal_cost(tactical_map, path))

        session, primary = active_session(tactical_map)
        event = session.commit_movement(
            actor_id=primary.actor_id,
            action_id="ACTION_MOVE",
            goal=TacticalCoord(0, 0, 1),
        )
        self.assertEqual(TacticalCoord(0, 0, 1), primary.coord)
        self.assertEqual(3, primary.action_budget)
        self.assertEqual("0,0,1", event.target_key)

    def test_enemy_occupancy_rejects_path_before_cost_is_spent(self) -> None:
        enemy = actor(
            "ACTOR_ENEMY",
            TacticalCoord(1, 0, 0),
            faction_id="FACTION_B",
            initiative=1,
        )
        session, primary = active_session(line_map(3), extra_actors=(enemy,))

        with self.assertRaisesRegex(ValueError, "no legal tactical path"):
            session.commit_movement(
                actor_id=primary.actor_id,
                action_id="ACTION_MOVE",
                goal=TacticalCoord(2, 0, 0),
            )

        self.assertEqual(TacticalCoord(0, 0, 0), primary.coord)
        self.assertEqual(4, primary.action_budget)
        self.assertEqual(0, session.event_index)

    def test_insufficient_budget_rejects_without_mutation(self) -> None:
        session, primary = active_session(line_map(3))
        primary.action_budget = 1

        with self.assertRaisesRegex(ValueError, "insufficient action budget"):
            session.commit_movement(
                actor_id=primary.actor_id,
                action_id="ACTION_SPRINT",
                goal=TacticalCoord(2, 0, 0),
            )

        self.assertEqual(TacticalCoord(0, 0, 0), primary.coord)
        self.assertEqual(1, primary.action_budget)
        self.assertEqual(0, session.event_index)

    def test_commit_failure_rolls_back_coord_budget_state_and_event_index(self) -> None:
        session, primary = active_session(line_map(3))

        def explode(**_kwargs):
            raise RuntimeError("forced event failure")

        session._append_movement_event = explode  # type: ignore[method-assign]

        with self.assertRaisesRegex(RuntimeError, "forced event failure"):
            session.commit_movement(
                actor_id=primary.actor_id,
                action_id="ACTION_MOVE",
                goal=TacticalCoord(2, 0, 0),
            )

        self.assertEqual(TacticalCoord(0, 0, 0), primary.coord)
        self.assertEqual(4, primary.action_budget)
        self.assertEqual(ACTIVATION_ACTIVE, primary.activation_state)
        self.assertEqual(0, session.event_index)
        self.assertEqual([], session.committed_events)

    def test_identical_movement_commit_has_identical_event_digest(self) -> None:
        first, first_actor = active_session(line_map(3))
        second, second_actor = active_session(line_map(3))

        event_a = first.commit_movement(
            actor_id=first_actor.actor_id,
            action_id="ACTION_MOVE",
            goal=TacticalCoord(2, 0, 0),
        )
        event_b = second.commit_movement(
            actor_id=second_actor.actor_id,
            action_id="ACTION_MOVE",
            goal=TacticalCoord(2, 0, 0),
        )

        self.assertEqual(event_a, event_b)


if __name__ == "__main__":
    unittest.main()
