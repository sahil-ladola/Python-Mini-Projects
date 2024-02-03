import requests
from flight_data import FlightData
import os

TEQUILA_APIKEY = os.environ["TEQUILA_APIKEY"]
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"


class FlightSearch:
    def get_iatacode(self, cityname):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {
            "apikey": TEQUILA_APIKEY
        }
        query = {
            "term": cityname,
            "location_types": "city"
        }
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, from_city_code, to_city_code, from_time, to_time):
        headers = {
            "apikey": TEQUILA_APIKEY
        }
        # Round Trip
        # query = {
        #     "fly_from": from_city_code,
        #     "fly_to": to_city_code,
        #     "date_from": from_time.strftime("%d/%m/%Y"),
        #     "date_to": to_time.strftime("%d/%m/%Y"),
        #     "nights_in_dst_from": 7,
        #     "nights_in_dst_to": 28,
        #     "one_for_city": 1,
        #     "max_stopovers": 0,
        #     "curr": "INR"
        # }

        # One Way
        query = {
            "fly_from": from_city_code,
            "fly_to": to_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No fights found for {to_city_code}.")
            return None
        # Round Trip
        # flight_data = FlightData(
        #     price=data["price"],
        #     from_city=data["route"][0]["cityFrom"],
        #     from_airport=data["route"][0]["flyFrom"],
        #     to_city=data["route"][0]["cityTo"],
        #     to_airport=data["route"][0]["flyTo"],
        #     going_date=data["route"][0]["local_departure"].split("T")[0],
        #     return_date=data["route"][1]["local_departure"].split("T")[0]
        # )

        # One way
        flight_data = FlightData(
            price=data["price"],
            from_city=data["route"][0]["cityFrom"],
            from_airport=data["route"][0]["flyFrom"],
            to_city=data["route"][0]["cityTo"],
            to_airport=data["route"][0]["flyTo"],
            going_date=data["route"][0]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.to_city}: ₹{flight_data.price}")
        return flight_data
