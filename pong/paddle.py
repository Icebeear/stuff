from turtle import Turtle, Screen
screen = Screen()

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 5)
        self.color("white")
        self.penup()
        self.setpos(x, y)
        self.setheading(90)

    def control(self, key1, key2):

        def up():
            self.forward(30)

        def down():
            self.backward(30)
        
        screen.onkey(up, key1)
        screen.onkey(down, key2)