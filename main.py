import json

def save_log(monday):
    log = monday.to_dict()
    with open('workout_log.json', 'w') as file:
        json.dump(log,file)
        
def open_log():
    try:
        with open('workout_log.json', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {}


class Workout:
    def __init__(self, date):
        self.date = date
        self.exercises = []
        self.log = {'date' : self.date, 'exercises' : self.exercises}

    def to_dict(self):
        return {
                'date' :  self.date,
                'exercises' : self.exercises
                }

    def from_dict(self, data): 
        self.date = data['date']
        self.exercises = data['exercises']


    def log_workout(self,exercise_name,weights,sets,reps):
        self.exercises.append({
                'exercise name' : exercise_name,
                'weights' : weights,
                'sets' : sets,
                'reps' : reps
                })
        save_log(monday)
 

    def view_workout(self):
        print(f"Date: {open_log()['date']}")
        for lists in open_log()['exercises']:
            print(f"{lists['exercise name']}: {lists['weights']} x {lists['reps']} x {lists['sets']}")

    def update_workout(self):
        pass


monday = Workout('Monday')

monday.view_workout()


# Program needs to handle multiple classes?


"""
To make the program useful for multiple workout instances, you could adjust the design to allow storing, retrieving, and managing multiple `Workout` sessions, each with its own date and exercises. Here’s an outline of the approach:

### 1. Use a List of Workouts in `save_log` and `open_log`
   - Instead of saving just one workout, save a list of workouts in `workout_log.json`. Each workout entry would be a dictionary (from `to_dict()`), allowing you to save multiple sessions.

### 2. Modify `save_log` to Handle Multiple Workouts
   - `save_log` could either:
     - Append a new workout to the existing list in `workout_log.json`.
     - Or, overwrite the list with all current workout instances in memory.

### 3. Update `open_log` to Load All Workouts
   - When `open_log()` loads the data, it should read the list of all workouts and then create `Workout` instances for each entry. 

### 4. Maintain a Collection of `Workout` Instances
   - Create a `WorkoutManager` class that holds a list of `Workout` instances and handles actions like adding, retrieving, or deleting specific workouts. 

This structure will allow you to create multiple workout sessions and manage them effectively. Would you like to start with any specific part of this setup?

"""