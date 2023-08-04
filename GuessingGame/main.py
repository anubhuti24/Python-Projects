import turtle
import pandas
TOTAL_STATES = 50


screen = turtle.Screen()
screen.title("US-GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
new_state_data = state_data.state.to_list()
guessed_state = []
score = 0

while len(guessed_state) < 50:
    player_input = screen.textinput(title=f"{score}/{TOTAL_STATES} US States", prompt="What is the another U.S. State?")
    player_input = player_input.capitalize()
    if player_input == "Exit":
        missing_states = [all_states for all_states in new_state_data if all_states not in guessed_state]
        final_states = pandas.DataFrame(missing_states)
        print(final_states.to_csv("states-to_learn.csv"))
        break
    if player_input in new_state_data:
        score += 1
        ans = state_data[state_data["state"] == player_input]
        guessed_state.append(player_input)
        x_cor = ans["x"]
        y_cor = ans["y"]
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(int(x_cor), int(y_cor))
        turtle.pensize(1)
        new_turtle.write(f"{player_input}", align="center", font=("Arial", 8, "normal"))
    if player_input not in new_state_data:
        turtle.write("Try attempting!!", align="left", font=("Arial", 9, "normal"))
        turtle.clear()
        continue

#

