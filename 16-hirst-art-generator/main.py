import turtle
from turtle import *
from random import randint


window = Screen()
x = Turtle()
x.hideturtle()
x.penup()
window.colormode(255)
window.setup(500,500)
def random_color():
	rgb = []
	for i in range(3):
		value = randint(0, 255)
		rgb.append(value)
	return tuple(rgb)


for pos in range(10):
	x.goto(-200,x.ycor()+30)
	for i in range(13):
		x.dot(20, random_color())
		x.forward(30)

# The Screen
window.exitonclick()
