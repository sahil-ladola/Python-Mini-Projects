class FlightData:
    # Round trip
    # def __init__(self, price, from_city, from_airport, to_city, to_airport, going_date, return_date):
    #     self.price = price
    #     self.from_city = from_city
    #     self.from_airport = from_airport
    #     self.to_city = to_city
    #     self.to_airport = to_airport
    #     self.going_date = going_date
    #     self.return_date = return_date
    # One Way
    def __init__(self, price, from_city, from_airport, to_city, to_airport, going_date):
        self.price = price
        self.from_city = from_city
        self.from_airport = from_airport
        self.to_city = to_city
        self.to_airport = to_airport
        self.going_date = going_date
