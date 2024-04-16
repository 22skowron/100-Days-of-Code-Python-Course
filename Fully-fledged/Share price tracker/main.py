import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = os.environ.get('API_KEY')
API_ENDPOINT = "https://www.alphavantage.co/query"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY
}

################################################################

################################################################
def should_send_message(spread):
    if spread < -0.05 or spread > 0.05:
        return True
    else:
        return False

def send_message(spread):
        if spread < -0.05:
            print(f"Tesla's stock price fell by {spread * 100}%. Fetch news details.")
        elif spread > 0.05:
            print(f"Tesla's stock price rose by {spread * 100}%. Fetch news details.")



    # Getting current date
current_date = dt.datetime.now().date()
yesterday_date = (current_date - dt.timedelta(days=1))
before_yesterday_date = (current_date - dt.timedelta(days=2))
yesterday_weekday = yesterday_date.weekday()

    # Explicitly defining data to check whether code works
# yesterday_date = "2023-12-29"
# before_yesterday_date = "2023-12-28"
# yesterday_weekday = 4


    # Getting Tesla's opening & closing price
response_stock = requests.get(url=API_ENDPOINT, params=parameters)
response_stock.raise_for_status()
data_tesla = response_stock.json()

try:
    if yesterday_weekday in range(1, 5):
        # yesterday's
        opening_price = float(data_tesla["Time Series (Daily)"][str(yesterday_date)]["1. open"])
        # before yesterday's
        closing_price = float(data_tesla["Time Series (Daily)"][str(before_yesterday_date)]["4. close"])

        spread = round((opening_price - closing_price) / closing_price, 4)
        if should_send_message(spread):
            send_message(spread)

        print(opening_price)
        print(closing_price)
        print(spread)

    elif yesterday_weekday == 0:

        friday_date = (current_date - dt.timedelta(days=4))

        # yesterday's
        opening_price = float(data_tesla["Time Series (Daily)"][str(yesterday_date)]["1. open"])
        # last friday's
        closing_price = float(data_tesla["Time Series (Daily)"][str(friday_date)]["4. close"])

        spread = round((opening_price - closing_price) / closing_price, 4)

        print("Yesterday was Monday. Checking the difference between Friday's closing and yesterday's opening price.")

        if should_send_message(spread):
            send_message(spread)

    elif yesterday_weekday == 5:
        print("Yesterday was Saturday. Stockmarket was closed.")
    elif yesterday_weekday == 6:
        print("Yesterday was Sunday. Stockmarket was closed.")

    # Might raise exceptions if there was a holiday and no data for a given period was given in API response
    # Code assumes that stock market is open every working day. It doesn't detect holiday etc.
except:
    print("Even though yesterday wasn't the weekend there is no stock market data "
          "either for yesterday or for the day before yesterday."
          "There must have been a holiday."
          "Therefore printing the difference between closing and opening price between latest two days for which "
          "stock data is available.")

    stock_market_days_list = [value for (key, value) in data_tesla["Time Series (Daily)"].items()]
    # last day
    opening_price = float(stock_market_days_list[0]["1. open"])
    # penultimate day
    closing_price = float(stock_market_days_list[1]["4. close"])

    spread = round((opening_price - closing_price) / closing_price, 4)
    if should_send_message(spread):
        send_message(spread)

    print(opening_price)
    print(closing_price)
    print(spread)









