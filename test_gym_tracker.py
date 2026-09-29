import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import main as app
from analytics import search_exercises, total_volume, workout_analytics
from exercise import Exercise
from storage import load_workouts, save_workouts
from workout import Workout


class GymTrackerTests(unittest.TestCase):
    def setUp(self):
        self.workout = Workout(
            "Push",
            "2026-09-29",
            [Exercise("Bench Press", 3, 10, 20)],
        )

    def test_valid_input_and_volume(self):
        exercise = Exercise(" Squat ", 4, 8, 50)
        self.assertEqual(exercise.name, "Squat")
        self.assertEqual(exercise.volume(), 1600)
        self.assertEqual(app.parse_positive_int("3"), 3)
        self.assertEqual(app.parse_weight("22.5"), 22.5)

    def test_invalid_numbers(self):
        for value in ("abc", "0", "-2"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                app.parse_positive_int(value)
        for value in ("heavy", "-1", "nan", "inf"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                app.parse_weight(value)

    def test_invalid_workout_type(self):
        with self.assertRaises(ValueError):
            Workout("Cardio", "2026-09-29")

    def test_search_found_and_not_found(self):
        self.assertEqual(search_exercises([self.workout], "bench press")[0][1].name, "Bench Press")
        self.assertEqual(search_exercises([self.workout], "deadlift"), [])

    def test_analytics(self):
        result = workout_analytics([self.workout])
        self.assertEqual(total_volume([self.workout]), 600)
        self.assertEqual(result["total_workouts"], 1)
        self.assertEqual(result["total_exercises"], 1)
        self.assertEqual(result["total_volume"], 600)
        self.assertEqual(result["workout_counts"], {"Push": 1, "Pull": 0, "Legs": 0})

    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "workouts.json"
            save_workouts([self.workout], path)
            loaded = load_workouts(path)
            self.assertEqual(loaded[0].workout_type, "Push")
            self.assertEqual(loaded[0].exercises[0].name, "Bench Press")
            self.assertEqual(loaded[0].total_volume(), 600)

    def test_reopening_program_loads_saved_workout(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "workouts.json"
            with patch.object(app, "WORKOUTS_FILE", path), patch(
                "builtins.input",
                side_effect=["1", "1", "2026-09-29", "Bench Press", "3", "10", "20", "no", "6"],
            ), patch("builtins.print"):
                app.main()

            with patch.object(app, "WORKOUTS_FILE", path), patch(
                "builtins.input", side_effect=["2", "6"]
            ), patch("builtins.print") as printed:
                app.main()

            output = " ".join(str(call) for call in printed.call_args_list)
            self.assertIn("Bench Press", output)


if __name__ == "__main__":
    unittest.main()