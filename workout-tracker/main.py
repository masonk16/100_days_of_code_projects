import os

import requests
import pprint

GENDER = "Male"
WEIGHT_KG = 108.5
HEIGHT_CM = 185
AGE = 24

exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("APP_KEY"),
    "Content-Type": "application/json",
}

exercise = input("What exercise did you do today?: ")

parameters = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_url, json=parameters, headers=headers)
result = response.json()
