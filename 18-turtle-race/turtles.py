from turtle import Turtle
from random import randint


class Racers(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("turtle")
		self.penup()
		self.turtle_color()
		self.goto(-230, -90)

	def turtle_color(self):
		rgb = []
		for i in range(3):
			value = randint(0, 255)
			rgb.append(value)
		self.fillcolor(tuple(rgb))

