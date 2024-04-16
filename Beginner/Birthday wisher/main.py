##################### Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


import pandas as pd
import datetime as dt
import random

df = pd.read_csv("birthdays.csv")



# GETTING CURRENT MONTH AND DAY
current_month = dt.datetime.now().month
current_day = dt.datetime.now().day

print(f"Current month: {current_month}\n"
      f"Current day: {current_day}\n")



# CHECKING IF SOMEBODY HAS BIRTHDAY TODAY
for index, row in df.iterrows():
    if current_day == row.loc["day"] and current_month == row["month"]:

        # PREPARING WISHES
        birthday_person = row.loc["name"]
        chance = random.randint(1,3)
        if chance == 1:
            with open("letter_templates/letter_1.txt") as file:
                wishes = file.read()
                wishes_personalized = wishes.replace("[NAME]", birthday_person)
                print(wishes_personalized)

        elif chance == 2:
            with open("letter_templates/letter_2.txt") as file:
                wishes = file.read()
                wishes_personalized = wishes.replace("[NAME]", birthday_person)
                print(wishes_personalized)

        elif chance == 3:
            with open("letter_templates/letter_3.txt") as file:
                wishes = file.read()
                wishes_personalized = wishes.replace("[NAME]", birthday_person)
                print(wishes_personalized)







