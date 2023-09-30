import turtle
import pandas as pd
from state import State


df = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S States Game")
screen.tracer(0)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state = State()
states_list = df["state"].to_list()
guessed_list = []

while len(guessed_list) < 50:
    screen.update()
    answer_state = screen.textinput(title=f"{len(guessed_list)}/50 state correct", prompt="Guess state?").title()
    if answer_state == "Exit":
        break
    if answer_state in states_list:
        guessed_list.append(answer_state)
        data = df[df.state == answer_state]
        coordinates = (int(data.x), int(data.y))
        state.show_on_map(answer_state, coordinates)


screen.exitonclick()
