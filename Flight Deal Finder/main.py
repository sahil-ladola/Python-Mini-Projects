from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "BOM"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_iatacode(row["city"])
    data_manager.destination = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_later = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_later
    )
    if flight.price < destination["lowestPrice"]:
        # Round Trip
        # notification_manager.send_email(message=f"Only {flight.price}/-\n"
        #                                         f"{flight.from_city}-{flight.from_airport} -> {flight.to_city}-{flight.to_airport}\n"
        #                                         f"{flight.going_date} to {flight.return_date}.")
        # One Way
        notification_manager.send_email(message=f"Only {flight.price}/-\n"
                                                f"{flight.from_city}-{flight.from_airport} -> "
                                                f"{flight.to_city}-{flight.to_airport}\n"
                                                f"{flight.going_date}.")
