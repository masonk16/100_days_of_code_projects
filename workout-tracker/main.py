import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

GENDER = "Male"
WEIGHT_KG = 108.5
HEIGHT_CM = 185
AGE = 24

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

SHEET_AUTH = os.environ["SHEET_AUTH"]

exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ["SHEET_ENDPOINT"]

nutrionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

sheety_headers = {
    "Authorization": SHEET_AUTH
}

exercise = input("What exercise did you do today?: ")

nutrionix_parameters = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_response = requests.post(url=exercise_url, json=nutrionix_parameters, headers=nutrionix_headers)
result = exercise_response.json()

today = datetime.now()

for exercise in result["exercises"]:
    sheety_parameters = {
        "sheet1": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise":  exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

sheety_response = requests.post(url=sheety_endpoint, json=sheety_parameters, headers=sheety_headers)
print(sheety_response.text)