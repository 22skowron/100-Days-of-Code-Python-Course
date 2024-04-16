from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()


ORIGIN_CITY_IATA = "WAW"


    # Check if "IATA code" column isn't empty. If so fill it with correspodning IATA codes.
if sheet_data[0]["iataCode"] == "":
    print("IATA column empty, filling ...")
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

    # Set the time period for the search
tomorrow = datetime.now() + timedelta(days=1)
two_months_from_today = datetime.now() + timedelta(days=(2 * 30))

    # Search for cheapest flight for each destination
for destination in sheet_data:
    # Only if IATA code has been found
    if destination["iataCode"] != "no IATA code found":
        flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=two_months_from_today
        )

        # Only if there were any flights found
        if flight is None:
            continue
        if flight.price < destination["lowestPrice"]:

            # notification_manager.send_sms(
            #     message=f"Low price alert! Only £{flight.price} to fly from
            #     {flight.origin_city}-{flight.origin_airport}to {flight.destination_city}-{flight.destination_airport},
            #     from {flight.out_date} to {flight.return_date}."
            # )

            print(f"Low price alert! Only {flight.price} EUR to fly from {flight.origin_city}-{flight.origin_airport}"
                  f" to {flight.destination_city}-{flight.destination_airport},"
                  f" from {flight.out_date}.")

    else:
        print(f"Couldn't find any flights for {destination["city"]} as there is no IATA code for such a city.")