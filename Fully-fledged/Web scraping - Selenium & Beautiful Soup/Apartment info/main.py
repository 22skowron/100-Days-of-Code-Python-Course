import requests
import selenium.common.exceptions
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint
import time
import json

    # SCRAPING APARTMENT DATA SECTION
###########################################################################################
URL_ZILLOW = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(URL_ZILLOW)

soup = BeautifulSoup(response.text, "html.parser")

    # Get addresses
address_tags = soup.find_all(name="address")
addresses = [tag.string.strip() for tag in address_tags]

    # Get prices
price_tags = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
prices = []
for tag in price_tags:
    price = tag.string
    if "+" in price:
        price = price.split("+")[0]
    elif "/" in price:
        price = price.split("/")[0]

    prices.append(price)

    # Get offer links
offer_link_tags = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
offer_links = [tag.get("href") for tag in offer_link_tags]

apartments = {}

for x in range(len(addresses)):

    apartments[f"Apartment{x+1}"] = {
        "address": addresses[x],
        "price": prices[x],
        "offer_link": offer_links[x]
    }

    # Dump to json
with open("apartments.json", "w") as file:
    json.dump(apartments, file, indent=4)



    # GOOGLE FORMS SECTION
###########################################################################################
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSctHvt5JUD1tRhR2iprWUsCg47N3pQMMaqG5wgf8H2gzC84uQ/viewform?usp=sf_link"

driver = webdriver.Chrome(chrome_options)


# driver.get(FORM_LINK)
# driver.maximize_window()
# time.sleep(2)


    # Enter inf. & submit a form for each apartment
for (apartment, details) in apartments.items():

    driver.get(FORM_LINK)
    driver.maximize_window()
    time.sleep(1)

    #     # Open next form
    # try:
    #     next_form = driver.find_element(By.LINK_TEXT, "Prześlij kolejną odpowiedź")
    #     next_form.click()
    #     time.sleep(1)
    # except selenium.common.exceptions.NoSuchElementException:
    #     # Thrown only in 1st iteration
    #     pass

        # Identify input windows:
    input_address = driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')[0]
    input_price = driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')[1]
    input_link = driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')[2]

        # Enter inf.
    input_address.send_keys(details["address"])
    input_price.send_keys(details["price"])
    input_link.send_keys(details["offer_link"])
    time.sleep(0.5)

        # Submit form
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_button.click()
    time.sleep(1)

driver.quit()

















