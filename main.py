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
        pass

    def update_workout(self):
        pass


monday = Workout('Monday')


monday.log_workout('Bench Press',225,3,12)
monday.log_workout('Bench Press',175,5,10)



print(open_log())


# Program needs to handle multiple classes?


