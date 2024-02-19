import random
from random import randint


DECK_OF_CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_deck = []
player_score = 0
deal_deck = []
computer_score = 0


def deal_card(amount, deck):
	for i in range(amount):
		card = DECK_OF_CARDS[randint(0, len(DECK_OF_CARDS) - 1)]
		deck.append(card)
	return deck


def calculate_score(deck):
	return sum(deck)


def compare():
	if calculate_score(player_deck) == calculate_score(deal_deck):
		return "Draw"
	elif calculate_score(player_deck) == 21:
		return "You win. You have a Blackjack!"
	elif calculate_score(deal_deck) == 21:
		return "You lose. Dealer has a Blackjack!"
	elif calculate_score(player_deck) > 21:
		return "You lose. You went over!"
	elif calculate_score(deal_deck) > 21:
		return "The Dealer went over, you win!"
	elif calculate_score(player_deck) > calculate_score(deal_deck):
		return "You win!!"
	else:
		return "You lose"


game_on = True

"""
Generate two lists with two numbers
"""
for i in [player_deck, deal_deck]:
	deal_card(2, i)


while game_on:
	print(f"Your cards: {player_deck}: Current Score: {calculate_score(player_deck)}")
	print(f"Computers first card: {deal_deck[0]}")
	"""
	Up here, we're just checking if the game ended or not.
	"""
	if calculate_score(player_deck) == 21 or calculate_score(deal_deck) == 21 or calculate_score(player_deck) > 21:
		game_on = False
	else:
		deal_pass = input("Would you like to deal another card or pass: ")

		if deal_pass == "deal":
			deal_card(1, player_deck)
		elif deal_pass == "pass":
			game_on = False
while calculate_score(deal_deck) != 21 and calculate_score(deal_deck) < 17:
	deal_card(1, deal_deck)

print(f"Your final hand{player_deck}, final_score:{calculate_score(player_deck)}")
print(f"Dealer's hand{deal_deck}, final_score:{calculate_score(deal_deck)}")
"""
And down here, see why the game ended.
"""
print(compare())


