import turtle
import pandas
import pandas as pd
from classes import GameCursor

#Screen settings
screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
screen.bgpic('blank_states_img.gif')

cursor = GameCursor()
STATES_FILE = '50_states.csv'
DATA = pandas.read_csv(STATES_FILE)
GAME_DURATION = len(DATA["state"])

state_values = DATA.state.values
state_list = DATA.state.values.tolist()
game_score = 0
game_round = 0
user_answer = ''

while game_round <= GAME_DURATION and user_answer != "Exit":
	user_answer = screen.textinput(title="Guess The State", prompt="What's another state's name?").title()
	print(f"Your current score is {game_score}")
	print(f"Round: {game_round}")

	if user_answer in state_values:
		"""
		If the user's answer is in the states_value , then remove that state from the state_list, and place the 
		answer on the board.
		"""
		state_list.remove(user_answer)
		x_cord = DATA[state_values == user_answer]['x'].values[0]
		y_cord = DATA[state_values == user_answer]['y'].values[0]
		cursor.place_answer(x_cord, y_cord, user_answer)
		game_score += 1
	else:
		print('not found')
	game_round += 1


#Save missing states to CSV
df = pd.DataFrame({'Missing States':state_list})
df.to_csv('missing.csv', index=False)


