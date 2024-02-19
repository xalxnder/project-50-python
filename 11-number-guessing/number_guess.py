from random import randint
from os import system, name
def clear(): system('cls' if name == 'nt' else 'clear')


RANDOM_NUM = randint(0,100)
MESSAGE = "Welcome to the number game game!"
print(MESSAGE)

def set_difficulty():
	difficulty = input("Would you like to play on 'Easy' or 'Hard' mode? ")
	if difficulty == "easy":
		return 10
	else:
		return 5


print(f"{RANDOM_NUM}")


def game():
	attempts = set_difficulty()
	while attempts != 0:
		print(f"You have {attempts} left.")
		player_guess = int(input("Make a guess: "))
		if player_guess == RANDOM_NUM:
			print("You got it!")
			attempts = 0
		elif player_guess > RANDOM_NUM:
			print("Sorry, too high.")
			attempts -= 1
		else:
			print("Sorry, too low.")
			attempts -= 1
	else:
		clear()
		print("Sorry, you didnt guess correctly. Game Over")


game()


