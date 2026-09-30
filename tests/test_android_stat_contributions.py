from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import unittest

from textrpg.android_bridge import create_session


CONTENT = Path(__file__).resolve().parents[1] / "content" / "vertical_slice_01.json"


def attribute(view, key):
    return next(stat for stat in view["status"]["attributes"] if stat["id"] == key)


def skill(view, key):
    return next(
        stat for group in view["status"]["skills"].values()
        for stat in group if stat["id"] == key
    )


class AndroidStatContributionTests(unittest.TestCase):
    def test_initial_schema_and_values_are_preserved_without_invented_contributions(self):
        session = create_session(CONTENT)
        before = deepcopy(session.state.snapshot())
        view = session.scene_view()
        expected = {
            "might": 30, "agility": 35, "endurance": 35, "intellect": 45,
            "will": 40, "perception": 40, "presence": 30,
        }
        self.assertEqual(expected, {s["id"]: s["base"] for s in view["status"]["attributes"]})
        for stat in view["status"]["attributes"]:
            self.assertEqual([], stat["contributions"])
            self.assertEqual(expected[stat["id"]], stat["effective"])
        self.assertEqual(before, session.state.snapshot())

    def test_equipped_contributions_follow_engine_equip_unequip_and_save_load(self):
        with TemporaryDirectory() as directory:
            session = create_session(CONTENT, save_path=Path(directory) / "save.json")
            for item in ("ITEM_DEPOT_JACKET", "ITEM_WORK_GLOVES", "ITEM_SIGNAL_RING", "ITEM_COURIER_NECKTAG"):
                view = session.equip(item)
            expectations = (
                (attribute(view, "endurance"), "body", "Depot utility jacket", 2, 37),
                (attribute(view, "perception"), "ring_1", "Signal ring", 1, 41),
                (attribute(view, "presence"), "neck", "Courier neck tag", 1, 31),
                (skill(view, "technical_systems"), "hands", "Insulated work gloves", 1, 26),
            )
            for stat, slot, label, value, total in expectations:
                self.assertEqual(total, stat["effective"])
                self.assertEqual(
                    [{"kind": "equipment", "label": label, "slot": slot, "value": value}],
                    stat["contributions"],
                )
            session.save()
            restored = create_session(CONTENT, save_path=Path(directory) / "save.json")
            self.assertEqual(view, restored.load())
            unequipped = restored.unequip("body")
            self.assertEqual(35, attribute(unequipped, "endurance")["effective"])
            self.assertEqual([], attribute(unequipped, "endurance")["contributions"])
            self.assertEqual(26, skill(unequipped, "technical_systems")["effective"])

    def test_hidden_condition_and_perk_provenance_stays_redacted(self):
        session = create_session(CONTENT)
        session.state.perks["PERK_PRIVATE_RUNTIME"] = {
            "visible": False, "modifiers": {"attributes.endurance": 3},
        }
        session.state.perks["PERK_PRIVATE_REGISTRY"] = {
            "modifiers": {"attributes.endurance": 4},
        }
        session.engine.perk_definitions["PERK_PRIVATE_REGISTRY"] = {
            "player_visible": False, "label": "SECRET PERK LABEL",
        }
        session.state.player["conditions"] = {
            "COND_PRIVATE_RUNTIME": {
                "visible": False, "modifiers": {"attributes.endurance": -1},
            },
            "COND_PRIVATE_REGISTRY": {
                "modifiers": {"attributes.endurance": -2},
            },
        }
        session.content.registries["conditions"]["COND_PRIVATE_REGISTRY"] = {
            "player_visible": False, "name": "SECRET CONDITION LABEL",
        }
        view = session.scene_view()
        stat = attribute(view, "endurance")
        self.assertEqual(39, stat["effective"])
        self.assertEqual(
            [{"kind": "unidentified", "label": "Unidentified modifier", "slot": None, "value": 4}],
            stat["contributions"],
        )
        encoded = json.dumps(view)
        for secret in ("PERK_PRIVATE", "COND_PRIVATE", "SECRET PERK LABEL", "SECRET CONDITION LABEL"):
            self.assertNotIn(secret, encoded)

    def test_canceling_visible_sources_are_retained_and_projection_is_detached(self):
        session = create_session(CONTENT)
        session.equip("ITEM_DEPOT_JACKET")
        session.state.player["conditions"] = {
            "COND_VISIBLE": {"modifiers": {"attributes.endurance": -2}},
        }
        session.content.registries["conditions"]["COND_VISIBLE"] = {"name": "Fatigue"}
        before = deepcopy(session.state.snapshot())
        view = session.scene_view()
        stat = attribute(view, "endurance")
        self.assertEqual(35, stat["effective"])
        self.assertFalse(stat["modified"])
        self.assertEqual([2, -2], [entry["value"] for entry in stat["contributions"]])
        self.assertEqual(["Depot utility jacket", "Fatigue"], [entry["label"] for entry in stat["contributions"]])
        self.assertTrue(all(set(entry) == {"kind", "label", "slot", "value"} for entry in stat["contributions"]))
        stat["contributions"][0]["value"] = 999
        self.assertEqual(before, session.state.snapshot())
        self.assertEqual(2, attribute(session.scene_view(), "endurance")["contributions"][0]["value"])


if __name__ == "__main__":
    unittest.main()
