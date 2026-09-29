from dataclasses import dataclass, field

if __package__:
    from .exercise import Exercise
else:
    from exercise import Exercise


WORKOUT_TYPES = ("Push", "Pull", "Legs")


@dataclass
class Workout:
    workout_type: str
    date: str
    exercises: list[Exercise] = field(default_factory=list)

    def __post_init__(self):
        if self.workout_type not in WORKOUT_TYPES:
            raise ValueError("Choose Push, Pull, or Legs for the workout type.")
        self.date = self.date.strip()
        if not self.date:
            raise ValueError("Please enter a date for the workout.")

    def add_exercise(self, exercise):
        if not isinstance(exercise, Exercise):
            raise TypeError("Add an Exercise to this workout.")
        self.exercises.append(exercise)

    def total_volume(self):
        return sum(exercise.volume() for exercise in self.exercises)