from flask import Flask, render_template, request
import random
import cv2
import mediapipe as mp
import numpy as np

app = Flask(__name__)

def generate_workout(pushup_count):
    if pushup_count < 10:
        strength_level = 'beginner'
    elif 10 <= pushup_count <= 25:
        strength_level = 'intermediate'
    else:
        strength_level = 'advanced'

    workout_plan = {
        'beginner': ['Knee Push-Ups * 10', 'Pike Push-Ups * 10', 'Mountain Climber * 20', 'Dumbbell Bicep Curls *15', 'Tricep Dips * 10'],
        'intermediate': ['Push-Ups * 20', 'Pike Push-Ups * 20', 'Abdominal Crunches *20', 'Hammer Curls * 20','Tricep Kickbacks * 20'],
        'advanced': ['Diamond Push-Ups * 25', 'Hindu Push-Ups * 20', 'Bicycle Crunches * 25', 'V-Up * 18','EZ Bar Curls * 25']
    }

    exercises = workout_plan[strength_level]
    random.shuffle(exercises)  # Shuffle the exercises for variety
    return '\n'.join(exercises)

def generate_lower_body_workout(squat_count):
    if squat_count < 10:
        strength_level = 'beginner'
    elif 10 <= squat_count <= 25:
        strength_level = 'intermediate'
    else:
        strength_level = 'advanced'

    workout_plan = {
        'beginner': ['Side Hops * 15','Bodyweight Squats * 20', 'Lunges * 20', 'Donkey Kicks * 25', 'Calf Raises * 25'],
        'intermediate': ['Barbell Squats * 25', 'Sumo Squat * 25', 'Wall Sit * 40 sec', 'Lunges * 30','Calf Raises * 40'],
        'advanced': ['Front Squats *30', 'Bulgarian Split Squats * 30', 'Wall Sit * 80 sec', 'Jumping Squats * 28','Calf Raises * 60']
    }

    exercises = workout_plan[strength_level]
    random.shuffle(exercises)  # Shuffle the exercises for variety
    return '\n'.join(exercises)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_workout', methods=['POST'])
def generate_upper_body_workout():
    if request.method == 'POST':
        pushup_count = int(request.form['pushup_count'])
        workout = generate_workout(pushup_count)
        return render_template('workout.html', workout=workout)

@app.route('/generate_lower_body_workout', methods=['POST'])
def generate_lower_body_workout_route():
    if request.method == 'POST':
        squat_count = int(request.form['squat_count'])
        workout = generate_lower_body_workout(squat_count)
        return render_template('workout.html', workout=workout)

if __name__ == '__main__':
    app.run(debug=True)