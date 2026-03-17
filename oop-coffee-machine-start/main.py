from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order = Menu()
Machine = CoffeeMaker()
Money = MoneyMachine()

on = True

while on:

    order_name = input("What would you like? (espresso/latte/cappuccino/): ").lower()

    if order_name == "off":
        break
    elif order_name == "report":
        Machine.report()
        Money.report()
    else:
        Drink = order.find_drink(order_name)

        if Machine.is_resource_sufficient(Drink):
            if Money.make_payment(Drink.cost):
                Machine.make_coffee(Drink)
