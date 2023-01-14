from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.score = 0
        self.goto(x=0, y=245)
        self.show_scoreboard()

    def show_scoreboard(self):
        self.clear()
        self.write(f"Scoreboard: {self.score}", move=False, align='center', font=('Arial', 15, 'normal'))

    def add_a_score(self):
        self.score += 1
        self.show_scoreboard()