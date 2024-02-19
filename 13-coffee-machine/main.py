from os import system, name


def clear(): system('cls' if name == 'nt' else 'clear')


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

COINS = {
	"quarter": 0.25,
	"dime": 0.10,
	"nickel": 0.05,
	"penny": 0.01
}


def report():
	water = resources["water"]
	milk = resources["milk"]
	coffee = resources["coffee"]
	money = resources["money"]
	return f"Water: {water}ml \nMilk: {milk}ml \nCoffee:{coffee}g \nMoney: ${money}"


def enough_resources(drink):
	ingredients_needed = []
	for ingredient, amount_required in MENU[drink]["ingredients"].items():
		if amount_required > resources[ingredient]:
			ingredients_needed.append(ingredient)
	if len(ingredients_needed) == 0:
		return True
	else:
		print(f"Sorry, there is not enough {' or '.join(ingredients_needed)}")
		return False


def calculate_coins(quarter_amount, dime_amount, nickel_amount, penny_amount):
	quarter_value = quarter_amount * COINS["quarter"]
	dime_value = dime_amount * COINS["dime"]
	nickel_value = nickel_amount * COINS["nickel"]
	penny_value = penny_amount * COINS["penny"]
	coin_sum = quarter_value + dime_value + nickel_value + penny_value
	return float(f"{coin_sum:.2f}")


def enough_money(money_given, drink):
	cost_of_drink = MENU[drink]["cost"]
	change = money_given - cost_of_drink
	if money_given < cost_of_drink:
		print("Sorry not enough money.")
		return False
	print(f"Here is your change {change:.2f}")
	return True


def ask_for_money():
	quarters = float(input("How many quarters will you be inserting? "))
	dimes = float(input("How many dimes will you be inserting? "))
	nickles = float(input("How many nickels will you be inserting? "))
	pennies = float(input("How many pennies will you be inserting? "))
	value = calculate_coins(quarter_amount=quarters, dime_amount=dimes, nickel_amount=nickles, penny_amount=pennies)
	return value


def make_drink(drink_choice, money):
	for ingredient, amount in MENU[drink_choice]["ingredients"].items():
		if ingredient in resources.keys():
			resources[ingredient] -= amount
	resources["money"] += money

	print(resources)


print(f"MENU \nEspresso - ${MENU['espresso']['cost']:.2f} "
	  f"\nLatte - ${MENU['latte']['cost']:.2f} "
	  f"\nCappuccino - ${MENU['cappuccino']['cost']:.2f}")
machine_on = True

while machine_on:
	drink_choice = input("What would you like?:").lower()
	while drink_choice not in ["report", "off", "espresso", "latte", "cappuccino"]:
		drink_choice = input("That wasnt a valid option. What would you like?:")
	if drink_choice == "report":
		clear()
		print(report())
	elif drink_choice in ["espresso", "latte", "cappuccino"]:
		user_money = ask_for_money()
		if enough_resources(drink_choice) and enough_money(user_money, drink_choice):
			make_drink(drink_choice, user_money)
			print(f"Here is your {drink_choice}")
	else:
		print("Machine powering off. Goodbye")
		machine_on = False
