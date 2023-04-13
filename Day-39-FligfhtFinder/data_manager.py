import requests
from requests.auth import HTTPBasicAuth


class DataManager:

    def __init__(self, username, password, sheet_endpoint):
        self.basic = HTTPBasicAuth(username, password)
        self. sheet_endpoint = sheet_endpoint

    def get_data(self):
        sheet_response = requests.get(self.sheet_endpoint, auth=self.basic).json()

        for row in sheet_response["arkusz1"]:
            if row["iataCode"] == "":
                row["iataCode"] = "TESTING"
                send_data = {"arkusz1": row}
                check = requests.put(self.sheet_endpoint + f'/{row["id"]}', json=send_data, auth=self.basic)
                print(check.text)

        return sheet_response["arkusz1"]


