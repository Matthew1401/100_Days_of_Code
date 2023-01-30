from turtle import Turtle
FONT = ("Stora", 8, "normal")


class StateName(Turtle):

    def __init__(self, states, x, y):
        self.states = states
        self.x = x
        self.y = y
        self.state = Turtle()
        self.state.up()
        self.state.hideturtle()

    def add_state(self, state_name):
        index = self.states.index(state_name)
        self.state.goto(x=self.x[index], y=self.y[index])
        self.state.write(arg=state_name, align="center", font=FONT)

    def game_over(self):
        self.state.homer()
        self.state.write(arg="You win!", align="center", font=("Stora", 20, "normal"))


