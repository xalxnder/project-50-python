bidders = {}
auction_on = True


def find_max(bidder_dict):
	max_bid = 0
	for bidder, amount in bidders.items():
		if amount > max_bid:
			winner = bidder
			max_bid = amount
	return f"The winner is {winner} with a bid of ${max_bid}"


while auction_on:
	bidder_name = input("What is your name?: ")
	bidder_bid = int(input("How much would you like to bid?: $"))
	bidders[bidder_name]=bidder_bid
	more_bidders = input("Are there any other bidders? ").lower()
	while more_bidders not in ["yes", "no"]:
		more_bidders = input("Are there any other bidders? Must enter \"Yes\" or\"No\" ").lower()
	if more_bidders == "yes":
		auction_on = True
	else:
		auction_on = False

print(find_max(bidders))



