import random
from random import randint
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Password Generator")


password = []

letter_count = int(input("How many letters would you like in your password: "))

for i in range(letter_count):
	password.append(letters[randint(0,len(letters)-1)])

symbol_count = int(input("How many symbols would you like in your password? "))

for i in range(symbol_count):
	password.append(symbols[randint(0,len(symbols)-1)])

number_count = int(input("How many numbers would you like in your password? "))

for i in range(number_count):
	password.append(numbers[randint(0,len(numbers)-1)])

random.shuffle(password)
password = "".join(password)

print(f"Your new password is: \n{password}")