from turtle import Turtle
TOP_BOUNDARY = 250
BOTTOM_BOUNDARY = -250
RIGHT_BOUNDARY = 280
LEFT_BOUNDARY = -280


class Paddle(Turtle):
	def __init__(self, side):
		super().__init__()
		self.shape("square")
		self.color("white")
		self.setheading(90)
		self.penup()
		self.shapesize(.9, 4.0)
		self.pick_side(side)

	def pick_side(self, side):
		if side == "left":
			self.goto(LEFT_BOUNDARY, 0)
		else:
			self.goto(RIGHT_BOUNDARY, 0)

	def player1_up(self):
		if self.ycor() < TOP_BOUNDARY:
			self.forward(20)

	def player1_down(self):
		if self.ycor() > BOTTOM_BOUNDARY:
			self.backward(20)

	def player2_up(self):
		if self.ycor() < TOP_BOUNDARY:
			self.forward(20)

	def player2_down(self):
		if self.ycor() > BOTTOM_BOUNDARY:
			self.backward(20)


class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.color("white")
		self.penup()
		self.shape("circle")
		self.setheading(190)

	def move_ball(self):
		if self.ycor() > RIGHT_BOUNDARY or self.ycor() < LEFT_BOUNDARY:
			self.setheading(self.heading() * -1)
			print(self.heading())
		self.forward(20)

	def collide_with_paddle(self, paddle1, paddle2):
		if self.distance(paddle1) < 50 or self.distance(paddle2) < 50:
			self.setheading(180 - self.heading())

	def past_player1(self):
		if self.xcor() < LEFT_BOUNDARY and self.heading():
			return True

	def past_player2(self):
		if self.xcor() > RIGHT_BOUNDARY and self.heading():
			return True



class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.color("white")
		self.penup()
		self.hideturtle()
		self.player1_score = 0
		self.player2_score = 0
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear()
		self.goto(-170, 220)
		self.write(self.player1_score, align="center", font=("Courier", 80, "normal"))
		self.goto(170, 220)
		self.write(self.player2_score, align="center", font=("Courier", 80, "normal"))

	def player1_point(self):
		self.player1_score += 1
		self.update_scoreboard()

	def player2_point(self):
		self.player2_score += 1
		self.update_scoreboard()






