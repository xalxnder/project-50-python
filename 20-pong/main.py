import time
from turtle import Screen
from pong_classes import Paddle, Ball, Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


player_1 = Paddle("left")
player_2 = Paddle("right")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_1.player1_up, "w")
screen.onkey(player_1.player1_down, "s")
screen.onkey(player_2.player2_up, "Up")
screen.onkey(player_2.player2_down, "Down")

game_on = True

while game_on:
	screen.update()
	time.sleep(0.05)
	ball.move_ball()

	ball.collide_with_paddle(player_1, player_2)
	if ball.past_player2():
		scoreboard.player1_point()
		ball.goto(0, 0)
	elif ball.past_player1():
		scoreboard.player2_point()
		ball.goto(0, 0)

screen.exitonclick()
