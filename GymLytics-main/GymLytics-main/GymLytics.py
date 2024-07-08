import argparse
from src.exercises.Lunges import Lunges
from src.exercises.Pushup import Pushup
from src.exercises.Plank import Plank
from src.exercises.ShoulderTap import ShoulderTap
from src.exercises.Squat import Squat

class GymLytics:
    def __init__(self):
        self.pushup = Pushup()
        self.plank = Plank()
        self.squat = Squat()
        self.shoulderTap = ShoulderTap()
        self.lunges = Lunges()

    def rep(self, exercise_type, source):
        exercise_type = exercise_type.lower()
        if exercise_type == "pushup":
            self.pushup.exercise(source)
        elif exercise_type == "squat":
            self.squat.exercise(source)
        elif exercise_type == "plank":
            self.plank.exercise(source)
        elif exercise_type == "shouldertap":
            self.shoulderTap.exercise(source)
        elif exercise_type == "lunges":
            self.lunges.exercise(source)
        else:
            raise ValueError(f"Exercise type '{exercise_type}' is not recognized.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', '-t', required=True, help="Type of exercise", type=str)
    parser.add_argument('--source', '-s', required=True, help="Path to video source", type=str)
    args = parser.parse_args()
    
    exercise_type = args.type
    source = args.source
    
    gym = GymLytics()
    gym.rep(exercise_type, source)
