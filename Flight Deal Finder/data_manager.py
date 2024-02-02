import requests

SHEETY_ENDPOINT = "https://api.sheety.co/c27c382024e5999321ff50d48c24758b/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.destination = {}

    def get_destination(self):
        response = requests.get(url=SHEETY_ENDPOINT)
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
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)
