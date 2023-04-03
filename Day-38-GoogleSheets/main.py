import requests
import os
from datetime import datetime

API_ID = os.environ['API_ID_DAY38']
API_KEY = os.environ['API_KEY_DAY38']

nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

body = {
    "query": input("Tell me which exercises you did: "),
}


response = requests.post(url=nutritionix_url, json=body, headers=headers)
print(response.text)

