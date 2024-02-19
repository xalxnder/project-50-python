GREETING = "Welcome to the tip calculator."
total_bill = float(input("What was the total bill? "))
tip_choice = int(input("What percentage would you like to give? 10, 12, or 15?"))
amount_of_guests = int(input("How many people will be splitting the bill?"))


def generate_bill(total, tip, guest_amount):
	tip = (tip_choice/100) * total_bill
	final_amount = (tip + total_bill) / amount_of_guests
	return 'Each person should pay ${:.2f}.'.format(final_amount)


print(generate_bill(total_bill, tip_choice, amount_of_guests))
