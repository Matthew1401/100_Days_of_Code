import requests
from datetime import datetime

MY_LAT = 52.237049
MY_LONG = 21.017532


response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
response_iss.raise_for_status()

data_iss = response_iss.json()

longitude = float(data_iss["iss_position"]["longitude"])
latitude = float(data_iss["iss_position"]["latitude"])

iss_position = (longitude, latitude)

print(iss_position)


parameter = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()

data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
print(sunset)


time_now = datetime.now()
print(time_now.hour)
