from turtles import Racers
from turtle import Screen
from random import randint

screen = Screen()
screen.setup(500, 400)
screen.colormode(255)
racer_list = []

for i in range(5):
	racer = Racers()
	racer.speed("slowest")
	racer_list.append(racer)

for i in range(len(racer_list)):
	current_racer = racer_list[i]
	prev_racer = racer_list[i - 1]
	current_racer.goto(-230, prev_racer.ycor() + 30)

race_on = True

while race_on:
	for turtle in racer_list:
		turtle.forward(randint(10, 40))
		if turtle.xcor() >= 200:
			race_on = False

screen.exitonclick()