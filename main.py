from math import isfinite


if __package__:
    from .analytics import search_exercises, total_volume, workout_analytics
    from .exercise import Exercise
    from .storage import WORKOUTS_FILE, load_workouts, save_workouts
    from .workout import WORKOUT_TYPES, Workout
else:
    from analytics import search_exercises, total_volume, workout_analytics
    from exercise import Exercise
    from storage import WORKOUTS_FILE, load_workouts, save_workouts
    from workout import WORKOUT_TYPES, Workout


def parse_positive_int(value):
    try:
        number = int(value)
    except ValueError as error:
        raise ValueError("enter a whole number, such as 3.") from error
    if number <= 0:
        raise ValueError("enter a number greater than zero.")
    return number


def parse_weight(value):
    try:
        weight = float(value)
    except ValueError as error:
        raise ValueError("enter a weight, such as 20 or 22.5.") from error
    if not isfinite(weight) or weight < 0:
        raise ValueError("enter a weight of zero or more.")
    return weight


def _read_number(prompt, parser):
    while True:
        try:
            return parser(input(prompt))
        except ValueError as error:
            print(f"Please {error}")


def _add_workout(workouts):
    print("\nChoose a workout:")
    for index, workout_type in enumerate(WORKOUT_TYPES, start=1):
        print(f"{index}. {workout_type}")

    workout_choice = input("Which workout type? ")
    if not workout_choice.isdigit() or not 1 <= int(workout_choice) <= len(WORKOUT_TYPES):
        print("Please choose 1, 2, or 3 for the workout type.")
        return

    workout_type = WORKOUT_TYPES[int(workout_choice) - 1]
    date = input("What date was this workout? ").strip()
    if not date:
        print("No date entered. Let's start again.")
        return

    workout = Workout(workout_type, date)
    print("\nDate:", workout.date)
    print("Workout:", workout_type)

    while True:
        name = input("Which exercise did you do? ").strip()
        if not name:
            print("Please enter an exercise name.")
            continue
        sets = _read_number("How many sets? ", parse_positive_int)
        reps = _read_number("How many reps per set? ", parse_positive_int)
        weight = _read_number("What weight did you use (kg)? ", parse_weight)
        workout.add_exercise(Exercise(name, sets, reps, weight))

        while True:
            add_more = input("Would you like to add another exercise? (yes/no): ").strip().lower()
            if add_more in ("yes", "no"):
                break
            print("Please answer yes or no.")
        if add_more == "no":
            break

    workouts.append(workout)
    save_workouts(workouts, WORKOUTS_FILE)
    print("Workout saved. Nice work!")


def main():
    workouts = load_workouts(WORKOUTS_FILE)

    while True:
        print("\n=== Gym Tracker ===")
        print("1. Add a workout")
        print("2. View workout history")
        print("3. See total training volume")
        print("4. Find an exercise")
        print("5. View workout stats")
        print("6. Quit")

        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            _add_workout(workouts)
        elif choice == "2":
            if not workouts:
                print("Nothing logged yet. Add a workout to get started.")
                continue
            print("\nYour workout history")
            for workout in workouts:
                print("\nDate:", workout.date)
                print("Workout:", workout.workout_type)
                for exercise in workout.exercises:
                    print(exercise)
                print("Total Volume:", workout.total_volume(), "kg")
        elif choice == "3":
            print("Total workout volume:", total_volume(workouts), "kg")
        elif choice == "4":
            matches = search_exercises(workouts, input("Which exercise are you looking for? "))
            if not matches:
                print("I couldn't find that exercise in your workout history.")
            for workout, exercise in matches:
                print("\nDate:", workout.date)
                print("Workout:", workout.workout_type)
                print(exercise)
        elif choice == "5":
            if not workouts:
                print("There are no workouts to summarize yet.")
                continue
            analytics = workout_analytics(workouts)
            print("\nYour workout stats")
            print("Total workouts:", analytics["total_workouts"])
            print("Total exercises:", analytics["total_exercises"])
            print("Total volume:", analytics["total_volume"], "kg")
            for workout_type, count in analytics["workout_counts"].items():
                print(f"{workout_type} workouts:", count)
        elif choice == "6":
            print("See you next workout!")
            break
        else:
            print("I didn't catch that. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()