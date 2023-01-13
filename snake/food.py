from turtle import Turtle
import random

cords = []
for x in range(-280, 300, 20):
    cords.append(x)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(0.5)
        self.penup()
        self.move()
        
    def move(self):
        self.setpos(random.choice(cords), random.choice(cords))





