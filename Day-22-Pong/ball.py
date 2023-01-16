from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.color("white")
        self.y = 0
        self.x = 0

    def move(self):
        self.y += 6
        self.x += 8
        self.goto(x=self.x, y=self.y)
