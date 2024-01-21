import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guess_state = []

while len(guess_state) < 50:
    answer = screen.textinput(f"{len(guess_state)}/50 state correct",
                              "What's another state's name?").title()
    if answer == "Exit":
        missing_state = [state for state in all_state if state not in guess_state] 
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break
    if answer in all_state:
        guess_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[data.state == answer]
        t.goto(int(state.x), int(state.y))
        t.write(answer) # t.write(state.state.item())



# def get_mouse_click_cor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()

