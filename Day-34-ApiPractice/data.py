import requests

parameter = {
    "amount": 10,
    "type": "boolean"
}

question_data = requests.get(url="https://opentdb.com/api.php", params=parameter)
question_data.raise_for_status()

question_data = question_data.json()
print(question_data)
