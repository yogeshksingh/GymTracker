def total_volume(workouts):
    return sum(workout.total_volume() for workout in workouts)


def search_exercises(workouts, name):
    search_name = name.strip().casefold()
    return [
        (workout, exercise)
        for workout in workouts
        for exercise in workout.exercises
        if exercise.name.casefold() == search_name
    ]


def workout_analytics(workouts):
    return {
        "total_workouts": len(workouts),
        "total_exercises": sum(len(workout.exercises) for workout in workouts),
        "total_volume": total_volume(workouts),
        "workout_counts": {
            workout_type: sum(workout.workout_type == workout_type for workout in workouts)
            for workout_type in ("Push", "Pull", "Legs")
        },
    }