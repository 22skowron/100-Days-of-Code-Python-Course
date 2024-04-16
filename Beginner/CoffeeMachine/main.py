MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

żadanie = ""
fuf = 1

def check_ingredients(coffee_name):
    # if MENU[coffee_name]["ingredients"]["water"] <= resources["water"]:
    #     x = 1
    # else:
    #     x = 0
    #     print("Sorry there is not enough water.")
    # if MENU[coffee_name]["ingredients"]["coffee"] <= resources["coffee"]:
    #     y = 1
    # else:
    #     y = 0
    #     print("Sorry there is not enough coffee.")
    # if coffee_name == "espresso" or (MENU[coffee_name]["ingredients"]["milk"] <= resources["milk"]):
    #     z = 1
    # else:
    #     z = 0
    #     print("Sorry there is not enough milk.")
    # if x == y == z == 1:
    #     return True
    # else:
    #     return False
    ###########################################################################
    for x in MENU[coffee_name]["ingredients"]:
        if MENU[coffee_name]["ingredients"][x] >= resources[x]:
            print(f"Sorry there is not enough {x}")
            return False
    return True


def check_coins(coffee_name, inserted_money):
    if MENU[coffee_name]["cost"] <= inserted_money:
        resources["money"] += MENU[coffee_name]["cost"]
        change = inserted_money - MENU[coffee_name]["cost"]
        if change > 0:
            print(f"Here is ${change} in change.")
        return True
    else:
        print(f"Sorry, there is not enough money. ${inserted_money} refunded.")
        return False


def make_coffee(coffee_name):
    # resources["water"] -= MENU[coffee_name]["ingredients"]["water"]
    # resources["coffee"] -= MENU[coffee_name]["ingredients"]["coffee"]
    # if coffee_name != "espresso":
    #     resources["milk"] -= MENU[coffee_name]["ingredients"]["milk"]
    ###########################################################################
    for x in MENU[coffee_name]["ingredients"]:
        resources[x] -= MENU[coffee_name]["ingredients"][x]



######################## VERSION WITH WHILE LOOP
# while żadanie.lower() != "off":
#     żadanie = input("  What would you like? (espresso/latte/cappuccino): ")
#     if żadanie == "report":
#         print(f"Water: {resources["water"]}")
#         print(f"Milk: {resources["milk"]}")
#         print(f"Coffee: {resources["coffee"]}")
#         print(f"Money: ${resources["money"]}")
#     elif żadanie == "espresso" or żadanie == "latte" or żadanie == "cappuccino":
#         ingredients_available = check_ingredients(żadanie)
#         if ingredients_available:
#             print("Please insert coins.")
#             coins = int(input("How many quarters?  ")) * 0.25
#             coins += int(input("How many dimes? ")) * 0.10
#             coins += int(input("How many nickles? ")) * 0.05
#             coins += int(input("How many pennies? ")) * 0.01
#             enough_money = check_coins(żadanie, coins)
#             if enough_money:
#                 make_coffee(żadanie)
#                 print("Here is your hot coffee! :)")


######################## VERSION WITH RECURSION

def coffee_machine():
    żadanie = input("  What would you like? (espresso/latte/cappuccino): ")
    if żadanie != "off":
        if żadanie == "report":
            print(f"Water: {resources["water"]}")
            print(f"Milk: {resources["milk"]}")
            print(f"Coffee: {resources["coffee"]}")
            print(f"Money: ${resources["money"]}")
        elif żadanie == "espresso" or żadanie == "latte" or żadanie == "cappuccino":
            ingredients_available = check_ingredients(żadanie)
            if ingredients_available:
                print("Please insert coins.")
                coins = int(input("How many quarters?  ")) * 0.25
                coins += int(input("How many dimes? ")) * 0.10
                coins += int(input("How many nickles? ")) * 0.05
                coins += int(input("How many pennies? ")) * 0.01
                enough_money = check_coins(żadanie, coins)
                if enough_money:
                    make_coffee(żadanie)
                    print("Here is your hot coffee! :)")
        coffee_machine()


coffee_machine()
print("koniec")


# quarters = $0.25,
# dimes = $0.10
# nickles = $0.05
# pennies = $0.01
