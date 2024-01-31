import requests
import os
from datetime import datetime

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
API_ENDPOINT = os.environ["API_ENDPOINT"]
EXERCISE_ENDPOINT = os.environ["EXERCISE_ENDPOINT"]
ADD_ROW = os.environ["ADD_ROW"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

user_input = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": user_input
}
response = requests.post(url=f"{API_ENDPOINT}/{EXERCISE_ENDPOINT}", json=exercise_params, headers=headers)
exercises = response.json()["exercises"]

current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%H:%M:%S")

for exercise in exercises:
    # print(exercise["duration_min"])
    sheet_inputs = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    # print(sheet_inputs)
    sheety_response = requests.post(ADD_ROW, json=sheet_inputs, auth=(USERNAME, PASSWORD))
