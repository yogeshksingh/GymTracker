# Gym Tracker

## Overview

Gym Tracker is a simple command-line app for keeping track of gym sessions. You can log exercises as you go, look back at previous workouts, and see how much weight you've moved over time. Everything is saved locally, so your data is still there the next time you open the app.

## Features

- Log Push, Pull, and Legs workouts with sets, reps, and weight.
- Browse your workout history and search for exercises by name.
- Check total training volume and see how many workouts you've done of each type.
- Keep workout data between sessions using local JSON storage.
- Validate workout types and numeric input.
- Run automated tests for important parts of the application.

## Tools and Technologies

- Python 3.9 or newer
- Python standard library:
  - `json`
  - `dataclasses`
  - `unittest`
- JSON file storage

## Setup

Clone the repository:

```sh
git clone https://github.com/yogeshksingh/GymTracker.git
```

Move into the project folder:

```sh
cd GymTracker
```

## Environment

Python 3.9 or newer is required.

You can check your Python version with:

```sh
python3 --version
```

## Dependencies

The project uses only Python standard-library modules, so no external packages need to be installed.

## Configuration

No additional configuration, API keys, or environment variables are required.

Workout data is stored locally in:

```text
workouts.json
```

## How to Run

From the project folder, start the application with:

```sh
python3 main.py
```

The application provides a menu for adding workouts, viewing workout history, checking total training volume, searching for exercises, and viewing workout statistics.

When you're finished, choose **6. Quit**. Your workout data will remain saved in `workouts.json` for the next time you run the application.

## Testing

The project includes automated tests using Python's built-in `unittest` module.

From the project folder, run:

```sh
python3 -m unittest -v
```

The tests cover areas including:

- Valid and invalid input
- Workout type validation
- Exercise searching
- Workout statistics
- Saving and loading workout data
- Reopening the application with saved data

Latest result: all 7 tests passed.

## Project Structure

```text
GymTracker/
├── main.py
├── exercise.py
├── workout.py
├── analytics.py
├── storage.py
├── test_gym_tracker.py
├── workouts.json
├── README.md
└── statement.md
```

## Data Storage

Workout information is stored locally in `workouts.json`. This allows the application to load previously recorded workouts when it is opened again.

## Project Report

A detailed project report is included in the repository as:

```text
Gym_Tracker_Final_Project_Report.pdf
```
