import turtle
from turtle import Turtle
from random import randint

turtle.colormode(255)


class Frog(Turtle):
	def __init__(self):
		super().__init__()
		self.color("Green")
		self.shape("turtle")
		self.penup()
		self.reset_pos()
		self.setheading(90)

	def up(self):
		self.forward(20)

	def down(self):
		self.backward(20)

	def reset_pos(self):
		self.goto(0, -250)


class Car:
	def __init__(self):
		super().__init__()
		self.car_list = []
		self.speed = 10

	def generate_color(self):
		r = randint(0, 255)
		g = randint(0, 255)
		b = randint(0, 255)
		color = (r, g, b)
		return color

	def set_cords(self):
		y_cord = randint(-280, 280)
		car_cord = (300, y_cord)
		return car_cord

	def generate(self):
		chance = randint(1, 5)
		if chance == 1:
			new_car = Turtle()
			new_car.penup()
			new_car.goto(self.set_cords())
			new_car.shape("square")
			new_car.shapesize(.9, 2.0)
			new_car.setheading(180)
			new_car.color(self.generate_color())
			self.car_list.append(new_car)

	def move_cars(self):
		for car in self.car_list:
			car.speed(0)
			car.forward(self.speed)

	def reset_cars(self):
		for car in self.car_list:
			car.reset()
			car.hideturtle()
			car.penup()

	def increase_speed(self):
		self.speed += 5


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.hideturtle()
		self.color("blue")
		self.goto(-170,200)
		self.level = 0
		self.update_score()

	def update_score(self):
		self.clear()
		self.level += 1
		self.write(f"Level:{self.level} ", align="center", font=("Courier", 30, "normal"))

	def game_over(self):
		self.goto(0,0)
		self.write(f"Game Over", align="center", font=("Courier", 30, "normal"))



