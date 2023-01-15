COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

import random
from turtle import Turtle

class Car:
    def __init__(self):
        self.cars = []
        
    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setpos(320, random.randint(-200, 250))
            new_car.setheading(180)
            self.cars.append(new_car)

    def move(self, velocity):
        for car in self.cars:
            car.forward(velocity)




