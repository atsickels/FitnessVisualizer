import csv
from app.model.Workout import Workout

INPUT_FILE_NAME = "data/workouts.csv"

def read_workouts():
    with open(INPUT_FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)
        workouts = [
            Workout(**workout) for workout in reader]
    return workouts
