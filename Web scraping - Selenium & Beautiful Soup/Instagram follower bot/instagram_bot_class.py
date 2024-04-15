import pprint
import time
import os
import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://www.instagram.com/"
LOGIN = os.environ.get('LOGIN')
PASSWORD = os.environ.get('PASSWORD')

class FollowerBot:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options)


    def login(self, login, password):
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep(3)
            # Discard cookies
        discard_cookies = self.driver.find_element(By.CLASS_NAME, "_a9_1")
        discard_cookies.click()
        time.sleep(3)
            # Insert login
        login_field = self.driver.find_element(
            By.CSS_SELECTOR,
            'input[aria-label="Numer telefonu, nazwa użytkownika lub adres e-mail"]')
        login_field.send_keys(login)
            # Insert password
        password_field = self.driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Hasło"]')
        password_field.send_keys(password)
            # Submit
        submit_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()
        time.sleep(5)


    def find_profile(self, ig_name):
        global IG_NAME
        self.driver.get(URL + ig_name + "/")
        time.sleep(3)
        IG_NAME = ig_name


    def follow_followers(self):
            # Get into 'followers' section
        self.driver.find_element(By.CSS_SELECTOR, f'a[href="/{IG_NAME}/followers/"]').click()
        time.sleep(3)

            # Return the number of follower-accounts that we can see
        # followers_div = self.driver.find_elements(By.CSS_SELECTOR, '.div[style="display: flex; flex-direction: column; padding-bottom: 0px; padding-top: 0px; position: relative;"]')[1]
        # followers_no = self.driver.execute_script("return arguments[0].children.length", followers_div)

            # Alternative approach
        followers_no = self.driver.execute_script('''return document.querySelectorAll('[style="display: flex; flex-direction: column; padding-bottom: 0px; padding-top: 0px; position: relative;"]')[1].children.length''')
        print(f"Accounts which we can follow: {followers_no}")

            # Identify scroll bar
        scrollable_element = self.driver.find_element(By.CLASS_NAME, "_aano")
        scroll_step = scrollable_element.size["height"]

        x = 1
        while True:
            try:
                user_account = self.driver.find_element(
                    By.XPATH,
                    f"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/"
                    f"div[2]/div/div/div[2]/div[2]/div/div[{str(x)}]")
            except selenium.common.NoSuchElementException:
                break
            # user_account.click()
            print("click")
            time.sleep(0.2)

            x += 1

                # Scroll down the height of the visible part of the scrollable_element (357 px)
                # after all visible accounts have been clicked
            if x % 6 == 0:
                self.driver.execute_script(f"arguments[0].scrollBy(0, {scroll_step})", scrollable_element)
                time.sleep(0.5)
                print("\nScroll!\n")


            # Just print statements
        print(f"\nAccounts followed: {x - 1}")
        if x-1 == int(followers_no):
            print("(Matches with: 'accounts which we can follow'.)")
        else:
            print("(Doesn't match with: 'accounts which we can follow'.)")

        print(f"\nHeight of the scrollable element: "
              f"{self.driver.execute_script("return arguments[0].scrollHeight", scrollable_element)} px.")
        print(f"Height of the visible part of the scrollable element (scroll_step): {scroll_step} px.")

    # Test class

# account_to_follow = "21savage"
# bot = FollowerBot()
# bot.login(LOGIN, PASSWORD)
# bot.find_profile(account_to_follow)
# bot.follow_followers()