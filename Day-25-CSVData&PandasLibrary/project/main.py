import turtle
import pandas
from state_name import StateName

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")
image = "blank_states_img.git"
screen.setup(width=725, height=491)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
x = data.x.to_list()
y = data.y.to_list()

states_text = StateName(states, x, y)

score = 0
game_is_on = True
while game_is_on:
    user_type = screen.textinput(f"{score}/50 States Correct", "What's another state name?").title()
    if user_type in states:
        score += 1
        states_text.add_state(user_type)

    if score == 50:
        states_text.game_over()
        game_is_on = False


screen.exitonclick()

