from pprint import pprint
import requests
from dotenv import load_dotenv
import os

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.environ.get('SHEETY_PRICES_ENDPOINT')
SHEETY_BEARER_TOKEN = os.environ.get('SHEETY_BEARER_TOKEN')
header_sheety = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=header_sheety)
        data = response.json()
        # pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                headers=header_sheety,
                json=new_data
            )




    # For testing

# searcher = DataManager()
# searcher.get_destination_data()
