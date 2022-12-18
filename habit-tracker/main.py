import requests
import os
from datetime import datetime

USERNAME = "masonmapfunde"
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "codinggraph1"

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
graph_config = {
    "id": "codinggraph1",
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "kuro",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

rec_info_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

info_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5"
}

response = requests.post(url=rec_info_endpoint, json=info_config, headers=headers)
print(response.text)