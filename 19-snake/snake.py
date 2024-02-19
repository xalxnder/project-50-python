from turtle import Turtle
from random import randint


class Snake(Turtle):

	def __init__(self):
		super().__init__()
		self.body = []
		self.init_snake()
		self.head = self.body[0]

	def reset_snake(self):
		for segments in self.body:
			segments.goto(1000, 1000)
		self.body.clear()
		self.init_snake()
		self.head = self.body[0]

	def init_snake(self):
		# Create the snake
		for i in range(3):
			snake_body = self.add_body()
			self.body.append(snake_body)
		# Place snake on board.
		for i in range(len(self.body[1:])):
			current_segment = self.body[i]
			prev_snake = self.body[i - 1]
			current_segment.goto(prev_snake.xcor() - 20, 0)

	def eat_food(self, food):
		if self.head.distance(food) < 30:
			return True
		else:
			return False

	def move_snake(self):
		for segment in range(len(self.body) - 1, 0, -1):
			new_x = self.body[segment - 1].xcor()
			new_y = self.body[segment - 1].ycor()
			self.body[segment].goto(new_x, new_y)

	def add_segment(self, lst):
		new_segment = self.add_body()
		lst.append(new_segment)

	def go_up(self):
		if self.head.heading() != 270:
			self.head.setheading(90)

	def go_down(self):
		if self.head.heading() != 90:
			self.head.setheading(270)

	def go_left(self):
		if self.head.heading() != 0:
			self.head.setheading(180)

	def go_right(self):
		if self.head.heading() != 180:
			self.head.setheading(0)

	@staticmethod
	def out_of_bounds(lst):
		return abs(lst.xcor()) > 260 or abs(lst.ycor()) > 260

	@staticmethod
	def add_body():
		body_part = Turtle("square")
		body_part.color("white")
		body_part.penup()
		return body_part


class Food(Turtle):
	def __init__(self):
		super().__init__()

	def create(self):
		self.penup()
		self.shape("circle")
		self.turtlesize(.8)
		self.color("blue")
		self.goto(randint(0, 200), randint(0, 200))

	def clear_move(self):
		self.goto(randint(0, 200), randint(0, 200))


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.goto(0, 270)
		self.score = 0
		self.highscore = self.get_highscore()
		self.color("blue")
		self.hideturtle()
		self.update_score()

	def update_score(self):
		self.clear()
		self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 20, "normal"))

	def reset_scoreboard(self):
		if self.score > self.highscore:
			self.highscore = self.score
		self.score = 0
		self.update_score()

	def increase_score(self):
		self.score += 1

	def save_score(self):
		with open ("highscore.txt", "w") as file:
			file.write(f"{self.highscore}")

	def get_highscore(self):
		with open ("highscore.txt", "r") as file:
			highscore = int(file.read())
			return highscore



