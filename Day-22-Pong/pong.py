from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
winning_points = screen.numinput("Winning points", "How many points to win?: ")

ball = Ball()
r_paddle = Paddle(side="right")
l_paddle = Paddle(side="left")
scoreboard = Scoreboard()
screen.update()

screen.listen()
# r_paddle moving.
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)
# l_paddle moving.
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if paddle missed the ball from the right side
    if ball.xcor() > 360:
        ball.miss()
        scoreboard.l_point()
        screen.update()
        time.sleep(0.5)

    # Detect if paddle missed the ball from the left side
    if ball.xcor() < -360:
        ball.miss()
        scoreboard.r_point()
        screen.update()
        time.sleep(0.5)

    # Checking if r_paddle wins
    if scoreboard.r_score == winning_points:
        game_is_on = False
        ball.hideturtle()
        scoreboard.game_end("Right")
        screen.update()

    # Checking if l_paddle wins
    if scoreboard.l_score == winning_points:
        game_is_on = False
        ball.hideturtle()
        scoreboard.game_end("Left")
        screen.update()

screen.exitonclick()
