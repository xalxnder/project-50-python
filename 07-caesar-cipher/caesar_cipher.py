alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
			'v', 'w', 'x', 'y', 'z']

print(alphabet.index("z"))
print(len(alphabet))
print(alphabet[-21])

def encrypt(shift_amount, secret):
	new_word = ""
	for letter in secret:
		if (shift_amount + alphabet.index(letter)) >= len(alphabet):
			"""
			Needed to figure out a way to handle when you go outside of alphabet length. What helped me come to the 
			solution was just by visualizing a number line. For example:
			-3 -2 -1 0 1 2 3 
			"""
			new_word += alphabet[shift_amount + (alphabet.index(letter) - len(alphabet))]
		elif letter in alphabet:
			new_word += alphabet[alphabet.index(letter) + shift_amount]
			new_word += " "
	return new_word

def decrypt(shift_amount,secret):
	original_word = ""
	for letter in secret:
		if (alphabet.index(letter) - shift_amount) < 0:
			original_word += alphabet[(alphabet.index(letter) + len(alphabet)) - shift_amount]
		elif letter in alphabet:
			original_word += alphabet[alphabet.index(letter) - shift_amount]
		elif letter == " ":
			original_word += " "
	return original_word


USER_CHOICE = input("Would you like to encrypt or decrypt a message? ")


while USER_CHOICE not in ["encrypt", "decrypt"]:
	USER_CHOICE = input("Please enter \"encrypt\" or \"decrypt\"! ")
MESSAGE = input("Please enter a message ")
SHIFT_AMOUNT = int(input("How much would you like to shift? "))


if USER_CHOICE == "encrypt":
	print(encrypt(SHIFT_AMOUNT, MESSAGE))
else:
	print(decrypt(SHIFT_AMOUNT, MESSAGE))


