from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")


def draw_a_square():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)


def write_a_dashed_line():
    for _ in range(15):
        tim.forward(10)
        tim.up()
        tim.forward(10)
        tim.down()











screen = Screen()
screen.exitonclick()
