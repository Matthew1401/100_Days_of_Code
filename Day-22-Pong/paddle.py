from turtle import Turtle
PADDLE_SPEED = 25
BORDER = 220


class Paddle(Turtle):

    def __init__(self, side):
        """Creating a paddle. Choose side == "left" or side == "right" to pick a side."""
        super().__init__()
        self.y = 0
        self.up()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        if side == "right":
            self.x = 350
            self.goto(x=self.x, y=0)
        elif side == "left":
            self.x = -350
            self.goto(x=self.x, y=0)

    def move_up(self):
        if self.y < BORDER:
            self.y += PADDLE_SPEED
            self.setposition(x=self.x, y=self.y)

    def move_down(self):
        if self.y > -BORDER:
            self.y -= PADDLE_SPEED
            self.setposition(x=self.x, y=self.y)
