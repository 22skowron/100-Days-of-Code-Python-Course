
import turtle
import pandas as pd

        # PREPAIRING LIST OF STATES NAMES IN LOWERCASE
data = pd.read_csv("50_states.csv")
states_list = data.state.to_list()

        # SETTING UP CANVAS
image = "blank_states_img.gif"
canvas = turtle.Screen()
canvas.addshape(image)
turtle.shape(image)

        # JOSH THE PRINTER
josh = turtle.Turtle()
josh.penup()
josh.hideturtle()
josh.color("black")

def josh_pls_print(state_name, x_cor, y_cor):
    josh.goto(x_cor, y_cor)
    josh.write(f"{state_name}", align="center", font=('Arial', 10, 'normal'))

        # MAIN PROGRAM
guessed_states = []
score = len(guessed_states)

while score != 50:
    answer = turtle.textinput(title=f"{score}/50 Guess the State", prompt="What's another state's name?").lower()
    if answer == "exit":
        break
    for state in states_list:
        if state.lower() == answer:
            row = data[data.state == state]
            x_cor = int(row.x)
            y_cor = int(row.y)
            # x_cor = row.x
            # y_cor = row.y
            josh_pls_print(state, x_cor, y_cor)
            score += 1
            states_list.remove(state)


        # EXPORTING UNKNOWN STATES TO CSV FILE
unknown_states = states_list
dictionary = {
    "Unknown states": unknown_states
}
prepared_dict = pd.DataFrame(dictionary)
prepared_dict.to_csv("list_of_unknown_states.csv")

