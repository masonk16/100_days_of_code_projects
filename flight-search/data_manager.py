import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT= "https://api.sheety.co/5a2e01fafcc55f932af52f3e9867cb60/flightDeals/prices")

class DataManager:
    """
    This class is responsible for talking to the Google Sheet.
    """

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

