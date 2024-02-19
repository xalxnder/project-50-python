from turtle import Turtle


class Controls(Turtle):
	def __int__(self):
		super().__init__()

	def move_forward(self):
		self.forward(10)

	def move_backward(self):
		self.backward(10)

	def turn_left(self):
		self.left(5)

	def turn_right(self):
		self.right(5)


