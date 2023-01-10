import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)


# def write_a_dashed_line():
#     for _ in range(15):
#         tim.forward(10)
#         tim.up()
#         tim.forward(10)
#         tim.down()


# def draw_a_triangle():
#     tim.pencolor("red")
#     for _ in range(3):
#         tim.forward(100)
#         tim.right(120)
#
#
# def draw_a_square():
#     tim.pencolor("blue")
#     for _ in range(4):
#         tim.forward(100)
#         tim.right(90)
#
#
# def draw_a_pentagon():
#     tim.pencolor("purple")
#     for _ in range(5):
#         tim.forward(100)
#         tim.right(72)
#
#
# def draw_a_hexagon():
#     tim.pencolor("green")
#     for _ in range(6):
#         tim.forward(100)
#         tim.right(60)
#
#
# def draw_a_heptagon():
#     tim.pencolor("brown")
#     for _ in range(7):
#         tim.forward(100)
#         tim.right(51.43)
#
#
# def draw_a_octagon():
#     tim.pencolor("magenta")
#     for _ in range(8):
#         tim.forward(100)
#         tim.right(45)
#
#
# def draw_a_nonagon():
#     tim.pencolor("cyan")
#     for _ in range(9):
#         tim.forward(100)
#         tim.right(40)
#
#
# def draw_a_decagon():
#     tim.pencolor("navy")
#     for _ in range(10):
#         tim.forward(100)
#         tim.right(36)
#
#
# draw_a_triangle()
# draw_a_square()
# draw_a_pentagon()
# draw_a_hexagon()
# draw_a_heptagon()
# draw_a_octagon()
# draw_a_nonagon()
# draw_a_decagon()

# colours = ["red", "tan", "green", "gold", "cyan", "purple", "brown", "magenta", "aquamarine", "pale violet red"]

# def move_up():
#     tim.up()
#     tim.left(90)
#     tim.forward(5)
#     tim.right(90)
#     tim.down()
#
#
# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         corner = 360 / num_sides
#         tim.forward(100)
#         tim.right(corner)
#     move_up()
#
#
# for shape_side in range(3, 11):
#     tim.color(r.choice(colours))
#     draw_shape(shape_side)


def random_color():
    r = random.randint(0, 155)
    g = random.randint(0, 155)
    b = random.randint(0, 155)
    return r, g, b   # This is a tuple


# tim.pensize(15)
# tim.speed("fastest")
# directions = [0, 90, 180, 270]
# while True:
#     tim.pencolor(random_color())
#     tim.fd(30)
#     tim.setheading(random.choice(directions))

tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(6)
screen = Screen()
screen.exitonclick()
