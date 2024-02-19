from random import randint
player_choice = int(input("What do you choose: \n 0:Rock\n 1:Paper \n 2:Scissors"))

computer_choice = randint(0,2)

if player_choice == computer_choice:
	print("DRAW")
elif player_choice == 0 and computer_choice == 2:
	print("You win! Rock crushes scissors")
elif player_choice == 1 and computer_choice == 0:
	print("You win! Paper covers rock")
elif player_choice == 2 and computer_choice == 1:
	print("You win! Scissors cuts paper")
elif player_choice == 2 and computer_choice == 0:
	print("You Lose! Rock crushes scissors")
elif player_choice == 0 and computer_choice == 1:
	print("You Lose! Paper covers rock")
elif player_choice == 1 and computer_choice == 2:
	print("You Lose! Scissors cuts paper")