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

COINS = {
    "quarters" : 0.25,
    "dimes" : 0.10,
    "nickles" : 0.05,
    "pennies" : 0.01
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def report():
    """shows the current resource values & the money made."""
    print(f"Water: {resources['water']}ml \n"
            f"Milk: {resources['milk']}ml \n" 
            f"Coffee: {resources['coffee']}g \n"
            f"Money: ${round(money,2)} ")

def check_resources(menu_option):
    """checks if there are enough resources to make that drink."""
    for content in MENU[menu_option]["ingredients"]:
        if resources[content] < MENU[menu_option]["ingredients"][content]:
            print(f"Sorry there is not enough {content}.")
            return False
    return True

def update_rescources(menu_option):
    """deducts ingredients to make the drink from the resources."""
    for content in MENU[menu_option]["ingredients"]:
        resources[content] -= MENU[menu_option]["ingredients"][content]
    global money
    money += MENU[menu_option]["cost"]
    

def transaction(menu_option, money):
    """Checks if the user has inserted enough money"""
    cost = MENU[menu_option]["cost"]
    if money < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money > cost:
        print(f"Here is ${money - cost} dollars in change.")
    return True

def insert_coins():
    """prompts the user to insert coins."""
    money = 0
    for coin in COINS:
        money += int(input(f"How many {coin} ? : ")) * COINS[coin]
    return money

def make_coffee(menu_option):
    """makes the drink the user selected."""
    if check_resources(menu_option):
        money = insert_coins()
        if transaction(menu_option, money):
            update_rescources(menu_option)
            return True
        return False
    return False

while True:
    
    menu_option = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while not ( menu_option in MENU or menu_option == "report" or menu_option =="off"):
        print("Sorry, we dont serve that !")
        menu_option = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if menu_option == "off":
        break
    elif menu_option == "report":
        report()
    else:
        if make_coffee(menu_option):
            print(f"Here is your {menu_option}. Enjoy !")
            
