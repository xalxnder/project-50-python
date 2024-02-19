from turtle import Turtle
import turtle

class GameCursor(Turtle):
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.penup()

	def place_answer(self, x, y, answer):
		self.goto(x, y)
		self.write(answer)




