import os
import requests
import datetime

API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")
MY_TOKEN = os.environ.get("MY_TOKEN")
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = 'https://api.sheety.co/2c408ce9f0ac3e6917e66cfd5863a5b8/myWorkouts/workouts'


workout_query = input("What workout/s did you do?")

time_now = datetime.datetime.today()

auth_headers = {
    "Authorization": f"Bearer {MY_TOKEN}"
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

body = {
 "query": workout_query,
 "gender": "male",
 "weight_kg": 70,
 "height_cm": 174,
 "age": 35
}

response = requests.post(url=nutritionix_endpoint, headers=headers, json=body)

for exercise in response.json()['exercises']:
    body = {
        'workout': {
            'exercise': exercise['name'],
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
            'date': time_now.strftime('%d/%m/%Y'),
            'time': time_now.strftime('%H:%M:%S')
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=body, headers=auth_headers)
    print(sheety_response.text)

