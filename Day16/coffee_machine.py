from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# init
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

command = ""

while command != "off":
    command = input(f"What would you like? ({menu.get_items()}): ").lower()
    
    if command == "report":
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(command):
        drink = menu.find_drink(command)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    elif command == "off":
        print("Shutting down...")