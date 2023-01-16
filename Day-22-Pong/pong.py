from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()

paddle1 = Paddle(side="right")
paddle2 = Paddle(side="left")
screen.update()

screen.listen()
# paddle1 moving.
screen.onkey(key="Up", fun=paddle1.move_up)
screen.onkey(key="Down", fun=paddle1.move_down)
# paddle2 moving.
screen.onkey(key="w", fun=paddle2.move_up)
screen.onkey(key="s", fun=paddle2.move_down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()




screen.exitonclick()
