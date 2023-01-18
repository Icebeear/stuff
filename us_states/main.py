from turtle import Turtle, Screen
import pandas 

data = pandas.read_csv("50_states.csv")

tim = Turtle()
tim.hideturtle()
tim.penup()

screen = Screen()
screen.setup(725, 491)
screen.bgpic("blank_states_img.gif")

num_states = 0
states = data.state.to_list()

state = True
while state:
    answer = screen.textinput(f"{num_states}/50 States Correct", "What next state?")
    if answer in states:
        num_states += 1
        state_data = data[data.state == answer]
        tim.setpos(int(state_data.x), int(state_data.y))
        tim.write(f"{answer}", True, align="center", font=("Arial", 7, "normal"))
    elif answer == "close":
        tim.bye()

screen.exitonclick()