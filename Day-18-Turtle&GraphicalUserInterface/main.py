from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")


def write_a_dashed_line():
    for _ in range(15):
        tim.forward(10)
        tim.up()
        tim.forward(10)
        tim.down()


def draw_a_triangle():
    tim.pencolor("red")
    for _ in range(3):
        tim.forward(100)
        tim.right(120)


def draw_a_square():
    tim.pencolor("blue")
    for _ in range(4):
        tim.forward(100)
        tim.right(90)


def draw_a_pentagon():
    tim.pencolor("purple")
    for _ in range(5):
        tim.forward(100)
        tim.right(72)


def draw_a_hexagon():
    tim.pencolor("green")
    for _ in range(6):
        tim.forward(100)
        tim.right(60)


def draw_a_heptagon():
    tim.pencolor("brown")
    for _ in range(7):
        tim.forward(100)
        tim.right(51.43)


def draw_a_octagon():
    tim.pencolor("magenta")
    for _ in range(8):
        tim.forward(100)
        tim.right(45)


def draw_a_nonagon():
    tim.pencolor("cyan")
    for _ in range(9):
        tim.forward(100)
        tim.right(40)


def draw_a_decagon():
    tim.pencolor("navy")
    for _ in range(10):
        tim.forward(100)
        tim.right(36)


draw_a_triangle()
draw_a_square()
draw_a_pentagon()
draw_a_hexagon()
draw_a_heptagon()
draw_a_octagon()
draw_a_nonagon()
draw_a_decagon()


screen = Screen()
screen.exitonclick()
