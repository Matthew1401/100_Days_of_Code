from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.pensize(4)
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write_a_crossing_line()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Stora", 80, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Stora", 80, "normal"))

    def write_a_crossing_line(self):
        self.goto(0, -300)
        self.setheading(90)
        for _ in range(20):
            self.down()
            self.forward(20)
            self.up()
            self.forward(20)

    def game_end(self, player):
        self.clear()
        self.home()
        self.write(f"{player} player wins!", align="center", font=("Stora", 40, "normal"))

