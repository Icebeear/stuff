from turtle import Turtle 
import random 
angles = (45, 135, 225, 315)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.angle = random.choice(angles)
        self.shape("circle")
        self.color("white")
        self.setheading(self.angle)
        self.penup()

    def move(self):
        self.forward(5)

    def bounce(self, paddle):
        if (self.ycor() < -280 or self.ycor() > 280) or ((self.xcor() > 330 or self.xcor() < -330) and (self.distance(paddle) < 50)):
            self.angle -= 45
            self.setheading(self.angle)
            
    def home(self):
        self.setpos(0, 0)
        self.angle -= 180
        self.setheading(self.angle)