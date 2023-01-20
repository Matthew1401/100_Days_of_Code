from turtle import Turtle

FONT = ("Stora", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.goto(-225, 250)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def increase_scoreboard(self):
        self.level += 1
        self.update_scoreboard()
