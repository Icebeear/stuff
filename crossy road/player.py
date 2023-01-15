STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle, Screen

screen = Screen()

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setpos(STARTING_POSITION)
        self.setheading(90)

    def control(self):

        def up():
            self.forward(MOVE_DISTANCE)

        screen.onkeypress(up, "Up")

    def finish(self):
        if self.ycor() == FINISH_LINE_Y:
            self.setpos(STARTING_POSITION)
            return True