from random import randint
"""
-  Generate a random word
	- This can be pregenerated for now.
-  Display the game board, represented by underscores "_".
	-  This should be length of the word to guess.
- Ask user to guess a letter.
- Start life counter
- If user guess is correct
	- Notify them
	- Display updated board with their guess in place
- If guess is wrong
	- Notify them
	- Display the board 
	- Subtract life from counter
"""

word_list = ["boy", "car","town", "tycoon", "mouse"]


def generate_word(lst):
	word = []
	word += lst[randint(0,len(lst)-1)]
	return word


def generate_board(word):
	game_board = []
	for i in range(len(word)):
		game_board.insert(0,"_")
	return game_board


def show_board(board):
	print(''.join(board))


def play_again():
	choice = input("Play again?").lower()
	if choice in ["y", "yes"]:
		game()
	elif choice in ["n", "no"]:
		print("Thanks for playing !")
		exit()


def reset():
	life_count = 6
	return life_count


def game():
	generated_word = generate_word(word_list)
	generated_board = generate_board(generated_word)
	life = reset()
	while life != 0:
		print(generated_word)
		user_guess = input("Please guess a letter: ")
		if user_guess in generated_word:
			position = [index for (index, char) in enumerate(generated_word) if user_guess == char][0]
			print("Correct!")
			generated_board[position] = user_guess
			if generated_word == "".join(generated_board):
				print("You win!")
				play_again()
		else:
			print("Sorry, try again.")
			life -= 1
		show_board(generated_board)
	print("Game Over")
	play_again()



game()
