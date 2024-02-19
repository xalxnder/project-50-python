from misc import *


def add(a, b):
	return a + b


def subtract(a, b):
	return a - b


def multiply(a, b):
	return a * b


def divide(a, b):
	return a / b


calculating = True


def calculate_answer(operation, num1, num2):
	answer = operations.get(operation)(num1, num2)
	return answer


clear()
operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide
}

answer = None
while calculating:
	if answer is None:
		print(calc)
		num_1 = float(input("What's the first number? "))
	num_2 = float(input("What's the next number? "))
	user_operation = input("Please enter an operation:")
	answer = calculate_answer(user_operation, num_1, num_2)
	print(f"{num_1}{user_operation}{num_2} = {answer}")
	calc_again = input("Would you like to keep calculating? ")
	if calc_again == "yes":
		num_1 = answer
	else:
		answer = None
		clear()
