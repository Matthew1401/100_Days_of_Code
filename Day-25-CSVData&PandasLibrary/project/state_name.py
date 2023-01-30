from turtle import Turtle
FONT = ("Stora", 8, "normal")


class StateName(Turtle):

    def __init__(self, all_states, x, y):
        self.all_states = all_states
        self.x = x
        self.y = y
        self.t = Turtle()
        self.t.up()
        self.t.hideturtle()

    def add_state(self, state_name):
        index = self.all_states.index(state_name)
        self.t.goto(x=self.x[index], y=self.y[index])
        self.t.write(arg=state_name, align="center", font=FONT)

    def game_over(self):
        self.t.home()
        self.t.write(arg="You win!", align="center", font=("Stora", 20, "normal"))


