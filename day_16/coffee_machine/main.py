from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

on = True
while on:
    menu_list = menu.get_items()
    order_name = input(f"What would you like? {menu_list} :").lower()
    while order_name not in menu_list and order_name != "off" and order_name != "report":
        print("Sorry, we dont serve that !")
        order_name = input(f"What would you like? {menu_list} :").lower()
        

    if order_name == "report":
        coffeemaker.report()
        moneymachine.report()
    elif order_name == "off":
        on = False
    else:
        drink = menu.find_drink(order_name)
        if coffeemaker.is_resource_sufficient(drink):
            if moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
