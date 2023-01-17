from turtle import Turtle
STARTING_SPEED = 10
INCREASE_SPEED = 2


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.color("white")
        self.x_move = STARTING_SPEED
        self.y_move = STARTING_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        if self.x_move > 0:
            self.x_move += INCREASE_SPEED
        elif self.x_move < 0:
            self.x_move -= INCREASE_SPEED

    def miss(self):
        self.bounce_x()
        if self.x_move > 0:
            self.x_move = STARTING_SPEED
            self.y_move = STARTING_SPEED
        else:
            self.x_move = -STARTING_SPEED
            self.y_move = STARTING_SPEED
        self.home()
