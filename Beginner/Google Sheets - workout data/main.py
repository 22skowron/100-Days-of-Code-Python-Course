import requests
import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()

API_ID = os.environ.get('API_ID')
API_KEI = os.environ.get('API_KEY')
API_ENDPOINT_NTRX = os.environ.get('API_ENDPOINT_NTRX')
API_ENDPOINT_SHEETY = os.environ.get('API_ENDPOINT_SHEETY')
BEARER_TOKEN_SHEETY = os.environ.get('BEARER_TOKEN_SHEETY')


    # User info about the workout
workout_info = input("What have you done today?: ")

    # Get workout info from Nutrinionix API

header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEI
}

parameters = {
    "query": workout_info,
    "gender": "male",
    "weight_kg": 78,
    "height_cm": 180,
    "age": 23
}

response = requests.post(url=API_ENDPOINT_NTRX, json=parameters, headers=header)
response.raise_for_status()

data = response.json()
print(data)
print(response)

    # Extract the interesting data from Nutrionix API response

exercise = data["exercises"][0]["name"]
calories_burnt = data["exercises"][0]["nf_calories"]
duration_min = data["exercises"][0]["duration_min"]
print(f"{exercise}\n{calories_burnt}\n{duration_min}")

    # Get current date and time from datetime module

current_date = dt.datetime.now().strftime("%d/%m/%Y")
current_time = dt.datetime.now().strftime("%H:%M:%S")
print(f"{current_date}\n{current_time}")

    # Update google sheet using Sheets API
header_sheety = {
    "Authorization": f"Bearer {BEARER_TOKEN_SHEETY}"
}

data_for_spreadsheet = {
    "arkusz1": {
        "date": current_date,
        "time": current_time,
        "exercise": exercise.capitalize(),
        "duration": duration_min,
        "calories": calories_burnt
    }
}

post_response = requests.post(
    url=API_ENDPOINT_SHEETY,
    json=data_for_spreadsheet,
    headers=header_sheety)


print(post_response)
post_response.raise_for_status()






