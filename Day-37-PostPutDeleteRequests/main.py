import requests
import os

USERNAME = os.environ.get("OWM_API_USERNAME_DAY37")
TOKEN = os.environ.get("OWM_API_TOKEN_DAY37")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

requests.post()
