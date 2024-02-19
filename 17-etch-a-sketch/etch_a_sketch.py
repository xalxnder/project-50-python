from turtle import Screen
from controls import Controls

controls = Controls()
screen = Screen()

screen.onkey(controls.move_forward, "Up")
screen.onkey(controls.move_backward, "Down")
screen.onkey(controls.turn_left, "Left")
screen.onkey(controls.turn_right, "Right")
# screen.onkey(controls.reset, "space")
screen.listen()
screen.exitonclick()
