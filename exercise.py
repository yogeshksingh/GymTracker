from dataclasses import dataclass
from math import isfinite


@dataclass
class Exercise:
    name: str
    sets: int
    reps: int
    weight: float

    def __post_init__(self):
        self.name = self.name.strip()
        if not self.name:
            raise ValueError("Please give the exercise a name.")
        if isinstance(self.sets, bool) or not isinstance(self.sets, int) or self.sets <= 0:
            raise ValueError("Sets must be a whole number greater than zero.")
        if isinstance(self.reps, bool) or not isinstance(self.reps, int) or self.reps <= 0:
            raise ValueError("Reps must be a whole number greater than zero.")
        if not isinstance(self.weight, (int, float)) or not isfinite(self.weight) or self.weight < 0:
            raise ValueError("Weight must be a valid number of zero or more.")
        self.weight = float(self.weight)

    def volume(self):
        return self.sets * self.reps * self.weight

    def __str__(self):
        return f"{self.name}: {self.sets} sets * {self.reps} reps * {self.weight:g} kg"