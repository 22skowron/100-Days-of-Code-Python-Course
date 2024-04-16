import json
import requests
from flight_data import FlightData
from pprint import pprint
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

TEQUILA_ENDPOINT = os.environ.get('TEQUILA_ENDPOINT')
TEQUILA_API_KEY = os.environ.get('TEQUILA_API_KEY')


class FlightSearch:
    def __init__(self):
        self.flight_number = 0
        self.flight_data_json = {}
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]

        if results != [] and results[0]["code"] is not None:
            code = results[0]["code"]
            return code
        else:
            return "no IATA code found"


    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "one_for_city": 1,
            "max_stopovers": 0,
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=header,
            params=query,
        )
        # pprint(response.json()["data"])

        # Check if there are any flights for given location
            # Search for direct connections
        try:
            data = response.json()["data"][0]
            non_direct_connection = False

            # pprint(response.json())
            print("Direct connection")
        except IndexError:
            try:
                    # Search for non_direct connections
                query.pop("max_stopovers")
                response = requests.get(
                    url=f"{TEQUILA_ENDPOINT}/v2/search",
                    headers=header,
                    params=query,
                )
                data = response.json()["data"][0]
                non_direct_connection = True

                # pprint(response.json())
                print("Non_direct connection")
            except IndexError:
                print(f"No flights found for {destination_city_code}.")
                return None


            # Get the info about the stopovers if present
        stopovers_dic = {}
        if non_direct_connection:
            j_part_no = 0
            for j_part in data["route"][:(len(data["route"])-1)]:
                j_part_no += 1
                city_name_stopover = j_part["cityTo"]
                stopover = {f"Stopover{j_part_no}": city_name_stopover}
                stopovers_dic.update(stopover)


            # In case of stopovers being present
        dest_indx = len(data["route"]) - 1

            # Update data to be passed in into a JSON file:
        new_data_json = {
                    "From": f"{data["route"][0]["cityFrom"]}, {data["route"][0]["flyFrom"]}",
                    "To": f"{data["route"][dest_indx]["cityTo"]}, {data["route"][dest_indx]["flyTo"]}",
                    "Departure date": data["route"][0]["local_departure"].split("T")[0],
                    # "Return date": data["route"][1]["local_departure"].split("T")[0],
                    "Price": f"{data["price"]} EUR",
                }
            # Update flight number
        self.flight_number += 1

        if stopovers_dic != {}:
            new_data_json.update({"Stopovers": stopovers_dic})

        self.flight_data_json[f"Flight{self.flight_number}"] = new_data_json

            # Store the information about the flight into a JSON file
        with open(file="../flight_deals.json", mode="w") as file:
            json.dump(self.flight_data_json, fp=file, indent=3)

            # If there were, then create a FlightData object storing inf about the cheapest ticket
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][dest_indx]["cityTo"],
            destination_airport=data["route"][dest_indx]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            stopovers=stopovers_dic,
            # return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.destination_city}: {flight_data.price} EUR")
        return flight_data


# code_searcher = FlightSearch()
#
#     # Time
# tomorrow = datetime.now() + timedelta(days=1)
# two_months_from_today = datetime.now() + timedelta(days=(2 * 30))
#
#     # Gets IATA code of Bali
# # print(code_searcher.get_destination_code("Bali"))
#
#     # Test get flight data - for "WAW" to "DPS" (Bali)
# code_searcher.check_flights(
#     origin_city_code="WAW",
#     destination_city_code="DPS",
#     from_time=tomorrow,
#     to_time=two_months_from_today
# )