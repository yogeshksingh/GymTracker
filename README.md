# Gym Tracker

## Overview

Gym Tracker is a simple little app for keeping tabs on your gym sessions without the usual hassle. You can log exercises as you go, look back at previous workouts, and quickly see how much weight you’ve moved over time. Everything is saved locally, so your data is still there the next time you open the app.

## Features

- Log Push, Pull, and Legs workouts with sets, reps, and weight.
- Browse your workout history and search for exercises by name.
- Check total training volume and see how many workouts you’ve done of each type.
- Keep your progress between sessions with local JSON storage.

## Tools and Technologies

- Python 3.9 or newer
- Python standard library (`json`, `dataclasses`, `unittest`)
- JSON file storage

## Installation

You don’t need any extra packages to get started. Just make sure Python 3.9 or newer is installed, then open a terminal in the project folder.

## How to Run

From the project folder, start the app with:

```sh
python3 main.py```

Your workouts are stored in `GymTracker/workouts.json`. When you’re done, choose **6. Quit** and your data will still be there next time you launch the app.

## Testing

To run the tests:

```sh
python3 -m unittest -v```

These checks cover valid and invalid input, workout types, exercise searching, workout stats, saving and loading, and reopening the app with saved data.

Latest result: all 7 tests passed.
