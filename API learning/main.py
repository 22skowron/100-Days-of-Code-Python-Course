import requests
import pprint
from dotenv import load_dotenv
import os

load_dotenv()

api_endpoint = os.environ.get('API_ENDPOINT')
api_key = os.environ.get('API_KEY')

parameters = {
    "lat": 52.229675,
    "lon": 21.012230,
    "cnt": 4,
    "appid": api_key
}


response = requests.get(api_endpoint, params=parameters)
response.raise_for_status()
print(response.status_code)

data = response.json()
# pprint.pprint(data)

id_list = [data["list"][x]["weather"][0]["id"] for x in range(len(data["list"]))]


def need_umbrella():
    for x in id_list:
        if x < 700:
            return True
        else: return False


if need_umbrella():
    print("Bring an umbrella.")
else:
    print("No need to bring an umbrella.")






