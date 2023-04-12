import requests
from requests.auth import HTTPBasicAuth


class DataManager:

    def __init__(self, username, password, sheet_endpoint):
        self.basic = HTTPBasicAuth(username, password)
        self. sheet_endpoint = sheet_endpoint

    def get_data(self):
        sheet_response = requests.get(self.sheet_endpoint, auth=self.basic)
        return sheet_response.json()["arkusz1"]


