from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

x = 0
all_snakes = []
for _ in range(0, 3):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.up()
    snake.goto(x=x, y=0)
    x -= 20
    all_snakes.append(snake)



screen.exitonclick()
