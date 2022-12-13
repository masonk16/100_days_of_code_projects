import requests

LAT = -17.766150
LONG = 30.979220
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
#
# iss_position = (latitude, longitude)
# print(iss_position)

parameters = {
    "lat": LAT,
    "lng": LONG,
}
response = requests.get("https://api.sunrise-sunset.org/json",
                        params=parameters)
response.raise_for_status()
data = response.json()
print(data)