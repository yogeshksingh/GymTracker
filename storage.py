import json
from pathlib import Path

from exercise import Exercise
from workout import Workout


WORKOUTS_FILE = Path(__file__).with_name("workouts.json")


def load_workouts(file_path=WORKOUTS_FILE):
    path = Path(file_path)
    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("Workout data must be a JSON list.")

    workouts = []
    for workout_data in data:
        exercises = [Exercise(**exercise_data) for exercise_data in workout_data["exercises"]]
        workouts.append(
            Workout(
                workout_type=workout_data["workout_type"],
                date=workout_data["date"],
                exercises=exercises,
            )
        )
    return workouts


def save_workouts(workouts, file_path=WORKOUTS_FILE):
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = [
        {
            "workout_type": workout.workout_type,
            "date": workout.date,
            "exercises": [
                {
                    "name": exercise.name,
                    "sets": exercise.sets,
                    "reps": exercise.reps,
                    "weight": exercise.weight,
                }
                for exercise in workout.exercises
            ],
        }
        for workout in workouts
    ]
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)