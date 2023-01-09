import random
from turtle import Turtle, Screen
screen = Screen()
screen.setup(500, 400)
bet = screen.textinput("Who win?", "Take color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
pos = [-70, -40, -10, 20, 50, 80]
turtles = []
for x in range(0, 6):
    tim = Turtle()
    tim.penup()
    tim.shape("turtle")
    tim.color(colors[x])
    tim.setpos(-230, pos[x])
    turtles.append(tim)

k = 0 
state = True 
while state:
    for turtle in turtles:
        turtle.forward(random.randint(2, 20))
        if turtle.xcor() >= (230):
            if bet == turtle.color()[0]:
                print(f"You win! {turtle.color()[0]} turtle win!")
            else:
                print(f"You lose! {turtle.color()[0]} turtle win!")
            state = False 
screen.exitonclick()