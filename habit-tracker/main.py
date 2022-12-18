import requests
import os

USERNAME = "masonmapfunde"
TOKEN = os.environ.get("TOKEN")

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
requests.post(url=graph_endpoint, json=graph_config)

