import turtle
import pandas
from state_name import StateName

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
x = data.x.to_list()
y = data.y.to_list()

states_text = StateName(all_states, x, y)

correct_guesses = []
score = 0
game_is_on = True
while game_is_on:
    user_type = screen.textinput(f"{score}/50 States Correct", "What's another state name?").title()

    if user_type == "Exit":
        game_is_on = False
        missing_states = []
        for state in all_states:
            if state not in correct_guesses:
                missing_states.append(state)
        data = pandas.DataFrame(missing_states)
        data.to_csv("a.csv")

    if user_type in all_states and user_type not in correct_guesses:
        score += 1
        states_text.add_state(user_type)
        correct_guesses.append(user_type)

    if score == 50:
        states_text.game_over()
        game_is_on = False




