from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine_on = True
menu = Menu()
coffee_machine = CoffeeMaker()
register = MoneyMachine()

coffee_machine.report()
register.report()

# coffee_machine.is_resource_sufficient()

while machine_on:
	user_choice = input("What drink would you like?")
	if user_choice == "report":
		coffee_machine.report()
		register.report()
	elif user_choice == "off":
		machine_on = False
	elif user_choice in ["latte", "espresso", "latte"]:
		drink = menu.find_drink(user_choice)
		if coffee_machine.is_resource_sufficient(drink):
			register.make_payment(drink.cost)
			coffee_machine.make_coffee(drink)
