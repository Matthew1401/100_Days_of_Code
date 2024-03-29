from turtle import Turtle
STARTING_SPEED = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.color("white")
        self.x_move = STARTING_SPEED
        self.y_move = STARTING_SPEED
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def miss(self):
        self.bounce_x()
        self.move_speed = 0.1
        self.home()
