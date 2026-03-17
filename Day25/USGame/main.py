import turtle
import pandas as pd

writer = turtle.Turtle()
writer.hideturtle()

screen = turtle.Screen()
screen.title("U.S States Game")

img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

df = pd.read_csv("50_states.csv")
state_list = df["state"].to_list()
guessed_state = []

print(state_list)
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        state_to_learn = [state for state in state_list if state not in guessed_state]
        file = pd.DataFrame(state_to_learn)
        file.to_csv("states_to_learn.csv")
        break
    if (df["state"] == answer_state).any():
        x_cor = df[df["state"] == answer_state]["x"].item()
        y_cor = df[df["state"] == answer_state]["y"].item()
        guessed_state.append(answer_state)
        writer.penup()
        writer.goto(x_cor,y_cor)
        writer.write(f"{answer_state}", move=False, align="center", font=('Arial', 8, 'normal'))
    
#states to be learnt
# for state in state_list:
#     if state not in guessed_state:
#         state_to_learn.append(state)
