import requests
import os

SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]

class DataManager:
    def __init__(self):
        self.destination = {}

    def get_destination(self):
        response = requests.get(url=SHEET_PRICES_ENDPOINT)
        data = response.json()
        self.destination = data["prices"]
        return self.destination

    def update_destination_codes(self):
        for city in self.destination:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEET_PRICES_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)
