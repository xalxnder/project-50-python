from turtle import Screen, Turtle
from random import randint
from snake import Snake, Food, Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake")

scoreboard = Scoreboard()
snake = Snake()


def collide_with_body():
	for x in snake.body[1:]:
		if snake.head.distance(x) < 10:
			return True


game_on = True
food = Food()
food.create()
while game_on:
	screen.update()
	time.sleep(.1)

	if snake.eat_food(food):
		scoreboard.increase_score()
		scoreboard.update_score()
		food.clear_move()
		snake.add_segment(snake.body)

	if snake.out_of_bounds(snake.head) or collide_with_body():
		scoreboard.save_score()
		scoreboard.reset_scoreboard()
		snake.reset_snake()
	snake.move_snake()

	snake.head.forward(20)
	screen.onkey(snake.go_up, "Up")
	screen.onkey(snake.go_down, "Down")
	screen.onkey(snake.go_left, "Left")
	screen.onkey(snake.go_right, "Right")

	screen.listen()

screen.exitonclick()
