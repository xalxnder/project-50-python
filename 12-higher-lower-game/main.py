from art import *
from data import *
from os import system, name
from random import randint
def clear(): system('cls' if name == 'nt' else 'clear')

# Print the higher lower art
print(logo)



# Print the first choice(A)
def pick_choice(data_dict):
	dict_length = len(data_dict) - 1
	choice = data_dict[(randint(0,dict_length))]
	return choice


def compare(a, b):
	if a['follower_count'] > b['follower_count']:
		return "a"
	elif b['follower_count'] > a['follower_count']:
		return "b"


score = 0
game_on = True
# Compare the user's choice with the correct answer

choice_a = pick_choice(data)
choice_b = pick_choice(data)



while game_on:
	if choice_a == choice_b:
		choice_b = pick_choice(data)
	else:
		print(f"A: {choice_a['name']}, a {choice_a['description']} from, {choice_a['country']}.")
		print(vs)
		print(f"B: {choice_b['name']}, a {choice_b['description']} from, {choice_b['country']}.")
		user_choice = input("Who has more followers? A, or B: ").lower()
		clear()
		if compare(choice_a, choice_b) == user_choice:
			score += 1
			print(f"You're right!Current score is {score}")
			choice_a = choice_b
			choice_b = pick_choice(data)
		else:
			print("Sorry, wrong answer. Game Over!")
			print(f"Final Score: {score}")
			game_on = False

