import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint
from dotenv import load_dotenv
import os
import time

load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL_log_in = "https://pl.linkedin.com/"
URL_job_offers = ("https://www.linkedin.com/jobs/search/?currentJobId=3774281502&distance"
                  "=25&f_E=1&geoId=105076658&keywords=Python&origin=JOBS_HOME_SEARCH_CARDS")
LINKEDIN_EMAIL = os.environ.get('LINKEDIN_EMAIL')
LINKEDIN_PASSWORD = os.environ.get('LINKEDIN_PASSWORD')

driver = webdriver.Chrome(chrome_options)
driver.get(URL_log_in)
current_tab = driver.current_window_handle

driver.maximize_window()
time.sleep(2)

    # Accept cookies
cookies_accept = driver.find_element(By.CLASS_NAME, "artdeco-global-alert-action")
cookies_accept.click()

    # Close app download prompt window (if popped up)
try:
    download_app = driver.find_element(By.CLASS_NAME, "cta-modal__dismiss-btn")
    download_app.click()
except selenium.common.NoSuchElementException:
    pass


    # Log me in
email_box = driver.find_element(By.ID, "session_key")
email_box.send_keys(LINKEDIN_EMAIL)

password_box = driver.find_element(By.ID, "session_password")
password_box.send_keys(LINKEDIN_PASSWORD)

log_in = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-btn--full-width")
log_in.click()

    # Navigate to job offers section with given criteria
driver.switch_to.window(current_tab)
driver.get(URL_job_offers)
time.sleep(4)

    # Identify scrollbar
scrollable_element = driver.find_element(By.CSS_SELECTOR, ".jobs-search-results-list")


    # Get list of job offers
job_offers = driver.find_elements(By.CLASS_NAME, "scaffold-layout__list-item")


    # MECHANISM

offers_scaffold_height = scrollable_element.size["height"]
print(f"Srollable element height: {offers_scaffold_height}\n")

heights_sum = 0

for offer in job_offers:

        # Scroll down if all fully-displayed offers were clicked
    if (heights_sum + int(offer.size["height"])) >= offers_scaffold_height:

        print("Scroll")
        driver.execute_script(f"arguments[0].scrollBy(0, {heights_sum})", scrollable_element)
        heights_sum = 0
        time.sleep(0.5)

        # Click the offer
    offer.click()
    time.sleep(0.5)
##########################################################################
# PLACE FOR CODE TO PERFORM SOME ACTIONS
# ON THE SELECTED OFFER
##########################################################################
    print(f"Current offer height: {offer.size["height"]}")
    print(f"Height of offers displayed & clicked: {heights_sum}\n")

        # Update heigths_sum after each click
    heights_sum += int(offer.size["height"])


time.sleep(3)
driver.close()