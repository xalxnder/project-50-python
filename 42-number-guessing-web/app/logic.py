from random import randint


def guess_number(guess):
    generated_number = randint(0, 10)
    player_guess = guess
    if player_guess == generated_number:
        return "correct"
    elif player_guess > generated_number:
        return "high"
    else:
        return "low"
