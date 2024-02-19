import pandas as pd

nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

user_input = input("Enter a word: ").upper()

solution = [nato_dict[letter] for letter in user_input]
print(solution)
