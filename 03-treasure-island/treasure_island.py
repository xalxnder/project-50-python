GREETING = "Welcome to Treasure Island!"

choice1 = input("You're at a crosssroad. Where do you want to go? Left or Right?")

if choice1 == "right":
	choice2 = input(
		"You've come to a lake. There is an island in the middle. Do you want to \"swim\" or \"wait for a boat"
		"?\"")
	if choice2 == "wait":
		choice3 = input("The boat has taken you to the island!! But you meet a troll. Do you want to fight, or talk?")

		if choice3 == "talk":
			print("You win!! The troll ended up being a nice guy!")
		else:
			print("The troll killed you. Game over.")
	else:
		print("Game over. You know you can't swim!")
else:
	print("Game over. Sorry")
