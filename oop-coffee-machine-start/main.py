from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
cashier = MoneyMachine()
menu_item = Menu()


is_on = True
while is_on:
    user_input = input("​What would you like? (espresso/latte/cappuccino):")
    if user_input == "report":
        coffee_machine.report()
        cashier.report()
    elif user_input == "off":
        is_on = False
    else:
        find_drink = menu_item.find_drink(user_input)
        if coffee_machine.is_resource_sufficient(find_drink) and cashier.make_payment(find_drink.cost):
            coffee_machine.make_coffee(find_drink)
