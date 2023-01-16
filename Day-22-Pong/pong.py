from turtle import Screen
from paddle import Paddle
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle(side="right")
paddle2 = Paddle(side="left")
screen.update()

screen.listen()
# paddle1 moving.
screen.onkey(key="w", fun=paddle1.move_up)
screen.onkey(key="s", fun=paddle1.move_down)
# paddle2 moving.
screen.onkey(key="Up", fun=paddle2.move_up)
screen.onkey(key="Down", fun=paddle2.move_down)

while True:
    time.sleep(0.1)
    screen.update()




screen.exitonclick()
