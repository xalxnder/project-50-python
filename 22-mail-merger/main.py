NAMES = "Input/Names/invited_names.txt"
LETTERS = "Input/Letters/starting_letter.txt"
READY_DIR = "Output/ReadyToSend/"

# for each name in invited_names.txt
with open(NAMES, "r") as name_file:
	name_list = name_file.readlines()
	name_list = [x[:-1] for x in name_list]



# Replace the [name] placeholder with the actual name.
with open(LETTERS, "r") as letter_file:
	letter_text = letter_file.read()
	for name in name_list:
		updated_letter = letter_text.replace("[name]", name)
	# Save the letters in the folder "ReadyToSend".
		with open(f"{READY_DIR}letter_for_{name}.txt", "w") as ready_file:
			ready_file.write(updated_letter)
