from turtle import Screen
from crossing_classes import Frog, Car, Scoreboard
import time

screen = Screen()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

frog = Frog()
car = Car()

screen.listen()
screen.onkey(frog.up, "Up")
screen.onkey(frog.down, "Down")

game_on = True

while game_on:

	time.sleep(0.1)
	screen.update()

	car.generate()
	car.move_cars()
	#Check For Collision
	for i in car.car_list:
		if frog.distance(i) < 25:
			game_on = False
			scoreboard.game_over()

	#Check if frog made it to end of board.
	if frog.ycor() >= 280:
		frog.reset_pos()
		car.reset_cars()
		scoreboard.update_score()
		car.increase_speed()



screen.exitonclick()
