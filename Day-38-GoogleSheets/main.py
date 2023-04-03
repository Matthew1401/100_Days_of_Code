import requests
import os
from datetime import datetime
from requests.auth import HTTPBasicAuth

GENDER = "male"
WEIGHT_KG = 56
HEIGHT_CM = 179
AGE = 26

API_ID = os.environ['API_ID_DAY38']
API_KEY = os.environ['API_KEY_DAY38']
USERNAME = os.environ['USERNAME_DAY38']
PASSWORD = os.environ['PASSWORD_DAY38']

basic = HTTPBasicAuth(USERNAME, PASSWORD)

sheet_endpoint = os.environ['SHEET_DAY38']
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

# I ran for 20 minutes and swim 20km.
parameters = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

result = requests.post(url=exercise_endpoint, json=parameters, headers=headers).json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=basic)

    print(sheet_response.text)
