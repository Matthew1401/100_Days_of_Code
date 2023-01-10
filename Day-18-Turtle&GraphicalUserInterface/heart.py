from turtle import *

tim = Turtle()
screen = Screen()
tim.pencolor("red")

tim.setheading(270)
tim.up()
tim.forward(100)
tim.down()

# Left side
tim.setheading(90)
tim.left(45)
tim.forward(250)

tim.setheading(90)

for _ in range(90):
    tim.forward(3)
    tim.right(2)

tim.setheading(90)

for _ in range(90):
    tim.forward(3)
    tim.right(2)

tim.right(45)
tim.forward(250)

screen.exitonclick()