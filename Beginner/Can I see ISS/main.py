import requests
import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()

MY_LAT = float(os.environ.get('WARSAW_LAT'))
MY_LONG = float(os.environ.get('WARSAW_LONG'))
OPEN_NOTIFY_ENDPOINT = os.environ.get('ON_ENDPOINT')
SUNRISE_SUNSET_ENDPOINT = os.environ.get('SS_ENDPOINT')

current_hour = dt.datetime.now().hour

      # GETTING CURRENT ISS POSITION COORDINATES
response_iss = requests.get(OPEN_NOTIFY_ENDPOINT)
data_iss = response_iss.json()

iss_lat = float(data_iss["iss_position"]["latitude"])
iss_long = float(data_iss["iss_position"]["longitude"])


      # GETTING THE TIME OF SUNRISE AND SUNSET
parameters = {
      "lat": MY_LAT,
      "lng": MY_LONG,
      "formatted": 0
}

response_sun = requests.get(SUNRISE_SUNSET_ENDPOINT, params=parameters)
response_sun.raise_for_status()
data_sun = response_sun.json()

sunrise_hour = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hour = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0])


      # Function which returns "yes" when we can see ISS and "no" when we can't
def can_see_ISS():
      # Checking if it's dark (night)
      if sunset_hour < current_hour or current_hour < sunrise_hour:
            # Checking if ISS's position is close to our position
            if MY_LAT-5 < iss_lat < MY_LAT+5 and MY_LONG-5 < iss_long <MY_LONG+5:
                  return True
            else:
                  print(f"ISS is to far from your location so as you were able to see it.\n"
                        f"ISS location is (LAT:{iss_lat}, LONG:{iss_long}),\n"
                        f"while your location is (LAT:{MY_LAT}, LONG:{MY_LONG})")
                  return False
      else:
            print("It's day. You can't see anything in the sky apart from clouds and the sun.")
            return False


if can_see_ISS():
      print(":)")
else:
      print(":(")



