from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.score = 0
        self.high_score = 0
        self.goto(x=0, y=270)
        self.show_scoreboard()

    def show_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.show_scoreboard()
    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def add_a_score(self):
        self.score += 1
        self.show_scoreboard()