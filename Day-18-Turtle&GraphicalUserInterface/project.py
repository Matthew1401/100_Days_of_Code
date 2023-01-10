# Day 18 Project: Painting dots
# import colorgram
# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
# for element in colors:
#     r = element.rgb.r
#     g = element.rgb.g
#     b = element.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors) <----- This is the color_list value
import turtle
from turtle import *
import random
turtle.colormode(255)

tim = Turtle()
tim.speed("fastest")
tim.hideturtle()
screen = Screen()
color_list = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5),
              (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252),
              (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9),
              (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167),
              (77, 234, 202), (52, 234, 243), (3, 67, 40)]

x = -235
y = -235
tim.up()
tim.setposition(x, y)
tim.down()

for _ in range(10):
    for _ in range(10):
        tim.pencolor(random.choice(color_list))
        tim.dot(20)
        tim.up()
        tim.forward(50)
        tim.down()
    tim.up()
    y += 50
    tim.setposition(x, y)
    tim.down()


screen.exitonclick()
